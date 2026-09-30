"""B29: 写入路径 upsert 前必须校验 embed_model 兼容性（Red phase）。

First-Principles fact F1 + B5: 跨模型向量空间不可混用。query.py 已在
查询路径校验 _check_model_compatibility（B5），但三个写入入口
（update_links / update_content / update_description）未校验——用 model-b
的 embedder 更新 model-a 的 DB 会用 model-b 的向量覆盖 model-a 的向量，
污染向量空间（与 mixed DB 同等危害，只是渐进式而非一次性）。

修复目标：三个写入入口在 upsert 前调用 _check_model_compatibility，
模型不匹配时 raise ValueError（消息含 "embed_model mismatch"）；
legacy DB（embed_model=""）不 raise（向后兼容，待 migrate 脚本回填）。
"""
from __future__ import annotations

import pytest

from scripts.kb.links import update_links
from scripts.kb.update_content import update_content
from scripts.kb.update_description import update_description
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def _build_doc_with_model(indexer, embedder, url="https://example.com/src"):
    """用 embedder.upsert 建 doc，DB embed_model = embedder.model_name。"""
    doc = make_doc(url=url, title="Source Doc")
    indexer.upsert(doc, embedder)
    return doc["id"]


def test_update_links_raises_on_model_mismatch(indexer, fake_embedder, fake_embedder_b):
    """B29-1: DB 是 model-A，用 model-B 调 update_links → raise ValueError。"""
    doc_id = _build_doc_with_model(indexer, fake_embedder)
    with pytest.raises(ValueError, match="embed_model mismatch"):
        update_links(doc_id, indexer, fake_embedder_b)


def test_update_content_raises_on_model_mismatch(indexer, fake_embedder, fake_embedder_b):
    """B29-2: DB 是 model-A，用 model-B 调 update_content → raise ValueError。"""
    doc_id = _build_doc_with_model(indexer, fake_embedder)
    with pytest.raises(ValueError, match="embed_model mismatch"):
        update_content(
            doc_id, context="new ctx", description="new desc",
            indexer=indexer, embedder=fake_embedder_b,
        )


def test_update_description_raises_on_model_mismatch(indexer, fake_embedder, fake_embedder_b):
    """B29-3: DB 是 model-A，用 model-B 调 update_description → raise ValueError。"""
    doc_id = _build_doc_with_model(indexer, fake_embedder)
    with pytest.raises(ValueError, match="embed_model mismatch"):
        update_description(
            doc_id, description="new desc",
            indexer=indexer, embedder=fake_embedder_b,
        )


def test_update_description_legacy_db_no_raise(indexer, fake_embedder, fake_embedder_b):
    """B29-4: legacy DB（embed_model=""）→ 不 raise，允许任何 embedder 写入。

    向后兼容：964 个 pre-existing docs 无 embed_model，待 migrate 脚本回填。
    期间写入路径不能 break（否则无法 backfill description）。
    用 put 建 doc（不盖章），embed_model 保持 doc 原值 ""。
    """
    doc = make_doc(url="https://example.com/legacy", embed_model="")
    indexer.put(doc, fake_embedder.embed(doc["title"]))
    # legacy DB → get_embed_models() 返回 {""} → real=set() → 不 raise
    updated = update_description(
        doc["id"], description="new desc",
        indexer=indexer, embedder=fake_embedder_b,
    )
    assert updated["description"] == "new desc"
