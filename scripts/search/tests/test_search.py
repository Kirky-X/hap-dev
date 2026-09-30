"""Tests for ``scripts.search.search`` using mocked httpx clients.

No real network requests are made. We assert:
- developer endpoint payload contains ``developerVertical.catalog``
- device endpoint payload contains ``harmonynorthVertical.categoryList``
- catalog filter (best-practices / harmonyos-guides / harmonyos-references)
  routes to the developer endpoint only
- ``--offset`` / ``--length`` propagate into ``cutPage``
- zero-result responses are not retried (the script returns total=0 and the
  post count matches the number of catalogs/endpoints searched)
- HTTP errors are surfaced in the ``errors`` field rather than swallowed
- result objects contain all required fields
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import httpx
import pytest

from scripts.search._http import (
    DEVICE_CATEGORY_LIST,
    DEVICE_HOST,
    DEVICE_PATH,
    DEVELOPER_CATALOGS,
    DEVELOPER_HOST,
    DEVELOPER_PATH,
)
from scripts.search.search import search


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------


def _make_response(payload: dict) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.raise_for_status.return_value = None
    resp.json.return_value = payload
    return resp


def _make_client(responses) -> MagicMock:
    """Build a fake httpx.Client whose successive ``post`` calls return the
    provided response dicts (or raise if the entry is an Exception)."""
    client = MagicMock(spec=httpx.Client)
    side = []
    for r in responses:
        if isinstance(r, Exception):
            side.append(r)
        else:
            side.append(_make_response(r))
    client.post.side_effect = side
    return client


def _dev_response(
    name: str = "doc-name",
    desc: str = "description",
    object_id: str = "obj-1",
    catalog_name: str = "Best Practices",
    lang: str = "arkts",
    kit: str = "ArkUI",
    anchors: list[dict] | None = None,
    code: str = "00000",
) -> dict:
    ext: dict = {
        "catalogName": catalog_name,
        "docCodeLanguage": lang,
        "kitName": kit,
    }
    if anchors is not None:
        ext["anchorList"] = anchors
    return {
        "code": code,
        "searchResult": [
            {
                "developerInfos": [
                    {
                        "name": name,
                        "description": desc,
                        "url": f"//docs.example.com/path/{object_id}",
                        "ext": json.dumps(ext),
                    }
                ]
            }
        ],
    }


def _device_response(
    name: str = "device-doc",
    desc: str = "device description",
    object_id: str = "dobj-1",
    code: str = "00000",
) -> dict:
    return {
        "code": code,
        "searchResult": [
            {
                "developerInfos": [
                    {
                        "name": name,
                        "description": desc,
                        "url": f"//device.harmonyos.com/docs/{object_id}",
                        "ext": "{}",
                    }
                ]
            }
        ],
    }


def _empty_response(code: str = "00000") -> dict:
    return {"code": code, "searchResult": []}


def _post_call(client: MagicMock, idx: int) -> tuple[str, dict]:
    """Return (url, json_payload) for the idx-th client.post call."""
    assert client.post.call_count >= idx + 1, (
        f"expected at least {idx + 1} post calls, got {client.post.call_count}"
    )
    call = client.post.call_args_list[idx]
    args, kwargs = call
    url = args[0] if args else kwargs.get("url")
    payload = kwargs.get("json")
    return url, payload


DEVELOPER_URL = f"https://{DEVELOPER_HOST}{DEVELOPER_PATH}"
DEVICE_URL = f"https://{DEVICE_HOST}{DEVICE_PATH}"


# ---------------------------------------------------------------------------
# developer endpoint payload
# ---------------------------------------------------------------------------


def test_developer_single_catalog_payload_contains_developer_vertical_catalog():
    client = _make_client([_dev_response()])
    result = search("kw", catalog="best-practices", client=client)
    assert client.post.call_count == 1
    url, payload = _post_call(client, 0)
    assert url == DEVELOPER_URL
    assert "developerVertical" in payload
    assert payload["developerVertical"]["catalog"] == "best-practices"
    assert payload["developerVertical"]["language"] == "zh"
    # device-only keys must NOT leak into developer payload
    assert "harmonynorthVertical" not in payload
    assert result["errors"] == []
    assert result["total"] == 1


def test_developer_endpoint_no_catalog_searches_all_three_catalogs():
    client = _make_client([_dev_response(object_id=f"o{i}") for i in range(len(DEVELOPER_CATALOGS))])
    result = search("kw", endpoint="developer", client=client)
    assert client.post.call_count == len(DEVELOPER_CATALOGS)
    seen_catalogs = []
    for i in range(len(DEVELOPER_CATALOGS)):
        url, payload = _post_call(client, i)
        assert url == DEVELOPER_URL
        assert payload["developerVertical"]["catalog"] in DEVELOPER_CATALOGS
        seen_catalogs.append(payload["developerVertical"]["catalog"])
    assert sorted(seen_catalogs) == sorted(DEVELOPER_CATALOGS)
    assert result["total"] == len(DEVELOPER_CATALOGS)
    assert result["errors"] == []


def test_catalog_filter_routes_only_to_developer_endpoint():
    for cat in DEVELOPER_CATALOGS:
        client = _make_client([_dev_response()])
        result = search("kw", catalog=cat, client=client)
        assert client.post.call_count == 1, f"catalog {cat} should hit developer only"
        url, payload = _post_call(client, 0)
        assert url == DEVELOPER_URL, f"catalog {cat} must not hit device endpoint"
        assert payload["developerVertical"]["catalog"] == cat
        assert result["total"] == 1


def test_developer_catalog_choice_validation_rejects_unknown():
    client = _make_client([])
    with pytest.raises(ValueError):
        search("kw", catalog="not-a-real-catalog", client=client)
    assert client.post.call_count == 0


# ---------------------------------------------------------------------------
# device endpoint payload
# ---------------------------------------------------------------------------


def test_device_endpoint_payload_contains_harmonynorth_vertical_category_list():
    client = _make_client([_device_response()])
    result = search("kw", endpoint="device", client=client)
    assert client.post.call_count == 1
    url, payload = _post_call(client, 0)
    assert url == DEVICE_URL
    assert "harmonynorthVertical" in payload
    assert payload["harmonynorthVertical"]["categoryList"] == DEVICE_CATEGORY_LIST
    assert payload["harmonynorthVertical"]["subTypeList"] == [0, 2]
    assert payload["harmonynorthVertical"]["language"] == "zh"
    # developer-only keys must NOT leak into device payload
    assert "developerVertical" not in payload
    assert result["errors"] == []


def test_device_endpoint_ignores_catalog_argument():
    # device endpoint has no catalog concept; passing catalog must not change
    # the payload structure and must NOT route to the developer endpoint.
    client = _make_client([_device_response()])
    search("kw", endpoint="device", catalog="best-practices", client=client)
    assert client.post.call_count == 1
    url, payload = _post_call(client, 0)
    assert url == DEVICE_URL
    assert "harmonynorthVertical" in payload
    assert "developerVertical" not in payload


# ---------------------------------------------------------------------------
# both endpoints (endpoint=None)
# ---------------------------------------------------------------------------


def test_both_endpoints_searches_developer_catalogs_and_device():
    n_dev = len(DEVELOPER_CATALOGS)
    responses = [_dev_response(object_id=f"d{i}") for i in range(n_dev)]
    responses.append(_device_response(object_id="dev-1"))
    client = _make_client(responses)
    result = search("kw", endpoint=None, client=client)
    assert client.post.call_count == n_dev + 1
    for i in range(n_dev):
        url, _ = _post_call(client, i)
        assert url == DEVELOPER_URL
    url, payload = _post_call(client, n_dev)
    assert url == DEVICE_URL
    assert "harmonynorthVertical" in payload
    assert result["total"] == n_dev + 1
    assert result["errors"] == []


# ---------------------------------------------------------------------------
# pagination
# ---------------------------------------------------------------------------


def test_offset_length_propagate_to_cutpage():
    client = _make_client([_dev_response()])
    search("kw", catalog="harmonyos-guides", offset=24, length=8, client=client)
    _, payload = _post_call(client, 0)
    assert payload["cutPage"] == {"offset": 24, "length": 8}


def test_offset_length_default_to_zero_and_twelve():
    client = _make_client([_dev_response()])
    search("kw", catalog="harmonyos-guides", client=client)
    _, payload = _post_call(client, 0)
    assert payload["cutPage"] == {"offset": 0, "length": 12}


def test_device_endpoint_pagination_propagates():
    client = _make_client([_device_response()])
    search("kw", endpoint="device", offset=15, length=5, client=client)
    _, payload = _post_call(client, 0)
    assert payload["cutPage"] == {"offset": 15, "length": 5}


# ---------------------------------------------------------------------------
# zero results -> no retry
# ---------------------------------------------------------------------------


def test_zero_results_developer_no_retry():
    client = _make_client([_empty_response()])
    result = search("kw", catalog="best-practices", client=client)
    assert client.post.call_count == 1  # no retry
    assert result["total"] == 0
    assert result["results"] == []
    assert result["errors"] == []


def test_zero_results_both_endpoints_no_retry():
    n_dev = len(DEVELOPER_CATALOGS)
    responses = [_empty_response() for _ in range(n_dev)]
    responses.append(_empty_response())  # device
    client = _make_client(responses)
    result = search("kw", endpoint=None, client=client)
    assert client.post.call_count == n_dev + 1  # exactly one call per catalog/endpoint
    assert result["total"] == 0
    assert result["errors"] == []


# ---------------------------------------------------------------------------
# error surfacing
# ---------------------------------------------------------------------------


def test_http_error_recorded_in_errors_field():
    client = _make_client([httpx.HTTPError("boom")])
    result = search("kw", catalog="best-practices", client=client)
    assert client.post.call_count == 1
    assert result["total"] == 0
    assert len(result["errors"]) == 1
    assert "best-practices" in result["errors"][0] or "HTTP" in result["errors"][0]


def test_api_error_code_recorded_in_errors_field():
    bad = _dev_response(code="99999")
    bad["rtnDesc"] = "internal error"
    client = _make_client([bad])
    result = search("kw", catalog="best-practices", client=client)
    assert result["total"] == 0
    assert len(result["errors"]) == 1


def test_partial_failure_does_not_mask_successful_results():
    n_dev = len(DEVELOPER_CATALOGS)
    responses = [_dev_response(object_id="ok-1")]
    # second developer catalog fails, third succeeds, device succeeds
    responses.append(httpx.HTTPError("fail"))
    responses.append(_dev_response(object_id="ok-2"))
    responses.append(_device_response(object_id="dev-ok"))
    client = _make_client(responses)
    result = search("kw", endpoint=None, client=client)
    assert client.post.call_count == n_dev + 1
    assert result["total"] == 3  # two developer hits + one device hit
    assert len(result["errors"]) == 1


# ---------------------------------------------------------------------------
# result object shape
# ---------------------------------------------------------------------------


def test_result_object_contains_all_required_fields():
    anchors = [{"anchorId": "a1", "title": "Anchor One"}]
    client = _make_client(
        [_dev_response(object_id="obj-9", anchors=anchors, catalog_name="Best Practices")]
    )
    result = search("kw", catalog="best-practices", client=client)
    assert result["total"] == 1
    item = result["results"][0]
    expected_keys = {
        "name",
        "description",
        "object_id",
        "catalog",
        "catalog_label",
        "language",
        "kit",
        "url",
        "anchors",
    }
    assert expected_keys.issubset(item.keys())
    assert item["object_id"] == "obj-9"
    assert item["catalog"] == "best-practices"
    assert item["catalog_label"] == "Best Practices"
    assert item["anchors"] == [{"id": "a1", "title": "Anchor One"}]
    assert item["url"].startswith("https://")


def test_search_return_shape_top_level_fields():
    client = _make_client([_dev_response()])
    result = search("kw", catalog="best-practices", offset=5, length=7, client=client)
    for key in ("keyword", "offset", "length", "total", "results", "errors"):
        assert key in result, f"missing top-level key {key}"
    assert result["keyword"] == "kw"
    assert result["offset"] == 5
    assert result["length"] == 7


def test_device_results_carry_device_catalog_marker():
    client = _make_client([_device_response(object_id="dev-obj")])
    result = search("kw", endpoint="device", client=client)
    assert result["total"] == 1
    item = result["results"][0]
    assert item["catalog"] == "device"
    assert item["object_id"] == "dev-obj"
