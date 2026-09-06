#!/usr/bin/env python3
"""
BOSS Auto Browse - SVG Asset Generator
======================================
用途：生成项目所需的 SVG 可视化资产（banner、architecture、gui_preview）
依赖：仅使用 Python 标准库，无需安装任何第三方包
运行方式：python docs/scripts/generate_assets.py
输出路径：docs/banner.svg, docs/architecture.svg, docs/gui_preview.svg

作者：LPK3215
"""

import os

# 项目根目录（相对于本脚本的 ../..）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")


# ---------------------------------------------------------------------------
# 1. Banner SVG — 项目横幅
# ---------------------------------------------------------------------------
def generate_banner():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="760" height="200" viewBox="0 0 760 200">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="50%" stop-color="#16213e"/>
      <stop offset="100%" stop-color="#0f3460"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#e94560"/>
      <stop offset="100%" stop-color="#f47b7b"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="760" height="200" rx="16" fill="url(#bgGrad)"/>

  <!-- Decorative right-arrow motifs -->
  <g opacity="0.06" fill="#e94560">
    <polygon points="600,40 640,60 600,80"/>
    <polygon points="640,60 680,80 640,100"/>
    <polygon points="680,80 720,100 680,120"/>
    <polygon points="600,100 640,120 600,140"/>
    <polygon points="640,120 680,140 640,160"/>
  </g>

  <!-- Accent bar -->
  <rect x="40" y="52" width="6" height="96" rx="3" fill="url(#accentGrad)"/>

  <!-- Title -->
  <text x="64" y="88" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="32" font-weight="700" fill="#ffffff">
    BOSS Auto Browse
  </text>

  <!-- Subtitle -->
  <text x="64" y="116" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="15" fill="#a0a0c0">
    定时向浏览器发送右箭头键 · 自动切换 BOSS 直聘候选人卡片
  </text>

  <!-- Badges row -->
  <g transform="translate(64, 140)">
    <!-- Version badge -->
    <rect x="0" y="0" width="80" height="24" rx="12" fill="#e94560" opacity="0.9"/>
    <text x="40" y="16" font-family="Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">v1.0.0</text>

    <!-- PowerShell badge -->
    <rect x="90" y="0" width="90" height="24" rx="12" fill="#013755" opacity="0.85"/>
    <text x="135" y="16" font-family="Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">PowerShell</text>

    <!-- Platform badge -->
    <rect x="190" y="0" width="70" height="24" rx="12" fill="#0078D4" opacity="0.85"/>
    <text x="225" y="16" font-family="Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">Windows</text>

    <!-- License badge -->
    <rect x="270" y="0" width="60" height="24" rx="12" fill="#2ea44f" opacity="0.85"/>
    <text x="300" y="16" font-family="Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">MIT</text>

    <!-- Open Source Toy badge -->
    <rect x="340" y="0" width="110" height="24" rx="12" fill="#6c5ce7" opacity="0.85"/>
    <text x="395" y="16" font-family="Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">Open Source Toy</text>
  </g>

  <!-- Right arrow icon (large, decorative) -->
  <g transform="translate(660, 100)" filter="url(#glow)">
    <circle cx="0" cy="0" r="36" fill="none" stroke="#e94560" stroke-width="2.5" opacity="0.3"/>
    <polygon points="-12,-14 14,0 -12,14 -4,0" fill="#e94560" opacity="0.8"/>
  </g>
</svg>"""

    path = os.path.join(DOCS_DIR, "banner.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {path}")


# ---------------------------------------------------------------------------
# 2. Architecture SVG — 核心架构流程图
# ---------------------------------------------------------------------------
def generate_architecture():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="480" viewBox="0 0 720 480">
  <defs>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e2a4a"/>
      <stop offset="100%" stop-color="#162040"/>
    </linearGradient>
    <linearGradient id="timerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3a2040"/>
      <stop offset="100%" stop-color="#2a1530"/>
    </linearGradient>
    <linearGradient id="browserGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a3040"/>
      <stop offset="100%" stop-color="#102030"/>
    </linearGradient>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#e94560"/>
    </marker>
    <marker id="arrowhead2" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#5ce1e6"/>
    </marker>
  </defs>

  <rect width="720" height="480" rx="12" fill="#0d1117"/>

  <!-- Title -->
  <text x="360" y="34" font-family="Segoe UI, sans-serif" font-size="16" font-weight="700" fill="#e0e0e0" text-anchor="middle">
    BOSS Auto Browse — Core Architecture
  </text>

  <!-- GUI Layer -->
  <rect x="40" y="60" width="640" height="100" rx="10" fill="url(#boxGrad)" stroke="#e94560" stroke-width="1.5" opacity="0.95"/>
  <text x="360" y="84" font-family="Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#e94560" text-anchor="middle">GUI Layer (System.Windows.Forms)</text>
  <text x="150" y="115" font-family="Segoe UI, sans-serif" font-size="11" fill="#c0c0d0" text-anchor="middle">Interval Input</text>
  <text x="150" y="138" font-family="Segoe UI, sans-serif" font-size="10" fill="#808090" text-anchor="middle">default: 2 sec</text>
  <text x="290" y="115" font-family="Segoe UI, sans-serif" font-size="11" fill="#c0c0d0" text-anchor="middle">Max Count Input</text>
  <text x="290" y="138" font-family="Segoe UI, sans-serif" font-size="10" fill="#808090" text-anchor="middle">0 = unlimited</text>
  <text x="430" y="115" font-family="Segoe UI, sans-serif" font-size="11" fill="#c0c0d0" text-anchor="middle">Status / Counter</text>
  <text x="430" y="138" font-family="Segoe UI, sans-serif" font-size="10" fill="#808090" text-anchor="middle">Sent: N</text>
  <text x="570" y="115" font-family="Segoe UI, sans-serif" font-size="11" fill="#c0c0d0" text-anchor="middle">Log List (max 200)</text>
  <text x="570" y="138" font-family="Segoe UI, sans-serif" font-size="10" fill="#808090" text-anchor="middle">newest on top</text>

  <!-- Start button -->
  <rect x="560" y="180" width="100" height="36" rx="8" fill="#2ea44f" opacity="0.9"/>
  <text x="610" y="203" font-family="Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Start / Pause</text>
  <line x1="560" y1="198" x2="530" y2="110" stroke="#2ea44f" stroke-width="2" stroke-dasharray="4,3" opacity="0.5"/>

  <!-- Timer Core -->
  <rect x="240" y="180" width="240" height="80" rx="10" fill="url(#timerGrad)" stroke="#e94560" stroke-width="1.5" opacity="0.95"/>
  <text x="360" y="208" font-family="Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#e94560" text-anchor="middle">Timer.Tick (core loop)</text>
  <text x="360" y="232" font-family="Segoe UI, sans-serif" font-size="10" fill="#a0a0c0" text-anchor="middle">every interval → find browser → activate → send key</text>
  <text x="360" y="250" font-family="Segoe UI, sans-serif" font-size="10" fill="#707080" text-anchor="middle">6 browsers · 4 keywords</text>

  <!-- Arrow: Start to Timer -->
  <line x1="560" y1="218" x2="480" y2="218" stroke="#e94560" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Win32 API Layer -->
  <rect x="40" y="190" width="170" height="60" rx="8" fill="url(#boxGrad)" stroke="#5ce1e6" stroke-width="1.5" opacity="0.9"/>
  <text x="125" y="212" font-family="Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#5ce1e6" text-anchor="middle">Win32 API (user32.dll)</text>
  <text x="125" y="230" font-family="Segoe UI, sans-serif" font-size="9" fill="#9090a0" text-anchor="middle">GetForegroundWindow</text>
  <text x="125" y="242" font-family="Segoe UI, sans-serif" font-size="9" fill="#9090a0" text-anchor="middle">ShowWindow · GetWindowThreadProcessId</text>

  <!-- Arrow: Timer to Win32 -->
  <line x1="240" y1="220" x2="210" y2="220" stroke="#5ce1e6" stroke-width="1.5" stroke-dasharray="3,2" marker-end="url(#arrowhead2)"/>

  <!-- Browser Detection -->
  <rect x="40" y="290" width="640" height="70" rx="10" fill="url(#browserGrad)" stroke="#5ce1e6" stroke-width="1.5" opacity="0.9"/>
  <text x="360" y="314" font-family="Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#5ce1e6" text-anchor="middle">Browser Detection &amp; Activation</text>
  <text x="100" y="338" font-family="Segoe UI, sans-serif" font-size="10" fill="#a0b0c0" text-anchor="middle">Get-TargetBrowserWindow</text>
  <text x="290" y="338" font-family="Segoe UI, sans-serif" font-size="10" fill="#a0b0c0" text-anchor="middle">Activate-BrowserWindow</text>
  <text x="480" y="338" font-family="Segoe UI, sans-serif" font-size="10" fill="#a0b0c0" text-anchor="middle">Confirm-KeySent</text>
  <text x="630" y="338" font-family="Segoe UI, sans-serif" font-size="10" fill="#a0b0c0" text-anchor="middle">Get-ForegroundProcessName</text>

  <!-- Arrow: Timer to Browser Detection -->
  <line x1="360" y1="260" x2="360" y2="290" stroke="#e94560" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Key Send -->
  <rect x="180" y="390" width="360" height="60" rx="10" fill="url(#boxGrad)" stroke="#e94560" stroke-width="1.5" opacity="0.95"/>
  <text x="360" y="414" font-family="Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#e94560" text-anchor="middle">SendKeys::SendWait("{RIGHT}")</text>
  <text x="360" y="434" font-family="Segoe UI, sans-serif" font-size="10" fill="#9090a0" text-anchor="middle">Simulates right arrow key press → switches candidate card</text>

  <!-- Arrow: Browser Detection to Key Send -->
  <line x1="360" y1="360" x2="360" y2="390" stroke="#e94560" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Browser icon (target) -->
  <rect x="580" y="395" width="80" height="50" rx="6" fill="#013755" opacity="0.6" stroke="#5ce1e6" stroke-width="1"/>
  <text x="620" y="415" font-family="Segoe UI, sans-serif" font-size="10" fill="#5ce1e6" text-anchor="middle">Browser</text>
  <text x="620" y="432" font-family="Segoe UI, sans-serif" font-size="9" fill="#7080a0" text-anchor="middle">BOSS / zhipin</text>
  <line x1="540" y1="420" x2="580" y2="420" stroke="#e94560" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Add-Log (side feedback) -->
  <rect x="40" y="390" width="110" height="50" rx="6" fill="#1a1a2e" opacity="0.7" stroke="#6c5ce7" stroke-width="1"/>
  <text x="95" y="410" font-family="Segoe UI, sans-serif" font-size="10" fill="#6c5ce7" text-anchor="middle">Add-Log</text>
  <text x="95" y="427" font-family="Segoe UI, sans-serif" font-size="9" fill="#606080" text-anchor="middle">feedback to GUI</text>
  <line x1="180" y1="420" x2="150" y2="415" stroke="#6c5ce7" stroke-width="1" stroke-dasharray="3,2" opacity="0.5"/>
</svg>"""

    path = os.path.join(DOCS_DIR, "architecture.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {path}")


# ---------------------------------------------------------------------------
# 3. GUI Preview SVG — 界面示意图
# ---------------------------------------------------------------------------
def generate_gui_preview():
    # All coordinates from the actual source code
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="520" viewBox="0 0 500 520">
  <defs>
    <linearGradient id="winBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f0f0f0"/>
      <stop offset="100%" stop-color="#e0e0e0"/>
    </linearGradient>
    <linearGradient id="btnStart" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2ea44f"/>
      <stop offset="100%" stop-color="#27a045"/>
    </linearGradient>
    <linearGradient id="btnStop" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#d0d0d0"/>
      <stop offset="100%" stop-color="#c0c0c0"/>
    </linearGradient>
    <linearGradient id="btnClose" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#e55"/>
      <stop offset="100%" stop-color="#d44"/>
    </linearGradient>
    <linearGradient id="logBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f5f5f5"/>
    </linearGradient>
  </defs>

  <!-- Window background (470x480 actual, offset by 15px padding) -->
  <rect x="15" y="15" width="470" height="480" rx="6" fill="url(#winBg)" stroke="#999" stroke-width="1.5"/>

  <!-- Title bar -->
  <rect x="15" y="15" width="470" height="28" rx="6" fill="#1a1a2e"/>
  <rect x="15" y="35" width="470" height="8" fill="#1a1a2e"/>
  <text x="30" y="34" font-family="Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#e0e0e0">BOSS Auto Browse</text>
  <!-- Window controls -->
  <circle cx="455" cy="29" r="5" fill="#ff5f57"/>
  <circle cx="438" cy="29" r="5" fill="#ffbd2e"/>
  <circle cx="421" cy="29" r="5" fill="#28c840"/>

  <!-- Interval label + input (lblInterval at 15,15; txtInterval at 130,12, size 55x24) -->
  <!-- Offset everything by +15 x, +43 y (title bar) -->
  <text x="30" y="63" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">Interval (sec):</text>
  <rect x="145" y="55" width="55" height="24" rx="3" fill="#fff" stroke="#bbb" stroke-width="1"/>
  <text x="152" y="71" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">2</text>

  <!-- Max count label + input -->
  <text x="215" y="63" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">Max count (0 = unlimited):</text>
  <rect x="375" y="55" width="75" height="24" rx="3" fill="#fff" stroke="#bbb" stroke-width="1"/>
  <text x="382" y="71" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">0</text>

  <!-- Status label -->
  <text x="30" y="98" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">Status: Stopped</text>
  <!-- Count label -->
  <text x="265" y="98" font-family="Segoe UI, sans-serif" font-size="11" fill="#333">Sent: 0</text>

  <!-- Log list background (at 15,85 size 425x290 → offset) -->
  <rect x="30" y="110" width="425" height="290" rx="4" fill="url(#logBg)" stroke="#ccc" stroke-width="1"/>

  <!-- Log entries (newest on top) -->
  <text x="40" y="128" font-family="Consolas, monospace" font-size="10" fill="#888">Tip: open one candidate detail page first so Right arrow flips candidates.</text>
  <text x="40" y="143" font-family="Consolas, monospace" font-size="10" fill="#888">Ready. Open BOSS/zhipin in a browser, then press Start.</text>
  <text x="40" y="158" font-family="Consolas, monospace" font-size="10" fill="#999">─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─</text>
  <text x="40" y="173" font-family="Consolas, monospace" font-size="10" fill="#2ea44f">[start] Started, interval=2 sec, max=/unlimited</text>
  <text x="40" y="188" font-family="Consolas, monospace" font-size="10" fill="#333">[1] chrome: BOSS直聘 - 候选人列表</text>
  <text x="40" y="203" font-family="Consolas, monospace" font-size="10" fill="#333">[2] chrome: BOSS直聘 - 候选人列表</text>
  <text x="40" y="218" font-family="Consolas, monospace" font-size="10" fill="#333">[3] chrome: BOSS直聘 - 候选人列表</text>
  <text x="40" y="233" font-family="Consolas, monospace" font-size="10" fill="#666">...</text>

  <!-- Buttons (at y=390, size 135x40 each, offset by +15x, +43y) -->
  <!-- Start button -->
  <rect x="30" y="405" width="135" height="40" rx="5" fill="url(#btnStart)"/>
  <text x="97" y="430" font-family="Segoe UI, sans-serif" font-size="13" font-weight="600" fill="#fff" text-anchor="middle">Start</text>

  <!-- Stop button (disabled) -->
  <rect x="175" y="405" width="135" height="40" rx="5" fill="url(#btnStop)" opacity="0.5"/>
  <text x="242" y="430" font-family="Segoe UI, sans-serif" font-size="13" font-weight="600" fill="#888" text-anchor="middle">Stop</text>

  <!-- Close button -->
  <rect x="320" y="405" width="135" height="40" rx="5" fill="url(#btnClose)"/>
  <text x="387" y="430" font-family="Segoe UI, sans-serif" font-size="13" font-weight="600" fill="#fff" text-anchor="middle">Close</text>

  <!-- Annotation -->
  <text x="250" y="475" font-family="Segoe UI, sans-serif" font-size="9" fill="#aaa" text-anchor="middle">GUI 界面示意图 — 实际运行效果以本地程序为准</text>
</svg>"""

    path = os.path.join(DOCS_DIR, "gui_preview.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    os.makedirs(DOCS_DIR, exist_ok=True)
    generate_banner()
    generate_architecture()
    generate_gui_preview()
    print("\nAll SVG assets generated successfully.")
