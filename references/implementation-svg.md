# Implementation: SVG And Fixed-Layout HTML

Use these tactics when applying the universal principles to SVG or other fixed-layout markup.

## Why SVG Needs Its Own Layer

SVG has renderer-specific behavior around anchoring, line breaks, and export quality.

These rules are implementation tactics, not universal design law.

## Practical Rules

- Validate anchored text based on actual rendered behavior.
- If using multi-line SVG text, make line breaks explicit.
- If a label is close to the edge in source, assume it is at risk in render.
- Prefer rendering SVG to PNG for final inspection.
- For GitHub and similar renderers, avoid relying on fragile SVG features when a PNG final export is safer.

## Audit Workflow

1. Run:

```bash
python3 scripts/svg_layout_audit.py path/to/file.svg
```

2. Treat the script as a first-pass heuristic audit only.
3. Read the script header before trusting a clean pass. It documents the current transform and container-detection limits.
4. Render the SVG to PNG or inspect it in the target renderer.
5. Fix source layout issues.
6. Re-render and re-check.

## Specific Implementation Risks

- `text-anchor` changes the actual rendered relationship between text and its anchor point.
- Multi-line text alignment can drift if line resets are not explicit.
- Labels that "fit" in XML can still look cramped in render.
- SVGs that are fine in one viewer can look wrong in README or browser embeds.
- The audit script can now use simple `path`, `circle`, and `ellipse` bounding boxes as containers, but this is still a best-effort approximation.
- If the file depends on `scale`, `rotate`, `matrix`, clipping masks, or complex bezier paths, prefer rendered inspection over heuristic confidence immediately.

## Typical Fixes

- widen the container
- split the copy across lines
- increase internal padding
- reduce decorative density
- export final delivery as PNG when the target surface is unreliable
