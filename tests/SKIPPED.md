# hap-dev 冒烟测试跳过说明

本目录测试全部离线可跑（`python3 -m pytest tests -q`，无网络、不装依赖、
无真机）。`scripts/` 下 Python 模块（kb/search/test）的测试位于
`scripts/*/tests/`，不在本目录口径内；本目录聚焦尚未覆盖的 `.mjs` 脚本。
以下场景依赖真实 HarmonyOS 工具链，按"不写假测试"原则未编写，仅说明原因。

## 跳过项

| 脚本 | 跳过场景 | 原因 | 已覆盖的替代路径 |
| --- | --- | --- | --- |
| `scripts/fix/collect-hilog.mjs` | 真实 `hdc shell hilog -x` 日志采集 | 需 DevEco Studio toolchain（DEVECO_HOME）+ 真机/模拟器 | DEVECO_HOME 缺失的显性失败路径（collect_failed, exit 1, 提示 DEVECO_HOME）真实测试 |
| `scripts/fix/fetch-faultlog.mjs` | 真实 `hdc file recv` faultlog 拉取 | 同上 | 参数校验（缺 --faultlog-name/--output-dir）与名称规范化（自动补 .log）+ hdc 失败显性化路径真实测试 |
| `scripts/fix/probe-faultlogger.mjs` | 真实 hidumper/ls faultlogger 探测 | 同上 | bundle 参数回显、非法 --max-age-minutes 不崩溃、hdc 失败显性化路径真实测试 |
| `scripts/fix/jscrash-report.mjs` | 无输入时实时采集设备 hilog | 需真机 + hdc | `--log-text`/`--log-file` 离线解析路径、--lines 越界、无输入时 DEVECO_HOME 错误路径真实测试 |
| `scripts/create/detect-sdk.mjs` | 真实 DevEco Studio SDK 探测 | 需真实 DEVECO_HOME 安装结构 | 用临时目录伪造 `tools/node/bin/node` + `sdk/default/sdk-pkg.json` 覆盖 sdk_pkg 命中、apiVersion 非字符串/越界回退、无 DEVECO_HOME 回退 22 |
| `scripts/create/copy-template.mjs` | 真实 hvigor 构建验证生成工程 | 需 DevEco/hvigor 工具链 | 临时模板覆盖复制/替换/verifyFiles 全流程与结构化错误码（exit 1/2/3/4）；仓内真实模板只读冒烟（输出写临时目录） |
| `scripts/fix/shared/hdc.mjs` | `runHdc` 真实 spawn hdc 命令 | hdc 二进制不存在于本环境 | `resolveHdcBinary` 的 DEVECO_HOME 缺失/二进制缺失错误分支经上层脚本真实触发；`targetArgs`/`runHdc` 为薄封装，由 CLI 端到端路径间接覆盖 |

## 覆盖说明

- `fix/shared/jscrash-parse.mjs`、`fix/shared/jscrash-faultlogger.mjs`、
  `fix/shared/utils.mjs` 为纯函数模块，全部导出函数均有真实行为测试
  （通过 node 子进程动态 import，无网络、无设备）。
- `node --check` 语法冒烟覆盖 `scripts/` 下全部 11 个 `.mjs` 文件。

## 运行方式

```bash
cd hap-dev && python3 -m pytest tests -q
```

依赖：Python 3 标准库 + pytest + node 运行时（node 缺失时相关用例自动 skip，
不会伪绿）。
