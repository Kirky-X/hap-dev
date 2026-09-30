"""B12: point_id collision must be detected at runtime.

原 _point_id(doc_id) = int(doc_id[:16], 16)。两个不同 sha1 id 理论上可能
共享前 16 hex 字符（碰撞概率极低但非零），导致 upsert 静默覆盖一方的数据
（向量+payload 全失）。

修复：
- build() 入口检测同一批次内 point_id 冲突，fail-loud
- upsert() 入口检测目标 point_id 已存在但 id 字段不同，fail-loud
- 相同 doc_id 重复 upsert 是 idempotent，不视为冲突
"""
from __future__ import annotations

import pytest

from scripts.kb.indexer import QdrantIndexer, _point_id


def test_point_id_collision_in_build_raises(indexer, fake_embedder):
    from scripts.kb.tests.conftest import make_doc
    doc_a = make_doc(url="https://example.com/a")
    doc_b = make_doc(url="https://example.com/b")
    # 强制前 16 hex 一致，后 24 hex 不同
    doc_a["id"] = "abcdef0123456789" + "a" * 24
    doc_b["id"] = "abcdef0123456789" + "b" * 24
    assert _point_id(doc_a["id"]) == _point_id(doc_b["id"])
    with pytest.raises(ValueError, match="point_id collision"):
        indexer.build([doc_a, doc_b], fake_embedder)


def test_point_id_collision_in_upsert_raises(indexer, fake_embedder):
    from scripts.kb.tests.conftest import make_doc
    doc_a = make_doc(url="https://example.com/a")
    doc_a["id"] = "abcdef0123456789" + "a" * 24
    indexer.upsert(doc_a, fake_embedder)
    # 不同 doc_id 但相同 point_id
    doc_b = make_doc(url="https://example.com/b")
    doc_b["id"] = "abcdef0123456789" + "b" * 24
    with pytest.raises(ValueError, match="point_id collision"):
        indexer.upsert(doc_b, fake_embedder)


def test_same_doc_id_re_upsert_no_collision(indexer, fake_embedder):
    """相同 doc_id 重复 upsert 是 idempotent，不应抛异常。"""
    from scripts.kb.tests.conftest import make_doc
    doc = make_doc(url="https://example.com/same")
    indexer.upsert(doc, fake_embedder)
    # 再次 upsert 同一 doc —— 不应抛
    indexer.upsert(doc, fake_embedder)
    # 数据应保留
    got = indexer.get(doc["id"])
    assert got is not None
    assert got["id"] == doc["id"]


def test_build_with_unique_ids_succeeds(indexer, fake_embedder):
    """正常情况（无冲突）build 应成功。"""
    from scripts.kb.tests.conftest import make_doc
    docs = [
        make_doc(url="https://example.com/1"),
        make_doc(url="https://example.com/2"),
        make_doc(url="https://example.com/3"),
    ]
    indexer.build(docs, fake_embedder)
    assert indexer.count() == 3


def test_point_id_collision_error_includes_both_ids(indexer, fake_embedder):
    """错误消息必须包含两个冲突的 doc_id 便于调试（Rule 12）。"""
    from scripts.kb.tests.conftest import make_doc
    doc_a = make_doc(url="https://example.com/a")
    doc_a["id"] = "abcdef0123456789" + "a" * 24
    indexer.upsert(doc_a, fake_embedder)
    doc_b = make_doc(url="https://example.com/b")
    doc_b["id"] = "abcdef0123456789" + "b" * 24
    with pytest.raises(ValueError) as exc_info:
        indexer.upsert(doc_b, fake_embedder)
    err_msg = str(exc_info.value)
    # 错误消息包含两个 doc_id
    assert doc_a["id"] in err_msg or doc_a["id"][:16] in err_msg
    assert doc_b["id"] in err_msg or doc_b["id"][:16] in err_msg
