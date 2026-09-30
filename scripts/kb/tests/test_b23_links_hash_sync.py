"""B23: links.py update_links 写入 links 后必须刷新 content_hash。

update_links 在 set_payload 写入新 links 时只写 `links`+`updated_at`，
未写 `content_hash`。links 是 content_hash 公式的输入字段之一（B4），
links 变化后 hash 与实际 links 脱钩——后续 reindex(force=False) 会
误判 doc 未变化而跳过重嵌入（即使向量已 stale）。

修复：在两处 set_payload 调用前用 _make_content_hash 重算 hash（含
context），写入 payload 的 content_hash 字段。对照实现：links_auto.py
_persist_links 已正确重算 hash 并写入。
"""
from __future__ import annotations

from unittest.mock import patch

from scripts.kb.links import update_links
from scripts.kb.sidebar_parser import NO_DESCRIPTION, _make_content_hash
from scripts.kb.tests.conftest import make_doc


def test_update_links_persists_content_hash_for_target(indexer, fake_embedder):
    """target 持久化时 payload 含 content_hash，且等于用新 links+context 重算。"""
    source = make_doc(url="https://example.com/source-target-hash")
    target = make_doc(
        url="https://example.com/target-hash",
        title="目标文档",
        context="target-ctx",
    )
    indexer.upsert(source, fake_embedder)
    indexer.upsert(target, fake_embedder)

    fake_recommendations = [
        {"url": target["url"], "name": target["title"], "item_id": "x"},
    ]

    # 拦截 set_payload 以记录 target 的 payload
    captured_payloads: list[tuple[str, dict]] = []
    real_set_payload = indexer.set_payload

    def spy_set_payload(doc_id: str, fields: dict) -> None:
        captured_payloads.append((doc_id, dict(fields)))
        return real_set_payload(doc_id, fields)

    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations), \
         patch.object(indexer, "set_payload", side_effect=spy_set_payload):
        update_links(source["id"], indexer, fake_embedder)

    # 找到 target 的 set_payload 调用
    target_payloads = [p for did, p in captured_payloads if did == target["id"]]
    assert target_payloads, "target 必须被 set_payload 持久化"
    target_payload = target_payloads[-1]

    # content_hash 键必须在 payload 中
    assert "content_hash" in target_payload, (
        "target set_payload 的 payload 必须含 content_hash 键"
    )

    # 重算预期 hash：用 target 当前的 links（已加 source_id）+ context
    stored_target = indexer.get(target["id"])
    expected_hash = _make_content_hash(
        target["title"], target["url"], target["doc_type"],
        target.get("description", NO_DESCRIPTION),
        stored_target["links"],  # 已含新加的 source_id
        context=target.get("context", ""),
    )
    assert target_payload["content_hash"] == expected_hash, (
        "target content_hash 必须基于新 links + 当前 context 重算"
    )


def test_update_links_persists_content_hash_for_source(indexer, fake_embedder):
    """source 持久化时 payload 含 content_hash，且等于用新 links+context 重算。"""
    source = make_doc(
        url="https://example.com/source-source-hash",
        context="source-ctx",
    )
    target = make_doc(url="https://example.com/target-source-hash", title="目标")
    indexer.upsert(source, fake_embedder)
    indexer.upsert(target, fake_embedder)

    fake_recommendations = [
        {"url": target["url"], "name": target["title"], "item_id": "x"},
    ]

    captured_payloads: list[tuple[str, dict]] = []
    real_set_payload = indexer.set_payload

    def spy_set_payload(doc_id: str, fields: dict) -> None:
        captured_payloads.append((doc_id, dict(fields)))
        return real_set_payload(doc_id, fields)

    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations), \
         patch.object(indexer, "set_payload", side_effect=spy_set_payload):
        update_links(source["id"], indexer, fake_embedder)

    # 找到 source 的 set_payload 调用
    source_payloads = [p for did, p in captured_payloads if did == source["id"]]
    assert source_payloads, "source 必须被 set_payload 持久化"
    source_payload = source_payloads[-1]

    assert "content_hash" in source_payload, (
        "source set_payload 的 payload 必须含 content_hash 键"
    )

    # 重算预期 hash：用 source 当前的 links（已加 target_id）+ context
    stored_source = indexer.get(source["id"])
    expected_hash = _make_content_hash(
        source["title"], source["url"], source["doc_type"],
        source.get("description", NO_DESCRIPTION),
        stored_source["links"],  # 已含新加的 target_id
        context=source.get("context", ""),
    )
    assert source_payload["content_hash"] == expected_hash, (
        "source content_hash 必须基于新 links + 当前 context 重算"
    )


def test_update_links_hash_reflects_new_links(indexer, fake_embedder):
    """content_hash 必须反映新 links——加 link 前后 hash 不同。"""
    source = make_doc(url="https://example.com/source-reflect")
    target = make_doc(url="https://example.com/target-reflect", title="目标")
    indexer.upsert(source, fake_embedder)
    indexer.upsert(target, fake_embedder)

    # 加 link 前的 hash（source.links == []）
    hash_before = indexer.get(source["id"])["content_hash"]

    fake_recommendations = [
        {"url": target["url"], "name": target["title"], "item_id": "x"},
    ]
    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations):
        update_links(source["id"], indexer, fake_embedder)

    # 加 link 后的 hash（source.links == [target_id]）
    hash_after = indexer.get(source["id"])["content_hash"]
    assert hash_after != hash_before, (
        "加 link 后 content_hash 必须变化 —— 证明 hash 反映新 links"
    )
