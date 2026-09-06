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
- 新增 docs/banner.svg 项目横幅（渐变背景 + 右箭头装饰 + 徽章）
- 新增 docs/architecture.svg 核心架构图（GUI → Timer → Win32 → Browser → SendKeys 流程）
- 新增 docs/gui_preview.svg GUI 界面示意图（按源码实际坐标绘制）
- 新增 docs/scripts/generate_assets.py SVG 生成脚本（可复用，纯标准库）
- README 新增徽章（version / license / platform / lang / type）
- README 新增界面预览、核心架构图可视化展示
- README 新增作者信息段落
- README 截图位置使用 `<!-- TODO: 截图待补充 -->` 占位
- 新增 project_overview/ 全景观览页（沉浸式项目仪表盘，含架构图、技术栈、核心函数、指标统计）
- 新增 project_overview/project_card.html 精简版项目名片长图（支持一键导出 PNG）
- 新增 project_overview.html 全景观览页入口文件
- README 新增 GitHub Stars 动态徽章
- README 新增可视化文档引导段落

### 改进

- CONTRIBUTING Commit 规范改为表格形式，新增 `chore:` 和 `style:` 类型
- CONTRIBUTING 新增分支命名规范表
- CONTRIBUTING 测试场景补充多浏览器同时打开、小数间隔时间场景
- FAQ 新增「如何从源码编译 exe」「杀毒软件报毒怎么办」「可以同时运行多个实例吗」「程序闪退」四个问题
- FAQ 新增「编译与安全」分类

## [1.0.0] - 2026-09-01

### 首次发布

> Release: [GitHub Release v1.0.0](https://github.com/LPK3215/boss_auto_browse/releases/tag/v1.0.0)

- 实现 GUI 界面，基于 `System.Windows.Forms`
- 支持定时自动发送右箭头键（`→`）到浏览器
- 支持多浏览器：Chrome、Edge、Firefox、Brave、Opera、Tabbit
- 智能窗口定位：优先匹配标题含 BOSS/zhipin 关键词的浏览器窗口
- 可配置间隔时间（秒）和最大发送次数（0 = 无限）
- 支持暂停 / 恢复 / 停止 / 关闭
- 实时日志列表，最多保留 200 条
- Win32 API 窗口激活与焦点确认
- 提供 `run.bat` 双击启动器
