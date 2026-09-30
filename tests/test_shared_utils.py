#!/usr/bin/env python3
"""fix/shared/utils.mjs 离线测试（toErrorMessage / printKv 输出格式）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, eval_mjs, kv_output, run_mjs_expr

MODULE = "fix/shared/utils.mjs"


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestUtils(unittest.TestCase):
    def test_error_message_from_error(self):
        value = eval_mjs(MODULE, "mod.toErrorMessage(new Error('boom'))")
        self.assertEqual(value, "boom")

    def test_error_message_from_plain_string(self):
        value = eval_mjs(MODULE, "mod.toErrorMessage('plain failure')")
        self.assertEqual(value, "plain failure")

    def test_print_kv_output_format(self):
        proc = run_mjs_expr(MODULE, "mod.printKv({ status: 'ok', count: 3 })")
        self.assertEqual(proc.returncode, 0)
        self.assertIn("status: ok", proc.stdout)
        self.assertIn("count: 3", proc.stdout)

    def test_print_kv_multiple_keys(self):
        proc = run_mjs_expr(
            MODULE, "mod.printKv({ a: 'x', b: 'y', c: 'z' })"
        )
        self.assertEqual(kv_output(proc.stdout), {"a": "x", "b": "y", "c": "z"})


if __name__ == "__main__":
    unittest.main()
