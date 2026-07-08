# P003 — Materials Page Prompt

**SDK Version:** 2.4.0
**Page ID:** P003
**Prompt File:** `PromptEngine/Materials.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C004`, `Core/COMPONENT_SYSTEM.md §C008`, `Core/COMPONENT_SYSTEM.md §C011`

---

## Purpose

Generate the complete materials and shopping list page. A reader who has never purchased hobby paints must be able to use this page to buy everything needed before starting. No ambiguity, no missing items.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | Full color array with brand/code | see PROJECT.yaml |
| `{{materials.tools}}` | `materials.tools[]` | Tool list | see PROJECT.yaml |
| `{{materials.consumables}}` | `materials.consumables[]` | Consumable supplies | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the MATERIALS page (P003) of a Mini4WD painting manual for "{{project.modelName}}".

This page is a complete shopping list and tool reference. It must be practical, scannable, and leave no room for guesswork.

**Page Layout: A4 (210x297mm), white background White**

**HEADER (C001):** Primary-color band TamiyaPrimary, 18mm. Left: "Mini4WD Manual". Right: "MATERIALS".
**FOOTER (C002):** Gray band LightGray, 12mm. Center: "{{project.modelName}} — Materials  |  P003".

**PAGE TITLE (below header, 22mm from top):**
"What You Will Need" in Bebas Neue Bold 28pt TamiyaPrimary, left margin 18mm.
Subtitle: "Complete shopping list for the {{paintScheme.name}} scheme" in Source Sans Pro Regular 11pt DarkGray, 32mm from top.

**TWO-COLUMN LAYOUT (from 40mm to 240mm):**

Left column (18mm to 101mm, width 83mm): PAINTS
Right column (109mm to 192mm, width 83mm): TOOLS & SUPPLIES
Gutter: 8mm

LEFT COLUMN — PAINTS:

Section heading: "PAINTS" in Source Sans Pro SemiBold 10pt TamiyaPrimary uppercase, with 2px primary-color underline spanning column width.

For each color in {{paintScheme.colors}}, render a Shopping List Row (C004):

Row height: 22mm
Row structure (left to right):
- Color swatch rectangle: 14x10mm, filled with color hex, border 1px LightGray, border-radius 2px
- Paint Code Box (C011): 36mm wide, primary-color border 1.5px TamiyaPrimary, border-radius 3px, brand 7pt MidGray above code 10pt Bebas Neue TamiyaPrimary
- Color name: Source Sans Pro SemiBold 9pt Black
- Finish tag: small pill badge, background #F5F0FA, text Source Sans Pro Regular 7pt TamiyaPrimary, border-radius 10px

Separate each row with a 1px LightGray hairline.

RIGHT COLUMN — TOOLS & SUPPLIES:

Section heading: "TOOLS & SUPPLIES" in Source Sans Pro SemiBold 10pt TamiyaPrimary uppercase, with 2px primary-color underline.

Sub-section "TOOLS" (icon: wrench glyph or [T]):
For each tool in {{materials.tools}}:
- Bullet: small filled circle TamiyaPrimary, 4px diameter
- Tool name: Source Sans Pro SemiBold 9pt Black
- Type tag: Source Sans Pro Regular 8pt MidGray in parentheses
- If optional: append "(optional)" in Source Sans Pro Italic 8pt MidGray
- Notes if present: Source Sans Pro Light 8pt DarkGray, indented 12px

Sub-section "CONSUMABLES" (icon: label glyph or [C]), after tool list:
For each consumable in {{materials.consumables}}:
- Bullet: open circle TamiyaPrimary, 4px diameter
- Name: Source Sans Pro SemiBold 9pt Black
- Specification: Source Sans Pro Regular 8pt DarkGray (e.g., "400 grit", "3mm width")
- If optional: append "(optional)"

**WARNING BOX C008 (at 244mm from top, full width minus margins):**
Red-left-border box: border-left 4px RedWarning, background #FFF8F8, border-radius 0 3px 3px 0, padding 10px.
Icon: warning triangle [!] in RedWarning, 14pt, left of text.
Heading: "SAFETY" in Source Sans Pro Bold 9pt RedWarning.
Body: "Always use paints in a well-ventilated area. Wear nitrile gloves when handling solvent-based paints and thinners. Keep away from open flames. Read all product safety data sheets before use." Source Sans Pro Regular 9pt DarkGray.

**REQUIRED ELEMENTS:**
- Paint list with code boxes for every color in paintScheme.colors
- Tool list from materials.tools
- Consumables list from materials.consumables
- Safety warning box (C008)
- Footer with P003

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| Every `paintScheme.colors[]` entry has a row in paint list | QA-061 |
| C011 code boxes formatted correctly | `Core/COMPONENT_SYSTEM.md §C011` |
| Safety warning C008 present | `Core/COMPONENT_SYSTEM.md §C008` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{Model}/{Variant}/ApprovedText/P003/content.yaml`
(where {Model} = PascalCase_Underscore model folder, {Variant} = PascalCase_Underscore variant folder derived from paintScheme.slug)

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
