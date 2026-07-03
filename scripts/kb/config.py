"""Configuration helpers for the kb submodule (task 4.1).

Loads/saves the repo config.json and provides a DEFAULT_CONFIG constant.
No hard-coded paths: db_path/collection come from config.json.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional

CONFIG_FILENAME = "config.json"

DEFAULT_CONFIG: dict[str, Any] = {
    "embed_model": "sentence-transformers/paraphrase-MiniLM-L3-v2",
    "embed_dim": 384,
    "embed_source": "modelscope",
    "embed_base_url": "",
    "embed_api_key": "",
    "rerank_model": "flashrank",
    "rerank_source": "local",
    "rerank_base_url": "",
    "rerank_api_key": "",
    "db_path": "data/harmonyos.qdrant",
    "collection": "harmonyos_docs",
    "sidebars_dir": "sidebars",
    "endpoints": {},
    "query": {
        "default_top_k": 5,
        "bm25_weight": 0.3,
        "vector_weight": 0.7,
    },
    # B14/T026: 网页内容过期天数。30 天内重复访问同一 url 用缓存，不重新抓取。
    "content_expire_days": 30,
}


def load_config(path: str) -> Optional[dict[str, Any]]:
    """Load a JSON config file.

    Returns None if the file does not exist. Raises ValueError on malformed JSON
    so callers cannot silently swallow corruption (Rule 12: fail loud).
    """
    p = Path(path)
    if not p.exists():
        return None
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config {path}: {e}") from e


def save_config(cfg: dict[str, Any], path: str) -> None:
    """Write cfg to path as UTF-8 JSON."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def ensure_config(config_path: Optional[str] = None) -> Optional[dict[str, Any]]:
    """Load config.json from the current working directory (or override).

    Returns None when the file is missing — caller decides whether to fall back
    to DEFAULT_CONFIG or report an error.
    """
    if config_path is None:
        config_path = os.path.join(os.getcwd(), CONFIG_FILENAME)
    return load_config(config_path)
