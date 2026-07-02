"""Bidirectional link extraction from doc content (tasks 4.10-4.11).

Parses a "相关推荐" / "相关文档" / "Related" section from a markdown body,
extracts referenced URLs (markdown links, <a href>, bare URLs), maps each URL to
its sha1 doc id, and writes the link bidirectionally:

    A.links += B.id   AND   B.links += A.id

Both docs' updated_at are refreshed. Payloads are updated in place via
`indexer.set_payload`, which does NOT re-embed (the spec's `update_links`
signature takes no embedder). Targets not present in the index are skipped (a
bidirectional link requires both endpoints to exist). Self-links are skipped.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from typing import Any

RELATED_HEADING_RE = re.compile(r"^#{1,6}\s+.*(相关推荐|相关文档|Related)", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
HTML_A_RE = re.compile(r"""<a\s+[^>]*?href=["']([^"']+)["']""", re.IGNORECASE)
BARE_URL_RE = re.compile(r"""https?://[^\s<>"')\]]+""")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _url_to_id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def _extract_related_block(content: str) -> str | None:
    """Return the text of the 相关推荐 block, or None if no such heading.

    The block starts at the matching heading and ends at the next heading of any
    level or at EOF.
    """
    lines = content.splitlines()
    start = None
    for i, line in enumerate(lines):
        if RELATED_HEADING_RE.match(line):
            start = i + 1
            break
    if start is None:
        return None
    block_lines = []
    for line in lines[start:]:
        if HEADING_RE.match(line):
            break
        block_lines.append(line)
    return "\n".join(block_lines)


def _extract_urls(block: str) -> list[str]:
    """Extract URLs from markdown links, <a href>, and bare URLs. Dedupe in order."""
    seen: set[str] = set()
    urls: list[str] = []
    # markdown links first (so [text](url) isn't double-counted as bare url)
    for _, url in MD_LINK_RE.findall(block):
        if url not in seen:
            seen.add(url)
            urls.append(url)
    for url in HTML_A_RE.findall(block):
        if url not in seen:
            seen.add(url)
            urls.append(url)
    # remove markdown-link spans before bare-url scan to avoid dupes
    stripped = MD_LINK_RE.sub(" ", block)
    stripped = HTML_A_RE.sub(" ", stripped)
    for url in BARE_URL_RE.findall(stripped):
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def update_links(doc_id: str, content_markdown: str, indexer: Any) -> list[str]:
    """Extract related-doc URLs from `content_markdown` and write bidirectional
    links between `doc_id` and each referenced doc that exists in the index.

    Returns the list of target doc ids that were (bidirectionally) linked.
    Raises KeyError if `doc_id` itself is not in the index (Rule 12).
    """
    source = indexer.get(doc_id)
    if source is None:
        raise KeyError(f"update_links: source doc_id not in index: {doc_id}")

    block = _extract_related_block(content_markdown)
    if block is None:
        return []

    urls = _extract_urls(block)
    now = _now_iso()
    linked: list[str] = []
    source_links: list[str] = list(source["links"])
    source_dirty = False

    for url in urls:
        target_id = _url_to_id(url)
        if target_id == doc_id:
            continue  # no self-link
        target = indexer.get(target_id)
        if target is None:
            continue  # target not indexed — cannot establish bidirectional link
        # forward: A.links += B.id
        if target_id not in source_links:
            source_links.append(target_id)
            source_dirty = True
        # backward: B.links += A.id
        target_links: list[str] = list(target["links"])
        target_dirty = False
        if doc_id not in target_links:
            target_links.append(doc_id)
            target_dirty = True
        if target_dirty:
            indexer.set_payload(target_id, {"links": target_links, "updated_at": now})
        linked.append(target_id)

    if source_dirty:
        indexer.set_payload(doc_id, {"links": source_links, "updated_at": now})

    return linked
