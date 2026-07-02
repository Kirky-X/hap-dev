"""B2: bidirectional auto-linking via vector cosine similarity.

auto_link(indexer, threshold=0.9, max_per_doc=10) -> dict

First-Principles fact F3: links semantics = "document relatedness". Two
kinds of links coexist:

  - explicit (from "相关推荐" blocks) — handled by links.py
  - implicit (from vector similarity) — handled by this module

User requirement: docs whose cosine similarity > 0.9 must be auto-linked
bidirectionally. The current DB ships with all 964 docs having links=[]
because links.py only extracts from "相关推荐" sections, which most docs lack.

Design:

  * for each stored doc, search its top-K nearest neighbours (K = max_per_doc
    + slack to allow self-filtering)
  * keep neighbours whose score > threshold (Qdrant cosine distance: higher
    score = more similar)
  * skip self-links (a doc must not link to itself)
  * bidirectional write: A.links += B.id AND B.links += A.id, but ONLY if the
    link doesn't already exist (idempotent — running twice yields 0 new pairs)
  * existing explicit links (from links.py) are preserved — auto_link appends,
    never overwrites
  * respect max_per_doc per side (each doc's link list is capped; if full, no
    new auto-link is added in that direction)

Returns {"pairs_linked": N, "docs_scanned": M}.

NB: this module reads each doc's stored vector via list_all(with_vectors=True)
and reuses it as the query — no embedder is needed, and no re-embedding
happens. set_payload updates only `links` + `updated_at`, leaving the vector
untouched (consistent with links.py).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .sidebar_parser import _make_content_hash, NO_DESCRIPTION


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _add_link_bidirectional(
    indexer: Any,
    a_id: str,
    b_id: str,
    a_doc: dict[str, Any],
    b_doc: dict[str, Any],
    max_per_doc: int,
    now: str,
) -> bool:
    """Add a↔b bidirectional link if not present and both sides have capacity.

    Mutates a_doc["links"] and b_doc["links"] in place (caller then persists
    via set_payload). Returns True ONLY if a complete bidirectional pair was
    added (both directions). Returns False if:
      - self-link
      - already linked both ways
      - capacity exceeded on EITHER side (we refuse to add a one-way link;
        bidirectionality is the contract — Rule 3 禁止简化实现)
    """
    if a_id == b_id:
        return False
    a_links: list[str] = a_doc["links"]
    b_links: list[str] = b_doc["links"]
    already = b_id in a_links and a_id in b_links
    if already:
        return False
    # Both sides must have capacity — bidirectional is the contract.
    if len(a_links) >= max_per_doc:
        return False
    if len(b_links) >= max_per_doc:
        return False
    if b_id not in a_links:
        a_links.append(b_id)
    if a_id not in b_links:
        b_links.append(a_id)
    return True


def _persist_links(indexer: Any, doc_id: str, doc: dict[str, Any], now: str) -> None:
    """Write the doc's links + updated_at back to the DB via set_payload.

    Also refreshes content_hash so a future reindex(force=False) sees the doc
    as consistent (links are part of content_hash per B4).
    """
    new_hash = _make_content_hash(
        doc["title"], doc["url"], doc["doc_type"],
        doc.get("description", NO_DESCRIPTION),
        doc["links"],
    )
    indexer.set_payload(doc_id, {
        "links": doc["links"],
        "updated_at": now,
        "content_hash": new_hash,
    })
    # Keep the in-memory doc dict in sync with what we just persisted (callers
    # may re-use it for subsequent pairs in the same batch).
    doc["updated_at"] = now
    doc["content_hash"] = new_hash


def auto_link(
    indexer: Any,
    threshold: float = 0.9,
    max_per_doc: int = 10,
    slack: int = 5,
) -> dict[str, Any]:
    """Auto-link docs whose cosine similarity > threshold.

    Args:
        indexer: QdrantIndexer (or compatible) with `search`, `get`,
            `set_payload`, `list_all` methods.
        threshold: cosine similarity above which two docs are linked. Default
            0.9 (per user requirement).
        max_per_doc: cap on each doc's link list. Default 10.
        slack: extra candidates to fetch beyond max_per_doc to allow
            self-filtering and threshold filtering. Default 5.

    Returns:
        {"pairs_linked": int, "docs_scanned": int}
    """
    docs = indexer.list_all(with_vectors=True)
    if not docs:
        return {"pairs_linked": 0, "docs_scanned": 0}

    # Build an id → doc dict so we can mutate links in memory and persist at
    # the end. We carry the doc dicts around so repeated lookups are cheap.
    by_id: dict[str, dict[str, Any]] = {d["id"]: d for d in docs}
    now = _now_iso()
    pairs_linked = 0
    dirty: set[str] = set()  # doc ids whose links changed

    # Search top_k = max_per_doc + slack + 1 (the +1 covers self if present).
    top_k = max_per_doc + slack + 1

    for doc in docs:
        vec = doc.get("embedding")
        if not vec:
            continue  # vector missing — cannot search (defensive; should not happen)
        candidates = indexer.search(vec, top_k=top_k)
        for c in candidates:
            if c["id"] == doc["id"]:
                continue  # no self-link
            if float(c.get("score", 0.0)) <= threshold:
                continue  # below threshold
            target = by_id.get(c["id"])
            if target is None:
                continue  # target not in our snapshot (shouldn't happen)
            added = _add_link_bidirectional(
                indexer, doc["id"], c["id"], doc, target, max_per_doc, now,
            )
            if added:
                pairs_linked += 1
                dirty.add(doc["id"])
                dirty.add(c["id"])

    # Persist dirty docs.
    for did in dirty:
        _persist_links(indexer, did, by_id[did], now)

    return {"pairs_linked": pairs_linked, "docs_scanned": len(docs)}
