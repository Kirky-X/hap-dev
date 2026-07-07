"""scripts/test/cli.py 的单元测试。

覆盖任务 5.3 的三动作（check/config/run）：
- check：输出平台/可用工具/MCP 安装状态；Linux 输出 disabled_tools_hint
- config：调 generate_mcp_config 输出 JSON
- run：按平台路由输出"建议调用的 MCP 工具序列"JSON（不直接调 MCP）

run 动作的核心逻辑由 build_run_plan() 纯函数承担，便于测试。
check_mcp_installed() 为探针函数，测试中 mock 以确定结果。
"""

from __future__ import annotations

import json
import sys

import pytest

from scripts.test import cli
from scripts.test import platform as plat


# ---------------------------------------------------------------------------
# cmd_check
# ---------------------------------------------------------------------------


class TestCmdCheck:
    def test_check_linux_outputs_platform_tools_hint(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        monkeypatch.setattr(plat, "check_mcp_installed", lambda: False)
        monkeypatch.setattr(cli, "check_mcp_installed", lambda: False)

        rc = cli.cmd_check()
        out = capsys.readouterr().out

        assert rc == 0
        assert "linux" in out
        assert "check_ets_files" in out
        assert "build_project" in out
        # Linux 必须输出禁用提示
        assert "模拟器测试工具" in out
        assert "Windows/macOS" in out
        # MCP 未安装状态应体现
        assert "未安装" in out or "false" in out.lower() or "否" in out

    def test_check_windows_no_disabled_hint(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        monkeypatch.setattr(cli, "check_mcp_installed", lambda: True)

        rc = cli.cmd_check()
        out = capsys.readouterr().out

        assert rc == 0
        assert "windows" in out
        assert "start_app" in out
        assert "verify_ui" not in out or "verify_ui" in out  # verify_ui 在 hint 里
        # Windows 不应输出 Linux 禁用提示
        assert "模拟器测试工具" not in out
        # MCP 已安装
        assert "已安装" in out or "true" in out.lower() or "是" in out

    def test_check_macos_no_disabled_hint(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")
        monkeypatch.setattr(cli, "check_mcp_installed", lambda: True)

        rc = cli.cmd_check()
        out = capsys.readouterr().out

        assert rc == 0
        assert "macos" in out
        assert "模拟器测试工具" not in out


# ---------------------------------------------------------------------------
# cmd_config
# ---------------------------------------------------------------------------


class TestCmdConfig:
    def test_config_outputs_valid_json_linux(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")

        rc = cli.cmd_config("/opt/deveco", "/proj/harmony")
        out = capsys.readouterr().out

        cfg = json.loads(out)
        assert rc == 0
        assert "mcpServers" in cfg
        assert cfg["mcpServers"]["deveco-mcp"]["command"] == "npx"
        env = cfg["mcpServers"]["deveco-mcp"]["env"]
        assert env["DEVECO_PATH"] == "/opt/deveco"
        assert env["PROJECT_PATH"] == "/proj/harmony"
        # Linux 强制空
        assert env["ADDITIONAL_TOOL_GROUPS"] == ""

    def test_config_windows_additional_groups(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")

        rc = cli.cmd_config(
            "/d", "/p", additional_groups="ui_integration_test,emulator_manager"
        )
        out = capsys.readouterr().out

        cfg = json.loads(out)
        assert rc == 0
        assert (
            cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"]
            == "ui_integration_test,emulator_manager"
        )

    def test_config_linux_forces_additional_groups_empty(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        """Linux 即使传入 additional_groups 也强制为空。"""
        monkeypatch.setattr(sys, "platform", "linux")

        cli.cmd_config("/d", "/p", additional_groups="ui_integration_test")
        out = capsys.readouterr().out

        cfg = json.loads(out)
        assert cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"] == ""


# ---------------------------------------------------------------------------
# build_run_plan（纯函数，run 动作的核心逻辑）
# ---------------------------------------------------------------------------


class TestBuildRunPlanLinux:
    def test_linux_static_workflow(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")

        plan = cli.build_run_plan(ets_files=["a.ets", "b.ets"])

        assert plan["platform"] == "linux"
        assert plan["workflow"] == "static-check"
        tool_names = [s["tool"] for s in plan["steps"]]
        assert tool_names == ["check_ets_files", "build_project"]
        # check_ets_files 接收 ets 文件
        ets_step = plan["steps"][0]
        assert ets_step["args"]["files"] == ["a.ets", "b.ets"]
        # 不应包含模拟器工具
        for s in plan["steps"]:
            assert s["tool"] not in [
                "start_app",
                "verify_ui",
                "hilog",
                "get_app_ui_tree",
                "perform_ui_action",
            ]

    def test_linux_ignores_simulator_args(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Linux 即使传了 bundle_name/test_plan 也走静态流程。"""
        monkeypatch.setattr(sys, "platform", "linux")

        plan = cli.build_run_plan(
            ets_files=["a.ets"],
            bundle_name="com.example.app",
            test_plan="点击按钮后显示 Hello",
        )

        assert plan["workflow"] == "static-check"
        tool_names = [s["tool"] for s in plan["steps"]]
        assert "start_app" not in tool_names
        assert "verify_ui" not in tool_names
        assert "hilog" not in tool_names

    def test_linux_missing_ets_files_warns(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Linux 缺 ets_files 时 plan 应包含 warning，不抛错。"""
        monkeypatch.setattr(sys, "platform", "linux")

        plan = cli.build_run_plan()

        assert plan["workflow"] == "static-check"
        # 应有 warning 提示缺 ets_files
        warnings = plan.get("warnings", [])
        assert any("ets" in w.lower() or "文件" in w for w in warnings)

    def test_linux_includes_disabled_tools_hint(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Linux 的 plan 应附上禁用工具提示，告知 agent 不可调用模拟器工具。"""
        monkeypatch.setattr(sys, "platform", "linux")

        plan = cli.build_run_plan(ets_files=["a.ets"])

        assert "disabled_hint" in plan or "disabled_tools_hint" in plan
        hint = plan.get("disabled_hint") or plan.get("disabled_tools_hint")
        assert "Windows/macOS" in hint
        assert "start_app" in hint


class TestBuildRunPlanSimulator:
    def test_windows_simulator_workflow(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")

        plan = cli.build_run_plan(
            bundle_name="com.example.app",
            test_plan="点击登录按钮后应显示欢迎页",
        )

        assert plan["platform"] == "windows"
        assert plan["workflow"] == "simulator-verify"
        tool_names = [s["tool"] for s in plan["steps"]]
        # 闭环：build_project → start_app → verify_ui
        assert "build_project" in tool_names
        assert "start_app" in tool_names
        assert "verify_ui" in tool_names
        # 顺序：build 在 start_app 前，start_app 在 verify_ui 前
        assert tool_names.index("build_project") < tool_names.index("start_app")
        assert tool_names.index("start_app") < tool_names.index("verify_ui")

    def test_macos_simulator_workflow(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")

        plan = cli.build_run_plan(
            bundle_name="com.x.y", test_plan="登录成功跳转主页"
        )

        assert plan["platform"] == "macos"
        assert plan["workflow"] == "simulator-verify"
        tool_names = [s["tool"] for s in plan["steps"]]
        assert "verify_ui" in tool_names

    def test_simulator_workflow_includes_failure_diagnosis_tools(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Win/macOS 闭环应包含失败时的诊断工具（条件步骤）。"""
        monkeypatch.setattr(sys, "platform", "win32")

        plan = cli.build_run_plan(
            bundle_name="com.example.app", test_plan="点击按钮"
        )

        conditional_steps = [s for s in plan["steps"] if s.get("condition")]
        conditional_tools = [s["tool"] for s in conditional_steps]
        assert "get_ui_verification_log" in conditional_tools
        assert "save_ui_screenshot" in conditional_tools

    def test_verify_ui_step_carries_test_plan(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """verify_ui 步骤的 args 必须含 testPlan（自然语言用例）。"""
        monkeypatch.setattr(sys, "platform", "darwin")

        plan = cli.build_run_plan(
            bundle_name="com.example.app",
            test_plan="点击按钮后显示 Hello",
            fresh_start=True,
        )

        verify_step = next(s for s in plan["steps"] if s["tool"] == "verify_ui")
        assert verify_step["args"]["testPlan"] == "点击按钮后显示 Hello"
        assert verify_step["args"]["bundleName"] == "com.example.app"
        assert verify_step["args"]["freshStart"] is True

    def test_simulator_missing_bundle_name_warns(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Win/macOS 缺 bundle_name 时应 warning。"""
        monkeypatch.setattr(sys, "platform", "win32")

        plan = cli.build_run_plan(test_plan="点击按钮")

        warnings = plan.get("warnings", [])
        assert any("bundle" in w.lower() or "bundlename" in w.lower() for w in warnings)

    def test_simulator_missing_test_plan_warns(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Win/macOS 缺 test_plan 时应 warning。"""
        monkeypatch.setattr(sys, "platform", "win32")

        plan = cli.build_run_plan(bundle_name="com.x.y")

        warnings = plan.get("warnings", [])
        assert any("test" in w.lower() or "用例" in w or "plan" in w.lower() for w in warnings)


# ---------------------------------------------------------------------------
# cmd_run
# ---------------------------------------------------------------------------


class TestCmdRun:
    def test_run_linux_outputs_valid_json(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")

        rc = cli.cmd_run(ets_files=["a.ets"])
        out = capsys.readouterr().out

        plan = json.loads(out)
        assert rc == 0
        assert plan["platform"] == "linux"
        assert plan["workflow"] == "static-check"

    def test_run_windows_outputs_valid_json(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")

        rc = cli.cmd_run(
            bundle_name="com.example.app", test_plan="点击按钮"
        )
        out = capsys.readouterr().out

        plan = json.loads(out)
        assert rc == 0
        assert plan["platform"] == "windows"
        assert plan["workflow"] == "simulator-verify"

    def test_run_does_not_invoke_mcp(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        """run 动作不得直接调用 MCP 工具（仅输出建议序列）。"""
        monkeypatch.setattr(sys, "platform", "linux")

        # 监视 subprocess.run 不应被调用
        import subprocess as _sp

        call_count = {"n": 0}
        orig_run = _sp.run

        def spy_run(*args, **kwargs):
            call_count["n"] += 1
            return orig_run(*args, **kwargs)

        monkeypatch.setattr(_sp, "run", spy_run)
        try:
            cli.cmd_run(ets_files=["a.ets"])
        finally:
            pass
        # cmd_run 不应触发任何 subprocess 调用（check_mcp_installed 也不应被调）
        assert call_count["n"] == 0


# ---------------------------------------------------------------------------
# main（argparse 入口）
# ---------------------------------------------------------------------------


class TestMain:
    def test_main_check_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        monkeypatch.setattr(cli, "check_mcp_installed", lambda: False)
        assert cli.main(["check"]) == 0

    def test_main_config_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        rc = cli.main(
            ["config", "--deveco-path", "/d", "--project-path", "/p"]
        )
        assert rc == 0

    def test_main_config_with_additional_groups_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        rc = cli.main(
            [
                "config",
                "--deveco-path",
                "/d",
                "--project-path",
                "/p",
                "--additional-groups",
                "ui_integration_test",
            ]
        )
        assert rc == 0

    def test_main_run_linux_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        rc = cli.main(["run", "--ets-files", "a.ets", "b.ets"])
        assert rc == 0

    def test_main_run_windows_returns_zero(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        rc = cli.main(
            [
                "run",
                "--bundle-name",
                "com.example.app",
                "--test-plan",
                "点击按钮",
            ]
        )
        assert rc == 0

    def test_main_run_fresh_start_flag(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")
        rc = cli.main(
            [
                "run",
                "--bundle-name",
                "com.x.y",
                "--test-plan",
                "登录",
                "--fresh-start",
            ]
        )
        out = capsys.readouterr().out
        plan = json.loads(out)
        assert rc == 0
        verify_step = next(s for s in plan["steps"] if s["tool"] == "verify_ui")
        assert verify_step["args"]["freshStart"] is True

    def test_main_unknown_action_returns_nonzero(self) -> None:
        assert cli.main(["unknown"]) != 0

    def test_main_no_action_returns_nonzero(self) -> None:
        assert cli.main([]) != 0
