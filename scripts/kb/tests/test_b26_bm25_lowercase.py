"""B26: BM25 分词器 ASCII 词大小写归一化。

query.py _tokenize 用 _ASCII_WORD_RE = r"[A-Za-z0-9_-]+" 区分大小写，
"HarmonyOS" 和 "harmonyos" 是不同 token，BM25 召回不一致——用户查询
"harmonyos" 无法匹配文档中的 "HarmonyOS"。

修复：ASCII word token 提取后调用 .lower() 归一化。CJK 字符无大小写，
不受影响。
"""
from __future__ import annotations

from scripts.kb.query import _tokenize


def test_ascii_word_lowercased():
    """大写 ASCII 词归一化为小写。"""
    assert _tokenize("HarmonyOS ArkTS") == ["harmonyos", "arkts"]


def test_case_normalized_consistency():
    """大小写不同的同一词归一化后一致。"""
    assert _tokenize("HarmonyOS ArkTS") == _tokenize("harmonyos ArkTS")
    assert _tokenize("harmonyos arkts") == _tokenize("HARMONYOS ARKTS")


def test_cjk_unchanged():
    """CJK 字符无大小写，归一化不影响。"""
    tokens = _tokenize("UIAbility_2 配置")
    assert tokens == ["uiability_2", "配", "置"]


def test_mixed_case_compound():
    """连字符/下划线连接的复合 token 整体小写。"""
    assert _tokenize("errorCode-123") == ["errorcode-123"]
    assert _tokenize("UIAbility_2") == ["uiability_2"]
