---
name: visual-layout-quality
description: "Use when creating, editing, reviewing, or debugging visual assets where layout quality matters: SVGs, PNG/JPG-backed graphics, Excalidraw exports, diagrams, README hero images, fixed-layout HTML, infographics, slide decks, and PDFs. Focus on overflow, container sizing, internal padding, spacing rhythm, centering, collisions, clipping, legibility, and rendered-output QA."
user-invocable: true
---

# Visual Layout Quality

Use this skill for any visual artifact where layout can fail after generation, export, or rendering.

This skill is intentionally split into two layers:

- universal layout principles that apply across formats
- format-specific implementation guidance for SVG, slides/PDFs, Excalidraw, and related surfaces

Keep the principles stable. Change the implementation layer when a tool or renderer behaves differently.

Read [incident-patterns.md](references/incident-patterns.md) when you want the generalized failure classes from local Codex and Claude history. Read [research-notes.md](references/research-notes.md) when you want the external basis for the principles below. Read [validation-round.md](references/validation-round.md) when you need the render-and-inspect workflow, time estimation, or PDF/slide guidance.

For implementation details, read only the file that matches the current artifact:

- [implementation-svg.md](references/implementation-svg.md)
- [implementation-slides-pdf.md](references/implementation-slides-pdf.md)
- [implementation-excalidraw.md](references/implementation-excalidraw.md)

## Core Rule

Do not treat source markup or scene data as the final truth.

For final-quality work, judge the rendered output that the user will actually see:

- exported PNG/JPG
- rendered SVG
- rendered PDF pages
- slide thumbnails
- Excalidraw export, not just the editable canvas

## Universal Principles

These rules should hold across formats unless a specific renderer forces an exception.

### 1. Content Outranks Decoration

Decorative elements are optional. Content is not.

- If a shape, arrow, grid, glow, or accent competes with text, the decoration loses.
- Background and decorative elements belong behind content in z-order.
- Decorative motifs should live in margins, background bands, or clearly secondary lanes.

### 2. Containers Must Fit Their Content

- If the copy grows, the container grows.
- If the container cannot grow, shorten or split the copy.
- A label that barely fits is treated as a failure.

### 3. Padding Is Part Of The Design, Not Spare Space

- Text should not ride the border of a component.
- Internal padding should be consistent within a component family.
- Weak breathing room is a real defect even if no border is crossed.

### 4. Spacing Must Communicate Structure

- Related elements get tighter spacing than unrelated elements.
- Titles need more separation from the next section boundary than sibling items need from each other.
- If all gaps are similar, hierarchy collapses.

### 5. Optical Alignment Beats Raw Arithmetic

- Centering is judged visually, not only numerically.
- Dot-and-label pairs, pills, badges, bullets, and icon rows frequently need optical correction after mathematical placement.

### 6. Legibility Beats Palette Fidelity

- If a color choice harms readability at the intended size, it fails.
- Overlong lines, low-contrast labels, and compressed text blocks are layout problems, not just typography problems.

### 7. Final Judgment Belongs To The Rendered Output

- Do not trust source markup or scene structure as the final truth.
- Judge the rendered artifact the user will actually see.

## Format Choice

Choose the final delivery format based on the target surface, not ideology.

- For GitHub READMEs, static embeds, and other hostile or inconsistent renderers, prefer PNG/JPG as the final delivery unless vector behavior is required and verified.
- SVG is acceptable as a source artifact when it materially improves editability, but do not rely on it as the only final output unless you validated the actual target renderer.
- For slide decks and PDFs, validate the rendered pages or thumbnails, not just the source `.pptx`, `.drawio`, `.excalidraw`, or SVG fragment.

## Required Workflow

Follow this order. Do not skip the rendered-output step for final assets.

### 1. Define the viewing context

Identify:

- final surface: README, browser, PDF, slide deck, doc, image export
- viewing size: thumbnail, embedded width, full slide, print, mobile
- stakes: draft, internal review, client-facing, executive-facing

Layout that barely works at full resolution often fails at embed size or in print thumbnails.

### 2. Build the content hierarchy first

Before adjusting pixels, classify content into:

- primary headline
- secondary support text
- metadata or stats
- grouped detail
- decoration

If too many elements behave like primary elements, the asset will feel crowded even if nothing overlaps.

### 3. Size from content outward

Containers must be sized from the content they hold.

- If the copy grows, the box grows.
- If the box cannot grow, shorten or split the copy.
- Do not force-fit multi-word labels into pills, buttons, badges, or cards without checking the rendered result.

### 4. Apply spacing as a system

Use spacing bands, not ad hoc pixel nudges:

- `8-12px`: tight internal separation inside chips, pills, icon-label pairs
- `12-16px`: dense card internals
- `16-24px`: standard card padding and related element gaps
- `24-32px`: separation between cards or sub-sections
- `32-64px`: major section spacing
- `48-64px`: canvas edge safety for medium and large graphics

Use an 8px rhythm where practical, but prioritize optical balance over rigid arithmetic.

### 5. Protect content from decoration

Decorative elements are allowed only if they do not compete with content.

- Keep accent bars, glows, grids, and shape motifs in margins or background layers.
- Put background and decorative shapes behind content in z-order.
- Arrows and connectors must terminate at the edge of the target object, not intrude into it.
- Do not let callout circles, shadows, or workflow arrows cross through labels.

### 6. Validate optical alignment

Do not trust mathematical center alone.

- Dots, icons, bullets, and text labels must look centered as a group.
- Rounded-rectangle labels often need small optical adjustments even when numerically centered.
- If the element feels off by eye, correct it even if the numbers match.

### 7. Render and inspect

For final-quality work, inspect the rendered output:

- SVG: render to PNG or open the rendered SVG in the actual target viewer
- PDF: render pages to images or thumbnails
- slides: render thumbnails or export to PDF and inspect pages
- Excalidraw: export the scene and inspect the export, not only the live editor

If the user has not explicitly requested a final QA round, offer the optional validation round described below.

## Non-Negotiable Cross-Format Rules

### Container Rules

- Text must not touch the visual edge of its container.
- Internal padding must be consistent within the same component family.
- A label that barely fits is treated as a failure; "inside the border" is not sufficient.
- If one card in a row needs more padding or height, usually the whole row should be normalized.

### Typography Rules

- Body copy should usually stay within readable line lengths; as an accessibility bound, avoid lines longer than 80 characters when possible.
- Use enough line height to prevent vertical crowding. Dense labels can go tighter; paragraphs should not.
- ALL-CAPS text needs more width and more breathing room than mixed case.
- Very light text on colored surfaces is a failure if it harms legibility, even if it matches the palette.

### Rhythm Rules

- Related elements should be grouped by smaller spacing than unrelated elements.
- Titles need visibly more space below them than the space between sibling items within the section.
- If a footer or bottom band feels glued to the section above it, increase the gap or reduce the footer prominence.

### Collision Rules

- No object may obscure text.
- No connector may cross a label unless the diagram form explicitly requires it and the label remains fully legible.
- No decorative motif may sit in the same visual lane as important content.

### Edge Safety Rules

- Important text or shapes should not ride the canvas edge.
- Leave a stronger edge margin on assets meant for GitHub embeds, thumbnails, or slides viewed on shared screens.

## Optional Validation Round

This skill supports an optional second-pass visual validation round.

When the model believes the asset is done, it should estimate how long a render-and-inspect pass will take and ask whether to run it, unless one of the auto-run conditions below is met.

### Ask Before Running When

- the asset is still an intermediate draft
- the validation round will materially slow the request
- the artifact count is large enough that the user may want to trade quality for time

Use a concise question such as:

`I can do a rendered QA pass on the exported asset. Estimated time: 3-6 minutes for this file. Want me to run it?`

### Auto-Run Without Asking When

- the user explicitly asked for polish, QA, review, validation, or final export
- the deliverable is client-facing or executive-facing
- the asset is an SVG, PDF, slide, or Excalidraw export with positioned text
- the request already includes phrases like "make sure it looks right", "check spacing", "inspect visually", or equivalent

### Time Estimation Heuristics

Use these rough bands before asking:

- single SVG, PNG, JPG, or simple diagram: `1-3 min`
- single PDF page or single slide: `1-3 min`
- small deck or PDF `2-10 pages/slides`: `3-8 min`
- medium deck or PDF `11-30 pages/slides`: `8-20 min`
- large deck or PDF `30+ pages/slides`: `15-40+ min`

If exports are already available, estimate near the low end. If rendering tools, screenshots, or retries are needed, estimate near the high end.

### What the Validation Round Must Do

1. Export or render the actual output.
2. Inspect the rendered pages or images.
3. Check the rendered output against this skill's rules, not just the source file.
4. Repair issues and re-render when needed.
5. Report whether the artifact passed and what was corrected.

Read [validation-round.md](references/validation-round.md) for the exact format-specific workflow.

## Implementation Layer

Do not overload the main principles with renderer-specific tactics.

Use:

- [implementation-svg.md](references/implementation-svg.md) for SVG and fixed-layout HTML
- [implementation-slides-pdf.md](references/implementation-slides-pdf.md) for slide decks and PDFs
- [implementation-excalidraw.md](references/implementation-excalidraw.md) for Excalidraw

## Reporting Failures

When you find problems, classify them using failure classes instead of vague statements:

- `container-copy mismatch`
- `padding collapse`
- `optical misalignment`
- `decorative intrusion`
- `section rhythm collapse`
- `edge clipping risk`
- `contrast / legibility failure`
- `render drift`

Report the visible symptom and the structural fix.

Prefer:

- `Delivery band headline collides with support line because the band is too short for the copy. Increase band height or split the copy.`

Not:

- `Spacing looks a little off.`

## Repair Strategy

When a layout fails, repair in this order:

1. remove or demote decorative interference
2. resize the container
3. adjust spacing bands
4. rewrite or split copy
5. reduce type size only if the hierarchy still holds

Do not use font-size reduction as the first fix unless the artifact is clearly oversized overall.

## What This Skill Is For

Invoke this skill for:

- README hero graphics
- SVG diagrams and infographics
- PNG or JPG marketing graphics with positioned text
- fixed-layout HTML destined for image or PDF export
- slide decks and PDF exports
- Excalidraw diagrams and exported boards
- visual QA after generation or before final delivery
