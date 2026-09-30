"""B8: BM25 tokenizer must handle English terms as whole tokens.

原 _tokenize 用 `[c for c in text if not c.isspace()]` 字符级切分，对英文术语
劣化：'ArkTS' → ['A','r','k','T','S']，导致查询 'ArkTS' 会匹配任何含这些字符
的文档（如 'ArkUI'、'API'），BM25 区分度严重下降。

修复目标：英文单词作为整 token；中文按字符切分；标点作为分隔符。
"""
from __future__ import annotations

from scripts.kb.query import _tokenize


def test_english_word_kept_as_single_token():
    tokens = _tokenize("ArkTS 入门")
    assert "arkts" in tokens  # B26: 归一化为小写
    assert "A" not in tokens  # 不能拆成单字符
    assert "r" not in tokens


def test_chinese_kept_as_individual_chars():
    tokens = _tokenize("ArkTS 入门指南")
    assert "入" in tokens
    assert "门" in tokens
    assert "指" in tokens
    assert "南" in tokens


def test_mixed_text_tokenizes_correctly():
    tokens = _tokenize("使用 ArkTS 编写 UIAbility 组件")
    # 英文整 token（B26: 小写归一化）
    assert "arkts" in tokens
    assert "uiability" in tokens
    # 中文字符
    assert "组" in tokens
    assert "件" in tokens


def test_punctuation_separates_tokens():
    tokens = _tokenize("ArkTS,harmonyos;UIAbility")
    assert "arkts" in tokens  # B26: 小写
    assert "harmonyos" in tokens
    assert "uiability" in tokens  # B26: 小写
    assert "," not in tokens
    assert ";" not in tokens


def test_lowercase_english_tokenized():
    tokens = _tokenize("harmonyos build")
    assert "harmonyos" in tokens
    assert "build" in tokens


def test_digits_kept_with_word():
    # 'errorcode-123' 应作为整 token（连字符连接的英文+数字）
    tokens = _tokenize("errorcode-123 ArkTS")
    assert "errorcode-123" in tokens
    assert "arkts" in tokens  # B26: 小写


def test_empty_string_returns_empty():
    assert _tokenize("") == []
    assert _tokenize("   \t\n  ") == []


def test_idempotent():
    # 相同输入两次结果一致
    t1 = _tokenize("ArkTS 入门指南")
    t2 = _tokenize("ArkTS 入门指南")
    assert t1 == t2
