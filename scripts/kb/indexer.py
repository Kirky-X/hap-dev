"""Qdrant local-mode indexer (tasks 4.6-4.7).

Stores the 9-field doc schema in a local Qdrant collection. The payload holds all
non-vector fields; the vector is computed from `description` when it has been
backfilled (i.e. != "无描述"), otherwise from `title` (per design D2).

Point ids are stable unsigned 64-bit ints derived from the doc's sha1 id, so
repeated `build` / `upsert` calls are idempotent (same id -> overwrite).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

from .sidebar_parser import NO_DESCRIPTION

# Payload field holding the doc id (the sha1 hex string). Qdrant point ids must
# be ints or UUIDs, so we keep the sha1 in payload and derive an int point id.
ID_FIELD = "id"


def _point_id(doc_id: str) -> int:
    """Stable uint64 point id from the first 16 hex chars of the sha1 id."""
    return int(doc_id[:16], 16)


def _embed_text(doc: dict[str, Any]) -> str:
    """D2: embed from description if backfilled, else from title."""
    desc = doc.get("description", NO_DESCRIPTION)
    if desc and desc != NO_DESCRIPTION:
        return desc
    return doc["title"]


class QdrantIndexer:
    def __init__(self, db_path: str, collection: str, dim: int = 384) -> None:
        self.db_path = db_path
        self.collection = collection
        self.dim = dim
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.client = QdrantClient(path=db_path)

    # ---- lifecycle --------------------------------------------------------

    def close(self) -> None:
        try:
            self.client.close()
        except Exception:
            pass

    def _ensure_collection(self, recreate: bool = False) -> None:
        vcfg = qm.VectorParams(size=self.dim, distance=qm.Distance.COSINE)
        exists = self.client.collection_exists(self.collection)
        if recreate:
            if exists:
                self.client.delete_collection(collection_name=self.collection)
            self.client.create_collection(collection_name=self.collection, vectors_config=vcfg)
            return
        if not exists:
            self.client.create_collection(collection_name=self.collection, vectors_config=vcfg)

    # ---- write ------------------------------------------------------------

    def build(self, docs: list[dict[str, Any]], embedder: Any) -> None:
        """Recreate the collection and index all `docs` from scratch.

        Idempotent: calling build twice with the same docs yields the same count
        because recreate drops stale points and upsert overwrites by point id.

        B1: each doc's payload is stamped with `embedder.model_name` so the
        stored vector's *identity* (not just its dim) is auditable later.
        """
        self._ensure_collection(recreate=True)
        if not docs:
            return
        # Stamp the embedder's model_name onto every doc — this is the single
        # source of truth for "which model produced this vector". A doc dict
        # arriving with a stale embed_model (e.g. from an old config) is
        # overwritten here because the embedder just produced the vector.
        for d in docs:
            d["embed_model"] = embedder.model_name
        texts = [_embed_text(d) for d in docs]
        vectors = embedder.embed_batch(texts)
        if len(vectors) != len(docs):
            raise ValueError(
                f"embed_batch returned {len(vectors)} vectors for {len(docs)} docs"
            )
        for v in vectors:
            if len(v) != self.dim:
                raise ValueError(
                    f"embedding dim {len(v)} != collection dim {self.dim}"
                )
        points = [
            qm.PointStruct(id=_point_id(d["id"]), vector=v, payload=self._payload(d))
            for d, v in zip(docs, vectors)
        ]
        self.client.upsert(collection_name=self.collection, points=points)

    def upsert(self, doc: dict[str, Any], embedder: Any) -> None:
        """Insert or overwrite a single doc; (re)compute its vector.

        B1: stamps `embedder.model_name` into the doc before writing.
        """
        self._ensure_collection(recreate=False)
        doc["embed_model"] = embedder.model_name
        vec = embedder.embed(_embed_text(doc))
        if len(vec) != self.dim:
            raise ValueError(
                f"embedding dim {len(vec)} != collection dim {self.dim}"
            )
        point = qm.PointStruct(id=_point_id(doc["id"]), vector=vec, payload=self._payload(doc))
        self.client.upsert(collection_name=self.collection, points=[point])

    def _payload(self, doc: dict[str, Any]) -> dict[str, Any]:
        """Payload = all schema fields except the vector.

        B1: includes `embed_model` as the 10th field. Old docs without it
        read back as "" via `_payload_from` (legacy tolerance).
        """
        return {
            ID_FIELD: doc["id"],
            "title": doc["title"],
            "doc_type": doc["doc_type"],
            "url": doc["url"],
            "description": doc.get("description", NO_DESCRIPTION),
            "links": doc.get("links", []),
            "created_at": doc["created_at"],
            "updated_at": doc["updated_at"],
            "content_hash": doc["content_hash"],
            "embed_model": doc.get("embed_model", ""),
        }

    # ---- read -------------------------------------------------------------

    def get(self, doc_id: str) -> Optional[dict[str, Any]]:
        """Retrieve a single doc by its sha1 id, or None if absent."""
        self._ensure_collection(recreate=False)
        flt = qm.Filter(must=[qm.FieldCondition(key=ID_FIELD, match=qm.MatchValue(value=doc_id))])
        res, _ = self.client.scroll(
            collection_name=self.collection,
            scroll_filter=flt,
            limit=1,
            with_payload=True,
            with_vectors=True,
        )
        if not res:
            return None
        return self._point_to_doc(res[0])

    def list_all(self, with_vectors: bool = False) -> list[dict[str, Any]]:
        """Return all docs. By default payload-only; pass with_vectors=True to
        also include the stored vector under the ``embedding`` key (used by merge
        to preserve existing vectors without re-embedding)."""
        self._ensure_collection(recreate=False)
        out: list[dict[str, Any]] = []
        offset = None
        while True:
            res, offset = self.client.scroll(
                collection_name=self.collection,
                limit=256,
                offset=offset,
                with_payload=True,
                with_vectors=with_vectors,
            )
            out.extend(self._point_to_doc(p, include_vector=with_vectors) for p in res)
            if offset is None:
                break
        return out

    def put(self, doc: dict[str, Any], vector: list[float]) -> None:
        """Write a doc with an EXPLICIT precomputed vector (no embedder). Used by
        merge to preserve existing vectors when copying docs into a new DB."""
        self._ensure_collection(recreate=False)
        if len(vector) != self.dim:
            raise ValueError(
                f"vector dim {len(vector)} != collection dim {self.dim}"
            )
        point = qm.PointStruct(id=_point_id(doc["id"]), vector=vector, payload=self._payload(doc))
        self.client.upsert(collection_name=self.collection, points=[point])

    def count_by_type(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for d in self.list_all():
            t = d["doc_type"]
            counts[t] = counts.get(t, 0) + 1
        return counts

    def count(self) -> int:
        """Total number of points in the collection."""
        self._ensure_collection(recreate=False)
        return self.client.count(collection_name=self.collection, exact=True).count

    def set_payload(self, doc_id: str, fields: dict[str, Any]) -> None:
        """Update payload fields of an existing doc in place, WITHOUT touching
        its vector. Used by links.py to write bidirectional links / refreshed
        updated_at without re-embedding (the spec's update_links signature takes
        no embedder). Raises if the point doesn't exist (Rule 12: fail loud)."""
        self._ensure_collection(recreate=False)
        existing = self.get(doc_id)
        if existing is None:
            raise KeyError(f"cannot set_payload: doc_id not in index: {doc_id}")
        self.client.set_payload(
            collection_name=self.collection,
            payload=fields,
            points=[_point_id(doc_id)],
        )

    def search(self, vector: list[float], top_k: int,
               doc_type: Optional[str] = None) -> list[dict[str, Any]]:
        """Vector search helper used by query.py. Returns docs with score."""
        self._ensure_collection(recreate=False)
        query_filter = None
        if doc_type:
            query_filter = qm.Filter(must=[
                qm.FieldCondition(key="doc_type", match=qm.MatchValue(value=doc_type))
            ])
        res = self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=top_k,
            query_filter=query_filter,
            with_payload=True,
            with_vectors=False,
        )
        out = []
        for s in res.points:
            doc = self._payload_from(s.payload)
            doc["score"] = float(s.score)
            out.append(doc)
        return out

    # ---- helpers ----------------------------------------------------------

    @staticmethod
    def _payload_from(payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": payload[ID_FIELD],
            "title": payload["title"],
            "doc_type": payload["doc_type"],
            "url": payload["url"],
            "description": payload.get("description", NO_DESCRIPTION),
            "links": payload.get("links", []) or [],
            "created_at": payload["created_at"],
            "updated_at": payload["updated_at"],
            "content_hash": payload["content_hash"],
            # B1: legacy tolerance — pre-B1 docs lack this field; treat as "".
            # Use `or ""` to also coerce None (left over by some Qdrant ops).
            "embed_model": payload.get("embed_model") or "",
        }

    def get_embed_models(self) -> set[str]:
        """B1: return the set of distinct embed_model values in the DB.

        Empty set = no docs. Set with single "" = legacy DB (all docs lack
        embed_model). Set with multiple non-empty values = mixed DB
        (cross-model contamination — caller should fail loud).
        Used by query/merge/reindex to validate model compatibility.
        """
        models: set[str] = set()
        for d in self.list_all():
            models.add(d.get("embed_model", ""))
        return models

    @classmethod
    def _point_to_doc(cls, point: Any, include_vector: bool = True) -> dict[str, Any]:
        doc = cls._payload_from(point.payload)
        if include_vector:
            v = point.vector
            if hasattr(v, "get") and "vector" in v:
                v = v["vector"]
            doc["embedding"] = list(v) if v is not None else []
        return doc
