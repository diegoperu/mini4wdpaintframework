# P010 — Final Checklist Prompt

**SDK Version:** 2.4.0
**Page ID:** P010
**Prompt File:** `PromptEngine/FinalChecklist.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C015`, `Core/DEFINITION_OF_DONE.md`

---

## Purpose

Generate the final quality checklist page. This is the last page of the manual. Its purpose is to help the reader verify their completed model against the intended paint scheme before assembly. It also provides storage and care instructions to preserve the paint job.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{paintScheme.name}}` | `paintScheme.name` | Scheme name | `Violet Phantom` |
| `{{project.version}}` | `project.version` | Manual version | `1.0.0` |
| `{{project.author}}` | `project.author` | Manual author | `Studio Mini4WD` |
| `{{paintScheme.colors}}` | `paintScheme.colors[]` | Colors for final verification | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the FINAL CHECKLIST page (P010) of a Mini4WD painting manual for "{{project.modelName}}".

This is the last page. The reader has completed the painting. This page guides a systematic final inspection and closes the manual with care instructions and manual metadata.

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):** Violet band #5B2D8E, 18mm. Left: "Mini4WD Manual". Right: "FINAL CHECK".
**FOOTER (C002):** Gray #E8E8E8, 12mm.
Left: "{{project.modelName}} — {{paintScheme.name}}" Source Sans Pro Regular 8pt #4A4A4A.
Center: "P010" Source Sans Pro Bold 8pt #5B2D8E.
Right: "Mini4WD Manual SDK v2.4.0" Source Sans Pro Regular 8pt #9B9B9B.

**PAGE TITLE (22mm from top):**
"Final Inspection Checklist" in Bebas Neue Bold 28pt #5B2D8E, left margin 18mm.
Subtitle: "Verify every item before reassembly." Source Sans Pro Regular 11pt #4A4A4A, 32mm from top.

**TWO-COLUMN LAYOUT (from 42mm to 200mm):**

Left column (18mm to 101mm): QUALITY INSPECTION

Section heading: "QUALITY CHECKS" Source Sans Pro SemiBold 10pt #5B2D8E uppercase, violet underline.

Checklist items — render each as a checkbox row:
Checkbox style: open square 12x12mm, border 1.5px #5B2D8E, border-radius 2px. Text to right: Source Sans Pro Regular 9pt #1A1A1A.

Paint Quality:
- [ ] Base coat fully opaque (no body color showing through)
- [ ] No runs, drips, or brush strokes visible from 30cm distance
- [ ] Finish consistent across all panels (no dull patches in gloss areas)
- [ ] Color matches reference: {{paintScheme.name}} scheme

For each color in {{paintScheme.colors}}:
- [ ] [color.name] applied correctly to [color intended area] — [color.paintCode]

Masking:
- [ ] Clean paint edges along all masked transitions (no bleed)
- [ ] No tape residue visible on any surface
- [ ] Masked areas fully covered by correct colors

Details:
- [ ] All detail areas painted per P007 guide
- [ ] Window surfaces clean and scratch-free
- [ ] Wheel rims and chassis painted as specified

Decals:
- [ ] All decals applied per P008 placement guide
- [ ] No decal lifting or edge peeling
- [ ] Decals fully sealed under clear top coat
- [ ] No air bubbles under decals

Top Coat:
- [ ] Top coat applied over entire body
- [ ] Top coat fully cured (24 hours minimum)
- [ ] Top coat finish (gloss/matte) matches scheme specification
- [ ] No clouding or fish-eye effects in clear coat

Right column (109mm to 192mm): CARE & STORAGE

Section heading: "CARE & STORAGE" Source Sans Pro SemiBold 10pt #5B2D8E uppercase, violet underline.

**CARE INSTRUCTIONS list (C015 style, compact):**
Icon: shield symbol or [S], 10pt #388E3C.
Body items (Source Sans Pro Regular 9pt #4A4A4A, bullet #388E3C 3px circle):
- Do not use solvents or alcohol-based cleaners on painted surfaces
- Clean with a dry or slightly damp lint-free microfiber cloth only
- Avoid prolonged exposure to direct sunlight (UV causes color shift)
- Store in a dust-free display case when not in use
- Do not apply adhesive labels directly onto painted surfaces
- Handle by chassis, not by body, to avoid fingerprints on paint

**STORAGE INSTRUCTIONS:**
- Wrap in acid-free tissue paper for long-term storage
- Keep at room temperature (15-25 degrees Celsius)
- Avoid high humidity storage (above 70% RH risks decal lifting)

**PHOTOGRAPHER'S TIPS C015:**
Notes box: background #F8F8F8, border 1px #E8E8E8, border-radius 3px, padding 8px.
Heading: "PHOTOGRAPHY TIPS" Source Sans Pro SemiBold 9pt #4A4A4A.
Body:
"For best photos: use a white sweep background, place two soft box lights at 45 degrees from front-left and front-right, shoot at model eye level with a 50mm equivalent lens, set aperture to f/8 for sharpness across the full model. Avoid direct flash — it flattens the finish and eliminates the depth of metallic and pearl paints."
Source Sans Pro Regular 9pt #4A4A4A.

**COMPLETION BADGE (center, 210mm from top):**
Badge rectangle: 120x32mm, background gradient from #5B2D8E to #3D1E60, border-radius 8px, centered horizontally.
Left: checkmark icon [V] 18pt #FFFFFF.
Center text: "SCHEME COMPLETE" Bebas Neue Bold 16pt #FFFFFF, letter-spacing 3px.
Sub-text: "{{paintScheme.name}}" Source Sans Pro Regular 9pt #8B5FBF (VioletLight), below main text.

**MANUAL METADATA (240mm from top, below badge):**
Gray section background #F8F8F8, full width minus margins, border-radius 3px, padding 8px.
Two-column metadata grid, Source Sans Pro Regular 8pt #9B9B9B:
Left: Manual Version: {{project.version}} | Author: {{project.author}} | Language: {{project.language}}
Right: SDK Version: 2.4.0 | Page Count: 10 | Scheme: {{paintScheme.name}}

**REQUIRED ELEMENTS:**
- Two-column layout: quality checklist (left) + care/storage (right)
- Checkbox for every paintScheme.colors[] entry
- Photography tips C015
- Completion badge
- Manual metadata section
- Footer with P010 and SDK version

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| Checkbox for every `paintScheme.colors[]` entry | QA-101 to QA-110 |
| Completion badge present | Prompt spec |
| Photography tips C015 present | `Core/COMPONENT_SYSTEM.md §C015` |
| Manual metadata complete | `Core/PDF_MASTER.md` |
| SDK version correct in footer | VERSION file |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P010_raw.md`

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine. This is the last page of every manual.*
