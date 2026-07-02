# test 子命令 —— 平台检测与测试验证

经 `python3 -m scripts.test.cli` 检测平台、生成 MCP 配置、按平台输出"建议调用的 MCP 工具序列"JSON。**CLI 不直接调 MCP**——MCP server 由 agent 层启动调用，CLI 只生成执行计划。

> 🔴 **CHECKPOINT**：本子命令**不**自动安装 MCP。MCP 由用户手动 `npm i -g @deveco-codegenie/mcp` 安装。agent 检测到未安装时**仅提示**用户安装，不代为执行。

## 三动作总览

| 动作 | 命令 | 用途 |
| ---- | ---- | ---- |
| `check` | `python3 -m scripts.test.cli check` | 检测平台 / 可用工具 / MCP 安装状态；Linux 输出禁用提示 |
| `config` | `python3 -m scripts.test.cli config --deveco-path <path> --project-path <path> [--additional-groups <groups>]` | 生成 MCP 配置 JSON |
| `run` | `python3 -m scripts.test.cli run [--ets-files f1.ets f2.ets] [--bundle-name <name>] [--test-plan <plan>] [--fresh-start]` | 按平台路由输出建议调用的 MCP 工具序列 JSON |

## 平台检测流程

### Step 1：执行 check

```bash
python3 -m scripts.test.cli check
```

输出三行（Linux 多一行禁用提示）：

```
平台: linux | windows | macos
启用工具: <逗号分隔的工具列表>
MCP 安装: 是 | 否
[Linux 额外] <禁用工具提示>
```

### Step 2：根据平台分流

| 平台 | 工作流 | MCP 模拟器工具 |
| ---- | ---- | ---- |
| Linux | 静态检查（`check_ets_files` + `build_project`） | ❌ 显式禁用并提示 |
| Windows | 模拟器全功能闭环 | ✅ 可用 |
| macOS | 模拟器全功能闭环 | ✅ 可用 |

### Step 3：MCP 未安装处理

`MCP 安装: 否` → 提示用户手动执行：

```bash
npm i -g @deveco-codegenie/mcp
```

**禁止** agent 自动代为安装。Linux 平台 MCP 即便未装也无需提示（模拟器工具本就禁用，仅需静态检查）。

## MCP 配置生成

### 环境变量

MCP server 启动依赖以下环境变量：

| 环境变量 | 必填 | 说明 |
| ---- | ---- | ---- |
| `DEVECO_PATH` | 是 | DevEco Studio 安装根目录 |
| `PROJECT_PATH` | 是 | 鸿蒙工程根路径 |
| `ADDITIONAL_TOOL_GROUPS` | 否 | 额外工具组（逗号分隔，如 `ui_integration_test,emulator_manager`） |
| `UI_VERIFY_BASE_URL` | verify_ui 用 | AI 视觉模型 API base URL |
| `UI_VERIFY_API_KEY` | verify_ui 用 | AI 视觉模型 API key |
| `UI_VERIFY_MODEL_NAME` | verify_ui 用 | AI 视觉模型名（如 `Qwen3-VL`） |

### 生成配置

```bash
python3 -m scripts.test.cli config \
  --deveco-path "/path/to/DevEco-Studio" \
  --project-path "/path/to/project" \
  [--additional-groups "ui_integration_test,emulator_manager"]
```

输出 MCP 配置 JSON（含 `DEVECO_PATH` / `PROJECT_PATH` / `ADDITIONAL_TOOL_GROUPS` 字段），用户/agent 据此启动 MCP server。

> 🔴 **CHECKPOINT**：`verify_ui` 工具依赖 AI 视觉模型。Windows/macOS 工作流用到 `verify_ui` 时，**必须** 提前配置 `UI_VERIFY_BASE_URL` / `UI_VERIFY_API_KEY` / `UI_VERIFY_MODEL_NAME`，否则 `verify_ui` 调用会失败。模型示例：`Qwen3-VL`。

## Linux 静态检查工作流

```bash
python3 -m scripts.test.cli run --ets-files file1.ets file2.ets [...]
```

未提供 `--ets-files` → `check_ets_files` 将扫描工程内所有 `.ets` 文件（CLI 在 `warnings` 中提示）。

执行计划 JSON：

```json
{
  "platform": "linux",
  "workflow": "static-check",
  "steps": [
    {"tool": "check_ets_files", "args": {"files": [...]}, "purpose": "ArkTS LSP 诊断（语法/类型错误）"},
    {"tool": "build_project", "args": {}, "purpose": "编译工程"}
  ],
  "on_failure": "check_ets_files 返回错误时停止流程，调 fix 子命令修复后重跑；build_project 失败时调 fix 子命令修复编译错误",
  "disabled_hint": "<模拟器工具禁用提示>",
  "warnings": [...]
}
```

### 执行规则

1. **先 `check_ets_files`**：对传入的 `.ets` / `.ts` 文件做 ArkTS LSP 诊断（语法 / 类型错误）。
2. **`check_ets_files` 报错 → 停止流程**，不继续 `build_project`。提示用户调 `fix` 子命令的 **error-fixes 轨道** 修复后重跑。
3. **`check_ets_files` 通过 → 跑 `build_project`**：编译工程。
4. **`build_project` 失败 → 调 `fix` 子命令** 修复编译错误，修后重跑闭环。
5. **`build_project` 成功 → Linux 工作流结束**（无模拟器验证）。

## Windows/macOS 模拟器验证闭环

```bash
python3 -m scripts.test.cli run \
  --bundle-name "com.example.foo" \
  --test-plan "首屏显示登录按钮；点击后跳到首页；首页有 3 个 tab" \
  [--fresh-start]
```

未提供 `--bundle-name` / `--test-plan` → CLI 在 `warnings` 中提示（`start_app` / `verify_ui` 需要这些参数）。

执行计划 JSON：

```json
{
  "platform": "windows | macos",
  "workflow": "simulator-verify",
  "steps": [
    {"tool": "build_project", "args": {}, "purpose": "编译工程"},
    {"tool": "start_app", "args": {"bundleName": "..."}, "purpose": "启动应用到模拟器/设备"},
    {"tool": "verify_ui", "args": {"bundleName": "...", "testPlan": "...", "freshStart": false},
     "purpose": "按自然语言测试用例验证 UI，返回 successPart/failPart/id"},
    {"tool": "get_ui_verification_log", "args": {"id": "<from verify_ui.id>"},
     "purpose": "verify_ui 失败时取验证日志，定位失败原因", "condition": "verify_ui.failPart 非空"},
    {"tool": "save_ui_screenshot", "args": {"id": "<from verify_ui.id>", "dirname": "./screenshots"},
     "purpose": "verify_ui 失败时保存截图，供 fix 子命令诊断", "condition": "verify_ui.failPart 非空"}
  ],
  "on_failure": "据 verify_ui.failPart 定位问题，调 get_ui_verification_log 取日志 + save_ui_screenshot 存截图，调 fix 子命令修复后重跑闭环",
  "warnings": [...]
}
```

### 闭环执行规则

1. **`build_project`**：编译工程。失败 → 调 `fix` error-fixes 轨道修复编译错误后重跑。
2. **`start_app`**：用 `bundleName` 启动应用到模拟器 / 设备。失败 → 检查 `bundleName`（从 `AppScope/app.json5` 读，与 fix runtime-fix 轨道同源）。
3. **`verify_ui`**：用自然语言 `testPlan` 验证 UI，返回 `successPart` / `failPart` / `id`。
   - `testPlan` 是自然语言描述的测试用例（例："首屏显示登录按钮；点击后跳到首页；首页有 3 个 tab"）。
   - `freshStart=true` 表示冷启动应用。
   - **依赖 AI 视觉模型**（`UI_VERIFY_BASE_URL` / `UI_VERIFY_API_KEY` / `UI_VERIFY_MODEL_NAME`，如 `Qwen3-VL`），缺一即失败。
4. **`verify_ui.failPart` 非空**（失败时）：
   - `get_ui_verification_log`（`id` 取自 `verify_ui.id`）→ 取验证日志定位失败原因。
   - `save_ui_screenshot`（`id` + `dirname`，默认 `./screenshots`）→ 保存截图供 `fix` 子命令诊断。
5. **调 `fix` 子命令**：根据日志 + 截图诊断（runtime-fix 轨道处理崩溃；error-fixes 轨道处理编译问题）。
6. **修复后重跑闭环**：从 `build_project` 重新开始，直至 `verify_ui.failPart` 为空。

## hilog 采集与 fix 协同

模拟器验证崩溃时，需采 hilog 喂给 `fix` runtime-fix 轨道。hilog 过滤参数：

| 参数 | 说明 |
| ---- | ---- |
| `iscrashLog` | 是否仅采崩溃日志 |
| `level` | 日志级别过滤 |
| `tag` | 标签过滤 |
| `domain` | 域过滤 |
| `bundleName` | 应用包名过滤（与 `AppScope/app.json5` 同源） |
| `keyword` | 关键词过滤 |

采集到的 hilog → 调 `fix` runtime-fix Case C 流程，喂给 `parse-jscrash-log.mjs --source hilog`。

## 边界情形

| 情形 | 处理 |
| ---- | ---- |
| MCP 未安装（Win/macOS） | 提示用户手动 `npm i -g @deveco-codegenie/mcp`，agent 不代装 |
| Linux 试图用模拟器工具 | CLI 显式返回 `disabled_hint`；agent 不调用 |
| `--ets-files` 缺失 | `check_ets_files` 扫全工程；CLI `warnings` 提示 |
| `--bundle-name` 缺失 | `start_app` / `verify_ui` 缺参数；CLI `warnings` 提示；从 `AppScope/app.json5` 读出后补回 |
| `--test-plan` 缺失 | `verify_ui` 缺测试用例；CLI `warnings` 提示；经 `AskUserQuestion` 让用户给出自然语言用例 |
| `verify_ui` 视觉模型环境变量缺失 | 提示用户配 `UI_VERIFY_BASE_URL` / `UI_VERIFY_API_KEY` / `UI_VERIFY_MODEL_NAME`，不强行调用 |
| `check_ets_files` 报错 | 停止流程，不继续 `build_project`；调 `fix` error-fixes 轨道 |
| `build_project` 失败 | 调 `fix` error-fixes 轨道修复后重跑 |
| `verify_ui.failPart` 非空 | 取 `get_ui_verification_log` + `save_ui_screenshot`，调 `fix` 诊断后重跑闭环 |
| 模拟器崩溃 | 采 hilog（按上表过滤）→ 喂给 `fix` runtime-fix Case C |
| 多设备连接 | 经 `AskUserQuestion` 让用户选；与 fix runtime-fix 设备选择规则一致 |

## 交付核对清单

### 通用
- [ ] `check` 已执行，平台 / 工具 / MCP 状态已知
- [ ] MCP 未装时已提示用户手动安装（Linux 除外）
- [ ] 模拟器工作流已配置 `UI_VERIFY_*` 环境变量

### Linux 静态检查
- [ ] `check_ets_files` 通过；未通过则已转 `fix` 修复并停止 build
- [ ] `build_project` 通过；未通过则已转 `fix` 修复

### Windows/macOS 模拟器验证
- [ ] `bundleName` 从 `AppScope/app.json5` 读取，未猜测
- [ ] `testPlan` 为用户确认的自然语言用例
- [ ] `build_project` 通过
- [ ] `start_app` 启动成功
- [ ] `verify_ui` 执行；`failPart` 非空时已取 `get_ui_verification_log` + `save_ui_screenshot`
- [ ] 失败时已调 `fix` 子命令诊断，修复后重跑闭环
- [ ] 崩溃时已采 hilog（按过滤参数）并喂给 `fix` runtime-fix

### 配置生成
- [ ] `config --deveco-path ... --project-path ...` 已生成 MCP 配置 JSON
- [ ] 用户已确认配置；MCP server 已启动
