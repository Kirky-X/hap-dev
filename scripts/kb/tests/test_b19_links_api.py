"""B19: links.py 改用 API 获取推荐 (Red phase).

update_links(doc_id, indexer, embedder) 三参（embedder 必传）：
1. 调用 recommend.get_recommendations(source.url) 获取推荐列表
2. 对每个推荐 url：
   - 已在 DB → 加双向 link
   - 不在 DB → fetch_content(url) 抓取 + indexer.upsert 嵌入新 doc + 加 link
3. 自链接跳过
4. embedder=None raise ValueError（fail-loud，禁止零向量污染）
5. API 失败 raise ValueError
"""
from __future__ import annotations

from unittest.mock import patch

import pytest

from scripts.kb.links import update_links
from scripts.kb.tests.conftest import make_doc


def _make_existing_target_doc(url: str, name: str = "已存在的目标文档") -> dict:
    """构造一个已存在于 DB 的 target doc。"""
    return make_doc(url=url, title=name)


def test_update_links_establishes_bidirectional_link_for_existing_target(indexer, fake_embedder):
    """B19-1: target 已在 DB → 加双向 link（不重算向量）。"""
    source = make_doc(url="https://example.com/source-existing")
    target = _make_existing_target_doc("https://example.com/target-existing", "目标文档A")
    indexer.upsert(source, fake_embedder)
    indexer.upsert(target, fake_embedder)
    source_id = source["id"]
    target_id = target["id"]

    fake_recommendations = [
        {"url": target["url"], "name": target["title"], "item_id": "target-existing"},
    ]
    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations):
        linked = update_links(source_id, indexer, fake_embedder)

    assert target_id in linked
    # 双向 link 已写入 DB
    stored_source = indexer.get(source_id)
    stored_target = indexer.get(target_id)
    assert target_id in stored_source["links"]
    assert source_id in stored_target["links"]


def test_update_links_fetches_and_upserts_missing_target(indexer, fake_embedder):
    """B19-2: target 不在 DB → fetch_content 抓取 + upsert 新 doc + 加 link。"""
    source = make_doc(url="https://example.com/source-missing-target")
    indexer.upsert(source, fake_embedder)
    source_id = source["id"]

    target_url = "https://example.com/target-missing"
    # target_url 的 sha1 id（与 _url_to_id 一致）
    import hashlib
    expected_target_id = hashlib.sha1(target_url.encode("utf-8")).hexdigest()

    fake_recommendations = [
        {"url": target_url, "name": "新抓取的目标", "item_id": "target-missing"},
    ]
    fake_context = "# 抓取到的内容\n\n这是网页原始 markdown。"

    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations), \
         patch("scripts.kb.links.fetch_content", return_value=fake_context):
        linked = update_links(source_id, indexer, fake_embedder)

    assert expected_target_id in linked
    # 新 doc 已写入 DB
    stored_target = indexer.get(expected_target_id)
    assert stored_target is not None
    assert stored_target["title"] == "新抓取的目标"
    assert stored_target["url"] == target_url
    assert stored_target["doc_type"] == "api-recommend"
    assert stored_target["context"] == fake_context
    assert stored_target["embed_model"] == fake_embedder.model_name
    # 双向 link
    stored_source = indexer.get(source_id)
    assert expected_target_id in stored_source["links"]
    assert source_id in stored_target["links"]


def test_update_links_skips_self_link(indexer, fake_embedder):
    """B19-3: API 返回 source 自身 url → 跳过（不建立自链接）。"""
    source = make_doc(url="https://example.com/source-self")
    indexer.upsert(source, fake_embedder)
    source_id = source["id"]

    fake_recommendations = [
        {"url": source["url"], "name": "自链接", "item_id": "source-self"},
    ]
    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations):
        linked = update_links(source_id, indexer, fake_embedder)

    assert linked == []
    stored = indexer.get(source_id)
    assert source_id not in stored["links"]


def test_update_links_api_failure_raises(indexer, fake_embedder):
    """B19-4: API 调用失败 raise ValueError（fail-loud，不静默返回空）。"""
    source = make_doc(url="https://example.com/source-api-fail")
    indexer.upsert(source, fake_embedder)

    with patch("scripts.kb.links.get_recommendations", side_effect=ValueError("API 500")):
        with pytest.raises(ValueError, match="API"):
            update_links(source["id"], indexer, fake_embedder)


def test_update_links_embedder_none_raises(indexer, fake_embedder):
    """B19-5: embedder=None raise ValueError（fail-loud，禁止零向量污染向量空间）。"""
    source = make_doc(url="https://example.com/source-emb-none")
    indexer.upsert(source, fake_embedder)

    with pytest.raises(ValueError, match="embedder"):
        update_links(source["id"], indexer, None)


def test_update_links_source_not_found_raises(indexer, fake_embedder):
    """B19-6: source doc 不存在 raise KeyError（fail-loud）。"""
    with pytest.raises(KeyError, match="doc_id"):
        update_links("nonexistent-source-id", indexer, fake_embedder)


def test_update_links_mixed_targets(indexer, fake_embedder):
    """B19-7: 混合场景——部分 target 已存在，部分需抓取，部分自链接。

    确保：已存在的加 link，不存在的抓取，自链接跳过。
    """
    source = make_doc(url="https://example.com/source-mixed")
    existing_target = _make_existing_target_doc(
        "https://example.com/target-existing-mixed", "已有目标"
    )
    indexer.upsert(source, fake_embedder)
    indexer.upsert(existing_target, fake_embedder)

    missing_target_url = "https://example.com/target-missing-mixed"

    fake_recommendations = [
        # 已存在
        {"url": existing_target["url"], "name": existing_target["title"], "item_id": "x1"},
        # 自链接
        {"url": source["url"], "name": "自链", "item_id": "x2"},
        # 缺失需抓取
        {"url": missing_target_url, "name": "新抓取目标", "item_id": "x3"},
    ]

    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations), \
         patch("scripts.kb.links.fetch_content", return_value="fake content"):
        linked = update_links(source["id"], indexer, fake_embedder)

    # 自链接跳过，其他两个都建立 link
    assert existing_target["id"] in linked
    import hashlib
    missing_id = hashlib.sha1(missing_target_url.encode("utf-8")).hexdigest()
    assert missing_id in linked
    assert len(linked) == 2

    # 双向 link 验证
    stored_source = indexer.get(source["id"])
    assert existing_target["id"] in stored_source["links"]
    assert missing_id in stored_source["links"]
    assert indexer.get(existing_target["id"])["links"].count(source["id"]) == 1
    assert indexer.get(missing_id)["links"].count(source["id"]) == 1


def test_update_links_idempotent(indexer, fake_embedder):
    """B19-8: 重复调用 update_links 不产生重复 link（幂等）。"""
    source = make_doc(url="https://example.com/source-idempotent")
    target = _make_existing_target_doc("https://example.com/target-idempotent", "幂等目标")
    indexer.upsert(source, fake_embedder)
    indexer.upsert(target, fake_embedder)

    fake_recommendations = [
        {"url": target["url"], "name": target["title"], "item_id": "x"},
    ]
    with patch("scripts.kb.links.get_recommendations", return_value=fake_recommendations):
        update_links(source["id"], indexer, fake_embedder)
        update_links(source["id"], indexer, fake_embedder)

    stored_source = indexer.get(source["id"])
    stored_target = indexer.get(target["id"])
    # 每边只有 1 个 link（不重复）
    assert stored_source["links"].count(target["id"]) == 1
    assert stored_target["links"].count(source["id"]) == 1
