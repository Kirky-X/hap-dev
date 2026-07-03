"""B16: 抓取 HarmonyOS 文档 url 网页内容为 markdown。

fetch_content(url) 解析 url 提取 (object_id, catalog)，调用
scripts.search.detail.detail() 获取 doc 内容（HTML 已转 Markdown），返回 str。

不支持的 catalog 路径 raise ValueError；detail() 返回 {'error': ...} 时 raise
ValueError（fail-loud，不静默返回空字符串）。

URL 路径片段 → catalog 映射覆盖 9 个 HarmonyOS 文档 catalog。HarmonyOS 文档 url
形如 ``https://developer.huawei.com/consumer/cn/doc/<catalog>/<object_id>``，
catalog 在 path 倒数第二段，object_id 在最后一段。
"""
from __future__ import annotations

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


def fetch_content(url: str) -> str:
    """抓取 url 对应的 HarmonyOS 文档内容（markdown 字符串）。

    Args:
        url: HarmonyOS 文档 url。

    Returns:
        doc 的 markdown 内容（非空 str）。如果 detail() 返回空 content，
        仍返回空 str（不视为错误——某些 doc 可能内容为空但抓取成功）。

    Raises:
        ValueError: url 解析失败（catalog 未知）或 detail() 返回 error。
    """
    object_id, catalog = extract_object_id_and_catalog(url)
    result = detail(object_id, catalog)
    if "error" in result:
        raise ValueError(f"fetch_content: detail 抓取失败: {result['error']}")
    return result.get("content", "") or ""
