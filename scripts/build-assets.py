#!/usr/bin/env python3
"""Generate the qDiff site's artwork from lightweight SVG sources.

Run from anywhere:  python3 scripts/build-assets.py

Sources:
  - the app icon is copied from the qDiff project (icons/qdiff.png)
  - every other image is drawn here, so the site has no stale product shots
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "docs" / "public"
ICONS = PUBLIC / "icons"
SHOTS = PUBLIC / "screenshots"
APP_ICON = Path("/Users/terry/nuecms-workspace/qdiff/icons/qdiff.png")

BLUE = "#3b82f6"
BLUE_DARK = "#2f6fe4"
GREEN = "#34c88b"
GREEN_DARK = "#20a877"
INK = "#1e293b"
MUTED = "#94a3b8"
LINE = "#e8edf5"
SOFT = "#f7f9fd"

FONT = "Helvetica,Arial,sans-serif"


# ── tiny SVG helpers ────────────────────────────────────────────────
def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def label(x, y, s, size=13, fill="#64748b", weight="600", anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
    )


def circle(cx, cy, r, fill, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {extra}/>'


def path(d, stroke="none", width=1, extra=""):
    return f'<path d="{d}" fill="{stroke}" {extra}/>' if stroke.startswith("#") and "stroke" not in extra else (
        f'<path d="{d}" stroke="{stroke}" stroke-width="{width}" fill="none" {extra}/>'
    )


def defs():
    return f"""<defs>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#1e3a5f" flood-opacity="0.13"/>
  </filter>
  <filter id="cardShadow" x="-30%" y="-30%" width="160%" height="180%">
    <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#1e3a5f" flood-opacity="0.14"/>
  </filter>
  <linearGradient id="blue" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#5aa2ff"/><stop offset="1" stop-color="{BLUE_DARK}"/>
  </linearGradient>
  <linearGradient id="green" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#69dfae"/><stop offset="1" stop-color="{GREEN_DARK}"/>
  </linearGradient>
  <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#fbfcff"/>
  </linearGradient>
  <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#bfe3ff"/><stop offset="1" stop-color="#e7f7ff"/>
  </linearGradient>
  <radialGradient id="glowBlue">
    <stop offset="0" stop-color="#dbeaff" stop-opacity="0.95"/>
    <stop offset="1" stop-color="#dbeaff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowGreen">
    <stop offset="0" stop-color="#dcf7ea" stop-opacity="0.95"/>
    <stop offset="1" stop-color="#dcf7ea" stop-opacity="0"/>
  </radialGradient>
</defs>"""


def window(x, y, w, h, tabs=True):
    """A macOS-like app window frame. Returns (svg parts, content origin)."""
    p = [rect(x, y, w, h, "url(#paper)", 20, 'filter="url(#shadow)" stroke="#e4eaf4" stroke-width="1"')]
    p.append(f'<path d="M{x} {y+20}a20 20 0 0 1 20 -20h{w-40}a20 20 0 0 1 20 20v32h-{w}z" fill="{SOFT}"/>')
    p.append(rect(x, y + 50, w, 1, "#e9eef6"))
    for i, c in enumerate(("#ff6059", "#ffbd2e", "#28c840")):
        p.append(circle(x + 28 + i * 22, y + 26, 6.5, c))
    if tabs:
        p.append(rect(x + w / 2 - 130, y + 16, 260, 20, "#e9eef5", 10))
        for i, cw in enumerate((26, 26, 26)):
            p.append(rect(x + w - 100 + i * 30, y + 19, cw, 14, "#e2e8f2", 5))
        p.append(rect(x + 24, y + 64, 104, 26, "#e9eef5", 8))
        p.append(label(x + 40, y + 81, "draft.txt", 12, "#64748b"))
        p.append(rect(x + 136, y + 64, 104, 26, BLUE, 8))
        p.append(label(x + 152, y + 81, "final.txt", 12, "#ffffff"))
        p.append(rect(x + 24, y + 102, w - 48, 1, "#eef2f8"))
    return p, (x + 24, y + 116)


def code_pane(p, x, y, w, rows, highlighted, side, row_h=32):
    """Two-column diff pane; `rows` is a list of text-line widths."""
    p.append(rect(x, y, w, len(rows) * row_h + 20, "#ffffff", 12, 'stroke="#edf1f7" stroke-width="1"'))
    for i, tw in enumerate(rows):
        ry = y + 10 + i * row_h
        if i in highlighted:
            bg = "#fff0ef" if side == "left" else "#eafaf2"
            p.append(rect(x + 6, ry, w - 12, row_h, bg, 6))
        p.append(label(x + 30, ry + row_h / 2 + 4, str(i + 1), 10, "#b7c2d2", "500", "end"))
        p.append(rect(x + 44, ry + 10, min(tw, w - 66), 8, "#dfe6f0", 4))
        if i in highlighted:
            strong = "#f7a7a0" if side == "left" else "#71d7a8"
            p.append(rect(x + 44 + min(tw, w - 66) * 0.45, ry + 8, 34, 12, strong, 4))
        elif i % 4 == 2:
            p.append(rect(x + 44 + min(tw, w - 66) + 8, ry + 10, 26, 8, "#eef2f8", 4))
    return p


def connectors(p, x, y, highlighted, row_h=32, span=28):
    for i in sorted(highlighted):
        cy = y + 10 + i * row_h + row_h / 2
        p.append(
            f'<path d="M{x} {cy} C{x+span*0.55} {cy-10}, {x+span*0.45} {cy+10}, {x+span} {cy}" '
            f'stroke="#a9c9f7" stroke-width="2" fill="none"/>'
        )
        p.append(circle(x, cy, 3, "#8fb8f2"))
        p.append(circle(x + span, cy, 3, "#8fb8f2"))
    return p


ROWS = [236, 178, 262, 205, 244, 168, 226, 194, 254, 182, 214, 158]
HL = (2, 5, 8)


def hero_svg(glows=True, drop_shadow=True):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 840" width="1200" height="840">', defs()]
    # soft background glows
    if glows:
        p.append(circle(140, 130, 290, "url(#glowBlue)"))
        p.append(circle(1090, 730, 300, "url(#glowGreen)"))
        p.append(circle(1060, 90, 190, "url(#glowBlue)"))

    frame, _ = window(70, 120, 1060, 590)
    p.extend(frame)
    left_x, right_x, pane_y = 96, 614, 244
    pane_w = 490
    code_pane(p, left_x, pane_y, pane_w, ROWS, HL, "left", 33)
    code_pane(p, right_x, pane_y, pane_w, ROWS, HL, "right", 33)
    connectors(p, left_x + pane_w + 2, pane_y, HL, 33, right_x - left_x - pane_w - 4)

    # bottom status bar
    p.append(rect(94, 660, 1012, 1, "#eef2f8"))
    p.append(rect(1000, 679, 34, 9, "#dfe6f0", 4))
    p.append(rect(1042, 679, 34, 9, "#dfe6f0", 4))

    # floating card — changes found
    p.append(rect(110, 700, 226, 96, "#ffffff", 18, 'filter="url(#cardShadow)" stroke="#e9eef5"'))
    p.append(circle(150, 748, 20, "url(#green)"))
    p.append(f'<path d="M141 748l6 6 12 -13" stroke="#ffffff" stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    p.append(label(184, 742, "3", 25, INK, "700"))
    p.append(rect(184, 754, 112, 8, "#dfe6f0", 4))
    p.append(rect(184, 768, 74, 8, "#eaeef5", 4))

    # floating card — two files
    p.append(rect(934, 44, 242, 96, "#ffffff", 18, 'filter="url(#cardShadow)" stroke="#e9eef5"'))
    p.append(circle(976, 92, 20, "url(#blue)"))
    p.append(rect(967, 84, 11, 16, "#ffffff", 2, 'opacity="0.95"'))
    p.append(rect(974, 88, 11, 16, "#ffffff", 2, 'opacity="0.75"'))
    p.append(rect(1010, 80, 132, 9, "#dfe6f0", 4))
    p.append(rect(1010, 98, 96, 9, "#eaeef5", 4))
    p.append(rect(1010, 113, 62, 7, "#c9e0ff", 4))
    p.append("</svg>")
    svg = "\n".join(p)
    if not drop_shadow:
        svg = svg.replace('filter="url(#shadow)" ', "").replace('filter="url(#cardShadow)" ', "")
    return svg


def files_svg():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540">', defs()]
    p.append(rect(0, 0, 960, 540, "#f5f8fe", 0))
    frame, _ = window(24, 34, 912, 472)
    p.extend(frame)
    rows = [200, 150, 218, 176, 205, 142, 190, 164, 216, 150, 182, 132]
    hl = (2, 5, 8)
    code_pane(p, 48, 166, 396, rows, hl, "left", 27)
    code_pane(p, 520, 166, 396, rows, hl, "right", 27)
    connectors(p, 448, 166, hl, 27, 68)
    p.append(rect(48, 484, 868, 1, "#eef2f8"))
    p.append(circle(70, 500, 6, GREEN))
    p.append(rect(84, 496, 76, 8, "#dfe6f0", 4))
    p.append("</svg>")
    return "\n".join(p)


def folders_svg():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540">', defs()]
    p.append(rect(0, 0, 960, 540, "#f5f8fe", 0))
    frame, _ = window(24, 34, 912, 472, tabs=False)
    p.extend(frame)
    # filter chips
    for i, (s, fill, fg) in enumerate((("All", BLUE, "#ffffff"), ("New", "#eef2f8", "#64748b"),
                                       ("Changed", "#eef2f8", "#64748b"), ("Missing", "#eef2f8", "#64748b"))):
        x = 160 + i * 108
        p.append(rect(x, 62, 96, 26, fill, 8))
        p.append(label(x + 48, 79, s, 12, fg, "600", "middle"))
    p.append(rect(48, 102, 868, 1, "#eef2f8"))
    labels = ["Documents", "Photos", "Notes.txt", "Cover.png", "Archive", "Readme.md", "Settings", "Exports"]
    widths = [116, 92, 104, 96, 88, 112, 84, 96]
    states = ["same", "new", "changed", "same", "missing", "changed", "same", "new"]
    colors = {"same": "#d8e0ec", "new": GREEN, "changed": "#f4a63c", "missing": "#f17b78"}
    for col, (x, w) in enumerate(((48, 424), (492, 424))):
        p.append(rect(x, 118, w, 366, "#ffffff", 12, 'stroke="#edf1f7"'))
        p.append(label(x + 20, 146, "Original" if col == 0 else "Backup", 12, MUTED))
        p.append(rect(x + 20, 156, w - 40, 1, "#eef2f8"))
        for i in range(8):
            ry = 170 + i * 38
            st = states[i] if col == 0 else ("same" if states[i] != "missing" else "empty")
            if st == "new":
                p.append(rect(x + 8, ry - 4, w - 16, 34, "#eafaf2", 6))
            elif st == "changed":
                p.append(rect(x + 8, ry - 4, w - 16, 34, "#fff7e9", 6))
            elif st == "missing":
                p.append(rect(x + 8, ry - 4, w - 16, 34, "#fff0ef", 6))
            indent = 20 + (16 if i in (2, 3, 5, 7) else 0)
            p.append(rect(x + indent, ry + 3, 18, 16, "#cbd9ee" if st != "new" else "#a9e4c7", 4))
            p.append(rect(x + indent + 27, ry + 6, widths[i], 9, "#dfe6f0", 4))
            p.append(circle(x + w - 30, ry + 11, 6, colors.get(st, "#eef2f8")))
    p.append("</svg>")
    return "\n".join(p)


def projects_svg():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540">', defs()]
    p.append(rect(0, 0, 960, 540, "#f5f8fe", 0))
    frame, _ = window(24, 34, 912, 472, tabs=False)
    p.extend(frame)
    p.append(rect(160, 62, 96, 26, BLUE, 8))
    p.append(label(208, 79, "Changes", 12, "#ffffff", "600", "middle"))
    p.append(label(282, 79, "History", 12, MUTED, "600"))
    p.append(rect(48, 102, 868, 1, "#eef2f8"))
    # left file list
    p.append(rect(48, 118, 336, 366, "#ffffff", 12, 'stroke="#edf1f7"'))
    names = ["HomeView.swift", "Settings.swift", "notes.md", "theme.css", "README.md", "AppIcon.png"]
    states = ["#f4a63c", GREEN, "#f4a63c", "#f4a63c", "#f17b78", "#d8e0ec"]
    for i, name in enumerate(names):
        ry = 134 + i * 56
        if i == 0:
            p.append(rect(56, ry, 320, 48, "#eaf2ff", 8))
        p.append(rect(68, ry + 15, 18, 18, "#d6e2f3", 5))
        p.append(label(98, ry + 29, name, 12, INK if i == 0 else "#64748b", "600"))
        p.append(circle(360, ry + 24, 6, states[i]))
    # right diff preview
    p.append(rect(400, 118, 516, 366, "#ffffff", 12, 'stroke="#edf1f7"'))
    p.append(label(420, 148, "HomeView.swift", 12, MUTED))
    p.append(rect(420, 160, 476, 1, "#eef2f8"))
    for i in range(9):
        ry = 174 + i * 33
        if i in (2, 5, 7):
            p.append(rect(412, ry - 2, 492, 30, "#eafaf2" if i != 5 else "#fff0ef", 6))
        p.append(label(432, ry + 18, str(i + 1), 10, "#b7c2d2", "500"))
        p.append(rect(452, ry + 9, [200, 168, 236, 190, 152, 224, 178, 206, 160][i], 8, "#dfe6f0", 4))
        if i in (2, 5, 7):
            p.append(rect(452 + 110, ry + 7, 40, 12, "#8ee0b8" if i != 5 else "#f7b0aa", 4))
    p.append("</svg>")
    return "\n".join(p)


def more_svg():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="960" height="540">', defs()]
    p.append(rect(0, 0, 960, 540, "#f5f8fe", 0))
    frame, _ = window(24, 34, 912, 472, tabs=False)
    p.extend(frame)
    p.append(label(48, 84, "Images", 14, INK, "700"))
    p.append(label(48, 104, "Side by side", 11, MUTED))
    for i, (x, overlay) in enumerate(((48, False), (492, True))):
        p.append(rect(x, 118, 424, 250, "#ffffff", 12, 'stroke="#edf1f7"'))
        p.append(rect(x + 12, 130, 400, 226, "url(#sky)", 8))
        p.append(circle(x + 320, 190, 30, "#ffd782"))
        p.append(f'<path d="M{x+12} 340 L{x+140} 220 L{x+230} 306 L{x+300} 250 L{x+412} 356 Z" fill="#8fc3e8"/>')
        p.append(f'<path d="M{x+12} 356 L{x+170} 268 L{x+270} 356 Z" fill="#5fa4d8"/>')
        if overlay:
            p.append(rect(x + 250, 235, 92, 72, "none", 8,
                          'stroke="#f17b78" stroke-width="3" stroke-dasharray="8 6"'))
        p.append(label(x + 212, 398, "Original" if i == 0 else "Updated", 12, MUTED, "600", "middle"))
    p.append(rect(48, 400, 868, 1, "#eef2f8"))
    p.append(label(48, 434, "Also works with archives and other file types", 13, INK, "600"))
    for i, s in enumerate(("ZIP", "TAR", "PNG", "HEX")):
        p.append(rect(48 + i * 106, 450, 92, 34, "#eef2f8", 8))
        p.append(label(94 + i * 106, 472, s, 12, "#64748b", "700", "middle"))
    p.append("</svg>")
    return "\n".join(p)


# ── feature icons (24×24 line icons, one shared file for light/dark) ─
ICON_PATHS = {
    "files": '<path d="M8 3h7l4 4v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/><path d="M15 3v5h4"/><path d="M4 8v11a2 2 0 0 0 2 2h9"/><path d="M9 13h6M9 16h4"/>',
    "folders": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 11h18"/><path d="M8 15h5"/>',
    "review": '<path d="M9 5h10M9 12h10M9 19h10"/><path d="M3 5l1.5 1.5L7 4"/><path d="M3 12l1.5 1.5L7 11"/><path d="M3 19l1.5 1.5L7 18"/>',
    "images": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9" r="1.8"/><path d="M3 17l5-5 4 4 3-3 6 6"/>',
    "navigate": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/>',
    "privacy": '<path d="M12 3l8 3v6c0 5-3.4 8.3-8 9-4.6-.7-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
}


def icon_svg(name):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" '
        'fill="none" stroke="#0f172a" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'
        + ICON_PATHS[name] + "</svg>"
    )


def preview_png(hero_png: Path, logo_png: Path, out: Path):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(247 - 12 * t), int(250 - 8 * t), 255))
    # Blur the alpha channel only — blurring an RGBA layer directly mixes
    # transparent black into the edges and leaves a grey halo.
    def glow_layer(box, strength, color):
        mask = Image.new("L", (W, H), 0)
        ImageDraw.Draw(mask).ellipse(box, fill=strength)
        mask = mask.filter(ImageFilter.GaussianBlur(90))
        layer = Image.new("RGBA", (W, H), color + (0,))
        layer.putalpha(mask)
        return layer

    img = Image.alpha_composite(
        img.convert("RGBA"), glow_layer((820, -220, 1420, 380), 210, (206, 230, 255))
    )
    img = Image.alpha_composite(
        img, glow_layer((960, 400, 1400, 840), 170, (214, 245, 230))
    ).convert("RGB")
    d = ImageDraw.Draw(img)

    # Product window, cropped on the right edge. The clean variant has no
    # glow or drop shadow, so a shadow drawn here stays a thin halo.
    shot = Image.open(hero_png).convert("RGBA")
    shot.thumbnail((690, 690), Image.LANCZOS)
    layer = Image.new("RGBA", (720, 520), (0, 0, 0, 0))
    layer.paste(shot, (8, 30), shot)
    img.paste(layer, (480, 55), layer)

    # left-hand copy
    logo = Image.open(logo_png).convert("RGBA")
    logo.thumbnail((92, 92), Image.LANCZOS)
    img.paste(logo, (72, 70), logo)
    bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    regular = "/System/Library/Fonts/Supplemental/Arial.ttf"
    f_title = ImageFont.truetype(bold, 76)
    f_sub = ImageFont.truetype(bold, 37)
    f_small = ImageFont.truetype(regular, 25)
    d.text((72, 190), "qDiff", font=f_title, fill="#16233a")
    d.text((74, 292), "See exactly", font=f_sub, fill="#1e293b")
    d.text((74, 338), "what changed", font=f_sub, fill="#1e293b")
    d.rounded_rectangle((74, 402, 154, 410), 4, fill=BLUE)
    d.text((74, 438), "Files   Folders   Projects", font=f_small, fill="#64748b")
    d.text((74, 486), "Compare side by side — all on your Mac.",
           font=ImageFont.truetype(regular, 20), fill="#8b98ab")
    img.save(out, "PNG", optimize=True)


def main():
    ICONS.mkdir(parents=True, exist_ok=True)
    SHOTS.mkdir(parents=True, exist_ok=True)

    # App icon → site logo (transparent, 256px) and a small favicon
    src = Image.open(APP_ICON).convert("RGBA")
    logo = src.resize((256, 256), Image.LANCZOS)
    logo.save(PUBLIC / "logo.png")
    src.resize((64, 64), Image.LANCZOS).save(PUBLIC / "favicon.png")

    for name, body in ICON_PATHS.items():
        svg = icon_svg(name)
        (ICONS / f"{name}.svg").write_text(svg, encoding="utf-8")
        (ICONS / f"{name}-dark.svg").write_text(svg, encoding="utf-8")

    svgs = {
        "hero": hero_svg(),
        "files": files_svg(),
        "folders": folders_svg(),
        "projects": projects_svg(),
        "more": more_svg(),
    }
    for name, svg in svgs.items():
        target = PUBLIC / ("hero-illustration.svg" if name == "hero" else SHOTS / f"{name}.svg")
        target.write_text(svg, encoding="utf-8")

    hero_png = PUBLIC / "hero-illustration.png"
    subprocess.run(
        ["rsvg-convert", "-w", "1800", "-h", "1260", str(PUBLIC / "hero-illustration.svg"), "-o", str(hero_png)],
        check=True,
    )
    clean_svg = Path("/tmp/qdiff-preview-window.svg")
    clean_png = Path("/tmp/qdiff-preview-window.png")
    clean_svg.write_text(hero_svg(glows=False, drop_shadow=False), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "1380", "-h", "966", str(clean_svg), "-o", str(clean_png)], check=True)
    preview_png(clean_png, PUBLIC / "logo.png", PUBLIC / "preview.png")
    print("Assets written to", PUBLIC)


if __name__ == "__main__":
    main()
