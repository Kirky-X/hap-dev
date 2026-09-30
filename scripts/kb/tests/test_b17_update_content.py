"""B17: update_content.py 一次性更新 context + description + 向量 + hash (Red phase).

update_content(doc_id, context, description, indexer, embedder) 是 B14 的核心
写入入口：原子地更新 doc 的 context/description/content_hash/embedding/
updated_at 五个字段。比 update_description 更全面——后者只更新 description，
而 update_content 同时更新 context（网页原始内容）。

fail-loud：空 context/空 description/doc 不存在均 raise（不静默吞掉）。
"""
from __future__ import annotations

import pytest

from scripts.kb.sidebar_parser import _make_content_hash
from scripts.kb.tests.conftest import make_doc
from scripts.kb.update_content import update_content


def test_update_content_updates_all_fields(indexer, fake_embedder):
    """B17-1: 调用后 doc 的 5 个字段全部更新到新值。"""
    doc = make_doc(url="https://example.com/test-update-all")
    indexer.upsert(doc, fake_embedder)
    doc_id = doc["id"]

    new_context = "# 标题\n\n这是抓取到的网页内容。"
    new_description = "ArkTS 文本常见问题解答"
    old_updated_at = doc["updated_at"]
    old_embedding = indexer.get(doc_id).get("embedding")

    result = update_content(doc_id, new_context, new_description, indexer, fake_embedder)

    # 5 个字段全部更新
    assert result["context"] == new_context
    assert result["description"] == new_description
    assert result["updated_at"] != old_updated_at
    # content_hash 反映新 context
    expected_hash = _make_content_hash(
        doc["title"], doc["url"], doc["doc_type"],
        new_description, doc.get("links", []), context=new_context,
    )
    assert result["content_hash"] == expected_hash

    # DB 中持久化的 doc 也已更新
    stored = indexer.get(doc_id)
    assert stored["context"] == new_context
    assert stored["description"] == new_description
    assert stored["content_hash"] == expected_hash

    # embedding 也应重新计算（向量随 description 变化）
    new_embedding = stored.get("embedding")
    assert new_embedding is not None
    assert new_embedding != old_embedding


def test_update_content_empty_context_raises(indexer, fake_embedder):
    """B17-2: 空 context raise ValueError（fail-loud）。"""
    doc = make_doc(url="https://example.com/test-empty-ctx")
    indexer.upsert(doc, fake_embedder)
    with pytest.raises(ValueError, match="context"):
        update_content(doc["id"], "", "valid description", indexer, fake_embedder)


def test_update_content_empty_description_raises(indexer, fake_embedder):
    """B17-3: 空 description raise ValueError（fail-loud）。"""
    doc = make_doc(url="https://example.com/test-empty-desc")
    indexer.upsert(doc, fake_embedder)
    with pytest.raises(ValueError, match="description"):
        update_content(doc["id"], "valid context", "", indexer, fake_embedder)


def test_update_content_no_description_marker_raises(indexer, fake_embedder):
    """B17-4: description 为 NO_DESCRIPTION 占位符时也 raise。"""
    from scripts.kb.sidebar_parser import NO_DESCRIPTION
    doc = make_doc(url="https://example.com/test-no-desc-marker")
    indexer.upsert(doc, fake_embedder)
    with pytest.raises(ValueError, match="description"):
        update_content(
            doc["id"], "valid context", NO_DESCRIPTION, indexer, fake_embedder,
        )


def test_update_content_doc_not_found_raises(indexer, fake_embedder):
    """B17-5: doc 不存在 raise KeyError（fail-loud）。"""
    with pytest.raises(KeyError, match="doc_id"):
        update_content(
            "nonexistent-id-12345",
            "some context",
            "some description",
            indexer,
            fake_embedder,
        )


def test_update_content_reflects_context_in_hash(indexer, fake_embedder):
    """B17-6: 相同 description 但不同 context 时，content_hash 必须不同。

    这是 B14 的核心目的——context 加入 hash 公式，让 reindex 能检测网页变化。
    """
    doc = make_doc(url="https://example.com/test-hash-context")
    indexer.upsert(doc, fake_embedder)
    doc_id = doc["id"]

    update_content(doc_id, "context-A", "same description", indexer, fake_embedder)
    hash_a = indexer.get(doc_id)["content_hash"]

    update_content(doc_id, "context-B", "same description", indexer, fake_embedder)
    hash_b = indexer.get(doc_id)["content_hash"]

    assert hash_a != hash_b, (
        "相同 description 但不同 context 时 content_hash 必须不同，"
        "否则 reindex 无法检测网页内容变化"
    )


def test_update_content_preserves_other_fields(indexer, fake_embedder):
    """B17-7: 更新不应破坏 title/url/doc_type/links/id 等其他字段。"""
    doc = make_doc(
        url="https://example.com/test-preserve",
        title="原标题",
        doc_type="app-docs",
        links=["some-link-id"],
    )
    indexer.upsert(doc, fake_embedder)
    doc_id = doc["id"]

    result = update_content(
        doc_id, "new context", "new description", indexer, fake_embedder,
    )

    assert result["id"] == doc_id
    assert result["title"] == "原标题"
    assert result["url"] == "https://example.com/test-preserve"
    assert result["doc_type"] == "app-docs"
    assert result["links"] == ["some-link-id"]
    assert result["embed_model"] == doc["embed_model"]


def test_update_content_stamps_embed_model(indexer, fake_embedder):
    """B17-8: 调用后 embed_model 被 indexer.upsert 盖章（与 update_description 一致）。"""
    doc = make_doc(url="https://example.com/test-stamp", embed_model="")
    indexer.upsert(doc, fake_embedder)
    doc_id = doc["id"]

    update_content(doc_id, "ctx", "desc", indexer, fake_embedder)

    stored = indexer.get(doc_id)
    assert stored["embed_model"] == fake_embedder.model_name
