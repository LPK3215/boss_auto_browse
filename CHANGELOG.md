# 变更记录

本项目版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范。

## [Unreleased]

### 新增

- 新增 FAQ.md 常见问题文档
- 新增 AUTHORS 作者信息文件
- 新增 .gitattributes 行尾规范
- README 项目结构树补充完整文件列表
- CONTRIBUTING 新增 Commit 规范和 PR 标题格式
- .gitignore 补充 PowerShell 临时文件和日志文件规则

## [1.0.0] - 2026-09-01

### 首次发布

- 实现 GUI 界面，基于 `System.Windows.Forms`
- 支持定时自动发送右箭头键（`→`）到浏览器
- 支持多浏览器：Chrome、Edge、Firefox、Brave、Opera、Tabbit
- 智能窗口定位：优先匹配标题含 BOSS/zhipin 关键词的浏览器窗口
- 可配置间隔时间（秒）和最大发送次数（0 = 无限）
- 支持暂停 / 恢复 / 停止 / 关闭
- 实时日志列表，最多保留 200 条
- Win32 API 窗口激活与焦点确认
- 提供 `run.bat` 双击启动器
