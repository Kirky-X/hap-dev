#!/usr/bin/env python3
"""hap-dev .mjs 脚本离线测试的 node 调用辅助（非 test_ 前缀，pytest 不收集）。

统一约定：
- DEVECO_HOME 置空 → hdc/DevEco SDK 探测走"未安装"显性错误路径，保证离线；
- run_mjs_expr 通过 node --input-type=module 动态 import 目标模块并 eval
  表达式，结果以 __RESULT__ 前缀 JSON 输出，供 Python 断言；
- node 不可用时所有测试 skip（不写假测试）。
"""
import json
import os
import shutil
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

NODE = shutil.which("node")

RESULT_PREFIX = "__RESULT__"

_HARNESS_CODE = (
    "import { pathToFileURL } from 'node:url';\n"
    "const mod = await import(pathToFileURL(process.env.MJS_PATH).href);\n"
    "const out = await eval(process.env.MJS_EXPR);\n"
    f"console.log('{RESULT_PREFIX}' + JSON.stringify(out === undefined ? null : out));\n"
)


def offline_env(extra=None):
    """干净离线环境：DEVECO_HOME 置空禁用真实工具链探测。"""
    env = os.environ.copy()
    env["DEVECO_HOME"] = ""
    if extra:
        env.update(extra)
    return env


def _require_node():
    if NODE is None:
        raise RuntimeError("node 不存在：.mjs 测试需 node 运行时（用例侧应先 skip）")


def run_mjs_expr(rel_path, expr, env_extra=None, timeout=30):
    """import scripts/<rel_path> 并求值 expr（引用 `mod`），返回 (returncode, stdout, stderr)。"""
    _require_node()
    full = os.path.join(SCRIPTS_DIR, rel_path)
    env = offline_env(env_extra)
    env["MJS_PATH"] = full
    env["MJS_EXPR"] = expr
    return subprocess.run(
        [NODE, "--input-type=module", "-e", _HARNESS_CODE],
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
    )


def eval_mjs(rel_path, expr, env_extra=None):
    """运行 run_mjs_expr 并解析 __RESULT__ JSON；非零退出或缺失标记时抛 AssertionError。"""
    proc = run_mjs_expr(rel_path, expr, env_extra=env_extra)
    if proc.returncode != 0:
        raise AssertionError(
            f"node harness 失败 ({rel_path}): {proc.stderr.strip()[:500]}"
        )
    for line in reversed(proc.stdout.splitlines()):
        if line.startswith(RESULT_PREFIX):
            return json.loads(line[len(RESULT_PREFIX):])
    raise AssertionError(f"未找到 {RESULT_PREFIX} 输出: {proc.stdout[:500]}")


def run_cli(rel_path, args, env_extra=None, timeout=60):
    """运行 scripts/<rel_path>（node 子进程），返回 CompletedProcess。"""
    _require_node()
    full = os.path.join(SCRIPTS_DIR, rel_path)
    return subprocess.run(
        [NODE, full, *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        env=offline_env(env_extra),
    )


def kv_output(stdout):
    """printKv 输出解析为 dict（key: value 行）。"""
    result = {}
    for line in stdout.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            result[key] = value
    return result
