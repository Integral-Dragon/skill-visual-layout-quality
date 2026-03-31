#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


NS_RE = re.compile(r"\{.*\}")


def strip_ns(tag: str) -> str:
    return NS_RE.sub("", tag)


def parse_length(value: str | None, fallback: float = 0.0) -> float:
    if value is None:
        return fallback
    match = re.match(r"^\s*(-?\d+(?:\.\d+)?)", value)
    return float(match.group(1)) if match else fallback


def parse_first_number(value: str | None, fallback: float = 0.0) -> float:
    if value is None:
        return fallback
    match = re.search(r"-?\d+(?:\.\d+)?", value)
    return float(match.group(0)) if match else fallback


def parse_style(style: str | None) -> dict[str, str]:
    if not style:
        return {}
    result: dict[str, str] = {}
    for part in style.split(";"):
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def pick_attr(node: ET.Element, name: str, default: str | None = None) -> str | None:
    if name in node.attrib:
        return node.attrib[name]
    return parse_style(node.attrib.get("style")).get(name, default)


def parse_translate(transform: str | None) -> tuple[float, float]:
    if not transform:
        return 0.0, 0.0
    total_x = 0.0
    total_y = 0.0
    for match in re.finditer(r"translate\(\s*(-?\d+(?:\.\d+)?)\s*(?:[, ]\s*(-?\d+(?:\.\d+)?))?\s*\)", transform):
        total_x += float(match.group(1))
        total_y += float(match.group(2) or 0.0)
    return total_x, total_y


def parse_viewbox(root: ET.Element) -> tuple[float, float]:
    viewbox = root.attrib.get("viewBox")
    if viewbox:
        nums = [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", viewbox)]
        if len(nums) == 4:
            return nums[2], nums[3]
    return parse_length(root.attrib.get("width"), 0.0), parse_length(root.attrib.get("height"), 0.0)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def is_all_caps(text: str) -> bool:
    letters = [c for c in text if c.isalpha()]
    return bool(letters) and all(c.upper() == c for c in letters)


def width_ratio(text: str, weight: str | None) -> float:
    bold = parse_first_number(weight, 400) >= 700
    caps = is_all_caps(text)
    if caps and bold:
        return 0.67
    if caps:
        return 0.62
    if bold:
        return 0.60
    return 0.55


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height

    def contains(self, x: float, y: float) -> bool:
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


@dataclass
class TextNode:
    text: str
    x: float
    y: float
    font_size: float
    font_weight: str | None
    anchor: str
    element: ET.Element

    @property
    def estimated_width(self) -> float:
        return len(self.text) * self.font_size * width_ratio(self.text, self.font_weight)


@dataclass
class TraversalState:
    offset_x: float = 0.0
    offset_y: float = 0.0


def collect_rects(root: ET.Element, state: TraversalState | None = None) -> list[Rect]:
    state = state or TraversalState()
    rects: list[Rect] = []
    dx, dy = parse_translate(root.attrib.get("transform"))
    next_state = TraversalState(state.offset_x + dx, state.offset_y + dy)
    if strip_ns(root.tag) == "rect":
        rects.append(
            Rect(
                x=parse_length(root.attrib.get("x")) + next_state.offset_x,
                y=parse_length(root.attrib.get("y")) + next_state.offset_y,
                width=parse_length(root.attrib.get("width")),
                height=parse_length(root.attrib.get("height")),
            )
        )
    for child in root:
        rects.extend(collect_rects(child, next_state))
    return rects


def collect_text_nodes(root: ET.Element, state: TraversalState | None = None) -> list[TextNode]:
    state = state or TraversalState()
    nodes: list[TextNode] = []
    dx, dy = parse_translate(root.attrib.get("transform"))
    next_state = TraversalState(state.offset_x + dx, state.offset_y + dy)
    if strip_ns(root.tag) == "text":
        text = normalize_text("".join(root.itertext()))
        if text:
            nodes.append(
                TextNode(
                    text=text,
                    x=parse_first_number(pick_attr(root, "x")) + next_state.offset_x,
                    y=parse_first_number(pick_attr(root, "y")) + next_state.offset_y,
                    font_size=parse_length(pick_attr(root, "font-size"), 16.0),
                    font_weight=pick_attr(root, "font-weight"),
                    anchor=pick_attr(root, "text-anchor", "start") or "start",
                    element=root,
                )
            )
    for child in root:
        nodes.extend(collect_text_nodes(child, next_state))
    return nodes


def choose_container(node: TextNode, rects: list[Rect], canvas_w: float, canvas_h: float) -> Rect:
    containing = [rect for rect in rects if rect.contains(node.x, node.y)]
    if containing:
        return min(containing, key=lambda r: r.area)
    return Rect(0.0, 0.0, canvas_w, canvas_h)


def auto_padding(container: Rect) -> float:
    if container.width <= 120:
        return 8.0
    if container.width <= 280:
        return 12.0
    if container.width <= 600:
        return 16.0
    return 24.0


def audit_svg(path: Path) -> int:
    root = ET.parse(path).getroot()
    canvas_w, canvas_h = parse_viewbox(root)
    rects = collect_rects(root)
    text_nodes = collect_text_nodes(root)

    problems: list[str] = []

    for node in text_nodes:
        container = choose_container(node, rects, canvas_w, canvas_h)
        pad = auto_padding(container)
        avail = max(container.width - 2 * pad, 0)
        est = node.estimated_width
        label = node.text[:72]

        if est > avail:
            problems.append(
                f"overflow risk: '{label}' est={est:.1f}px available={avail:.1f}px "
                f"anchor={node.anchor} font={node.font_size:g}px container=({container.x:g},{container.y:g},{container.width:g},{container.height:g})"
            )

        if container.width != canvas_w:
            if node.anchor == "start" and node.x - container.x < pad:
                problems.append(f"padding risk: '{label}' start anchor too close to left edge")
            if node.anchor == "end" and (container.x + container.width - node.x) < pad:
                problems.append(f"padding risk: '{label}' end anchor too close to right edge")
            if node.anchor == "middle":
                half = est / 2
                if half > (container.width / 2 - pad):
                    problems.append(f"padding risk: '{label}' centered text has weak side padding")

        if node.x < 24 or node.x > canvas_w - 24 or node.y < 24 or node.y > canvas_h - 24:
            problems.append(f"edge risk: '{label}' is close to canvas edge")

        tspans = [child for child in node.element if strip_ns(child.tag) == "tspan"]
        if len(tspans) > 1:
            missing_reset = [t for t in tspans[1:] if "x" not in t.attrib]
            if missing_reset:
                problems.append(f"multi-line risk: '{label}' has tspans without repeated x attribute")

    print(path)
    if problems:
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print("  OK: no obvious overflow, padding, or edge risks found")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit SVG text for likely layout risks.")
    parser.add_argument("paths", nargs="+", help="SVG files to inspect")
    args = parser.parse_args()

    exit_code = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            print(f"{path}\n  - missing file", file=sys.stderr)
            exit_code = 1
            continue
        exit_code = max(exit_code, audit_svg(path))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
