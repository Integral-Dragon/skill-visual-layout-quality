# Validation Round

This file defines the optional second-pass render validation workflow.

## Purpose

A source file can be internally consistent and still fail after export or rendering.

Use this workflow when:

- the asset is final or client-facing
- the asset uses positioned text
- the format is SVG, PPTX, PDF, Excalidraw, or fixed-layout HTML
- the user explicitly asks for QA, polish, or visual inspection

## Ask-or-Auto Decision

Estimate the validation time before running it unless the user already asked for QA.

Suggested phrasing:

`I can run a rendered QA pass on the exported output. Estimated time: 4-8 minutes for this deck. Want me to do it?`

Auto-run without asking when:

- final deliverable quality is clearly required
- the user already complained about layout issues
- the current artifact type has a high render-risk profile

## Time Estimation

Use rough, honest bands:

- single asset, already exported: `1-3 min`
- single asset, export still needed: `2-5 min`
- small deck or PDF: `3-8 min`
- medium deck or PDF: `8-20 min`
- large deck or PDF: `15-40+ min`

Increase the estimate when:

- rendering tools are not already in place
- multiple retries are likely
- the workflow depends on screenshots or app launches

## Workflow by Format

### SVG

1. Run `python3 scripts/svg_layout_audit.py asset.svg`
2. Render to PNG or open the actual rendered SVG
3. Inspect the raster output
4. Repair
5. Re-render

### Slides / PPTX

1. Render thumbnails or export to PDF
2. Inspect rendered slides, not only source shapes
3. Look for title spacing, card padding, footer crowding, overlap, and legibility failures
4. Repair in source deck
5. Re-render and confirm

### PDF

1. Render pages to images or inspect thumbnails
2. For short PDFs, inspect every page
3. For long PDFs, inspect all pages if stakes are high; otherwise inspect representative pages plus any flagged pages
4. Repair source and re-render

### Excalidraw

1. Export the scene to PNG or SVG
2. Inspect the export
3. If the editor state looks wrong until clicked, treat that as a render-risk warning
4. Re-export after any nudge needed to stabilize text metrics
5. Judge the exported result only

## Pass Criteria

The visual passes only if:

- no visible overlap remains
- internal padding looks intentional
- section spacing communicates grouping
- centered items look centered
- text is legible at intended size
- the rendered artifact looks correct in the target surface
