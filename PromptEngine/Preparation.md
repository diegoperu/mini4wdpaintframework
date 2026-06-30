# P004 — Preparation Page Prompt

**SDK Version:** 2.1.0
**Page ID:** P004
**Prompt File:** `PromptEngine/Preparation.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C007`, `Core/COMPONENT_SYSTEM.md §C008`, `Core/COMPONENT_SYSTEM.md §C009`, `Core/COMPONENT_SYSTEM.md §C013`, `Core/COMPONENT_SYSTEM.md §C014`

---

## Purpose

Generate the surface preparation page. Preparation is the most critical phase of the painting process — poor preparation causes every defect. This page must communicate the sequence clearly and include all warnings about common mistakes.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{preparationSteps}}` | `preparationSteps[]` | Ordered preparation steps | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the PREPARATION page (P004) of a Mini4WD painting manual for "{{project.modelName}}".

Surface preparation determines the quality of the final result. Every step is mandatory. The layout must guide the reader through a clear numbered sequence with time estimates and warnings.

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):** Violet band #5B2D8E, 18mm. Left: "Mini4WD Manual". Right: "PREPARATION".
**FOOTER (C002):** Gray #E8E8E8, 12mm. Center: "{{project.modelName}} — Preparation  |  P004".

**PAGE TITLE (22mm from top):**
"Surface Preparation" in Bebas Neue Bold 28pt #5B2D8E, left margin 18mm.
Subtitle: "Follow every step in order. Do not skip." Source Sans Pro Regular 11pt #4A4A4A, 32mm from top.

**EXPLODED VIEW DIAGRAM (C007, right column 130mm to 192mm, 40mm to 140mm):**
A schematic diagram showing the body shell disassembled into its main components (body, chassis, wheels, windows). Each component labeled with a small arrow and Source Sans Pro Regular 8pt #4A4A4A label. Lines from labels use #9B9B9B. Background: white. Note: if render not available, describe as [EXPLODED VIEW PLACEHOLDER].

**PREPARATION STEPS (left column 18mm to 120mm, from 40mm):**

For each step in {{preparationSteps}}, render:

STEP BLOCK:
- Step Number (C013): circle 18x18mm, background #5B2D8E, text = step number in Bebas Neue Bold 14pt #FFFFFF, centered. Position: left edge of column.
- Title: Source Sans Pro Bold 11pt #1A1A1A, 24mm from left, vertically aligned with step circle center.
- Time Box (C014): small pill shape, background #F5F0FA, border 1px #5B2D8E, border-radius 10px, padding 3px 8px. Text: duration value from step.durationSeconds formatted as "~X min" in Source Sans Pro Regular 8pt #5B2D8E. Position: right of title, same baseline.
- Description: Source Sans Pro Regular 10pt #4A4A4A, 24mm from left, below title, line-height 1.5.
- Warning (if step.warning is set): inline C008 mini — left border 3px #D32F2F, background #FFF8F8, text Source Sans Pro Italic 9pt #D32F2F. Immediately below description.
- Tip (if step.tip is set): inline C009 mini — left border 3px #C8A838, background #FFFDF0, text Source Sans Pro Italic 9pt #4A4A4A. Immediately below warning or description.
- Separator: 1px #E8E8E8 horizontal rule, full column width, below tip/warning, 8px margin above next step.

Preparation steps from PROJECT.yaml:
{{preparationSteps}}

**TIPS BOX C009 (below step list, before footer, full width minus margins):**
Gold-left-border box: border-left 4px #C8A838, background #FFFDF0, border-radius 0 3px 3px 0, padding 10px.
Icon: lightbulb [*] in #C8A838, 14pt.
Heading: "PRO TIPS" Source Sans Pro Bold 9pt #C8A838.
Body (these are SDK-standard tips, always include):
"1. Wash the body with mild dish soap and warm water before any sanding. Fingerprints contain oils that prevent paint adhesion.
2. Let the body dry completely (minimum 2 hours) before applying primer.
3. Sand in one direction only — never circular motions on visible surfaces.
4. Wipe down with a tack cloth immediately before priming. Any dust will be sealed in."
Source Sans Pro Regular 9pt #4A4A4A.

**REQUIRED ELEMENTS:**
- Numbered steps from preparationSteps[] with C013 step circles
- Time estimates C014 per step
- Exploded view diagram C007 (right column)
- Per-step warnings C008 where step.warning is set
- Per-step tips C009 where step.tip is set
- Pro tips box C009 at bottom
- Footer with P004

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| All `preparationSteps[]` rendered | QA-061 |
| Step numbers use C013 circle style | `Core/COMPONENT_SYSTEM.md §C013` |
| Time boxes present where duration specified | `Core/COMPONENT_SYSTEM.md §C014` |
| Exploded view C007 present | `Core/COMPONENT_SYSTEM.md §C007` |
| Pro tips C009 at bottom | `Core/COMPONENT_SYSTEM.md §C009` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P004_raw.md`

---

*Part of Mini4WD Manual SDK v2.1.0 — PromptEngine.*
