"""B17: 一次性更新 doc 的 context + description + 向量 + hash。

update_content(doc_id, context, description, indexer, embedder) 是 B14 的核心
写入入口。与 update_description（只更新 description）不同，update_content 同时
更新 context（网页原始内容），并原子地重算 content_hash 和 embedding。

原子性保证：通过 indexer.upsert 一次性写入 payload + 向量，避免中间状态。
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .sidebar_parser import NO_DESCRIPTION, _make_content_hash


def update_content(
    doc_id: str,
    context: str,
    description: str,
    indexer: Any,
    embedder: Any,
) -> dict[str, Any]:
    """原子地更新 doc 的 context + description + 向量 + hash + updated_at。

    Args:
        doc_id: 目标 doc id。
        context: doc 的网页原始内容（markdown）。非空，空字符串 raise。
        description: doc 的人工/生成描述。非空、非 NO_DESCRIPTION。
        indexer: QdrantIndexer（或兼容）实例。
        embedder: 嵌入器（必传，None 由 indexer.upsert 自身 raise）。

    Returns:
        更新后的 doc dict。

    Raises:
        KeyError: doc_id 不存在于索引（fail-loud）。
        ValueError: context 或 description 为空 / 占位符。
    """
    doc = indexer.get(doc_id)
    if doc is None:
        raise KeyError(f"update_content: doc_id not in index: {doc_id}")
    if not context:
        raise ValueError("update_content: context 不能为空")
    if not description or description == NO_DESCRIPTION:
        raise ValueError("update_content: description 必须是真实非空字符串")

    # 更新 4 个字段，第 5 个（embedding）由 indexer.upsert 内部重算
    doc["context"] = context
    doc["description"] = description
    doc["updated_at"] = datetime.now(timezone.utc).isoformat()
    doc["content_hash"] = _make_content_hash(
        doc["title"], doc["url"], doc["doc_type"],
        description, doc.get("links", []),
        context=context,
    )

    # upsert 重算向量（从 description，因 description != NO_DESCRIPTION）并盖章
    # embed_model；payload（含 context/description/content_hash/updated_at）
    # 也一并写入。这是原子写入入口。
    indexer.upsert(doc, embedder)
    return doc
