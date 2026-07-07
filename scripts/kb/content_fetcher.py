"""B16/B18: 抓取 HarmonyOS 文档 url 网页内容为 markdown + 过期检测。

fetch_content(url) 解析 url 提取 (object_id, catalog)，调用
scripts.search.detail.detail() 获取 doc 内容（HTML 已转 Markdown），返回 str。

is_content_expired(doc, expire_days): 检查 doc.updated_at 是否距今 > expire_days。
should_refresh_content(doc, new_context): 对比 new_context sha1 与 doc.context sha1。
touch_updated_at(doc_id, indexer): 只更新 updated_at，不改 context/向量/hash。

不支持的 catalog 路径 raise ValueError；detail() 返回 {'error': ...} 时 raise
ValueError（fail-loud，不静默返回空字符串）。

URL 路径片段 → catalog 映射覆盖 9 个 HarmonyOS 文档 catalog。HarmonyOS 文档 url
形如 ``https://developer.huawei.com/consumer/cn/doc/<catalog>/<object_id>``，
catalog 在 path 倒数第二段，object_id 在最后一段。
"""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlparse

from scripts.search.detail import detail

# url path 中的 catalog 关键字 → detail() 期望的 catalog 名称。
# 当前是一一映射；如果将来 detail() 接受别名，可在此扩展。
URL_PATH_TO_CATALOG: dict[str, str] = {
    "harmonyos-guides": "harmonyos-guides",
    "harmonyos-references": "harmonyos-references",
    "harmonyos-faqs": "harmonyos-faqs",
    "harmonyos-design": "harmonyos-design",
    "harmonyos-atomic": "harmonyos-atomic",
    "harmonyos-agc": "harmonyos-agc",
    "harmonyos-app": "harmonyos-app",
    "harmonyos-best-practices": "harmonyos-best-practices",
    "harmonyos-architecture": "harmonyos-architecture",
}

# 默认过期天数（D6/D9）。30 天内重复访问同一 url 用缓存，不重新抓取。
DEFAULT_EXPIRE_DAYS = 30

# HarmonyOS 官方文档站点 host 白名单（SSRF 防护）。
# fetch_content 只信任这两个 host；其余一律拒绝。即便 detail() 实际只请求
# 固定的 DETAIL_HOST，url 的 host 仍必须语义合法 —— 拒绝攻击者用合法
# catalog 路径段伪装的非法 host（如 ``https://evil.com/harmonyos-guides/...``）。
# 用 frozenset 避免误改；hostname 经 urlparse 规范化为小写、剥离端口。
ALLOWED_HOSTS: frozenset[str] = frozenset(
    {
        "developer.huawei.com",
        "device.harmonyos.com",
    }
)


def _now_iso() -> str:
    """当前 UTC 时间的 ISO8601 字符串（与 sidebar_parser._now_iso 一致）。"""
    return datetime.now(timezone.utc).isoformat()


def extract_object_id_and_catalog(url: str) -> tuple[str, str]:
    """从 HarmonyOS 文档 url 提取 (object_id, catalog)。

    url 形如 ``https://developer.huawei.com/consumer/cn/doc/<catalog>/<object_id>``。
    catalog 必须在 URL_PATH_TO_CATALOG 白名单内，否则 raise ValueError。

    Args:
        url: HarmonyOS 文档 url。

    Returns:
        (object_id, catalog) 二元组。

    Raises:
        ValueError: url 无 path、path 段数不足、或 catalog 不在白名单。
    """
    if not url:
        raise ValueError("extract_object_id_and_catalog: url 不能为空")

    path = urlparse(url).path
    # 末尾斜杠剥离后再 split，避免空尾段
    segments = [s for s in path.rstrip("/").split("/") if s]
    if len(segments) < 2:
        raise ValueError(
            f"extract_object_id_and_catalog: url path 段数不足，无法解析 catalog/object_id: {url!r}"
        )

    # path 最后两段：[..., catalog, object_id]
    catalog_key = segments[-2]
    object_id = segments[-1]
    if catalog_key not in URL_PATH_TO_CATALOG:
        raise ValueError(
            f"extract_object_id_and_catalog: 不支持的 catalog 路径段 {catalog_key!r} "
            f"(url={url!r}); expected one of {sorted(URL_PATH_TO_CATALOG.keys())}"
        )
    return object_id, URL_PATH_TO_CATALOG[catalog_key]


def _validate_host(url: str) -> str:
    """校验 url 的 host 在 HarmonyOS 文档白名单内；返回规范化 host。

    defense-in-depth：``detail()`` 实际只请求固定 DETAIL_HOST，但 url 的 host
    仍必须语义合法 —— 拒绝攻击者用合法 catalog 路径段伪装的非法 host
    （如 ``https://evil.com/harmonyos-guides/<id>``）。

    Args:
        url: 待校验的 HarmonyOS 文档 url。

    Returns:
        规范化的小写 host（``urlparse().hostname`` 已剥离端口/大小写）。

    Raises:
        ValueError: host 缺失或不在 ``ALLOWED_HOSTS`` 白名单。
    """
    host = urlparse(url).hostname
    if host is None or host not in ALLOWED_HOSTS:
        raise ValueError(
            f"fetch_content: url host {host!r} 不在允许白名单 {sorted(ALLOWED_HOSTS)}；"
            f"仅允许 HarmonyOS 官方文档站点（SSRF 防护）。url={url!r}"
        )
    return host


def fetch_content(url: str) -> str:
    """抓取 url 对应的 HarmonyOS 文档内容（markdown 字符串）。

    Args:
        url: HarmonyOS 文档 url。

    Returns:
        doc 的 markdown 内容（非空 str）。如果 detail() 返回空 content，
        仍返回空 str（不视为错误——某些 doc 可能内容为空但抓取成功）。

    Raises:
        ValueError: url 解析失败（catalog 未知）、host 不在白名单（SSRF）、
            或 detail() 返回 error。
    """
    object_id, catalog = extract_object_id_and_catalog(url)
    _validate_host(url)  # SSRF 防护：host 必须在 HarmonyOS 官方白名单
    result = detail(object_id, catalog)
    if "error" in result:
        raise ValueError(f"fetch_content: detail 抓取失败: {result['error']}")
    return result.get("content", "") or ""


def is_content_expired(
    doc: dict[str, Any], expire_days: int = DEFAULT_EXPIRE_DAYS
) -> bool:
    """检查 doc 的 context 是否过期（updated_at 距今 > expire_days）。

    Args:
        doc: doc dict，必须含 ``updated_at`` 字段（ISO8601 字符串）。
        expire_days: 过期阈值天数，默认 30。

    Returns:
        True 若 updated_at 距今 > expire_days 天；False 若 <= expire_days。

    Raises:
        ValueError: updated_at 字段缺失或无法解析（fail-loud）。
    """
    updated_at = doc.get("updated_at")
    if not updated_at:
        raise ValueError("is_content_expired: doc 缺少 updated_at 字段")

    # fromisoformat 支持 +00:00 时区后缀；如果带 'Z' 后缀需替换为 +00:00
    ts_str = (
        updated_at.replace("Z", "+00:00") if updated_at.endswith("Z") else updated_at
    )
    try:
        updated_dt = datetime.fromisoformat(ts_str)
    except ValueError as exc:
        raise ValueError(
            f"is_content_expired: updated_at 无法解析为 ISO8601: {updated_at!r}"
        ) from exc

    # 如果 updated_at 是 naive datetime（无时区），假设为 UTC
    if updated_dt.tzinfo is None:
        updated_dt = updated_dt.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    age = now - updated_dt
    return age.days > expire_days


def should_refresh_content(doc: dict[str, Any], new_context: str) -> bool:
    """对比 new_context 的 sha1 与 doc.context 的 sha1。

    一致 → 网页没变，只需 touch_updated_at（节省重新总结 description 的 LLM 调用）。
    不一致 → 网页变了，需要全量更新（context + description + 向量 + hash + links）。

    Args:
        doc: doc dict，含 ``context`` 字段（可能为 ""）。
        new_context: 重新抓取的网页内容。

    Returns:
        True 若 sha1 不同（需要刷新）；False 若 sha1 相同（无需刷新）。
    """
    old_hash = hashlib.sha1((doc.get("context") or "").encode("utf-8")).hexdigest()
    new_hash = hashlib.sha1((new_context or "").encode("utf-8")).hexdigest()
    return old_hash != new_hash


def touch_updated_at(doc_id: str, indexer: Any) -> None:
    """只更新 doc 的 updated_at 字段，不改 context/向量/hash/description。

    用于 should_refresh_content 返回 False 的场景：网页没变，但 updated_at 已
    过期，刷一下时间戳避免下次 is_content_expired 误判。

    Args:
        doc_id: 目标 doc id。
        indexer: QdrantIndexer（或兼容）实例。

    Raises:
        KeyError: doc 不存在（fail-loud）。set_payload 内部已校验白名单，
            updated_at 在 PAYLOAD_FIELDS 内，不会被拒。
    """
    # 检查 doc 是否存在（fail-loud，避免 set_payload 静默失败）
    if indexer.get(doc_id) is None:
        raise KeyError(f"touch_updated_at: doc_id not in index: {doc_id}")
    indexer.set_payload(doc_id, {"updated_at": _now_iso()})
