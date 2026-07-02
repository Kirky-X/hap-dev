# create 子命令 —— 创建 ArkTS 工程

经 skill 私有 Node 脚本 `scripts/create/copy-template.mjs` 创建 ArkTS 工程：模板递归复制 + 占位符替换 + DevEco SDK 自动探测 + bundleName 派生 + `main_pages.json` / `EntryAbility.ets` 同步。

> 模板源位于 `references/project-template/application/`，脚本读取此目录作为脚手架基础。所有模板文件、二进制资源、占位符替换、SDK 探测均由脚本统一完成，agent 不手动逐文件复制。

> 🔴 **CHECKPOINT**：脚本依赖 `node`。若环境无 `node`，立即停止并向用户说明无法执行；不要退化为"模型逐文件复制"模式。

## 必填参数

执行前必须确认下表参数。缺值时经 `AskUserQuestion` 向用户询问，禁止 agent 凭空捏造：

| 参数 | 必填 | 默认 | 示例 |
| ---- | ---- | ---- | ---- |
| `projectPath` | 是 | — | `/Users/yellow/Desktop/projects` |
| `appName` | 是 | — | `HelloWorld` |
| `bundleName` | 自动派生，无需询问 | `com.example.{appName lowercase}` | `com.example.helloworld` |
| `apiLevel` | 否 | 脚本从 DevEco SDK metadata 自动探测，fallback `22` | `21` |

### appName 规则

`appName` 必须匹配 `^[A-Za-z][A-Za-z0-9_]{0,127}$`。**中文 / 非 ASCII 名一律拒绝**——脚本退出码 `4`，错误码 `APP_NAME_INVALID`。

当用户提供中文或非 ASCII 名时，agent **MUST**：

1. 按含义给出 2-3 个 UpperCamelCase ASCII 候选（例：`购物车` → `ShoppingCart` / `ShopCart` / `Cart`；`天气预报` → `WeatherForecast` / `Weather` / `Forecast`）。仅当含义不明时退化为拼音。
2. 经 `AskUserQuestion` 让用户选择，**禁止 agent 代为决定**（即使某个候选看起来明显更好）。
3. 永不将原始非 ASCII 名传给脚本。

### 目录冲突

若 `{projectPath}/{appName}` 已存在且非空，脚本退出码 `2` 并输出 `PROJECT_EXISTS` JSON。看到此错误时，经 `AskUserQuestion` 询问用户是否覆盖、改名或取消——**禁止 agent 自行删除目录或静默重跑**。

### apiLevel 探测优先级

用户显式指定 SDK/API level 时直接透传。用户未指定时，**禁止 agent 凭模型猜版本**，让脚本按以下固定优先级探测：

1. `DEVECO_HOME/sdk/default/sdk-pkg.json` → `data` → `apiVersion`
2. fallback `22`

脚本 stdout JSON 中的 `apiLevel` / `source` / `detectedFrom` 字段为权威值，agent **不得** 再读 `{DEVECO_HOME}/sdk/**` 下的文件来"验证"它。

### 复杂应用需求清单（可选）

仅当用户在创建工程的同时提出复杂业务需求（页面/导航/特性点）且当前会话没有已批准的 Plan Mode 计划时，**才**简要列一份需求清单：

- 要实现的页面
- 首屏 / 入口页
- 页面间导航关系
- 每页关键特性点
- 页面与导航的验证点

清单保持简洁，自动继续执行；仅当缺必填工程参数或需求自相矛盾时才停下来问。**禁止** 把本子命令扩展成 ArkUI 设计指南——UI 实现前请先加载 `references/arkui/`。

## 执行流程（5 步）

### Step 1：运行私有脚本

```bash
node "{SKILL_DIR}/scripts/create/copy-template.mjs" \
  --project-path "{projectPath}" \
  --app-name "{appName}" \
  --bundle-name "{bundleName}" \
  --api-level "{apiLevel}"
```

用户未显式指定 `apiLevel` 时**省略 `--api-level`**，让脚本从 DevEco metadata 探测。

执行约束：

- 不手动逐文件复制模板。
- 递归复制、二进制资源复制、占位符替换、基础校验全部由脚本完成。
- SDK 探测归脚本；不在 prompt 中靠猜测决定 SDK 版本。
- 脚本非零退出码 → 向用户报告错误并停止，不继续后续步骤。

### Step 2：验证结果

至少验证下列文件存在：

- `{projectPath}/{appName}/build-profile.json5`

文件缺失 → 视为创建失败，**不**进入后续编译或页面生成步骤。

脚本输出 `source: "fallback"` → 本地 SDK metadata 不完整。交付工程路径时同时警告用户（例："Find no sdk-pkg.json, can not probe sdk version"）。

### Step 3：切换会话工程上下文（必做）

创建成功后调用 `switch_cwd`，目标路径为生成的工程根 `{projectPath}/{appName}`。

理由：

- `build_project` 与 `start_app` 只有在当前会话上下文目录为真实工程根时才正确工作。
- 本子命令在当前路径下生成完整工程；不切换上下文则后续 build/run 可能失败或落到错误目录。

`switch_cwd` 失败 → 报告上下文切换失败并停止，**不**进入特性实现 / `build_project` / `start_app`。

### Step 4：在生成工程内继续特性工作

仅当用户在创建请求之外还提了应用行为 / UI / 页面 / 业务需求时执行，且必须 `switch_cwd` 成功之后。

实现前：

- 读 `entry/src/main/resources/base/profile/main_pages.json` 确认启动页列表。
- 读启动页文件，通常是 `entry/src/main/ets/pages/Index.ets` 与 `entry/src/main/ets/entryability/EntryAbility.ets`。
- 修改实际启动页或其导航路径，确保所求特性从首屏可达。

> 🔴 **CRITICAL：`EntryAbility.ets` 与 `main_pages.json` 必须保持同步。**
>
> `EntryAbility.ets` 调用 `windowStage.loadContent('pages/SomePage', ...)` 加载首屏。该 page 路径**必须**出现在 `main_pages.json` 的 `src` 数组中——否则框架静默加载失败，导致**白屏**。
>
> 创建自定义 page 并更新 `main_pages.json` 时，**必须**同步更新 `EntryAbility.ets`：
> - 若**重命名或替换** `main_pages.json` 第一项，同步更新 `loadContent()` 指向新首屏。
> - 若在 `main_pages.json` 数组**前部插入**新 splash / landing page，同步更新 `loadContent()` 指向该页。
>
> 编辑后必须重新读这两个文件确认一致。

- 不要只创建一个新命名 page/component 就算完成，除非启动页能路由到它。

> 🔴 **CRITICAL：桌面应用名 —— `app_name` 与 `EntryAbility_label` 必须同时更新。**
>
> 桌面图标标签由 `EntryAbility_label` 控制，不是 `app_name`：
> - `AppScope/resources/base/element/string.json` → `app_name` —— 应用级标签（设置等处使用）。
> - `entry/src/main/resources/base/element/string.json` → `EntryAbility_label` —— Ability 级标签（**桌面图标显示的就是这个**）。

特性实现完毕后运行 `build_project`；成功后再 `start_app`。

### Step 5：向用户回报

所有请求的创建 / 实现 / 编译 / 运行 / 验证工作完成，或遇到阻塞失败立即回报。

回报内容：

- 工程绝对路径
- appName / bundleName / API Level
- 选中 API level 的 `source`：`user_input` / `sdk_pkg` / `fallback`
- 模板完整性校验是否通过
- `switch_cwd` 是否成功
- 有特性工作时，build / run / 验证状态

## 边界情形

| 情形 | 处理 |
| ---- | ---- |
| 环境 `node` 不可用 | 立即停止并告知用户；不退化为模型逐文件复制 |
| `appName` 含非 ASCII | 经 `AskUserQuestion` 提 2-3 ASCII 候选，用户选后再调脚本 |
| 目标目录已存在非空 | 脚本 exit 2 `PROJECT_EXISTS`；经 `AskUserQuestion` 询问覆盖 / 改名 / 取消 |
| `build-profile.json5` 缺失 | 视为创建失败，停止后续步骤 |
| `source: "fallback"` | 交付路径同时警告 SDK metadata 不完整 |
| `switch_cwd` 失败 | 停止，不进入特性实现 / build / run |
| `main_pages.json` 与 `EntryAbility.ets` 不同步 | 框架静默加载失败导致白屏；编辑后必须双向重读确认 |
| 桌面图标名错 | 只改 `app_name` 不够；必须同步改 `EntryAbility_label` |
| 用户已批准 Plan | 不要新建 plan、不要 `plan_enter` / `plan_write`、不要再次请求批准；以现有 plan 为准 |

## 交付核对清单

- [ ] 必填参数齐全；`appName` 通过正则；非 ASCII 名已经用户从候选中选定
- [ ] 脚本以正确参数运行，退出码 0
- [ ] `{projectPath}/{appName}/build-profile.json5` 存在
- [ ] `switch_cwd` 成功切到工程根
- [ ] （有特性工作时）`main_pages.json` 与 `EntryAbility.ets` 双向同步
- [ ] （有特性工作时）桌面图标 `EntryAbility_label` 与 `app_name` 同步
- [ ] （有特性工作时）`build_project` 通过；`start_app` 启动成功
- [ ] 回报包含路径 / appName / bundleName / API Level / `source` / 完整性 / `switch_cwd` 状态 / build+run 状态
