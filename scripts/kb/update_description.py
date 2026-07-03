"""Description backfill (tasks 4.12-4.13).

Implements design D6: when a query hits a doc whose description is still "无描述",
the agent fetches the doc body, generates a description, and calls this function
to backfill it. Backfilling MUST recompute the embedding from the new description
(per D2: description backfill switches the embedding source from title to desc).

B14/T015: content_hash 公式含 context 后，update_description 必须用 doc 当前
context 重算 hash（否则 doc 已有非空 context 时 hash 会算错，导致后续 reindex
误判需要重新嵌入）。不委托给 update_content——后者要求 context 非空（agent
回填场景），而 update_description 是 legacy 路径（doc 可能尚无 context）。
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .query import _check_model_compatibility
from .sidebar_parser import NO_DESCRIPTION, _make_content_hash


def update_description(
    doc_id: str,
    description: str,
    indexer: Any,
    embedder: Any,
) -> dict[str, Any]:
    """Backfill `description` for doc `doc_id` and recompute its vector.

    Raises KeyError if the doc isn't in the index (Rule 12: fail loud).
    Returns the updated doc dict.

    B13: MUST recompute content_hash after changing description — B4 added
    description to the content_hash formula, so a stale hash here would leave
    the doc in an inconsistent state.

    B14/T015: content_hash 公式加入 context 后，必须用 doc 当前 context 重算
    hash（不传 context 会默认 ""，对已有非空 context 的 doc 会算错 hash）。
    不委托给 update_content（后者要求 context 非空），保留独立的 legacy 写入
    路径——update_description 只更新 description，不动 context。
    """
    doc = indexer.get(doc_id)
    if doc is None:
        raise KeyError(f"update_description: doc_id not in index: {doc_id}")
    _check_model_compatibility(indexer, embedder)
    if not description or description == NO_DESCRIPTION:
        raise ValueError("update_description: description must be a real, non-empty string")

    doc["description"] = description
    doc["updated_at"] = datetime.now(timezone.utc).isoformat()
    # B14/T015: 用 doc 当前 context 重算 hash（可能为 ""，对应 legacy docs）
    doc["content_hash"] = _make_content_hash(
        doc["title"], doc["url"], doc["doc_type"],
        doc["description"], doc.get("links", []),
        context=doc.get("context", ""),
    )

    # indexer.upsert recomputes the vector from `description` (since it now !=
    # "无描述"), overwriting both the vector and the payload's description +
    # updated_at + content_hash fields in one shot.
    indexer.upsert(doc, embedder)
    return doc
