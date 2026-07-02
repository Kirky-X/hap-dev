"""Re-index embeddings (tasks 4.14-4.15).

reindex(indexer, embedder, force=False) -> int

Implements design D9 (simplified per spec), with B6 auto-force upgrade:

* force=True  -> re-embed EVERY stored doc.
* force=False -> "content_hash 比对" + "embed_model 比对":
    - if the embedder's model_name differs from any stored doc's embed_model
      -> auto-upgrade to force=True (B6: model changed, all vectors stale)
    - else for each stored doc, recompute content_hash from its current
      ``title + url + doc_type + description + links`` and compare to the stored
      ``content_hash``. A mismatch means the doc was modified after indexing
      -> re-embed that doc AND fix its content_hash field. Unmodified docs are
      skipped.

Returns the number of docs that were re-embedded.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .sidebar_parser import NO_DESCRIPTION, _make_content_hash


def _content_hash(
    title: str,
    url: str,
    doc_type: str,
    description: str = NO_DESCRIPTION,
    links: list[str] | None = None,
) -> str:
    """B4: delegated to sidebar_parser._make_content_hash (single source of truth).

    Two call sites previously computed content_hash independently — that drift
    was itself a bug (reindex would always detect a "change" because its hash
    algorithm differed from the one used at build time).
    """
    return _make_content_hash(title, url, doc_type, description, links)


def _embed_text(doc: dict[str, Any]) -> str:
    desc = doc.get("description", NO_DESCRIPTION)
    if desc and desc != NO_DESCRIPTION:
        return desc
    return doc["title"]


def _model_changed(stored: list[dict[str, Any]], embedder: Any) -> bool:
    """B6: True if embedder.model_name differs from any stored doc's embed_model.

    Empty embed_model in stored docs is treated as "unknown" — we DO NOT
    trigger a reindex for legacy DBs (the migrate-embed-model script handles
    that explicitly). Once a doc has a real embed_model value, a mismatch
    with the current embedder means the vectors are stale.
    """
    cur = embedder.model_name
    for doc in stored:
        stored_model = doc.get("embed_model", "")
        if stored_model and stored_model != cur:
            return True
    return False


def reindex(indexer: Any, embedder: Any, force: bool = False) -> int:
    stored = indexer.list_all()
    if not stored:
        return 0

    # B6: model change auto-upgrade. If the user changed embed_model in
    # config.json but forgot to pass --force, reindex would otherwise return 0
    # (content_hash unchanged) and silently leave every vector stale.
    if not force and _model_changed(stored, embedder):
        force = True

    targets: list[dict[str, Any]] = []
    if force:
        targets = list(stored)
    else:
        for doc in stored:
            recomputed = _content_hash(
                doc["title"], doc["url"], doc["doc_type"],
                doc.get("description", NO_DESCRIPTION),
                doc.get("links", []),
            )
            if doc["content_hash"] != recomputed:
                # fix the stored content_hash before re-embedding
                doc["content_hash"] = recomputed
                doc["updated_at"] = datetime.now(timezone.utc).isoformat()
                targets.append(doc)

    count = 0
    for doc in targets:
        # indexer.upsert recomputes the vector from description (if backfilled)
        # or title, and overwrites payload + vector in one shot. It also stamps
        # embedder.model_name onto the doc (B1).
        indexer.upsert(doc, embedder)
        count += 1
    return count
