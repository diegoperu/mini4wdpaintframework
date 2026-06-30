# P002 — Color Scheme Prompt

**SDK Version:** 2.1.0
**Page ID:** P002
**Prompt File:** `PromptEngine/ColorScheme.md`
**Dependencies:** `PROJECT.yaml`, `Core/COLOR_SYSTEM.md`, `Core/COMPONENT_SYSTEM.md §C003`, `Core/COMPONENT_SYSTEM.md §C010`, `Core/COMPONENT_SYSTEM.md §C011`, `Core/RENDER_GUIDE.md §2`

---

## Purpose

Generate the color scheme overview page. This page provides the reader with a complete technical map of the model's paint scheme: which colors go where, in what finish, and with which products. The three-view orthographic render is mandatory — it gives spatial context that no written description can replace.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{paintScheme.name}}` | `paintScheme.name` | Scheme name | `Violet Phantom` |
| `{{paintScheme.description}}` | `paintScheme.description` | Scheme description | `A deep violet body with silver trim` |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | Full color array | see PROJECT.yaml |
| `{{paintScheme.colorNotes}}` | `paintScheme.colorNotes` | General notes | `Apply metallic in one direction` |
| `{{paths.colorSchemeRenderFront}}` | `paths.colorSchemeRenderFront` | Front view render path | `Images/P002_front.png` |
| `{{paths.colorSchemeRenderSide}}` | `paths.colorSchemeRenderSide` | Side view render path | `Images/P002_side.png` |
| `{{paths.colorSchemeRenderTop}}` | `paths.colorSchemeRenderTop` | Top view render path | `Images/P002_top.png` |

---

## Prompt Template

--- START PROMPT ---

You are generating the COLOR SCHEME page (P002) of a Mini4WD painting manual for the model "{{project.modelName}}". This page presents the complete paint scheme "{{paintScheme.name}}" through orthographic renders and a technical color legend.

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):**
Full-width violet band (#5B2D8E), 18mm height.
Left: "Mini4WD Manual" Bebas Neue 16pt white.
Right: "COLOR SCHEME" Source Sans Pro SemiBold 9pt uppercase white.

**FOOTER (C002):**
Full-width light gray band (#E8E8E8), 12mm height.
Center: "{{project.modelName}} — Color Scheme  |  P002" Source Sans Pro 8pt #4A4A4A.

**THREE-VIEW RENDERS (main upper area, from 22mm to 165mm top):**

Divide the main area horizontally into three equal columns (each ~63mm wide, 4mm gutter).

Left column — FRONT VIEW:
- Image: {{paths.colorSchemeRenderFront}}
- Label below image: "FRONT" in Source Sans Pro SemiBold 8pt uppercase #5B2D8E, centered
- Orthographic projection, no perspective

Center column — SIDE VIEW:
- Image: {{paths.colorSchemeRenderSide}}
- Label below image: "SIDE" in Source Sans Pro SemiBold 8pt uppercase #5B2D8E, centered
- Orthographic projection, no perspective

Right column — TOP VIEW:
- Image: {{paths.colorSchemeRenderTop}}
- Label below image: "TOP" in Source Sans Pro SemiBold 8pt uppercase #5B2D8E, centered
- Orthographic projection, no perspective

All renders: white background, no shadows, equal scale.

**SECTION DIVIDER (at 168mm from top):**
Full-width horizontal rule, 1px, color #E8E8E8.
Label: "PAINT LEGEND" in Source Sans Pro SemiBold 9pt #5B2D8E, uppercase, left-aligned at 18mm, 172mm from top.

**COLOR LEGEND TABLE (C010 + C011, from 178mm to 272mm):**

For each color in the paint scheme, render one row with these columns:

| Swatch | Code Box | Color Name | Finish | Area | Notes |
|--------|----------|------------|--------|------|-------|

SWATCH (C003): Filled rectangle 18x12mm, background = the color's hex value, border 1px #E8E8E8, border-radius 2px.

CODE BOX (C011): Rectangle with violet border (#5B2D8E, 1.5px), border-radius 3px, padding 4px. Inside: brand name in 7pt #9B9B9B above the product code in 10pt Bebas Neue #5B2D8E. Width 36mm.

COLOR NAME: Source Sans Pro SemiBold 10pt #1A1A1A.

FINISH: Source Sans Pro Regular 9pt #4A4A4A. Values: Gloss / Matte / Satin / Metallic / Pearl / Flat.

AREA: Source Sans Pro Regular 9pt #4A4A4A. Brief description of where this color is applied.

NOTES: Source Sans Pro Light Italic 8pt #9B9B9B. Optional technical note.

Paint colors to render (from PROJECT.yaml paintScheme.colors):
{{paintScheme.colors}}

**CALLOUT C006 (if colorNotes is non-empty, at 274mm from top):**
Violet-left-border callout box (border 3px #5B2D8E, background #F5F0FA, border-radius 3px, padding 8px).
Heading: "NOTE" Source Sans Pro SemiBold 9pt #5B2D8E.
Body: "{{paintScheme.colorNotes}}" Source Sans Pro Regular 9pt #4A4A4A.

**REQUIRED ELEMENTS:**
- Three renders (front, side, top) with labels
- Full color legend with one row per color
- Code boxes with brand and product code for each color
- Footer with P002 page number

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| Three render panels present and labeled | Prompt spec above |
| Color legend has one row per `paintScheme.colors[]` entry | QA-061 to QA-070 |
| Paint code boxes formatted per C011 spec | `Core/COMPONENT_SYSTEM.md §C011` |
| All colors reference `Core/COLOR_SYSTEM.md` design tokens | QA-046 to QA-060 |
| Page level DoD | `Core/DEFINITION_OF_DONE.md §Page Level DoD` |

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P002_raw.md`

---

*Part of Mini4WD Manual SDK v2.1.0 — PromptEngine.*
