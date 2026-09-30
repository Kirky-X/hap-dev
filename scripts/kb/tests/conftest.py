"""Shared pytest fixtures for the kb tests.

Tests use a temporary directory for the Qdrant local DB so they never touch
the real ``data/harmonyos.qdrant`` shipped with the skill.
"""
from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest

# Ensure ``scripts`` package is importable when tests are run from the
# hap-dev root via ``python3 -m pytest scripts/kb/tests``.
HAP_DEV_ROOT = Path(__file__).resolve().parents[2]
if str(HAP_DEV_ROOT) not in sys.path:
    sys.path.insert(0, str(HAP_DEV_ROOT))

from scripts.kb.sidebar_parser import NO_DESCRIPTION  # noqa: E402


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_doc(
    url: str = "https://example.com/doc",
    title: str = "示例文档标题",
    doc_type: str = "app-docs",
    description: str = NO_DESCRIPTION,
    links: list[str] | None = None,
    embed_model: str = "test-model-A",
    context: str = "",
) -> dict[str, Any]:
    """Build a minimal doc dict matching the 11-field schema (after B14 upgrade)."""
    doc_id = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return {
        "id": doc_id,
        "title": title,
        "doc_type": doc_type,
        "url": url,
        "description": description,
        "links": links or [],
        "created_at": _now_iso(),
        "updated_at": _now_iso(),
        "content_hash": hashlib.sha1(
            (title + url + doc_type + description + context + "|links:").encode("utf-8")
        ).hexdigest(),
        "embed_model": embed_model,
        "context": context,
    }


class FakeEmbedder:
    """Deterministic embedder for tests — no model download, no network.

    Produces a unit vector along an axis determined by ``model_name`` so that
    different model names yield non-overlapping vector spaces (mirrors the
    First-Principles fact F1: same dim ≠ same space).

    The text contributes two significant components (not just tiny noise) so
    that distinct texts produce visibly different vectors — cosine similarity
    between "ArkTS" and "UIAbility" is well below 0.9, while identical titles
    still produce cosine = 1.0.
    """

    def __init__(self, model_name: str = "test-model-A", dim: int = 8) -> None:
        self.model_name = model_name
        self.dim = dim
        # axis = hash(model_name) % dim — same model always maps to same axis
        self._axis = hash(model_name) % dim

    def embed(self, text: str) -> list[float]:
        vec = [0.0] * self.dim
        vec[self._axis] = 1.0
        # Text contributes two significant components (bytes 0-7 of hash /
        # 255). This makes different texts produce visibly different vectors
        # while keeping identical texts identical.
        h = abs(hash(text))
        vec[(self._axis + 1) % self.dim] = ((h >> 0) & 0xFF) / 255.0
        vec[(self._axis + 2) % self.dim] = ((h >> 8) & 0xFF) / 255.0
        # renormalize
        norm = sum(v * v for v in vec) ** 0.5
        return [v / norm for v in vec]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed(t) for t in texts]


@pytest.fixture
def fake_embedder() -> FakeEmbedder:
    return FakeEmbedder(model_name="test-model-A", dim=8)


@pytest.fixture
def fake_embedder_b() -> FakeEmbedder:
    """A *different* model with the SAME dim — must not be treated as compatible."""
    return FakeEmbedder(model_name="test-model-B", dim=8)


@pytest.fixture
def tmp_db(tmp_path: Path) -> str:
    return str(tmp_path / "test.qdrant")


@pytest.fixture
def indexer(tmp_db: str):
    from scripts.kb.indexer import QdrantIndexer

    idx = QdrantIndexer(db_path=tmp_db, collection="test_docs", dim=8)
    yield idx
    idx.close()
