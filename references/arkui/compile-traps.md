# ArkUI 编译陷阱与错误码锚点（compile-traps）

按**编译错误码/陷阱类别**直查的速查页，与 error-fixes（按症状 31 类）互补。吸收自 DevEco Studio 第一方 skill `hmos-arkui-develop-skill`（quick-rules/quick-apis，2026-10-16 对标），已按 hap-dev 体系重组。

> 来源：DevEco Studio 内置 skill `hmos-arkui-develop-skill`（本地安装路径因平台而异；其 quick-rules/quick-apis 实测经验库，2026-10-16 对标收编，本文为高发项摘录，完整规则库见该 skill）。官方错误码文档补充：[hvigor 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode)（构建期）、[调试错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-errorcode)。

## 错误码速查表

| 错误码/规则名 | 含义 | 一线修复 |
| ---- | ---- | ---- |
| `10505001` | 成员属性名与组件链式方法/通用属性重名；属性不存在；wrapBuilder 泛型漏 `[]`；Repeat 链上 `.cachedCount()` | 改业务前缀命名（见下）；cachedCount 移到滚动容器 |
| `10605038` | 无类型对象字面量（arkts-no-untyped-obj-literals） | 给字面量显式类型上下文 |
| `10605040` | 内联对象字面量作类型（arkts-no-obj-literals-as-types）；@Builder 形参用内联类型 | 声明命名 interface/class |
| `10905202` | `Button('label')` 与 children 同时传入 | 二选一：`Button('OK')` 或 `Button() { Text('x') }` |
| `140109` | @Builder 内修改入参（API 23+） | 入参只读；需要回传用回调 |
| `130000` | addMonitor 目标非 @ObservedV2 class / @ComponentV2 实例 | 检查装饰器版本匹配 |
| `130002` | addMonitor 回调必须为命名函数 | 改命名函数 |
| `100003` | Router 页面栈超 32 页 | Navigation 化或减栈 |
| `100005`/`100006` | Navigation 跳转未注册 builder / 目标非 NavDestination | 注册 navDestination builder |
| `100021`/`106203` | 声明式 FrameNode 不允许修改 / 未挂载节点操作 | 用 NodeContainer/AttributeUpdater 正规通道 |
| `arkts-no-decl-merging` | 跨文件顶层 interface/class 重名（同 hap 共享全局作用域，碰撞发生在文件之间） | 业务前缀命名（CartItem vs OrderItem） |

## 命名禁区

**@State/@Prop/@Local 等成员名禁止与通用属性/链式方法重名**（→ `10505001`）。禁区清单（非穷举，所有通用属性名 + CustomComponent 基类属性均禁）：`id`、`width`、`height`、`margin`、`padding`、`offset`、`position`、`border`、`borderRadius`、`backgroundColor`、`brightness`、`direction`、`value`、`scale`、`rotate`、`opacity`、`visibility`、`zIndex`、`size`、`layoutWeight`、`aspectRatio`、`flexBasis`、`flexGrow`、`flexShrink`、`alignSelf`、`justifyContent`、`alignItems`、`alignContent`、`borderWidth`、`borderColor`、`borderStyle`、`borderImage`、`foregroundColor`、`colorFilter`、`clip`、`gradient`、`blur`、`shadow`、`transform`、`markAnchor`、`translate`、`clickEffect`、`hoverEffect`、`draggable`、`enabled`、`tabIndex`。

写法：业务前缀消歧义——`currentValue` 而非 `value`，`moveDirection` 而非 `direction`。

**框架保留字**（方法/变量重名 → 运行时异常）：`rerender`、`initialRender`、`aboutToBeDeleted`、`observeComponentCreation(2)`、`updateStateVars`、`updateDirtyElements`、`createStorageLink/Prop`、`createLocalStorageLink/Prop`、`declareWatch`、`addProvidedVar`、`initializeConsume`、`reconnectToConsume`、`getRecycleManager`、`aboutToReuseInternal`、`aboutToRecycleInternal`、`recycleSelf` 等（框架内部生成方法全禁，完整全表见来源 skill 的 quick-rules 03-component 保留字节）。

## 构造参数字段名陷阱（实测高发，禁止凭记忆编造）

| 组件 | ❌ 臆造 | ✅ 正确 |
| ---- | ---- | ---- |
| TimePicker | `TimePicker({ useMilitaryTime: true })`（该字段属 TimePickerDialog） | `TimePicker()` 后用链式/selected 属性 |
| Tabs | `Tabs(this.tabsController)` | `Tabs({ controller: this.tabsController })` |
| MenuItem | `MenuItem({ value: '复制', icon: $r(...) })` | `MenuItem({ content: '复制', startIcon: $r(...) })` |
| Shape | `Shape({ viewPort: {...} })`（viewPort 是链式方法） | `Shape().viewPort({x,y,w,h})` |
| PersistentStorage | `persistProp('k','v')` 传 `{key,default}` 对象字段名混乱 | 按 API 签名 `defaultValue` 字段 |
| Badge | 省略 style；count 与 value 同传 | `Badge({ count, style: { badgeSize, badgeColor } })`，count/value 二选一 |
| Select | `Select({ options: [...] })` | 直接传数组 `Select([{ value: 'A' }])` |
| bindPopup | `.bindPopup(this.show)` 单参 | `.bindPopup(this.show, { message: 'text' })` 两参 |
| WaterFlow / RichEditor / Scroll | `WaterFlow(controller)` / `RichEditor()` 无参 / `Scroll(Scroller)` | WaterFlow 空构造；RichEditor 必传 `{controller}`；`Scroll(new Scroller())` |
| Swiper | `.previousMargin(40)` | `.prevMargin(40)` |
| Navigation | `.subtitle('...')` | Navigation 无 subtitle，用 `.title()` |

其他属性规则：无缩写属性（无 `.bgColor()/.radius()/.textSize()`）；枚举禁字符串且大小写精确（`TextAlign.Center` 非 `'center'`、`FlexAlign.Start` 非 `.start`）；margin/padding 无多参简写（用 `{top,right,...}`）；`Row({space:16})` 在构造器传；Stack 居中用 `alignContent` 非 justifyContent；animateTo 的 `curve` 必须枚举。

## V1/V2 状态管理混用矩阵

| 装饰器体系 | 只能用在 | 成员 |
| ---- | ---- | ---- |
| V1 | @Component | @State/@Prop/@Link/@Provide/@Consume/@Watch/@ObjectLink/@Observed |
| V2 | @ComponentV2 | @Local/@Param/@Provider/@Consumer/@Monitor/@Computed/@ObservedV2/@Trace |

硬约束：

- **V1 storage API 不能存 @ObservedV2 实例**：`AppStorage.setOrCreate`/`LocalStorage` 存入 @ObservedV2 对象 → **运行时 crash**。@ObservedV2 对象走 `AppStorageV2`/`PersistenceV2`（仅 @ComponentV2 内）。
- @Link/@ObjectLink 不本地初始化（值从父传入）；@ObjectLink 禁止整体赋值（`this.objLink = new Info()` ❌，只改属性）；@Param 只读（@ComponentV2 内 `this.x = ...` 报 read-only）；@Local 只能内部初始化。
- @State 只代理第一层：嵌套属性变化需 `@Observed` 类 + 子组件 `@ObjectLink`；嵌套数组 push/splice 不刷新（数组引用未变）。
- @Builder 按引用传递：形参 `$$: InterfaceType`（内联类型 → `10605040`）；**多参数不刷新**（合并为单对象参数）；@Builder 内禁改入参（→ `140109`）；@Watch 回调内禁调 @Builder、禁改自身监视变量（无限循环）；`wrapBuilder` 泛型必须 tuple：`WrappedBuilder<[CardData]>` ✅，漏 `[]` → `10505001`。
- 访问限定符：@Link/@ObjectLink 禁 private；所有装饰器禁 protected（struct 无继承，全告警）。

## 渲染控制（ForEach/LazyForEach/Repeat）

- **必须提供 keyGenerator（第三参数）**：key 用业务 ID 不用索引；缺省时 ForEach 默认 `index + '__' + JSON.stringify(item)`——复杂对象序列化吃内存，**bigint/循环引用直接 jscrash**（编译缺陷→运行崩溃，转 fix runtime-fix）。
- ForEach/LazyForEach **不是真实组件**：不能 `.layoutWeight()/.width()` 等链式布局属性，包进容器后再设。
- Repeat(V2)：`virtualScroll` 需设 totalCount；**`.cachedCount()` 放滚动容器上**，放 Repeat 链 → `10505001`；virtualScroll 仅 @ComponentV2 内可用。
- LazyForEach：dataSource 不可重新赋值（用 DataChangeListener 通知）；仅 List/Grid/WaterFlow/Swiper 支持（Scroll 不支持）；同容器禁与 ForEach 混用。

## 容器直接子组件约束

| 容器 | 唯一合法直接子组件 |
| ---- | ---- |
| List | ListItem / ListItemGroup |
| Grid | GridItem |
| Tabs | TabContent |
| WaterFlow | FlowItem |

## 废弃接口替换

| ❌ 废弃 | ✅ 替代 |
| ---- | ---- |
| CustomDialogController | `promptAction.openCustomDialog` |
| pageTransition() | Navigation/Modal 转场 |
| `@ohos.router` 做导航 | Navigation + NavDestination |
| 全局 `animateTo`/`vp2px`（API 18+） | `this.getUIContext().animateTo()` 等 |
| @Component 内 `static {}` | 移除（V1 不执行，API 22 起告警） |
