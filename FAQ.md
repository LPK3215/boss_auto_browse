# 常见问题

## 运行相关

### 双击 run.bat 没反应或闪退？

以管理员身份运行 PowerShell，执行：

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

然后再双击 `run.bat`。`run.bat` 中已包含 `-ExecutionPolicy Bypass`，但如果系统策略过于严格可能仍需调整。

### 提示 "无法加载文件，因为在此系统上禁止运行脚本"

这是 PowerShell 执行策略限制。用以下命令解除：

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 程序启动了但没有自动按键？

确保：
1. 浏览器已打开，且窗口没有最小化
2. 已进入 BOSS 直聘的候选人/职位详情页
3. 点击了 GUI 中的 **Start** 按钮
4. 状态栏显示 "Running"

### 按键发送后浏览器没有反应？

工具会优先激活标题含 "BOSS"/"zhipin" 的窗口。如果浏览器标题不包含这些关键词，会 fallback 到任意浏览器。确保目标浏览器在前台，且详情页已加载完成。

## 浏览器支持

### 支持哪些浏览器？

Chrome、Edge、Firefox、Brave、Opera、Tabbit。其他基于 Chromium 的浏览器如果进程名不同，需要手动在 `boss_auto_browse_gui.ps1` 的 `$allowedBrowsers` 数组中添加。

### 如何添加新浏览器？

编辑 `boss_auto_browse_gui.ps1`，找到第 19 行：

```powershell
$allowedBrowsers = @("chrome", "msedge", "firefox", "brave", "opera", "Tabbit")
```

在数组中添加你的浏览器进程名即可。

## 功能相关

### 间隔时间最小可以设多少？

可以设为小数（如 `0.5` 秒），但不建议低于 1 秒，否则浏览器可能来不及响应右箭头键。

### 最大次数设为 0 是什么意思？

0 表示无限，会一直发送直到手动停止。设为正整数（如 50）则发送 50 次后自动停止。

### 日志最多保留多少条？

200 条。超出后自动从底部移除旧日志。

### 工具会修改浏览器页面内容吗？

不会。工具仅模拟键盘按键（右箭头），不注入任何 JavaScript 或修改 DOM。所有操作都是系统级的按键发送。

## 编译与安全

### 如何从源码编译 exe？

本项目提供的 `boss_auto_browse_gui.exe` 是通过 [PS2EXE](https://github.com/MScholtes/PS2EXE) 将 PowerShell 脚本打包为可执行文件的。如需自行编译：

```powershell
# 安装 PS2EXE 模块
Install-Module -Name ps2exe -Scope CurrentUser

# 编译
Invoke-PS2EXE -Input .\boss_auto_browse_gui.ps1 -Output .\boss_auto_browse_gui.exe -NoConsole
```

### 杀毒软件/Windows Defender 报毒怎么办？

由于 `boss_auto_browse_gui.exe` 是由 PowerShell 脚本打包生成，部分杀毒软件可能误报。解决方法：

1. **使用源码运行**：直接运行 `boss_auto_browse_gui.ps1`，不走 exe
2. **添加信任**：在杀毒软件中将 `boss_auto_browse_gui.exe` 添加到信任列表
3. **自行编译**：按上文步骤从源码自行编译，增强可信度

### 可以同时运行多个实例吗？

技术上可以，但不建议。多个实例会同时发送按键，可能导致目标浏览器窗口反复切换。如果需要在不同浏览器中使用，建议错开间隔时间或分时运行。

### 程序闪退或没有界面？

可能是 PowerShell 环境问题。尝试：

1. 用 `run.bat` 启动（已包含 `-ExecutionPolicy Bypass`）
2. 在 PowerShell 中手动运行脚本，查看报错信息：
   ```powershell
   powershell -ExecutionPolicy Bypass -NoProfile -File boss_auto_browse_gui.ps1
   ```
3. 确保 `.NET Framework` 可用（`System.Windows.Forms` 依赖它）
