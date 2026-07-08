# Assets/DesignSystem/Palette/

**Version:** 2.4.0
**Token source:** Assets/DesignSystem/Tokens/tokens.example.yaml
**Spec:** Core/STYLE_GUIDE.md §1

---

## Purpose

This document is the **visual reference** for the SDK color palette. It documents every color token with its hex value, RGB equivalent, intended usage, and explicit Do/Don't guidance. Use it when evaluating whether a generated page uses colors correctly.

For authoritative color philosophy, see `Core/COLOR_SYSTEM.md`.

---

## Primary Palette

| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| `TamiyaPrimary` | `#114B69` | 17, 75, 105 | Header band, side panel background, primary brand element |
| `TamiyaDark` | `#0B2F42` | 11, 47, 66 | Header border-bottom, hover state, deep shadow on primary-color |
| `TamiyaLight` | `#76ABC7` | 118, 171, 199 | Callout borders, secondary headings on white, tinted elements |
| `TamiyaUltraLight` | `#E8EFF2` | 232, 239, 242 | Background fills for callouts, alternating zones (NOT body background) |

### Primary Palette Usage Rules

**TamiyaPrimary**
- ✅ DO: Use for all header bands (C001), all side panel backgrounds, the C013 Step Number badge, C014 Time Box border
- ❌ DON'T: Use as body background (must remain White), use for body text on white, apply a gradient over it

**TamiyaDark**
- ✅ DO: Use as a shadow color within primary-color zones, use for the footer top-border, use for PanelBorder
- ❌ DON'T: Use directly on white backgrounds (low contrast), use as a large block color

**TamiyaLight**
- ✅ DO: Use for callout left-borders (C006), use for secondary text color when describing a primary-color-themed element
- ❌ DON'T: Use as body text color on white (insufficient contrast for 11pt text)

**TamiyaUltraLight**
- ✅ DO: Use for callout box backgrounds (C006), hover-state row fills
- ❌ DON'T: Use as the main page background (must always be pure white)

---

## Neutral Palette

| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| `White` | `#FFFFFF` | 255, 255, 255 | **ALL page backgrounds** — mandatory, immutable |
| `OffWhite` | `#F8F8F8` | 248, 248, 248 | Alternating table row fills |
| `LightGray` | `#E8E8E8` | 232, 232, 232 | Dividers, table borders, component outlines |
| `MidGray` | `#9B9B9B` | 155, 155, 155 | Placeholder text, metadata, secondary labels |
| `DarkGray` | `#4A4A4A` | 74, 74, 74 | **ALL body text** — primary reading color |
| `Black` | `#1A1A1A` | 26, 26, 26 | Headlines (H1, Display level), maximum contrast contexts |

### Neutral Palette Usage Rules

**White (#FFFFFF)**
- ✅ DO: Use as the background for every page content area, every component interior, every render container
- ❌ DON'T: Tint it, replace it with OffWhite for the main background, use transparency over it

**DarkGray (#4A4A4A)**
- ✅ DO: Use for all body text (11pt BodyFont), all caption text, all list items
- ❌ DON'T: Use for headlines (use Black), use on primary-color backgrounds (use White)

**MidGray (#9B9B9B)**
- ✅ DO: Use for metadata (page number in footer, SDK version label, secondary annotations)
- ❌ DON'T: Use for body copy (fails WCAG AA contrast at 11pt), use on colored backgrounds

---

## Accent Palette

| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| `GoldAccent` | `#C8A838` | 200, 168, 56 | Tips box left-border (C009), achievement indicators |
| `GoldLight` | `#F5E9B8` | 245, 233, 184 | Tips box background fill (C009) |

### Accent Palette Usage Rules

**GoldAccent / GoldLight**
- ✅ DO: Use exclusively for the Tips component (C009) and optional achievement badges
- ❌ DON'T: Use for warnings (use RedWarning), use as a general decoration, use as body text color

---

## Semantic Palette

| Token | Hex | RGB | When to Use |
|-------|-----|-----|-------------|
| `RedWarning` | `#D32F2F` | 211, 47, 47 | C008 Warning border and icon — safety risks only |
| `RedWarningLight` | `#FFEBEE` | 255, 235, 238 | C008 Warning background fill |
| `GreenSuccess` | `#388E3C` | 56, 142, 60 | Completion checkmarks, Final Checklist (P010) success states |
| `GreenSuccessLight` | `#E8F5E9` | 232, 245, 233 | Success background fill |
| `BlueInfo` | `#1976D2` | 25, 118, 210 | Secondary informational callouts |
| `BlueInfoLight` | `#E3F2FD` | 227, 242, 253 | Info callout background fill |

### Semantic Palette Usage Rules

- ✅ DO: Use semantic colors **only** for their designated semantic function
- ❌ DON'T: Use RedWarning for any non-warning element, use GreenSuccess decoratively
- ❌ DON'T: Mix semantic colors within the same component (a single box cannot be both warning and success)

---

## Forbidden Color Combinations

The following combinations are explicitly prohibited:

| Forbidden Combination | Reason |
|-----------------------|--------|
| TamiyaLight text on White background | Contrast ratio < 3:1 for 11pt body text (WCAG AA fail) |
| MidGray text on White background at body size | Contrast ratio ~3.5:1 — fails WCAG AA for normal text |
| Gold text on White background | Insufficient contrast |
| White text on White background | Invisible |
| Any gradient on the Header band | Violates Core/DESIGN_LANGUAGE.md Rule 47 (no decorative gradients) |
| RedWarning on TamiyaPrimary background | Color conflict, semantic confusion |

---

## Print Color Equivalents

For print-ready PDF export (CMYK FOGRA39 profile), use these approximate equivalents:

| Token | Hex | CMYK (approximate) | Pantone (approx.) |
|-------|-----|---------------------|-------------------|
| TamiyaPrimary | #114B69 | C:84 M:29 Y:0 K:59 (sRGB-basis approx., not color-managed) | Not verified |
| TamiyaDark | #0B2F42 | C:83 M:29 Y:0 K:74 (sRGB-basis approx., not color-managed) | Not verified |
| GoldAccent | #C8A838 | C:0 M:15 Y:75 K:20 | Pantone 124 C |
| RedWarning | #D32F2F | C:0 M:85 Y:80 K:15 | Pantone 485 C |
| GreenSuccess | #388E3C | C:75 M:0 Y:80 K:30 | Pantone 363 C |

> ⚠️ **Note:** CMYK conversions are approximate. Always validate a print proof before a production run. Pantone references are closest visual matches, not exact equivalents.

---

## Color Accessibility Summary

| Context | Pair | Contrast Ratio | WCAG AA (4.5:1 normal / 3:1 large) |
|---------|------|----------------|-------------------------------------|
| Body text | DarkGray on White | ~8.6:1 | ✅ Passes |
| Headline | Black on White | ~18.1:1 | ✅ Passes |
| Header text | White on TamiyaPrimary | ~9.4:1 | ✅ Passes |
| Callout text | DarkGray on TamiyaUltraLight | ~7.4:1 | ✅ Passes |
| Warning text | DarkGray on RedWarningLight | ~7.0:1 | ✅ Passes |
| Tips text | DarkGray on GoldLight | ~6.8:1 | ✅ Passes |
| Secondary label | MidGray on White | ~3.5:1 | ⚠️ Large text only |
