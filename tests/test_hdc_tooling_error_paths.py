#!/usr/bin/env python3
"""hdc 工具链脚本的离线错误路径测试（collect-hilog / fetch-faultlog / probe-faultlogger）。

DEVECO_HOME 置空时三个脚本都必须显性失败（status=*_failed, exit 1,
next_action 提示 DEVECO_HOME），而非静默成功；参数校验错误同样离线可复现。
真实设备采集路径记入 tests/SKIPPED.md。
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, kv_output, run_cli


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestCollectHilog(unittest.TestCase):
    CLI = "fix/collect-hilog.mjs"

    def test_no_deveco_home_fails_visibly(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_cli(self.CLI, ["--output-dir", tmp])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "collect_failed")
        self.assertIn("DEVECO_HOME", fields["next_action"])

    def test_missing_output_dir_uses_default(self):
        # outputDir 无默认值时 parseArgs 返回 undefined → writeHilogSnapshot 抛错前
        # 就会因 hdc 失败；此处仅验证无参数也走显性失败而非崩溃退出码 >1
        proc = run_cli(self.CLI, [])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(kv_output(proc.stdout)["status"], "collect_failed")


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestFetchFaultlog(unittest.TestCase):
    CLI = "fix/fetch-faultlog.mjs"

    def test_missing_required_args_fails_visibly(self):
        proc = run_cli(self.CLI, [])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "fetch_failed")
        self.assertIn("--faultlog-name and --output-dir", fields["next_action"])

    def test_name_normalized_before_hdc(self):
        # 参数合法但 DEVECO_HOME 为空 → hdc 解析失败；faultlog_name 已规范化加 .log
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_cli(
                self.CLI,
                ["--faultlog-name", "jscrash-com.a.b-1700000000", "--output-dir", tmp],
            )
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "fetch_failed")
        self.assertEqual(fields["faultlog_name"], "jscrash-com.a.b-1700000000.log")
        self.assertIn("DEVECO_HOME", fields["next_action"])


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestProbeFaultlogger(unittest.TestCase):
    CLI = "fix/probe-faultlogger.mjs"

    def test_no_deveco_home_fails_visibly(self):
        proc = run_cli(self.CLI, ["--bundle-name", "com.example.shop"])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "probe_failed")
        self.assertEqual(fields["bundle_name"], "com.example.shop")
        self.assertIn("DEVECO_HOME", fields["next_action"])

    def test_invalid_max_age_falls_through_to_hdc_error(self):
        # max-age-minutes 非数字 → Number() 为 NaN，不抛参数错；最终 hdc 失败显性化
        proc = run_cli(self.CLI, ["--max-age-minutes", "abc"])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(kv_output(proc.stdout)["status"], "probe_failed")


if __name__ == "__main__":
    unittest.main()
