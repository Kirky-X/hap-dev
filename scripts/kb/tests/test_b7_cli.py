"""B7: cli.py — link-auto and migrate-embed-model subcommands (Red→Green).

Smoke-test the two new CLI subcommands end-to-end through the argparse layer.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.kb.cli import main as cli_main
from scripts.kb.tests.conftest import FakeEmbedder, make_doc


def _write_config(tmp_path: Path, db_path: str, embed_model: str = "test-model-A") -> Path:
    cfg = {
        "embed_model": embed_model,
        "embed_dim": 8,
        "embed_source": "",
        "embed_base_url": "",
        "embed_api_key": "",
        "rerank_model": "",
        "rerank_source": "",
        "rerank_base_url": "",
        "rerank_api_key": "",
        "db_path": db_path,
        "collection": "test_docs",
        "sidebars_dir": "sidebars",
        "endpoints": {},
        "query": {"default_top_k": 5, "bm25_weight": 0.3, "vector_weight": 0.7},
    }
    cfg_path = tmp_path / "config.json"
    cfg_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2))
    return cfg_path


def test_cli_link_auto_end_to_end(tmp_path, monkeypatch):
    """B7-1: `cli link-auto` discovers pairs and writes them to the DB."""
    db_path = str(tmp_path / "test.qdrant")
    cfg_path = _write_config(tmp_path, db_path)

    # Build a DB with two near-identical docs (cosine ~ 1.0)
    from scripts.kb.indexer import QdrantIndexer

    emb = FakeEmbedder(model_name="test-model-A", dim=8)
    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    docs = [
        make_doc(url="https://example.com/a", title="ArkTS 入门"),
        make_doc(url="https://example.com/b", title="ArkTS 入门"),
    ]
    idx.build(docs, emb)
    idx.close()

    # Run cli link-auto
    result = cli_main(["link-auto", "--threshold", "0.9", "--max-per-doc", "10",
                       "--config", str(cfg_path)])
    assert result["pairs_linked"] >= 1
    assert result["docs_scanned"] == 2

    # Verify links were actually written to the DB
    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    try:
        a = idx.get(docs[0]["id"])
        b = idx.get(docs[1]["id"])
        assert docs[1]["id"] in a["links"]
        assert docs[0]["id"] in b["links"]
    finally:
        idx.close()


def test_cli_migrate_embed_model_on_legacy_db(tmp_path):
    """B7-2: `cli migrate-embed-model` stamps the model name on legacy docs."""
    db_path = str(tmp_path / "legacy.qdrant")
    cfg_path = _write_config(tmp_path, db_path, embed_model="the-real-model")

    # Build a legacy DB without embed_model by hand
    from qdrant_client import QdrantClient
    from qdrant_client.http import models as qm
    import hashlib

    client = QdrantClient(path=db_path)
    client.create_collection(
        collection_name="test_docs",
        vectors_config=qm.VectorParams(size=8, distance=qm.Distance.COSINE),
    )
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
        # no embed_model — simulates pre-B1 data
    }
    point_id = int(legacy_id[:16], 16)
    client.upsert(
        collection_name="test_docs",
        points=[qm.PointStruct(id=point_id, vector=[1.0] + [0.0] * 7,
                               payload=legacy_payload)],
    )
    client.close()

    # Run migrate
    result = cli_main(["migrate-embed-model", "--config", str(cfg_path)])
    assert result["migrated"] == 1
    assert result["model"] == "the-real-model"

    # Verify the field was actually written
    from scripts.kb.indexer import QdrantIndexer

    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    try:
        got = idx.get(legacy_id)
        assert got is not None
        assert got["embed_model"] == "the-real-model"
    finally:
        idx.close()


def test_cli_migrate_embed_model_idempotent(tmp_path):
    """B7-3: running migrate twice on an already-migrated DB is a no-op."""
    db_path = str(tmp_path / "idem.qdrant")
    cfg_path = _write_config(tmp_path, db_path, embed_model="the-model")

    # Build a properly-stamped DB
    from scripts.kb.indexer import QdrantIndexer

    emb = FakeEmbedder(model_name="the-model", dim=8)
    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    idx.build([make_doc(url="https://example.com/x")], emb)
    idx.close()

    result = cli_main(["migrate-embed-model", "--config", str(cfg_path)])
    assert result["migrated"] == 0
    assert result["skipped"] == 1
    assert "already" in result["note"]


def test_cli_migrate_embed_model_refuses_mixed_db(tmp_path):
    """B7-4: a DB with mixed embed_models must be refused, not 'fixed'."""
    db_path = str(tmp_path / "mixed.qdrant")
    cfg_path = _write_config(tmp_path, db_path, embed_model="model-A")

    # Manually craft two docs with different embed_models
    from qdrant_client import QdrantClient
    from qdrant_client.http import models as qm
    import hashlib

    client = QdrantClient(path=db_path)
    client.create_collection(
        collection_name="test_docs",
        vectors_config=qm.VectorParams(size=8, distance=qm.Distance.COSINE),
    )
    for url, model in [("https://a.example.com", "model-A"),
                       ("https://b.example.com", "model-B")]:
        did = hashlib.sha1(url.encode("utf-8")).hexdigest()
        pid = int(did[:16], 16)
        payload = {
            "id": did, "title": "T", "doc_type": "app-docs", "url": url,
            "description": "无描述", "links": [],
            "created_at": "2024-01-01T00:00:00+00:00",
            "updated_at": "2024-01-01T00:00:00+00:00",
            "content_hash": "x", "embed_model": model,
        }
        client.upsert(
            collection_name="test_docs",
            points=[qm.PointStruct(id=pid, vector=[1.0] + [0.0] * 7,
                                   payload=payload)],
        )
    client.close()

    with pytest.raises(RuntimeError, match="mixed embed_models"):
        cli_main(["migrate-embed-model", "--config", str(cfg_path)])
