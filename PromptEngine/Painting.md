# P005 — Painting Sequence Prompt

**SDK Version:** 2.4.0
**Page ID:** P005
**Prompt File:** `PromptEngine/Painting.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C005`, `Core/COMPONENT_SYSTEM.md §C008`, `Core/COMPONENT_SYSTEM.md §C011`, `Core/COMPONENT_SYSTEM.md §C013`, `Core/COMPONENT_SYSTEM.md §C014`

---

## Purpose

Generate the paint application sequence page. The sequence must be presented in exact order — primer first, then base coats, secondary colors, metallics, and details. Drying time warnings are mandatory between coats.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | Color definitions | see PROJECT.yaml |
| `{{paintSequence}}` | `paintSequence[]` | Ordered paint steps | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the PAINTING SEQUENCE page (P005) of a Mini4WD painting manual for "{{project.modelName}}".

The paint sequence is the technical heart of the manual. Every step must specify: what color, what area, what technique, how many coats, and how long to wait. The reader must never be uncertain about what comes next.

**Page Layout: A4 (210x297mm), white background White**

**HEADER (C001):** Violet band VioletPrimary, 18mm. Left: "Mini4WD Manual". Right: "PAINTING".
**FOOTER (C002):** LightGray, 12mm. Center: "{{project.modelName}} — Painting  |  P005".

**PAGE TITLE (22mm from top):**
"Paint Application Sequence" in Bebas Neue Bold 28pt VioletPrimary, left margin 18mm.
Subtitle: "Apply in the exact order shown. Respect all drying times." Source Sans Pro Regular 11pt DarkGray, 32mm from top.

**PAINT SEQUENCE TIMELINE (C005, full width minus margins, from 42mm):**

The sequence is rendered as a vertical timeline. A thin 2px vertical line in LightGray runs down the center-left (at 30mm from left margin), connecting all steps.

For each step in {{paintSequence}}, render a SEQUENCE BLOCK:

SEQUENCE BLOCK STRUCTURE:
- Step Number (C013): circle 20x20mm, background VioletPrimary. If step.colorId refers to a color, use that color's hex as background instead of violet. Text = step number in Bebas Neue Bold 14pt White. Centered on the timeline line.
- Color Swatch: 16x10mm rectangle filled with the step's color hex, border 1px LightGray, border-radius 2px. 8mm to the right of the step circle.
- Paint Code Box (C011): 38mm wide. Brand 7pt MidGray above code 10pt Bebas Neue VioletPrimary. Violet border 1.5px. 8mm to the right of swatch.
- Area Label: "Area:" Source Sans Pro Regular 8pt MidGray + area value Source Sans Pro SemiBold 9pt Black. Right of code box.
- Technique Badge: pill shape, background #F5F0FA, border 1px VioletLight, text Source Sans Pro Regular 8pt VioletPrimary. Values: Brush / Airbrush / Spray Can.
- Coats: "x{{coats}} coats" Source Sans Pro SemiBold 9pt Black. Right of technique badge.
- Time Box (C014): pill shape, background #F5F0FA, border 1px VioletPrimary. "{{dryingTime}}" Source Sans Pro Regular 8pt VioletPrimary. Aligned right of block.
- Notes (if set): Source Sans Pro Light Italic 8pt DarkGray, below the main row, indented to color swatch position.

DRYING TIME WARNING (C008) between steps where dryingTime is specified:
Compact inline warning: icon [!] RedWarning + "Wait {{dryingTime}} before proceeding to next step." Source Sans Pro Italic 9pt RedWarning. Background #FFF8F8, border-left 3px RedWarning, padding 4px 8px. Full width minus margins.

Paint sequence from PROJECT.yaml:
{{paintSequence}}

Available colors for reference:
{{paintScheme.colors}}

**GENERAL DRYING WARNING (C008, full width, after last step):**
Border-left 4px RedWarning, background #FFF8F8, padding 10px.
Icon: [!] 14pt RedWarning.
Heading: "CRITICAL: DRYING TIMES" Source Sans Pro Bold 9pt RedWarning.
Body: "Never apply the next coat before the previous one is fully dry to touch. Applying over wet paint causes wrinkling, lifting, and surface defects that cannot be corrected without stripping and restarting. When in doubt, wait longer." Source Sans Pro Regular 9pt DarkGray.

**REQUIRED ELEMENTS:**
- All steps from paintSequence[] in order
- C013 step circles with color-matched backgrounds
- C011 code boxes per step
- C014 time boxes where dryingTime is specified
- C008 inline drying warnings between steps
- C008 general drying time warning at bottom
- Footer with P005

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| Steps match `paintSequence[]` order exactly | QA-061 |
| Step circles color-coded per step color | `Core/COMPONENT_SYSTEM.md §C013` |
| Drying time warnings between every step with dryingTime | QA-071 to QA-080 |
| Code boxes formatted correctly | `Core/COMPONENT_SYSTEM.md §C011` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{Model}/{Variant}/ApprovedText/P005/content.yaml`
(where {Model} = PascalCase_Underscore model folder, {Variant} = PascalCase_Underscore variant folder derived from paintScheme.slug)

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
