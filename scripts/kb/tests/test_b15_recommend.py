"""B15: recommend.py 调用 getRecommendInfo API 获取推荐列表 (Red phase).

get_recommendations(doc_url) 从 url 提取 itemID（最后一段 path），POST 到
华为推荐 API，解析 result.recommendList，返回 [{url, name, item_id}, ...]。

失败时 raise ValueError（fail-loud，不静默返回空）。
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from scripts.kb.recommend import RECOMMEND_API, get_recommendations


SAMPLE_DOC_URL = (
    "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq"
)


def _mock_response(recommend_list: list[dict]) -> MagicMock:
    """构造一个成功的 mock response，json() 返回 {result: {recommendList: ...}}。"""
    resp = MagicMock()
    resp.raise_for_status.return_value = None
    resp.json.return_value = {
        "result": {"recommendList": recommend_list}
    }
    return resp


def test_get_recommendations_returns_list_of_dicts():
    """B15-1: 返回 list[dict]，每个 dict 含且仅含 url/name/item_id 三个键。"""
    mock_resp = _mock_response([
        {"url": "https://example.com/a", "name": "文档A", "itemId": "id-a"},
        {"url": "https://example.com/b", "name": "文档B", "itemId": "id-b"},
    ])
    with patch.object(httpx.Client, "post", return_value=mock_resp) as mock_post:
        result = get_recommendations(SAMPLE_DOC_URL)

    assert isinstance(result, list)
    assert len(result) == 2
    for item in result:
        assert set(item.keys()) == {"url", "name", "item_id"}
    assert result[0] == {
        "url": "https://example.com/a",
        "name": "文档A",
        "item_id": "id-a",
    }
    # 验证 POST 被调用，且用的是 RECOMMEND_API
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert args[0] == RECOMMEND_API or kwargs.get("url") == RECOMMEND_API


def test_get_recommendations_extracts_item_id_from_url():
    """B15-2: itemID 从 url 最后一段提取（arkts-text-faq）。"""
    mock_resp = _mock_response([])
    with patch.object(httpx.Client, "post", return_value=mock_resp) as mock_post:
        get_recommendations(SAMPLE_DOC_URL)

    args, kwargs = mock_post.call_args
    # POST body 在 json= 参数里
    body = kwargs.get("json") or (args[1] if len(args) > 1 else {})
    assert body["itemID"] == "arkts-text-faq", (
        f"itemID 应为 url 最后一段 'arkts-text-faq'，got {body.get('itemID')!r}"
    )


def test_get_recommendations_empty_url_raises():
    """B15-3: 空 url raise ValueError（fail-loud）。"""
    with pytest.raises(ValueError, match="url"):
        get_recommendations("")


def test_get_recommendations_network_failure_raises():
    """B15-4: 网络失败（httpx 连接错误）raise ValueError（不静默返回空）。"""
    with patch.object(httpx.Client, "post", side_effect=httpx.ConnectError("network down")):
        with pytest.raises(ValueError, match="网络|network|API"):
            get_recommendations(SAMPLE_DOC_URL)


def test_get_recommendations_http_error_raises():
    """B15-5: HTTP 4xx/5xx（raise_for_status 抛错）raise ValueError。"""
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
        "500 Server Error",
        request=MagicMock(),
        response=MagicMock(status_code=500),
    )
    with patch.object(httpx.Client, "post", return_value=mock_resp):
        with pytest.raises(ValueError):
            get_recommendations(SAMPLE_DOC_URL)


def test_get_recommendations_trailing_slash_stripped():
    """B15-6: url 末尾斜杠在提取 itemID 前应被剥离。"""
    mock_resp = _mock_response([])
    with patch.object(httpx.Client, "post", return_value=mock_resp) as mock_post:
        get_recommendations(SAMPLE_DOC_URL + "/")

    args, kwargs = mock_post.call_args
    body = kwargs.get("json") or (args[1] if len(args) > 1 else {})
    assert body["itemID"] == "arkts-text-faq", (
        "末尾斜杠应被 rstrip('/') 剥离，itemID 仍为 'arkts-text-faq'"
    )
