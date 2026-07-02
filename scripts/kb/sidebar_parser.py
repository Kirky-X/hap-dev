"""Sidebar markdown parser (tasks 4.2-4.3).

Parses HarmonyOS sidebar `.md` files into doc records. Each line of the form

    #### N.N.N. [title](url)
    #### N.N.N [title](url)

( exactly 4 hashes, a numbered heading, then a markdown link ) is one doc record.

The regex is fixed by the spec: `^####\\s+[\\d.]+\\s+\\[([^\\]]+)\\]\\(([^)]+)\\)`.
Lines whose `####` heading has plain text only (no `[title](url)` link) are NOT
doc records — they are category headers. This means device-api / device-dev
sidebars, which use plain-text `####` headings, yield zero records by design.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Exactly four hashes (a fifth '#' would occupy the position where \s is required,
# so ##### / ###### lines are excluded).
LINE_RE = re.compile(r"^####\s+[\d.]+\s+\[([^\]]+)\]\(([^)]+)\)")

# Map sidebar filename -> doc_type. Order matches the spec.
SIDEBAR_FILE_MAP: dict[str, str] = {
    "harmonyos-agc-help-sidebar.md": "agc-help",
    "harmonyos-app-api-references-sidebar.md": "app-api-references",
    "harmonyos-app-docs-sidebar-full.md": "app-docs",
    "harmonyos-architecture-guide-sidebar.md": "architecture-guide",
    "harmonyos-atomic-guide-sidebar.md": "atomic-guide",
    "harmonyos-best-practices-sidebar.md": "best-practices",
    "harmonyos-design-guide-sidebar.md": "design-guide",
    "harmonyos-device-api-sidebar.md": "device-api",
    "harmonyos-device-dev-sidebar.md": "device-dev",
}

NO_DESCRIPTION = "无描述"


def _now_iso() -> str:
    # ISO8601 with timezone; fromisoformat round-trips cleanly.
    return datetime.now(timezone.utc).isoformat()


def _make_id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def _make_content_hash(
    title: str,
    url: str,
    doc_type: str,
    description: str = NO_DESCRIPTION,
    links: list[str] | None = None,
) -> str:
    """Content fingerprint = sha1 over the doc's *content-bearing* fields.

    First-Principles fact F2: content_hash exists to flag docs that need
    re-embedding. Since description is the primary embedding source (design
    D2: embed from description when backfilled, else title), a description
    change MUST change the hash. links are included because they affect
    payload consistency (merge inspects them). Order-invariant on links
    (sorted) — membership is what counts, not insertion order.
    """
    sorted_links = sorted(links) if links else []
    raw = (
        title + url + doc_type + description
        + "|links:" + ",".join(sorted_links)
    ).encode("utf-8")
    return hashlib.sha1(raw).hexdigest()


def parse_sidebar(path: str, doc_type: str) -> list[dict[str, Any]]:
    """Parse a sidebar markdown file into a list of doc records.

    Each record has the 10-field schema (after B1+B4 upgrade):
      id, title, doc_type, url, description, links,
      created_at, updated_at, content_hash, embed_model.
    `embed_model` is initially "" — the indexer stamps it with the embedder's
    model_name on build/upsert. `embedding` (the vector) is intentionally NOT
    set here — the indexer computes it from `title` (or `description` after
    backfill).

    Raises FileNotFoundError if `path` does not exist (Rule 12: fail loud).
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"sidebar file not found: {path}")

    now = _now_iso()
    docs: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            m = LINE_RE.match(line)
            if not m:
                continue
            title, url = m.group(1), m.group(2)
            doc_id = _make_id(url)
            if doc_id in seen_ids:
                # duplicate URL within same sidebar — skip silently but deterministically
                continue
            seen_ids.add(doc_id)
            docs.append({
                "id": doc_id,
                "title": title,
                "doc_type": doc_type,
                "url": url,
                "description": NO_DESCRIPTION,
                "links": [],
                "created_at": now,
                "updated_at": now,
                "content_hash": _make_content_hash(
                    title, url, doc_type, NO_DESCRIPTION, [],
                ),
                # embed_model is "" until the indexer stamps it on build/upsert
                "embed_model": "",
            })
    return docs


def parse_all_sidebars(sidebars_dir: str) -> list[dict[str, Any]]:
    """Parse all 9 known sidebar files in `sidebars_dir` into a flat list."""
    base = Path(sidebars_dir)
    all_docs: list[dict[str, Any]] = []
    for fname, doc_type in SIDEBAR_FILE_MAP.items():
        fpath = base / fname
        if not fpath.exists():
            # Missing sidebar is an explicit error, not silent skip (Rule 12).
            raise FileNotFoundError(f"missing sidebar: {fpath}")
        all_docs.extend(parse_sidebar(str(fpath), doc_type))
    return all_docs
