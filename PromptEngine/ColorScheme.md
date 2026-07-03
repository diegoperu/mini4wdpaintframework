# P002 — Color Scheme Prompt

**SDK Version:** 2.4.0
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

**Page Layout: A4 (210x297mm), white background White**

**HEADER (C001):**
Full-width violet band (VioletPrimary), 18mm height.
Left: "Mini4WD Manual" Bebas Neue 16pt white.
Right: "COLOR SCHEME" Source Sans Pro SemiBold 9pt uppercase white.

**FOOTER (C002):**
Full-width light gray band (LightGray), 12mm height.
Center: "{{project.modelName}} — Color Scheme  |  P002" Source Sans Pro 8pt DarkGray.

**THREE-VIEW RENDERS (main upper area, from 22mm to 165mm top):**

Divide the main area horizontally into three equal columns (each ~63mm wide, 4mm gutter).

Left column — FRONT VIEW:
- Image: {{paths.colorSchemeRenderFront}}
- Label below image: "FRONT" in Source Sans Pro SemiBold 8pt uppercase VioletPrimary, centered
- Orthographic projection, no perspective

Center column — SIDE VIEW:
- Image: {{paths.colorSchemeRenderSide}}
- Label below image: "SIDE" in Source Sans Pro SemiBold 8pt uppercase VioletPrimary, centered
- Orthographic projection, no perspective

Right column — TOP VIEW:
- Image: {{paths.colorSchemeRenderTop}}
- Label below image: "TOP" in Source Sans Pro SemiBold 8pt uppercase VioletPrimary, centered
- Orthographic projection, no perspective

All renders: white background, no shadows, equal scale.

**SECTION DIVIDER (at 168mm from top):**
Full-width horizontal rule, 1px, color LightGray.
Label: "PAINT LEGEND" in Source Sans Pro SemiBold 9pt VioletPrimary, uppercase, left-aligned at 18mm, 172mm from top.

**COLOR LEGEND TABLE (C010 + C011, from 178mm to 272mm):**

For each color in the paint scheme, render one row with these columns:

| Swatch | Code Box | Color Name | Finish | Area | Notes |
|--------|----------|------------|--------|------|-------|

SWATCH (C003): Filled rectangle 18x12mm, background = the color's hex value, border 1px LightGray, border-radius 2px.

CODE BOX (C011): Rectangle with violet border (VioletPrimary, 1.5px), border-radius 3px, padding 4px. Inside: brand name in 7pt MidGray above the product code in 10pt Bebas Neue VioletPrimary. Width 36mm.

COLOR NAME: Source Sans Pro SemiBold 10pt Black.

FINISH: Source Sans Pro Regular 9pt DarkGray. Values: Gloss / Matte / Satin / Metallic / Pearl / Flat.

AREA: Source Sans Pro Regular 9pt DarkGray. Brief description of where this color is applied.

NOTES: Source Sans Pro Light Italic 8pt MidGray. Optional technical note.

Paint colors to render (from PROJECT.yaml paintScheme.colors):
{{paintScheme.colors}}

**CALLOUT C006 (if colorNotes is non-empty, at 274mm from top):**
Violet-left-border callout box (border 3px VioletPrimary, background #F5F0FA, border-radius 3px, padding 8px).
Heading: "NOTE" Source Sans Pro SemiBold 9pt VioletPrimary.
Body: "{{paintScheme.colorNotes}}" Source Sans Pro Regular 9pt DarkGray.

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

Save output to: `Projects/{Model}/{Variant}/ApprovedText/P002/content.yaml`
(where {Model} = PascalCase_Underscore model folder, {Variant} = PascalCase_Underscore variant folder derived from paintScheme.slug)

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
