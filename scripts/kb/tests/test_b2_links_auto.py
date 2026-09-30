"""B2: links_auto — auto-link docs whose cosine similarity > threshold (Red).

First-Principles fact F3: links semantics = "document relatedness". Two kinds
of links coexist:
  - explicit (from "相关推荐" blocks) — handled by links.py
  - implicit (from vector similarity) — handled by links_auto.py (this module)

User requirement: docs with cosine > 0.9 must be auto-linked bidirectionally.
"""
from __future__ import annotations

import pytest

from scripts.kb.links_auto import auto_link
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def test_auto_link_high_similarity_pair(indexer, fake_embedder):
    """B2-1: two docs with cosine > threshold → bidirectional links established."""
    # Two docs with identical titles → identical embeddings → cosine = 1.0
    docs = [
        make_doc(url="https://example.com/a", title="ArkTS 入门指南"),
        make_doc(url="https://example.com/b", title="ArkTS 入门指南"),
    ]
    indexer.build(docs, fake_embedder)

    stats = auto_link(indexer, threshold=0.9, max_per_doc=10)
    assert stats["pairs_linked"] == 1, f"expected 1 pair linked, got {stats}"

    a = indexer.get(docs[0]["id"])
    b = indexer.get(docs[1]["id"])
    assert docs[1]["id"] in a["links"]
    assert docs[0]["id"] in b["links"]


def test_auto_link_low_similarity_not_linked(indexer, fake_embedder):
    """B2-2: two docs with cosine < threshold → no links."""
    # Different titles → different embeddings (FakeEmbedder uses text hash for
    # perturbation along axis (axis+1)%dim, so distinct texts produce distinct
    # but very close vectors — cosine ~ 0.99999). Use threshold=0.999999 to
    # force them apart.
    docs = [
        make_doc(url="https://example.com/a", title="ArkTS"),
        make_doc(url="https://example.com/b", title="UIAbility"),
    ]
    indexer.build(docs, fake_embedder)

    stats = auto_link(indexer, threshold=0.999999, max_per_doc=10)
    assert stats["pairs_linked"] == 0

    a = indexer.get(docs[0]["id"])
    b = indexer.get(docs[1]["id"])
    assert a["links"] == []
    assert b["links"] == []


def test_auto_link_respects_max_per_doc(indexer, fake_embedder):
    """B2-3: max_per_doc=2 with 4 identical docs → each doc has at most 2 links."""
    docs = [
        make_doc(url=f"https://example.com/{i}", title="Same Title") for i in range(4)
    ]
    indexer.build(docs, fake_embedder)

    stats = auto_link(indexer, threshold=0.9, max_per_doc=2)
    # B28: pairs_linked 语义变更——"任一方向新增"计 1（与 links.py
    # _add_bidirectional_link 一致），单边补全也算。容量约束是真正的
    # 验收意图（注释 "each doc has at most 2 links"），用直接断言验证。
    for d in docs:
        got = indexer.get(d["id"])
        assert len(got["links"]) <= 2, (
            f"doc {d['id']} has {len(got['links'])} links, max_per_doc=2"
        )


def test_auto_link_idempotent(indexer, fake_embedder):
    """B2-4: running auto_link twice does not duplicate links."""
    docs = [
        make_doc(url="https://example.com/a", title="Same"),
        make_doc(url="https://example.com/b", title="Same"),
    ]
    indexer.build(docs, fake_embedder)

    auto_link(indexer, threshold=0.9, max_per_doc=10)
    stats2 = auto_link(indexer, threshold=0.9, max_per_doc=10)
    assert stats2["pairs_linked"] == 0, (
        f"second run should find 0 new pairs, got {stats2['pairs_linked']}"
    )

    a = indexer.get(docs[0]["id"])
    assert a["links"] == [docs[1]["id"]]
    b = indexer.get(docs[1]["id"])
    assert b["links"] == [docs[0]["id"]]


def test_auto_link_no_self_link(indexer, fake_embedder):
    """B2-5: a doc must never link to itself."""
    docs = [make_doc(url="https://example.com/a", title="Solo")]
    indexer.build(docs, fake_embedder)
    auto_link(indexer, threshold=0.9, max_per_doc=10)
    a = indexer.get(docs[0]["id"])
    assert docs[0]["id"] not in a["links"]


def test_auto_link_preserves_existing_explicit_links(indexer, fake_embedder):
    """B2-6: explicit links (from '相关推荐') must not be wiped by auto_link."""
    doc_a = make_doc(url="https://example.com/a", title="A", links=[])
    doc_b = make_doc(url="https://example.com/b", title="A")  # high sim
    doc_c = make_doc(url="https://example.com/c", title="Completely Different Topic")
    # Pre-establish an explicit link a→c
    doc_a["links"] = [doc_c["id"]]
    doc_c["links"] = [doc_a["id"]]
    indexer.build([doc_a, doc_b, doc_c], fake_embedder)

    auto_link(indexer, threshold=0.9, max_per_doc=10)

    a = indexer.get(doc_a["id"])
    c = indexer.get(doc_c["id"])
    # a must still link to c (explicit) AND now to b (auto)
    assert doc_c["id"] in a["links"], "explicit link a→c was wiped"
    assert doc_b["id"] in a["links"], "auto link a→b not added"
    # c must still link to a (explicit, even though their sim is low)
    assert doc_a["id"] in c["links"], "explicit link c→a was wiped"
