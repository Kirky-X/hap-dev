"""平台检测、工具组路由、MCP 配置生成、MCP 安装探针。

本模块是 test 子命令的"平台感知层"：根据 ``sys.platform`` 判定当前操作系统，
决定哪些 DevEco-MCP 工具可用，并据此生成 MCP server 启动配置或给出禁用提示。

核心约束（对应 references/commands/test.md）：

- **Linux 仅静态检查**：模拟器/运行时工具（start_app / get_app_ui_tree /
  perform_ui_action / hilog / verify_ui）在 Linux 不可用 —— DevEco-MCP 的
  UI 自动化依赖 Windows/macOS 上的 DevEco Studio 模拟器。Linux 强制
  ``ADDITIONAL_TOOL_GROUPS=""``，从源头杜绝 agent 误调用模拟器工具。
- **未知平台显式失败**（fail-loud，Rule 12）：detect_platform / enabled_tools /
  disabled_tools_hint 遇到未知 sys.platform 一律 raise ValueError，绝不静默
  退化为"某默认平台"——否则会在错误 OS 上误启用工具。
- **check_mcp_installed 为探针**：subprocess 异常时返回 False，不向上抛
  （探针性质，不应让一次探针失败炸掉整个 check 动作）。

模块仅依赖标准库（shutil/subprocess/sys），不引入第三方，方便在任意 Python
环境直接 ``python3 -m scripts.test.cli check``。
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from typing import Optional

# ---------------------------------------------------------------------------
# 平台 → 名称映射
# ---------------------------------------------------------------------------

# sys.platform 字符串 → 内部平台名（与执行计划 JSON 的 "platform" 字段一致）。
# 新增平台支持时在此扩展；命中不了即 fail-loud（见 detect_platform）。
_PLATFORM_MAP: dict[str, str] = {
    "linux": "linux",
    "win32": "windows",
    "darwin": "macos",
}


def detect_platform() -> str:
    """返回当前平台的内部名称：``linux`` / ``windows`` / ``macos``。

    基于 ``sys.platform``（测试通过 monkeypatch 覆写）。未知平台 raise
    ValueError —— 绝不静默退化，避免在未支持 OS 上误启用工具。

    Returns:
        ``linux`` / ``windows`` / ``macos``。

    Raises:
        ValueError: ``sys.platform`` 不在已知映射内。
    """
    name = _PLATFORM_MAP.get(sys.platform)
    if name is None:
        raise ValueError(
            f"detect_platform: 不支持的 sys.platform={sys.platform!r}; "
            f"expected one of {sorted(_PLATFORM_MAP.keys())}"
        )
    return name


# ---------------------------------------------------------------------------
# 平台 → 启用工具组
# ---------------------------------------------------------------------------

# Windows/macOS 全量默认工具组（与 DevEco-MCP 暴露的默认工具一一对应）。
# 顺序固定 —— references/commands/test.md 与契约测试都依赖此顺序。
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

# Linux 子集：仅静态检查（ArkTS LSP 诊断 + 编译）。模拟器工具全部禁用。
_LINUX_TOOLS: list[str] = ["check_ets_files", "build_project"]

# 模拟器/运行时工具，Linux 必须禁用（disabled_tools_hint 引用）。
_SIMULATOR_TOOLS: tuple[str, ...] = (
    "start_app",
    "get_app_ui_tree",
    "perform_ui_action",
    "hilog",
    "verify_ui",
)


def enabled_tools(platform: Optional[str] = None) -> list[str]:
    """返回指定平台启用的 MCP 工具名列表。

    Args:
        platform: 平台名；为 None 时取 ``detect_platform()``。

    Returns:
        工具名列表（顺序稳定）。Linux 返回 2 个静态工具，Windows/macOS
        返回 10 个全量工具。

    Raises:
        ValueError: 未知平台。
    """
    if platform is None:
        platform = detect_platform()
    if platform == "linux":
        return list(_LINUX_TOOLS)
    if platform in ("windows", "macos"):
        return list(_FULL_TOOLS)
    raise ValueError(
        f"enabled_tools: 未知平台 {platform!r}; expected one of ['linux', 'windows', 'macos']"
    )


# ---------------------------------------------------------------------------
# MCP 配置生成
# ---------------------------------------------------------------------------

# DevEco-MCP server 的启动命令与包名（与 references/commands/test.md 一致）。
_MCP_COMMAND = "npx"
_MCP_ARGS: list[str] = ["-y", "@deveco-codegenie/mcp"]


def generate_mcp_config(
    deveco_path: str,
    project_path: str,
    additional_groups: str = "",
) -> dict:
    """生成 DevEco-MCP server 的 MCP 配置 dict（可直接写入 .mcp.json）。

    结构::

        {"mcpServers": {"deveco-mcp": {
            "command": "npx",
            "args": ["-y", "@deveco-codegenie/mcp"],
            "env": {
                "DEVECO_PATH": ...,
                "PROJECT_PATH": ...,
                "ADDITIONAL_TOOL_GROUPS": ...,  # Linux 强制 ""
            },
        }}}

    Args:
        deveco_path: DevEco Studio 安装根目录（写入 ``DEVECO_PATH``）。
        project_path: 鸿蒙工程根路径（写入 ``PROJECT_PATH``）。
        additional_groups: 额外工具组（逗号分隔）。**Linux 强制为空字符串**
            —— 模拟器工具组在 Linux 不可用，从配置层杜绝误启用。

    Returns:
        MCP 配置 dict。
    """
    # Linux 强制清空 additional_groups：模拟器工具组不可用。
    # 直接读 sys.platform（与 detect_platform 同源），保持语义最直接。
    if sys.platform == "linux":
        additional_groups = ""
    return {
        "mcpServers": {
            "deveco-mcp": {
                "command": _MCP_COMMAND,
                "args": list(_MCP_ARGS),
                "env": {
                    "DEVECO_PATH": deveco_path,
                    "PROJECT_PATH": project_path,
                    "ADDITIONAL_TOOL_GROUPS": additional_groups,
                },
            }
        }
    }


# ---------------------------------------------------------------------------
# 禁用工具提示
# ---------------------------------------------------------------------------

# Linux 的精确禁用提示（契约 test_platform.py 期望逐字相等）。
_LINUX_DISABLED_HINT = (
    "模拟器测试工具(start_app/UI树/UI操作/hilog/verify_ui)需 Windows/macOS，"
    "当前 Linux 仅支持静态检查(check_ets_files/build_project)"
)


def disabled_tools_hint(platform: str) -> str:
    """返回指定平台的禁用工具提示字符串。

    Args:
        platform: 平台名（``linux``/``windows``/``macos``）。

    Returns:
        Linux 返回精确禁用提示；Windows/macOS 返回空串（无禁用项）。

    Raises:
        ValueError: 未知平台。
    """
    if platform == "linux":
        return _LINUX_DISABLED_HINT
    if platform in ("windows", "macos"):
        return ""
    raise ValueError(
        f"disabled_tools_hint: 未知平台 {platform!r}; "
        "expected one of ['linux', 'windows', 'macos']"
    )


# ---------------------------------------------------------------------------
# MCP 安装探针
# ---------------------------------------------------------------------------

# npx 探针超时（秒）：探针不得长时间挂起 check 动作。
_MCP_PROBE_TIMEOUT = 10

# 探针命令：--no-install 避免触发 npx 联网下载（仅本地已安装时才执行），
# --version 让包快速返回并退出，避免误启动 MCP server（会等 stdin）。
# 测试通过 monkeypatch subprocess.run 直接控 returncode，命令本身不影响契约。
_MCP_PROBE_ARGS: list[str] = ["--no-install", "@deveco-codegenie/mcp", "--version"]


def check_mcp_installed() -> bool:
    """探测本机是否已安装 DevEco-MCP（``@deveco-codegenie/mcp``）。

    流程：
      1. ``shutil.which("npx")`` 找不到 npx → 直接 False；
      2. 否则用 npx 探测 MCP 包是否可用（``--version``，``--no-install``
         不联网下载），returncode==0 → True；
      3. 任何 OSError / SubprocessError（含超时、二进制丢失）→ False。

    本函数为**探针性质**：失败只返回 False，不向上抛（一次探针失败不应
    炸掉整个 check 动作）。

    Returns:
        True 若 npx 存在且 MCP 包可定位；False 否则。
    """
    npx = shutil.which("npx")
    if not npx:
        return False
    try:
        result = subprocess.run(
            [npx, *_MCP_PROBE_ARGS],
            capture_output=True,
            text=True,
            timeout=_MCP_PROBE_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError):
        # FileNotFoundError / TimeoutExpired / 其他子进程错误 → 探针失败
        return False
    return result.returncode == 0
