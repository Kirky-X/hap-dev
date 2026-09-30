"""B20: query.py BM25 优先用 context 字段 (Red phase).

_bm25_text(doc): 优先 context（信息最丰富），否则 description（非 NO_DESCRIPTION），
否则 title。_embed_text(doc): 不变（description 优先，否则 title）——向量仍用
description 因为是 agent 总结的精炼版。

BM25 索引构建用 _bm25_text，向量嵌入用 _embed_text。
"""
from __future__ import annotations

from scripts.kb.query import _bm25_text, _embed_text
from scripts.kb.sidebar_parser import NO_DESCRIPTION
from scripts.kb.tests.conftest import make_doc


def test_bm25_text_prefers_context():
    """B20-1: doc 有 context → 返回 context（信息最丰富）。"""
    doc = make_doc(url="https://example.com/test-ctx")
    doc["context"] = "这是网页原始内容，信息最丰富"
    doc["description"] = "这是描述"
    assert _bm25_text(doc) == "这是网页原始内容，信息最丰富"


def test_bm25_text_falls_back_to_description_when_no_context():
    """B20-2: doc 无 context 但有 description → 返回 description。"""
    doc = make_doc(url="https://example.com/test-desc")
    doc["context"] = ""
    doc["description"] = "这是描述"
    assert _bm25_text(doc) == "这是描述"


def test_bm25_text_falls_back_to_title_when_no_context_no_description():
    """B20-3: doc 无 context 且 description == NO_DESCRIPTION → 返回 title。"""
    doc = make_doc(url="https://example.com/test-title", title="文档标题")
    doc["context"] = ""
    doc["description"] = NO_DESCRIPTION
    assert _bm25_text(doc) == "文档标题"


def test_bm25_text_falls_back_to_title_when_context_missing_field():
    """B20-4: doc 完全缺 context 字段（legacy）→ 返回 description 或 title。"""
    doc = make_doc(url="https://example.com/test-legacy", title="Legacy 标题")
    # 故意不设 context 字段（模拟 legacy doc）
    if "context" in doc:
        del doc["context"]
    doc["description"] = NO_DESCRIPTION
    assert _bm25_text(doc) == "Legacy 标题"


def test_embed_text_prefers_description_over_title():
    """B20-5: _embed_text 不变——description 优先（非 NO_DESCRIPTION），否则 title。"""
    doc = make_doc(url="https://example.com/test-embed-desc", title="标题")
    doc["description"] = "精炼描述"
    doc["context"] = "原始内容"  # context 不影响 _embed_text
    assert _embed_text(doc) == "精炼描述"


def test_embed_text_falls_back_to_title_when_no_description():
    """B20-6: _embed_text 无 description（或 NO_DESCRIPTION）→ 返回 title。"""
    doc = make_doc(url="https://example.com/test-embed-title", title="只有标题")
    doc["description"] = NO_DESCRIPTION
    doc["context"] = "原始内容"  # context 不影响 _embed_text
    assert _embed_text(doc) == "只有标题"


def test_bm25_text_context_takes_priority_over_description_and_title():
    """B20-7: 同时有 context/description/title 时，context 优先。"""
    doc = make_doc(url="https://example.com/test-priority", title="标题")
    doc["description"] = "描述"
    doc["context"] = "原始内容"
    assert _bm25_text(doc) == "原始内容"


def test_bm25_text_empty_context_falls_back():
    """B20-8: context 为空字符串（非 None）→ 回退到 description。"""
    doc = make_doc(url="https://example.com/test-empty-ctx", title="标题")
    doc["context"] = ""
    doc["description"] = "描述"
    assert _bm25_text(doc) == "描述"
