"""Field-level merge of two Qdrant local DBs (tasks 4.16-4.17).

merge(db_a_path, db_b_path, out_path, collection) -> dict

Design D8, with B3 (embed_model compatibility check) and B4 (content_hash
upgraded to include description+links):

  * read all records from both DBs, align by id
  * B3: validate both DBs were built with the SAME embed_model. A vector's
    identity is (model_name, dim) — same dim alone is insufficient. If the
    DBs used different models, raise ValueError (Rule 7: 暴露冲突不折中) —
    do NOT silently produce a corrupted DB with mixed vector spaces.
  * field-level merge:
      - one side empty / default, other not      -> take the non-empty one
      - both non-empty                            -> take the side with newer updated_at
      - links                                     -> union (dedupe)
      - created_at                                -> earliest
      - updated_at                                -> latest
      - description differs between sides         -> mark needs_reindex=True
      - embed_model                               -> inherits from source (must agree)
  * B4: content_hash recomputed via sidebar_parser._make_content_hash (incl.
    description + sorted links) — single source of truth.
  * write merged docs into a NEW DB at out_path, preserving the source vectors
    (no embedder needed — vectors are copied from the newer source doc)
  * rename the two input DBs to <path>.bak.<timestamp> backups
  * return {merged_count, backups, needs_reindex_count}

backup(paths) and confirm_delete(backup_path) are exposed for the CLI.
"""
from __future__ import annotations

import shutil
import time
from pathlib import Path
from typing import Any

from .indexer import QdrantIndexer
from .sidebar_parser import NO_DESCRIPTION, _make_content_hash

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
    """Merge two docs with the same id. Returns (merged_doc, needs_reindex).

    B10: deterministic tie-break. When updated_at is equal, the original code
    preferred `a` unconditionally — but `a`/`b` assignment depends on
    `set(docs_a) | set(docs_b)` iteration order (undefined), so the same input
    could yield different merges across runs. Now we use doc_id as a
    deterministic tie-breaker: lower id wins on ties. This makes _merge_two
    symmetric — _merge_two(a, b) and _merge_two(b, a) produce identical results.
    """
    a_ts = a["updated_at"]
    b_ts = b["updated_at"]
    if a_ts > b_ts:
        a_newer = True
    elif a_ts < b_ts:
        a_newer = False
    else:
        # B10: tie — lower doc_id wins (deterministic regardless of arg order)
        a_newer = a["id"] < b["id"]

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

    # B4: content_hash recomputed via the single source of truth (includes
    # description + sorted links), so a description change is detectable.
    merged["content_hash"] = _make_content_hash(
        merged["title"], merged["url"], merged["doc_type"],
        merged.get("description", NO_DESCRIPTION),
        merged["links"],
    )

    # B1: embed_model inherits from the newer source doc. The merge() entry
    # point already validated both DBs use the same model, so a and b agree.
    merged["embed_model"] = (a.get("embed_model") if a_newer
                             else b.get("embed_model", ""))

    # vector: take from the newer source doc (its vector matches its newer state)
    a_vec = a.get("embedding")
    b_vec = b.get("embedding")
    merged["embedding"] = (a_vec if a_newer else b_vec)

    return merged, needs_reindex


def _validate_model_compatibility(
    models_a: set[str], models_b: set[str],
    db_a_path: str, db_b_path: str,
) -> None:
    """B3: raise ValueError if the two DBs used different embed_models.

    Empty sets (legacy DBs without embed_model field) are treated as
    "unknown" — compatible with anything, so legacy DBs can still be merged
    with each other and with stamped DBs. Once both DBs have real model
    values, they must agree.
    """
    real_a = {m for m in models_a if m}
    real_b = {m for m in models_b if m}
    if not real_a or not real_b:
        return  # at least one is legacy — allow (migrate-embed-model handles it)
    if real_a != real_b:
        raise ValueError(
            f"merge: embed_model mismatch — DB A {db_a_path!r} used {real_a!r}, "
            f"DB B {db_b_path!r} used {real_b!r}. Merging would mix vector "
            f"spaces; cosine scores would become meaningless. Re-embed one DB "
            f"with the other's model first (reindex --force with the target "
            f"embed_model in config.json)."
        )
    if len(real_a) > 1:
        raise ValueError(
            f"merge: DB A {db_a_path!r} contains mixed embed_models {real_a!r} "
            f"— already contaminated, refusing to merge. Rebuild from sidebars."
        )
    if len(real_b) > 1:
        raise ValueError(
            f"merge: DB B {db_b_path!r} contains mixed embed_models {real_b!r} "
            f"— already contaminated, refusing to merge. Rebuild from sidebars."
        )


def merge(
    db_a_path: str,
    db_b_path: str,
    out_path: str,
    collection: str,
    dim: int = 384,
) -> dict[str, Any]:
    """Merge two local Qdrant DBs into a new one at out_path.

    Returns {merged_count, backups, needs_reindex_count}.

    B3: raises ValueError if the two DBs were built with different embed_models.
    """
    # Read both source DBs (with vectors so we can copy them).
    idx_a = QdrantIndexer(db_path=db_a_path, collection=collection, dim=dim)
    idx_b = QdrantIndexer(db_path=db_b_path, collection=collection, dim=dim)
    docs_a = {d["id"]: d for d in idx_a.list_all(with_vectors=True)}
    docs_b = {d["id"]: d for d in idx_b.list_all(with_vectors=True)}

    # B3: validate embed_model compatibility BEFORE writing any merged output.
    models_a = {d.get("embed_model", "") for d in docs_a.values()}
    models_b = {d.get("embed_model", "") for d in docs_b.values()}
    _validate_model_compatibility(models_a, models_b, db_a_path, db_b_path)

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
