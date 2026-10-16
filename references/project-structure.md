# 工程目录结构（Stage/FA 模型）

DevEco Studio 工程目录结构速查。创建/修复/构建时定位文件用。依据官方《工程目录结构介绍》（2026-10 抓取）：<https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-project-structure>

> 🔴 **CHECKPOINT**：目录树截图中存在正文未列出的条目（`.hvigor/`、`.idea/`、C++ 工程的 `.cxx/` 与 `build/`、根级 `local.properties`）——它们是构建/IDE 本地产物，**禁止**当作工程源码修改或提交内容分析对象。

## ArkTS 工程结构（Stage 模型，API 10+）

```text
MyApplication/
├── .hvigor/                      # hvigor 缓存（图有文无，勿动）
├── .idea/                        # IDE 配置（图有文无）
├── AppScope/
│   └── app.json5                 # 应用全局配置（bundleName 在此，fix runtime-fix 读它）
├── entry/                        # 模块，编译生成一个 HAP
│   └── src/
│       ├── main/
│       │   ├── ets/              # ArkTS 源码
│       │   │   ├── entryability/         # 入口 UIAbility
│       │   │   ├── entrybackupability/   # 备份恢复扩展
│       │   │   └── pages/                # 页面（Index.ets）
│       │   ├── resources/                # 资源（见下表）
│       │   └── module.json5              # 模块配置（HAP 配置/设备配置/全局配置）
│       ├── mock/                 # Mock 能力配置
│       ├── ohosTest/             # Instrument Test
│       └── test/                 # Local Test
│   ├── build-profile.json5      # 模块级：buildOption/targets/混淆开关（arkOptions.obfuscation）
│   ├── hvigorfile.ts            # 模块级构建任务脚本
│   ├── obfuscation-rules.txt    # 混淆规则（本模块，见 build.md 混淆节）
│   └── oh-package.json5         # 三方包声明：包名/版本/入口/依赖
├── oh_modules/                   # 三方库依赖（类比 node_modules）
├── build-profile.json5          # 应用级：签名 signingConfigs、products
├── code-linter.json5            # 代码检查规则
├── hvigorfile.ts                # 应用级构建任务脚本
├── local.properties             # 本机路径（SDK 等，图有文无，不入库）
├── oh-package.json5             # 全局依赖配置（overrides/overrideDependencyMap/parameterFile）
└── oh-package-lock.json5        # 应用级依赖锁定
```

## C++ 工程额外目录（Stage 模型，API 10+）

在 ArkTS 工程基础上，entry 增有：

| 路径 | 作用 |
| ---- | ---- |
| `entry/.cxx/`、`entry/build/` | C++/构建缓存（图有文无，勿动） |
| `entry/libs/{abi}/` | .so 存放，**默认打包进产物**（abi 如 arm64-v8a） |
| `src/main/cpp/types/libentry/index.d.ts` | C++ API 接口描述（缺它编译报 Cannot find module，见 build.md 报错速查） |
| `src/main/cpp/types/libentry/oh-package.json5` | .so 声明文件入口与包名 |
| `src/main/cpp/CMakeLists.txt` | CMake 构建脚本（ninja 报错/undefined symbol 排查处） |
| `src/main/cpp/napi_init.cpp` | C++ API 实现 |

## JS 工程结构（FA 模型，仅 JS）

`entry/src/main/js/MainAbility/`：`i18n/`（多语言资源）、`pages/`、`app.js`（承载 Ability 生命周期）；模块配置为 `src/main/config.json`（非 module.json5）。FA 模型为新工程不推荐，仅维护旧工程时参考。

## 资源目录（三模型通用）

| 目录 | 内容 |
| ---- | ---- |
| `base/element/` | 字符串/整型/颜色/样式等 json（string.json、color.json、float.json、integer.json、boolean.json、pattern.json、plural.json、intarray.json、strarray.json） |
| `base/media/` | 多媒体（.png/.gif/.mp3/.mp4 等） |
| `rawfile/` | 任意格式原始文件；**不**按设备状态匹配，须按路径+文件名引用 |

## 关键配置文件职责（改错高发区）

| 文件 | 层级 | 职责 | 报错关联 |
| ---- | ---- | ---- | -------- |
| `AppScope/app.json5` | 应用 | 全局配置、bundleName | bundleName 来源（fix runtime-fix 约束） |
| `src/main/module.json5` | 模块 | HAP 配置/设备配置/abilities | Schema validate failed 高发地 |
| `build-profile.json5` | 应用 | 签名 signingConfigs、products | 签名/构建模式 |
| `build-profile.json5` | 模块 | buildOption/targets/混淆开关 | caseSensitiveCheck、obfuscation |
| `oh-package.json5` | 应用/模块 | 依赖 | devDependencies 误配 → OhmUrl 报错 |
| `hvigor-config.json5`（工程级，`~/.hvigor` 侧） | 构建 | nodeOptions.maxOldSpaceSize、logging.level | OOM/日志级别 |

官方详细说明：[module.json5 配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)、[资源分类与访问](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access)
