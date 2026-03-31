# Visual Layout Quality — Extended Reference

This document provides the detailed rationale and derivations behind the rules in SKILL.md.

---

## Character Width Ratio Derivation

The ratios used in this skill are derived from real font metrics, with a safety margin applied.

### Source: Arial / Helvetica Metrics

The OS/2 table in Arial (the most common web-safe font) reports:

- **xAvgCharWidth** = 904 units
- **unitsPerEm (upem)** = 2048

This gives a raw average character width ratio of:

```
904 / 2048 = 0.4414
```

This is the average width of lowercase Latin characters relative to 1em. However, this raw value is too tight for layout safety because:

1. **Uppercase letters are wider** — capital letters like M, W, Q average roughly 15-25% wider than lowercase.
2. **Real text is mixed case** — even body text contains capitals at sentence starts, proper nouns, and acronyms.
3. **Punctuation varies** — some punctuation (em-dash, ellipsis) is significantly wider than the average character.
4. **Different fonts vary** — Inter, Segoe UI, and Roboto have slightly different metrics. A safety margin covers the spread.

### Safety Margin Calculation

Starting from the raw 0.441 ratio:

| Adjustment           | Factor | Cumulative |
|----------------------|--------|------------|
| Raw xAvgCharWidth    | 0.441  | 0.441      |
| Mixed-case overhead  | +15%   | 0.507      |
| Font variation margin| +8%    | 0.548      |
| **Rounded up**       |        | **0.55**   |

This gives us the **0.55** ratio for normal weight (400-500) text.

### Weight and Case Adjustments

**Bold (700-800): 0.60**

Bold glyphs are wider due to thicker strokes that extend the sidebearings. Empirical measurement across Arial Bold, Inter Bold, and Roboto Bold shows approximately 8-10% wider average character widths. Applying this to 0.55:

```
0.55 * 1.09 = 0.5995 -> 0.60
```

**ALL-CAPS normal: 0.62**

Uppercase letters are wider than mixed-case averages. The uppercase-only average for Arial is approximately 0.53 (raw), which with the same safety margins gives:

```
0.53 * 1.08 * 1.08 = 0.618 -> 0.62
```

**ALL-CAPS bold: 0.67**

Combining the uppercase and bold adjustments:

```
0.62 * 1.08 = 0.6696 -> 0.67
```

### When These Ratios Underestimate

The ratios are designed to be safe for most Latin text, but they may underestimate in these cases:

- **Strings dominated by wide characters** (W, M, @, %, em-dash) — add 10-15% to the estimate.
- **Monospace fonts** — use 0.60 for all weights (each character is exactly 0.60em in most monospace fonts).
- **CJK characters** — use 1.0 (full-width characters occupy 1em each).
- **Very small font sizes (< 12px)** — hinting and rounding can make glyphs slightly wider than predicted.

### When These Ratios Overestimate

- **Strings dominated by narrow characters** (i, l, 1, punctuation like periods and commas).
- **Condensed font variants** — reduce the ratio by 15-20%.

---

## textLength and lengthAdjust

SVG provides two attributes for controlling rendered text width:

### `textLength`

Sets the exact rendered width of a text element. The browser stretches or compresses the text (letter-spacing and/or glyph widths) to fit.

```xml
<text x="60" y="100" textLength="280" lengthAdjust="spacingAndGlyphs">
  This text will be exactly 280px wide
</text>
```

### `lengthAdjust`

Controls how the browser adjusts the text to match `textLength`:

| Value              | Behaviour                                              |
|--------------------|--------------------------------------------------------|
| `spacing`          | Only adjusts letter-spacing (default). Glyphs keep their natural width. |
| `spacingAndGlyphs` | Adjusts both letter-spacing and glyph widths. More aggressive fitting. |

### When to Use textLength

**Use it as a safety net for borderline text:**

- Text that is close to the container edge (within 10% of overflow).
- Titles or headings where you want exact alignment with a container.
- Labels that must fit a fixed-width badge or pill shape.

Example:
```xml
<rect x="50" y="80" width="200" height="36" rx="18" fill="#e0e0e0"/>
<text x="150" y="103" text-anchor="middle" font-size="14"
      textLength="180" lengthAdjust="spacingAndGlyphs">
  Status: In Progress
</text>
```

### When NOT to Use textLength

- **Short labels** (fewer than 10 characters) — compression looks unnatural on short strings.
- **Body text** — paragraph text should never be force-fitted; rewrite or reflow instead.
- **When the estimate shows plenty of room** (more than 20% margin) — textLength adds unnecessary complexity.
- **Multi-line text** — textLength applies per-element, not per-line in a tspan group. Each tspan would need its own textLength, which is fragile.

---

## Common Font Metrics Table

Pre-computed estimated widths for common font sizes and string lengths, using the normal weight ratio (0.55).

### Estimated Width (px) by Font Size and Character Count

| Chars | 12px | 13px | 14px | 15px | 16px | 18px | 20px | 22px | 24px |
|-------|------|------|------|------|------|------|------|------|------|
| 5     | 33   | 36   | 39   | 41   | 44   | 50   | 55   | 61   | 66   |
| 10    | 66   | 72   | 77   | 83   | 88   | 99   | 110  | 121  | 132  |
| 15    | 99   | 107  | 116  | 124  | 132  | 149  | 165  | 182  | 198  |
| 20    | 132  | 143  | 154  | 165  | 176  | 198  | 220  | 242  | 264  |
| 25    | 165  | 179  | 193  | 206  | 220  | 248  | 275  | 303  | 330  |
| 30    | 198  | 215  | 231  | 248  | 264  | 297  | 330  | 363  | 396  |
| 35    | 231  | 250  | 270  | 289  | 308  | 347  | 385  | 424  | 462  |
| 40    | 264  | 286  | 308  | 330  | 352  | 396  | 440  | 484  | 528  |
| 45    | 297  | 322  | 347  | 371  | 396  | 446  | 495  | 545  | 594  |
| 50    | 330  | 358  | 385  | 413  | 440  | 495  | 550  | 605  | 660  |

### Quick Formula

For any combination not in the table:

```
estimated_width = char_count * font_size * 0.55
```

Replace 0.55 with the appropriate ratio for bold (0.60), ALL-CAPS (0.62), or ALL-CAPS bold (0.67).

---

## Common Container Width Reference

Standard container widths encountered in web and infographic contexts:

| Context                  | Width   | Usable (20px pad) | Usable (32px pad) |
|--------------------------|---------|--------------------|--------------------|
| Mobile portrait          | 375px   | 335px              | 311px              |
| Mobile landscape         | 667px   | 627px              | 603px              |
| Email template           | 600px   | 560px              | 536px              |
| Card (small)             | 280px   | 240px              | 216px              |
| Card (medium)            | 330px   | 290px              | 266px              |
| Card (large)             | 414px   | 374px              | 350px              |
| Sidebar panel            | 300px   | 260px              | 236px              |
| Half-width column        | 500px   | 460px              | 436px              |
| Full content area        | 800px   | 760px              | 736px              |
| Wide infographic         | 1200px  | 1160px             | 1136px             |

---

## Line Height and Vertical Rhythm

The `ceil(font_size * 1.4)` rule for line spacing comes from the standard 1.4 line-height ratio, which provides comfortable readability for body text. The ceiling function ensures whole-pixel values for crisp rendering.

| Font Size | Line Height (1.4) | Rounded |
|-----------|-------------------|---------|
| 12px      | 16.8              | 17      |
| 13px      | 18.2              | 19      |
| 14px      | 19.6              | 20      |
| 15px      | 21.0              | 21      |
| 16px      | 22.4              | 23      |
| 18px      | 25.2              | 26      |
| 20px      | 28.0              | 28      |
| 22px      | 30.8              | 31      |
| 24px      | 33.6              | 34      |

For headings, a tighter ratio of 1.2 is acceptable:

| Font Size | Line Height (1.2) | Rounded |
|-----------|-------------------|---------|
| 24px      | 28.8              | 29      |
| 28px      | 33.6              | 34      |
| 32px      | 38.4              | 39      |
| 36px      | 43.2              | 44      |
| 40px      | 48.0              | 48      |
