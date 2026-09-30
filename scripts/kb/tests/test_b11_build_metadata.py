"""B11: build_db must persist build metadata alongside the DB.

原 build_db 完成后无任何元数据持久化，无法回答："这个 DB 是用哪个 embed_model
建的？何时建的？包含多少文档？是否与 sidebars/ 同步？" 导致 query 时无法
快速判断 DB 是否 stale。

修复：build_db 写入 `<db_path>.meta.json`，含 embed_model/embed_dim/built_at
/doc_count/content_hashes 等字段。提供 read_build_meta() 读取。
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

from scripts.kb.build_db import read_build_meta, write_build_meta


def test_write_build_meta_creates_file(tmp_path):
    db_path = str(tmp_path / "test.qdrant")
    stats = {
        "built": 100,
        "total_vectors": 100,
        "embed_model": "test-model",
        "collection": "test_docs",
        "counts": {"app-docs": 50, "best-practices": 50},
        "db_path": db_path,
    }
    content_hashes = {"abc123", "def456"}
    meta = write_build_meta(db_path, stats, content_hashes, embed_dim=384)
    meta_path = Path(f"{db_path}.meta.json")
    assert meta_path.exists()
    on_disk = json.loads(meta_path.read_text(encoding="utf-8"))
    assert on_disk["embed_model"] == "test-model"
    assert on_disk["embed_dim"] == 384
    assert on_disk["doc_count"] == 100
    assert on_disk["collection"] == "test_docs"
    assert set(on_disk["content_hashes"]) == {"abc123", "def456"}
    assert "built_at" in on_disk
    assert on_disk["meta_version"] == 1


def test_read_build_meta_returns_none_if_missing(tmp_path):
    db_path = str(tmp_path / "nonexistent.qdrant")
    assert read_build_meta(db_path) is None


def test_read_build_meta_round_trip(tmp_path):
    db_path = str(tmp_path / "test.qdrant")
    stats = {
        "built": 50,
        "total_vectors": 50,
        "embed_model": "m2",
        "collection": "c",
        "counts": {},
        "db_path": db_path,
    }
    write_build_meta(db_path, stats, {"h1", "h2"}, embed_dim=8)
    meta = read_build_meta(db_path)
    assert meta is not None
    assert meta["embed_model"] == "m2"
    assert meta["embed_dim"] == 8
    assert meta["doc_count"] == 50
    assert set(meta["content_hashes"]) == {"h1", "h2"}


def test_write_build_meta_overwrites_existing(tmp_path):
    db_path = str(tmp_path / "test.qdrant")
    stats1 = {"built": 1, "total_vectors": 1, "embed_model": "old",
              "collection": "c", "counts": {}, "db_path": db_path}
    stats2 = {"built": 2, "total_vectors": 2, "embed_model": "new",
              "collection": "c", "counts": {}, "db_path": db_path}
    write_build_meta(db_path, stats1, {"a"}, embed_dim=8)
    # 确保时间戳不同
    time.sleep(0.01)
    write_build_meta(db_path, stats2, {"b"}, embed_dim=8)
    meta = read_build_meta(db_path)
    assert meta["embed_model"] == "new"
    assert meta["doc_count"] == 2
    assert meta["content_hashes"] == ["b"]


def test_meta_includes_schema_version(tmp_path):
    """meta 文件必须有 schema version，便于未来升级时识别旧格式。"""
    db_path = str(tmp_path / "test.qdrant")
    stats = {"built": 1, "total_vectors": 1, "embed_model": "m",
             "collection": "c", "counts": {}, "db_path": db_path}
    write_build_meta(db_path, stats, set(), embed_dim=8)
    meta = read_build_meta(db_path)
    assert meta["meta_version"] == 1
