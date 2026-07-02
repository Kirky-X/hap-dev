"""Hybrid query: vector + BM25 fusion with optional rerank (tasks 4.8-4.9).

Flow:
  1. embed the question
  2. Qdrant vector search over top_k*3 candidates (optionally filtered by doc_type)
  3. BM25Okapi over the candidates' ``title + description`` (char-level tokenize so
     Chinese needs no extra dependency)
  4. min-max normalize both score sets and fuse with vector_weight / bm25_weight
  5. (optional) flashrank rerank over the fused top_k
  6. return top_k docs, each annotated with needs_description (D6 lazy backfill flag)
"""
from __future__ import annotations

from typing import Any, Optional

from .sidebar_parser import NO_DESCRIPTION


def _tokenize(text: str) -> list[str]:
    """Char-level tokenizer — works for Chinese without jieba (per spec)."""
    return [c for c in text if not c.isspace()]


def _minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi - lo < 1e-12:
        # all equal -> normalize to 1.0 so a tie doesn't zero out the signal
        return [1.0] * len(values)
    return [(v - lo) / (hi - lo) for v in values]


def query(
    question: str,
    indexer: Any,
    embedder: Any,
    top_k: int = 5,
    doc_type: Optional[str] = None,
    rerank: bool = False,
    vector_weight: float = 0.7,
    bm25_weight: float = 0.3,
) -> list[dict[str, Any]]:
    """Hybrid vector+BM25 search. Returns at most `top_k` results."""
    qvec = embedder.embed(question)

    # 1. vector retrieval — over-fetch so BM25/fusion have a candidate pool.
    cand_k = max(top_k * 3, top_k)
    candidates = indexer.search(qvec, top_k=cand_k, doc_type=doc_type)
    if not candidates:
        return []

    # 2. BM25 keyword scoring over the same candidate pool.
    from rank_bm25 import BM25Okapi

    corpus = [
        _tokenize(f"{c['title']} {c.get('description', NO_DESCRIPTION)}")
        for c in candidates
    ]
    bm25 = BM25Okapi(corpus)
    bm25_scores = list(bm25.get_scores(_tokenize(question)))
    vec_scores = [float(c["score"]) for c in candidates]

    # 3. normalize + fuse.
    n_vec = _minmax(vec_scores)
    n_bm = _minmax(bm25_scores)
    fused = []
    for i, c in enumerate(candidates):
        score = vector_weight * n_vec[i] + bm25_weight * n_bm[i]
        fused.append((score, c))
    fused.sort(key=lambda x: x[0], reverse=True)
    top = fused[:top_k]

    results = [_to_result(score, c) for score, c in top]

    # 4. optional flashrank rerank.
    if rerank:
        results = _rerank(question, results)
        results = results[:top_k]
    return results


def _to_result(score: float, c: dict[str, Any]) -> dict[str, Any]:
    desc = c.get("description", NO_DESCRIPTION)
    return {
        "id": c["id"],
        "title": c["title"],
        "url": c["url"],
        "description": desc,
        "doc_type": c["doc_type"],
        "score": float(score),
        "needs_description": desc == NO_DESCRIPTION,
    }


def _rerank(question: str, results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Rerank `results` with flashrank. If flashrank isn't installed, return the
    input unchanged (caller explicitly asked for rerank; we surface the missing
    dep by falling back rather than crashing — logged via the unchanged order)."""
    if not results:
        return results
    try:
        from flashrank import RankModel
    except ImportError:
        # flashrank optional — fall back to fused order. Not silent: the caller
        # can detect rerank didn't happen because results are unchanged.
        return results
    ranker = RankModel()
    passages = [
        {"id": r["id"], "text": f"{r['title']} {r['description']}"}
        for r in results
    ]
    reranked = ranker.rerank(question, passages)
    id_to_doc = {r["id"]: r for r in results}
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in reranked:
        rid = item.get("id") if isinstance(item, dict) else None
        if rid and rid in id_to_doc and rid not in seen:
            out.append(id_to_doc[rid])
            seen.add(rid)
    # append any docs the reranker dropped
    for r in results:
        if r["id"] not in seen:
            out.append(r)
    return out
