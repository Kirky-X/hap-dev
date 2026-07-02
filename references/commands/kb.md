# kb 子命令 —— 本地 Qdrant 知识库

本地 Qdrant 知识库，9 类 sidebar 文档分类存储，向量嵌入（默认 `sentence-transformers/paraphrase-MiniLM-L3-v2+`，可切 ModelScope / 云端 OpenAI）+ bm25 关键词索引 + 可选 FlashRank 重排。`description` 懒填充 + 向量回填 + 双向链接。

> 🔴 **CHECKPOINT**：所有路径 / 模型名 / 端点都从 `config.json` 读，禁止硬编码（参见"禁止事项 #2"）。

## 子动作路由表

命令格式：`python3 -m scripts.kb.cli <action> [args]`

| 子动作 | 用途 | 关键参数 |
| ---- | ---- | ---- |
| `query`（默认） | 混合向量+BM25 检索 | `--question` `--top-k` `--doc-type` `--rerank` |
| `build` | 解析 sidebars 构建索引 | `--sidebars-dir` |
| `merge` | 合并两个库为新库 | `--db-a` `--db-b` `--out` |
| `reindex` | 重算向量 | `--force` |
| `update-description` | 回填单文档 description | `--id` `--description` |
| `update-links` | 提取并写入双向链接 | `--id` `--content` |
| `config` | 打印当前生效配置 | （无） |

`--config <path>` 全局可选，覆盖默认 `config.json` 加载路径。

## 9 类 doc_type

| doc_type | sidebar 文件 |
| ---- | ---- |
| `agc-help` | `harmonyos-agc-help-sidebar.md` |
| `app-api-references` | `harmonyos-app-api-references-sidebar.md` |
| `app-docs` | `harmonyos-app-docs-sidebar-full.md` |
| `architecture-guide` | `harmonyos-architecture-guide-sidebar.md` |
| `atomic-guide` | `harmonyos-atomic-guide-sidebar.md` |
| `best-practices` | `harmonyos-best-practices-sidebar.md` |
| `design-guide` | `harmonyos-design-guide-sidebar.md` |
| `device-api` | `harmonyos-device-api-sidebar.md` |
| `device-dev` | `harmonyos-device-dev-sidebar.md` |

`query --doc-type` 只接受上述 9 类之一；不指定则全库检索。

## config.json 字段说明

| 字段 | 默认值 | 说明 |
| ---- | ---- | ---- |
| `embed_model` | `sentence-transformers/paraphrase-MiniLM-L3-v2+` | 嵌入模型；`openai://` 前缀走云端 |
| `embed_dim` | `384` | 嵌入维度 |
| `embed_source` | `modelscope` | 模型来源（`modelscope` / `local` / `openai`） |
| `embed_base_url` | `""` | 云端嵌入 API base URL |
| `embed_api_key` | `""` | 云端嵌入 API key |
| `rerank_model` | `flashrank` | 重排模型；`none` 禁用重排 |
| `rerank_source` | `local` | 重排模型来源 |
| `rerank_base_url` / `rerank_api_key` | `""` | 云端重排 API 配置 |
| `db_path` | `data/harmonyos.qdrant` | Qdrant 本地存储路径 |
| `collection` | `harmonyos_docs` | 集合名 |
| `sidebars_dir` | `sidebars` | sidebar 源目录 |
| `endpoints` | 见 `config.json` | 搜索端点（developer / device），详情见 `search` 子命令文档 |
| `query.default_top_k` | `5` | `query` 默认 top-k |

## 主要流程

### 1. query（默认子动作）

```bash
python3 -m scripts.kb.cli query \
  --question "如何在 ArkUI 里实现一个登录页" \
  [--top-k 5] \
  [--doc-type best-practices] \
  [--rerank]
```

未传 `--top-k` → 用 `config.json` 的 `query.default_top_k`（默认 5）。

输出 JSON 数组，每项含 `id` / `title` / `url` / `score` / `doc_type` / `description` / `needs_description` 等字段。

#### 命中 `needs_description=True` → 触发懒填充

`description` 字段为空或为 "无描述" 时，`needs_description=True`。agent **MUST** 执行懒填充：

1. 从命中文档取 `id`（即 `object_id`）与 `catalog`（或 `doc_type` 对应的 catalog）。
2. 调 `search detail` 取正文：
   ```bash
   python3 scripts/search/detail.py <object_id> <catalog>
   ```
3. agent 基于正文生成 **≤200 字** description。
4. 回填并重算向量：
   ```bash
   python3 -m scripts.kb.cli update-description \
     --id <id> \
     --description "<不超 200 字的描述>"
   ```
   脚本自动重算向量并更新 `updated_at`。
5. （继续）触发链接提取流程（见下文）。

### 2. update-links（双向链接提取）

agent 在 description 回填过程中已取到正文，**接着** 提取链接：

```bash
python3 -m scripts.kb.cli update-links \
  --id <id> \
  --content "<markdown 正文>"
```

`--content` 也支持传文件路径（脚本检测到路径存在则读文件）。

脚本行为：

- 解析正文中的"相关推荐"区块。
- 把推荐链接的 URL → id 映射。
- **双向写入**：A 文档的 `related_ids` 加 B，B 文档的 `related_ids` 也加 A。

> 🔴 **CHECKPOINT**：双向链接必须真正双向写入；不允许只写单向。

### 3. build（构建索引）

```bash
python3 -m scripts.kb.cli build [--sidebars-dir <dir>]
```

未传 `--sidebars-dir` → 用 `config.json` 的 `sidebars_dir`（默认 `sidebars`）。

脚本：解析 9 个 sidebar 文件 → 生成文档记录 → 嵌入 → 写入 Qdrant。输出 `{built, counts}`。

### 4. reindex（重算向量）

```bash
python3 -m scripts.kb.cli reindex [--force]
```

不带 `--force` → 仅对 `content_hash` 与 `title+url+doc_type` 不一致的文档重算（即检测变更）。
带 `--force` → 全量重算所有文档向量。

### 5. merge（合并两个库）

```bash
python3 -m scripts.kb.cli merge \
  --db-a <pathA> \
  --db-b <pathB> \
  --out <new_path>
```

脚本行为：

1. 创建新库 `<new_path>`。
2. 把 A、B 两个旧库改名为 `<old>.bak.<timestamp>`（备份）。
3. 字段级 `updated_at` 比较：同一文档（按 `id`）取 `updated_at` 较新的一方。
4. 输出 JSON `{merged, needs_reindex_count, ...}`。
5. 若 `needs_reindex_count > 0` → 脚本在 stderr 提示：在新库上跑 `reindex --force` 刷新向量。

**用户后续操作**：

- 检查新库无误后，删除备份：
  ```bash
  python3 -m scripts.kb.cli merge --confirm-delete <backup_path>
  ```
- 备份未删前可随时回滚。

### 6. update-description（单文档 description 回填）

```bash
python3 -m scripts.kb.cli update-description \
  --id <id> \
  --description "<不超 200 字>"
```

脚本：写入 description → 重算该文档向量 → 更新 `updated_at`。输出 `{updated: <id>}`。

### 7. config（打印生效配置）

```bash
python3 -m scripts.kb.cli config
```

打印当前生效的 `config.json` JSON。

## 切换模型流程

切换嵌入模型：

1. 编辑 `config.json` 的 `embed_model`（如改为 `openai://text-embedding-3-small` 或其他 ModelScope 模型）。
2. 全量重算：
   ```bash
   python3 -m scripts.kb.cli reindex --force
   ```
3. 重算后所有文档向量基于新模型。

> 切换后维度 `embed_dim` 也要相应改；维度不匹配会导致 Qdrant 报错。

## 预构建库（开箱即用）

`data/harmonyos.qdrant/` 已提交仓库（基于默认模型 `paraphrase-MiniLM-L3-v2+` 预构建）。clone 即用，无需重算。

启用条件（参见 SKILL.md "config.json 驱动"）：

- `config.json` 缺失 → agent 经 `AskUserQuestion` 询问；选默认 → 生成默认 `config.json` 并用预构建库。
- `embed_model` 为默认值且 `data/harmonyos.qdrant/` 存在 → **直接用预构建库，不重算**。
- `embed_model` 非默认 → 下载模型 + `reindex --force` 全量重算。

## ArkUI references 协同

查询 ArkUI 问题（组件 / 布局 / 状态管理 / `.ets` UI 代码）时，**同时**参考 `references/arkui/`：

| 文件 | 用途 |
| ---- | ---- |
| `references/arkui/component-cookbook.md` | 组件 cookbook |
| `references/arkui/api-guardrails.md` | API 使用护栏 |
| `references/arkui/common-mistakes.md` | 常见错误 |
| `references/arkui/ui-quality-checklist.md` | UI 质量检查清单 |

`kb query` 命中 ArkUI 主题文档后，agent 应**同时**查阅上述 references，避免给出与项目风格冲突的建议。

## 失败模式与 fallback

| 触发条件 | 一线修复 | 兜底 |
| ---- | ---- | ---- |
| `config.json` 缺失 | agent 经 `AskUserQuestion` 询问，选默认则生成默认配置 | 用户拒绝配置则停止，提示手动编辑 `config.json` |
| 预构建库不存在 | 调 `kb build` 从 `sidebars/` 重建 | `sidebars/` 缺失则提示用户从 `temp/` 复制 |
| `kb query` 无结果 | 换关键词或调 `search` 在线搜索 | `search` 也无结果则建议直访 `developer.huawei.com` |
| ModelScope 模型下载失败 | 重试 + 镜像源配置 | 提示用户手动下载或切 `openai://` 云端模型 |

## 边界情形

| 情形 | 处理 |
| ---- | ---- |
| `--doc-type` 非 9 类之一 | argparse 校验失败，退出码 2；提示合法值 |
| `query` 命中但 `needs_description=True` | 必须执行 description 懒填充流程；不填充算违规 |
| `update-links` 仅单向写 | 禁止；脚本必须双向写 `related_ids` |
| `merge` 后 `needs_reindex_count > 0` | 在新库跑 `reindex --force` 刷新向量 |
| 切换模型后维度不匹配 | 同步改 `embed_dim`，再 `reindex --force` |
| `update-description` 描述超 200 字 | agent 自我截断到 200 字内（脚本不强制，但规范要求） |

## 交付核对清单

### query 流程
- [ ] `--question` 已传；`--doc-type`（如有）属于 9 类之一
- [ ] 命中 `needs_description=True` 文档时已执行懒填充（取正文 → 生成 ≤200 字 → update-description）
- [ ] 懒填充后已执行 update-links 双向链接
- [ ] ArkUI 主题查询同时参考了 `references/arkui/`

### build / reindex 流程
- [ ] `sidebars_dir` 来自 `config.json` 或 `--sidebars-dir`，未硬编码
- [ ] 切换模型后已 `reindex --force` 全量重算
- [ ] 维度 `embed_dim` 与新模型匹配

### merge 流程
- [ ] `--db-a` `--db-b` `--out` 三参数齐全
- [ ] 旧库已自动备份为 `.bak.<timestamp>`
- [ ] `needs_reindex_count > 0` 时已在新库跑 `reindex --force`
- [ ] 用户确认新库无误后已调 `merge --confirm-delete <backup>` 删备份

### config 流程
- [ ] `embed_model` / `rerank_model` / `db_path` / `endpoints` 全部从 `config.json` 读
- [ ] 切换 `embed_model` 后已同步改 `embed_dim` 并 `reindex --force`
