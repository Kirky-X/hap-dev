"""test 子命令的 CLI 入口：平台检测 / 配置生成 / 执行计划输出。

三个动作（详见 references/commands/test.md）::

    python3 -m scripts.test.cli check
    python3 -m scripts.test.cli config --deveco-path <p> --project-path <p> [--additional-groups <g>]
    python3 -m scripts.test.cli run [--ets-files f1 f2] [--bundle-name <n>] [--test-plan <p>] [--fresh-start]

关键设计：

- **CLI 不直接调 MCP**：run 动作只输出"建议调用的 MCP 工具序列"JSON，由 agent
  层据此启动 MCP server 并执行。``cmd_run`` 不调用 subprocess / check_mcp_installed
  （契约 test_run_does_not_invoke_mcp 断言）。
- **build_run_plan 为纯函数**：run 动作的路由逻辑全部下沉到 ``build_run_plan``，
  便于直接单测（无需 capsys 解析 JSON）。
- **Linux 强制静态检查**：build_run_plan 在 Linux 永远走 static-check workflow，
  忽略 bundle_name / test_plan；并附 ``disabled_hint`` 告知 agent 模拟器工具不可用。
- **未知 / 缺失动作 fail-loud**：main 遇到未知子命令或无子命令返回非零（契约
  test_main_unknown_action_returns_nonzero / test_main_no_action_returns_nonzero）。

输出约定：``cmd_config`` / ``cmd_run`` 仅打印单个合法 JSON 对象（stdout），
便于 agent 用 ``json.loads`` 直接解析。``cmd_check`` 打印人类可读的多行状态。
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

# ---------------------------------------------------------------------------
# check 动作
# ---------------------------------------------------------------------------


def cmd_check() -> int:
    """检测并打印：平台 / 启用工具 / MCP 安装状态；Linux 额外打印禁用提示。

    输出格式（多行）::

        平台: <linux|windows|macos>
        启用工具: <逗号分隔的工具列表>
        MCP 安装: 是 | 否
        [仅 Linux] <disabled_tools_hint>

    Returns:
        0（检测本身永不失败；MCP 未装只是状态，不是错误 —— 用户手动安装）。
    """
    platform = detect_platform()
    tools = enabled_tools(platform)
    installed = check_mcp_installed()

    print(f"平台: {platform}")
    print(f"启用工具: {', '.join(tools)}")
    print(f"MCP 安装: {'是' if installed else '否'}")
    if platform == "linux":
        # Linux 必须额外输出禁用提示（契约 test_check_linux_outputs_platform_tools_hint）
        print(disabled_tools_hint(platform))
    return 0


# ---------------------------------------------------------------------------
# config 动作
# ---------------------------------------------------------------------------


def cmd_config(
    deveco_path: str,
    project_path: str,
    additional_groups: str = "",
) -> int:
    """生成 MCP 配置 JSON 并打印到 stdout。

    ``additional_groups`` 在 Linux 由 ``generate_mcp_config`` 强制清空。

    Args:
        deveco_path: DevEco Studio 安装根目录。
        project_path: 鸿蒙工程根路径。
        additional_groups: 额外工具组（逗号分隔）。

    Returns:
        0。
    """
    cfg = generate_mcp_config(deveco_path, project_path, additional_groups)
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------------------------
# run 动作的核心纯函数：build_run_plan
# ---------------------------------------------------------------------------

# verify_ui 失败时诊断步骤引用的 verify_ui.id（运行时由 agent 从 verify_ui
# 返回值回填，计划阶段用占位符标注数据流）。
_VERIFY_ID_REF = "<from verify_ui.id>"

# Linux 静态检查的 on_failure 说明（与 references/commands/test.md 一致）。
_LINUX_ON_FAILURE = (
    "check_ets_files 返回错误时停止流程，调 fix 子命令修复后重跑；"
    "build_project 失败时调 fix 子命令修复编译错误"
)

# Win/macOS 模拟器闭环的 on_failure 说明。
_SIMULATOR_ON_FAILURE = (
    "据 verify_ui.failPart 定位问题，调 get_ui_verification_log 取日志 + "
    "save_ui_screenshot 存截图，调 fix 子命令修复后重跑闭环"
)


def build_run_plan(
    ets_files: Optional[list[str]] = None,
    bundle_name: Optional[str] = None,
    test_plan: Optional[str] = None,
    fresh_start: bool = False,
) -> dict:
    """按平台构建"建议调用的 MCP 工具序列"执行计划（纯函数）。

    - **Linux**：永远走 ``static-check`` workflow（check_ets_files → build_project），
      忽略 bundle_name / test_plan，附 ``disabled_hint``。
    - **Windows / macOS**：走 ``simulator-verify`` 闭环（build_project →
      start_app → verify_ui，外加 verify_ui 失败时的条件诊断步骤
      get_ui_verification_log / save_ui_screenshot）。

    缺失关键参数时不抛错，只在 ``warnings`` 里提示（agent 据此经 AskUserQuestion
    补全或从工程文件读取）。

    Args:
        ets_files: Linux 静态检查的目标 .ets 文件列表（空则扫描全工程）。
        bundle_name: Win/macOS 启动应用的包名。
        test_plan: Win/macOS verify_ui 的自然语言测试用例。
        fresh_start: 是否冷启动应用。

    Returns:
        执行计划 dict（``platform`` / ``workflow`` / ``steps`` / ``on_failure``
        / ``warnings``，Linux 额外含 ``disabled_hint``）。
    """
    platform = detect_platform()
    warnings: list[str] = []

    if platform == "linux":
        files = list(ets_files) if ets_files else []
        if not files:
            warnings.append(
                "未提供 --ets-files，check_ets_files 将扫描工程内所有 .ets 文件"
            )
        steps = [
            {
                "tool": "check_ets_files",
                "args": {"files": files},
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
            "on_failure": _LINUX_ON_FAILURE,
            "disabled_hint": disabled_tools_hint("linux"),
            "warnings": warnings,
        }

    # Windows / macOS：模拟器验证闭环
    if not bundle_name:
        warnings.append(
            "未提供 --bundle-name，start_app/verify_ui 缺少 bundleName；"
            "请从 AppScope/app.json5 读取后补回"
        )
    if not test_plan:
        warnings.append(
            "未提供 --test-plan，verify_ui 缺少自然语言测试用例；"
            "请经 AskUserQuestion 让用户给出"
        )

    bn = bundle_name or ""
    tp = test_plan or ""
    steps = [
        {
            "tool": "build_project",
            "args": {},
            "purpose": "编译工程",
        },
        {
            "tool": "start_app",
            "args": {"bundleName": bn},
            "purpose": "启动应用到模拟器/设备",
        },
        {
            "tool": "verify_ui",
            "args": {
                "bundleName": bn,
                "testPlan": tp,
                "freshStart": bool(fresh_start),
            },
            "purpose": "按自然语言测试用例验证 UI，返回 successPart/failPart/id",
        },
        {
            "tool": "get_ui_verification_log",
            "args": {"id": _VERIFY_ID_REF},
            "purpose": "verify_ui 失败时取验证日志，定位失败原因",
            "condition": "verify_ui.failPart 非空",
        },
        {
            "tool": "save_ui_screenshot",
            "args": {"id": _VERIFY_ID_REF, "dirname": "./screenshots"},
            "purpose": "verify_ui 失败时保存截图，供 fix 子命令诊断",
            "condition": "verify_ui.failPart 非空",
        },
    ]
    return {
        "platform": platform,
        "workflow": "simulator-verify",
        "steps": steps,
        "on_failure": _SIMULATOR_ON_FAILURE,
        "warnings": warnings,
    }


def cmd_run(
    ets_files: Optional[list[str]] = None,
    bundle_name: Optional[str] = None,
    test_plan: Optional[str] = None,
    fresh_start: bool = False,
) -> int:
    """构建执行计划并打印为 JSON 到 stdout。

    **不得调用 MCP / subprocess**（契约 test_run_does_not_invoke_mcp）——
    仅输出建议序列，由 agent 层据此执行。

    Returns:
        0。
    """
    plan = build_run_plan(
        ets_files=ets_files,
        bundle_name=bundle_name,
        test_plan=test_plan,
        fresh_start=fresh_start,
    )
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------------------------
# argparse 入口
# ---------------------------------------------------------------------------

_PROG = "scripts.test.cli"


def _build_parser() -> argparse.ArgumentParser:
    """构造 argparse parser（每个动作独立 subparser）。"""
    parser = argparse.ArgumentParser(
        prog=_PROG,
        description="HarmonyOS test 子命令：平台检测 / MCP 配置生成 / 测试执行计划输出。",
    )
    sub = parser.add_subparsers(dest="action")

    sub.add_parser("check", help="检测平台 / 可用工具 / MCP 安装状态")

    p_config = sub.add_parser("config", help="生成 MCP 配置 JSON")
    p_config.add_argument(
        "--deveco-path", required=True, help="DevEco Studio 安装根目录"
    )
    p_config.add_argument("--project-path", required=True, help="鸿蒙工程根路径")
    p_config.add_argument(
        "--additional-groups",
        default="",
        help="额外工具组（逗号分隔，Linux 强制为空）",
    )

    p_run = sub.add_parser("run", help="输出建议调用的 MCP 工具序列 JSON")
    p_run.add_argument(
        "--ets-files",
        nargs="*",
        default=None,
        help="Linux 静态检查的 .ets 文件列表（空则扫描全工程）",
    )
    p_run.add_argument("--bundle-name", default=None, help="Win/macOS 应用包名")
    p_run.add_argument("--test-plan", default=None, help="verify_ui 自然语言测试用例")
    p_run.add_argument(
        "--fresh-start",
        action="store_true",
        help="冷启动应用（freshStart=true）",
    )

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """CLI 入口。

    Args:
        argv: 参数列表（默认取 sys.argv[1:]）。

    Returns:
        0 成功；非零表示未知 / 缺失动作或参数错误。
    """
    parser = _build_parser()
    # argparse 在参数错误时 raise SystemExit(2)；这里捕获转成返回码，
    # 让 main 始终返回 int（契约 test_main_unknown_action_returns_nonzero）。
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 2
        return code

    if args.action == "check":
        return cmd_check()
    if args.action == "config":
        return cmd_config(
            args.deveco_path,
            args.project_path,
            args.additional_groups,
        )
    if args.action == "run":
        return cmd_run(
            ets_files=args.ets_files,
            bundle_name=args.bundle_name,
            test_plan=args.test_plan,
            fresh_start=args.fresh_start,
        )

    # 无子命令：打印用法到 stderr，返回非零（契约 test_main_no_action_returns_nonzero）
    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
