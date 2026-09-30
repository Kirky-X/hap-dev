"""B22: merge.py _merge_two 必须保留 context 字段并纳入 content_hash。

B14 把 context 加入 content_hash 公式后，_merge_two 仍按 _SCALAR_FIELDS
合并标量字段，但 context 不在 _SCALAR_FIELDS 中（语义不同：context 是网页
原始内容而非元数据）。修复前 _merge_two 未在 merged dict 中设 context，
且 _make_content_hash 调用未传 context，导致合并后 doc 的 context 丢失且
hash 与实际内容脱钩——后续 reindex(force=False) 会误判 doc 未变化而跳过
重嵌入。

修复：在 _merge_two 内显式合并 context（复用 _merge_scalar 逻辑，空值
判定为 ""），并把 merged["context"] 传给 _make_content_hash。
"""
from __future__ import annotations

from scripts.kb.merge import _merge_two
from scripts.kb.sidebar_parser import NO_DESCRIPTION, _make_content_hash
from scripts.kb.tests.conftest import make_doc


def _make_doc_with_id(
    doc_id: str,
    title: str,
    description: str,
    updated_at: str,
    context: str = "",
    embed_model: str = "m",
    url: str | None = None,
):
    """Build a doc with explicit id/updated_at/context for deterministic tests.

    `url` defaults to f"https://example.com/{doc_id}"；可显式传相同 url
    以在控制变量测试中让 a/b 的 url 一致（仅 context 不同）。
    """
    doc = make_doc(
        url=url if url is not None else f"https://example.com/{doc_id}",
        title=title,
        description=description,
        embed_model=embed_model,
    )
    doc["id"] = doc_id
    doc["updated_at"] = updated_at
    doc["context"] = context
    return doc


def test_merge_two_preserves_context_newer_wins():
    """a_newer=True 时 merged['context'] 取 a 的 context。"""
    a = _make_doc_with_id(
        "a" * 40, "A-title", "desc A",
        "2026-07-03T10:00:00+00:00",  # newer
        context="ctx-a",
    )
    b = _make_doc_with_id(
        "b" * 40, "B-title", "desc B",
        "2026-07-03T00:00:00+00:00",
        context="ctx-b",
    )
    merged, _ = _merge_two(a, b)
    assert "context" in merged, "merged dict 必须含 context 字段"
    assert merged["context"] == "ctx-a", "newer wins — a 的 context 应胜出"


def test_merge_two_preserves_context_when_one_side_empty():
    """一方 context 为空时取非空方。"""
    # a context 为空，b 有 context
    a = _make_doc_with_id(
        "a" * 40, "A-title", "desc A",
        "2026-07-03T10:00:00+00:00",  # a newer
        context="",
    )
    b = _make_doc_with_id(
        "b" * 40, "B-title", "desc B",
        "2026-07-03T00:00:00+00:00",
        context="ctx-b",
    )
    merged, _ = _merge_two(a, b)
    # a 虽 newer 但 context 空，应取 b 的非空 context
    assert merged["context"] == "ctx-b", "一方为空时取非空方"

    # 反过来：a 有 context，b 为空
    a2 = _make_doc_with_id(
        "a" * 40, "A-title", "desc A",
        "2026-07-03T10:00:00+00:00",
        context="ctx-a",
    )
    b2 = _make_doc_with_id(
        "b" * 40, "B-title", "desc B",
        "2026-07-03T00:00:00+00:00",
        context="",
    )
    merged2, _ = _merge_two(a2, b2)
    assert merged2["context"] == "ctx-a", "一方为空时取非空方"


def test_merge_two_content_hash_includes_context():
    """merged['content_hash'] 必须基于 merged['context'] 重算（含 context）。"""
    a = _make_doc_with_id(
        "a" * 40, "A-title", "desc A",
        "2026-07-03T10:00:00+00:00",
        context="ctx-a",
    )
    b = _make_doc_with_id(
        "b" * 40, "B-title", "desc B",
        "2026-07-03T00:00:00+00:00",
        context="ctx-b",
    )
    merged, _ = _merge_two(a, b)

    expected_hash = _make_content_hash(
        merged["title"], merged["url"], merged["doc_type"],
        merged.get("description", NO_DESCRIPTION),
        merged["links"],
        context=merged["context"],
    )
    assert merged["content_hash"] == expected_hash, (
        "content_hash 必须含 context —— hash 公式应反映 context 字段"
    )


def test_merge_two_content_hash_changes_with_context():
    """context 不同时 content_hash 必须不同（证明 hash 含 context）。

    控制变量：a 和 b 的 title/description/url/doc_type/links 都相同，
    仅 context 不同。a newer 时 merged context=ctx-a，b newer 时
    merged context=ctx-b，两次 merge 的 hash 应不同。
    """
    same_url = "https://example.com/same-doc"
    # a newer — merged 取 a 的字段（context=ctx-a）
    a_newer = _make_doc_with_id(
        "a" * 40, "same-title", "same desc",
        "2026-07-03T10:00:00+00:00",  # a newer
        context="ctx-a",
        url=same_url,
    )
    b_older = _make_doc_with_id(
        "b" * 40, "same-title", "same desc",
        "2026-07-03T00:00:00+00:00",
        context="ctx-b",
        url=same_url,
    )
    merged_a_newer, _ = _merge_two(a_newer, b_older)

    # b newer — merged 取 b 的字段（context=ctx-b）
    a_older = _make_doc_with_id(
        "a" * 40, "same-title", "same desc",
        "2026-07-03T00:00:00+00:00",  # a older now
        context="ctx-a",
        url=same_url,
    )
    b_newer = _make_doc_with_id(
        "b" * 40, "same-title", "same desc",
        "2026-07-03T10:00:00+00:00",  # b newer
        context="ctx-b",
        url=same_url,
    )
    merged_b_newer, _ = _merge_two(a_older, b_newer)

    # 两次 merge 的 title/description/url/links 都相同，仅 context 不同
    # （ctx-a vs ctx-b），故 hash 必须不同
    assert merged_a_newer["content_hash"] != merged_b_newer["content_hash"], (
        "context 不同时 content_hash 必须不同 —— 证明 hash 公式含 context"
    )
