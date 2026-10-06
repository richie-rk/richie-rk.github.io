#!/usr/bin/env python3
"""Measure every page against the design refactor's gates.

Serves the repo over http (fonts and view transitions need http, not file://),
loads each page in headless Chromium at 390x844 and 1440x900 in the dark and
light colour schemes, and prints the verification table as Markdown.

    python tools/measure.py                          # table and gates
    python tools/measure.py --details                # also long blocks, door tops, TOC height
    python tools/measure.py --out docs/measure-baseline.md

Needs Playwright for Python: pip install playwright, then
python -m playwright install chromium.

How each column is measured:
- Words in main: main.innerText split on whitespace, less the labels of visible
  diagrams, so it counts prose only.
- Height: document.documentElement.scrollHeight.
- Blocks over 6 lines: visible p and li in main, lines = round(height / line-height).
  An li that wraps block children (a nested list or paragraphs) is skipped, so
  its children are counted instead of the whole item.
- Muted share: characters of visible text in main p, li and dd set in
  --text-muted, over all such characters. Visually hidden text and anything the
  browser skips rendering (a closed <details>) are left out. Links are accent
  text, not muted; --details also reports the share that is not --text at all.
- First-screen elements: whether each key element sits fully inside the first
  viewport at scroll 0.
- Horizontal overflow: the document, and every visible .figure__scroll, whose
  scrollWidth exceeds its clientWidth.
"""

import argparse
import functools
import http.server
import json
import subprocess
import sys
import threading
from datetime import date
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
VIEWPORTS = [(390, 844), (1440, 900)]
SCHEMES = ["dark", "light"]
PHONE = "390x844"

DEEP_DIVE_FIRST_SCREEN = {
    "name": ".case-study__name",
    "claim": ".case-study__claim",
    "summary": ".case-study__summary",
    "at-a-glance": ".case-study__overview",
}

# Page name, file, and the elements that must sit in the first screen (the
# header is always checked first).
PAGES = [
    ("index", "index.html", {
        "role": ".hero__role",
        "claim": ".hero__claim",
        "proof": ".hero__proof",
        "buttons": ".hero .button-row",
        "email": ".hero .email-copy",
        "first door name": ".project__name",
    }),
    ("max-ai", "max-ai.html", DEEP_DIVE_FIRST_SCREEN),
    ("final-docs", "final-docs.html", DEEP_DIVE_FIRST_SCREEN),
    ("encompass-automation", "encompass-automation.html", DEEP_DIVE_FIRST_SCREEN),
    ("cv", "cv.html", {"name": "h1", "role": ".cv__tagline", "contact": ".cv__contact"}),
    ("letter", "letter.html", {"heading": "h1"}),
    ("404", "404.html", {"heading": "h1", "button": ".button"}),
]

# Words in main and height at 390x844, measured at commit c10c193 before the
# refactor. "Unchanged" targets allow 10% either way.
BASELINE = {
    "index": {"words": 973, "height": 8147},
    "max-ai": {"words": 1387, "height": 8721},
    "final-docs": {"words": 1116, "height": 8169},
    "cv": {"words": 669, "height": 5711},
    "letter": {"words": 180, "height": 3193},
    "404": {"words": 29, "height": 844},
}
LEEWAY = 0.10

# The brief's targets. words/height: a maximum, or "baseline" for unchanged.
GATES = {
    "index": {"words": 500, "height": 4500, "muted": 0.20},
    "max-ai": {"words": "baseline", "height": 7000, "muted": 0.20},
    "final-docs": {"words": "baseline", "height": 7000, "muted": 0.20},
    "encompass-automation": {"height": 7000, "muted": 0.20},
    "cv": {"words": "baseline", "height": 5500},
    "letter": {"words": "baseline", "height": "baseline"},
    "404": {"words": "baseline", "height": "baseline"},
}

MEASURE_JS = """
(firstScreen) => {
  const main = document.querySelector('main');
  const doc = document.documentElement;
  // checkVisibility() also catches content the browser skips rendering, such as
  // the inside of a closed <details>, which still reports a layout box.
  const isHidden = (el) => {
    if (el.closest('.visually-hidden')) return true;
    if (!el.checkVisibility({ visibilityProperty: true })) return true;
    const r = el.getBoundingClientRect();
    return r.width === 0 && r.height === 0;
  };

  // Diagram labels are not prose, so the text of visible SVGs is taken back out.
  const count = (text) => text.trim().split(/\\s+/).filter(Boolean).length;
  const words = count(main.innerText) - [...main.querySelectorAll('svg')]
    .filter((svg) => !isHidden(svg))
    .reduce((n, svg) => n + count(svg.textContent), 0);

  const BLOCK_CHILD = 'p, ul, ol, dl, div, figure, pre, blockquote, table, h1, h2, h3, h4';
  const blocks = [];
  for (const el of main.querySelectorAll('p, li')) {
    if (isHidden(el)) continue;
    if (el.tagName === 'LI' && el.querySelector(BLOCK_CHILD)) continue;
    const cs = getComputedStyle(el);
    let lh = parseFloat(cs.lineHeight);
    if (Number.isNaN(lh)) lh = parseFloat(cs.fontSize) * 1.2;
    const box = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom)
      + parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth);
    const lines = Math.round((el.getBoundingClientRect().height - box) / lh);
    blocks.push({ lines, text: el.innerText.trim().replace(/\\s+/g, ' ').slice(0, 90) });
  }

  const colourOf = (token) => {
    const probe = document.createElement('span');
    probe.style.color = `var(${token})`;
    main.append(probe);
    const colour = getComputedStyle(probe).color;
    probe.remove();
    return colour;
  };
  const textColour = colourOf('--text'), mutedColour = colourOf('--text-muted');
  let chars = 0, muted = 0, notText = 0;
  const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    const el = node.parentElement;
    if (!el || !el.closest('p, li, dd') || isHidden(el)) continue;
    const n = node.data.replace(/\\s+/g, '').length;
    if (!n) continue;
    chars += n;
    const colour = getComputedStyle(el).color;
    if (colour === mutedColour) muted += n;
    if (colour !== textColour) notText += n;
  }

  const firstScreenResult = [];
  for (const [label, selector] of [['header', '.site-header'], ...Object.entries(firstScreen)]) {
    const el = [...document.querySelectorAll(selector)].find((e) => !isHidden(e));
    if (!el) { firstScreenResult.push({ label, status: 'missing' }); continue; }
    const r = el.getBoundingClientRect();
    const top = Math.round(r.top + scrollY), bottom = Math.round(r.bottom + scrollY);
    const status = bottom <= innerHeight ? 'in' : top < innerHeight ? 'partial' : 'below';
    firstScreenResult.push({ label, status, top, bottom });
  }

  const overflow = [];
  if (doc.scrollWidth > doc.clientWidth) overflow.push(`page +${doc.scrollWidth - doc.clientWidth}px`);
  [...document.querySelectorAll('.figure__scroll')].forEach((el, i) => {
    if (isHidden(el)) return;
    if (el.scrollWidth > el.clientWidth + 1) overflow.push(`figure ${i + 1} +${el.scrollWidth - el.clientWidth}px`);
  });

  const toc = document.querySelector('.toc');
  return {
    words,
    height: doc.scrollHeight,
    blocks,
    muted: chars ? muted / chars : 0,
    notText: chars ? notText / chars : 0,
    firstScreen: firstScreenResult,
    overflow,
    doorTops: [...document.querySelectorAll('.project__name')]
      .filter((e) => !isHidden(e))
      .map((e) => ({ name: e.innerText.replace(/\\s+/g, ' ').trim(), top: Math.round(e.getBoundingClientRect().top + scrollY) })),
    tocHeight: toc && !isHidden(toc) ? Math.round(toc.getBoundingClientRect().height) : null,
  };
}
"""


def serve(root):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(Quiet, directory=str(root))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def git_label():
    def run(*args):
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()

    # Only the site's own files count; tools/ and docs/ don't change what is measured.
    sha = run("rev-parse", "--short", "HEAD") or "unknown"
    dirty = run("status", "--porcelain", "--", ".", ":!tools", ":!docs")
    return sha + (" plus uncommitted changes" if dirty else "")


def measure(pages):
    server = serve(ROOT)
    base = f"http://127.0.0.1:{server.server_address[1]}/"
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width, height in VIEWPORTS:
            for scheme in SCHEMES:
                context = browser.new_context(viewport={"width": width, "height": height}, color_scheme=scheme)
                page = context.new_page()
                for name, file, first_screen in pages:
                    page.goto(base + file, wait_until="load")
                    page.evaluate("document.fonts.ready.then(() => new Promise(requestAnimationFrame))")
                    data = page.evaluate(MEASURE_JS, first_screen)
                    results.append({"page": name, "viewport": f"{width}x{height}", "scheme": scheme, **data})
                context.close()
        version = browser.version
        browser.close()
    server.shutdown()
    return results, version


def fmt_int(n):
    return f"{n:,}"


def long_blocks(blocks):
    return [b for b in blocks if b["lines"] > 6]


def blocks_cell(blocks):
    over = long_blocks(blocks)
    longest = max((b["lines"] for b in blocks), default=0)
    return f"{len(over)} of {len(blocks)} (longest {longest})"


def first_screen_cell(items):
    parts = []
    for item in items:
        if item["status"] == "in":
            parts.append(item["label"])
        elif item["status"] == "missing":
            parts.append(f"{item['label']} missing")
        elif item["status"] == "partial":
            parts.append(f"{item['label']} cut off at {fmt_int(item['top'])} px")
        else:
            parts.append(f"{item['label']} below, at {fmt_int(item['top'])} px")
    return ", ".join(parts)


def judge(name, rows):
    """Return gate cells for one page: words, height, blocks, muted, first screen, overflow, result."""
    gate = GATES.get(name, {})
    base = BASELINE.get(name)
    phone = [r for r in rows if r["viewport"] == PHONE]
    cells, failed = [], False

    def verdict(ok, text):
        nonlocal failed
        failed |= not ok
        return ("pass " if ok else "FAIL ") + text

    def limit_cell(key, value, unit=""):
        target = gate.get(key)
        if target is None:
            return f"n/a {fmt_int(value)}{unit}"
        if target == "baseline":
            if not base:
                return f"n/a {fmt_int(value)}{unit} (no baseline)"
            ref = base[key]
            return verdict(abs(value - ref) <= ref * LEEWAY, f"{fmt_int(value)}{unit} (baseline {fmt_int(ref)} +/- 10%)")
        return verdict(value <= target, f"{fmt_int(value)}{unit} (max {fmt_int(target)})")

    cells.append(limit_cell("words", max(r["words"] for r in phone)))
    cells.append(limit_cell("height", max(r["height"] for r in phone), " px"))

    over = max(len(long_blocks(r["blocks"])) for r in phone)
    cells.append(verdict(over == 0, f"{over}"))

    worst_muted = max(r["muted"] for r in rows)
    if "muted" in gate:
        cells.append(verdict(worst_muted <= gate["muted"], f"{worst_muted:.2f} (max {gate['muted']:.2f})"))
    else:
        cells.append(f"n/a {worst_muted:.2f}")

    misses = sorted({i["label"] for r in phone for i in r["firstScreen"] if i["status"] != "in"})
    cells.append(verdict(not misses, "all in" if not misses else "not in: " + ", ".join(misses)))

    spills = sorted({o for r in rows for o in r["overflow"]})
    cells.append(verdict(not spills, "none" if not spills else ", ".join(spills)))

    cells.append("FAIL" if failed else "pass")
    return cells


def report(results, version, details):
    lines = [
        "# Measurements",
        "",
        f"Commit {git_label()}, measured {date.today().isoformat()} by `python tools/measure.py` "
        f"in headless Chromium {version}.",
        "",
        "| Page | Viewport | Scheme | Words in main | Height (px) | Blocks over 6 lines | Muted share "
        "| First-screen elements | Horizontal overflow |",
        "| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |",
    ]
    order = [name for name, _, _ in PAGES]
    results = sorted(results, key=lambda r: (order.index(r["page"]), r["viewport"] != PHONE, r["scheme"]))
    for r in results:
        lines.append(
            f"| {r['page']} | {r['viewport']} | {r['scheme']} | {fmt_int(r['words'])} | {fmt_int(r['height'])} "
            f"| {blocks_cell(r['blocks'])} | {r['muted']:.2f} | {first_screen_cell(r['firstScreen'])} "
            f"| {', '.join(r['overflow']) or 'none'} |"
        )

    lines += [
        "",
        "## Gates",
        "",
        f"Targets from the brief. Words, height, long blocks and the first screen are judged at {PHONE}; "
        "muted share and overflow across all four runs. \"Baseline\" targets allow 10% either way.",
        "",
        "| Page | Words in main | Height at 390 | Blocks over 6 lines | Muted share | First screen at 390 "
        "| Horizontal overflow | Result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for name in order:
        rows = [r for r in results if r["page"] == name]
        if rows:
            lines.append(f"| {name} | " + " | ".join(judge(name, rows)) + " |")

    if details:
        lines += ["", f"## Details at {PHONE}, dark", ""]
        for name in order:
            row = next((r for r in results if r["page"] == name and r["viewport"] == PHONE and r["scheme"] == "dark"), None)
            if not row:
                continue
            lines.append(f"### {name}")
            lines.append("")
            if row["doorTops"]:
                tops = ", ".join(f"{d['name']} at {fmt_int(d['top'])} px" for d in row["doorTops"])
                lines.append(f"- Project names: {tops}")
            if row["tocHeight"] is not None:
                lines.append(f"- TOC height: {row['tocHeight']} px")
            lines.append(f"- Share of body text not in --text (muted plus links): {row['notText']:.2f}")
            for block in long_blocks(row["blocks"]):
                lines.append(f"- {block['lines']} lines: {block['text']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--details", action="store_true", help="list long blocks, project-name tops and TOC height")
    parser.add_argument("--out", type=Path, help="also write the Markdown report to this file")
    parser.add_argument("--json", type=Path, help="write the raw measurements as JSON")
    parser.add_argument("--pages", help="comma-separated page names to measure (default: all)")
    args = parser.parse_args()

    wanted = set(args.pages.split(",")) if args.pages else None
    pages = [p for p in PAGES if (ROOT / p[1]).exists() and (wanted is None or p[0] in wanted)]
    results, version = measure(pages)

    text = report(results, version, args.details)
    sys.stdout.reconfigure(encoding="utf-8")
    print(text, end="")
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    if args.json:
        args.json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
