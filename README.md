# Visual Layout Quality — Claude Code Skill

A Claude Code skill that validates text layout in SVGs, HTML, and infographics against overflow, padding, and spacing rules.

## What It Does

When you create or edit visual assets that contain positioned text — SVGs, fixed-layout HTML, infographics, email templates — this skill checks for:

- **Text overflow**: estimates rendered text width and verifies it fits within its container
- **Padding consistency**: enforces an 8px-grid padding system across all containers
- **Canvas edge safety**: ensures no elements are clipped at viewport edges
- **Element collision**: checks spacing between adjacent elements
- **Multi-line correctness**: validates tspan usage, repeated x attributes, and line spacing in SVGs
- **SVG best practices**: viewBox presence, no foreignObject, font fallback chains, filter region sizing

The skill uses character width safety ratios derived from real font metrics (Arial xAvgCharWidth) with safety margins for mixed case, bold, and ALL-CAPS text.

## Installation

### User-level (available in all projects)

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git ~/.claude/skills/visual-layout-quality
```

### Project-level (available to all contributors on a specific project)

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git .claude/skills/visual-layout-quality
```

Then add `.claude/skills/visual-layout-quality` to your `.gitignore` if you do not want to vendor the skill into the project repo, or commit it if you want everyone on the project to have it.

## Usage

### Direct invocation

```
/visual-layout-quality
```

Validates the current file against all layout rules.

```
/visual-layout-quality path/to/file.svg
```

Validates a specific file.

### Auto-triggering

The skill auto-triggers when Claude Code detects that you are creating, editing, or reviewing any visual asset with positioned text.

### During reviews

When reviewing visual diffs or debugging clipped text, invoke the skill to get a report of all layout violations with estimated vs. available widths and suggested fixes.

## Reference

See [reference.md](reference.md) for the full derivation of character width ratios, font metrics tables, textLength/lengthAdjust guidance, and common container width reference data.

## License

MIT -- see [LICENSE](LICENSE).
