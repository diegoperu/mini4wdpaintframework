# P001 — Cover Page Prompt

**SDK Version:** 2.4.0
**Page ID:** P001
**Prompt File:** `PromptEngine/Cover.md`
**Dependencies:** `PROJECT.yaml`, `Core/RENDER_GUIDE.md §2`, `Core/STYLE_GUIDE.md §1`, `Core/COMPONENT_SYSTEM.md §C001`, `Core/COMPONENT_SYSTEM.md §C002`

---

## Purpose

Generate the cover page of the Mini4WD painting manual. The cover is the reader's first visual contact with the manual and must establish the editorial identity immediately: clean, technical, precise, with strong typographic hierarchy and a high-quality render of the model.

The cover must feel like a professional Tamiya product catalog page — not a hobbyist document.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Official model name | `Proto Emperor` |
| `{{project.seriesName}}` | `project.seriesName` | Series or edition name | `Championship Series` |
| `{{paintScheme.name}}` | `paintScheme.name` | Paint scheme name | `Violet Phantom` |
| `{{paths.coverRenderPath}}` | `paths.coverRenderPath` | Path to approved cover render | `Images/cover_3q.png` |
| `{{project.year}}` | `project.year` | Production year | `2024` |
| `{{project.author}}` | `project.author` | Manual author name | `Studio Mini4WD` |

---

## Pre-Generation Checklist

Before running this prompt, verify:

- [ ] `paths.coverRenderPath` points to an approved render (see `Core/RENDER_GUIDE.md §7`)
- [ ] Cover render is 3/4 front-left angle (see `Core/RENDER_GUIDE.md §2`)
- [ ] Cover render resolution is minimum 2480x3508px (see `Core/RENDER_GUIDE.md §5`)
- [ ] Cover render has pure white background (White)
- [ ] All tokens above are substituted before sending the prompt

---

## Prompt Template

> Copy everything between the START and END markers. Substitute all tokens before use.

--- START PROMPT ---

You are a professional graphic designer generating the COVER PAGE (P001) of a Mini4WD painting manual. This is a printed A4 document following a precise design system. Your output is a detailed layout specification that describes every element, its position, dimensions, typography, and color. A designer will use your output to produce the final page.

**Document Specification:**
- Page size: A4 -- 210x297mm
- Resolution: 300 dpi
- Color mode: sRGB
- Background: pure white (White)

**COMPONENT C001 -- HEADER (top of page)**

Position: top edge, full width, height 18mm
Background: solid VioletPrimary
Left zone (from left margin, 18mm in): logotype "Mini4WD Manual" in Bebas Neue Bold, 16pt, color White, vertically centered
Right zone (from right margin, 18mm in): label "COVER" in Source Sans Pro SemiBold, 9pt, uppercase, color White, letter-spacing 2px, vertically centered
No dividers, no gradient, no shadow on header band.

**COMPONENT C002 -- FOOTER (bottom of page)**

Position: bottom edge, full width, height 12mm
Background: LightGray
Center: text "{{project.modelName}} Painting Manual  --  P001" in Source Sans Pro Regular, 8pt, color DarkGray, vertically centered
Right zone (from right margin, 18mm in): text "2024" in Source Sans Pro Regular, 8pt, color MidGray

**MAIN AREA (between header and footer)**

The main area spans from 18mm top (below header) to 285mm (above footer).
Background: pure white (White).

RENDER PLACEMENT:
- Load image from: {{paths.coverRenderPath}}
- Position: horizontally centered, vertically centered in main area
- Size: fill approximately 70% of page width, maintaining aspect ratio
- The model render must appear at a 3/4 front-left angle (as per RENDER_GUIDE section 2)
- The render background must be transparent or pure white -- no shadow below render

SERIES LABEL (text overlay, upper-left zone of main area):
- Position: left margin (18mm from left), 24mm from top edge (6mm below header bottom)
- Text: "{{project.seriesName}}"
- Font: Source Sans Pro Regular, 13pt
- Color: VioletLight
- Letter-spacing: 1px

MODEL NAME (text overlay, lower-center zone of main area):
- Position: horizontally centered, 242mm from top (approximately 40mm above footer)
- Text: "{{project.modelName}}"
- Font: Bebas Neue Bold, 52pt
- Color: VioletPrimary
- Letter-spacing: 3px

PAINT SCHEME NAME (text overlay, below model name):
- Position: horizontally centered, 258mm from top
- Text: "{{paintScheme.name}}"
- Font: Source Sans Pro Light Italic, 17pt
- Color: DarkGray

VIOLET ACCENT LINE (decorative, above model name):
- Position: horizontally centered, width 60mm, height 2px, at 238mm from top
- Color: VioletPrimary

REQUIRED ELEMENTS CHECKLIST -- verify all are present:
- C001 Header: full width, 18mm, solid VioletPrimary, "Mini4WD Manual" left, "COVER" right
- C002 Footer: full width, 12mm, LightGray, centered model name and page number
- Model render: white background, 3/4 front-left angle, centered
- Series label: VioletLight, 13pt, upper-left
- Model name: VioletPrimary, Bebas Neue 52pt, lower-center
- Paint scheme name: DarkGray, italic, below model name
- Violet accent line: 60mm wide, above model name

OUTPUT FORMAT:

Provide your response in two parts:

Part 1 -- Layout Summary: A narrative description (3-5 sentences) of the visual result as a reader would experience it.

Part 2 -- Element Specification Table:
List every element with: Element name, Position (mm from top-left), Size, Font, Color, Notes.
Do not leave any field empty.

--- END PROMPT ---

---

## Post-Generation Validation

After the AI produces output, verify against:

| Check | Reference |
|-------|-----------|
| All 7 required elements present | Prompt checklist above |
| Layout items QA-001 to QA-015 | `Core/QA_SYSTEM.md §Layout` |
| Typography QA-031 to QA-045 | `Core/QA_SYSTEM.md §Typography` |
| Render QA-016 to QA-030 | `Core/QA_SYSTEM.md §Rendering` |
| Page level Definition of Done | `Core/DEFINITION_OF_DONE.md §Page Level DoD` |

Save output to: `ApprovedAssets/Text/P001/content.yaml`
Save approved output to: `Assets/ApprovedManual/{{project.modelSlug}}/P001.png`

---

## Common Errors for P001

| Error | How to Detect | Fix |
|-------|--------------|-----|
| Gray background on render | Visual inspection | Regenerate render with white background |
| Missing series name label | Check element table | Add VioletLight text overlay |
| Model name in wrong font | Check font spec | Must be Bebas Neue, not Source Sans Pro |
| Header gradient instead of solid | Visual inspection | Replace with flat VioletPrimary |
| Page number missing in footer | Check C002 spec | Footer must contain "P001" |
| Render too small (<50% page width) | Measure in output | Scale render to 70% page width |

---

*Part of Mini4WD Manual SDK v2.4.0 -- PromptEngine. See `Core/PAGE_SYSTEM.md §P001` for page architecture specification.*
