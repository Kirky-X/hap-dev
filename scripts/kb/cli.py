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
from pathlib import Path
from typing import Any, Optional

# Allow both ``python3 -m scripts.kb.cli`` and direct
# ``python3 <skill_root>/scripts/kb/cli.py`` invocation by ensuring the
# skill root (hap-dev) is on sys.path when run as a plain script.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.kb.config import DEFAULT_CONFIG, ensure_config, load_config
from scripts.kb.content_fetcher import (
    DEFAULT_EXPIRE_DAYS,
    fetch_content,
    is_content_expired,
)
from scripts.kb.embed import Embedder
from scripts.kb.indexer import QdrantIndexer
from scripts.kb.links import update_links
from scripts.kb.links_auto import auto_link
from scripts.kb.merge import merge as do_merge
from scripts.kb.query import query as do_query
from scripts.kb.reindex import reindex as do_reindex
from scripts.kb.sidebar_parser import parse_all_sidebars
from scripts.kb.update_content import update_content
from scripts.kb.update_description import update_description

ACTIONS = ("query", "build", "merge", "reindex", "update-description",
           "recommend-api", "link-auto", "migrate-embed-model", "config",
           "fetch-content", "update-content", "migrate-context",
           "refresh-expired", "fetch-and-update")


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
    """Load config and merge with DEFAULT_CONFIG (B14/T026).

    旧 config.json 可能缺新字段（如 content_expire_days）——合并确保
    新字段在旧 config 上也有默认值，避免 KeyError。
    """
    if config_arg:
        cfg = load_config(config_arg)
        if cfg is None:
            raise FileNotFoundError(f"config file not found: {config_arg}")
    else:
        cfg = ensure_config()
        if cfg is None:
            return dict(DEFAULT_CONFIG)
    # 浅合并：DEFAULT_CONFIG 提供默认值，cfg 覆盖（cfg 的值优先）
    merged = dict(DEFAULT_CONFIG)
    merged.update(cfg)
    return merged


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

    # B14/T028: 4 个新子命令（recommend-api 已在 T022 实现）
    fc = sub.add_parser("fetch-content",
                        help="fetch a single url's markdown content (B16)")
    fc.add_argument("--url", required=True,
                    help="HarmonyOS doc url to fetch")
    fc.add_argument("--config", default=None)

    uc = sub.add_parser("update-content",
                        help="update doc context + description + vector + hash (B17)")
    uc.add_argument("--doc-id", required=True)
    uc.add_argument("--description", required=True,
                    help="new description (agent-generated summary)")
    uc.add_argument("--context-file", default=None,
                    help="path to a file containing the fetched markdown content; "
                         "if absent, reads from stdin")
    uc.add_argument("--config", default=None)

    mc = sub.add_parser("migrate-context",
                        help="backfill context field on legacy docs (B14 migration)")
    mc.add_argument("--config", default=None)

    # T-verify: 一体化增量更新——抓取正文(context) + 回填 description + 向量。
    # 禁止只回填 description 而漏掉 context（Rule 12/需求：增量必须带完整页面内容）。
    # 不支持的 catalog 显式报错，不写半截数据。
    fau = sub.add_parser(
        "fetch-and-update",
        help="fetch url content + backfill context+description+vector atomically (T-verify)",
    )
    fau.add_argument("--url", required=True, help="HarmonyOS doc url to fetch")
    fau.add_argument("--doc-id", required=True, help="target doc id in the index")
    fau.add_argument("--description", default=None,
                     help="≤200字描述；省略时从抓取正文自动生成首段摘要")
    fau.add_argument("--config", default=None)

    re = sub.add_parser("refresh-expired",
                        help="list docs whose content has expired (B18, does NOT refresh)")
    re.add_argument("--expire-days", type=int, default=None,
                    help="override content_expire_days from config")
    re.add_argument("--config", default=None)

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
    return out


def _run_fetch_content(args: argparse.Namespace) -> Any:
    """B16: 抓取单个 url 的 markdown 内容并输出。"""
    cfg = _load_cfg(args.config)
    # fetch_content 不需要 indexer/embedder，只调用 detail API
    content = fetch_content(args.url)
    out = {"content": content}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _auto_summary(content: str, fallback: str, max_len: int = 200) -> str:
    """从抓取正文自动生成 ≤max_len 字的描述（无需 LLM，确定性逻辑）。

    去掉 markdown 标题标记/#、空行、列表符号（-/*/#）等无意义片段，取第一个
    有意义的句子/段落作为摘要。若正文无可提取内容则用 fallback（url）。
    """
    import re

    # 导航/目录等无实质内容的噪声片段，整句跳过
    NOISE_HINTS = ("目录", "chevron", "table of contents", "toc", "上一篇",
                   "下一篇", "previous", "next", "首页", "目录chevron")
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            continue
        # strip 常见 markdown 噪声：标题 #、列表 -/*、引用 >
        cleaned = re.sub(r"^[#>\-\*\s]+", "", line).strip()
        # 跳过过短或无实质内容（如纯 "list"、目录锚点、噪声提示）
        if len(cleaned) < 8 or any(h in cleaned.lower() for h in NOISE_HINTS):
            continue
        # 取第一句（中英文句号/换行截断）
        sent = re.split(r"[。.!?！？\n]", cleaned)[0].strip()
        if len(sent) >= 8 and not any(h in sent.lower() for h in NOISE_HINTS):
            return sent[:max_len]
    return fallback[:max_len]


def _run_fetch_and_update(args: argparse.Namespace) -> Any:
    """T-verify: 抓取 url 正文 → 原子回填 context+description+向量。

    禁止只回填 description：fetch-and-update 必须拿到真实 context（页面正文）。
    若 fetch_content 失败（catalog 不支持 / url 失效），显式 raise，不写半截数据。
    description 省略时从正文首段自动生成 ≤200 字摘要（截断保护）。
    """
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)
    try:
        # 1. 抓取真实正文（fail-loud：catalog 不支持 / 网络失败都会 raise）
        content = fetch_content(args.url)
        if not content or not content.strip():
            raise ValueError(
                f"fetch-and-update: 抓取到空正文，拒绝写半截数据 (url={args.url!r})"
            )
        # 2. description：优先用显式传入，否则从正文自动生成首段摘要
        description = (args.description or "").strip()
        if not description:
            description = _auto_summary(content, fallback=args.url)
        # 截断保护：description ≤ 200 字
        if len(description) > 200:
            description = description[:197].rstrip() + "…"
        # 3. 原子写入 context + description + 向量 + hash
        update_content(args.doc_id, content, description, idx, emb)
    finally:
        idx.close()
    out = {"updated": args.doc_id, "context_len": len(content), "description": description}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_update_content(args: argparse.Namespace) -> Any:
    """B17: 更新 doc 的 context + description + 向量 + hash。

    context 读取顺序：--context-file > stdin，两者都无时 raise ValueError。
    """
    cfg = _load_cfg(args.config)
    emb = make_embedder(cfg)
    idx = make_indexer(cfg)

    # context 优先级：--context-file > stdin
    if args.context_file:
        from pathlib import Path
        ctx_path = Path(args.context_file)
        if not ctx_path.exists():
            raise FileNotFoundError(f"context file not found: {args.context_file}")
        context = ctx_path.read_text(encoding="utf-8")
    else:
        # 回退 stdin
        context = sys.stdin.read()
    context = context.strip()
    if not context:
        raise ValueError(
            "update-content: context 不能为空——提供 --context-file 或通过 stdin 输入"
        )

    try:
        update_content(args.doc_id, context, args.description, idx, emb)
    finally:
        idx.close()
    out = {"updated": args.doc_id}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_migrate_context(args: argparse.Namespace) -> Any:
    """B14 迁移：给缺 context 字段的 doc 写 ""。

    Idempotent：已有 context 字段（无论是否为空）的 doc 跳过。用 iter_raw_payloads
    检查原始 payload 字段是否存在——_payload_from 会把缺失的 context 默认成 ""，
    无法区分"字段缺失"和"字段为空"。

    性能：用 Qdrant 批量 set_payload（一次写所有缺字段的 point），避免逐个
    idx.set_payload（每个都要 get() scroll 查询存在性，710 docs 会超时）。
    """
    cfg = _load_cfg(args.config)
    idx = make_indexer(cfg)
    try:
        raw_items = idx.iter_raw_payloads()
        migrated_pids: list[int] = []
        skipped = 0
        for pid, raw in raw_items:
            if "context" in raw:
                skipped += 1
                continue
            migrated_pids.append(pid)
        # 批量写 context=""（Qdrant set_payload 支持一次写多个 point）
        BATCH = 256
        for i in range(0, len(migrated_pids), BATCH):
            batch = migrated_pids[i:i + BATCH]
            idx.client.set_payload(
                collection_name=idx.collection,
                payload={"context": ""},
                points=batch,
            )
    finally:
        idx.close()
    out = {"migrated": len(migrated_pids), "skipped": skipped}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def _run_refresh_expired(args: argparse.Namespace) -> Any:
    """B18: 扫描过期 doc 仅输出 doc_id 列表（不执行刷新）。

    刷新由 agent 据此手动执行：fetch_content → should_refresh_content →
    touch_updated_at 或 update_content + update_links。
    """
    cfg = _load_cfg(args.config)
    expire_days = args.expire_days if args.expire_days is not None else cfg.get(
        "content_expire_days", DEFAULT_EXPIRE_DAYS,
    )
    idx = make_indexer(cfg)
    try:
        docs = idx.list_all()
        expired_ids = [
            doc["id"] for doc in docs
            if is_content_expired(doc, expire_days=expire_days)
        ]
    finally:
        idx.close()
    out = {"expired_doc_ids": expired_ids, "expire_days": expire_days}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


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
    # B14/T028: 4 个新子命令
    "fetch-content": _run_fetch_content,
    "fetch-and-update": _run_fetch_and_update,
    "update-content": _run_update_content,
    "migrate-context": _run_migrate_context,
    "refresh-expired": _run_refresh_expired,
}


def main(argv: Optional[list[str]] = None) -> Any:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = _DISPATCH[args.action]
    return handler(args)


if __name__ == "__main__":
    main()
