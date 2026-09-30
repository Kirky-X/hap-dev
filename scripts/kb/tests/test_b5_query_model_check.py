"""B5: query() must reject embedder whose model differs from the DB (Red phase).

First-Principles fact F1: a vector's identity is (model_name, dim). If the
embedder used to embed the question is a different model than the one that
produced the stored vectors, the cosine scores are meaningless — query must
fail loud (Rule 12), never silently return wrong results.
"""
from __future__ import annotations

import pytest

from scripts.kb.query import query
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def test_query_raises_on_model_mismatch(indexer, fake_embedder, fake_embedder_b):
    """B5-1: DB built with model-A, query with model-B → raise ValueError."""
    docs = [make_doc(url="https://example.com/a", title="ArkTS 入门")]
    indexer.build(docs, fake_embedder)

    with pytest.raises(ValueError, match="embed_model.*mismatch|model.*differs"):
        query("ArkTS", indexer, fake_embedder_b, top_k=5)


def test_query_succeeds_when_models_match(indexer, fake_embedder):
    """B5-2: DB built with model-A, query with model-A → returns results."""
    docs = [
        make_doc(url="https://example.com/a", title="ArkTS 入门"),
        make_doc(url="https://example.com/b", title="UIAbility 介绍"),
    ]
    indexer.build(docs, fake_embedder)
    results = query("ArkTS", indexer, fake_embedder, top_k=2)
    assert len(results) >= 1


def test_query_succeeds_on_legacy_db_without_embed_model(indexer, fake_embedder):
    """B5-3: legacy DB (no embed_model field) → query proceeds without raising.

    Migration concern: the 964 pre-existing docs have no embed_model. Until
    the migrate script backfills them, query must not break (it would block
    every existing user). Instead, it should treat empty embed_model as
    "unknown" and proceed with a warning logged.

    After migration, this test should be removed (the DB will have embed_model).
    """
    # Manually craft a doc WITHOUT embed_model by stripping it post-build
    docs = [make_doc(url="https://example.com/legacy", title="Legacy")]
    indexer.build(docs, fake_embedder)
    # Wipe the embed_model field directly via set_payload
    from qdrant_client.http import models as qm

    point_id = int(docs[0]["id"][:16], 16)
    indexer.client.set_payload(
        collection_name=indexer.collection,
        payload={"embed_model": None},
        points=[point_id],
    )
    # Now delete the field entirely (set to None leaves key with None; we want
    # truly missing). Easier: unset via overwrite payload.
    indexer.client.delete_payload(
        collection_name=indexer.collection,
        keys=["embed_model"],
        points=[point_id],
    )

    # query should NOT raise — it should return results (with a warning)
    results = query("Legacy", indexer, fake_embedder, top_k=1)
    assert len(results) >= 1
