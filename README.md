# Visual Layout Quality

A reusable visual QA skill for layout-heavy assets.

It is designed to catch the failure modes that repeatedly show up in generated visuals:

- text that technically fits but feels cramped
- internal padding collapse
- containers that do not grow with copy
- arrows, accents, and overlays intruding into content
- weak spacing rhythm between sections
- source files that look fine but rendered output that does not

## Scope

The skill is intended for:

- SVG graphics
- PNG/JPG-backed visuals with positioned text
- README hero graphics
- fixed-layout HTML and infographics
- Excalidraw exports
- slide decks and PDFs

## What Changed From The Original Version

The original skill was mostly an SVG overflow checker with width math.

This version adds:

- broader failure classes beyond overflow
- a clean separation between universal principles and format-specific implementation guidance
- slide deck and PDF validation guidance
- font substitution as a first-class layout risk
- render-and-inspect workflow as a first-class requirement
- optional second-pass visual validation with time estimation
- Excalidraw export guidance
- a lightweight `scripts/svg_layout_audit.py` script for first-pass SVG checks
- reference material split by incident patterns, external guidance, and validation workflow
- a checked-in review-round note capturing Claude/Codex/user iteration

## Repo Layout

```text
skill-visual-layout-quality/
  SKILL.md
  reference.md
  references/
    incident-patterns.md
    implementation-excalidraw.md
    implementation-slides-pdf.md
    implementation-svg.md
    research-notes.md
    review-round-2026-03-31.md
    validation-round.md
  scripts/
    svg_layout_audit.py
```

## Installation

### Claude Code

Personal:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git ~/.claude/skills/visual-layout-quality
```

Project-level:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git .claude/skills/visual-layout-quality
```

### Codex

Local install:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git ~/.codex/skills/visual-layout-quality
```

## Usage Notes

Use the skill when generating, reviewing, or debugging any visual artifact where layout quality matters.

The skill now supports an optional second-pass rendered QA round:

- it estimates how long the extra validation will take
- it asks before running it unless the task is clearly final/polish/QA work
- it validates the rendered output, not just the source asset

## SVG Audit Script

For SVGs, you can run:

```bash
python3 scripts/svg_layout_audit.py path/to/file.svg
```

This is a first-pass heuristic audit only. Final judgment should still come from the rendered output.

## License

MIT. See [LICENSE](LICENSE).
