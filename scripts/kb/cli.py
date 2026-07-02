"""Unified CLI entrypoint for the kb submodule (task 4.18).

Usage:
    python3 -m scripts.kb.cli <action> [options]

Actions:
    query                --question --top-k --doc-type --rerank
    build                --sidebars-dir
    merge                --db-a --db-b --out
    reindex              --force
    update-description   --id --description
    update-links         --id --content
    config               (print current config)

db_path / collection / sidebars_dir / embed_model all come from config.json —
no hard-coded paths (per spec). `--config` overrides the config file location;
otherwise the config.json in the current working directory is used, falling back
to DEFAULT_CONFIG when absent.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Optional

from .config import DEFAULT_CONFIG, ensure_config, load_config
from .embed import Embedder
from .indexer import QdrantIndexer
from .links import update_links
from .merge import merge as do_merge
from .query import query as do_query
from .reindex import reindex as do_reindex
from .sidebar_parser import parse_all_sidebars
from .update_description import update_description

ACTIONS = ("query", "build", "merge", "reindex", "update-description",
           "update-links", "config")


# ---- factories (kept module-level so tests can monkeypatch them) -----------

def make_embedder(cfg: dict[str, Any]) -> Embedder:
    return Embedder(
        cfg["embed_model"],
        base_url=cfg.get("embed_base_url", ""),
        api_key=cfg.get("embed_api_key", ""),
        source=cfg.get("embed_source", ""),
    )


def make_indexer(cfg: dict[str, Any]) -> QdrantIndexer:
    return QdrantIndexer(
        db_path=cfg["db_path"],
        collection=cfg["collection"],
        dim=cfg.get("embed_dim", 384),
    )


def _load_cfg(config_arg: Optional[str]) -> dict[str, Any]:
    if config_arg:
        cfg = load_config(config_arg)
        if cfg is None:
            raise FileNotFoundError(f"config file not found: {config_arg}")
        return cfg
    cfg = ensure_config()
    if cfg is None:
        return dict(DEFAULT_CONFIG)
    return cfg


# ---- argument parser -------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="scripts.kb.cli",
        description="HarmonyOS local Qdrant knowledge-base tool",
    )
    sub = p.add_subparsers(dest="action", required=True)

    q = sub.add_parser("query", help="hybrid vector+BM25 search")
    q.add_argument("--question", required=True)
    q.add_argument("--top-k", type=int, default=None)
    q.add_argument("--doc-type", default=None)
    q.add_argument("--rerank", action="store_true")
    q.add_argument("--config", default=None)

    b = sub.add_parser("build", help="parse sidebars and build the index")
    b.add_argument("--sidebars-dir", default=None,
                   help="override sidebars_dir from config")
    b.add_argument("--config", default=None)

    m = sub.add_parser("merge", help="merge two DBs into a new one")
    m.add_argument("--db-a", required=True)
    m.add_argument("--db-b", required=True)
    m.add_argument("--out", required=True)
    m.add_argument("--config", default=None)

    r = sub.add_parser("reindex", help="recompute embeddings")
    r.add_argument("--force", action="store_true")
    r.add_argument("--config", default=None)

    ud = sub.add_parser("update-description", help="backfill a doc description")
    ud.add_argument("--id", required=True)
    ud.add_argument("--description", required=True)
    ud.add_argument("--config", default=None)

    ul = sub.add_parser("update-links", help="extract & write bidirectional links")
    ul.add_argument("--id", required=True)
    ul.add_argument("--content", required=True,
                    help="doc body markdown, or a path to a file containing it")
    ul.add_argument("--config", default=None)

    c = sub.add_parser("config", help="print the effective config")
    c.add_argument("--config", default=None)
    return p


# ---- action handlers -------------------------------------------------------

def _run_query(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        top_k = args.top_k if args.top_k is not None else cfg.get("query", {}).get("default_top_k", 5)
        results = do_query(args.question, idx, emb, top_k=top_k,
                           doc_type=args.doc_type, rerank=args.rerank)
    finally:
        idx.close()
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return results


def _run_build(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    sidebars_dir = args.sidebars_dir or cfg.get("sidebars_dir", "sidebars")
    docs = parse_all_sidebars(sidebars_dir)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        idx.build(docs, emb)
        counts = idx.count_by_type()
    finally:
        idx.close()
    out = {"built": len(docs), "counts": counts}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_merge(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    res = do_merge(args.db_a, args.db_b, args.out, cfg["collection"],
                   dim=cfg.get("embed_dim", 384))
    print(json.dumps(res, ensure_ascii=False, indent=2))
    if res["needs_reindex_count"] > 0:
        print(f"NOTE: {res['needs_reindex_count']} docs had description changes — "
              f"run `reindex --force` on {args.out} to refresh their vectors.",
              file=sys.stderr)
    return res


def _run_reindex(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        n = do_reindex(idx, emb, force=args.force)
    finally:
        idx.close()
    out = {"reindexed": n}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_update_description(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        doc = update_description(args.id, args.description, idx, emb)
    finally:
        idx.close()
    out = {"updated": args.id}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return doc


def _run_update_links(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    idx = make_indexer(cfg)
    try:
        content = args.content
        if os.path.exists(content):
            with open(content, encoding="utf-8") as f:
                content = f.read()
        linked = update_links(args.id, content, idx)
    finally:
        idx.close()
    out = {"linked": linked}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return linked


def _run_config(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return cfg


_DISPATCH = {
    "query": _run_query,
    "build": _run_build,
    "merge": _run_merge,
    "reindex": _run_reindex,
    "update-description": _run_update_description,
    "update-links": _run_update_links,
    "config": _run_config,
}


def main(argv: Optional[list[str]] = None) -> Any:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = _DISPATCH[args.action]
    return handler(args)


if __name__ == "__main__":
    main()
