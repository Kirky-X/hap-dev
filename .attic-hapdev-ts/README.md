# hap-dev .ts 双实现迁移残留（2026-09-12）

scripts/fix/ 原有 Bun(.ts) 与 Node(.mjs) 两套实现，全部文档只引用 .mjs 版本。
为消除双倍维护与漂移面，.ts 版本移入本目录。确认无 Bun 依赖后可整体删除。

迁移清单：collect-hilog / fetch-faultlog / parse-jscrash-log / probe-faultlogger / shared/{hdc,jscrash-faultlogger,jscrash-parse,utils}
