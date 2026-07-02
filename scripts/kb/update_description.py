"""Description backfill (tasks 4.12-4.13).

Implements design D6: when a query hits a doc whose description is still "无描述",
the agent fetches the doc body, generates a description, and calls this function
to backfill it. Backfilling MUST recompute the embedding from the new description
(per D2: description backfill switches the embedding source from title to desc).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .sidebar_parser import NO_DESCRIPTION


def update_description(
    doc_id: str,
    description: str,
    indexer: Any,
    embedder: Any,
) -> dict[str, Any]:
    """Backfill `description` for doc `doc_id` and recompute its vector.

    Raises KeyError if the doc isn't in the index (Rule 12: fail loud).
    Returns the updated doc dict.
    """
    doc = indexer.get(doc_id)
    if doc is None:
        raise KeyError(f"update_description: doc_id not in index: {doc_id}")
    if not description or description == NO_DESCRIPTION:
        raise ValueError("update_description: description must be a real, non-empty string")

    doc["description"] = description
    doc["updated_at"] = datetime.now(timezone.utc).isoformat()

    # indexer.upsert recomputes the vector from `description` (since it now !=
    # "无描述"), overwriting both the vector and the payload's description +
    # updated_at fields in one shot.
    indexer.upsert(doc, embedder)
    return doc
