# Review Round: 2026-03-31

This note captures the first external critique loop after the major rewrite.

## Participants

- Codex: initial rewrite and self-rating
- Claude: critical review of the rewrite
- user: direction on structure, generality, and follow-up priorities

## Rating Comparison

- Codex initial rating: `8/10`
- Claude review rating: `7/10`
- Codex revised rating after review: `7.5/10`
- Claude follow-up review after the first refinement pass: `8/10`

## Claude's Main Findings

1. The universal-principles vs implementation split is the right architecture.
2. The rendered QA workflow is the strongest part of the redesign.
3. The skill was still stronger for SVG than for slides/PDF.
4. `SKILL.md` had redundancy between principles and non-negotiable rules.
5. `implementation-slides-pdf.md` was too thin.
6. Font substitution should be a first-class failure mode.
7. `svg_layout_audit.py` had significant blind spots.
8. Auto-run conditions for validation were too broad.

## Resulting Follow-Up Changes

- added `font substitution drift` as a failure class
- strengthened slides/PDF implementation guidance
- tightened auto-run language to `final-quality` assets
- added batch timing guidance for validation rounds
- clarified that optical alignment only has teeth during rendered QA
- reduced `SKILL.md` redundancy by replacing the old non-negotiable section with a smaller operational-check section
- improved the SVG audit script with:
  - `style=` parsing
  - basic `translate()` handling
  - inherited transform offsets for nested groups

## Claude Follow-Up Findings

Claude's next review judged most structural issues addressed and called out four remaining priorities:

1. add a minimal PPTX/PDF audit helper for parity with the SVG script
2. add an explicit `Known Limitations` block to `svg_layout_audit.py`
3. improve the SVG width heuristic for CJK and monospace text
4. add limited path/container support if it can be done without major complexity

## Current State After The Follow-Up Pass

Those four priorities are now addressed to a practical first version:

1. `scripts/pptx_pdf_layout_audit.py` exists and provides lightweight parity for slides and PDFs
2. `scripts/svg_layout_audit.py` now has an explicit `Known limitations` block in the script header
3. the SVG width heuristic now treats CJK and monospace text differently from default Latin text
4. the SVG audit now includes limited bounding-box support for:
   - `rect`
   - `circle`
   - `ellipse`
   - simple closed `path` containers built from line commands

This does not mean the tooling is complete.

The scripts are still intentionally heuristic:

- SVG support is not transform-complete and is not font-metric accurate
- PDF support is still metadata-level only and does not inspect actual rendered text frames
- rendered thumbnails or exported page/image inspection still outrank script output

The practical result is that the repo now feels structurally finished enough for another external review round.

## Why This Note Exists

The point is not just to preserve praise or criticism. The point is to preserve:

- what changed after outside review
- how ratings shifted after critique
- which weaknesses were judged structural vs tactical

This is intended as a lightweight evolution record for future review rounds.
