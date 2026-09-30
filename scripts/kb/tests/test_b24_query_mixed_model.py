"""B24: query.py _check_model_compatibility 必须拒绝混合模型 DB。

现有实现只检查 `cur not in real`（embedder 不在 DB 模型集合），不检查
`len(real) > 1`（DB 已被混合模型污染）。混合模型 DB 的余弦相似度无意义——
不同模型产生的向量在不同空间，cosine 跨空间比较是数值噪声。

修复：在 `cur not in real` 检查前加 `len(real) > 1` 检查，raise ValueError
（消息与 merge.py:156-165 一致："mixed embed_models" + "contaminated"）。

对照实现：merge.py _validate_model_compatibility 已对双方 DB 检查 len > 1。
"""
from __future__ import annotations

import pytest

from scripts.kb.query import _check_model_compatibility


class _FakeIndexer:
    """只暴露 get_embed_models() 的假 indexer，用于 _check_model_compatibility。"""

    def __init__(self, models: set[str]) -> None:
        self._models = models

    def get_embed_models(self) -> set[str]:
        return self._models


class _FakeEmbedder:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name


def test_mixed_models_db_raises():
    """DB 含 2 个不同 embed_model → raise ValueError（已污染）。"""
    idx = _FakeIndexer({"model-a", "model-b"})
    emb = _FakeEmbedder("model-a")
    with pytest.raises(ValueError) as exc_info:
        _check_model_compatibility(idx, emb)
    msg = str(exc_info.value)
    assert "mixed embed_models" in msg, f"消息应含 'mixed embed_models'，实际: {msg!r}"
    assert "contaminated" in msg, f"消息应含 'contaminated'，实际: {msg!r}"


def test_legacy_db_no_raise():
    """DB 全是 legacy（embed_model=""）→ 不 raise。"""
    idx = _FakeIndexer({""})
    emb = _FakeEmbedder("model-a")
    # legacy DB 允许通过（migrate-embed-model 会回填）
    _check_model_compatibility(idx, emb)  # 不应 raise


def test_single_model_match_no_raise():
    """DB 单一模型且 embedder 匹配 → 不 raise。"""
    idx = _FakeIndexer({"model-a"})
    emb = _FakeEmbedder("model-a")
    _check_model_compatibility(idx, emb)  # 不应 raise


def test_single_model_mismatch_raises():
    """DB 单一模型但 embedder 不匹配 → raise（已有逻辑，B5）。"""
    idx = _FakeIndexer({"model-a"})
    emb = _FakeEmbedder("model-b")
    with pytest.raises(ValueError):
        _check_model_compatibility(idx, emb)
