#!/usr/bin/env python3
"""create/detect-sdk.mjs 离线测试。

用临时目录伪造 DEVECO_HOME 结构（tools/node/bin/node + sdk/default/sdk-pkg.json）
覆盖真实探测逻辑；未设置时回退 apiLevel 22。
真实 DevEco Studio SDK 探测记入 tests/SKIPPED.md。
"""
import json
import os
import stat
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, eval_mjs

MODULE = "create/detect-sdk.mjs"


def _make_deveco_home(tmp, api_version):
    """构造 DEVECO_HOME 目录结构：tools/node/bin/node + sdk/default/sdk-pkg.json。"""
    node_bin = os.path.join(tmp, "tools", "node", "bin", "node")
    os.makedirs(os.path.dirname(node_bin), exist_ok=True)
    with open(node_bin, "w", encoding="utf-8") as fh:
        fh.write("#!/bin/sh\n")
    os.chmod(node_bin, os.stat(node_bin).st_mode | stat.S_IXUSR)

    sdk_dir = os.path.join(tmp, "sdk", "default")
    os.makedirs(sdk_dir, exist_ok=True)
    # 真实 sdk-pkg.json 中 apiVersion 是字符串（脚本 parse() 对非 string 直接回退）
    payload = {"data": {"apiVersion": str(api_version)}} if api_version is not None else {}
    with open(os.path.join(sdk_dir, "sdk-pkg.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh)
    return tmp


def detect_with_env(env_extra):
    return eval_mjs(MODULE, "mod.detectApiLevel()", env_extra=env_extra)


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestDetectApiLevel(unittest.TestCase):
    def test_no_deveco_home_fallback_22(self):
        result = detect_with_env({"DEVECO_HOME": ""})
        self.assertEqual(result, {"apiLevel": 22, "source": "fallback"})

    def test_sdk_pkg_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = _make_deveco_home(tmp, 20)
            result = eval_mjs(MODULE, "mod.detectApiLevel()", env_extra={"DEVECO_HOME": home})
        self.assertEqual(result["apiLevel"], 20)
        self.assertEqual(result["source"], "sdk_pkg")
        self.assertEqual(result["devecoHome"], home)
        self.assertIn("sdk-pkg.json", result["detectedFrom"])

    def test_invalid_api_version_falls_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = _make_deveco_home(tmp, 99)
            result = eval_mjs(MODULE, "mod.detectApiLevel()", env_extra={"DEVECO_HOME": home})
        self.assertEqual(result["apiLevel"], 22)
        self.assertEqual(result["source"], "fallback")
        self.assertEqual(result["devecoHome"], home)

    def test_home_without_node_binary_ignored(self):
        # DEVECO_HOME 指向存在但无 tools/node 的目录 → 视为未找到，回退
        with tempfile.TemporaryDirectory() as tmp:
            result = eval_mjs(MODULE, "mod.detectApiLevel()", env_extra={"DEVECO_HOME": tmp})
        self.assertEqual(result["source"], "fallback")
        self.assertEqual(result["apiLevel"], 22)

    def test_non_string_api_version_falls_back(self):
        # apiVersion 为数字（非 string）→ parse() 直接回退，不猜类型
        with tempfile.TemporaryDirectory() as tmp:
            home = _make_deveco_home(tmp, 20)
            with open(
                os.path.join(home, "sdk", "default", "sdk-pkg.json"),
                "w",
                encoding="utf-8",
            ) as fh:
                json.dump({"data": {"apiVersion": 20}}, fh)
            result = eval_mjs(MODULE, "mod.detectApiLevel()", env_extra={"DEVECO_HOME": home})
        self.assertEqual(result["apiLevel"], 22)
        self.assertEqual(result["source"], "fallback")

    def test_below_minimum_api_falls_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = _make_deveco_home(tmp, 15)
            result = eval_mjs(MODULE, "mod.detectApiLevel()", env_extra={"DEVECO_HOME": home})
        self.assertEqual(result["apiLevel"], 22)


if __name__ == "__main__":
    unittest.main()
