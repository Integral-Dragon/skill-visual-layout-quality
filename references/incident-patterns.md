# Incident Patterns

These failure classes are distilled from recurring issues in local Codex and Claude history on this machine.

## 1. Container-Copy Mismatch

The words grow, but the containing box does not.

Recurring examples:

- README hero stat bands and delivery bands where copy fit mathematically but still crowded the edge.
- diagram labels where the text enlarged and the outer box stayed fixed.
- buttons or pills where labels were not truly contained after export.

Rule:

- If the copy changes materially, re-evaluate the container size before continuing.

## 2. Padding Collapse

The text is technically inside the container but feels glued to the border.

Recurring examples:

- repeated complaints about "inner padding is bad"
- workflow boxes with insufficient breathing room between title and body
- labels in rounded rectangles that looked compressed

Rule:

- Treat weak internal breathing room as a real failure, not a polish-only issue.

## 3. Decorative Intrusion

Decoration enters the same space as content.

Recurring examples:

- slide headers overlapping content or leftover reference artifacts
- workflow graphics partially obscuring text
- arrows running into target objects instead of terminating at their edge
- decorative bars or shapes layered above text because of insertion order

Rule:

- Decoration must live in background layers or margins. If it crosses content, it loses.

## 4. Optical Misalignment

The coordinates say centered, but the visual grouping does not.

Recurring examples:

- green dots not centered with adjacent labels
- centered words inside rounded rectangles still looking off
- checkmarks and warning symbols misaligned in rendered docs

Rule:

- Validate grouping by eye after numeric placement.

## 5. Rhythm Collapse

The spacing system breaks down across the asset.

Recurring examples:

- not enough space between section title and boxes
- lower panels fighting the section above
- footer or bottom ribbon appearing jammed against the content

Rule:

- Section spacing must communicate grouping. Major bands need visibly more air than intra-band details.

## 6. Legibility Failure

Text is present but not readable enough.

Recurring examples:

- text that became too light on colored surfaces
- dense content blocks that were technically complete but illegible in presentation view

Rule:

- If the intended viewing surface makes the text hard to read, it fails.

## 7. Render Drift

The source looks acceptable, but the final export or target renderer does not.

Recurring examples:

- SVGs that looked acceptable in source but failed in README or final inspection
- user preference for PNG final assets because rendered SVG output proved unreliable
- Excalidraw scenes that appeared janked until reselected or re-expanded

Rule:

- Final judgment belongs to the rendered artifact, not the editable source.
