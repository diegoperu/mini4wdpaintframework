# P003 — Materials Page Prompt

**SDK Version:** 2.1.0
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

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):** Violet band #5B2D8E, 18mm. Left: "Mini4WD Manual". Right: "MATERIALS".
**FOOTER (C002):** Gray band #E8E8E8, 12mm. Center: "{{project.modelName}} — Materials  |  P003".

**PAGE TITLE (below header, 22mm from top):**
"What You Will Need" in Bebas Neue Bold 28pt #5B2D8E, left margin 18mm.
Subtitle: "Complete shopping list for the {{paintScheme.name}} scheme" in Source Sans Pro Regular 11pt #4A4A4A, 32mm from top.

**TWO-COLUMN LAYOUT (from 40mm to 240mm):**

Left column (18mm to 101mm, width 83mm): PAINTS
Right column (109mm to 192mm, width 83mm): TOOLS & SUPPLIES
Gutter: 8mm

LEFT COLUMN — PAINTS:

Section heading: "PAINTS" in Source Sans Pro SemiBold 10pt #5B2D8E uppercase, with 2px violet underline spanning column width.

For each color in {{paintScheme.colors}}, render a Shopping List Row (C004):

Row height: 22mm
Row structure (left to right):
- Color swatch rectangle: 14x10mm, filled with color hex, border 1px #E8E8E8, border-radius 2px
- Paint Code Box (C011): 36mm wide, violet border 1.5px #5B2D8E, border-radius 3px, brand 7pt #9B9B9B above code 10pt Bebas Neue #5B2D8E
- Color name: Source Sans Pro SemiBold 9pt #1A1A1A
- Finish tag: small pill badge, background #F5F0FA, text Source Sans Pro Regular 7pt #5B2D8E, border-radius 10px

Separate each row with a 1px #E8E8E8 hairline.

RIGHT COLUMN — TOOLS & SUPPLIES:

Section heading: "TOOLS & SUPPLIES" in Source Sans Pro SemiBold 10pt #5B2D8E uppercase, with 2px violet underline.

Sub-section "TOOLS" (icon: wrench glyph or [T]):
For each tool in {{materials.tools}}:
- Bullet: small filled circle #5B2D8E, 4px diameter
- Tool name: Source Sans Pro SemiBold 9pt #1A1A1A
- Type tag: Source Sans Pro Regular 8pt #9B9B9B in parentheses
- If optional: append "(optional)" in Source Sans Pro Italic 8pt #9B9B9B
- Notes if present: Source Sans Pro Light 8pt #4A4A4A, indented 12px

Sub-section "CONSUMABLES" (icon: label glyph or [C]), after tool list:
For each consumable in {{materials.consumables}}:
- Bullet: open circle #5B2D8E, 4px diameter
- Name: Source Sans Pro SemiBold 9pt #1A1A1A
- Specification: Source Sans Pro Regular 8pt #4A4A4A (e.g., "400 grit", "3mm width")
- If optional: append "(optional)"

**WARNING BOX C008 (at 244mm from top, full width minus margins):**
Red-left-border box: border-left 4px #D32F2F, background #FFF8F8, border-radius 0 3px 3px 0, padding 10px.
Icon: warning triangle [!] in #D32F2F, 14pt, left of text.
Heading: "SAFETY" in Source Sans Pro Bold 9pt #D32F2F.
Body: "Always use paints in a well-ventilated area. Wear nitrile gloves when handling solvent-based paints and thinners. Keep away from open flames. Read all product safety data sheets before use." Source Sans Pro Regular 9pt #4A4A4A.

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

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P003_raw.md`

---

*Part of Mini4WD Manual SDK v2.1.0 — PromptEngine.*
