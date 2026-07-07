"""scripts/test/platform.py 的单元测试。

覆盖任务 5.1/5.2 的所有断言点：
- detect_platform() 基于 sys.platform 返回 "linux"/"windows"/"macos"
- enabled_tools() Linux 仅 2 工具，Windows/macOS 全默认工具组
- generate_mcp_config() 生成含 DEVECO_PATH/PROJECT_PATH/ADDITIONAL_TOOL_GROUPS 的 MCP 配置
- Linux 时 additional_groups 强制为空字符串
- check_mcp_installed() 用 shutil.which + subprocess 检查 npx 与 @deveco-codegenie/mcp
- disabled_tools_hint(platform) Linux 返回精确禁用提示

测试通过 monkeypatch 修改 sys.platform，不真正安装 MCP。
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from typing import Any

import pytest

from scripts.test import platform as plat


# ---------------------------------------------------------------------------
# detect_platform
# ---------------------------------------------------------------------------


class TestDetectPlatform:
    def test_linux(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        assert plat.detect_platform() == "linux"

    def test_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        assert plat.detect_platform() == "windows"

    def test_macos(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")
        assert plat.detect_platform() == "macos"

    def test_unknown_platform_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """未知平台必须显式失败，不得静默退化（Rule 12）。"""
        monkeypatch.setattr(sys, "platform", "freebsd")
        with pytest.raises(ValueError):
            plat.detect_platform()


# ---------------------------------------------------------------------------
# enabled_tools
# ---------------------------------------------------------------------------

EXPECTED_FULL_TOOLS = [
    "check_ets_files",
    "check_cpp_files",
    "build_project",
    "start_app",
    "get_app_ui_tree",
    "perform_ui_action",
    "hilog",
    "harmonyos_knowledge_search",
    "project_sync",
    "init_project_path",
]

EXPECTED_LINUX_TOOLS = ["check_ets_files", "build_project"]

# 模拟器/运行时工具，Linux 必须禁用
SIMULATOR_TOOLS = [
    "start_app",
    "get_app_ui_tree",
    "perform_ui_action",
    "hilog",
    "verify_ui",
]


class TestEnabledTools:
    def test_linux_explicit(self) -> None:
        tools = plat.enabled_tools("linux")
        assert tools == EXPECTED_LINUX_TOOLS
        for disabled in SIMULATOR_TOOLS:
            assert disabled not in tools

    def test_windows_explicit(self) -> None:
        assert plat.enabled_tools("windows") == EXPECTED_FULL_TOOLS

    def test_macos_explicit(self) -> None:
        assert plat.enabled_tools("macos") == EXPECTED_FULL_TOOLS

    def test_linux_default_uses_sys_platform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        assert plat.enabled_tools() == EXPECTED_LINUX_TOOLS

    def test_win32_default_uses_sys_platform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        assert plat.enabled_tools() == EXPECTED_FULL_TOOLS

    def test_darwin_default_uses_sys_platform(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")
        assert plat.enabled_tools() == EXPECTED_FULL_TOOLS

    def test_unknown_platform_raises(self) -> None:
        with pytest.raises(ValueError):
            plat.enabled_tools("unknown_os")


# ---------------------------------------------------------------------------
# generate_mcp_config
# ---------------------------------------------------------------------------


class TestGenerateMcpConfig:
    def test_basic_structure(self) -> None:
        cfg = plat.generate_mcp_config("/opt/deveco", "/proj/harmony")
        assert cfg == {
            "mcpServers": {
                "deveco-mcp": {
                    "command": "npx",
                    "args": ["-y", "@deveco-codegenie/mcp"],
                    "env": {
                        "DEVECO_PATH": "/opt/deveco",
                        "PROJECT_PATH": "/proj/harmony",
                        "ADDITIONAL_TOOL_GROUPS": "",
                    },
                }
            }
        }

    def test_env_contains_all_three_keys(self) -> None:
        cfg = plat.generate_mcp_config("/d", "/p")
        env = cfg["mcpServers"]["deveco-mcp"]["env"]
        assert set(env.keys()) == {"DEVECO_PATH", "PROJECT_PATH", "ADDITIONAL_TOOL_GROUPS"}

    def test_command_is_npx_with_mcp_package(self) -> None:
        cfg = plat.generate_mcp_config("/d", "/p")
        server = cfg["mcpServers"]["deveco-mcp"]
        assert server["command"] == "npx"
        assert server["args"] == ["-y", "@deveco-codegenie/mcp"]

    def test_additional_groups_default_empty(self) -> None:
        cfg = plat.generate_mcp_config("/d", "/p")
        assert cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"] == ""

    def test_additional_groups_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        cfg = plat.generate_mcp_config(
            "/d", "/p", additional_groups="ui_integration_test,emulator_manager"
        )
        assert (
            cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"]
            == "ui_integration_test,emulator_manager"
        )

    def test_additional_groups_macos(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "darwin")
        cfg = plat.generate_mcp_config("/d", "/p", additional_groups="ui_integration_test")
        assert (
            cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"]
            == "ui_integration_test"
        )

    def test_linux_forces_additional_groups_empty(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Linux 时 additional_groups 必须强制为空字符串（模拟器工具组不可用）。"""
        monkeypatch.setattr(sys, "platform", "linux")
        cfg = plat.generate_mcp_config(
            "/d", "/p", additional_groups="ui_integration_test,emulator_manager"
        )
        assert cfg["mcpServers"]["deveco-mcp"]["env"]["ADDITIONAL_TOOL_GROUPS"] == ""

    def test_deveco_and_project_paths_propagated(self) -> None:
        cfg = plat.generate_mcp_config("/custom/deveco", "/custom/proj")
        env = cfg["mcpServers"]["deveco-mcp"]["env"]
        assert env["DEVECO_PATH"] == "/custom/deveco"
        assert env["PROJECT_PATH"] == "/custom/proj"


# ---------------------------------------------------------------------------
# disabled_tools_hint
# ---------------------------------------------------------------------------

EXPECTED_LINUX_HINT = (
    "模拟器测试工具(start_app/UI树/UI操作/hilog/verify_ui)需 Windows/macOS，"
    "当前 Linux 仅支持静态检查(check_ets_files/build_project)"
)


class TestDisabledToolsHint:
    def test_linux_hint_exact_message(self) -> None:
        assert plat.disabled_tools_hint("linux") == EXPECTED_LINUX_HINT

    def test_linux_hint_mentions_all_disabled_tools(self) -> None:
        hint = plat.disabled_tools_hint("linux")
        assert "start_app" in hint
        assert "hilog" in hint
        assert "verify_ui" in hint
        assert "check_ets_files" in hint
        assert "build_project" in hint
        assert "Windows/macOS" in hint or "Win/macOS" in hint

    def test_windows_hint_empty(self) -> None:
        assert plat.disabled_tools_hint("windows") == ""

    def test_macos_hint_empty(self) -> None:
        assert plat.disabled_tools_hint("macos") == ""

    def test_unknown_platform_raises(self) -> None:
        with pytest.raises(ValueError):
            plat.disabled_tools_hint("unknown_os")


# ---------------------------------------------------------------------------
# check_mcp_installed
# ---------------------------------------------------------------------------


class _FakeCompleted:
    def __init__(self, returncode: int, stdout: str = "", stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


class TestCheckMcpInstalled:
    def test_npx_missing_returns_false(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(shutil, "which", lambda cmd: None)
        assert plat.check_mcp_installed() is False

    def test_npx_present_mcp_locatable_returns_true(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            shutil, "which", lambda cmd: "/usr/bin/npx" if cmd == "npx" else None
        )

        def fake_run(cmd: list[str], **kwargs: Any) -> _FakeCompleted:
            return _FakeCompleted(0, stdout="1.0.0\n")

        monkeypatch.setattr(subprocess, "run", fake_run)
        assert plat.check_mcp_installed() is True

    def test_npx_present_mcp_not_locatable_returns_false(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            shutil, "which", lambda cmd: "/usr/bin/npx" if cmd == "npx" else None
        )

        def fake_run(cmd: list[str], **kwargs: Any) -> _FakeCompleted:
            return _FakeCompleted(1, stderr="not found")

        monkeypatch.setattr(subprocess, "run", fake_run)
        assert plat.check_mcp_installed() is False

    def test_subprocess_exception_returns_false(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """subprocess 抛异常时返回 False，不向上抛（探针性质）。"""
        monkeypatch.setattr(
            shutil, "which", lambda cmd: "/usr/bin/npx" if cmd == "npx" else None
        )

        def fake_run(cmd: list[str], **kwargs: Any) -> Any:
            raise FileNotFoundError("npx binary missing")

        monkeypatch.setattr(subprocess, "run", fake_run)
        assert plat.check_mcp_installed() is False
