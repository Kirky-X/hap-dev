"""B28: links_auto _add_link_bidirectional 分方向补全单向链接。

现有 _add_link_bidirectional 在任一方 len(links) >= max_per_doc 时直接返回 False，
即使另一方向容量未满且该方向链接缺失，也不补全。这导致单向已存在的链接
（a→b 已存在）因 b 容量满无法回链（b→a 缺失），丢失 b→a 链接损害检索召回。

修复：分别检查每个方向的容量与存在性，只补全容量未满且不存在的方向。
返回 True 若任一方向新增。与 links.py _add_bidirectional_link 语义一致。
"""
from __future__ import annotations

from scripts.kb.links_auto import _add_link_bidirectional


def _make_doc(doc_id: str, links: list[str]) -> dict:
    return {"id": doc_id, "links": list(links)}


def test_one_side_full_other_empty_completes_partial():
    """a 满（["x","y"]，max=2）但 b_id 不在其中；b 空 → 补全 b→a，a→b 跳过。"""
    a_doc = _make_doc("a", ["x", "y"])
    b_doc = _make_doc("b", [])
    result = _add_link_bidirectional(None, "a", "b", a_doc, b_doc, max_per_doc=2, now="now")
    assert result is True, "应返回 True（b→a 新增）"
    assert b_doc["links"] == ["a"], f"b_links 应为 ['a']，实际: {b_doc['links']}"
    assert a_doc["links"] == ["x", "y"], "a_links 不变（已满）"


def test_both_not_full_and_already_linked_returns_false():
    """双方都未满且互含 → 返回 False（已存在）。"""
    a_doc = _make_doc("a", ["b"])
    b_doc = _make_doc("b", ["a"])
    result = _add_link_bidirectional(None, "a", "b", a_doc, b_doc, max_per_doc=2, now="now")
    assert result is False, "应返回 False（已存在）"
    assert a_doc["links"] == ["b"]
    assert b_doc["links"] == ["a"]


def test_both_full_returns_false():
    """双方都满 → 返回 False（无法补全任何方向）。"""
    a_doc = _make_doc("a", ["x", "y"])
    b_doc = _make_doc("b", ["z", "w"])
    result = _add_link_bidirectional(None, "a", "b", a_doc, b_doc, max_per_doc=2, now="now")
    assert result is False, "应返回 False（双方都满）"
    assert a_doc["links"] == ["x", "y"]
    assert b_doc["links"] == ["z", "w"]


def test_both_not_full_and_not_linked_adds_both():
    """双方都未满且互不含 → 双向都加。"""
    a_doc = _make_doc("a", [])
    b_doc = _make_doc("b", [])
    result = _add_link_bidirectional(None, "a", "b", a_doc, b_doc, max_per_doc=2, now="now")
    assert result is True
    assert a_doc["links"] == ["b"]
    assert b_doc["links"] == ["a"]


def test_one_side_already_linked_other_not_completes_missing():
    """a→b 已存在，b→a 缺失且 b 未满 → 补全 b→a。"""
    a_doc = _make_doc("a", ["b"])
    b_doc = _make_doc("b", [])
    result = _add_link_bidirectional(None, "a", "b", a_doc, b_doc, max_per_doc=2, now="now")
    assert result is True, "应返回 True（b→a 新增）"
    assert a_doc["links"] == ["b"], "a_links 不变（已有 b）"
    assert b_doc["links"] == ["a"], f"b_links 应为 ['a']，实际: {b_doc['links']}"
