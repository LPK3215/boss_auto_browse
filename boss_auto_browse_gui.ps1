# BOSS Auto Browse - GUI (standalone script)
# Double-click wrapper: boss_auto_browse_gui.exe (compiled from this file)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class BossAutoWin32 {
    [DllImport("user32.dll")]
    public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);
    [DllImport("user32.dll")]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
}
"@

$allowedBrowsers = @("chrome", "msedge", "firefox", "brave", "opera", "Tabbit")
$targetKeywords = @("BOSS", "Boss", "boss", "zhipin")
$shell = New-Object -ComObject WScript.Shell
$script:count = 0
$script:running = $false
$script:maxCount = 0

function Get-ForegroundProcessName {
    $hwnd = [BossAutoWin32]::GetForegroundWindow()
    if ($hwnd -eq [IntPtr]::Zero) { return $null }
    $pidValue = 0
    [void][BossAutoWin32]::GetWindowThreadProcessId($hwnd, [ref]$pidValue)
    if ($pidValue -eq 0) { return $null }
    try { return (Get-Process -Id $pidValue -ErrorAction Stop).ProcessName } catch { return $null }
}

function Get-AnyBrowserWindow {
    foreach ($name in $allowedBrowsers) {
        $process = Get-Process -Name $name -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 } |
            Sort-Object Id |
            Select-Object -First 1
        if ($null -ne $process) { return $process }
    }
    return $null
}

function Get-TargetBrowserWindow {
    $candidates = foreach ($name in $allowedBrowsers) {
        Get-Process -Name $name -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 -and -not [string]::IsNullOrWhiteSpace($_.MainWindowTitle) }
    }
    if (-not $candidates) { return Get-AnyBrowserWindow }
    foreach ($candidate in ($candidates | Sort-Object ProcessName, Id)) {
        foreach ($keyword in $targetKeywords) {
            if ($candidate.MainWindowTitle -like "*$keyword*") { return $candidate }
        }
    }
    return Get-AnyBrowserWindow
}

function Activate-BrowserWindow($process) {
    [void][BossAutoWin32]::ShowWindow($process.MainWindowHandle, 9)
    [void]$shell.AppActivate([int]$process.Id)
    Start-Sleep -Milliseconds 300
    $activeProcess = Get-ForegroundProcessName
    if ($allowedBrowsers -contains $activeProcess) { return $true }
    Start-Sleep -Milliseconds 500
    $activeProcess = Get-ForegroundProcessName
    return ($allowedBrowsers -contains $activeProcess)
}

function Confirm-KeySent {
    $after = Get-ForegroundProcessName
    return ($allowedBrowsers -contains $after)
}

function Add-Log($message) {
    $script:logList.Items.Insert(0, $message)
    while ($script:logList.Items.Count -gt 200) {
        $script:logList.Items.RemoveAt($script:logList.Items.Count - 1)
    }
}

# ---------- Build UI ----------
$form = New-Object System.Windows.Forms.Form
$form.Text = "BOSS Auto Browse"
$form.Size = New-Object System.Drawing.Size(470, 480)
$form.StartPosition = [System.Windows.Forms.FormStartPosition]::CenterScreen
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedDialog
$form.MaximizeBox = $false

$lblInterval = New-Object System.Windows.Forms.Label
$lblInterval.Text = "Interval (sec):"
$lblInterval.Location = New-Object System.Drawing.Point(15, 15)
$lblInterval.Size = New-Object System.Drawing.Size(110, 24)
$form.Controls.Add($lblInterval)

$txtInterval = New-Object System.Windows.Forms.TextBox
$txtInterval.Text = "2"
$txtInterval.Location = New-Object System.Drawing.Point(130, 12)
$txtInterval.Size = New-Object System.Drawing.Size(55, 24)
$form.Controls.Add($txtInterval)

$lblMax = New-Object System.Windows.Forms.Label
$lblMax.Text = "Max count (0 = unlimited):"
$lblMax.Location = New-Object System.Drawing.Point(200, 15)
$lblMax.Size = New-Object System.Drawing.Size(160, 24)
$form.Controls.Add($lblMax)

$txtMax = New-Object System.Windows.Forms.TextBox
$txtMax.Text = "0"
$txtMax.Location = New-Object System.Drawing.Point(360, 12)
$txtMax.Size = New-Object System.Drawing.Size(75, 24)
$form.Controls.Add($txtMax)

$lblStatus = New-Object System.Windows.Forms.Label
$lblStatus.Text = "Status: Stopped"
$lblStatus.Location = New-Object System.Drawing.Point(15, 50)
$lblStatus.Size = New-Object System.Drawing.Size(220, 24)
$form.Controls.Add($lblStatus)

$lblCount = New-Object System.Windows.Forms.Label
$lblCount.Text = "Sent: 0"
$lblCount.Location = New-Object System.Drawing.Point(250, 50)
$lblCount.Size = New-Object System.Drawing.Size(180, 24)
$form.Controls.Add($lblCount)

$script:logList = New-Object System.Windows.Forms.ListBox
$script:logList.Location = New-Object System.Drawing.Point(15, 85)
$script:logList.Size = New-Object System.Drawing.Size(425, 290)
$script:logList.HorizontalScrollbar = $true
$form.Controls.Add($script:logList)

$btnStart = New-Object System.Windows.Forms.Button
$btnStart.Text = "Start"
$btnStart.Location = New-Object System.Drawing.Point(15, 390)
$btnStart.Size = New-Object System.Drawing.Size(135, 40)
$form.Controls.Add($btnStart)

$btnStop = New-Object System.Windows.Forms.Button
$btnStop.Text = "Stop"
$btnStop.Location = New-Object System.Drawing.Point(160, 390)
$btnStop.Size = New-Object System.Drawing.Size(135, 40)
$btnStop.Enabled = $false
$form.Controls.Add($btnStop)

$btnClose = New-Object System.Windows.Forms.Button
$btnClose.Text = "Close"
$btnClose.Location = New-Object System.Drawing.Point(305, 390)
$btnClose.Size = New-Object System.Drawing.Size(135, 40)
$form.Controls.Add($btnClose)

$timer = New-Object System.Windows.Forms.Timer
$timer.Add_Tick({
    if (-not $script:running) { return }

    if ($script:maxCount -gt 0 -and $script:count -ge $script:maxCount) {
        $timer.Stop()
        $script:running = $false
        $lblStatus.Text = "Status: Finished (max count reached)"
        $btnStart.Text = "Start"
        $btnStart.Enabled = $true
        $btnStop.Enabled = $false
        Add-Log "[done] Reached max count $($script:count)"
        return
    }

    $target = Get-TargetBrowserWindow
    if ($null -eq $target) {
        Add-Log "[wait] No supported browser window found. Keep Chrome/Edge open."
        return
    }

    if (Activate-BrowserWindow $target) {
        try {
            [System.Windows.Forms.SendKeys]::SendWait("{RIGHT}")
            if (Confirm-KeySent) {
                $script:count += 1
                $lblCount.Text = "Sent: $($script:count)"
                Add-Log "[$($script:count)] $($target.ProcessName): $($target.MainWindowTitle)"
            } else {
                Add-Log "[skip] Key sent but browser lost focus."
            }
        } catch {
            Add-Log "[error] SendKeys failed: $($_.Exception.Message)"
        }
    } else {
        Add-Log "[wait] Could not activate browser window."
    }
})

$btnStart.Add_Click({
    if ($script:running) {
        # Pause
        $timer.Stop()
        $script:running = $false
        $btnStart.Text = "Resume"
        $lblStatus.Text = "Status: Paused"
        Add-Log "[pause] Paused."
        return
    }

    $interval = 2.0
    $parsedInterval = 0.0
    if ([double]::TryParse($txtInterval.Text, [ref]$parsedInterval) -and $parsedInterval -gt 0) {
        $interval = $parsedInterval
    }

    $script:maxCount = 0
    $parsedMax = 0
    if ([int]::TryParse($txtMax.Text, [ref]$parsedMax) -and $parsedMax -gt 0) {
        $script:maxCount = $parsedMax
    }

    $timer.Interval = [int]($interval * 1000)
    $script:running = $true
    $btnStart.Text = "Pause"
    $btnStop.Enabled = $true
    $limitText = if ($script:maxCount -gt 0) { "/$($script:maxCount)" } else { "/unlimited" }
    $lblStatus.Text = "Status: Running (every $interval sec)"
    Add-Log "[start] Started, interval=$interval sec, max=$limitText"
    $timer.Start()
})

$btnStop.Add_Click({
    $timer.Stop()
    $script:running = $false
    $script:count = 0
    $lblCount.Text = "Sent: 0"
    $btnStart.Text = "Start"
    $btnStart.Enabled = $true
    $btnStop.Enabled = $false
    $lblStatus.Text = "Status: Stopped"
    Add-Log "[stop] Stopped and reset count."
})

$btnClose.Add_Click({
    $form.Close()
})

$form.Add_FormClosing({
    $timer.Stop()
})

$script:logList.Items.Insert(0, "Ready. Open BOSS/zhipin in a browser, then press Start.")
$script:logList.Items.Insert(0, "Tip: open one candidate detail page first so Right arrow flips candidates.")
[void]$form.ShowDialog()
