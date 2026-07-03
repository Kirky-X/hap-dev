"""Unified CLI entrypoint for the kb submodule (task 4.18 + B7 link-auto/migrate).

Usage:
    python3 -m scripts.kb.cli <action> [options]

Actions:
    query                --question --top-k --doc-type --rerank
    build                --sidebars-dir
    merge                --db-a --db-b --out
    reindex              --force
    update-description   --id --description
    recommend-api        --doc-id                    (B19, 替代旧 update-links)
    link-auto            --threshold --max-per-doc     (B2)
    migrate-embed-model  [--model <name>]              (B1 migration)
    config               (print current config)

db_path / collection / sidebars_dir / embed_model all come from config.json —
no hard-coded paths (per spec). `--config` overrides the config file location;
otherwise the config.json in the current working directory is used, falling back
to DEFAULT_CONFIG when absent.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Optional

from .config import DEFAULT_CONFIG, ensure_config, load_config
from .embed import Embedder
from .indexer import QdrantIndexer
from .links import update_links
from .links_auto import auto_link
from .merge import merge as do_merge
from .query import query as do_query
from .reindex import reindex as do_reindex
from .sidebar_parser import parse_all_sidebars
from .update_description import update_description

ACTIONS = ("query", "build", "merge", "reindex", "update-description",
           "recommend-api", "link-auto", "migrate-embed-model", "config")


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

    ul = sub.add_parser("recommend-api",
                        help="call getRecommendInfo API and write bidirectional links (B19)")
    ul.add_argument("--doc-id", required=True,
                    help="source doc id (must already exist in the index)")
    ul.add_argument("--config", default=None)

    la = sub.add_parser("link-auto",
                        help="auto-link docs by vector cosine similarity (B2)")
    la.add_argument("--threshold", type=float, default=0.9,
                    help="cosine similarity above which two docs are linked")
    la.add_argument("--max-per-doc", type=int, default=10,
                    help="cap on each doc's link list")
    la.add_argument("--config", default=None)

    me = sub.add_parser("migrate-embed-model",
                        help="backfill embed_model field on legacy docs (B1)")
    me.add_argument("--model", default=None,
                    help="override the model name to stamp "
                         "(defaults to config.json's embed_model)")
    me.add_argument("--config", default=None)

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


def _run_recommend_api(args: argparse.Namespace) -> Any:
    """B19: 调用 getRecommendInfo API 建立 source doc 与推荐 docs 的双向 link。

    替代旧 _run_update_links（B19 破坏性变更：删除 markdown 解析，改用官方推荐 API）。
    embedder 从配置初始化（新 doc 入库时立即嵌入并盖章 embed_model）。
    """
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        linked = update_links(args.doc_id, idx, emb)
    finally:
        idx.close()
    out = {"linked": linked}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return linked


def _run_config(args: argparse.Namespace) -> Any:
    cfg = _load_cfg(args.config)
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return cfg


def _run_link_auto(args: argparse.Namespace) -> Any:
    """B2: auto-link docs by vector cosine similarity > threshold."""
    cfg = _load_cfg(args.config)
    idx = make_indexer(cfg)
    try:
        stats = auto_link(
            idx,
            threshold=args.threshold,
            max_per_doc=args.max_per_doc,
        )
    finally:
        idx.close()
    out = {
        "pairs_linked": stats["pairs_linked"],
        "docs_scanned": stats["docs_scanned"],
        "threshold": args.threshold,
        "max_per_doc": args.max_per_doc,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_migrate_embed_model(args: argparse.Namespace) -> Any:
    """B1 migration: stamp embed_model onto legacy docs that lack it.

    Reads the DB's current embed_model set:
      - if all docs have the same non-empty value → no-op (already migrated)
      - if all docs have empty embed_model (legacy) → stamp config.embed_model
      - if mixed → refuse (Run handler's stderr message explains recovery)
    """
    cfg = _load_cfg(args.config)
    target_model = args.model or cfg.get("embed_model", "")
    if not target_model:
        raise ValueError(
            "migrate-embed-model: no model to stamp — pass --model or set "
            "embed_model in config.json"
        )
    idx = make_indexer(cfg)
    try:
        docs = idx.list_all()
        if not docs:
            out = {"migrated": 0, "skipped": 0, "model": target_model, "note": "empty DB"}
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return out
        models = {d.get("embed_model", "") for d in docs}
        real_models = {m for m in models if m}
        if len(real_models) > 1:
            raise RuntimeError(
                f"migrate-embed-model: DB already contains mixed embed_models "
                f"{real_models!r} — contaminated, refusing to migrate. "
                f"Rebuild from sidebars: `python3 scripts/kb/build_db.py`."
            )
        if len(real_models) == 1 and next(iter(real_models)) != target_model:
            existing = next(iter(real_models))
            raise RuntimeError(
                f"migrate-embed-model: DB already stamped with {existing!r} "
                f"but config says {target_model!r}. Either revert config.json "
                f"to {existing!r}, or run `python3 scripts/kb/build_db.py` to "
                f"rebuild with {target_model!r}."
            )
        if len(real_models) == 1:
            # All docs already stamped with target_model — nothing to do
            out = {
                "migrated": 0, "skipped": len(docs),
                "model": target_model,
                "note": "all docs already have embed_model",
            }
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return out
        # All docs have empty embed_model (legacy) — stamp target_model
        migrated = 0
        for d in docs:
            idx.set_payload(d["id"], {"embed_model": target_model})
            migrated += 1
        out = {"migrated": migrated, "skipped": 0, "model": target_model}
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return out
    finally:
        idx.close()


_DISPATCH = {
    "query": _run_query,
    "build": _run_build,
    "merge": _run_merge,
    "reindex": _run_reindex,
    "update-description": _run_update_description,
    "recommend-api": _run_recommend_api,
    "link-auto": _run_link_auto,
    "migrate-embed-model": _run_migrate_embed_model,
    "config": _run_config,
}


def main(argv: Optional[list[str]] = None) -> Any:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = _DISPATCH[args.action]
    return handler(args)


if __name__ == "__main__":
    main()
