# Dex Ideas

These scores were normalized after the first Hopper backlog pass so they mean the same thing across the combined list, not just inside the original Dex file.

## 1. Rendered QA helper for exported assets

Build a small helper that standardizes:

- render SVG to PNG
- export PPTX to PDF or thumbnails
- render PDF pages to images
- present a single checklist-oriented inspection pass

Why it matters:

- the skill already says rendered output outranks source truth
- the process is currently described well, but still mostly manual

Scores:

- Effort: `4`
- Uncertainty: `3`
- Impact: `4`

## 2. PDF text-box preflight beyond `pdfinfo`

Extend the PDF helper with something like `pdfplumber` so the script can inspect:

- text block counts
- basic bounding boxes
- suspicious density or footer collisions

Why it matters:

- the current PDF path is honest but thin
- this would make the PDF lane more useful than metadata symmetry alone

Scores:

- Effort: `3`
- Uncertainty: `3`
- Impact: `3`

## 3. Better SVG multiline text handling

Improve the SVG audit so `tspan dy` and multiline vertical stacking are accounted for.

Why it matters:

- current SVG coverage is good enough for v1
- multiline vertical overflow is still an obvious blind spot

Scores:

- Effort: `2`
- Uncertainty: `2`
- Impact: `2`

## 4. Broader fixture coverage

Add more test fixtures for:

- PPTX edge cases with theme fonts
- SVG cases with simple paths and multiline text
- one Excalidraw export case if practical

Why it matters:

- the smoke tests are good for v1 confidence
- broader fixtures would make future edits safer

Scores:

- Effort: `3`
- Uncertainty: `2`
- Impact: `3`

## 5. Rename the GitHub repo slug

Rename the repo from `skill-visual-layout-quality` to `skill-visual-asset-layout`.

Why it matters:

- the skill name is already updated
- the stale repo slug is minor but real friction

Scores:

- Effort: `1`
- Uncertainty: `1`
- Impact: `1`
