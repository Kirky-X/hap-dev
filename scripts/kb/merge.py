"""Field-level merge of two Qdrant local DBs (tasks 4.16-4.17).

merge(db_a_path, db_b_path, out_path, collection) -> dict

Design D8:
  * read all records from both DBs, align by id
  * field-level merge:
      - one side empty / default, other not      -> take the non-empty one
      - both non-empty                            -> take the side with newer updated_at
      - links                                     -> union (dedupe)
      - created_at                                -> earliest
      - updated_at                                -> latest
      - description differs between sides         -> mark needs_reindex=True
  * write merged docs into a NEW DB at out_path, preserving the source vectors
    (no embedder needed — vectors are copied from the newer source doc)
  * rename the two input DBs to <path>.bak.<timestamp> backups
  * return {merged_count, backups, needs_reindex_count}

backup(paths) and confirm_delete(backup_path) are exposed for the CLI.
"""
from __future__ import annotations

import hashlib
import shutil
import time
from pathlib import Path
from typing import Any

from .indexer import QdrantIndexer
from .sidebar_parser import NO_DESCRIPTION

# Fields merged by the "non-empty priority, else newer wins" rule.
_SCALAR_FIELDS = ["title", "doc_type", "url", "description"]


def _is_empty(field: str, value: Any) -> bool:
    if value is None:
        return True
    if field == "description":
        return value == NO_DESCRIPTION or value == ""
    if field == "links":
        return value == [] or value is None
    return value == ""


def _merge_scalar(field: str, a_val: Any, b_val: Any, a_newer: bool) -> Any:
    a_empty = _is_empty(field, a_val)
    b_empty = _is_empty(field, b_val)
    if a_empty and not b_empty:
        return b_val
    if b_empty and not a_empty:
        return a_val
    if a_empty and b_empty:
        return a_val  # both empty -> default
    # both non-empty -> newer wins
    return a_val if a_newer else b_val


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def _merge_two(a: dict[str, Any], b: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    """Merge two docs with the same id. Returns (merged_doc, needs_reindex)."""
    a_newer = a["updated_at"] >= b["updated_at"]

    a_desc = a.get("description", NO_DESCRIPTION)
    b_desc = b.get("description", NO_DESCRIPTION)
    needs_reindex = (a_desc != b_desc)

    merged: dict[str, Any] = {"id": a["id"]}
    for field in _SCALAR_FIELDS:
        merged[field] = _merge_scalar(field, a.get(field), b.get(field), a_newer)

    # links: union
    merged["links"] = _dedupe(list(a.get("links", [])) + list(b.get("links", [])))

    # timestamps
    merged["created_at"] = min(a["created_at"], b["created_at"])
    merged["updated_at"] = max(a["updated_at"], b["updated_at"])

    # content_hash: recompute from merged identity fields
    merged["content_hash"] = hashlib.sha1(
        (merged["title"] + merged["url"] + merged["doc_type"]).encode("utf-8")
    ).hexdigest()

    # vector: take from the newer source doc (its vector matches its newer state)
    a_vec = a.get("embedding")
    b_vec = b.get("embedding")
    merged["embedding"] = (a_vec if a_newer else b_vec)

    return merged, needs_reindex


def merge(
    db_a_path: str,
    db_b_path: str,
    out_path: str,
    collection: str,
    dim: int = 384,
) -> dict[str, Any]:
    """Merge two local Qdrant DBs into a new one at out_path.

    Returns {merged_count, backups, needs_reindex_count}.
    """
    # Read both source DBs (with vectors so we can copy them).
    idx_a = QdrantIndexer(db_path=db_a_path, collection=collection, dim=dim)
    idx_b = QdrantIndexer(db_path=db_b_path, collection=collection, dim=dim)
    docs_a = {d["id"]: d for d in idx_a.list_all(with_vectors=True)}
    docs_b = {d["id"]: d for d in idx_b.list_all(with_vectors=True)}
    idx_a.close()
    idx_b.close()

    all_ids = set(docs_a) | set(docs_b)
    merged_docs: list[dict[str, Any]] = []
    needs_reindex_count = 0
    for did in all_ids:
        a = docs_a.get(did)
        b = docs_b.get(did)
        if a is not None and b is None:
            merged_docs.append(a)
        elif b is not None and a is None:
            merged_docs.append(b)
        else:
            assert a is not None and b is not None
            m, needs = _merge_two(a, b)
            if needs:
                needs_reindex_count += 1
            merged_docs.append(m)

    # Write the merged DB, preserving source vectors (no embedder).
    idx_out = QdrantIndexer(db_path=out_path, collection=collection, dim=dim)
    idx_out._ensure_collection(recreate=True)
    for m in merged_docs:
        vec = m.get("embedding")
        if vec is None:
            raise RuntimeError(
                f"merge: doc {m['id']} has no source vector to preserve"
            )
        idx_out.put(m, vec)
    idx_out.close()

    # Back up the two source DBs by renaming.
    backups = backup([db_a_path, db_b_path])

    return {
        "merged_count": len(merged_docs),
        "backups": backups,
        "needs_reindex_count": needs_reindex_count,
    }


def backup(paths: list[str]) -> list[str]:
    """Rename each existing path to <path>.bak.<timestamp>. Non-existent paths
    are skipped (and omitted from the returned list)."""
    ts = time.strftime("%Y%m%d%H%M%S", time.localtime()) + f".{time.time_ns() % 1_000_000:06d}"
    out: list[str] = []
    for p in paths:
        src = Path(p)
        if not src.exists():
            continue
        dst = Path(f"{p}.bak.{ts}")
        # prefer atomic rename; fall back to recursive move across filesystems
        try:
            src.rename(dst)
        except OSError:
            shutil.move(str(src), str(dst))
        out.append(str(dst))
    return out


def confirm_delete(backup_path: str) -> None:
    """Permanently delete a backup directory. Raises FileNotFoundError if missing
    (Rule 12: don't pretend a delete succeeded when the path didn't exist)."""
    p = Path(backup_path)
    if not p.exists():
        raise FileNotFoundError(f"backup not found: {backup_path}")
    if p.is_dir():
        shutil.rmtree(p)
    else:
        p.unlink()
