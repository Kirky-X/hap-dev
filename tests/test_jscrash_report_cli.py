#!/usr/bin/env python3
"""fix/jscrash-report.mjs CLI 离线路径测试。

--log-text / --log-file 输入不触碰 hdc（真实设备 hilog 采集记入 tests/SKIPPED.md）；
无输入时走 hdc 解析失败路径（DEVECO_HOME 置空保证离线可复现）。
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, kv_output, run_cli

CLI = "fix/jscrash-report.mjs"

CRASH_LOG = """bundleName: com.example.shop
TypeError: uncaught exception
    at onPageShow (entry/src/main/ets/pages/Index.ets:10:5)
"""


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestJscrashReportCli(unittest.TestCase):
    def test_log_text_offline_path(self):
        proc = run_cli(CLI, ["--log-text", CRASH_LOG])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "detected")
        self.assertEqual(fields["source"], "text")
        self.assertEqual(fields["error_type"], "TypeError")

    def test_log_file_source(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".log", delete=False, encoding="utf-8"
        ) as fh:
            fh.write(CRASH_LOG)
            path = fh.name
        try:
            proc = run_cli(CLI, ["--log-file", path])
            self.assertEqual(proc.returncode, 0)
            fields = kv_output(proc.stdout)
            self.assertEqual(fields["source"], "file")
            self.assertEqual(fields["status"], "detected")
        finally:
            os.unlink(path)

    def test_include_text_report(self):
        proc = run_cli(CLI, ["--log-text", CRASH_LOG, "--include-text"])
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Crash signature detected.", proc.stdout)

    def test_lines_out_of_range_exit_1(self):
        proc = run_cli(CLI, ["--log-text", CRASH_LOG, "--lines", "100"])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "parse_failed")
        self.assertIn("between 200 and 10000", fields["next_action"])

    def test_both_inputs_conflict_exit_1(self):
        proc = run_cli(CLI, ["--log-text", "a", "--log-file", "b"])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(kv_output(proc.stdout)["status"], "parse_failed")

    def test_no_input_fails_visible_without_deveco(self):
        # 无 --log-text/--log-file → 尝试 hdc 采集；DEVECO_HOME 为空 → 显性失败
        proc = run_cli(CLI, [])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "parse_failed")
        self.assertIn("DEVECO_HOME", fields["next_action"])

    def test_device_id_forwarded_in_detected_path(self):
        proc = run_cli(
            CLI, ["--log-text", CRASH_LOG, "--device-id", "127.0.0.1:5555"]
        )
        self.assertEqual(proc.returncode, 0)
        # device_id 不改变离线解析结果（仅记录在报告中）
        self.assertEqual(kv_output(proc.stdout)["status"], "detected")


if __name__ == "__main__":
    unittest.main()
