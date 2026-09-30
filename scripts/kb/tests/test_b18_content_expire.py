"""B18: 过期检测 + hash 对比 + touch_updated_at (Red phase).

is_content_expired(doc, expire_days): 检查 doc.updated_at 是否距今 > expire_days。
should_refresh_content(doc, new_context): 对比 new_context sha1 与 doc.context sha1。
touch_updated_at(doc_id, indexer): 只更新 updated_at，不改 context/向量/hash。
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from scripts.kb.content_fetcher import (
    is_content_expired,
    should_refresh_content,
    touch_updated_at,
)
from scripts.kb.tests.conftest import make_doc


def _doc_with_updated_at(days_ago: int) -> dict:
    """构造一个 updated_at 为 N 天前的 doc。"""
    doc = make_doc(url=f"https://example.com/test-expire-{days_ago}")
    doc["updated_at"] = (
        datetime.now(timezone.utc) - timedelta(days=days_ago)
    ).isoformat()
    return doc


def test_is_content_expired_31_days_ago_true():
    """B18-1: updated_at 31 天前 → 过期（expire_days=30）。"""
    doc = _doc_with_updated_at(31)
    assert is_content_expired(doc, expire_days=30) is True


def test_is_content_expired_29_days_ago_false():
    """B18-2: updated_at 29 天前 → 未过期（expire_days=30）。"""
    doc = _doc_with_updated_at(29)
    assert is_content_expired(doc, expire_days=30) is False


def test_is_content_expired_exactly_30_days_ago_false():
    """B18-3: updated_at 恰好 30 天前 → 未过期（边界：> 才过期，不含 =）。"""
    doc = _doc_with_updated_at(30)
    assert is_content_expired(doc, expire_days=30) is False


def test_is_content_expired_default_expire_days():
    """B18-4: 默认 expire_days=30。"""
    doc = _doc_with_updated_at(31)
    assert is_content_expired(doc) is True
    doc2 = _doc_with_updated_at(29)
    assert is_content_expired(doc2) is False


def test_is_content_expired_invalid_updated_at_raises():
    """B18-5: updated_at 无法解析时 raise ValueError（fail-loud）。"""
    doc = make_doc(url="https://example.com/test-bad-date")
    doc["updated_at"] = "not-a-date"
    with pytest.raises(ValueError, match="updated_at|时间"):
        is_content_expired(doc, expire_days=30)


def test_should_refresh_content_different_context_true():
    """B18-6: new_context sha1 != doc.context sha1 → 需要刷新。"""
    doc = make_doc(url="https://example.com/test-refresh-diff")
    doc["context"] = "old content"
    assert should_refresh_content(doc, "new content") is True


def test_should_refresh_content_same_context_false():
    """B18-7: new_context sha1 == doc.context sha1 → 不需要刷新。"""
    doc = make_doc(url="https://example.com/test-refresh-same")
    doc["context"] = "same content"
    assert should_refresh_content(doc, "same content") is False


def test_should_refresh_content_both_empty_false():
    """B18-8: doc 无 context 且 new_context 也空 → 不需要刷新（都是空）。"""
    doc = make_doc(url="https://example.com/test-refresh-empty")
    doc["context"] = ""
    assert should_refresh_content(doc, "") is False


def test_should_refresh_content_empty_doc_non_empty_new_true():
    """B18-9: doc 无 context，new_context 非空 → 需要刷新。"""
    doc = make_doc(url="https://example.com/test-refresh-new")
    doc["context"] = ""
    assert should_refresh_content(doc, "fetched content") is True


def test_touch_updated_at_only_updates_timestamp(indexer, fake_embedder):
    """B18-10: touch_updated_at 只改 updated_at，不改 context/向量/hash/description。"""
    doc = make_doc(url="https://example.com/test-touch")
    indexer.upsert(doc, fake_embedder)
    doc_id = doc["id"]

    before = indexer.get(doc_id)
    old_updated_at = before["updated_at"]
    old_context = before.get("context", "")
    old_description = before["description"]
    old_content_hash = before["content_hash"]
    old_embedding = before.get("embedding")

    # 确保时间戳会变（等待微小时间）
    import time
    time.sleep(0.01)

    touch_updated_at(doc_id, indexer)

    after = indexer.get(doc_id)
    assert after["updated_at"] != old_updated_at, "updated_at 必须更新"
    assert after.get("context", "") == old_context, "context 不应变"
    assert after["description"] == old_description, "description 不应变"
    assert after["content_hash"] == old_content_hash, "content_hash 不应变"
    assert after.get("embedding") == old_embedding, "向量不应变"


def test_touch_updated_at_doc_not_found_raises(indexer):
    """B18-11: doc 不存在 raise KeyError（fail-loud）。"""
    with pytest.raises(KeyError, match="doc_id"):
        touch_updated_at("nonexistent-id-xyz", indexer)
