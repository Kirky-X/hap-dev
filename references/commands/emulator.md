# emulator —— 模拟器命令行管理（Emulator CLI + hdc）

DevEco Studio 内置模拟器与 Command Line Tools 独立模拟器的命令行操作全集：镜像下载、创建/启动/关闭、hdc 连接推包、场景化模拟与 UI 自动化。内容依据华为官方文档（2026-10 抓取）：

- 通过命令行使用模拟器：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line>（DevEco Studio 文档中心同内容镜像：<https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-emulator-command-line>，命令集已比对一致）
- 模拟器工具（CLT 集成版）：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-emulator>
- 模拟器概述：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-overview>（章节内另有[修改模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-modify)、[模拟器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-faqs)）

## 工具形态与版本边界

| 形态 | 路径 | 平台 |
| ---- | ---- | ---- |
| DevEco Studio 内置 | `{DevEco Studio 安装目录}/tools/emulator` | Windows / macOS |
| Command Line Tools 集成 | `{CLT 安装目录}/emulator` | CLT 6.1.0 Release 起 Windows/macOS；**26.0.0 起支持 Linux** |

> 🔴 **CHECKPOINT**：若某版本模拟器在 DevEco Studio 中需要登录开发者账号，则该模拟器无法命令行启动，只能在 GUI 启动。命令行参数自 DevEco Studio 6.1.0 Beta1 起不区分大小写（`-list` 等价 `-LIST`）；名称/路径含空格或特殊字符必须加引号；macOS 未配 PATH 时用 `./Emulator`。

通用约定：

```bash
export PATH="{工具目录}/emulator:$PATH"   # 或进入目录直接执行
Emulator -help                             # 全部命令
Emulator -help -create                     # 单命令详解（26.0.0+）
```

## 镜像与生命周期

```bash
# 镜像（6.1.0 Beta1+）
Emulator -imageList -deviceType phone [-downloaded true] [-http_proxy {协议://user:pass@host:port}]
Emulator -install   -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot /path/Sdk [-force]
Emulator -uninstall -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot /path/Sdk [-force]

# 创建（-hotBoot true 建快照热启动实例）
Emulator -create Mate70Pro -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" \
  -instancePath /path/Emulator -imageRoot /path/Sdk \
  [-screenProfile "Mate 70 Pro"] [-storage 8] [-memory 16] [-hotBoot true]

# 查询 / 删除
Emulator -list -details
Emulator -delete Mate70Pro -instancePath /path/Emulator -force

# 启动（6.1.0 Beta1+ 用 -start；更早版本用 -hvd）
Emulator -start "my Emulator" -instancePath /path/Emulator -imageRoot /path/Sdk [-hdcport 12345] [-bootMode coldboot] [-noWindow]
Emulator -hvd "my Emulator" -path /path/Emulator -imageRoot /path/Sdk   # 旧版语法

# 关闭
Emulator -stop "my Emulator"
```

`-start` 参数要点：

| 参数 | 说明 |
| ---- | ---- |
| `-hdcport` | 指定 hdc 端口，范围 10000-16555（6.0.1 Beta1+） |
| `-bootMode` | 6.1.0 Release+：`coldboot`（冷启动，保留数据）/ `snapshot`（热启动，恢复上次关机快照，需创建时选 Quick Boot 或 `-hotBoot true`）/ `reset`（清数据冷启动）。缺省按创建时选择 |
| `-noWindow` | 无界面启动。**无图形界面的 Linux 环境（CI 服务器）必选**（26.0.0+） |
| `-instancePath` / `-imageRoot` | 6.1.0 Beta1 起可选，缺省用 DevEco Studio 中的路径 |

配置辅助：`-config -instancePath … -imageRoot … [-http_proxy …]` 持久化默认路径；`-unset instancePath` 清除；`-screenProfileList -deviceType phone -details [-update]` 查屏幕模板；`-logZip "my Emulator" -logPath /path/Log.zip` 收集日志（须 .zip 后缀）；`-version`；`-license accept` 首次同意协议。

## hdc 连接模拟器

模拟器的 hdc 端点为 `127.0.0.1:5555`；端口被占时自 5555 起步进 +2（5555/5557/5559…，范围 5555-15555）：

```bash
hdc list targets            # 确认是否已连接
hdc tconn 127.0.0.1:5555    # 未连接时手动建立
# 连接后与真机一致：bm install / aa start 等（见 build.md hdc 安装运行节）
```

## 场景化模拟与 UI 自动化

统一模式：`Emulator -instance {模拟器名称} <能力参数>`。

```bash
Emulator -instance "Mate 80 Pro" -rotation left            # 旋转 left/right
Emulator -instance "Mate 80 Pro" -volume up                # 音量 up/down
Emulator -instance "Mate 80 Pro" -power                    # 亮/灭屏
Emulator -instance "Mate 80 Pro" -shake                    # 摇一摇
Emulator -instance "Mate X7" -foldedState half-open        # 折叠开合
Emulator -instance "Mate 80 Pro" -screenshot -screenshotPath "/path/"
Emulator -instance "Mate 80 Pro" -battery 50               # 电量
Emulator -instance "Mate 80 Pro" -batteryStatus 1          # 电池状态 0/1
Emulator -instance "Mate 80 Pro" -gps -longitude 180 -latitude 90 -altitude 2000 -bearing 200
# GUI 等价（DevEco 位置模拟）：仅支持 debug 签名应用（release 上架包不可），设备需 API 26.0.0+ 与开发者模式
# https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mock-location
Emulator -instance "Mate 80 Pro" -outdoorRunning           # 运动场景（另有 -outdoorCycling / -drivingNavigation）
Emulator -instance "Mate 80 Pro" -sensor -light 50         # 传感器 -light/-steps/-heartrate
```

UI 自动化（控件 ID 来自 `-uiLayout` 输出的 Widget Tree）：

```bash
Emulator -instance "Mate 80 Pro" -uiLayout -i              # 当前界面控件树（-a 全量）
Emulator -instance "Mate 80 Pro" -click 10                 # 按控件 ID 点击
Emulator -instance "Mate 80 Pro" -click "100 100"          # 按坐标点击
Emulator -instance "Mate 80 Pro" -slide "10 up"            # 控件上滑（另支持 坐标对/控件到坐标）
Emulator -instance "Mate 80 Pro" -slide "100 100 200 200"  # 从 (100,100) 滑到 (200,200)
Emulator -instance "Mate 80 Pro" -fill "10 Hello,World"    # 向控件 ID 10 输入文本
```

## Linux 平台专项（26.0.0+）

- 仅支持 Ubuntu 18.04+，先装依赖：`apt install -y libatomic1 libpulse0 libegl1 libgbm1 libgl1 libpng16-16 libfontconfig1 libfreetype6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libsm6 libice6 libxkbcommon-x11-0 libxkbcommon0 libglib2.0-0`
- 依赖 KVM：当前用户加入 `/dev/kvm` 所属组。
- 图形渲染依赖 `/dev/dri` 渲染节点（card0/renderD128 等）：当前用户加入对应节点用户组。
- 远程桌面操作 Linux 时，图形驱动须支持 OpenGL ≥ 4.1。
- 无图形界面环境启动**必加** `-noWindow`。

## 与 test 子命令的协同（路由规则）

| 场景 | 通道 |
| ---- | ---- |
| Windows/macOS + DevEco MCP 已装 | `test` 子命令 MCP 闭环（build_project → start_app → verify_ui 自然语言用例），本页命令作为补充（模拟器没起、要旋转/GPS 等场景化操作时） |
| MCP 未装、Linux 平台、CI 无图形环境 | **原生 CLI 通道**：Emulator CLI 起模拟器（`-noWindow`）→ hdc tconn → bm install / aa start → hilog 采集喂 `fix` runtime-fix |
| UI 断言 | MCP 不可用时用 `-uiLayout -i` 输出比对控件树；或 `-screenshot` 存图后由 agent 视觉判断 |

## 离线部署（无网络环境）

先在有网电脑下载 DevEco Studio 与所需镜像（如 `D:\Sdk\system-image\HarmonyOS-xxx\phone_all_x86`），再把 DevEco 与镜像拷到无网机：**镜像子文件夹路径必须与有网机一致**（`system-image\HarmonyOS-xxx\phone_all_x86` 全层同名），创建模拟器时把镜像路径指到拷贝后的根（如 `D:\No-network\Sdk`）。详见[离线部署模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-no-network)。

## 失败模式

| 症状 | 一线修复 |
| ---- | ---- |
| 命令行启动无反应/失败 | 该版本模拟器需登录账号 → 只能 GUI 启动；或首次使用未 `-license accept` |
| `hdc list targets` 看不到模拟器 | `hdc tconn 127.0.0.1:5555`；端口占用则 +2 递增试到 15555 |
| Linux 启动崩溃 | 依赖未装齐 / 用户不在 kvm、/dev/dri 组；远程桌面 OpenGL < 4.1 |
| 无图形 Linux 卡在窗口初始化 | 漏了 `-noWindow` |
| `-bootMode snapshot` 失败 | 创建时未选 Quick Boot / 未加 `-hotBoot true`，改 coldboot 或重建 |
| macOS 提示无法验证开发者 | 系统设置 > 隐私与安全性 > 仍要打开；或改用 DevEco Studio 目录下的 Emulator |
| 镜像下载失败 | 网络受限时 `-http_proxy` 配代理（密码特殊字符需转义） |
| 端口范围报错 | `-hdcport` 超出 10000-16555 |
