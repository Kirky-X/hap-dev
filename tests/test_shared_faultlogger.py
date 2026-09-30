#!/usr/bin/env python3
"""fix/shared/jscrash-faultlogger.mjs 纯函数离线测试
（faultlog 文件名提取 / bundle 过滤 / 时间戳排序 / 时效窗口）。
"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, eval_mjs

MODULE = "fix/shared/jscrash-faultlogger.mjs"


def call(fn, *args):
    expr = f"mod.{fn}({', '.join(json.dumps(a) for a in args)})"
    return eval_mjs(MODULE, expr)


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestExtractNames(unittest.TestCase):
    def test_extract_and_dedupe(self):
        text = (
            "jscrash-com.a.b-1700000000.log\n"
            "jscrash-com.a.b-1700000000.log\n"
            "jscrash-x.y-1700000001.log\n"
            "other-line.txt"
        )
        self.assertEqual(
            call("extractJscrashFaultlogNames", text),
            ["jscrash-com.a.b-1700000000.log", "jscrash-x.y-1700000001.log"],
        )

    def test_no_match_empty(self):
        self.assertEqual(call("extractJscrashFaultlogNames", "no logs here"), [])


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestParseFaultlogEntry(unittest.TestCase):
    def test_second_precision_multiplied(self):
        entry = call("parseFaultlogEntry", "jscrash-com.a.b-1700000000.log")
        self.assertEqual(entry["timestampMs"], 1700000000000)

    def test_millisecond_precision_kept(self):
        entry = call("parseFaultlogEntry", "jscrash-com.a.b-1700000000123.log")
        self.assertEqual(entry["timestampMs"], 1700000000123)

    def test_no_timestamp_null(self):
        entry = call("parseFaultlogEntry", "jscrash-com.a.b.log")
        self.assertIsNone(entry["timestampMs"])


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestFilterByBundle(unittest.TestCase):
    NAMES = [
        "jscrash-com.example.shop-1700000000.log",
        "jscrash-com.other.app-1700000001.log",
    ]

    def test_empty_bundle_keeps_all(self):
        self.assertEqual(call("filterFaultlogsByBundle", self.NAMES, ""), self.NAMES)

    def test_bundle_match(self):
        result = call("filterFaultlogsByBundle", self.NAMES, "com.example.shop")
        self.assertEqual(result, [self.NAMES[0]])

    def test_uid_suffix_stripped_from_bundle_part(self):
        names = ["jscrash-com.example.shop-10001-1700000000.log"]
        result = call("filterFaultlogsByBundle", names, "com.example.shop")
        self.assertEqual(result, names)

    def test_no_match_falls_back_to_all(self):
        result = call("filterFaultlogsByBundle", self.NAMES, "com.nothere.zzz")
        self.assertEqual(result, self.NAMES)


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestSortByRecency(unittest.TestCase):
    def test_newest_first_null_last_name_tiebreak(self):
        names = [
            "jscrash-b-1700000000.log",
            "jscrash-nots.log",
            "jscrash-a-1700000100.log",
            "jscrash-nots2.log",
        ]
        result = call("sortFaultlogsByRecency", names)
        self.assertEqual(
            result,
            [
                "jscrash-a-1700000100.log",
                "jscrash-b-1700000000.log",
                # 无时间戳按名称倒序稳定排尾
                "jscrash-nots2.log",
                "jscrash-nots.log",
            ],
        )


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestSelectWithinMaxAge(unittest.TestCase):
    # NOW-fresh=300s（恰好 5min，边界保留）、NOW-stale=400s（超出 5min 窗口）
    NAMES = [
        "jscrash-fresh-1700000100.log",
        "jscrash-stale-1700000000.log",
        "jscrash-nots.log",
    ]
    NOW = 1700000400000

    def test_window_filters_stale_keeps_null_ts(self):
        result = call("selectWithinMaxAge", self.NAMES, 5, self.NOW)
        self.assertEqual(result, ["jscrash-fresh-1700000100.log", "jscrash-nots.log"])

    def test_all_out_of_window_falls_back_to_all(self):
        result = call(
            "selectWithinMaxAge",
            ["jscrash-fresh-1700000100.log", "jscrash-stale-1700000000.log"],
            1,
            self.NOW,
        )
        self.assertEqual(
            result,
            ["jscrash-fresh-1700000100.log", "jscrash-stale-1700000000.log"],
        )

    def test_nonpositive_age_untouched(self):
        result = call("selectWithinMaxAge", self.NAMES, 0, self.NOW)
        self.assertEqual(result, self.NAMES)


if __name__ == "__main__":
    unittest.main()
