"""B14: schema v3 — 加 context 字段 + content_hash 公式升级 (Red phase).

context 字段存储 url 抓取的原始 markdown 内容：
1. parse_sidebar 返回的 doc 必须有 context="" 初始值
2. _make_content_hash 必须接受 context 参数（默认 "" 向后兼容）
3. context 变化必须改变 content_hash（B14 核心：检测网页变化）
4. context 必须进入 hash 原文（顺序：title+url+doc_type+description+context+"|links:"+sorted(links)）
"""
from __future__ import annotations

import hashlib

import pytest

from scripts.kb.indexer import PAYLOAD_FIELDS, QdrantIndexer
from scripts.kb.sidebar_parser import _make_content_hash, parse_sidebar
from scripts.kb.tests.conftest import make_doc


# ---- T002: parse_sidebar context 字段 ----

def test_parse_sidebar_doc_has_context_field(tmp_path):
    """B14-1: parse_sidebar 返回的每个 doc 有 context="" 字段。"""
    sidebar = tmp_path / "test-sidebar.md"
    sidebar.write_text(
        "#### 1.1.1 [示例标题](https://example.com/doc1)\n",
        encoding="utf-8",
    )
    docs = parse_sidebar(str(sidebar), "app-docs")
    assert len(docs) == 1
    doc = docs[0]
    assert "context" in doc, "doc 必须有 context 字段（B14 schema v3）"
    assert doc["context"] == "", "新 doc 的 context 必须初始为空字符串"


def test_parse_sidebar_all_docs_have_context(tmp_path):
    """B14-2: 多个 doc 都有 context 字段。"""
    sidebar = tmp_path / "multi.md"
    sidebar.write_text(
        "#### 1.1.1 [标题A](https://example.com/a)\n"
        "#### 1.1.2 [标题B](https://example.com/b)\n"
        "#### 1.1.3 [标题C](https://example.com/c)\n",
        encoding="utf-8",
    )
    docs = parse_sidebar(str(sidebar), "app-docs")
    assert len(docs) == 3
    for d in docs:
        assert d.get("context") == ""


# ---- T002: _make_content_hash context 参数 ----

def test_make_content_hash_accepts_context_param():
    """B14-3: _make_content_hash 接受 context 参数（默认 "" 向后兼容）。

    不传 context 应等于传 context="" —— 旧调用方零改动。
    """
    h_old = _make_content_hash("T", "U", "D", "Desc", ["a"])
    h_empty = _make_content_hash("T", "U", "D", "Desc", ["a"], context="")
    assert h_old == h_empty, "context 默认空字符串应与旧公式一致（向后兼容）"


def test_make_content_hash_context_changes_hash():
    """B14-4: context 变化必须改变 content_hash（检测网页变化的核心）。"""
    h1 = _make_content_hash("T", "U", "D", "Desc", [], context="旧内容")
    h2 = _make_content_hash("T", "U", "D", "Desc", [], context="新内容")
    assert h1 != h2, "context 变化必须改变 content_hash"


def test_make_content_hash_context_in_raw():
    """B14-5: context 必须进入 hash 原文（顺序：description + context + links）。"""
    title, url, doc_type, desc = "T", "U", "D", "Desc"
    context = "网页原始内容"
    links = ["b", "a"]
    expected_raw = (
        title + url + doc_type + desc + context
        + "|links:" + ",".join(sorted(links))
    ).encode("utf-8")
    expected = hashlib.sha1(expected_raw).hexdigest()
    actual = _make_content_hash(title, url, doc_type, desc, links, context=context)
    assert actual == expected, (
        f"context 必须进入 hash 原文；got {actual!r} expected {expected!r}"
    )


# ---- T005: indexer PAYLOAD_FIELDS + _payload_from + set_payload ----


def test_payload_fields_contains_context():
    """B14-6: PAYLOAD_FIELDS whitelist 必须含 context（set_payload 才能写它）。"""
    assert "context" in PAYLOAD_FIELDS, (
        "PAYLOAD_FIELDS 必须含 context（B14 schema v3）"
    )


def test_payload_from_legacy_missing_context():
    """B14-7: _payload_from 对缺 context 的 legacy payload 返回 ""。"""
    legacy_payload = {
        "id": "abc123",
        "title": "T",
        "doc_type": "D",
        "url": "U",
        "description": "Desc",
        "links": [],
        "created_at": "2020-01-01T00:00:00+00:00",
        "updated_at": "2020-01-01T00:00:00+00:00",
        "content_hash": "hash",
        "embed_model": "model-x",
        # 注意：legacy payload 没有 context 字段
    }
    doc = QdrantIndexer._payload_from(legacy_payload)
    assert doc["context"] == "", (
        "legacy payload 缺 context 字段时，_payload_from 应返回空字符串"
    )


def test_payload_from_legacy_context_none():
    """B14-8: _payload_from 对 context=None 的 payload 返回 ""（Qdrant ops 残留）。"""
    payload_with_none = {
        "id": "abc123",
        "title": "T",
        "doc_type": "D",
        "url": "U",
        "description": "Desc",
        "links": [],
        "created_at": "2020-01-01T00:00:00+00:00",
        "updated_at": "2020-01-01T00:00:00+00:00",
        "content_hash": "hash",
        "embed_model": "model-x",
        "context": None,  # Qdrant ops 可能残留 None
    }
    doc = QdrantIndexer._payload_from(payload_with_none)
    assert doc["context"] == "", "context=None 应被 coerce 为空字符串"


def test_set_payload_accepts_context(indexer, fake_embedder):
    """B14-9: set_payload({"context": "..."}) 不抛异常（whitelist 接受 context）。"""
    doc = make_doc(url="https://example.com/set-payload-test")
    indexer.upsert(doc, fake_embedder)

    indexer.set_payload(doc["id"], {"context": "这是抓取的网页内容"})

    stored = indexer.get(doc["id"])
    assert stored is not None
    assert stored["context"] == "这是抓取的网页内容"


def test_set_payload_still_rejects_unknown_fields(indexer, fake_embedder):
    """B14-10: set_payload 仍拒绝未知字段（whitelist 仍有效，未因加 context 而放宽）。"""
    doc = make_doc(url="https://example.com/whitelist-test")
    indexer.upsert(doc, fake_embedder)

    with pytest.raises(ValueError, match="unknown payload field"):
        indexer.set_payload(doc["id"], {"bogus_field": "should fail"})
