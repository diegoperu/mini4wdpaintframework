# Style Guide

This document is the technical specification for the visual design of all pages produced by the Mini4WD Manual SDK. It translates the principles in `DESIGN_LANGUAGE.md` into exact values. Every value listed here is authoritative.

Where a value is also a Design Token, the token name is noted. Token values must match this document. If they conflict, this document takes precedence and the token must be updated.

See also: `COLOR_SYSTEM.md` for extended color documentation, `COMPONENT_SYSTEM.md` for component dimensions.

---

## 1. Color Palette

All colors are documented in full in `COLOR_SYSTEM.md`. The values below are the working reference.

### 1.1 Primary Colors

| Token | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| `{{token.VioletPrimary}}` | VioletPrimary | `#5B2D8E` | 91, 45, 142 | Header band, side panel, primary borders |
| `{{token.VioletDark}}` | VioletDark | `#3D1E60` | 61, 30, 96 | Header text shadow, pressed states |
| `{{token.VioletLight}}` | VioletLight | `#8B5FBF` | 139, 95, 191 | Divider lines on violet background, hover states |

### 1.2 Neutral Colors

| Token | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| `{{token.White}}` | White | `#FFFFFF` | 255, 255, 255 | Page background (mandatory) |
| `{{token.OffWhite}}` | OffWhite | `#F8F8F8` | 248, 248, 248 | Table alternating rows, code block backgrounds |
| `{{token.LightGray}}` | LightGray | `#E8E8E8` | 232, 232, 232 | Dividers, borders on white |
| `{{token.MidGray}}` | MidGray | `#9B9B9B` | 155, 155, 155 | Secondary labels, captions |
| `{{token.DarkGray}}` | DarkGray | `#4A4A4A` | 74, 74, 74 | Secondary body text |
| `{{token.Black}}` | Black | `#1A1A1A` | 26, 26, 26 | Primary body text, headings |

### 1.3 Accent Colors

| Token | Name | Hex | RGB | Usage |
|---|---|---|---|---|
| `{{token.GoldAccent}}` | GoldAccent | `#C8A838` | 200, 168, 56 | Tips, premium markers, important callouts |
| `{{token.RedWarning}}` | RedWarning | `#D32F2F` | 211, 47, 47 | Warning boxes, error indicators |
| `{{token.GreenSuccess}}` | GreenSuccess | `#388E3C` | 56, 142, 60 | Checklist completion, success states |
| `{{token.BlueInfo}}` | BlueInfo | `#1976D2` | 25, 118, 210 | Informational notes, links |

---

## 2. Typography

### 2.1 Font Families

**Title Font (Display and H1)**
- Primary: `Bebas Neue`
- Fallback 1: `Impact`
- Fallback 2: `Arial Narrow Bold`
- CSS stack: `"Bebas Neue", Impact, "Arial Narrow", sans-serif`
- Token: `{{token.TitleFont}}`
- Usage: Cover title, page section headers only. Never body text.

**Body Font (H2 through Body)**
- Primary: `Source Sans Pro`
- Fallback 1: `Open Sans`
- Fallback 2: `Helvetica Neue`
- Fallback 3: `Arial`
- CSS stack: `"Source Sans Pro", "Open Sans", "Helvetica Neue", Arial, sans-serif`
- Token: `{{token.BodyFont}}`
- Usage: All body text, subheadings, captions, labels.

**Monospace Font (Codes and Part Numbers)**
- Primary: `JetBrains Mono`
- Fallback 1: `Courier New`
- Fallback 2: `monospace`
- CSS stack: `"JetBrains Mono", "Courier New", monospace`
- Token: `{{token.MonoFont}}`
- Usage: Paint codes (e.g., `TS-29`), part numbers, technical identifiers.

### 2.2 Type Scale

| Level | Size | Line Height | Weight | Font Family | Token |
|---|---|---|---|---|---|
| Display | 48pt | 1.1 | 400 (Regular) | TitleFont | `{{token.FontScaleDisplay}}` |
| H1 | 36pt | 1.2 | 400 | TitleFont | `{{token.FontScaleH1}}` |
| H2 | 28pt | 1.3 | 700 (Bold) | BodyFont | `{{token.FontScaleH2}}` |
| H3 | 22pt | 1.4 | 600 (SemiBold) | BodyFont | `{{token.FontScaleH3}}` |
| Body | 11pt | 1.6 | 400 | BodyFont | `{{token.FontScaleBody}}` |
| Caption | 9pt | 1.5 | 400 | BodyFont | `{{token.FontScaleCaption}}` |
| Label | 8pt | 1.4 | 600 | BodyFont | `{{token.FontScaleLabel}}` |

> 📝 **Note:** "pt" here refers to typographic points (1pt = 1/72 inch). For digital tools that use pixels, multiply by 1.333 to convert (e.g., 11pt ≈ 14.7px at 96dpi).

### 2.3 Text Color Assignments

| Context | Color | Hex |
|---|---|---|
| Body text on white | Black | `#1A1A1A` |
| Headers on white | Black | `#1A1A1A` |
| Text on VioletPrimary | White | `#FFFFFF` |
| Captions | MidGray | `#9B9B9B` |
| Part codes (mono) | VioletDark | `#3D1E60` |
| Warning text | RedWarning | `#D32F2F` |

---

## 3. Grid System

### 3.1 Page Formats

Two page formats are supported. Projects must specify one in `Templates/PDF_CONFIG.yaml`.

| Format | Dimensions | Token |
|---|---|---|
| A4 | 210 × 297 mm | `{{token.PageFormatA4}}` |
| US Letter | 216 × 279 mm | `{{token.PageFormatLetter}}` |

Both formats use the same relative margin and grid specifications. Absolute measurements are derived from the chosen format.

### 3.2 Page Margins

| Position | Value | Token |
|---|---|---|
| Top | 15mm | `{{token.PageMarginTop}}` |
| Bottom | 20mm | `{{token.PageMarginBottom}}` |
| Left (inner) | 18mm | `{{token.PageMarginLeft}}` |
| Right (outer) | 18mm | `{{token.PageMarginRight}}` |

> ⚠️ **Warning:** The header band (C001) is positioned at the top edge of the page, not at the margin. The 15mm top margin defines where content begins after the header. The footer (C002) is aligned to the bottom edge.

### 3.3 Column Grid

| Property | Value | Token |
|---|---|---|
| Total columns | 12 | `{{token.GridColumns}}` |
| Gutter width | 4mm | `{{token.ColumnGap}}` |
| Main content area | 8 columns | — |
| Side panel | 4 columns | — |

Column widths are derived from: `(page_width - left_margin - right_margin - (11 × gutter)) / 12`

For A4: `(210 - 18 - 18 - 44) / 12 = 10.8mm per column`

### 3.4 Content Zones

```
┌────────────────────────────────────────────────────┐
│  C001 HEADER  (full width, 18mm, VioletPrimary)   │
├──────────────────────────────┬─────────────────────┤
│                              │                     │
│   MAIN CONTENT AREA          │  SIDE PANEL         │
│   (8 columns)                │  (4 columns)        │
│                              │  VioletPrimary bg   │
│                              │                     │
│                              │                     │
│                              │                     │
│                              │                     │
├──────────────────────────────┴─────────────────────┤
│  C002 FOOTER  (full width, 12mm)                   │
└────────────────────────────────────────────────────┘
```

Not all pages use the side panel. See `PAGE_SYSTEM.md` for per-page layout.

---

## 4. Spacing Scale

All spacing values are multiples of 4px. Use only values from this scale for padding, margin, and gap.

| Step | Value | Token |
|---|---|---|
| xs | 4px / 1mm | `{{token.SpacingXS}}` |
| sm | 8px / 2mm | `{{token.SpacingSM}}` |
| md | 12px / 3mm | `{{token.SpacingMD}}` |
| lg | 16px / 4mm | `{{token.SpacingLG}}` |
| xl | 24px / 6mm | `{{token.SpacingXL}}` |
| 2xl | 32px / 8mm | `{{token.Spacing2XL}}` |
| 3xl | 48px / 12mm | `{{token.Spacing3XL}}` |
| 4xl | 64px / 16mm | `{{token.Spacing4XL}}` |
| 5xl | 96px / 24mm | `{{token.Spacing5XL}}` |

---

## 5. Component Styling Reference

Full component specifications are in `Core/COMPONENT_SYSTEM.md`. The values below are the visual summary.

| Component | Height | Background | Border |
|---|---|---|---|
| C001 Header | 18mm | VioletPrimary | None |
| C002 Footer | 12mm | White | LightGray top, 0.5pt |
| C003 Palette | Variable | White | LightGray, 1pt |
| C006 Callout | Variable | OffWhite | BlueInfo left, 4px |
| C008 Warning | Variable | White | RedWarning left, 4px |
| C009 Tips | Variable | White | GoldAccent left, 4px |
| C013 Step Number | 12mm × 12mm | VioletPrimary | None (circle) |
| C014 Time Box | 10mm × 18mm | OffWhite | LightGray, 1pt |

---

## 6. Shadows

Shadows are used only on floating elements (rendered car images, callout boxes that appear to lift off the page). They are never used on structural elements (header, footer, side panel).

| Level | Value | Token | Usage |
|---|---|---|---|
| Subtle | `0 1px 3px rgba(0,0,0,0.12)` | `{{token.ShadowSubtle}}` | Table cells, component borders |
| Medium | `0 4px 6px rgba(0,0,0,0.16)` | `{{token.ShadowMedium}}` | Renders on white, callout boxes |
| Strong | `0 8px 16px rgba(0,0,0,0.20)` | `{{token.ShadowStrong}}` | Cover render, featured elements |

---

## 7. Border Radius

| Context | Value | Token |
|---|---|---|
| Callout boxes, tip boxes | 4px | `{{token.BorderRadius}}` |
| Paint swatches | 2px | `{{token.BorderRadiusSwatch}}` |
| Step number circles | 50% (full circle) | — |
| All other elements | 0 (square) | — |

---

## 8. Image Guidelines

### 8.1 Render Images
- Minimum padding from any page edge: 8px (`{{token.ImagePadding}}`)
- Background: must be white (`#FFFFFF`) or transparent PNG
- Drop shadow: Medium or Strong depending on page context
- Renders must not be cropped tighter than 10% padding around the model

### 8.2 Reference Photography (in Assets/ReferenceModels/)
- Reference photos in the SDK are not used directly in manual pages
- When shown for guidance in documentation: desaturated 10%, contrast +5%
- Always labeled with "(Reference)" in the caption

### 8.3 Icons
- Size: 24×24px base (scalable)
- Color: matches component role (white on violet, gold on white, red for warnings)
- Format: SVG preferred, PNG fallback at 2× resolution
- No icon may be recolored outside its defined role
