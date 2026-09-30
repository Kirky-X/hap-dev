#!/usr/bin/env python3
"""fix/parse-jscrash-log.mjs CLI 端到端离线测试（--log-text/--log-file 全离线路径）。"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, kv_output, run_cli

CLI = "fix/parse-jscrash-log.mjs"

CRASH_LOG = """Fault logger info:
bundleName: com.example.shop
processName: com.example.shop
TypeError: Cannot read property 'name' of undefined
    at onInit (entry/src/main/ets/pages/Index.ets:25:13)
"""


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestParseJscrashLogCli(unittest.TestCase):
    def test_detected_exit_0(self):
        proc = run_cli(CLI, ["--log-text", CRASH_LOG])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "detected")
        self.assertEqual(fields["error_type"], "TypeError")
        self.assertEqual(fields["source"], "text")
        self.assertIn("Index.ets", fields["suspected_file"])
        self.assertTrue(fields["keywords"])

    def test_plain_text_no_crash_signature_exit_0(self):
        proc = run_cli(CLI, ["--log-text", "nothing wrong here"])
        self.assertEqual(proc.returncode, 0)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "no_crash_signature")

    def test_include_text_prints_full_report(self):
        proc = run_cli(CLI, ["--log-text", CRASH_LOG, "--include-text"])
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Crash signature detected.", proc.stdout)
        self.assertIn("Top stack:", proc.stdout)

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
            self.assertEqual(fields["status"], "detected")
            self.assertEqual(fields["source"], "file")
        finally:
            os.unlink(path)

    def test_both_sources_conflict_exit_1(self):
        proc = run_cli(CLI, ["--log-text", "a", "--log-file", "b"])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "parse_failed")
        self.assertIn("--log-file or --log-text", fields["next_action"])

    def test_no_source_exit_1(self):
        proc = run_cli(CLI, [])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(kv_output(proc.stdout)["status"], "parse_failed")

    def test_missing_value_exit_1(self):
        proc = run_cli(CLI, ["--log-file"])
        self.assertEqual(proc.returncode, 1)

    def test_missing_log_file_exit_1(self):
        proc = run_cli(CLI, ["--log-file", "/nonexistent/dir/crash.log"])
        self.assertEqual(proc.returncode, 1)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["status"], "parse_failed")
        self.assertIn("log file not found", fields["next_action"])

    def test_device_and_source_override(self):
        proc = run_cli(
            CLI,
            ["--log-text", CRASH_LOG, "--device", "emulator-9100", "--source", "hilog"],
        )
        self.assertEqual(proc.returncode, 0)
        fields = kv_output(proc.stdout)
        self.assertEqual(fields["source"], "hilog")


if __name__ == "__main__":
    unittest.main()
