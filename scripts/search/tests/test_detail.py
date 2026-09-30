"""Tests for ``scripts.search.detail`` using mocked httpx clients.

Asserts:
- detail(object_id, catalog) hits the correct detail endpoint URL on the
  developer host and sends objectId/catalogName in the payload
- HTML content is converted to Markdown preserving code blocks, headings,
  lists, tables, and links
- empty content is returned as an empty string (not an error)
- anchors from the response are parsed into ``[{id, title}]``
- HTTP / API errors surface as ``{"error": ...}`` rather than being swallowed
- invalid catalog / empty object_id are rejected explicitly
"""

from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest

from scripts.search._http import DETAIL_HOST, DETAIL_PATH
from scripts.search.detail import detail

DETAIL_URL = f"https://{DETAIL_HOST}{DETAIL_PATH}"


def _make_response(payload: dict) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.raise_for_status.return_value = None
    resp.json.return_value = payload
    return resp


def _make_client(responses) -> MagicMock:
    client = MagicMock(spec=httpx.Client)
    side = []
    for r in responses:
        side.append(r if isinstance(r, Exception) else _make_response(r))
    client.post.side_effect = side
    return client


def _ok_response(
    title: str = "Doc Title",
    lang: str = "cn",
    version: str = "1.0.0",
    html: str = "<p>hello</p>",
    anchors: list[dict] | None = None,
    code: int = 0,
) -> dict:
    value: dict = {
        "title": title,
        "lang": lang,
        "version": version,
        "content": {"content": html},
    }
    if anchors is not None:
        value["anchorList"] = anchors
    return {"code": code, "value": value}


# ---------------------------------------------------------------------------
# endpoint routing
# ---------------------------------------------------------------------------


def test_detail_calls_correct_endpoint_url():
    client = _make_client([_ok_response()])
    detail("obj-1", "harmonyos-guides", client=client)
    assert client.post.call_count == 1
    args, kwargs = client.post.call_args
    url = args[0] if args else kwargs.get("url")
    assert url == DETAIL_URL


def test_detail_payload_contains_object_id_and_catalog():
    client = _make_client([_ok_response()])
    detail("obj-1", "harmonyos-references", client=client)
    _, kwargs = client.post.call_args
    payload = kwargs["json"]
    assert payload["objectId"] == "obj-1"
    assert payload["catalogName"] == "harmonyos-references"
    assert payload["language"] == "cn"


def test_detail_invalid_catalog_raises_value_error():
    client = _make_client([])
    with pytest.raises(ValueError):
        detail("obj-1", "not-a-catalog", client=client)
    assert client.post.call_count == 0


def test_detail_empty_object_id_raises_value_error():
    client = _make_client([])
    with pytest.raises(ValueError):
        detail("", "harmonyos-guides", client=client)
    with pytest.raises(ValueError):
        detail("   ", "harmonyos-guides", client=client)
    assert client.post.call_count == 0


# ---------------------------------------------------------------------------
# HTML -> Markdown preservation
# ---------------------------------------------------------------------------


def test_detail_html_to_markdown_preserves_codeblock_and_heading():
    html = "<h2>Section</h2><pre><code>let x = 1;</code></pre>"
    client = _make_client([_ok_response(html=html)])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert "error" not in result
    content = result["content"]
    assert "## Section" in content
    assert "```" in content
    assert "let x = 1;" in content


def test_detail_html_to_markdown_preserves_lists_table_link():
    html = (
        "<h3>Sub</h3>"
        "<ul><li>alpha</li><li>beta</li></ul>"
        "<ol><li>first</li><li>second</li></ol>"
        '<table><tr><th>K</th><th>V</th></tr>'
        "<tr><td>1</td><td>2</td></tr></table>"
        '<a href="https://example.com">click</a>'
    )
    client = _make_client([_ok_response(html=html)])
    result = detail("obj-1", "best-practices", client=client)
    content = result["content"]
    assert "### Sub" in content
    assert "- alpha" in content
    assert "1. first" in content
    assert "| K | V |" in content
    assert "| 1 | 2 |" in content
    assert "[click](https://example.com)" in content


def test_detail_html_to_markdown_preserves_h1_h4_h6():
    html = "<h1>H1</h1><h4>H4</h4><h6>H6</h6>"
    client = _make_client([_ok_response(html=html)])
    result = detail("obj-1", "harmonyos-guides", client=client)
    content = result["content"]
    assert "# H1" in content
    assert "#### H4" in content
    assert "###### H6" in content


# ---------------------------------------------------------------------------
# empty content
# ---------------------------------------------------------------------------


def test_detail_empty_content_returns_empty_string():
    # content.content missing
    resp = {"code": 0, "value": {"title": "T", "lang": "cn", "version": "1"}}
    client = _make_client([resp])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert "error" not in result
    assert result["content"] == ""


def test_detail_blank_html_content_returns_empty_string():
    resp = _ok_response(html="   ")
    client = _make_client([resp])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert result["content"] == ""


# ---------------------------------------------------------------------------
# anchors
# ---------------------------------------------------------------------------


def test_detail_anchors_parsed_into_id_title():
    anchors = [
        {"anchorId": "a1", "title": "First"},
        {"anchorId": "a2", "title": "Second"},
    ]
    client = _make_client([_ok_response(anchors=anchors)])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert result["anchors"] == [
        {"id": "a1", "title": "First"},
        {"id": "a2", "title": "Second"},
    ]


def test_detail_no_anchors_returns_empty_list():
    client = _make_client([_ok_response()])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert result["anchors"] == []


# ---------------------------------------------------------------------------
# error surfacing
# ---------------------------------------------------------------------------


def test_detail_http_error_returns_error_dict():
    client = _make_client([httpx.HTTPError("boom")])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert "error" in result
    assert "HTTP" in result["error"] or "boom" in result["error"]


def test_detail_api_error_code_returns_error_dict():
    resp = _ok_response(code=500)
    resp["message"] = "internal server error"
    client = _make_client([resp])
    result = detail("obj-1", "harmonyos-guides", client=client)
    assert "error" in result
    assert "500" in result["error"] or "internal" in result["error"].lower()


# ---------------------------------------------------------------------------
# return shape
# ---------------------------------------------------------------------------


def test_detail_return_shape_contains_required_fields():
    client = _make_client([_ok_response(title="T", lang="cn", version="2.0")])
    result = detail("obj-1", "harmonyos-guides", client=client)
    expected = {"title", "object_id", "catalog", "language", "version", "anchors", "content"}
    assert expected.issubset(result.keys())
    assert result["title"] == "T"
    assert result["object_id"] == "obj-1"
    assert result["catalog"] == "harmonyos-guides"
    assert result["language"] == "cn"
    assert result["version"] == "2.0"
