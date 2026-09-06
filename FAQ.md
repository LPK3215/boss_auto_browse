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
