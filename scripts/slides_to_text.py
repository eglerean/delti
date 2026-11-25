#!/usr/bin/env python3
"""Make a text-only handout from a Slidev deck.

Reads slides.md and writes slides_text.md: one section per slide with its
headings, text, lists, tables and links. Images, SVG graphics, styles,
speaker notes and layout markup are left out.

Usage: python3 scripts/slides_to_text.py [input.md] [output.md]
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def split_slides(text):
    """Return a list of (frontmatter, body) pairs, one per slide.

    A slide starts at a `---` line outside code fences. When the lines up to
    the next `---` look like YAML, they are that slide's frontmatter.
    """
    lines = text.split("\n")
    seps, fence = [], False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            fence = not fence
        if not fence and line.rstrip() == "---":
            seps.append(i)

    def is_yaml(a, b):
        block = lines[a + 1:b]
        return (
            bool(block)
            and all(re.match(r"^(\s+\S|[\w-]+:|\s*$|#)", x) for x in block)
            and any(re.match(r"^[\w-]+:", x) for x in block)
        )

    slides, k = [], 0
    # Text before the first separator (if any) is ignored: Slidev decks start with `---`
    while k < len(seps):
        start = seps[k]
        if k + 1 < len(seps) and is_yaml(start, seps[k + 1]):
            front = "\n".join(lines[start + 1:seps[k + 1]])
            body_start, k = seps[k + 1] + 1, k + 2
        else:
            front, body_start, k = "", start + 1, k + 1
        body_end = seps[k] if k < len(seps) else len(lines)
        slides.append((front, "\n".join(lines[body_start:body_end])))
    return slides


def frontmatter_value(front, key):
    m = re.search(rf"^{key}:\s*(.+)$", front, re.M)
    return m.group(1).strip().strip("\"'") if m else ""


def clean_body(body):
    # Drop speaker notes, styles, graphics and images entirely
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"<style[^>]*>.*?</style>", "", body, flags=re.S | re.I)
    body = re.sub(r"<svg[^>]*>.*?</svg>", "", body, flags=re.S | re.I)
    body = re.sub(r"<img[^>]*>", "", body, flags=re.I)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    # Slidev slot markers (::left::) and Vue/icon components (<CcBy />, <carbon-logo-github ... />)
    body = re.sub(r"^::[\w-]+::\s*$", "", body, flags=re.M)
    body = re.sub(r"<([A-Z][\w-]*|[a-z]+-[\w-]+)\b[^>]*/>", "", body)
    body = re.sub(r"<([a-z]+-[\w-]+)\b[^>]*>.*?</\1>", "", body, flags=re.S)

    out = []
    for line in body.split("\n"):
        had_html = bool(re.search(r"</?[a-zA-Z][^>]*>", line))
        line = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", line, flags=re.S)
        line = re.sub(r"\[\s*\]\([^)]*\)", "", line)
        line = re.sub(r"</?(strong|b)>", "**", line)
        line = re.sub(r"</?(em|i)>", "*", line)
        line = re.sub(r"<br\s*/?>", "\n", line)
        line = re.sub(r"<li[^>]*>", "\n- ", line)
        line = re.sub(r"</?(p|div|ol|ul|li)\b[^>]*>", "\n", line)
        line = re.sub(r"</span>\s*(?=<span)", " · ", line)
        line = re.sub(r"</?[a-zA-Z][^>]*>", "", line)
        line = html.unescape(line)
        if had_html:
            # Text that came out of HTML blocks: drop the HTML indentation
            line = "\n".join(part.strip() for part in line.split("\n"))
        out.append(line.rstrip())
    text = "\n".join(out)

    # Headings: the eyebrow (######) becomes an italic line; others move down one level
    def heading(m):
        level, title = len(m.group(1)), m.group(2).strip()
        if level == 6:
            return f"*{title}*"
        return "#" * min(level + 1, 6) + " " + title

    text = re.sub(r"^(#{1,6})\s+(.*)$", heading, text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides.md"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "slides_text.md"
    slides = split_slides(src.read_text(encoding="utf-8"))

    deck_title = frontmatter_value(slides[0][0], "title") if slides else ""
    author = frontmatter_value(slides[0][0], "author") if slides else ""
    parts = [f"# {deck_title}" if deck_title else "# Slides"]
    if author:
        parts.append(f"{author}. Text-only handout generated from `{src.name}`.")

    for n, (front, body) in enumerate(slides, start=1):
        text = clean_body(body)
        if not text:
            continue
        parts.append(f"---\n\n<sub>Slide {n}</sub>\n\n{text}")

    dst.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {dst} ({len(slides)} slides)")


if __name__ == "__main__":
    main()
