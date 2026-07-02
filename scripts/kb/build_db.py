"""One-shot prebuild script for the HarmonyOS knowledge base (task 7.1).

Usage:
    python3 scripts/kb/build_db.py [--config CONFIG] [--sidebars-dir DIR]

Reads ``config.json`` (or DEFAULT_CONFIG when absent), parses the 9 sidebar
files in ``sidebars_dir``, builds a fresh Qdrant local-mode index at
``db_path`` using the configured ``embed_model``, and prints a summary of the
result (per-doc-type counts, total vectors, on-disk size of the DB).

This is the script users invoke to (re)generate the prebuilt
``data/harmonyos.qdrant`` shipped with the skill. The default config uses
``sentence-transformers/paraphrase-MiniLM-L3-v2`` via ModelScope; switching
``embed_model`` in ``config.json`` then re-running this script refreshes all
vectors (see also ``reindex.py`` for hash-delta re-embedding).

Note: the user's original spec named the model ``paraphrase-MiniLM-L3-v2+``
(with a trailing ``+``), but that suffix is invalid for both HuggingFace repo
ids and ModelScope — the actual published model is ``paraphrase-MiniLM-L3-v2``
(no ``+``). ``config.json`` and ``DEFAULT_CONFIG`` use the correct name.

The script reuses ``cli.make_embedder`` / ``cli.make_indexer`` /
``sidebar_parser.parse_all_sidebars`` so behaviour stays consistent with
``python3 -m scripts.kb.cli build`` — single source of truth (Rule 8).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

# Allow both ``python3 -m scripts.kb.build_db`` and direct
# ``python3 scripts/kb/build_db.py`` invocation by ensuring the project
# root (hap-dev) is on sys.path when run as a plain script.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.kb import cli  # noqa: E402
from scripts.kb.config import DEFAULT_CONFIG, ensure_config, load_config  # noqa: E402
from scripts.kb.sidebar_parser import parse_all_sidebars  # noqa: E402


def _format_size(n: int) -> str:
    """Human-readable byte count (KB / MB)."""
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.2f} MB"


def _dir_size(path: str) -> int:
    """Total bytes of all files under ``path`` (recursive). 0 if missing."""
    p = Path(path)
    if not p.exists():
        return 0
    if p.is_file():
        return p.stat().st_size
    total = 0
    for root, _dirs, files in os.walk(p):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def _load_cfg(config_arg: str | None) -> dict[str, Any]:
    """Load config from explicit path, cwd config.json, or DEFAULT_CONFIG."""
    if config_arg:
        cfg = load_config(config_arg)
        if cfg is None:
            raise FileNotFoundError(f"config file not found: {config_arg}")
        return cfg
    cfg = ensure_config()
    if cfg is None:
        return dict(DEFAULT_CONFIG)
    return cfg


def build_database(config_arg: str | None = None,
                   sidebars_override: str | None = None) -> dict[str, Any]:
    """Build the index and return a stats dict (also used by tests)."""
    cfg = _load_cfg(config_arg)
    sidebars_dir = sidebars_override or cfg.get("sidebars_dir", "sidebars")
    db_path = cfg["db_path"]

    # Parse sidebars first — fail loud before touching the embedder (Rule 12).
    docs = parse_all_sidebars(sidebars_dir)
    if not docs:
        raise RuntimeError(
            f"no docs parsed from sidebars_dir={sidebars_dir!r} — "
            "every sidebar produced 0 records; refusing to build an empty index"
        )

    emb = cli.make_embedder(cfg)
    idx = cli.make_indexer(cfg)
    try:
        idx.build(docs, emb)
        counts = idx.count_by_type()
        total = idx.count()
    finally:
        idx.close()

    size_bytes = _dir_size(db_path)
    stats = {
        "built": len(docs),
        "total_vectors": total,
        "counts": counts,
        "db_path": db_path,
        "db_size_bytes": size_bytes,
        "db_size_human": _format_size(size_bytes),
        "embed_model": cfg.get("embed_model", ""),
        "collection": cfg.get("collection", ""),
    }
    return stats


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="build_db.py",
        description="One-shot prebuild of the HarmonyOS Qdrant knowledge base.",
    )
    p.add_argument(
        "--config", default=None,
        help="path to config.json (defaults to ./config.json or DEFAULT_CONFIG)",
    )
    p.add_argument(
        "--sidebars-dir", default=None,
        help="override sidebars_dir from config",
    )
    args = p.parse_args(argv)

    print(f"[build_db] loading config…", file=sys.stderr)
    try:
        stats = build_database(args.config, args.sidebars_dir)
    except FileNotFoundError as e:
        print(f"[build_db] ERROR: {e}", file=sys.stderr)
        return 2
    except RuntimeError as e:
        print(f"[build_db] ERROR: {e}", file=sys.stderr)
        return 3

    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print(
        f"[build_db] done: {stats['total_vectors']} vectors across "
        f"{len(stats['counts'])} doc types, "
        f"DB size {stats['db_size_human']} at {stats['db_path']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
