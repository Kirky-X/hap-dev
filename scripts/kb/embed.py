"""Embedding abstraction (tasks 4.4-4.5).

Embedder picks one of two backends based on the model_name prefix:

* ``openai://<model>``  -> cloud, OpenAI-compatible ``POST {base_url}/v1/embeddings``
                          via httpx. ``base_url`` and ``api_key`` come from config.
* anything else         -> local sentence-transformers. When ``source == "modelscope"``
                          the model is fetched via ``modelscope.snapshot_download`` first
                          (best-effort: falls back to the raw name if modelscope isn't
                          installed).

The model is loaded lazily on first embed so constructing an Embedder is cheap and
tests can mock sentence_transformers / httpx without triggering downloads.
"""
from __future__ import annotations

from typing import Any, Optional

import httpx

OPENAI_PREFIX = "openai://"


class Embedder:
    def __init__(
        self,
        model_name: str,
        base_url: str = "",
        api_key: str = "",
        source: str = "",
    ) -> None:
        self.model_name = model_name
        self.base_url = base_url
        self.api_key = api_key
        self.source = source
        self._is_cloud = model_name.startswith(OPENAI_PREFIX)
        self._model: Optional[Any] = None  # lazy-loaded local backend

    # ---- public API -------------------------------------------------------

    def embed(self, text: str) -> list[float]:
        """Embed a single string; return a list of floats (384-dim for the
        default model)."""
        if self._is_cloud:
            return self._embed_cloud([text])[0]
        if self._model is None:
            self._model = self._load_local()
        vec = self._model.encode([text])
        return _vec_to_list(vec[0])

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of strings. Returns [] for an empty input (no API call)."""
        if not texts:
            return []
        if self._is_cloud:
            return self._embed_cloud(texts)
        if self._model is None:
            self._model = self._load_local()
        vecs = self._model.encode(texts)
        return [_vec_to_list(v) for v in vecs]

    # ---- backends ---------------------------------------------------------

    def _load_local(self) -> Any:
        """Load the sentence-transformers backend, optionally via modelscope."""
        from sentence_transformers import SentenceTransformer  # lazy import

        name: Any = self.model_name
        if self.source == "modelscope":
            try:
                from modelscope import snapshot_download
                name = snapshot_download(self.model_name)
            except ImportError:
                # modelscope not installed — fall back to the raw name; ST will
                # pull from HuggingFace if reachable. Not silently swallowing: the
                # caller asked for modelscope but the dep is missing — we still
                # attempt a real load which will fail loudly if unreachable.
                pass
        return SentenceTransformer(name)

    def _embed_cloud(self, texts: list[str]) -> list[list[float]]:
        model = self.model_name[len(OPENAI_PREFIX):]
        if not self.base_url:
            raise ValueError(
                "openai:// embed model requires embed_base_url in config (got empty)"
            )
        url = self.base_url.rstrip("/") + "/v1/embeddings"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        resp = httpx.post(
            url,
            json={"model": model, "input": texts},
            headers=headers,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        # OpenAI returns data sorted by index; sort to be safe.
        items = sorted(data["data"], key=lambda d: d.get("index", 0))
        return [list(item["embedding"]) for item in items]


def _vec_to_list(v: Any) -> list[float]:
    """Normalize numpy / list / tuple vector to a plain list[float]."""
    if hasattr(v, "tolist"):
        v = v.tolist()
    return [float(x) for x in v]
