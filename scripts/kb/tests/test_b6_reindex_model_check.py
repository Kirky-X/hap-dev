"""B6: reindex() must auto-upgrade to force=True when embed_model changes (Red).

Bug A11: reindex(force=False) only compares content_hash. If the user changes
embed_model in config.json but the docs' content_hash hasn't changed, force=False
returns 0 — leaving all vectors stale (from the old model). reindex must
detect the model change and auto-upgrade to force=True.
"""
from __future__ import annotations

from scripts.kb.reindex import reindex
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def test_reindex_auto_force_on_model_change(indexer, fake_embedder, fake_embedder_b):
    """B6-1: DB built with model-A, reindex with model-B → all docs re-embedded
    (auto force=True), and DB embed_model field updated to model-B.
    """
    docs = [
        make_doc(url="https://example.com/a", title="A"),
        make_doc(url="https://example.com/b", title="B"),
    ]
    indexer.build(docs, fake_embedder)
    assert indexer.get_embed_models() == {"test-model-A"}

    # reindex with model-B embedder — should auto-force
    n = reindex(indexer, fake_embedder_b, force=False)
    assert n == 2, f"expected 2 docs re-embedded (auto-force), got {n}"

    # DB should now report model-B
    assert indexer.get_embed_models() == {"test-model-B"}


def test_reindex_no_force_when_model_same(indexer, fake_embedder):
    """B6-2: DB built with model-A, reindex with model-A force=False → 0 docs
    (content_hash unchanged, model unchanged).
    """
    docs = [make_doc(url="https://example.com/a", title="A")]
    indexer.build(docs, fake_embedder)
    n = reindex(indexer, fake_embedder, force=False)
    assert n == 0


def test_reindex_force_true_always_reembeds(indexer, fake_embedder):
    """B6-3: regression — force=True still re-embeds every doc even if nothing changed."""
    docs = [make_doc(url="https://example.com/a", title="A")]
    indexer.build(docs, fake_embedder)
    n = reindex(indexer, fake_embedder, force=True)
    assert n == 1
