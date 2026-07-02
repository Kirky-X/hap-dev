# HAP-DEV —— 鸿蒙应用开发 Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

hap-dev 是一个面向 AI agent 的鸿蒙(HarmonyOS / ArkTS / ArkUI)应用开发 skill。它聚合 5 个子命令,覆盖从工程创建、错误修复、测试验证、本地知识库查询到在线文档搜索的全生命周期。

## 5 个子命令速览

| 子命令     | 一句话功能                                                     | 主要脚本                                       |
| ---------- | -------------------------------------------------------------- | ---------------------------------------------- |
| `create`   | 从内置 ArkTS 工程模板创建 HAP 项目(参数化 appName/包名/bundle)| `scripts/create/copy-template.mjs`             |
| `fix`      | 三轨修复路由:编译错误(21 类)→ 运行时崩溃(JSCrash)→ 语法规范 | `scripts/fix/*.mjs` + `references/error-fixes/`|
| `test`     | MCP 平台检测:Linux 静态检查 / Win·macOS 模拟器闭环            | `scripts/test/platform.py` + `cli.py`          |
| `kb`       | 本地 Qdrant 知识库:7 子动作(query/build/merge/reindex/…)      | `scripts/kb/*.py` + 预构建库                   |
| `search`   | 双端点(developer/device)在线文档搜索 + 详情 HTML→Markdown    | `scripts/search/{_http,search,detail}.py`      |

子命令路由表、触发词、各子动作完整流程见 [SKILL.md](SKILL.md) 与 [references/commands/](references/commands/)。

## 安装

### Python 依赖(kb / search / test 子命令)

```bash
pip install -r requirements.txt
```

依赖清单:

- **必需**: `qdrant-client`、`rank-bm25`、`httpx`、`sentence-transformers`、`modelscope`
- **可选**: `flashrank`(重排)、`openai`(云端嵌入模型)

### Node.js 依赖(create / fix 子命令)

仅需 Node.js 18+(无外部 npm 依赖,全部使用 `node:*` 内置模块)。脚本位置:

- `scripts/create/copy-template.mjs` + `detect-sdk.mjs`
- `scripts/fix/{jscrash-report,parse-jscrash-log,probe-faultlogger,fetch-faultlog,collect-hilog}.mjs`

### DevEco MCP(test 子命令,模拟器验证)

`test` 子命令通过 `@deveco-codegenie/mcp` 操控 DevEco Studio 模拟器。MCP 工具仅 Windows / macOS 可用,Linux 自动降级为静态检查。

```bash
npm install -g @deveco-codegenie/mcp
```

安装后 `scripts/test/cli.py check` 会验证 MCP 可用性,并生成包含 `DEVECO_PATH` / `PROJECT_PATH` 的 MCP 配置。

## config.json 配置

仓库根 `config.json` 是 kb 子命令的唯一配置源(缺失时回落到 `DEFAULT_CONFIG`,但首次使用会通过 AskUserQuestion 询问)。

| 字段                  | 默认值                                                  | 说明                                       |
| --------------------- | ------------------------------------------------------- | ------------------------------------------ |
| `embed_model`         | `sentence-transformers/paraphrase-MiniLM-L3-v2`         | 嵌入模型(本地 ST / `openai://` 云端)     |
| `embed_dim`           | `384`                                                   | 嵌入维度(必须匹配模型)                   |
| `embed_source`        | `modelscope`                                            | 模型下载源(`modelscope` / `''` HF)        |
| `embed_base_url`      | `""`                                                    | 云端 OpenAI 兼容 base_url                  |
| `embed_api_key`       | `""`                                                    | 云端 API key                               |
| `rerank_model`        | `flashrank`                                             | 重排模型(`flashrank` / `openai://…`)      |
| `rerank_source`       | `local`                                                 | 重排模型源                                 |
| `db_path`             | `data/harmonyos.qdrant`                                 | Qdrant 本地库路径                          |
| `collection`          | `harmonyos_docs`                                        | Qdrant 集合名                              |
| `sidebars_dir`        | `sidebars`                                              | sidebar 解析目录                           |
| `endpoints.developer` | `svc-drcn.developer.huawei.com` + 3 catalogs            | developer 端点                             |
| `endpoints.device`    | `svc-drcn.harmonyos.com`                                | device 端点                                |
| `query.default_top_k` | `5`                                                     | 默认返回 top-k                             |
| `query.bm25_weight`   | `0.3`                                                   | BM25 融合权重                              |
| `query.vector_weight` | `0.7`                                                   | 向量融合权重                               |

> **模型名说明**: 用户原 spec 写作 `paraphrase-MiniLM-L3-v2+`(带尾随 `+`),但 `+` 字符在 HuggingFace / ModelScope 仓库 id 中均非法,实际发布的模型名为 `paraphrase-MiniLM-L3-v2`(无 `+`)。`config.json` 与 `DEFAULT_CONFIG` 已使用正确名称。

## 预构建知识库

仓库附带预构建的 `data/harmonyos.qdrant/`(本地 Qdrant 持久化目录),由默认嵌入模型生成,开箱即用:

- **964 条向量**覆盖 7 个文档类型(`device-api` / `device-dev` sidebar 为纯文本标题,设计上产出 0 条)
- 库体积约 **4.3 MB**
- 直接运行 `python3 -m scripts.kb.cli query --question "<keyword>"` 即可查询

### 一键重建 / 切换模型后重索引

```bash
# 完全重建(从 sidebars/ 重新解析、重新嵌入)
python3 scripts/kb/build_db.py

# 仅重嵌入(content_hash 变化或 description 回填的文档)
python3 -m scripts.kb.cli reindex

# 强制全量重嵌入(切换 embed_model 后必跑)
python3 -m scripts.kb.cli reindex --force
```

切换 `embed_model` 的标准流程:

1. 编辑 `config.json` 修改 `embed_model` / `embed_dim` / `embed_source`
2. 运行 `python3 scripts/kb/build_db.py`(全量重建)
3. 验证查询:`python3 -m scripts.kb.cli query --question "测试"`

### 数据库合并

合并两个 Qdrant 库,字段级择优(`description != "无描述"` 优先,`updated_at` 最新者胜):

```bash
python3 -m scripts.kb.cli merge --db-a data/harmonyos.qdrant \
                                 --db-b path/to/other.qdrant \
                                 --out data/harmonyos.merged.qdrant
```

合并后:`description` 变化的文档会标记 `needs_reindex_count`,需运行 `reindex --force` 刷新向量。原库不会被修改,合并产出为新文件。

## 文档 schema(9 字段)

每条文档记录包含:

| 字段            | 类型           | 说明                                                          |
| --------------- | -------------- | ------------------------------------------------------------- |
| `id`            | str (sha1 hex) | URL 的 SHA1,稳定主键                                         |
| `title`         | str            | 文档标题(来自 sidebar `#### N.N. [title](url)`)              |
| `doc_type`      | str            | 文档类型(9 类,见下表)                                       |
| `url`           | str            | 文档原始 URL                                                  |
| `description`   | str            | 文档描述(初始 `"无描述"`,访问详情时回填并重算向量)         |
| `links`         | list[str]      | 双向关联文档 id 列表(从页面"相关推荐"区块解析)              |
| `created_at`    | ISO8601        | 创建时间                                                      |
| `updated_at`    | ISO8601        | 更新时间(description/links 变化时刷新)                      |
| `content_hash`  | str (sha1 hex) | `title+url+doc_type` 的 SHA1,reindex 增量判断用              |

嵌入向量从 `description` 计算(若已回填),否则从 `title` 计算(冷启动)。

### 9 个文档类型

| doc_type             | sidebar 文件                                     | 说明                  |
| -------------------- | ------------------------------------------------- | --------------------- |
| `agc-help`           | `harmonyos-agc-help-sidebar.md`                   | AGC 帮助              |
| `app-api-references` | `harmonyos-app-api-references-sidebar.md`         | 应用 API 参考         |
| `app-docs`           | `harmonyos-app-docs-sidebar-full.md`              | 应用开发文档          |
| `architecture-guide` | `harmonyos-architecture-guide-sidebar.md`         | 架构指南              |
| `atomic-guide`       | `harmonyos-atomic-guide-sidebar.md`               | 原子化服务指南        |
| `best-practices`     | `harmonyos-best-practices-sidebar.md`             | 最佳实践              |
| `design-guide`       | `harmonyos-design-guide-sidebar.md`               | 设计指南              |
| `device-api`         | `harmonyos-device-api-sidebar.md`                 | 设备 API(纯文本标题) |
| `device-dev`         | `harmonyos-device-dev-sidebar.md`                 | 设备开发(纯文本标题) |

> `device-api` / `device-dev` 的 sidebar `####` 行为纯文本标题(无 `[title](url)` 链接),按设计产出 0 条记录。这两个文档类型通过 `search` 子命令(device 端点)在线访问。

## 平台支持矩阵

| 平台    | create | fix(诊断) | fix(hilog/faultlog) | test(静态) | test(模拟器) | kb   | search |
| ------- | :----: | :--------: | :------------------: | :---------: | :-----------: | :--: | :----: |
| Linux   |   ✓    |     ✓      |          ✗           |      ✓      |      ✗        |  ✓   |   ✓    |
| Windows |   ✓    |     ✓      |          ✓           |      ✓      |      ✓        |  ✓   |   ✓    |
| macOS   |   ✓    |     ✓      |          ✓           |      ✓      |      ✓        |  ✓   |   ✓    |

- `test` 子命令在 Linux 显式禁用模拟器工具并提示用户(`scripts/test/platform.py:disabled_tools_hint`)
- `fix` 的 hilog / faultlog 采集依赖 `hdc`,仅 Win / macOS 可用

## 仓库结构

```
hap-dev/
├── SKILL.md                          # 5 子命令路由器 + 通用规则
├── config.json                       # kb 配置(模型/库/端点)
├── requirements.txt                  # Python 依赖
├── sidebars/                         # 9 个 harmonyos-*-sidebar.md
├── data/
│   └── harmonyos.qdrant/             # 预构建 Qdrant 本地库(~4.3 MB)
├── references/
│   ├── commands/{create,fix,test,kb,search}.md  # 5 子命令流程文档
│   ├── error-fixes/                  # 21 类 ArkTS 编译错误 + assets
│   ├── runtime-fix/                  # JSCrash 诊断 README + evals
│   ├── grammar/                      # ArkTS 语法规范 + topic-aliases
│   ├── arkui/                        # ArkUI 组件 cookbook + 检查清单
│   └── project-template/application/ # 完整 ArkTS 工程模板
└── scripts/
    ├── create/                       # copy-template.mjs + detect-sdk.mjs
    ├── fix/                          # 5 个 .mjs 诊断脚本 + shared/
    ├── kb/                           # 11 模块 + tests/ + build_db.py
    ├── search/                       # _http.py + search.py + detail.py + tests/
    └── test/                         # platform.py + cli.py + tests/
```

## 测试

```bash
# 全部测试(kb + search + test 子命令)
python3 -m pytest scripts/ -v

# 仅 kb 子命令
python3 -m pytest scripts/kb/tests/ -v
```

测试使用 `FakeEmbedder`(SHA1 派生的确定性向量)替代真实模型下载,确保离线可运行。当前共 192+ 测试用例。

## 开发工作流

本项目使用 OpenSpec 规格驱动开发,变更记录在 `openspec/changes/`:

- `openspec/changes/create-hap-dev-skill/` —— 当前创建变更(proposal / design / specs / tasks)
- 工作流参考 [specmark skill](../specmark/)

## License

MIT,见 [LICENSE](LICENSE)。
