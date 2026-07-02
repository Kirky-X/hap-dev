# fix 子命令 —— 错误修复（症状路由 + 三轨道）

按用户症状路由到三条修复轨道之一：编译错误（error-fixes）/ 运行时崩溃（runtime-fix）/ 语法规范（grammar）。**先按症状路由表选轨道，再进入轨道执行**。

> 🔴 **CHECKPOINT**：症状歧义时按 **error-fixes → runtime-fix → grammar** 顺序 fallback。禁止凭模型直觉挑轨道。

## 症状路由表

| 用户症状 | 路由轨道 | 入口 |
| ---- | ---- | ---- |
| 有 build / 编译失败日志或类型错误，**无** jscrash / stack | error-fixes | [`references/error-fixes/`](../error-fixes/) 21 类 + `assets/*.ets` |
| 有 jscrash / stack / faultlog / 白屏 / 闪退，**或** build 成功但运行即崩 | runtime-fix | `scripts/fix/*.mjs`（5 脚本） |
| 纯语法咨询 / TS→ArkTS 差异 / "某语法是否允许" | grammar | [`references/grammar/`](../grammar/) |
| 症状不明 | fallback：error-fixes → runtime-fix → grammar | 见下文"症状歧义处理" |

### 症状歧义处理

按 `error-fixes → runtime-fix → grammar` 顺序尝试：编译 / 类型错误信号（`error:`、`ArkTS:ERROR`、`type 'X' is not assignable`）→ error-fixes；运行时崩溃信号（`jscrash`、`TypeError`、`faultlog`、白屏、闪退、build 成功后崩溃）→ runtime-fix；纯语法咨询 → grammar；仍不明确 → 经 `AskUserQuestion` 让用户提供更明确症状，不强行猜测。

---

## 轨道一：error-fixes（编译 / 类型错误）

适用：编译失败、类型不匹配、build 报错。**无** 运行时崩溃证据。

### Error Categories 快速参考表

下表列出 21 类常见编译错误及一线修复方向，每类对应 `references/error-fixes/<category>.md` 与 `assets/<Name>.ets`。

| 错误类别 | 描述 | 一线修复 |
| ---- | ---- | ---- |
| Notification API Type Errors | `ContentType` 类型不兼容 | 转为 `number` 类型 |
| Window API Type Errors | `window.getLastWindow` 类型推断问题 | 用 callback 模式 |
| AppStorage Type Errors | `AppStorage.get()` 类型推断错 | 用 `@StorageLink` + `LocalStorage` 或 `AppStorage.setAndLink`（避免 `setOrCreate`） |
| Object Spread Type Errors | 对象展开类型推断错 | 显式为对象标注类型 |
| @StorageLink Default Value Errors | `@StorageLink` 属性缺默认值 | 加 `= undefined` 或具体默认值 |
| Object Literal Interface Errors | 对象字面量无显式接口 | 用前先定义 interface |
| Object Literal Type Errors | 对象字面量类型用在返回类型注解 | 定义 interface 作为返回类型 |
| Function Return Type Errors | 返回类型推断受限 | 加显式返回类型注解 |
| Arrow Function Conversion Errors | 用 function 表达式而非箭头函数 | 转 `function` 为箭头函数 `=>` |
| Color Property Errors | 用了不存在的 `Color` 属性 | 用十六进制颜色值替代 |
| Interface Method Signature Errors | 对象字面量方法签名不匹配 | 用属性语法 `method: () => {}` 替代方法语法 |
| AvoidArea Type Errors | `AvoidArea` 缺 `visible` 属性 | 给 AvoidArea 对象加 `visible: false` |
| Standalone Function `this` Errors | 独立函数里用 `this` | 把 context 作为参数传入：`function foo(context: Context)` |
| TitleButtonRect Type Errors | `getTitleButtonRect` 返回类型错；访问不存在的 `left` / `top` | 用 `window.TitleButtonRect` 而非 `window.Rect`；只有 `width` / `height` |
| Catch Clause Type Errors | catch 子句里写类型注解 | 删类型注解或用 `any` / `unknown` |
| ESObject Type Errors | `ESObject` 类型受限 | 用 `ESModule` 或具体类型替代 |
| Resource Conversion Errors | Resource 转 string / number 失败 | 在 UI 组件里直接用 Resource，或用 ResourceManager |
| Unused Variable Warnings | 变量声明未使用 | 用 `console.info` / `hilog` 或删除 |
| IDataSource Type Errors | `LazyForEach` 需 IDataSource 实现 | 为 LazyForEach 实现 IDataSource 接口 |
| Duplicate Entry Errors | 同一文件多个 `@Entry` | 删除多余 `@Entry`，子组件用 `@Component` |
| Possibly Null Errors | 访问属性时对象可能为 null | 用 `!== null` 检查或可选链 |

> 21 类对应 references 文件命名（除 `Window Rect/Size Type Errors` 用 `window_rect_size_errors.md`，其余按下划线小写约定）。完整文档：[`references/error-fixes/`](../error-fixes/)；代码示例：`references/error-fixes/assets/*.ets`。

### 执行流程

1. 收集编译 / 类型错误原文（来自用户或 `test` 子命令的 `build_project` / `check_ets_files` 输出）。
2. 提取错误关键词（类型名、API 名、错误消息），对照上表定位类别。
3. 读对应 `references/error-fixes/<category>.md` 与 `assets/*.ets` 示例。
4. 按"一线修复"方向做最小修改，**不重构无关代码**。
5. 修改后跑 `build_project` 验证；仍报错回到步骤 2 重新定位。

### 边界情形

| 情形 | 处理 |
| ---- | ---- |
| 错误不在 21 类内 | 经 `search` 子命令在线查官方文档；找不到则 fallback 到 grammar 轨道审查语法 |
| 错误同时涉及多个类别 | 逐类修复，先修最先报的错；每次修后重新跑 build |
| 涉及未知 `@ohos.*` / `@kit.*` API | 调 `search` 查 API 约束，**不** 凭模型记忆瞎改 |

---

## 轨道二：runtime-fix（运行时崩溃 / JSCrash）

适用：jscrash / stack / faultlog / 白屏 / 闪退 / build 成功但运行即崩。

> 🔴 **核心约束**：在拿到具体崩溃锚点前，**禁止**对工程做大规模 `Read` / `Glob` / `Explore`。锚点包括 `error_type` / `error_message` / `suspected_file` / `top_stack` 或用户明确指出的崩溃页面 / 模块。

> 🔴 **bundleName 来源**：`bundleName` **必须** 从 `AppScope/app.json5` 读取 `app.bundleName` 字段（如 `com.example.hmos.sample`）。**禁止** 从 `vendor`、模块目录名、`com.example` 前缀猜测。

### 5 个私有 Node 脚本

| 脚本 | 用途 |
| ---- | ---- |
| `scripts/fix/jscrash-report.mjs` | 解析用户直接提供的崩溃原文 |
| `scripts/fix/parse-jscrash-log.mjs` | 解析本地日志文件 / hilog 文件 |
| `scripts/fix/probe-faultlogger.mjs` | 探测设备 faultlogger 最近的崩溃记录 |
| `scripts/fix/fetch-faultlog.mjs` | 拉取指定 faultlog 到本地 |
| `scripts/fix/collect-hilog.mjs` | 设备 hilog 采集 |

所有脚本通过 Shell 执行：

```bash
node "{SKILL_DIR}/scripts/fix/<script>.mjs" ...
```

`{SKILL_DIR}` 替换为本 skill 根目录绝对路径。脚本 stdout 输出稳定 `key: value` 文本；非零退出码 → 当前步骤无法继续，agent **必须** 报告 `next_action` 中的原因并停止，不猜测。

环境无 `node` → 立即停止并说明无法执行。

### Case A：用户已提供原始崩溃文本

```bash
node "{SKILL_DIR}/scripts/fix/jscrash-report.mjs" \
  --log-text "{crashLog}" \
  --bundle-name "{bundleName}" \
  --include-text
```

### Case B：用户提供 `@file` 或本地日志路径

```bash
node "{SKILL_DIR}/scripts/fix/parse-jscrash-log.mjs" \
  --log-file "{logFilePath}" \
  --bundle-name "{bundleName}" \
  --include-text
```

### Case C：用户仅描述症状，无日志

日志采集可选——仅在需要更具体运行时锚点时用。采集设备证据前：

1. **读 `AppScope/app.json5`** 取 `app.bundleName` 精确值作为 `{bundleName}`，禁止猜测。
2. 解析目标设备：
   - 用户提供 `deviceId` → 后续设备命令全部用它。
   - 未提供 → 先 `hdc_log(action="list_devices")`。
   - 仅 1 台设备 → 用之。
   - 多台设备 → 经 `AskUserQuestion` 让用户选，**禁止** 在用户选定前 probe faultlogger / fetch faultlog / collect hilog。
   - 0 台设备 → 报告无法采集设备证据，请求用户提供已连接设备或本地崩溃日志。

用户在选定设备上复现崩溃后，先 probe faultlogger：

```bash
node "{SKILL_DIR}/scripts/fix/probe-faultlogger.mjs" \
  --bundle-name "{bundleName}" \
  --device-id "{deviceId}" \
  --max-age-minutes "30" \
  --limit "10"
```

`status: found` → 拉取并解析最新 faultlog：

```bash
node "{SKILL_DIR}/scripts/fix/fetch-faultlog.mjs" \
  --faultlog-name "{latestFaultlog}" \
  --device-id "{deviceId}" \
  --output-dir "{tempDir}"

node "{SKILL_DIR}/scripts/fix/parse-jscrash-log.mjs" \
  --log-file "{localFaultlogPath}" \
  --bundle-name "{bundleName}" \
  --source file \
  --include-text
```

`status: not_found` → **禁止** 大规模读工程或凭症状瞎猜。请用户在选定设备上再次复现，立即重新 probe。

faultlogger 不可用 / 复现仍无 faultlog / 解析后仍不够 → 回退到 hilog：

```bash
node "{SKILL_DIR}/scripts/fix/collect-hilog.mjs" \
  --device-id "{deviceId}" \
  --lines "4000" \
  --output-dir "{tempDir}"

node "{SKILL_DIR}/scripts/fix/parse-jscrash-log.mjs" \
  --log-file "{hilogPathFromCollect}" \
  --bundle-name "{bundleName}" \
  --source hilog \
  --include-text
```

### 输出契约

`jscrash-report.mjs` 与 `parse-jscrash-log.mjs` 输出的 `key: value` 块包含：

- `status`: `detected` | `no_crash_signature` | `parse_failed`
- `source`: `file` | `text` | `hilog` 等
- `error_type`
- `error_message`
- `suspected_file`
- `top_stack`: `|` 分隔的栈帧
- `keywords`: 逗号分隔
- `next_action`

`--include-text` 在结构化块之后追加人类可读摘要。

`status: no_crash_signature` → 证据太弱，**禁止** 直接进入大规模读代码。请求用户提供更好的日志 / 更清晰的复现 / 额外运行时线索。

### 常见崩溃特征

| 特征 | 典型原因 | 一线修复方向 |
| ---- | ---- | ---- |
| `TypeError` 访问属性 | 渲染 / 生命周期内 state 为 null / undefined | 加 null 守卫、提前初始化、移到更安全生命周期 |
| `ReferenceError` | 作用域错、import 失效、符号缺失 | 修符号归属、import 路径、回调捕获 |
| `RangeError` | 索引非法、递归死循环、过大数据访问 | 加边界检查、断循环、夹紧索引 |
| `BusinessError` / `ParameterError` | 框架 API 前置条件不满足 | 校验参数 / 权限 / 调用时机 |

### 解释规则

- 优先看应用栈帧，过滤框架噪声；第一个具体 `.ets` / `.ts` / `.js` 路径作为起点，**不** 作为最终结论。
- 用户给了复现步骤 → 信任用户步骤胜于纯栈猜；栈指向非入口页 → 假定交互触发，除非证据证明冷启崩溃。
- **不** 大范围重构；先修崩溃路径。

### 约束

- **禁止** 仅凭 prompt 推理就声称修好了崩溃。
- **禁止** 用重试、随机延时、大范围防御性重写替代根因修复。
- 涉及陌生 `@ohos.*` / `@kit.*` API → 先查约束再改。
- 本子命令**不** 决定最终编译 / 运行 / 验证次序，那是 `test` 子命令的事。

### 与其他子命令协同

与 `test`：模拟器验证崩溃的 `get_ui_verification_log` + `save_ui_screenshot` + hilog 喂给本轨道 Case C；与 `search`：陌生 `@ohos.*` API 错误调 `search` 在线查官方文档补充修复依据。

---

## 轨道三：grammar（语法规范 / TS→ArkTS 差异）

适用：纯语法咨询、TS→ArkTS 差异、"某语法是否允许"等问题。**无** 编译错误日志，**无** 运行时崩溃证据。

### 核心检查清单

写 / 改 `.ets` 文件前：

- 把代码当作 ArkTS，**不** 当通用 TypeScript；不用 `any` / `unknown`（除非用户显式允许）、`as` 类型断言、模板字面量、内联对象字面量类型；不把 namespace 当运行时值。
- 不依赖结构化类型；用命名 class / interface / 显式 `implements`；不把 `obj[key]` 动态属性访问作为常规建模模式，优先用已知名称直接访问。
- 给对象字面量显式类型上下文（typed 变量 / 参数 / class / interface 构造）；定义命名 interface / class 替代内联类型；用字符串拼接 + 显式转换替代模板字面量。
- 避免受限 TS 模式：解构声明、解构参数、function 表达式、嵌套局部函数声明、class 表达式、`delete`、`in`、`for...in`、`typeof Foo` 类型查询。

### Reference 顺序

按需读：

1. `references/grammar/topic-aliases.json` —— 主题别名映射
2. `references/grammar/basic-syntax.md` —— ArkTS 常规写法（写代码时用）
3. `references/grammar/restrictions.md` —— 受限语法 / 操作符 / 对象字面量规则 / `Sendable` / 审查意见（禁语法咨询时用）
4. `references/grammar/ts-diff.md` —— TS 移植 / "为何熟悉 TS 模式在 ArkTS 不工作"（移植咨询时用）

### Source 归属

`basic-syntax.md` 与 `ts-diff.md` 是 guide 导向摘要（基于 ArkTS 语言指南章节）；`restrictions.md` 是基于 linter 摘要的实现派生指南，**必须** 明确说明这一点，**禁止** 当作官方规范原文。guide 解释与 linter 限制同时适用 → 两者都提，用一两句说明关系。

### 响应格式

除非用户另要，用：

```markdown
- Topic: <短主题>
- Source: <guide-summary | linter-summary | ts-diff-summary>
- Reference: <reference 文件与章节>
- Why it matches: <一句话>
- Guidance: <一两句话>
```

用户给了代码 → 在 guidance 后追加简短重写建议。

### 工作规则

- 优先直接语法指引，避免大段语言教程；优先命名 ArkTS 替代（class、interface、显式字段类型、箭头函数、直接属性访问）；引用短且可追溯。
- **禁止** 扩展到 build / run / debug / 工具工作流，除非用户在语法答案之后显式要求。

### 边界情形

| 情形 | 处理 |
| ---- | ---- |
| 用户问"某语法是否允许"，但代码中也有 build 报错 | 转到 error-fixes 轨道 |
| 用户问 ArkUI 组件 / 布局 | 不属本轨道，路由到 `kb` 子命令 + `references/arkui/` |
| references 都未覆盖某语法 | 调 `search` 在线查官方 ArkTS 文档，**不** 凭模型记忆下结论 |

---

## 跨轨道协同

| 场景 | 协同 |
| ---- | ---- |
| error-fixes 遇到陌生 `@ohos.*` API 错误 | 调 `search` 子命令在线查官方文档 |
| runtime-fix 涉及未知 API 约束 | 调 `search` 子命令在线查 |
| grammar 不确定某限制是否来自 linter | 看 `restrictions.md` 顶部说明；仍不确定调 `search` |
| test 子命令模拟器崩溃 | test 输出 hilog / faultlog → 喂给 runtime-fix Case C |

## 交付核对清单

### error-fixes 轨道
- [ ] 编译错误原文已收集；错误类别已在 21 类表内定位（或确认表外并调 search）
- [ ] 读过对应 `references/error-fixes/<category>.md` + `assets/*.ets`；修改最小化，不重构无关代码；修改后 `build_project` 通过

### runtime-fix 轨道
- [ ] `bundleName` 从 `AppScope/app.json5` 读取；选定 Case A / B / C 并执行对应脚本；多设备场景下经 `AskUserQuestion` 让用户选 device
- [ ] 拿到 `status: detected` 锚点后才进入定向代码读取；`no_crash_signature` 时不大规模读代码；修复后跑 `test` 模拟器验证或用户手动复现

### grammar 轨道
- [ ] 按 reference 顺序读对应文件；响应格式符合规范（Topic / Source / Reference / Why / Guidance）
- [ ] 区分 guide-summary 与 linter-summary 归属；不扩展到 build / run / debug 流程
