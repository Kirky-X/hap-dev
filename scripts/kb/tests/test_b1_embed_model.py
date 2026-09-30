"""B1: embed_model field must be persisted per-doc (Red phase).

Tests that the indexer records which embedding model produced each vector so
that query/merge/reindex can detect cross-model contamination. A vector's
"identity" is (model_name, dim) — same dim alone is insufficient (First
Principles fact F1).
"""
from __future__ import annotations

import pytest

from scripts.kb.indexer import QdrantIndexer
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def test_build_records_embed_model_in_payload(indexer, fake_embedder):
    """B1-1: build() writes embed_model into every doc's payload."""
    docs = [
        make_doc(url="https://example.com/a", title="A"),
        make_doc(url="https://example.com/b", title="B"),
    ]
    indexer.build(docs, fake_embedder)

    for d in docs:
        got = indexer.get(d["id"])
        assert got is not None
        assert got["embed_model"] == fake_embedder.model_name, (
            f"payload.embed_model missing or wrong for {d['id']}: got {got.get('embed_model')!r}"
        )


def test_upsert_writes_embed_model(indexer, fake_embedder):
    """B1-2: upsert() writes embed_model on single-doc insert."""
    doc = make_doc(url="https://example.com/single", title="Single")
    indexer.upsert(doc, fake_embedder)
    got = indexer.get(doc["id"])
    assert got is not None
    assert got["embed_model"] == fake_embedder.model_name


def test_get_embed_models_returns_set(indexer, fake_embedder):
    """B1-3: get_embed_models() returns the set of distinct models in the DB.

    Used by query/merge/reindex to detect cross-model contamination.
    """
    docs = [
        make_doc(url="https://example.com/a", embed_model="model-A"),
        make_doc(url="https://example.com/b", embed_model="model-A"),
        make_doc(url="https://example.com/c", embed_model="model-B"),
    ]
    # build() with model-A embedder — the embedder stamps its model_name onto
    # each doc, overriding whatever embed_model field the doc came in with.
    # We want build to be the source of truth: if the doc says model-A and
    # the embedder is model-A, fine; if they disagree, the embedder wins
    # (the vector was just produced by the embedder, after all).
    indexer.build(docs, fake_embedder)
    models = indexer.get_embed_models()
    assert models == {fake_embedder.model_name}, (
        f"expected single model {fake_embedder.model_name!r}, got {models!r}"
    )


def test_get_embed_models_empty_db_returns_empty_set(indexer):
    """B1-4: empty DB returns empty set (not None, not error)."""
    assert indexer.get_embed_models() == set()


def test_payload_from_legacy_doc_without_embed_model(tmp_db):
    """B1-5: reading a legacy doc (no embed_model field) returns "" not KeyError.

    Migration concern: the 964 pre-existing docs in data/harmonyos.qdrant
    were built without embed_model. The reader must tolerate this until the
    migrate-embed-model script backfills them.
    """
    from qdrant_client import QdrantClient
    from qdrant_client.http import models as qm

    # Manually craft a "legacy" payload without embed_model
    client = QdrantClient(path=tmp_db)
    client.create_collection(
        collection_name="legacy",
        vectors_config=qm.VectorParams(size=8, distance=qm.Distance.COSINE),
    )
    import hashlib

    legacy_id = hashlib.sha1(b"https://legacy.example.com").hexdigest()
    legacy_payload = {
        "id": legacy_id,
        "title": "Legacy",
        "doc_type": "app-docs",
        "url": "https://legacy.example.com",
        "description": "无描述",
        "links": [],
        "created_at": "2024-01-01T00:00:00+00:00",
        "updated_at": "2024-01-01T00:00:00+00:00",
        "content_hash": "abc123",
        # NOTE: no embed_model field — simulates pre-B1 data
    }
    point_id = int(legacy_id[:16], 16)
    client.upsert(
        collection_name="legacy",
        points=[qm.PointStruct(id=point_id, vector=[1.0] + [0.0] * 7, payload=legacy_payload)],
    )
    client.close()

    idx = QdrantIndexer(db_path=tmp_db, collection="legacy", dim=8)
    try:
        got = idx.get(legacy_id)
        assert got is not None
        assert got.get("embed_model", "") == "", (
            "legacy docs without embed_model must read back as empty string, "
            f"got {got.get('embed_model')!r}"
        )
    finally:
        idx.close()


def test_put_preserves_embed_model_from_doc(indexer):
    """B1-6: put(doc, vector) — used by merge — preserves doc['embed_model'].

    merge() copies vectors from source DBs without re-embedding; the embed_model
    field must travel with the doc dict so the merged DB knows each vector's
    origin.
    """
    doc = make_doc(url="https://example.com/put", embed_model="preserved-model")
    vec = [1.0] + [0.0] * 7
    indexer.put(doc, vec)
    got = indexer.get(doc["id"])
    assert got is not None
    assert got["embed_model"] == "preserved-model"


def test_build_rejects_dim_mismatch(indexer, fake_embedder):
    """B1-7: regression — dim mismatch still raises (existing behaviour)."""
    docs = [make_doc(url="https://example.com/x")]
    # Use an embedder whose dim differs from the indexer's dim (8).
    wrong_emb = FakeEmbedder(model_name="test-model-A", dim=16)
    with pytest.raises(ValueError, match="dim"):
        indexer.build(docs, wrong_emb)
