# 提交与 Issue 引用

- 使用 Conventional Commits，按独立修复、文档和版本准备拆分提交。
- 与 Issue 直接相关的修复提交引用对应编号，例如 `fix(probability): preserve reply attachments (#7)`。
- 独立 review 修复、README 调整、发布规范和版本号更新使用各自的提交，Issue 引用仅用于相关修复。
- Issue 的回复与关闭由维护者处理；发布操作保留 Issue 当前状态，提交和 Release 使用普通关联引用。

# Release 发布格式

- Release 名称使用中文插件名并附版本号：`麦麦多平台TTS语音 v<版本号>`。
- 正文条目使用中文，分区标题保留英文，依次使用 `# Features`、`# Fixes`。
- `Features` 列出新增功能，`Fixes` 列出修复；条目有关联 Issue 或 PR 时附对应 GitHub 链接，引用以实际关联为准。
- 存在首次贡献者时，在修复列表之后添加 `## New Contributors`，用中文说明其首次贡献，并链接对应 PR。
- 正文末尾使用 `**Full Changelog**`，链接到上一发布标签和本次标签之间的 GitHub compare 页面。
- 发布前完成相关测试、PC 与手机 WebUI 交互检查、版本及文档核对。
- 发布正文保留运行要求和必要升级提示，使用中文描述；功能与修复条目直接说明变化，验证结果记录在开发说明中。
- 发布资料中的版本号与 `_manifest.json`、README、WebUI 页脚和 changelog 保持一致。

正文结构：

```markdown
# Features

- 新增功能说明。([相关 Issue 或 PR](实际关联链接))

# Fixes

- 修复内容说明。([相关 Issue 或 PR](实际关联链接))

运行要求与必要升级提示。

**Full Changelog**: [上一标签...本次标签](https://github.com/WhiteCloudOL/maimai-tts-plugin/compare/上一标签...本次标签)
```

首次贡献者分区按实际贡献情况插入正文结构，Issue 或 PR 链接按条目的实际关联填写。
