"""Shared HTTP utilities for HarmonyOS search scripts.

Centralizes endpoint host/path constants (loaded from config.json with
hard-coded fallbacks), the ``api_post`` helper that routes to either the
``developer`` or ``device`` endpoint, ``parse_anchors`` migrated from the
legacy HOS-Search tool, and an ``html_to_markdown`` converter implemented
with the standard ``re`` module.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import httpx

# ---------------------------------------------------------------------------
# Endpoint configuration: load from config.json, fall back to hard-coded
# defaults so the module remains usable even if config.json is missing or
# the project layout changes.
# ---------------------------------------------------------------------------


def _load_endpoints() -> dict[str, dict[str, Any]]:
    # scripts/search/_http.py -> parents[2] = hap-dev (project root).
    config_path = Path(__file__).resolve().parents[2] / "config.json"
    try:
        with open(config_path, "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
        endpoints = cfg.get("endpoints", {})
        if isinstance(endpoints, dict):
            return endpoints
    except (OSError, json.JSONDecodeError):
        pass
    return {}


_endpoints = _load_endpoints()
_developer_cfg = _endpoints.get("developer", {}) if isinstance(_endpoints.get("developer"), dict) else {}
_device_cfg = _endpoints.get("device", {}) if isinstance(_endpoints.get("device"), dict) else {}

DEVELOPER_HOST: str = _developer_cfg.get("host", "svc-drcn.developer.huawei.com")
DEVELOPER_PATH: str = _developer_cfg.get(
    "path",
    "/community/servlet/consumer/partnerCommunityService/developer/search",
)
DEVELOPER_CATALOGS: list[str] = list(
    _developer_cfg.get("catalogs", ["best-practices", "harmonyos-guides", "harmonyos-references"])
)
DEVICE_HOST: str = _device_cfg.get("host", "svc-drcn.harmonyos.com")
DEVICE_PATH: str = _device_cfg.get(
    "path",
    "/servlet/partnerCommunityService/developer/harmonyNorthSearch",
)

# Detail endpoint lives on the developer host but uses a different path
# (fetched via getDocumentById). Kept here so detail.py does not hard-code
# any URL/host/path (task 3.5 requirement: import endpoint path from _http).
DETAIL_HOST: str = DEVELOPER_HOST
DETAIL_PATH: str = _developer_cfg.get(
    "detailPath",
    "/community/servlet/consumer/cn/documentPortal/getDocumentById",
)

# Catalog labels for human-friendly display, keyed by catalog slug.
CATALOG_LABELS: dict[str, str] = {
    "best-practices": "Best Practices",
    "harmonyos-guides": "HarmonyOS Guides",
    "harmonyos-references": "HarmonyOS References",
}

# Device endpoint fixed categories (from captured request sample).
DEVICE_CATEGORY_LIST: list[int] = [1, 3, 4, 8, 10, 11, 12, 13, 16]
DEVICE_SUB_TYPE_LIST: list[int] = [0, 2]

COMMON_HEADERS: dict[str, str] = {
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "origin": "https://developer.huawei.com",
    "referer": "https://developer.huawei.com/",
    "user-agent": "HOS-Search-Skill/2.0.0 (HarmonyOS Dev Skill)",
}

TIMEOUT = 30

_VALID_ENDPOINTS = {"developer", "device"}


def endpoint_url(endpoint: str = "developer") -> str:
    """Return the full HTTPS URL for the given endpoint."""
    if endpoint == "developer":
        return f"https://{DEVELOPER_HOST}{DEVELOPER_PATH}"
    if endpoint == "device":
        return f"https://{DEVICE_HOST}{DEVICE_PATH}"
    raise ValueError(
        f"Unknown endpoint: {endpoint!r}; expected one of {sorted(_VALID_ENDPOINTS)}"
    )


def api_post(
    payload: dict,
    endpoint: str = "developer",
    client: httpx.Client | None = None,
) -> dict | None:
    """POST ``payload`` to the selected endpoint and return parsed JSON.

    Returns ``None`` on HTTP error so callers can record the failure in an
    ``errors`` list (errors are surfaced explicitly, never swallowed silently
    in a default success value).
    """
    if endpoint not in _VALID_ENDPOINTS:
        raise ValueError(
            f"Unknown endpoint: {endpoint!r}; expected one of {sorted(_VALID_ENDPOINTS)}"
        )
    url = endpoint_url(endpoint)
    should_close = client is None
    client = client or httpx.Client(timeout=TIMEOUT, headers=COMMON_HEADERS)
    try:
        resp = client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPError as exc:
        print(f"HTTP error ({endpoint}): {exc}", file=sys.stderr)
        return None
    finally:
        if should_close:
            client.close()


def parse_anchors(data: dict, key: str = "anchorList") -> list[dict]:
    """Extract ``[{id, title}]`` from a dict's anchor list field.

    Migrated verbatim in spirit from the legacy HOS-Search ``_http.parse_anchors``;
    tolerates missing fields and non-list values.
    """
    raw = data.get(key, []) if isinstance(data, dict) else []
    if not isinstance(raw, list):
        return []
    anchors: list[dict] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        anchors.append(
            {
                "id": item.get("anchorId", "") or "",
                "title": item.get("title", "") or "",
            }
        )
    return anchors


# ---------------------------------------------------------------------------
# HTML -> Markdown converter implemented with the standard ``re`` module.
#
# Supported elements (required by task 3.1):
#   - code blocks:  <pre>...</pre>            -> ```...```
#   - inline code:  <code>...</code>          -> `...`
#   - headings:     <h1>..<h6>                -> # .. ######
#   - lists:        <ul><li> / <ol><li>       -> - / 1.
#   - tables:       <table><tr><td/th>        -> | a | b |
#   - links:        <a href="...">text</a>    -> [text](url)
# Also handles: <strong>/<b>, <em>/<i>, <p>, <br>, <hr>, <blockquote>,
# script/style stripping, and common HTML entities.
# ---------------------------------------------------------------------------

_PRE_RE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.DOTALL | re.IGNORECASE)
_CODE_RE = re.compile(r"<code[^>]*>(.*?)</code>", re.DOTALL | re.IGNORECASE)
_SCRIPT_RE = re.compile(r"<script[^>]*>.*?</script>", re.DOTALL | re.IGNORECASE)
_STYLE_RE = re.compile(r"<style[^>]*>.*?</style>", re.DOTALL | re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_A_RE = re.compile(
    r'<a\s+[^>]*?href\s*=\s*"([^"]*)"[^>]*>(.*?)</a>',
    re.DOTALL | re.IGNORECASE,
)
_A_SQUOTE_RE = re.compile(
    r"<a\s+[^>]*?href\s*=\s*'([^']*)'[^>]*>(.*?)</a>",
    re.DOTALL | re.IGNORECASE,
)
_STRONG_RE = re.compile(r"<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>", re.DOTALL | re.IGNORECASE)
_EM_RE = re.compile(r"<(?:em|i)\b[^>]*>(.*?)</(?:em|i)>", re.DOTALL | re.IGNORECASE)
_TABLE_RE = re.compile(r"<table[^>]*>.*?</table>", re.DOTALL | re.IGNORECASE)
_TR_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
_CELL_RE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.DOTALL | re.IGNORECASE)
_OL_RE = re.compile(r"<ol[^>]*>(.*?)</ol>", re.DOTALL | re.IGNORECASE)
_UL_RE = re.compile(r"<ul[^>]*>(.*?)</ul>", re.DOTALL | re.IGNORECASE)
_LI_RE = re.compile(r"<li[^>]*>(.*?)</li>", re.DOTALL | re.IGNORECASE)
_H_RE = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.DOTALL | re.IGNORECASE)
_P_OPEN_RE = re.compile(r"<p\b[^>]*>", re.IGNORECASE)
_P_CLOSE_RE = re.compile(r"</p>", re.IGNORECASE)
_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_HR_RE = re.compile(r"<hr\s*/?>", re.IGNORECASE)
_BQ_RE = re.compile(r"<blockquote\b[^>]*>(.*?)</blockquote>", re.DOTALL | re.IGNORECASE)

_ENTITY_MAP = {
    "&amp;": "&",
    "&lt;": "<",
    "&gt;": ">",
    "&quot;": '"',
    "&apos;": "'",
    "&nbsp;": " ",
}
_ENTITY_DEC_RE = re.compile(r"&#(\d+);")
_ENTITY_HEX_RE = re.compile(r"&#x([0-9a-fA-F]+);", re.IGNORECASE)
_BLANK_LINES_RE = re.compile(r"\n{3,}")
_TRAILING_SPACES_RE = re.compile(r" +\n")


def _decode_entities(text: str) -> str:
    for ent, ch in _ENTITY_MAP.items():
        text = text.replace(ent, ch)
    text = _ENTITY_DEC_RE.sub(lambda m: _safe_chr(m.group(1), 10), text)
    text = _ENTITY_HEX_RE.sub(lambda m: _safe_chr(m.group(1), 16), text)
    return text


def _safe_chr(value: str, base: int) -> str:
    try:
        return chr(int(value, base))
    except (ValueError, OverflowError):
        return f"&#{('x' + value) if base == 16 else value};"


def _strip_tags(html: str) -> str:
    return _TAG_RE.sub("", html)


def _convert_table(match: re.Match[str]) -> str:
    table_html = match.group(0)
    rows = _TR_RE.findall(table_html)
    parsed: list[list[str]] = []
    for row in rows:
        cells = _CELL_RE.findall(row)
        parsed.append([_strip_tags(c).strip() for c in cells])
    # Drop fully empty rows.
    parsed = [r for r in parsed if any(cell for cell in r)]
    if not parsed:
        return ""
    n_cols = max(len(r) for r in parsed)
    lines: list[str] = []
    for idx, row in enumerate(parsed):
        padded = [row[c].strip() if c < len(row) else "" for c in range(n_cols)]
        lines.append("| " + " | ".join(padded) + " |")
        if idx == 0:
            lines.append("| " + " | ".join("-" for _ in range(n_cols)) + " |")
    return "\n" + "\n".join(lines) + "\n"


def _convert_list(match: re.Match[str], ordered: bool) -> str:
    body = match.group(1)
    items = _LI_RE.findall(body)
    out: list[str] = []
    for i, raw in enumerate(items, start=1):
        text = _strip_tags(raw).strip()
        text = re.sub(r"\s+", " ", text)
        prefix = f"{i}. " if ordered else "- "
        out.append(prefix + text)
    return "\n" + "\n".join(out) + "\n" if out else ""


def _convert_heading(match: re.Match[str]) -> str:
    level = int(match.group(1))
    text = _strip_tags(match.group(2)).strip()
    text = re.sub(r"\s+", " ", text)
    return f"\n\n{'#' * level} {text}\n\n"


def _convert_pre(match: re.Match[str]) -> str:
    inner = match.group(1)
    # Strip nested tags inside <pre> but preserve text/code formatting.
    inner = _TAG_RE.sub("", inner)
    inner = _decode_entities(inner)
    # Trim a single leading/trailing newline introduced by formatting.
    inner = inner.replace("\r\n", "\n").replace("\r", "\n")
    if inner.startswith("\n"):
        inner = inner[1:]
    if inner.endswith("\n"):
        inner = inner[:-1]
    return f"\n```\n{inner}\n```\n"


def html_to_markdown(html: str) -> str:
    """Convert a HarmonyOS developer doc HTML fragment to Markdown.

    Implemented with the standard ``re`` module per task 3.1. Preserves code
    blocks (```), headings (#/##/###), lists (-/1.), tables (|), and links
    ([text](url)). Returns an empty string for empty/None input.
    """
    if not html or not html.strip():
        return ""

    text = html

    # 1. Drop script/style blocks entirely.
    text = _SCRIPT_RE.sub("", text)
    text = _STYLE_RE.sub("", text)

    # 2. Protect <pre> blocks first so later tag-stripping cannot corrupt
    #    their inner content. The placeholder stores the rendered markdown.
    pre_blocks: list[str] = []

    def _stash_pre(m: re.Match[str]) -> str:
        pre_blocks.append(_convert_pre(m))
        return f"\x00PRE{len(pre_blocks) - 1}\x00"

    text = _PRE_RE.sub(_stash_pre, text)

    # 3. Tables -> Markdown tables (before generic tag stripping).
    text = _TABLE_RE.sub(_convert_table, text)

    # 4. Lists (unordered then ordered). Handle nested lists by running the
    #    substitution a few times to flatten one level per pass.
    for _ in range(3):
        new_text = _UL_RE.sub(lambda m: _convert_list(m, ordered=False), text)
        if new_text == text:
            break
        text = new_text
    for _ in range(3):
        new_text = _OL_RE.sub(lambda m: _convert_list(m, ordered=True), text)
        if new_text == text:
            break
        text = new_text

    # 5. Headings.
    text = _H_RE.sub(_convert_heading, text)

    # 6. Links (double-quoted href first, then single-quoted).
    text = _A_RE.sub(r"[\2](\1)", text)
    text = _A_SQUOTE_RE.sub(r"[\2](\1)", text)

    # 7. Inline emphasis.
    text = _STRONG_RE.sub(r"**\1**", text)
    text = _EM_RE.sub(r"*\1*", text)

    # 8. Blockquotes.
    text = _BQ_RE.sub(lambda m: "\n> " + _strip_tags(m.group(1)).strip() + "\n", text)

    # 9. Inline <code> (after pre blocks are stashed, so this only hits
    #    non-pre inline code).
    text = _CODE_RE.sub(r"`\1`", text)

    # 10. Paragraph / line breaks / horizontal rules.
    text = _P_OPEN_RE.sub("\n\n", text)
    text = _P_CLOSE_RE.sub("\n", text)
    text = _BR_RE.sub("\n", text)
    text = _HR_RE.sub("\n---\n", text)

    # 11. Strip any remaining tags.
    text = _TAG_RE.sub("", text)

    # 12. Decode HTML entities.
    text = _decode_entities(text)

    # 13. Restore protected <pre> blocks.
    def _restore_pre(m: re.Match[str]) -> str:
        return pre_blocks[int(m.group(1))]

    text = re.sub(r"\x00PRE(\d+)\x00", _restore_pre, text)

    # 14. Collapse excessive blank lines and trailing whitespace.
    text = _BLANK_LINES_RE.sub("\n\n", text)
    text = _TRAILING_SPACES_RE.sub("\n", text)
    return text.strip()
