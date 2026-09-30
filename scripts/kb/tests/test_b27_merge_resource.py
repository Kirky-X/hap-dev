"""B27: merge.py QdrantIndexer 实例异常时必须关闭（资源泄漏修复）。

merge() 创建 3 个 QdrantIndexer（idx_a, idx_b, idx_out）。Qdrant 本地模式持有
文件锁，异常时不关闭会导致后续操作无法重新打开 DB。现有代码在正常路径调用
close()，但异常路径（list_all/put 抛 RuntimeError）无 try/finally 保护。

修复：用 try/finally 包裹 idx_a/idx_b（读取阶段）和 idx_out（写入阶段）。
QdrantIndexer.close() 已吞异常，finally 中再 close 一次是安全的。
"""
from __future__ import annotations

import pytest
from unittest.mock import patch

from scripts.kb.indexer import QdrantIndexer
from scripts.kb.merge import merge
from scripts.kb.tests.conftest import make_doc


def _build_db(db_path: str, docs, embedder):
    idx = QdrantIndexer(db_path=db_path, collection="test_docs", dim=8)
    idx.build(docs, embedder)
    idx.close()


def test_merge_closes_idx_a_idx_b_on_list_all_failure(tmp_path, fake_embedder):
    """list_all 抛 RuntimeError 时，idx_a 和 idx_b 的 close() 必须被调用。"""
    db_a = str(tmp_path / "a.qdrant")
    db_b = str(tmp_path / "b.qdrant")
    out = str(tmp_path / "out.qdrant")
    _build_db(db_a, [make_doc(url="https://example.com/a")], fake_embedder)
    _build_db(db_b, [make_doc(url="https://example.com/b")], fake_embedder)

    close_calls: list[str] = []
    original_close = QdrantIndexer.close

    def spy_close(self):
        close_calls.append(self.db_path)
        return original_close(self)

    with patch.object(QdrantIndexer, "list_all", side_effect=RuntimeError("boom")), \
         patch.object(QdrantIndexer, "close", spy_close):
        with pytest.raises(RuntimeError, match="boom"):
            merge(db_a, db_b, out, collection="test_docs", dim=8)

    # idx_a 和 idx_b 都必须被 close（idx_out 还未创建）
    assert any(db_a in c for c in close_calls), \
        f"idx_a.close() 必须被调用，实际 close 调用: {close_calls}"
    assert any(db_b in c for c in close_calls), \
        f"idx_b.close() 必须被调用，实际 close 调用: {close_calls}"


def test_merge_closes_idx_out_on_put_failure(tmp_path, fake_embedder):
    """idx_out.put 抛 RuntimeError 时，idx_out 的 close() 必须被调用。"""
    db_a = str(tmp_path / "a.qdrant")
    db_b = str(tmp_path / "b.qdrant")
    out = str(tmp_path / "out.qdrant")
    _build_db(db_a, [make_doc(url="https://example.com/a")], fake_embedder)
    _build_db(db_b, [make_doc(url="https://example.com/b")], fake_embedder)

    close_calls: list[str] = []
    original_close = QdrantIndexer.close

    def spy_close(self):
        close_calls.append(self.db_path)
        return original_close(self)

    with patch.object(QdrantIndexer, "put", side_effect=RuntimeError("put-boom")), \
         patch.object(QdrantIndexer, "close", spy_close):
        with pytest.raises(RuntimeError, match="put-boom"):
            merge(db_a, db_b, out, collection="test_docs", dim=8)

    # idx_out 必须被 close（out path 出现在 close_calls 中）
    assert any(out in c for c in close_calls), \
        f"idx_out.close() 必须被调用，实际 close 调用: {close_calls}"
