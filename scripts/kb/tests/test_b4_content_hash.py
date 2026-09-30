"""B4: content_hash must include description + links (Red phase).

First-Principles fact F2: content_hash is the doc's "content fingerprint" —
its purpose is to detect "this doc needs re-embedding". Since description is
the primary embedding source (per design D2), a description change MUST
change the hash. The current hash = sha1(title+url+doc_type) misses this.
"""
from __future__ import annotations

import hashlib

from scripts.kb.sidebar_parser import _make_content_hash, NO_DESCRIPTION
from scripts.kb.merge import _merge_two
from scripts.kb.reindex import _content_hash as reindex_content_hash
from scripts.kb.tests.conftest import make_doc


def test_sidebar_parser_hash_includes_description():
    """B4-1: same title/url/doc_type but different description → different hash."""
    h1 = _make_content_hash("T", "U", "D", NO_DESCRIPTION)
    h2 = _make_content_hash("T", "U", "D", "新描述")
    assert h1 != h2, "description change must change content_hash"


def test_sidebar_parser_hash_includes_links():
    """B4-2: same title/url/doc_type/description but different links → different hash."""
    h1 = _make_content_hash("T", "U", "D", "Desc", [])
    h2 = _make_content_hash("T", "U", "D", "Desc", ["other-doc-id"])
    assert h1 != h2, "links change must change content_hash"


def test_sidebar_parser_hash_links_order_invariant():
    """B4-3: links with same members but different order → same hash.

    Order-independence matters because links is a list (insertion-ordered)
    but semantically a set (membership is what counts).
    """
    h1 = _make_content_hash("T", "U", "D", "Desc", ["a", "b"])
    h2 = _make_content_hash("T", "U", "D", "Desc", ["b", "a"])
    assert h1 == h2, "links order must not affect hash (set semantics)"


def test_reindex_hash_matches_sidebar_parser_hash():
    """B4-4: reindex._content_hash and sidebar_parser._make_content_hash must agree.

    Single source of truth (Rule 8): both call sites must use the same hash
    algorithm, otherwise reindex would always think the hash changed.
    """
    h1 = reindex_content_hash("T", "U", "D", "Desc", ["a"])
    h2 = _make_content_hash("T", "U", "D", "Desc", ["a"])
    assert h1 == h2


def test_merge_recomputes_hash_with_description_and_links():
    """B4-5: merge._merge_two must recompute hash including description+links."""
    a = make_doc(url="https://example.com/a", title="A", description="desc-A",
                 links=["other"])
    b = make_doc(url="https://example.com/a", title="A", description="desc-B",
                 links=[])
    # Force b to be newer so its description wins
    b["updated_at"] = "2099-01-01T00:00:00+00:00"
    a["updated_at"] = "2000-01-01T00:00:00+00:00"

    merged, _ = _merge_two(a, b)
    expected = _make_content_hash(
        merged["title"], merged["url"], merged["doc_type"],
        merged["description"], merged["links"],
    )
    assert merged["content_hash"] == expected, (
        f"merge content_hash={merged['content_hash']!r} expected={expected!r}"
    )
