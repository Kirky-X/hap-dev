"""HarmonyOS developer docs search across the developer and device endpoints.

Usage:
    python3 -m scripts.search.search <keyword> [--catalog CATALOG]
        [--endpoint developer|device] [--offset OFFSET] [--length LENGTH]

Routing rules (deterministic, see ``_resolve_plan``):
- ``endpoint="device"`` always queries the device endpoint; ``catalog`` is
  ignored (the device endpoint has no catalog concept).
- ``catalog`` set (must be one of ``DEVELOPER_CATALOGS``) queries only the
  developer endpoint with that single catalog.
- ``endpoint="developer"`` with ``catalog=None`` queries all developer
  catalogs.
- ``endpoint=None`` with ``catalog=None`` queries all developer catalogs AND
  the device endpoint.

Errors are surfaced explicitly in the ``errors`` list; the script never
retries on zero results (retry logic lives in the agent layer).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Allow both ``python3 -m scripts.search.search`` and direct
# ``python3 scripts/search/search.py`` invocation by ensuring the project
# root (hap-dev) is on sys.path when run as a plain script.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import httpx

from scripts.search._http import (
    DEVICE_CATEGORY_LIST,
    DEVICE_SUB_TYPE_LIST,
    DEVELOPER_CATALOGS,
    api_post,
    parse_anchors,
)

DEVELOPER_CATALOG_LABEL = "Developer"
DEVICE_CATALOG = "device"
DEVICE_CATALOG_LABEL = "Device"
DEFAULT_LENGTH = 12
MAX_LENGTH = 100
_VALID_ENDPOINTS = {"developer", "device", None}


def _parse_ext(ext_raw: Any) -> dict:
    """Tolerantly parse the ``ext`` field of a search hit into a dict."""
    if isinstance(ext_raw, dict):
        return ext_raw
    if isinstance(ext_raw, str):
        if not ext_raw:
            return {}
        try:
            parsed = json.loads(ext_raw)
            return parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            return {}
    return {}


def _build_developer_payload(
    keyword: str, catalog: str, offset: int, length: int, ts: str
) -> dict:
    return {
        "deviceId": "ESN",
        "deviceType": "1",
        "language": "zh",
        "country": "CN",
        "keyWord": keyword,
        "requestOrgin": 5,
        "ts": ts,
        "developerVertical": {
            "category": 1,
            "language": "zh",
            "catalog": catalog,
            "searchSubTitle": 0,
            "scene": 2,
            "subType": 4,
        },
        "cutPage": {"offset": offset, "length": length},
    }


def _build_device_payload(keyword: str, offset: int, length: int, ts: str) -> dict:
    return {
        "deviceId": "ESN",
        "deviceType": "1",
        "ts": ts,
        "language": "zh",
        "country": "CN",
        "requestOrgin": 20,
        "whetherToCorrect": 1,
        "whetherToSynonym": 1,
        "keyWord": keyword,
        "harmonynorthVertical": {
            "language": "zh",
            "categoryList": list(DEVICE_CATEGORY_LIST),
            "subTypeList": list(DEVICE_SUB_TYPE_LIST),
        },
        "cutPage": {"offset": offset, "length": length},
    }


def _resolve_plan(
    catalog: str | None, endpoint: str | None
) -> list[tuple[str, str | None]]:
    """Return the ordered list of ``(endpoint, catalog)`` tuples to query.

    Pure deterministic routing per Rule 5: no heuristics, no model judgement.
    """
    if endpoint not in _VALID_ENDPOINTS:
        raise ValueError(
            f"Unknown endpoint: {endpoint!r}; expected 'developer', 'device', or None"
        )

    # device endpoint wins regardless of catalog (device has no catalog).
    if endpoint == "device":
        return [("device", None)]

    # From here endpoint is None or "developer" (both go through developer catalogs).
    if catalog is not None:
        if catalog not in DEVELOPER_CATALOGS:
            raise ValueError(
                f"Unknown catalog: {catalog!r}; expected one of {DEVELOPER_CATALOGS}"
            )
        return [("developer", catalog)]

    # catalog is None.
    plan: list[tuple[str, str | None]] = [
        ("developer", cat) for cat in DEVELOPER_CATALOGS
    ]
    if endpoint is None:
        plan.append(("device", None))
    return plan


def _extract_object_id(url_path: str) -> str:
    if not url_path:
        return ""
    url_path = url_path.rstrip("/")
    if "/" in url_path:
        return url_path.rsplit("/", 1)[-1]
    return url_path


def _normalize_url(url_path: str) -> str:
    if not url_path:
        return ""
    if url_path.startswith("//"):
        return f"https:{url_path}"
    return url_path


def _parse_developer_hits(
    data: dict, catalog: str
) -> list[dict]:
    results: list[dict] = []
    for group in data.get("searchResult", []) or []:
        if not isinstance(group, dict):
            continue
        for info in group.get("developerInfos", []) or []:
            if not isinstance(info, dict):
                continue
            ext = _parse_ext(info.get("ext", "{}"))
            url_path = info.get("url", "") or ""
            results.append(
                {
                    "name": info.get("name", "") or "",
                    "description": info.get("description", "") or "",
                    "object_id": _extract_object_id(url_path),
                    "catalog": catalog,
                    "catalog_label": ext.get("catalogName", "") or "",
                    "language": ext.get("docCodeLanguage", "") or "",
                    "kit": ext.get("kitName", "") or "",
                    "url": _normalize_url(url_path),
                    "anchors": parse_anchors(ext),
                }
            )
    return results


def _parse_device_hits(data: dict) -> list[dict]:
    results: list[dict] = []
    for group in data.get("searchResult", []) or []:
        if not isinstance(group, dict):
            continue
        for info in group.get("developerInfos", []) or []:
            if not isinstance(info, dict):
                continue
            ext = _parse_ext(info.get("ext", "{}"))
            url_path = info.get("url", "") or ""
            results.append(
                {
                    "name": info.get("name", "") or "",
                    "description": info.get("description", "") or "",
                    "object_id": _extract_object_id(url_path),
                    "catalog": DEVICE_CATALOG,
                    "catalog_label": ext.get("catalogName", "") or DEVICE_CATALOG_LABEL,
                    "language": ext.get("docCodeLanguage", "") or "",
                    "kit": ext.get("kitName", "") or "",
                    "url": _normalize_url(url_path),
                    "anchors": parse_anchors(ext),
                }
            )
    return results


def search(
    keyword: str,
    catalog: str | None = None,
    endpoint: str | None = None,
    offset: int = 0,
    length: int = DEFAULT_LENGTH,
    client: httpx.Client | None = None,
) -> dict:
    """Search HarmonyOS docs across the configured endpoints.

    Returns ``{keyword, offset, length, total, results, errors}``. ``errors``
    is a list of human-readable strings; HTTP/API failures are surfaced there
    rather than swallowed. Zero-result responses are returned as ``total=0``
    without retry.
    """
    if not keyword or not keyword.strip():
        raise ValueError("keyword must not be empty")
    if offset < 0:
        raise ValueError(f"offset must be >= 0, got {offset}")
    if length <= 0:
        raise ValueError(f"length must be > 0, got {length}")

    plan = _resolve_plan(catalog, endpoint)
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    all_results: list[dict] = []
    errors: list[str] = []

    for ep, cat in plan:
        if ep == "developer":
            payload = _build_developer_payload(keyword, cat, offset, length, ts)
            label = f"developer catalog {cat}"
        else:
            payload = _build_device_payload(keyword, offset, length, ts)
            label = "device endpoint"

        data = api_post(payload, endpoint=ep, client=client)
        if data is None:
            errors.append(f"HTTP request failed for {label}")
            continue

        code = data.get("code")
        # developer/device endpoints return code as string "00000" on success.
        if str(code) != "00000":
            desc = data.get("rtnDesc") or data.get("message") or "unknown"
            errors.append(f"API error for {label}: code={code} desc={desc}")
            continue

        if ep == "developer":
            all_results.extend(_parse_developer_hits(data, cat))
        else:
            all_results.extend(_parse_device_hits(data))

    return {
        "keyword": keyword,
        "offset": offset,
        "length": length,
        "total": len(all_results),
        "results": all_results,
        "errors": errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Search HarmonyOS developer and device docs",
    )
    parser.add_argument("keyword", help="Search keyword")
    parser.add_argument(
        "--catalog",
        choices=DEVELOPER_CATALOGS,
        default=None,
        help="Developer catalog filter (only applies to developer endpoint)",
    )
    parser.add_argument(
        "--endpoint",
        choices=["developer", "device"],
        default=None,
        help="Endpoint to query. If omitted, both endpoints are queried.",
    )
    parser.add_argument(
        "--offset", type=int, default=0, help="Pagination offset (default 0)"
    )
    parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help=f"Results per page (default {DEFAULT_LENGTH}, max {MAX_LENGTH})",
    )
    args = parser.parse_args(argv)

    length = min(args.length, MAX_LENGTH)
    try:
        result = search(
            args.keyword,
            catalog=args.catalog,
            endpoint=args.endpoint,
            offset=args.offset,
            length=length,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    # Non-zero exit code when every query failed so callers can detect it.
    if result["total"] == 0 and result["errors"] and not result["results"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
