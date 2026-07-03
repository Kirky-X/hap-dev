"""B15: 调用华为 getRecommendInfo API 获取推荐文档列表。

get_recommendations(doc_url) 从 url 提取 itemID（最后一段 path），POST 到
华为推荐 API（匿名访问，无需认证），解析 result.recommendList，返回
[{"url": ..., "name": ..., "item_id": ...}, ...]。

失败时 raise ValueError（fail-loud，不静默返回空列表）。
"""
from __future__ import annotations

import httpx

# 华为推荐 API：匿名访问，返回与给定 doc 关联的推荐文档列表。
# rcmScenario="003" 对应「相关推荐」场景，recallNum 控制返回数量。
RECOMMEND_API = (
    "https://svc-drcn.developer.huawei.com/community/servlet/"
    "consumer/partnerCommunityService/v1/servlet/open/getRecommendInfo"
)

# HTTP 超时（秒）。15s 足够覆盖网络抖动，避免长时间挂起。
_TIMEOUT = 15.0


def get_recommendations(doc_url: str, recall_num: int = 10) -> list[dict]:
    """调用 getRecommendInfo API 获取推荐文档列表。

    Args:
        doc_url: 文档 url，从中提取最后一段 path 作为 itemID。
            例如 "https://.../harmonyos-guides/arkts-text-faq" → "arkts-text-faq"。
        recall_num: 期望返回的推荐数量，默认 10。

    Returns:
        list[dict]，每个 dict 含且仅含三个键：
            - url: 推荐 doc 的 url
            - name: 推荐 doc 的标题
            - item_id: 推荐 doc 的 itemId（API 原始字段）

    Raises:
        ValueError: url 为空、网络失败、HTTP 错误或响应解析失败。
            fail-loud 原则——不静默返回空列表掩盖错误。
    """
    if not doc_url:
        raise ValueError("get_recommendations: doc_url 不能为空")

    # 从 url 提取 itemID：末尾斜杠先剥离，再取最后一段。
    # 例如 ".../arkts-text-faq/" → "arkts-text-faq"
    item_id = doc_url.rstrip("/").rsplit("/", 1)[-1]
    if not item_id:
        raise ValueError(f"get_recommendations: 无法从 url 提取 itemID: {doc_url!r}")

    body = {
        "title": "",
        "itemID": item_id,
        "rcmScenario": "003",
        "recallNum": recall_num,
        "bottomCoverType": 0,
        "plateType": 1,
    }

    try:
        with httpx.Client(timeout=_TIMEOUT) as client:
            resp = client.post(RECOMMEND_API, json=body)
            resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise ValueError(
            f"get_recommendations: API 返回 HTTP {exc.response.status_code}"
        ) from exc
    except httpx.RequestError as exc:
        # 涵盖 ConnectError / TimeoutException / 等
        raise ValueError(f"get_recommendations: 网络请求失败: {exc}") from exc

    try:
        data = resp.json()
    except Exception as exc:
        raise ValueError(f"get_recommendations: 响应非 JSON: {exc}") from exc

    recommend_list = (data.get("result") or {}).get("recommendList") or []
    if not isinstance(recommend_list, list):
        raise ValueError(
            f"get_recommendations: result.recommendList 非 list: "
            f"{type(recommend_list).__name__}"
        )

    # 字段名映射：API 返回 itemId → 我们用 item_id（Python 风格）
    return [
        {
            "url": r["url"],
            "name": r["name"],
            "item_id": r["itemId"],
        }
        for r in recommend_list
    ]
