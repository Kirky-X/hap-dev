"""test 子命令 - 平台检测与 MCP 工具启用策略。

设计决策 D7：检测 sys.platform，Windows/macOS 启用模拟器工具，Linux 仅启用静态检查。

@deveco-codegenie/mcp 的模拟器控制类工具（start_app/get_app_ui_tree/perform_ui_action/
hilog/verify_ui）仅支持 Windows/macOS；Linux 仅支持 check_ets_files（ArkTS LSP 诊断）
与 build_project。本模块负责：
1. 检测当前平台
2. 按平台返回启用的 MCP 工具列表
3. 生成 MCP 配置（DEVECO_PATH/PROJECT_PATH/ADDITIONAL_TOOL_GROUPS）
4. 探测 @deveco-codegenie/mcp 是否可调用
5. 给出禁用工具的提示文本
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from typing import Optional

__all__ = [
    "detect_platform",
    "enabled_tools",
    "generate_mcp_config",
    "check_mcp_installed",
    "disabled_tools_hint",
]

# MCP 包名（npx 调用）
MCP_PACKAGE = "@deveco-codegenie/mcp"

# Windows/macOS 启用的全部默认工具组（按 MCP 工具清单顺序）
_FULL_TOOLS: list[str] = [
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

# Linux 仅启用静态检查 + 构建（模拟器工具不可用）
_LINUX_TOOLS: list[str] = ["check_ets_files", "build_project"]

# Linux 禁用工具的提示文本（任务描述给定的精确字符串）
_LINUX_DISABLED_HINT = (
    "模拟器测试工具(start_app/UI树/UI操作/hilog/verify_ui)需 Windows/macOS，"
    "当前 Linux 仅支持静态检查(check_ets_files/build_project)"
)

# sys.platform → 内部平台名映射
_PLATFORM_MAP: dict[str, str] = {
    "linux": "linux",
    "win32": "windows",
    "darwin": "macos",
}


def detect_platform() -> str:
    """检测当前操作系统平台。

    返回 "linux" / "windows" / "macos"。
    未知平台抛 ValueError（Rule 12：失败显性化，不静默退化）。
    """
    plat_name = _PLATFORM_MAP.get(sys.platform)
    if plat_name is None:
        raise ValueError(
            f"不支持的平台 sys.platform={sys.platform!r}，"
            f"仅支持 linux/win32/darwin"
        )
    return plat_name


def enabled_tools(platform: Optional[str] = None) -> list[str]:
    """返回当前平台启用的 MCP 工具列表。

    Args:
        platform: 平台名（"linux"/"windows"/"macos"）。None 时调用 detect_platform()。

    Returns:
        Linux 返回 ["check_ets_files", "build_project"]；
        Windows/macOS 返回全部默认工具组（10 个）。
    """
    if platform is None:
        platform = detect_platform()
    if platform == "linux":
        return list(_LINUX_TOOLS)
    if platform in ("windows", "macos"):
        return list(_FULL_TOOLS)
    raise ValueError(
        f"未知平台 {platform!r}，仅支持 linux/windows/macos"
    )


def generate_mcp_config(
    deveco_path: str,
    project_path: str,
    additional_groups: Optional[str] = None,
) -> dict:
    """生成 @deveco-codegenie/mcp 的 MCP 配置 dict。

    结构：
        {"mcpServers": {"deveco-mcp": {
            "command": "npx",
            "args": ["-y", "@deveco-codegenie/mcp"],
            "env": {
                "DEVECO_PATH": <deveco_path>,
                "PROJECT_PATH": <project_path>,
                "ADDITIONAL_TOOL_GROUPS": <additional_groups or "">
            }
        }}}

    Linux 平台时 additional_groups 强制为空字符串（模拟器工具组不可用，禁用激活）。
    """
    # Linux 强制清空 additional_groups（模拟器工具组在 Linux 无意义）
    if detect_platform() == "linux":
        effective_additional = ""
    else:
        effective_additional = additional_groups or ""

    return {
        "mcpServers": {
            "deveco-mcp": {
                "command": "npx",
                "args": ["-y", MCP_PACKAGE],
                "env": {
                    "DEVECO_PATH": deveco_path,
                    "PROJECT_PATH": project_path,
                    "ADDITIONAL_TOOL_GROUPS": effective_additional,
                },
            }
        }
    }


def check_mcp_installed() -> bool:
    """探测 npx 与 @deveco-codegenie/mcp 是否可调用。

    策略：
    1. shutil.which("npx") 检查 npx 可执行文件存在
    2. subprocess 调用 npx -y @deveco-codegenie/mcp --version（或等价命令）
       验证包可定位

    返回 bool。任何异常（npx 缺失/包未安装/网络错误）均返回 False，
    因为这是一个探针函数，不向上抛（CLI 层会据此提示用户手动安装）。
    """
    if shutil.which("npx") is None:
        return False
    try:
        result = subprocess.run(
            ["npx", "-y", MCP_PACKAGE, "--version"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (FileNotFoundError, subprocess.SubprocessError, OSError):
        return False
    return result.returncode == 0


def disabled_tools_hint(platform: Optional[str] = None) -> str:
    """返回禁用工具的提示文本。

    Args:
        platform: 平台名。None 时调用 detect_platform()。

    Returns:
        Linux 返回模拟器工具禁用提示；Windows/macOS 返回空字符串。
    """
    if platform is None:
        platform = detect_platform()
    if platform == "linux":
        return _LINUX_DISABLED_HINT
    if platform in ("windows", "macos"):
        return ""
    raise ValueError(
        f"未知平台 {platform!r}，仅支持 linux/windows/macos"
    )
