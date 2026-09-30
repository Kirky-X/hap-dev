#!/usr/bin/env python3
"""hap-dev 全部 .mjs 脚本语法冒烟：node --check 逐一校验（离线、无副作用）。"""
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, SCRIPTS_DIR, offline_env

MJS_FILES = [
    "create/copy-template.mjs",
    "create/detect-sdk.mjs",
    "fix/collect-hilog.mjs",
    "fix/fetch-faultlog.mjs",
    "fix/jscrash-report.mjs",
    "fix/parse-jscrash-log.mjs",
    "fix/probe-faultlogger.mjs",
    "fix/shared/hdc.mjs",
    "fix/shared/jscrash-faultlogger.mjs",
    "fix/shared/jscrash-parse.mjs",
    "fix/shared/utils.mjs",
]


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 冒烟")
class TestMjsSyntax(unittest.TestCase):
    def test_all_scripts_pass_node_check(self):
        for rel in MJS_FILES:
            with self.subTest(script=rel):
                path = os.path.join(SCRIPTS_DIR, rel)
                self.assertTrue(os.path.isfile(path), f"脚本缺失: {rel}")
                proc = subprocess.run(
                    [NODE, "--check", path],
                    capture_output=True,
                    text=True,
                    timeout=30,
                    env=offline_env(),
                )
                self.assertEqual(proc.returncode, 0, f"{rel} 语法错误: {proc.stderr}")

    def test_inventory_matches_scripts_dir(self):
        found = sorted(
            os.path.relpath(os.path.join(root, name), SCRIPTS_DIR)
            for root, _dirs, files in os.walk(SCRIPTS_DIR)
            for name in files
            if name.endswith(".mjs")
        )
        self.assertEqual(found, sorted(MJS_FILES))


if __name__ == "__main__":
    unittest.main()
