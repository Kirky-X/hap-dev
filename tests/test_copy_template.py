#!/usr/bin/env python3
"""create/copy-template.mjs 端到端离线测试。

参数校验与结构化错误码（exit 1/2/3/4）为真实行为；复制/替换/校验逻辑用
临时模板目录覆盖，另对仓内真实模板（references/project-template/application，
只读）做一次冒烟。真实 hvigor 构建记入 tests/SKIPPED.md。
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _mjs_harness import NODE, REPO_ROOT, run_cli

CLI = "create/copy-template.mjs"
REAL_TEMPLATE = os.path.join(REPO_ROOT, "references", "project-template", "application")


def make_template(root):
    """构造满足 REQUIRED_FILES 与替换点要求的最小模板。"""
    files = {
        "build-profile.json5": '{"product": "6.0.2(22)"}',
        "hvigor/hvigor-config.json5": '{"model": "6.0.2"}',
        "oh-package.json5": '{"model": "6.0.2"}',
        "AppScope/resources/base/media/layered_image.json": "{}",
        "AppScope/resources/base/media/background.png": "png",
        "AppScope/resources/base/media/foreground.png": "png",
        "entry/src/main/resources/base/media/layered_image.json": "{}",
        "entry/src/main/resources/base/media/background.png": "png",
        "entry/src/main/resources/base/media/foreground.png": "png",
        "AppScope/resources/base/element/string.json": '{"name": "MyApplication"}',
        "AppScope/app.json5": '{"bundle": "com.example.myapplication"}',
    }
    for rel, content in files.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    return root


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def stderr_json(proc):
    return json.loads(proc.stderr)


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestArgValidation(unittest.TestCase):
    def test_missing_project_path_exit_1(self):
        proc = run_cli(CLI, ["--app-name", "MyApp"])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Missing required argument --project-path", proc.stderr)

    def test_missing_app_name_exit_1(self):
        proc = run_cli(CLI, ["--project-path", "/tmp/x"])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Missing required argument --app-name", proc.stderr)

    def test_invalid_app_name_exit_4(self):
        proc = run_cli(CLI, ["--project-path", "/tmp/x", "--app-name", "1Bad-Name"])
        self.assertEqual(proc.returncode, 4)
        payload = stderr_json(proc)
        self.assertEqual(payload["code"], "APP_NAME_INVALID")
        self.assertIn("rawAppName", payload)

    def test_unsupported_api_level_exit_1(self):
        proc = run_cli(
            CLI,
            ["--project-path", "/tmp/x", "--app-name", "MyApp", "--api-level", "99"],
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Unsupported apiLevel", proc.stderr)

    def test_template_dir_not_found_exit_3(self):
        proc = run_cli(
            CLI,
            [
                "--project-path", "/tmp/x",
                "--app-name", "MyApp",
                "--template-dir", "/nonexistent/template/dir",
            ],
        )
        self.assertEqual(proc.returncode, 3)
        payload = stderr_json(proc)
        self.assertEqual(payload["code"], "TEMPLATE_DIR_NOT_FOUND")


@unittest.skipUnless(NODE, "node 不存在，跳过 .mjs 测试")
class TestCopyFlow(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.template = make_template(os.path.join(self._tmp.name, "template"))
        self.work = os.path.join(self._tmp.name, "work")
        os.makedirs(self.work, exist_ok=True)

    def tearDown(self):
        self._tmp.cleanup()

    def _args(self, extra=None):
        return [
            "--template-dir", self.template,
            "--project-path", self.work,
            "--app-name", "ShopApp",
            "--bundle-name", "com.acme.shop",
            *(extra or []),
        ]

    def test_success_api_level_20_rewrites_versions(self):
        proc = run_cli(CLI, self._args(["--api-level", "20"]))
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        result = json.loads(proc.stdout)
        self.assertTrue(result["verified"])
        self.assertEqual(result["apiLevel"], 20)
        self.assertEqual(result["source"], "user_input")
        self.assertEqual(result["bundleName"], "com.acme.shop")

        target = os.path.join(self.work, "ShopApp")
        self.assertIn("6.0.0(20)", read(target, "build-profile.json5"))
        self.assertIn("6.0.0", read(target, "hvigor/hvigor-config.json5"))
        self.assertIn("6.0.0", read(target, "oh-package.json5"))
        self.assertIn("ShopApp", read(target, "AppScope/resources/base/element/string.json"))
        self.assertIn("com.acme.shop", read(target, "AppScope/app.json5"))

    def test_api_level_22_keeps_files_untouched(self):
        proc = run_cli(CLI, self._args(["--api-level", "22"]))
        self.assertEqual(proc.returncode, 0)
        target = os.path.join(self.work, "ShopApp")
        self.assertIn("6.0.2(22)", read(target, "build-profile.json5"))

    def test_default_bundle_name_from_app_name(self):
        proc = run_cli(
            CLI,
            [
                "--template-dir", self.template,
                "--project-path", self.work,
                "--app-name", "ShopApp",
                "--api-level", "22",
            ],
        )
        self.assertEqual(proc.returncode, 0)
        result = json.loads(proc.stdout)
        self.assertEqual(result["bundleName"], "com.example.shopapp")

    def test_existing_target_exit_2(self):
        first = run_cli(CLI, self._args(["--api-level", "22"]))
        self.assertEqual(first.returncode, 0)
        second = run_cli(CLI, self._args(["--api-level", "22"]))
        self.assertEqual(second.returncode, 2)
        payload = stderr_json(second)
        self.assertEqual(payload["code"], "PROJECT_EXISTS")

    def test_template_files_complete(self):
        proc = run_cli(CLI, self._args(["--api-level", "22"]))
        self.assertEqual(proc.returncode, 0)
        target = os.path.join(self.work, "ShopApp")
        for rel in (
            "build-profile.json5",
            "AppScope/resources/base/media/background.png",
            "entry/src/main/resources/base/media/foreground.png",
        ):
            self.assertTrue(os.path.isfile(os.path.join(target, rel)), rel)


@unittest.skipUnless(
    NODE and os.path.isdir(REAL_TEMPLATE), "node 不存在或仓内真实模板缺失"
)
class TestRealTemplateSmoke(unittest.TestCase):
    def test_real_template_copy_smoke(self):
        # 只读真实模板，输出到临时目录（api-level 22 跳过版本改写）
        with tempfile.TemporaryDirectory() as work:
            proc = run_cli(
                CLI,
                [
                    "--project-path", work,
                    "--app-name", "SmokeApp",
                    "--api-level", "22",
                ],
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            result = json.loads(proc.stdout)
            self.assertTrue(result["verified"])
            self.assertEqual(result["source"], "user_input")
            self.assertTrue(
                os.path.isfile(
                    os.path.join(work, "SmokeApp", "build-profile.json5")
                )
            )


if __name__ == "__main__":
    unittest.main()
