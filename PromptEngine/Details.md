# P007 — Fine Details Prompt

**SDK Version:** 2.4.0
**Page ID:** P007
**Prompt File:** `PromptEngine/Details.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C005`, `Core/COMPONENT_SYSTEM.md §C009`, `Core/COMPONENT_SYSTEM.md §C012`, `Core/COMPONENT_SYSTEM.md §C015`

---

## Purpose

Generate the fine detail painting page. Details are what separate a good paint job from an excellent one. This page focuses on small areas — windows, cockpit, wheel rims, aerodynamic accents — that require precision brushwork and steady hands.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{detailAreas}}` | `detailAreas[]` | Detail area definitions | see PROJECT.yaml |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | Color definitions for cross-reference | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the FINE DETAILS page (P007) of a Mini4WD painting manual for "{{project.modelName}}".

This page covers all small areas requiring precision painting: windows, cockpit interior, wheel rims, chassis accents, aerodynamic details. Each area gets its own close-up zoom panel and step-by-step instructions.

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):** Violet band #5B2D8E, 18mm. Left: "Mini4WD Manual". Right: "DETAILS".
**FOOTER (C002):** Gray #E8E8E8, 12mm. Center: "{{project.modelName}} — Details  |  P007".

**PAGE TITLE (22mm from top):**
"Fine Detail Painting" in Bebas Neue Bold 28pt #5B2D8E, left margin 18mm.
Subtitle: "Use a size 000 brush. Work under good light. Thin paints to 50% with appropriate thinner." Source Sans Pro Regular 11pt #4A4A4A, 32mm from top.

**DETAIL PANELS GRID (from 42mm):**

Arrange detail areas in a 2-column grid.
Column width: 88mm each, gutter 14mm, margins 18mm.
Each panel height: approximately (available height) / ceil(count/2).

For each area in {{detailAreas}}, render a DETAIL PANEL:

DETAIL PANEL STRUCTURE:
- Panel border: 1px #E8E8E8, border-radius 4px, padding 8px
- Panel title bar: background #F5F0FA, padding 4px 8px, border-radius 3px 3px 0 0
  - Area ID pill: 20x14mm, background #5B2D8E, text = area.id Source Sans Pro SemiBold 8pt #FFFFFF
  - Area name: Source Sans Pro SemiBold 10pt #1A1A1A, right of ID pill, 6px gap
- Zoom image (C012): maximum width within panel, border 1.5px #5B2D8E, border-radius 3px
  - Label "ZOOM" in Source Sans Pro SemiBold 7pt #5B2D8E, top-right corner inside border
  - Content: close-up render of the detail area. If not available: [ZOOM PLACEHOLDER: {{area.name}}]
- Color reference row below image:
  - Color swatch: 12x8mm filled with color hex (from colorId cross-reference), border 1px #E8E8E8
  - Color code box (mini C011): 28mm, brand 6pt above code 8pt Bebas Neue #5B2D8E, violet border
  - Technique: Source Sans Pro Regular 8pt #4A4A4A
- Instructions: Source Sans Pro Regular 9pt #4A4A4A, line-height 1.5
  - If area.notes is set, include as the primary instruction text
  - If no notes, use this SDK default: "Apply with a dry size 000 brush using short, controlled strokes. Do not overload the brush. Two thin coats are better than one thick coat."

Detail areas from PROJECT.yaml:
{{detailAreas}}

Color reference for cross-referencing colorId values:
{{paintScheme.colors}}

**TIPS BOX C009 (after grid, before notes, full width):**
Gold-left-border box: border-left 4px #C8A838, background #FFFDF0, padding 10px.
Icon: [*] #C8A838.
Heading: "DETAIL PAINTING TIPS" Source Sans Pro Bold 9pt #C8A838.
Body:
"1. THIN YOUR PAINT: Detail paints should flow freely off a size 000 brush without globbing. Mix 1 part paint to 1 part appropriate thinner.
2. DRY THE BRUSH: Wipe excess paint on a paper towel before each stroke. The brush should look almost dry — this is the dry-brush technique.
3. LIGHT OVER DARK: Always apply lighter colors over darker ones. If you make a mistake on a light color over dark, you will need to repaint the dark base first.
4. STEADY YOUR HAND: Rest your painting hand wrist on a stable surface. Never paint freehand in the air for detail work.
5. MAGNIFICATION: Use a 10x loupe or magnifying glass to inspect your work. Errors invisible to the naked eye will show in photographs."
Source Sans Pro Regular 9pt #4A4A4A.

**NOTES BOX C015 (at bottom, if any model-specific notes exist):**
Light gray box: background #F8F8F8, border 1px #E8E8E8, border-radius 3px, padding 10px.
Heading: "MODEL-SPECIFIC NOTES" Source Sans Pro SemiBold 9pt #4A4A4A.
Body: free text from notes field in detailAreas, or: "No model-specific detail notes for this scheme."
Source Sans Pro Regular 9pt #4A4A4A.

**REQUIRED ELEMENTS:**
- Grid of detail panels, one per detailAreas[] entry
- Zoom C012 per panel
- Color reference per panel
- Tips box C009
- Notes box C015
- Footer with P007

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| Panel for every `detailAreas[]` entry | QA-061 |
| C012 zoom present in each panel | `Core/COMPONENT_SYSTEM.md §C012` |
| C009 tips box present | `Core/COMPONENT_SYSTEM.md §C009` |
| C015 notes box present | `Core/COMPONENT_SYSTEM.md §C015` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P007_raw.md`

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
