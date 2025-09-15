#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
from collections import defaultdict
from typing import List, Dict, Optional

MIL_TO_MM = 0.0254
NUM_RE = re.compile(r'\s*([+-]?\d+(?:\.\d+)?)(mm|mil)?\s*\Z')

ELEMENT_RE = re.compile(
    r'''
    ^(\s*)                                   # 1: leading whitespace (indent)
    Element\[
      "([^"]*)" \s+                          # 2: flags/lock
      "([^"]*)" \s+                          # 3: footprint
      "([^"]*)" \s+                          # 4: refdes
      "([^"]*)" \s+                          # 5: value
      ([^\s]+) \s+                           # 6: x
      ([^\s]+) \s+                           # 7: y
      ([^\s]+) \s+                           # 8: angle
      ([^\s]+) \s+                           # 9: mirror
      ([^\s]+) \s+                           # 10: int
      ([^\s]+) \s+                           # 11: int
      "([^"]*)"                              # 12: desc/comment
    \]
    (.*)$                                    # 13: trailing
    ''',
    re.VERBOSE
)

def to_mm(tok: str) -> float:
    m = NUM_RE.fullmatch(tok)
    if not m:
        raise ValueError(f"Bad length token: {tok!r}")
    val, unit = m.group(1), (m.group(2) or "mm").lower()
    x = float(val)
    return x if unit == "mm" else x * MIL_TO_MM

def fmt_mm(x: float) -> str:
    return f"{x:.4f}mm"

def page_from_refdes(refdes: str) -> Optional[int]:
    m = re.search(r'(\d+)', refdes)
    if not m:
        return None
    return int(m.group(1)) // 100

class Element:
    __slots__ = ("indent","flags","fp","refdes","value",
                 "x_tok","y_tok","ang","mir","i1","i2","desc","trail",
                 "line_index","orig_line")
    def __init__(self, m: re.Match, line_index: int, line: str):
        self.indent = m.group(1)
        self.flags  = m.group(2)
        self.fp     = m.group(3)
        self.refdes = m.group(4)
        self.value  = m.group(5)
        self.x_tok  = m.group(6)
        self.y_tok  = m.group(7)
        self.ang    = m.group(8)
        self.mir    = m.group(9)
        self.i1     = m.group(10)
        self.i2     = m.group(11)
        self.desc   = m.group(12)
        self.trail  = m.group(13)
        self.line_index = line_index
        self.orig_line  = line

    def rewrite_xy_mm(self, x_mm: float, y_mm: float) -> str:
        return (
            f'{self.indent}Element["{self.flags}" "{self.fp}" "{self.refdes}" '
            f'"{self.value}" {fmt_mm(x_mm)} {fmt_mm(y_mm)} {self.ang} {self.mir} '
            f'{self.i1} {self.i2} "{self.desc}"]{self.trail}'
        )

def parse_elements(lines: List[str]):
    elems: List[Element] = []
    for i, line in enumerate(lines):
        m = ELEMENT_RE.match(line)
        if m:
            elems.append(Element(m, i, line))
    return elems

def stack_pages(
    lines: List[str],
    anchor_x_mm: float,
    start_y_mm: float,
    page_spacing_mm: float,
    pages_include: Optional[set],
    pages_exclude: Optional[set],
):
    out = list(lines)
    elems = parse_elements(lines)

    # group by inferred page
    groups: Dict[int, List[Element]] = defaultdict(list)
    for e in elems:
        p = page_from_refdes(e.refdes)
        if p is not None:
            groups[p].append(e)

    # page ordering + filtering
    order = sorted(groups.keys())
    if pages_include is not None:
        order = [p for p in order if p in pages_include]
    if pages_exclude is not None:
        order = [p for p in order if p not in pages_exclude]

    # apply: every element in a page goes to the same anchor (stacked)
    for idx, p in enumerate(order):
        y_anchor = start_y_mm + idx * page_spacing_mm
        x_anchor = anchor_x_mm
        for e in groups[p]:
            out[e.line_index] = e.rewrite_xy_mm(x_anchor, y_anchor)

    return out, order, {p: len(groups[p]) for p in order}

def main():
    ap = argparse.ArgumentParser(
        description="Stack each inferred page’s parts at a single XY and place pages vertically with fixed spacing."
    )
    ap.add_argument("input", help=".pcb input")
    ap.add_argument("output", help=".pcb output")
    ap.add_argument("--anchor-x-mm", type=float, default=10.0, help="X anchor for all pages (mm). Default: 10.0")
    ap.add_argument("--start-y-mm", type=float, default=10.0, help="Top Y anchor of first page (mm). Default: 10.0")
    ap.add_argument("--page-spacing-mm", type=float, default=20.0, help="Vertical spacing between page anchors (mm). Default: 20.0")
    ap.add_argument("--pages", type=str, default=None, help="Comma-separated pages to include (e.g. '2,4,7'). Default: all inferred pages.")
    ap.add_argument("--exclude-pages", type=str, default=None, help="Comma-separated pages to exclude.")
    ap.add_argument("--dry-run", action="store_true", help="Don’t write; just report planned changes.")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    pages_include = None
    if args.pages:
        pages_include = set(int(p.strip()) for p in args.pages.split(",") if p.strip())

    pages_exclude = None
    if args.exclude_pages:
        pages_exclude = set(int(p.strip()) for p in args.exclude_pages.split(",") if p.strip())

    out_lines, order, counts = stack_pages(
        lines=lines,
        anchor_x_mm=args.anchor_x_mm,
        start_y_mm=args.start_y_mm,
        page_spacing_mm=args.page_spacing_mm,
        pages_include=pages_include,
        pages_exclude=pages_exclude
    )

    print("Pages (top to bottom):", order)
    print("Element counts per page:", counts)
    print(f"Anchor X: {args.anchor_x_mm:.3f} mm, First Y: {args.start_y_mm:.3f} mm, Spacing: {args.page_spacing_mm:.3f} mm")

    if args.dry_run:
        print("Dry-run only; not writing output.")
        return

    with open(args.output, "w", encoding="utf-8") as f:
        f.writelines(out_lines)
    print(f"Wrote: {args.output}")

if __name__ == "__main__":
    main()
