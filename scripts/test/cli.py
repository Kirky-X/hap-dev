"""test 子命令 CLI 入口。

用法：
    python3 -m scripts.test.cli check
    python3 -m scripts.test.cli config --deveco-path <path> --project-path <path> \
        [--additional-groups <groups>]
    python3 -m scripts.test.cli run [--ets-files f1.ets f2.ets] \
        [--bundle-name <name>] [--test-plan <plan>] [--fresh-start]

三动作：
- check：检测平台/可用工具/MCP 安装状态；Linux 输出禁用提示
- config：生成 MCP 配置 JSON（DEVECO_PATH/PROJECT_PATH/ADDITIONAL_TOOL_GROUPS）
- run：按平台路由输出"建议调用的 MCP 工具序列"JSON 供 agent 执行
       （不直接调 MCP——MCP server 由 agent 层启动调用）

设计决策 D7：
- Linux: check_ets_files(传入 .ets 文件) → build_project
- Win/macOS: build_project → start_app → verify_ui(自然语言用例) →
  失败时 get_ui_verification_log + save_ui_screenshot
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional

from scripts.test.platform import (
    check_mcp_installed,
    detect_platform,
    disabled_tools_hint,
    enabled_tools,
    generate_mcp_config,
)

__all__ = [
    "cmd_check",
    "cmd_config",
    "build_run_plan",
    "cmd_run",
    "main",
]


# ---------------------------------------------------------------------------
# check 动作
# ---------------------------------------------------------------------------


def cmd_check() -> int:
    """输出平台/可用工具/MCP 安装状态；Linux 输出禁用工具提示。"""
    pf = detect_platform()
    tools = enabled_tools(pf)
    installed = check_mcp_installed()
    print(f"平台: {pf}")
    print(f"启用工具: {', '.join(tools)}")
    print(f"MCP 安装: {'是' if installed else '否'}")
    if pf == "linux":
        print(disabled_tools_hint(pf))
    return 0


# ---------------------------------------------------------------------------
# config 动作
# ---------------------------------------------------------------------------


def cmd_config(
    deveco_path: str,
    project_path: str,
    additional_groups: Optional[str] = None,
) -> int:
    """生成 MCP 配置并输出 JSON。"""
    cfg = generate_mcp_config(deveco_path, project_path, additional_groups)
    print(json.dumps(cfg, indent=2, ensure_ascii=False))
    return 0


# ---------------------------------------------------------------------------
# run 动作（核心逻辑在 build_run_plan 纯函数）
# ---------------------------------------------------------------------------


def build_run_plan(
    ets_files: Optional[list[str]] = None,
    bundle_name: Optional[str] = None,
    test_plan: Optional[str] = None,
    fresh_start: bool = False,
) -> dict:
    """构建建议调用的 MCP 工具序列（不执行 MCP，仅生成计划 JSON）。

    Linux: check_ets_files(传入 .ets 文件) → build_project
    Win/macOS: build_project → start_app → verify_ui →
              失败时 get_ui_verification_log + save_ui_screenshot
    """
    pf = detect_platform()
    warnings: list[str] = []

    if pf == "linux":
        if not ets_files:
            warnings.append(
                "未提供 --ets-files，check_ets_files 将扫描工程内所有 .ets 文件"
            )
        steps = [
            {
                "tool": "check_ets_files",
                "args": {"files": list(ets_files) if ets_files else []},
                "purpose": "ArkTS LSP 诊断（语法/类型错误）",
            },
            {
                "tool": "build_project",
                "args": {},
                "purpose": "编译工程",
            },
        ]
        return {
            "platform": "linux",
            "workflow": "static-check",
            "steps": steps,
            "on_failure": (
                "check_ets_files 返回错误时停止流程，调 fix 子命令修复后重跑；"
                "build_project 失败时调 fix 子命令修复编译错误"
            ),
            "disabled_hint": disabled_tools_hint(pf),
            "warnings": warnings,
        }

    # Win/macOS 模拟器验证闭环
    if not bundle_name:
        warnings.append(
            "未提供 --bundle-name，start_app/verify_ui 需要 bundleName 参数"
        )
    if not test_plan:
        warnings.append(
            "未提供 --test-plan，verify_ui 需要自然语言测试用例"
        )

    steps = [
        {
            "tool": "build_project",
            "args": {},
            "purpose": "编译工程",
        },
        {
            "tool": "start_app",
            "args": {"bundleName": bundle_name or "<REQUIRED>"},
            "purpose": "启动应用到模拟器/设备",
        },
        {
            "tool": "verify_ui",
            "args": {
                "bundleName": bundle_name or "<REQUIRED>",
                "testPlan": test_plan or "<REQUIRED>",
                "freshStart": fresh_start,
            },
            "purpose": "按自然语言测试用例验证 UI，返回 successPart/failPart/id",
        },
        {
            "tool": "get_ui_verification_log",
            "args": {"id": "<from verify_ui.id>"},
            "purpose": "verify_ui 失败时取验证日志，定位失败原因",
            "condition": "verify_ui.failPart 非空",
        },
        {
            "tool": "save_ui_screenshot",
            "args": {
                "id": "<from verify_ui.id>",
                "dirname": "./screenshots",
            },
            "purpose": "verify_ui 失败时保存截图，供 fix 子命令诊断",
            "condition": "verify_ui.failPart 非空",
        },
    ]
    return {
        "platform": pf,
        "workflow": "simulator-verify",
        "steps": steps,
        "on_failure": (
            "据 verify_ui.failPart 定位问题，调 get_ui_verification_log 取日志 + "
            "save_ui_screenshot 存截图，调 fix 子命令修复后重跑闭环"
        ),
        "warnings": warnings,
    }


def cmd_run(
    ets_files: Optional[list[str]] = None,
    bundle_name: Optional[str] = None,
    test_plan: Optional[str] = None,
    fresh_start: bool = False,
) -> int:
    """输出建议 MCP 工具序列 JSON（不直接调 MCP）。"""
    plan = build_run_plan(
        ets_files=ets_files,
        bundle_name=bundle_name,
        test_plan=test_plan,
        fresh_start=fresh_start,
    )
    print(json.dumps(plan, indent=2, ensure_ascii=False))
    return 0


# ---------------------------------------------------------------------------
# argparse 入口
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python3 -m scripts.test.cli",
        description=(
            "hap-dev test 子命令：MCP 平台检测与测试工具序列生成。"
            "支持 check/config/run 三动作。"
        ),
    )
    sub = parser.add_subparsers(dest="action")

    sub.add_parser(
        "check", help="检测平台/可用工具/MCP 安装状态"
    )

    p_config = sub.add_parser("config", help="生成 MCP 配置 JSON")
    p_config.add_argument(
        "--deveco-path", required=True, help="DevEco Studio 安装根目录"
    )
    p_config.add_argument(
        "--project-path", required=True, help="鸿蒙工程根路径"
    )
    p_config.add_argument(
        "--additional-groups",
        default=None,
        help="额外工具组（逗号分隔，如 ui_integration_test,emulator_manager）",
    )

    p_run = sub.add_parser("run", help="输出建议调用的 MCP 工具序列 JSON")
    p_run.add_argument(
        "--ets-files",
        nargs="*",
        default=None,
        help=".ets 文件列表（Linux 静态检查用）",
    )
    p_run.add_argument(
        "--bundle-name",
        default=None,
        help="应用 bundleName（Win/macOS 模拟器验证用）",
    )
    p_run.add_argument(
        "--test-plan",
        default=None,
        help="自然语言测试用例（Win/macOS verify_ui 用）",
    )
    p_run.add_argument(
        "--fresh-start",
        action="store_true",
        help="冷启动应用（verify_ui 的 freshStart 参数）",
    )

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """argparse 入口，返回退出码。"""
    parser = _build_parser()

    # 捕获 argparse 的 SystemExit（如未知 action / 缺必需参数 / --help）
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return int(e.code) if isinstance(e.code, int) else 2

    if not args.action:
        parser.print_help(sys.stderr)
        return 2

    if args.action == "check":
        return cmd_check()
    if args.action == "config":
        return cmd_config(
            args.deveco_path,
            args.project_path,
            additional_groups=args.additional_groups,
        )
    if args.action == "run":
        return cmd_run(
            ets_files=args.ets_files,
            bundle_name=args.bundle_name,
            test_plan=args.test_plan,
            fresh_start=args.fresh_start,
        )

    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
