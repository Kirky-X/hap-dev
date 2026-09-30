"""B25: set_payload 白名单移除向量承载字段 title/description。

indexer.py PAYLOAD_FIELDS 原本包含 title 和 description，注释理由"links.py /
merge.py legitimately write it via set_payload when merging"错误——links.py 不写
title/description（只写 links/updated_at/content_hash），merge.py 用 put() 而非
set_payload。title/description 是向量嵌入源（_embed_text 从 description/title
计算），通过 set_payload 写它们会绕过 upsert 重算向量，导致向量与 payload 不一致。

修复：从 PAYLOAD_FIELDS 移除 title 和 description。set_payload(doc_id,
{"title": "new"}) raise ValueError（fail-loud，Rule 12）。
"""
from __future__ import annotations

import pytest

from scripts.kb.indexer import PAYLOAD_FIELDS
from scripts.kb.tests.conftest import make_doc


def test_set_payload_rejects_title(indexer, fake_embedder):
    """title 是向量承载字段，set_payload 写 title 会绕过 upsert 重算向量。"""
    doc = make_doc(url="https://example.com/b25-title")
    indexer.upsert(doc, fake_embedder)
    with pytest.raises(ValueError, match="unknown payload field"):
        indexer.set_payload(doc["id"], {"title": "new-title"})


def test_set_payload_rejects_description(indexer, fake_embedder):
    """description 是向量承载字段，set_payload 写 description 会绕过 upsert。"""
    doc = make_doc(url="https://example.com/b25-desc")
    indexer.upsert(doc, fake_embedder)
    with pytest.raises(ValueError, match="unknown payload field"):
        indexer.set_payload(doc["id"], {"description": "new-desc"})


def test_set_payload_allows_links(indexer, fake_embedder):
    """links 仍允许（links.py/links_auto.py 通过 set_payload 写 links）。"""
    doc = make_doc(url="https://example.com/b25-links")
    indexer.upsert(doc, fake_embedder)
    indexer.set_payload(doc["id"], {"links": ["other-id"]})  # 不应 raise


def test_set_payload_allows_content_hash(indexer, fake_embedder):
    """content_hash 仍允许（links.py/links_auto.py 刷新 hash 时写）。"""
    doc = make_doc(url="https://example.com/b25-hash")
    indexer.upsert(doc, fake_embedder)
    indexer.set_payload(doc["id"], {"content_hash": "abc123"})  # 不应 raise


def test_payload_fields_excludes_title_and_description():
    """白名单不含 title/description（向量承载字段必须经 upsert）。"""
    assert "title" not in PAYLOAD_FIELDS, "title 不应在 PAYLOAD_FIELDS 中（向量承载字段）"
    assert "description" not in PAYLOAD_FIELDS, "description 不应在 PAYLOAD_FIELDS 中"
    # 仍含其他字段
    assert "links" in PAYLOAD_FIELDS
    assert "content_hash" in PAYLOAD_FIELDS
    assert "context" in PAYLOAD_FIELDS
    assert "embed_model" in PAYLOAD_FIELDS
