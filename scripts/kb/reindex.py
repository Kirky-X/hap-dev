"""Re-index embeddings (tasks 4.14-4.15).

reindex(indexer, embedder, force=False) -> int

Implements design D9 (simplified per spec):

* force=True  -> re-embed EVERY stored doc (e.g. embed_model changed).
* force=False -> "content_hash 比对": for each stored doc, recompute content_hash
  from its current ``title + url + doc_type`` and compare to the stored
  ``content_hash`` field. A mismatch means the doc was modified after indexing
  (title/url/doc_type changed without refreshing content_hash) -> re-embed that
  doc AND fix its content_hash field. Unmodified docs are skipped.

Returns the number of docs that were re-embedded.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any

from .sidebar_parser import NO_DESCRIPTION


def _content_hash(title: str, url: str, doc_type: str) -> str:
    return hashlib.sha1((title + url + doc_type).encode("utf-8")).hexdigest()


def _embed_text(doc: dict[str, Any]) -> str:
    desc = doc.get("description", NO_DESCRIPTION)
    if desc and desc != NO_DESCRIPTION:
        return desc
    return doc["title"]


def reindex(indexer: Any, embedder: Any, force: bool = False) -> int:
    stored = indexer.list_all()
    if not stored:
        return 0

    targets: list[dict[str, Any]] = []
    if force:
        targets = list(stored)
    else:
        for doc in stored:
            recomputed = _content_hash(doc["title"], doc["url"], doc["doc_type"])
            if doc["content_hash"] != recomputed:
                # fix the stored content_hash before re-embedding
                doc["content_hash"] = recomputed
                doc["updated_at"] = datetime.now(timezone.utc).isoformat()
                targets.append(doc)

    count = 0
    for doc in targets:
        # indexer.upsert recomputes the vector from description (if backfilled)
        # or title, and overwrites payload + vector in one shot.
        indexer.upsert(doc, embedder)
        count += 1
    return count
