"""B16: content_fetcher.py 抓取 url 网页内容为 markdown (Red phase).

fetch_content(url) 解析 url 提取 object_id 和 catalog，调用
scripts.search.detail.detail() 获取 doc 内容（HTML→Markdown），返回 str。

不支持的 catalog 路径 raise ValueError；detail() 返回 error 时 raise
ValueError（fail-loud，不静默返回空字符串）。
"""
from __future__ import annotations

from unittest.mock import patch

import pytest

from scripts.kb.content_fetcher import (
    URL_PATH_TO_CATALOG,
    extract_object_id_and_catalog,
    fetch_content,
)


SAMPLE_URL = (
    "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq"
)


def test_extract_object_id_and_catalog_parses_known_url():
    """B16-1: 已知 catalog 路径正确解析 (object_id, catalog)。"""
    object_id, catalog = extract_object_id_and_catalog(SAMPLE_URL)
    assert object_id == "arkts-text-faq"
    assert catalog == "harmonyos-guides"


def test_extract_object_id_and_catalog_strips_trailing_slash():
    """B16-2: 末尾斜杠应被剥离，object_id 仍为最后一段。"""
    object_id, catalog = extract_object_id_and_catalog(SAMPLE_URL + "/")
    assert object_id == "arkts-text-faq"
    assert catalog == "harmonyos-guides"


def test_extract_object_id_and_catalog_unknown_path_raises():
    """B16-3: url path 中无已知 catalog 关键字，raise ValueError。"""
    bad_urls = [
        "https://example.com/foo/bar",
        "https://example.com/unknown/whatever",
        "https://example.com/",
    ]
    for url in bad_urls:
        with pytest.raises(ValueError, match="catalog|不支持"):
            extract_object_id_and_catalog(url)


def test_fetch_content_returns_non_empty_str():
    """B16-4: 成功调用返回非空 markdown str。"""
    fake_result = {"content": "# 标题\n\n正文内容。"}
    with patch("scripts.kb.content_fetcher.detail", return_value=fake_result):
        content = fetch_content(SAMPLE_URL)
    assert isinstance(content, str)
    assert len(content) > 0
    assert "标题" in content


def test_fetch_content_propagates_detail_error_as_value_error():
    """B16-5: detail() 返回 {'error': ...} 时 raise ValueError（fail-loud）。"""
    fake_result = {"error": "API error: code=404 message=not found"}
    with patch("scripts.kb.content_fetcher.detail", return_value=fake_result):
        with pytest.raises(ValueError, match="error|失败"):
            fetch_content(SAMPLE_URL)


def test_fetch_content_unknown_catalog_raises():
    """B16-6: url catalog 不在白名单时 raise ValueError（不调用 detail）。"""
    with pytest.raises(ValueError, match="catalog|不支持"):
        fetch_content("https://example.com/foo/bar")


def test_url_path_to_catalog_matches_detail_capability():
    """B16-7: URL_PATH_TO_CATALOG 必须与 detail() 真实支持的 catalog 对齐。

    BUG 修复（T-verify）：旧映射用 9 个 harmonyos-* 前缀，但 detail() 底层 API
    只接受 DEVELOPER_CATALOGS（best-practices / harmonyos-guides /
    harmonyos-references），二者完全不匹配会导致 fetch-content 永远失败。修复后
    映射只保留"路径段 == 真实 catalog"的直通项，其余 catalog 显式报错。
    """
    from scripts.search.detail import DEVELOPER_CATALOGS

    assert set(URL_PATH_TO_CATALOG.keys()) == set(DEVELOPER_CATALOGS), (
        f"映射必须等于 detail 真实支持的 catalog: "
        f"{set(DEVELOPER_CATALOGS) ^ set(URL_PATH_TO_CATALOG.keys())}"
    )
    # 不在直通项中的路径段必须显式 raise（不误映射）
    for bad_seg in ("design-guides", "architecture-guides", "atomic-guides", "app"):
        with pytest.raises(ValueError, match="不支持|detail API 暂不支持"):
            extract_object_id_and_catalog(
                f"https://developer.huawei.com/consumer/cn/doc/{bad_seg}/some-id"
            )
