"""B10: merge tie-break must be deterministic when updated_at is equal.

原 _merge_two 用 `a_newer = a["updated_at"] >= b["updated_at"]`，时间戳相等时
a 永远胜出。但 `all_ids = set(docs_a) | set(docs_b)` 迭代顺序未定义，
a/b 在 _merge_two(a, b) 调用中扮演哪个角色取决于 set 迭代顺序，导致
相同输入多次 merge 可能产生不同结果（非确定性）。

修复：updated_at 相等时用 doc_id 字典序作为确定性 tie-breaker（lower id wins）。
"""
from __future__ import annotations

from scripts.kb.merge import _merge_two
from scripts.kb.tests.conftest import make_doc


def _make_doc_with_id(doc_id: str, title: str, description: str,
                       updated_at: str, embed_model: str = "m"):
    """Build a doc with explicit id and updated_at for deterministic tests."""
    doc = make_doc(url=f"https://example.com/{doc_id}", title=title,
                   description=description, embed_model=embed_model)
    doc["id"] = doc_id
    doc["updated_at"] = updated_at
    return doc


def test_tie_break_lower_id_wins():
    """相同 updated_at，id 较低者胜出。"""
    ts = "2026-07-03T00:00:00+00:00"
    a = _make_doc_with_id("ffff0000" * 5, "A-title", "desc A", ts)
    b = _make_doc_with_id("0000ffff" * 5, "B-title", "desc B", ts)
    merged, _ = _merge_two(a, b)
    # b 的 id 较低，应胜出
    assert merged["title"] == "B-title"
    assert merged["description"] == "desc B"


def test_tie_break_same_result_on_swapped_args():
    """交换参数顺序不应改变结果（确定性）。"""
    ts = "2026-07-03T00:00:00+00:00"
    a = _make_doc_with_id("ffff0000" * 5, "A-title", "desc A", ts)
    b = _make_doc_with_id("0000ffff" * 5, "B-title", "desc B", ts)
    m1, _ = _merge_two(a, b)
    m2, _ = _merge_two(b, a)  # 交换参数
    assert m1["title"] == m2["title"]
    assert m1["description"] == m2["description"]


def test_newer_wins_over_tie_break():
    """updated_at 不同时，newer 胜出，无视 id 字典序。"""
    a = _make_doc_with_id("z" * 40, "A-title", "desc A",
                          "2026-07-03T10:00:00+00:00")  # newer
    b = _make_doc_with_id("0" * 40, "B-title", "desc B",
                          "2026-07-03T00:00:00+00:00")  # older
    merged, _ = _merge_two(a, b)
    # a 更新，应胜出（即使 a 的 id 更高）
    assert merged["title"] == "A-title"


def test_tie_break_with_equal_descriptions():
    """updated_at 相等且 description 相等时，tie-break 仍选 lower id。"""
    ts = "2026-07-03T00:00:00+00:00"
    a = _make_doc_with_id("bbbbbbbb" * 5, "A-title", "same desc", ts)
    b = _make_doc_with_id("aaaaaaaa" * 5, "B-title", "same desc", ts)
    merged, needs = _merge_two(a, b)
    # description 相同 → needs_reindex=False
    assert needs is False
    # b 的 id 较低，title 取 b
    assert merged["title"] == "B-title"


def test_tie_break_does_not_affect_links_union():
    """links 是 union，不受 tie-break 影响。"""
    ts = "2026-07-03T00:00:00+00:00"
    a = _make_doc_with_id("zzzz" * 10, "A", "desc", ts)
    b = _make_doc_with_id("aaaa" * 10, "B", "desc", ts)
    a["links"] = ["link1", "link2"]
    b["links"] = ["link2", "link3"]
    merged, _ = _merge_two(a, b)
    assert merged["links"] == ["link1", "link2", "link3"]
