"""CJK tokenizer guard on the local embed backend (English-only model sinking).

paraphrase-MiniLM-L3-v2（bert-base-uncased 词表）把所有中文映射成 [UNK]，
同长度标题的向量全部塌缩且检索静默退化——守卫必须在加载时 fail loud。
"""
import unittest
from unittest import mock

try:
    import sentence_transformers  # noqa: F401

    _HAS_ST = True
except ImportError:
    _HAS_ST = False  # CI 轻量环境不装 torch 级依赖；嵌入守卫测试在装有 sentence-transformers 的本地环境执行


class _UnkTokenizer:
    unk_token_id = 100

    def __call__(self, text):
        return {"input_ids": [101, 100, 100, 102]}


class _BrokenST:
    def __init__(self, name):
        self.tokenizer = _UnkTokenizer()


class _HealthyTokenizer:
    unk_token_id = 100

    def __call__(self, text):
        return {"input_ids": [101, 5582, 2841, 102]}


class _HealthyST:
    def __init__(self, name):
        self.tokenizer = _HealthyTokenizer()


@unittest.skipUnless(_HAS_ST, "sentence-transformers 未安装（CI 轻量环境）")
class TestCjkGuard(unittest.TestCase):
    MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    def test_cjk_to_unk_raises(self):
        from scripts.kb.embed import Embedder
        with mock.patch("sentence_transformers.SentenceTransformer", _BrokenST):
            with self.assertRaises(ValueError):
                Embedder(self.MODEL)._load_local()

    def test_healthy_tokenizer_loads(self):
        from scripts.kb.embed import Embedder
        with mock.patch("sentence_transformers.SentenceTransformer", _HealthyST):
            st = Embedder(self.MODEL)._load_local()
        self.assertIsInstance(st, _HealthyST)

    def test_no_unk_concept_skips_probe(self):
        from scripts.kb.embed import Embedder

        class _TokWithoutUnk:
            unk_token_id = None

            def __call__(self, text):
                return {"input_ids": [1, 2, 3]}

        class _ST:
            def __init__(self, name):
                self.tokenizer = _TokWithoutUnk()

        with mock.patch("sentence_transformers.SentenceTransformer", _ST):
            st = Embedder(self.MODEL)._load_local()
        self.assertIsInstance(st, _ST)


if __name__ == "__main__":
    unittest.main()
