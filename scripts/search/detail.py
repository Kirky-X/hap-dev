"""HarmonyOS developer doc detail fetcher.

Fetches a single document by ``object_id`` from the developer-host detail
endpoint (``getDocumentById``), converts the embedded HTML content to
Markdown, and returns ``{title, object_id, catalog, language, version,
anchors, content}``.

Migrated from ``temp/HOS-Search/scripts/detail.py`` with the endpoint
host/path imported from ``_http`` (no hard-coded URLs).

Usage:
    python3 -m scripts.search.detail <object_id> <catalog_name>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow both ``python3 -m scripts.search.detail`` and direct
# ``python3 scripts/search/detail.py`` invocation by ensuring the project
# root (hap-dev) is on sys.path when run as a plain script.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import httpx

from scripts.search._http import (
    COMMON_HEADERS,
    DETAIL_HOST,
    DETAIL_PATH,
    DEVELOPER_CATALOGS,
    TIMEOUT,
    html_to_markdown,
    parse_anchors,
)

DETAIL_URL = f"https://{DETAIL_HOST}{DETAIL_PATH}"


def detail(
    object_id: str,
    catalog: str,
    client: httpx.Client | None = None,
) -> dict:
    """Fetch a HarmonyOS doc and return its cleaned Markdown content.

    Returns ``{title, object_id, catalog, language, version, anchors,
    content}`` on success, or ``{"error": "..."}`` on HTTP/API failure
    (errors surfaced explicitly, never swallowed).
    """
    if not object_id or not object_id.strip():
        raise ValueError("object_id must not be empty")
    if catalog not in DEVELOPER_CATALOGS:
        raise ValueError(
            f"Invalid catalog: {catalog!r}; expected one of {DEVELOPER_CATALOGS}"
        )

    payload = {
        "objectId": object_id,
        "version": "",
        "catalogName": catalog,
        "language": "cn",
    }

    should_close = client is None
    # follow_redirects=False（httpx 默认）：SSRF 防护 —— 拒绝 3xx 跳转到内网/任意 host。
    # 显式写出而非依赖默认值，避免未来误改 / httpx 版本漂移引入重定向跟随。
    client = client or httpx.Client(
        timeout=TIMEOUT, headers=COMMON_HEADERS, follow_redirects=False
    )
    try:
        resp = client.post(DETAIL_URL, json=payload)
        resp.raise_for_status()
        data = resp.json()
    except httpx.HTTPError as exc:
        return {"error": f"HTTP request failed: {exc}"}
    finally:
        if should_close:
            client.close()

    # Detail endpoint reports success with integer code 0 (and historically
    # also the string "0"); accept both to stay robust to API drift.
    if data.get("code") not in (0, "0"):
        msg = data.get("message") or data.get("rtnDesc") or "unknown"
        return {"error": f"API error: code={data.get('code')} message={msg}"}

    value = data.get("value", {}) or {}
    if not isinstance(value, dict):
        value = {}
    content_data = value.get("content", {}) or {}
    if not isinstance(content_data, dict):
        content_data = {}
    raw_html = content_data.get("content", "") or ""
    markdown = html_to_markdown(raw_html) if raw_html else ""

    return {
        "title": value.get("title", "") or "",
        "object_id": object_id,
        "catalog": catalog,
        "language": value.get("lang", "cn") or "cn",
        "version": value.get("version", "") or "",
        "anchors": parse_anchors(value),
        "content": markdown,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a HarmonyOS developer doc by object_id and catalog",
    )
    parser.add_argument(
        "object_id", help="Document object ID (last segment of doc URL)"
    )
    parser.add_argument(
        "catalog_name",
        choices=DEVELOPER_CATALOGS,
        help="Catalog name the document belongs to",
    )
    args = parser.parse_args(argv)

    try:
        result = detail(args.object_id, args.catalog_name)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if "error" in result:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
