# Implementation: Excalidraw

Use these tactics when applying the universal principles to Excalidraw scenes and exports.

## Why Excalidraw Needs Its Own Layer

Excalidraw can show transient layout drift between the editable scene and the exported result.

This is an implementation concern, not a reason to weaken the core principles.

## Practical Rules

- Validate the exported output, not just the editable scene.
- If text metrics look stale or objects appear to jump after selection, re-export and judge the export.
- If the scene editor and export disagree, the export wins.

## Validation Workflow

1. Export the scene to PNG or SVG.
2. Inspect the export.
3. If the editor looked janked before selection or resize, treat that as a render-risk warning.
4. Make any stabilizing adjustment needed in the scene.
5. Re-export and judge the export only.

## Typical Fixes

- increase box size to restore breathing room
- clean up connector endpoints so arrows stop at the target edge
- normalize spacing between related nodes
- remove decorative clutter that competes with labels
