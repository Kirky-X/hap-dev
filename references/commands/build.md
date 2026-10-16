# build —— 命令行构建、签名与发布（hvigorw / hap-sign-tool / 上架）

无 DevEco Studio 图形界面的构建通道：CI 流水线、Linux 服务器、脚本化构建 HAP/HSP/HAR/APP、命令行签名与上架。内容依据华为官方文档（2026-10 抓取）：

- 搭建流水线：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app>
- 发布应用：<https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-publish-app>
- 命令行工具总览：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-tools>

> 🔴 **CHECKPOINT**：发布证书 + 发布 Profile 只能用于打包上架，不能调试运行；只有 Release 包可上架。构建 App 包缺省即 Release（`buildMode` 缺省规则：App=release，HAP/HSP/HAR=debug）。

## 环境准备（CI 流水线）

Command Line Tools（CLT）内嵌 HarmonyOS SDK，无需单独下载。下载：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-get>

系统要求：64 位；Linux 需 GLIBC ≥ 2.28、内存 ≥ 8GB（推荐 16GB）、硬盘 ≥ 100GB。JDK 版本随 CLT：**26.0.0 及以上配 JDK 21，26.0.0 以下配 JDK 17**。

```bash
export COMMANDLINE_TOOL_DIR=/opt                      # CLT 解压根目录，按实际修改
export JAVA_HOME=/opt/jdk-21                          # 26.0.0+ 用 JDK 21；以下用 JDK 17
export PATH=$PATH:$JAVA_HOME/bin
export NODE_HOME=${COMMANDLINE_TOOL_DIR}/command-line-tools/tool/node   # Windows 同路径；Linux/macOS 在 tool/node/bin
export PATH=$PATH:$NODE_HOME/bin
export HDC_HOME=${COMMANDLINE_TOOL_DIR}/command-line-tools/sdk/default/openharmony/toolchains
export PATH=${COMMANDLINE_TOOL_DIR}/command-line-tools/bin:$PATH        # hvigorw / ohpm
export PATH=$PATH:$HDC_HOME

# 验证
java -version && node -v && hvigorw -v && ohpm -v
```

镜像仓库（工程依赖 npm 三方组件时必配）：

```bash
npm config set registry https://repo.huaweicloud.com/repository/npm/
npm config set "@ohos:registry" https://repo.harmonyos.com/npm/
ohpm config set registry https://ohpm.openharmony.cn/ohpm/
```

Linux 构建若用纹理压缩功能，需安装 libGL1（Ubuntu/Debian：`apt install -y libgl1-mesa-dev`；CentOS/RHEL：`mesa-libGL-devel`）。

## 构建步骤

### 1. 安装依赖

进入**工程根目录及每个模块目录**分别执行（不是只装根目录）：

```bash
cd "$PROJECT_PATH" && ohpm install --all
cd "$PROJECT_PATH/entry" && ohpm install --all
# 其余模块同理
```

> ⚠️ 工程路径每一级都不得以 `.` 开头（隐藏目录），否则模块代码/配置会作为资源打进产物，不做混淆加密。

### 2. hvigorw 构建

```bash
cd "$PROJECT_PATH"

hvigorw clean --no-daemon

# HAP：产物 ${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/xxx.hap
hvigorw assembleHap --mode module -p product=default -p buildMode=release --no-daemon

# HSP/HAR：产物 {moduleName}/build/{productName}/outputs/{targetName}/(xxx.har | xxx.hsp)
hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon
hvigorw assembleHar --mode module -p module=library1@default -p product=default --no-daemon

# APP（上架包）：产物 ${PROJECT_PATH}/build/outputs/{productName}/xxx.app
hvigorw assembleApp --mode project -p product=default -p buildMode=release --no-daemon
```

常用扩展参数：

| 参数 | 说明 |
| ---- | ---- |
| `-p buildMode={debug\|release}` | 构建模式。缺省：HAP/HSP/HAR=debug，App=release |
| `-p product={ProductName}` | 指定 product，缺省 default |
| `-p module={ModuleName}@{TargetName}` | 指定模块与 target（多个逗号分隔；target 缺省 default）。须与 `--mode module` 搭配 |
| `-p ohos-test-coverage={true\|false}` | 测试框架覆盖率插桩编译 |
| `--no-daemon` | 流水线必加：禁用守护进程，避免 CI 进程残留 |
| 任务 | `clean` / `assembleHap` / `assembleApp` / `assembleHsp` / `assembleHar` |

CI 专项注意：

- **Linux 大小写敏感**：Windows/macOS 编译通过 ≠ Linux 通过。工程级 `build-profile.json5` 配 `"buildOption": { "strictMode": { "caseSensitiveCheck": true } }` 提前暴露。
- **内存**：非 daemon 模式改 `${COMMANDLINE_TOOL_DIR}/command-line-tools/hvigor/bin/hvigorw` 第 15 行 `NODE_OPTS="--max-old-space-size=10240"`；daemon 模式参考守护进程内存文档。
- **无网络环境**：在有网机器 `npm install` 出 `pnpm@10.28.2` 的 node_modules，拷到无网机 `~/hvigor/wrapper/tools/{版本}/`（26.0.0 以下为 `tools/`），再 `npm config set offline true`；npm/ohpm 依赖同理离线拷贝。

## 构建报错排查

官方入口（2026-10 抓取）：

- 错误码索引：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode>
- 编译构建常见问题：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs>
- 日志记录：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-log>

### 排查流程

1. **拿全量日志**：`hvigorw <task> -d --no-daemon`（日志级别 `-e`/`-w`/`-i`/`-d`，`-d` 输出全部；堆栈跟踪经 hvigor-config.json5 的 `debugging.stacktrace` 开启）。
2. **从日志取错误码 `003xxxxx` 或报错文本**，按码段路由下表；无错误码的报错文本对 FAQ 速查表。
3. **分类处置**：代码级（00305 语法 / 00309 ArkTS 编译，及 ArkTS:ERROR 行）→ `fix` error-fixes 轨道；配置/依赖/签名类按下表与 FAQ 处理。

### hvigor 错误码分段（共 400+ 码，全量按码查官方分类页）

| 码段 | 类别 | 官方页 |
| ---- | ---- | ------ |
| 00301 | 依赖（SDK 缺失/版本低/ohpm 依赖） | [ide-hvigor-errorcode-00301](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00301) |
| 00302 | 脚本（hvigorfile.ts） | [ide-hvigor-errorcode-00302](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00302) |
| 00303 | 配置（build-profile/module.json5/app.json5 字段） | [ide-hvigor-errorcode-00303-1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00303-1) |
| 00304 | 资源缺失 | [ide-hvigor-errorcode-00304](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00304) |
| 00305 | 语法（→ fix error-fixes 轨道） | [ide-hvigor-errorcode-00305](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00305) |
| 00306 | 规格（HAP 包规格校验） | [ide-hvigor-errorcode-00306](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00306) |
| 00307 | 权限 | [ide-hvigor-errorcode-00307](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00307) |
| 00308 | 操作异常 | [ide-hvigor-errorcode-00308](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00308) |
| 00309 | ArkTS 编译（→ fix error-fixes 轨道） | [ide-hvigor-errorcode-00309](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00309) |
| 109 等 | hap-sign-tool 签名工具 | [hapsigntool-errorcode](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hapsigntool-errorcode) |
| 00401-00404 | 调试（运行配置/热重载/调试失败/hdc 命令失败） | [调试错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-errorcode) |

### 高频报错速查（FAQ 提炼）

| 报错 | 一线修复 |
| ---- | ---- |
| `JS heap out of memory`（daemon） | hvigor-config.json5：`"nodeOptions": { "maxOldSpaceSize": 8192 }`（Hvigor 3.1.0+） |
| `JS heap out of memory`（非 daemon） | hvigorw 脚本第 15 行 `NODE_OPTS="--max-old-space-size=…"` |
| Linux `NewSpace::Rebalance Allocation failed` | 非 Node 内存不足：`sysctl -w vm.max_map_count=<新值>`（永久：/etc/sysctl.conf + `sysctl -p`） |
| 编译内存/CPU 占用过高 | hvigor-config.json5 `properties`：`hvigor.pool.cache.capacity: 0`、调低 `hvigor.pool.maxSize` / `ohos.arkCompile.maxSize` |
| `keystore password was incorrect` | p12 密码错：build-profile 里是密文，签名工具要明文；区分 keyAlias 密码与 keystore 密码 |
| `Init keystore failed: parseAlgParameters failed: ObjectIdentifier()` | 高版本 JDK 生成 p12、低版本 JDK 签名不兼容 → 统一 JDK 版本 |
| `generate SignerBlock failed` | 公私钥不配对：keyAlias 私钥与 appCertFile 证书须同一次 CSR 申请配对 |
| `Schema validate failed` | 配置文件字段缺失/拼错（如启动界面字段被删）；按报错 `instancePath`/`missingProperty` 定位补齐 |
| `No available entry module found` | feature 模块 `entryModules` 名称与 entry 模块名不一致；或工程级 modules 中 feature 排在 entry 前 |
| `input module releaseType is different` | 各模块 SDK 版本不一致 → 全部模块用同一 SDK 重打包再打 APP |
| `Duplicated files found in module` | 同名 .so 多处存在 → buildOption 用 `select`/`pickFirsts`/`pickLasts` 选定 |
| `Cannot find module XXX … (.so 引用)` | 缺 native 声明：cpp 目录下建 `types/libxxx/index.d.ts` + oh-package.json5，并加本地依赖 |
| `Failed to get a resolved OhmUrl by filepath` | 运行时依赖误配 `devDependencies` → 移到 `dependencies` |
| `Property xxx does not exist on type 'typeof BuildProfile'` | 各 target `buildProfileFields` key 不一致 → 对齐，或配到工程级 |
| `ninja: error: mkdir(xxx): No such file or directory` | 路径超 CMAKE_OBJECT_PATH_MAX(250) → CMakeLists.txt 调大 |
| C++ `undefined symbol` | 源文件未入 CMake 构建或缺库 → 检查 CMakeLists.txt 的源文件与链接库 |

### 与 fix 子命令的路由边界

- **代码级编译错误**（ArkTS:ERROR、00305/00309 码）→ `fix` error-fixes 轨道（31 类 references）。
- **环境/配置/签名/内存类** → 本节速查表 + 错误码分类页。
- 构建成功但运行崩溃 → `fix` runtime-fix 轨道（jscrash/faultlogger）。

## 代码混淆加固（ArkGuard）

ArkGuard 源码混淆对 ArkTS 的变量名/属性名/文件名/导入导出名做混淆，提升逆向难度。依据官方文档（2026-10 抓取）：

- 开启指南：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-guide>
- 配置选项：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-rule-options>
- 保留选项：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-keep-options>

> 🔴 **CHECKPOINT**：混淆**仅 release 编译生效**，debug 编译不混淆。排查"行为差异是否由混淆引起"时切换混淆开关，不要只切编译模式。

### 开启

模块 `build-profile.json5`：

```json5
"arkOptions": {
  "obfuscation": {
    "ruleOptions": {
      "enable": true,                      // 混淆开关
      "files": ["./obfuscation-rules.txt"] // 本模块混淆规则
    },
    "consumerFiles": ["./consumer-rules.txt"] // 仅 HAR/HSP：被依赖时生效
  }
}
```

版本差异：DevEco Studio **5.0.3.600 起**新建工程默认**关闭**混淆，但 obfuscation-rules.txt 默认含 4 项推荐选项；**5.0.3.600 之前**新建工程默认开启混淆（API 10+ Stage 模型）。开开关只启用默认混淆（局部变量和参数），更多能力靠规则文件。

### 三个配置文件

| 文件 | 生效范围 | 注意 |
| ---- | ---- | ---- |
| `obfuscation-rules.txt` | 编译本模块 | 可自由配置选项与保留项 |
| `consumer-rules.txt` | 编译依赖本 HAR/HSP 的其他模块 | **建议只配保留选项（-keep-\*）**，配 enable 类选项会干扰宿主 |
| `obfuscation.txt` | 编译产物，随 HAR/HSP 发布 | 三方库的 obfuscation.txt 仅在**模块级** oh-package.json5 依赖时生效 |

### 混淆选项

| 选项 | 作用 |
| ---- | ---- |
| `-enable-property-obfuscation` | 属性名混淆（影响面最大，最后适配前先跑通其他项） |
| `-enable-toplevel-obfuscation` | 顶层作用域名称混淆（globalThis 访问会失效，需 `-keep-global-name`） |
| `-enable-export-obfuscation` | 导入导出名混淆 |
| `-enable-filename-obfuscation` | 文件名混淆（动态 import/routerMap/ohmUrl 跳转需 `-keep-file-name`） |
| `-enable-string-property-obfuscation` | 字符串属性名混淆 |
| `-compact` / `-remove-log` / `-remove-comments` | 去空格 / 移除 console.\* / 移除注释 |
| `-apply-namecache <file>` / `-print-namecache` | 复用/导出名称映射（增量混淆） |
| `-keep-property-name` / `-keep-global-name` / `-keep-file-name` | 保留白名单（属性/顶层名/文件名） |

### 适配顺序（官方推荐，逐项验证后再开下一项）

1. `-enable-toplevel-obfuscation`：globalThis 全局变量用 `-keep-global-name` 保留。
2. `-enable-property-obfuscation`：三种场景必须保留——①静态定义/动态访问（或反之）的属性名；②点语法访问非 ArkTS 定义的字段（so 库 API、JSON 字段、数据库字段）；③HAR 发布给他人时，不可二次混淆的属性写进 consumer-rules.txt。
3. `-enable-export-obfuscation`：HSP 对外接口用 `-keep-global-name`、对外 class/interface 属性用 `-keep-property-name`；`import … from 'library.so'` 的接口名保留。
4. `-enable-filename-obfuscation`：动态 import、routerMap 的 pageSourceFile、`@bundle:` ohmUrl 跳转路径用 `-keep-file-name` 保留。

### 产物与报错栈还原

- 混淆后代码：`build/default/[...]/release/<模块名>`；映射表与白名单：`.../release/obfuscation/`（`nameCache.json` 名称映射、`systemApiCache.json` 系统 API 白名单）。
- **发布前必须备份 `sourceMaps.map` + `nameCache.json`**（流水线构建拿不到时用本地编译产物代替）。
- 混淆后 jscrash 堆栈难读：CLT 的 `hstack` 插件自动还原（`ide-command-line-hstack`）。与 `fix` runtime-fix 轨道协同：喂 parse-jscrash-log.mjs 前先 hstack 还原。

### 约束

- 不支持在 hvigor 构建流程中添加自定义混淆插件。
- 开启混淆的模块依赖已混淆的远程 HAR 时会被**二次混淆**——HAR 提供方把不可再混淆的属性写进 consumer-rules.txt。

## 签名

调试与发布签名分开：**调试签名**优先 GUI 自动签名（DevEco Studio 登录账号后 `File > Project Structure > Signing Configs` 勾选自动生成，自动生成调试证书与 Profile；详见[自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-auto)），以下场景**必须手动签名**：跨设备调试、跨应用交互调试、断网调试、多用户共享密钥、kit 需配置指纹。**命令行/CI 无 GUI，自动签名不可用 → 走路径 B 手动签名（调试或发布证书按需申请）**。

### 路径 A：build-profile.json5 配置 signingConfigs（hvigor 构建时自动签）

工程级 `build-profile.json5` 配好 `signingConfigs`（含 .cer/.p7b/.p12 与 material 文件夹——material 默认与 .p12 同路径）后，构建产物直接出 `xxx-signed.hap`（可装真机）与 `xxx-unsigned.hap`。字段与 GUI 对应关系：Store File(.p12)/Store Password/Key Alias/Key Password/Sign Alg（固定 `SHA256withECDSA`）/Profile File(.p7b)/Certpath File(.cer)。

### 路径 B：keytool 生成密钥 + hap-sign-tool 手动签名

```bash
# 1. 生成密钥库 .p12（storepass≥8位、两种以上字符类型；validity 建议 9125=25 年）
keytool -genkeypair -alias "demo_key" -keyalg EC -groupname secp256r1 -sigalg SHA256withECDSA \
  -dname "C=CN,O=HUAWEI,OU=HUAWEI IDE,CN=demo_key" \
  -keystore /path/demo.p12 -storetype pkcs12 -validity 9125 -storepass <密码> -keypass <密码>

# 2. 生成证书请求文件 .csr（alias/keystore 与上一步一致）
keytool -certreq -alias "demo_key" -sigalg SHA256withECDSA \
  -keystore /path/demo.p12 -storetype pkcs12 -file /path/demo.csr

# 3. AGC 用 .csr 申请调试/发布证书 .cer 与 Profile .p7b（GUI 也可用 CertificateTool：
#    https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-publish-app 附 Win x64/Mac x64/Mac ARM64 三平台包与 SHA256 校验码）

# 4. hap-sign-tool 签名（工具在 ${COMMANDLINE_TOOL_DIR}/command-line-tools/sdk/default/openharmony/toolchains/lib）
java -jar hap-sign-tool.jar sign-app -keyAlias "demo_key" -signAlg "SHA256withECDSA" -mode "localSign" \
  -appCertFile /path/demo.cer -profileFile /path/demo.p7b \
  -inFile /path/xxx-unsigned.hap -outFile /path/xxx-signed.hap \
  -keystoreFile /path/demo.p12 -keyPwd <密码> -keystorePwd <密码>
# APP 包签名：inFile/outFile 换成 .app 即可
```

签名工具详参：<https://gitcode.com/openharmony/developtools_hapsigner>

## 发布上架

| 版本 | 流程 |
| ---- | ---- |
| DevEco Studio 26.0.0+ | 构建出 .app（`Build > Build Hap(s)/APP(s) > Build APP(s)` 或 `hvigorw assembleApp`）→ 菜单 `Build > Upload Product` 登录上传。上传时自动重签名（支持 AGC 云管理证书或开发者自建证书），产物生成 `re-signed.app` 后缀包。上传类型三种：AppGallery Connect（云证书重签+上传）/ Testing Only（仅测试）/ Custom（自定义签名管理） |
| 26.0.0 以下 | 手动准备 .p12/.csr → AGC 申请发布证书 .cer + 发布 Profile .p7b → 手动签名（路径 A/B）→ 上传 AGC |

约束：Upload Product 仅支持中国境内（不含港澳台）；仅支持上传工程 `build/outputs` 目录下的包；勿上传敏感信息（密码/源码/私钥/调试包/业务日志）。

## hdc 安装运行

推送的 HAP 必须已签名，否则安装失败：

```bash
hdc file send "$PROJECT_PATH/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
hdc shell aa start -a EntryAbility -b com.example.myapplication -m entry
```

目标为模拟器时，先 `hdc tconn 127.0.0.1:5555` 建立连接（见 [emulator.md](emulator.md)）。

## 失败模式

| 症状 | 一线修复 |
| ---- | ---- |
| `hvigorw: command not found` | `command-line-tools/bin` 未入 PATH；或未 `cd` 到工程根目录（hvigorw 需在工程内执行） |
| 依赖下载失败 | npm/ohpm registry 未配置；内网走代理 |
| Windows/macOS 编译过、Linux 编译不过 | 大小写引用不一致；`caseSensitiveCheck: true` 后重编译定位 |
| 构建内存溢出（OOM） | 非 daemon 改 hvigorw 的 NODE_OPTS；daemon 模式调守护进程内存 |
| 产物未混淆 | 工程路径含 `.` 开头的隐藏目录，迁移工程路径 |
| 签名后真机装不上 | 确认推的是 `-signed` 包；发布证书/Profile 不能用于调试运行 |
| 上架包被拒 | 非 Release 包；或用调试证书签名 |
| 混淆后运行白屏/功能失效 | 动态访问属性、so/JSON/数据库字段未保留 → 对照适配顺序加 `-keep-property-name`/`-keep-global-name`；动态 import/路由路径未保留 → `-keep-file-name` |
| 混淆后崩溃堆栈不可读 | 用备份的 sourceMaps.map + nameCache.json 跑 `hstack` 还原后再进 `fix` runtime-fix |
| 依赖的 HAR 行为异常 | 该 HAR 的 obfuscation.txt 被二次混淆；联系 HAR 提供方在 consumer-rules.txt 补保留项 |
| Linux 无显示器 CI 要跑模拟器 | 用 Emulator CLI `-noWindow`（见 emulator.md；26.0.0+ 支持 Linux） |

## 与其他子命令的协同

- 构建报错 → `fix` error-fixes 轨道；产物崩溃 → `fix` runtime-fix 轨道。
- DevEco MCP 可用时的构建走 `test` 子命令 `build_project`（MCP 封装）；本页是 MCP 不可用/CI 场景的原生 CLI 通道。
