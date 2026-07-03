"""Bidirectional link extraction via getRecommendInfo API (B19 重写).

update_links(doc_id, indexer, embedder) 三参（embedder 必传）：
1. 读 source doc，调用 recommend.get_recommendations(source.url) 获取推荐列表
2. 对每个推荐 url：
   a. 计算 target_id = sha1(url)
   b. 自链接跳过
   c. target 已在 DB → 加双向 link（不重算向量）
   d. target 不在 DB → fetch_content(url) 抓取 → 构造新 doc → indexer.upsert
      嵌入并盖章 embed_model → 加双向 link
3. 写入双向 link + 更新 updated_at

embedder=None raise ValueError（fail-loud，禁止零向量污染向量空间）。
API 失败 raise ValueError（fail-loud，不静默返回空列表）。

B19 破坏性变更：删除所有 markdown 解析正则（RELATED_HEADING_RE 等）和
_extract_related_block/_extract_urls——华为官方推荐 API 替代网页抓取。
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any

from .content_fetcher import fetch_content
from .query import _check_model_compatibility
from .recommend import get_recommendations
from .sidebar_parser import NO_DESCRIPTION, _make_content_hash


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _url_to_id(url: str) -> str:
    """url → doc_id（与 sidebar_parser._make_id 一致：sha1(url)）。"""
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def _build_new_target_doc(
    url: str,
    name: str,
    context: str,
    now: str,
) -> dict[str, Any]:
    """构造一个新 doc dict（用于 API 推荐但 DB 中不存在的 target）。

    字段填充策略（design D7）：
      - id: sha1(url)（与 sidebar_parser 一致，保证幂等）
      - title: API 返回的 name
      - doc_type: "api-recommend"（区分来源）
      - description: NO_DESCRIPTION（agent 后续 update_content 填充）
      - context: fetch_content 抓取的网页原始内容
      - embed_model: ""（indexer.upsert 会盖章为 embedder.model_name）
    """
    doc_id = _url_to_id(url)
    return {
        "id": doc_id,
        "title": name,
        "doc_type": "api-recommend",
        "url": url,
        "description": NO_DESCRIPTION,
        "links": [],
        "created_at": now,
        "updated_at": now,
        "content_hash": _make_content_hash(
            name, url, "api-recommend", NO_DESCRIPTION, [], context=context,
        ),
        "embed_model": "",
        "context": context,
    }


def _add_bidirectional_link(
    source_doc: dict[str, Any],
    target_doc: dict[str, Any],
) -> bool:
    """在 source_doc 和 target_doc 之间加双向 link（如果不存在）。

    返回 True 若任一方向新增了 link；False 若两个方向都已存在（幂等）。
    """
    added = False
    if target_doc["id"] not in source_doc["links"]:
        source_doc["links"].append(target_doc["id"])
        added = True
    if source_doc["id"] not in target_doc["links"]:
        target_doc["links"].append(source_doc["id"])
        added = True
    return added


def update_links(
    doc_id: str,
    indexer: Any,
    embedder: Any,
) -> list[str]:
    """通过 API 获取推荐并建立双向 link。

    Args:
        doc_id: source doc id。
        indexer: QdrantIndexer（或兼容）实例。
        embedder: 嵌入器（必传）。新 doc 入库时立即用 embedder 嵌入并盖章
            embed_model；embedder 为 None 时 raise ValueError（fail-loud，
            禁止零向量污染向量空间——会导致 links_auto 余弦计算分母为零）。

    Returns:
        linked doc_ids 列表（已建立双向 link 的 target ids）。

    Raises:
        KeyError: source doc_id 不存在于索引（fail-loud）。
        ValueError: embedder 为 None；API 调用失败；fetch_content 失败。
    """
    if embedder is None:
        raise ValueError(
            "update_links: embedder 不能为 None——新 doc 入库需立即嵌入并盖章 "
            "embed_model，零向量会污染 links_auto 余弦计算（分母为零）"
        )
    _check_model_compatibility(indexer, embedder)

    source = indexer.get(doc_id)
    if source is None:
        raise KeyError(f"update_links: source doc_id not in index: {doc_id}")

    # 调用 API 获取推荐列表（失败时 get_recommendations 自身 raise ValueError）
    recommendations = get_recommendations(source["url"])

    now = _now_iso()
    linked: list[str] = []
    source_dirty = False

    for rec in recommendations:
        target_url = rec["url"]
        target_id = _url_to_id(target_url)

        # 自链接跳过
        if target_id == doc_id:
            continue

        target = indexer.get(target_id)
        if target is None:
            # target 不在 DB → 抓取 + upsert 新 doc
            # fetch_content 对不支持的 catalog 路径（如 games-guides）raise
            # ValueError——recommend API 会返回非 HarmonyOS 文档，跳过这些推荐
            # 而非让整个操作失败（Rule 12：跳过原因在 stderr 输出，不静默吞掉）
            try:
                context = fetch_content(target_url)
            except ValueError as e:
                import sys
                print(f"update_links: skip {target_url} — {e}",
                      file=sys.stderr)
                continue
            target = _build_new_target_doc(
                url=target_url,
                name=rec.get("name") or target_url,
                context=context,
                now=now,
            )
            # upsert 重算向量（从 title，因 description == NO_DESCRIPTION）并盖章
            # embed_model；payload（含 context）也一并写入
            indexer.upsert(target, embedder)

        # 加双向 link（幂等）
        if _add_bidirectional_link(source, target):
            source_dirty = True
            # target 的 links 已变化 → 持久化
            # B23: content_hash 必须与 links 同步刷新，否则 reindex(force=False)
            # 误判 doc 未变化而跳过重嵌入（即使向量已 stale）
            target_hash = _make_content_hash(
                target["title"], target["url"], target["doc_type"],
                target.get("description", NO_DESCRIPTION),
                target["links"],
                context=target.get("context", ""),
            )
            indexer.set_payload(target["id"], {
                "links": target["links"],
                "updated_at": now,
                "content_hash": target_hash,
            })
        linked.append(target["id"])

    # 持久化 source 的 links（如果变化）
    if source_dirty:
        source_hash = _make_content_hash(
            source["title"], source["url"], source["doc_type"],
            source.get("description", NO_DESCRIPTION),
            source["links"],
            context=source.get("context", ""),
        )
        indexer.set_payload(doc_id, {
            "links": source["links"],
            "updated_at": now,
            "content_hash": source_hash,
        })

    return linked
