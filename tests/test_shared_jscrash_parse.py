#!/usr/bin/env python3
"""fix/shared/jscrash-parse.mjs 纯函数离线测试（buildCrashReport / 格式化 / next_action）。"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, eval_mjs

CRASH_LOG = """Fault logger info:
Timestamp: 2026-09-30 10:00:00.000
bundleName: com.example.shop
processName: com.example.shop
pid: 12345
Uid: 10001
TypeError: Cannot read property 'name' of undefined
    at onInit (entry/src/main/ets/pages/Index.ets:25:13)
    at anonymous (oh_modules/.ohpm/lib/other.js:3:1)
"""

PLAIN_TEXT = "hello world nothing special here"

# 标准 faultlogger 形态：Reason → Error name → Error message 固定行序，
# Error name 与 Error message 两行都命中 CRASH_SIGNAL_RE
FAULTLOGGER_LOG = """Pid: 12345
Uid: 20020123
Process name: com.example.testapp
Reason: TypeError
Error name: TypeError
Error message: Cannot read property 'width' of null
Stacktrace:
    at onPageShow (entry/src/main/ets/pages/Index.ets:25:5)
    at anonymous (entry/src/main/ets/pages/Index.ets:12:1)
"""

MODULE = "fix/shared/jscrash-parse.mjs"


def build_report(log_text, source="text", device="default", bundle="", process=""):
    expr = (
        f"mod.buildCrashReport({json.dumps(log_text)}, "
        f"{json.dumps(source)}, {json.dumps(device)}, "
        f"{json.dumps(bundle)}, {json.dumps(process)})"
    )
    return eval_mjs(MODULE, expr)


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestBuildCrashReport(unittest.TestCase):
    def test_detected_full_signature(self):
        report = build_report(CRASH_LOG)
        self.assertEqual(report["status"], "detected")
        self.assertEqual(report["errorType"], "TypeError")
        self.assertEqual(report["bundle"], "com.example.shop")
        self.assertEqual(report["process"], "com.example.shop")
        self.assertIn("TypeError", report["errorMessage"])
        self.assertIn("Index.ets", report["suspectedFile"])

    def test_top_stack_frames_extracted(self):
        report = build_report(CRASH_LOG)
        self.assertEqual(len(report["topStack"]), 2)
        self.assertIn("Index.ets:25:13", report["topStack"][0])
        self.assertIn("other.js:3:1", report["topStack"][1])

    def test_application_frame_beats_ohpm_frame(self):
        report = build_report(CRASH_LOG)
        # 应用页帧得分高于 oh_modules 依赖帧
        self.assertIn("entry/src/main/ets/pages/Index.ets", report["suspectedFile"])

    def test_keywords_detected(self):
        report = build_report(CRASH_LOG)
        self.assertIn("typeerror", report["keywords"])

    def test_bundle_and_process_hint_override(self):
        report = build_report(
            CRASH_LOG, bundle="com.hint.app", process="myproc"
        )
        self.assertEqual(report["bundle"], "com.hint.app")
        self.assertEqual(report["process"], "myproc")

    def test_plain_text_no_crash_signature(self):
        report = build_report(PLAIN_TEXT)
        self.assertEqual(report["status"], "no_crash_signature")
        self.assertEqual(report["errorType"], "UnknownError")
        self.assertEqual(report["suspectedFile"], "(not found)")

    def test_faultlogger_error_message_takes_body_line(self):
        report = build_report(FAULTLOGGER_LOG)
        self.assertEqual(report["status"], "detected")
        # error_message 必须取真正的消息正文行，而非其前的 Error name 行
        self.assertEqual(report["errorMessage"], "Cannot read property 'width' of null")

    def test_device_and_source_fields(self):
        report = build_report(CRASH_LOG, source="file", device="emulator-9100")
        self.assertEqual(report["source"], "file")
        self.assertEqual(report["device"], "emulator-9100")


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestFormatting(unittest.TestCase):
    def test_next_action_detected(self):
        report = build_report(CRASH_LOG)
        action = eval_mjs(MODULE, f"mod.buildNextActionText({json.dumps(report)})")
        self.assertIn("Inspect", action)
        self.assertIn("Index.ets", action)

    def test_next_action_no_crash(self):
        report = build_report(PLAIN_TEXT)
        action = eval_mjs(MODULE, f"mod.buildNextActionText({json.dumps(report)})")
        self.assertIn("fuller crash log", action)

    def test_format_text_contains_fields(self):
        report = build_report(CRASH_LOG)
        text = eval_mjs(MODULE, f"mod.formatCrashReportText({json.dumps(report)})")
        self.assertIn("Crash signature detected.", text)
        self.assertIn("bundle: com.example.shop", text)
        self.assertIn("error_type: TypeError", text)
        self.assertIn("Top stack:", text)
        self.assertIn("Evidence excerpt:", text)


if __name__ == "__main__":
    unittest.main()
