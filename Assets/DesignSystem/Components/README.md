# Assets/DesignSystem/Components/

**Version:** 2.1.0
**Authoritative spec:** Core/COMPONENT_SYSTEM.md
**Token source:** Assets/DesignSystem/Tokens/tokens.example.yaml

---

## Purpose

This directory contains visual wireframe specifications, dimension tables, and token-reference summaries for all SDK components (C001–C015). It is the **practitioner's quick reference** for building pages.

The **authoritative** component specification is `Core/COMPONENT_SYSTEM.md`. When this directory and `COMPONENT_SYSTEM.md` conflict, `COMPONENT_SYSTEM.md` wins. File a correction issue to keep them synchronized.

---

## What Belongs Here

- ASCII wireframe diagrams for each component
- Dimension tables (width, height, padding, margins)
- Token reference tables listing every token a component uses
- Variant diagrams (e.g., C001 Standard vs C001 Cover variant)
- Layout integration examples (how components nest within page layouts)

## What Does Not Belong Here

- Authoritative specs (those live in Core/COMPONENT_SYSTEM.md)
- Actual image files (renders, icons) — those live in other Assets/ subdirectories
- Page assembly instructions (those live in Core/PAGE_SYSTEM.md)

---

## Component Index

| ID | Component | Page(s) |
|----|-----------|---------|
| C001 | Header | All pages |
| C002 | Footer | All pages |
| C003 | Palette | P002 Color Scheme |
| C004 | Shopping List | P003 Materials |
| C005 | Paint Sequence | P005 Painting |
| C006 | Callout | P004, P005, P006, P007, P008 |
| C007 | Exploded View | P004 Preparation |
| C008 | Warning | P004, P005, P006, P008 |
| C009 | Tips | P004, P005, P006, P007, P008 |
| C010 | Paint Legend | P002 Color Scheme |
| C011 | Paint Code Box | P002, P003, P005 |
| C012 | Zoom | P006, P007, P008 |
| C013 | Step Number | P004, P005, P006, P007, P008 |
| C014 | Time Box | P004, P005 |
| C015 | Notes | P007, P008, P009, P010 |

---

## ASCII Wireframe Convention

All wireframes in this directory use the following ASCII box-drawing characters:

```
┌ ─ ┐   Top border
│   │   Side borders
└ ─ ┘   Bottom border
├ ─ ┤   Internal horizontal divider
│   │   Internal vertical divider (same as sides)
←───→   Dimension annotation
↑       Height annotation start
↓       Height annotation end
```

Token references in wireframes use `{{token.Name}}` notation.

---

## Component Wireframes

### C001 — Header

```
←──────────────────── Page width ({{token.PageWidth}}) ───────────────────→
┌──────────────────────────────────────────────────────────────────────────┐ ↑
│                                                                          │ {{token.HeaderHeight}}
│  [LOGO]  Mini4WD Manual           [Series Name]            [PAGE LABEL] │ (18mm)
│  20×20mm  TitleFont 14pt White     H3 White (optional)     Label 8pt    │ ↓
└──────────────────────────────────────────────────────────────────────────┘
Background: {{token.VioletPrimary}}
Text color: {{token.White}}

VARIANT — Cover (P001):
┌──────────────────────────────────────────────────────────────────────────┐
│  [LOGO]  Mini4WD Manual                                        [COVER]  │
│          Full-bleed variant — right label shows "COVER" only            │
└──────────────────────────────────────────────────────────────────────────┘
```

**Tokens used:**
| Property | Token |
|----------|-------|
| Background | `{{token.VioletPrimary}}` |
| Height | `{{token.HeaderHeight}}` |
| Text color | `{{token.White}}` |
| Logo typeface | `{{token.TitleFont}}` |
| Page label size | `{{token.LabelSize}}` |
| Left padding | `{{token.L}}` (16px) |
| Right padding | `{{token.L}}` (16px) |

---

### C002 — Footer

```
←──────────────────── Page width ({{token.PageWidth}}) ───────────────────→
┌──────────────────────────────────────────────────────────────────────────┐ ↑
│  [Model Name] Painting Manual                      P001 · SDK v2.1.0   │ {{token.FooterHeight}}
│  Caption 9pt {{token.MidGray}}                     Label 8pt right      │ (12mm)
└──────────────────────────────────────────────────────────────────────────┘
Background: {{token.LightGray}} (top border 1px {{token.MidGray}})
```

**Tokens used:** `{{token.FooterHeight}}`, `{{token.LightGray}}`, `{{token.MidGray}}`, `{{token.CaptionSize}}`, `{{token.LabelSize}}`

---

### C006 — Callout (Informational)

```
←──────────── Content column width ───────────────────────────────────────→
┌ {{token.CalloutBorder}} 4px left-border ─────────────────────────────────┐
│                                                                          │
│  ℹ  CALLOUT TITLE                                                        │
│     H4 {{token.VioletPrimary}} 16pt                                      │
│                                                                          │
│     Callout body text. Explains a technique, material choice,            │
│     or design decision relevant to the current step.                     │
│     BodyFont {{token.BodySize}} {{token.DarkGray}}                       │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
Background: {{token.CalloutBackground}}
Border: 4px left solid {{token.CalloutBorder}}
Border radius: {{token.BorderRadius}}
Padding: {{token.XL}} (24px) all sides
```

---

### C008 — Warning

```
┌ {{token.WarningColor}} 4px left-border ──────────────────────────────────┐
│                                                                          │
│  ⚠  WARNING TITLE                                                        │
│     H4 {{token.RedWarning}} 16pt bold                                    │
│                                                                          │
│     Warning text. Describes a safety risk, irreversible step,            │
│     or common mistake that damages the model or finish.                  │
│     BodyFont {{token.BodySize}} {{token.DarkGray}}                       │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
Background: {{token.RedWarningLight}}
Border: 4px left solid {{token.RedWarning}}
```

---

### C009 — Tips

```
┌ {{token.GoldAccent}} 4px left-border ────────────────────────────────────┐
│                                                                          │
│  ★  PRO TIP                                                              │
│     H4 {{token.GoldAccent}} 16pt                                         │
│                                                                          │
│     Tip text. Shares a professional technique, shortcut, or              │
│     quality-enhancing practice for the current step.                     │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
Background: {{token.GoldLight}}
Border: 4px left solid {{token.GoldAccent}}
```

---

### C013 — Step Number

```
  ╔═══╗
  ║ 1 ║  ← Circle/square badge
  ╚═══╝
  Background: {{token.VioletPrimary}}
  Text: {{token.White}}, TitleFont, 22pt
  Size: 32×32px (minimum)
```

---

### C014 — Time Box

```
  ┌───────────┐
  │  ⏱ 30min │  ← Inline time estimate
  └───────────┘
  Background: {{token.VioletUltraLight}}
  Border: 1px {{token.VioletLight}}
  Text: {{token.VioletPrimary}}, BodyFont 11pt
```

---

### C011 — Paint Code Box

```
  ┌─────────────────────────┐
  │  ██  TS-57              │  ← Color swatch + code
  │      Blue Violet        │
  │      Tamiya / Gloss     │
  └─────────────────────────┘
  Swatch: 24×24px, actual paint color
  Code: MonoFont {{token.MonoFont}} 11pt {{token.Black}}
  Name: BodyFont 9pt {{token.DarkGray}}
  Brand: Caption 9pt {{token.MidGray}}
  Background: {{token.White}}
  Border: 1px {{token.LightGray}}
```

---

## Adding New Components

1. Reserve an ID in `Core/COMPONENT_SYSTEM.md` — IDs are assigned sequentially (C016, C017, ...)
2. Document the full spec in `Core/COMPONENT_SYSTEM.md` before creating the wireframe here
3. Add the wireframe to this README under a new `### C0XX — Name` section
4. Update the Component Index table above
5. Update `Core/PAGE_SYSTEM.md` for any pages that use the new component
6. Add entry to `CHANGELOG.md`
