---
name: visual-layout-quality
description: "Validates text layout in SVGs, HTML, and infographics against overflow, padding, and spacing rules. Use when creating or editing visual assets with text in bounding containers — SVGs, fixed-layout HTML, infographics, email templates. Trigger when the user creates, edits, or reviews any visual with positioned text."
user-invocable: true
---

# Visual Layout Quality

Mandatory validation rules for every visual asset containing positioned text. Apply these checks whenever creating, editing, or reviewing SVGs, fixed-layout HTML, infographics, email templates, or any visual where text sits inside a bounding container.

---

## Character Width Safety Ratios

Use these multipliers to estimate the rendered pixel width of a string. Multiply `font_size` by the ratio, then multiply by the character count.

| Weight / Style         | Ratio |
|------------------------|-------|
| Normal (400-500)       | 0.55  |
| Bold (700-800)         | 0.60  |
| ALL-CAPS normal        | 0.62  |
| ALL-CAPS bold          | 0.67  |

**Estimated text width** = `char_count * font_size * ratio`

---

## Overflow Check Formula

Run this check for **every** text element before finalising a visual.

### Left-anchored text (text-anchor="start" or default)

```
text_x + (char_count * font_size * ratio) <= container_right_edge - padding
```

### Center-anchored text (text-anchor="middle")

```
estimated_width / 2 <= (container_width / 2) - padding
```

### Right-anchored text (text-anchor="end")

```
text_x - estimated_width >= container_left_edge + padding
```

If any check fails, the text will overflow. Shorten the text, reduce the font size, or widen the container.

---

## Max Characters Per Line — Quick Reference

Common container widths at common font sizes, using 20px padding on each side (usable width = container - 40px) and normal weight (ratio 0.55).

| Container | Usable | 13px | 14px | 15px | 16px | 18px | 20px | 22px |
|-----------|--------|------|------|------|------|------|------|------|
| 280px     | 240px  | 33   | 31   | 29   | 27   | 24   | 21   | 19   |
| 306px     | 266px  | 37   | 34   | 32   | 30   | 26   | 24   | 21   |
| 330px     | 290px  | 40   | 37   | 35   | 33   | 29   | 26   | 23   |
| 414px     | 374px  | 52   | 48   | 45   | 42   | 37   | 34   | 30   |
| 600px     | 560px  | 78   | 72   | 67   | 63   | 56   | 50   | 46   |

For bold text, multiply the max by `0.55 / 0.60 = 0.917` (subtract roughly 8%).
For ALL-CAPS normal, multiply by `0.55 / 0.62 = 0.887` (subtract roughly 11%).
For ALL-CAPS bold, multiply by `0.55 / 0.67 = 0.821` (subtract roughly 18%).

---

## Padding Rules (8px Grid)

All padding values align to an 8px grid for visual consistency.

| Token    | Value  | Use case                        |
|----------|--------|---------------------------------|
| pad-xs   | 8px    | Badge / pill text to edge       |
| pad-sm   | 16px   | Tight card inset                |
| pad-md   | 20px   | Standard card inset             |
| pad-lg   | 32px   | Generous card inset             |
| pad-xl   | 52px   | Canvas edge safety margin       |
| gap-card | 16-24px| Space between adjacent cards    |
| gap-line | ceil(font_size * 1.4) | Line-to-line vertical spacing |

---

## Canvas Edge Safety

Every visible element must respect canvas edge margins:

```
x >= 52
x + width <= canvas_width - 52
y >= font_size + 20
y <= canvas_height - 20
```

These margins prevent text from clipping at the edges of the rendered viewport and provide breathing room when the asset is embedded in a page.

---

## Multi-line Text Rules

SVG has **no automatic text wrapping**. You must handle line breaks manually.

- Use `<tspan>` elements or separate `<text>` elements for each line.
- **Repeat the `x` attribute** on every `<tspan>` to reset the horizontal position.
- Set `dy` for vertical line spacing: `dy = ceil(font_size * 1.4)`

Example:
```xml
<text x="60" y="100" font-size="16" fill="#1a1a2e">
  <tspan x="60" dy="0">First line of text here</tspan>
  <tspan x="60" dy="23">Second line continues here</tspan>
  <tspan x="60" dy="23">Third line wraps manually</tspan>
</text>
```

---

## Adjacent Element Collision

When placing elements near each other, enforce minimum gaps:

**Horizontal adjacency:**
```
right_element_x >= left_element_x + left_element_width + 16
```

**Vertical adjacency:**
```
lower_element_y >= upper_element_y + ceil(font_size * 1.4)
```

These minimums prevent visual crowding and ensure readability at standard zoom levels.

---

## Pre-commit Layout Checklist

Run through this checklist before finalising any visual asset:

- [ ] Every text element has been checked against the overflow formula
- [ ] Padding is consistent within each container (using pad-* tokens)
- [ ] Canvas edge safety margins are respected (52px horizontal, font_size+20 / 20px vertical)
- [ ] Multi-line text uses explicit tspan with repeated x and correct dy
- [ ] Adjacent elements have at least 16px horizontal / 1.4em vertical gap
- [ ] Bold and ALL-CAPS text uses the correct (wider) ratio
- [ ] Font sizes are readable at intended display size (minimum 12px for body text)
- [ ] No text element extends beyond its parent container

---

## SVG-Specific Rules

- **Always set explicit `width`, `height`, and `viewBox`** on the root `<svg>` element.
- **No `<foreignObject>`** — it breaks GitHub README rendering and many SVG consumers.
- **Font family fallback chain** — always end with a generic family:
  ```
  font-family="Inter, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
  ```
- **Extend filter regions** for shadows and glows — set `x="-50%" y="-50%" width="200%" height="200%"` on `<filter>` elements to prevent clipping of blur effects.

---

## HTML / Infographic Rules

The same character width ratios and overflow formulas apply to:

- Fixed-width HTML layouts (email templates, embedded widgets)
- PDF generation from HTML
- Infographic creation tools
- Any context where text is placed in a container of known pixel width

**Core principle:** Compute the estimated text width using the ratios above, then compare to the container width minus padding on both sides. If it does not fit, adjust before rendering.

---

## When to Use

Invoke this skill in these situations:

- **`/visual-layout-quality`** — validate the current file against all rules
- **`/visual-layout-quality path/to/file.svg`** — validate a specific file
- **Creating new SVGs** — this skill auto-triggers when you create or edit SVGs, fixed-layout HTML, or infographics
- **Reviewing visual diffs** — check whether a change introduces overflow or spacing violations
- **Debugging clipped text** — when text appears cut off in a rendered visual, run the overflow check to find the violation

---

## Validation Process

When validating a visual asset, follow this sequence:

1. **Identify all text elements** and their parent containers (rect, card, section, or canvas).
2. **Compute estimated width** for each text element using the character width ratios.
3. **Check against container bounds** using the appropriate overflow formula (left/center/right anchored).
4. **Verify padding consistency** within each container — all text should use the same pad-* token.
5. **Check canvas edge safety margins** — no element should violate the 52px horizontal or vertical margin rules.
6. **Check adjacent element spacing** — verify minimum gaps between neighbouring elements.
7. **Report violations** with the estimated width vs. available width, and suggest a fix (shorter text, smaller font, wider container).
