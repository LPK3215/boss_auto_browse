# 贡献指南

这是一个小玩具项目，核心就一个脚本，维护成本低。如果你发现了 bug 或有小的改进想法，欢迎提交。

## 提交 Issue

- Bug 报告：描述复现步骤、环境信息（Windows 版本、PowerShell 版本、浏览器及版本）
- 功能建议：说明使用场景和期望效果

提交 Issue 前，请先搜索是否已有相同 Issue，避免重复。

## 提交 Pull Request

1. Fork 本仓库
2. 创建分支：`git checkout -b feature/your-feature-name`
3. 修改代码，确保逻辑正确
4. 如果修改了 `boss_auto_browse_gui.ps1`，请通过以下方式验证：
   ```powershell
   # 运行脚本验证功能正常
   powershell -ExecutionPolicy Bypass -NoProfile -File boss_auto_browse_gui.ps1
   ```
5. 提交 Commit，信息清晰描述改动内容
6. 发起 Pull Request，标题格式：`[feat]` / `[fix]` / `[docs]` + 简述

## Commit 规范

- `feat:` 新功能（如 `feat: add keyboard shortcut support`）
- `fix:` bug 修复（如 `fix: timer not stopping on close`）
- `docs:` 文档更新（如 `docs: update FAQ`）
- `refactor:` 重构（如 `refactor: simplify window detection logic`）

## 代码规范

- 保持 PowerShell 风格一致：函数名使用 `Verb-Noun` 格式
- 变量名使用 `camelCase`，脚本级变量使用 `$script:` 前缀
- 每个函数之间保留一个空行
- 逻辑块之间适当添加空行提高可读性
- 注释使用英文，保持简洁明了

## 项目结构说明

本项目核心文件只有一个 `boss_auto_browse_gui.ps1`，所有逻辑都在其中。新增功能建议优先在现有文件内扩展，避免过度拆分。

## 测试场景

提交 PR 前，建议测试以下场景：

- [ ] 无浏览器时启动，日志提示正常
- [ ] 有浏览器但无 BOSS 标题，能 fallback 到任意浏览器
- [ ] Start → Pause → Resume 流程正常
- [ ] Stop 能正确重置计数
- [ ] 设置最大次数后达到上限自动停止
- [ ] 关闭窗口时 Timer 正确停止

## 行为准则

请保持友善和尊重，共同维护良好的社区氛围。
