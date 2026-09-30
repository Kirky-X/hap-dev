"""B3: merge() must reject DBs built with different embed_models (Red phase).

First-Principles fact F1 + Rule 7 (暴露冲突不折中): merging two DBs whose
vectors come from different models yields a DB with mixed vector spaces —
cosine scores become meaningless. merge() must fail loud instead of silently
producing a corrupted DB.
"""
from __future__ import annotations

import pytest

from scripts.kb.merge import merge
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def _build_db(db_path: str, docs, embedder):
    from scripts.kb.indexer import QdrantIndexer

    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    idx.build(docs, embedder)
    idx.close()


def test_merge_raises_on_model_mismatch(tmp_path, fake_embedder, fake_embedder_b):
    """B3-1: DB A built with model-A, DB B built with model-B → merge raises."""
    db_a = str(tmp_path / "a.qdrant")
    db_b = str(tmp_path / "b.qdrant")
    out = str(tmp_path / "out.qdrant")

    _build_db(db_a, [make_doc(url="https://example.com/a", title="A")], fake_embedder)
    _build_db(db_b, [make_doc(url="https://example.com/b", title="B")], fake_embedder_b)

    with pytest.raises(ValueError, match="embed_model.*differ|model.*mismatch"):
        merge(db_a, db_b, out, collection="test_docs", dim=8)


def test_merge_succeeds_when_models_match(tmp_path, fake_embedder):
    """B3-2: DB A and DB B both built with model-A → merge succeeds."""
    db_a = str(tmp_path / "a.qdrant")
    db_b = str(tmp_path / "b.qdrant")
    out = str(tmp_path / "out.qdrant")

    _build_db(db_a, [make_doc(url="https://example.com/a", title="A")], fake_embedder)
    _build_db(db_b, [make_doc(url="https://example.com/b", title="B")], fake_embedder)

    res = merge(db_a, db_b, out, collection="test_docs", dim=8)
    assert res["merged_count"] == 2


def test_merge_preserves_embed_model_in_output(tmp_path, fake_embedder):
    """B3-3: merged DB must carry embed_model for each doc (no field loss)."""
    db_a = str(tmp_path / "a.qdrant")
    db_b = str(tmp_path / "b.qdrant")
    out = str(tmp_path / "out.qdrant")

    _build_db(db_a, [make_doc(url="https://example.com/a", title="A")], fake_embedder)
    _build_db(db_b, [make_doc(url="https://example.com/b", title="B")], fake_embedder)

    merge(db_a, db_b, out, collection="test_docs", dim=8)

    from scripts.kb.indexer import QdrantIndexer

    idx = QdrantIndexer(db_path=out, collection="test_docs", dim=8)
    try:
        models = idx.get_embed_models()
        assert models == {fake_embedder.model_name}
    finally:
        idx.close()
