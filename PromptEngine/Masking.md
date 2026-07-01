# P006 — Masking Technique Prompt

**SDK Version:** 2.4.0
**Page ID:** P006
**Prompt File:** `PromptEngine/Masking.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C006`, `Core/COMPONENT_SYSTEM.md §C008`, `Core/COMPONENT_SYSTEM.md §C012`, `Core/COMPONENT_SYSTEM.md §C013`

---

## Purpose

Generate the masking technique guide. Masking is the step most commonly performed incorrectly by beginners. This page must provide annotated views showing exactly which areas to mask, in what sequence, and with what materials.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{maskingZones}}` | `maskingZones[]` | Masking zone definitions | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the MASKING page (P006) of a Mini4WD painting manual for "{{project.modelName}}".

This page must show: which areas to mask, in what order, and with what technique. Masking is sequence-critical — wrong order causes paint to bleed under tape or lift the previous layer. The annotated render is the core visual.

**Page Layout: A4 (210x297mm), white background #FFFFFF**

**HEADER (C001):** Violet band #5B2D8E, 18mm. Left: "Mini4WD Manual". Right: "MASKING".
**FOOTER (C002):** Gray #E8E8E8, 12mm. Center: "{{project.modelName}} — Masking  |  P006".

**PAGE TITLE (22mm from top):**
"Masking Guide" in Bebas Neue Bold 28pt #5B2D8E, left margin 18mm.
Subtitle: "Apply masks in numbered order to prevent bleed and lifting." Source Sans Pro Regular 11pt #4A4A4A, 32mm from top.

**ANNOTATED RENDER (upper area, 40mm to 155mm):**
Full-width annotated view of the model body showing all masking zones highlighted.

Annotation style:
- Masking zones: semi-transparent overlay fill in #C8A838 at 40% opacity over the zone area on the render
- Each zone labeled with a circle number: filled circle 16x16mm #C8A838, text = maskingOrder number in Bebas Neue Bold 11pt #FFFFFF
- Leader lines from circle numbers to zones: 1px dashed #C8A838
- Background of annotated render: white #FFFFFF
- Note: if render not available, describe as [MASKING ANNOTATED VIEW PLACEHOLDER - show body outline with numbered zones]

Place the annotated render centered, maximum width fitting between 18mm left margin and 192mm right margin.

**MASKING CALLOUT C006 (right side panel if space, or below render):**
Violet-left-border callout: border-left 3px #5B2D8E, background #F5F0FA, padding 8px.
Heading: "TAPE TYPES" Source Sans Pro SemiBold 9pt #5B2D8E.
Body:
- "Standard masking tape (18mm): for straight edges and flat areas"
- "Low-tack washi tape (6mm): for curves and delicate previously painted surfaces"
- "Liquid masking fluid: for irregular shapes and complex areas"
- "Pre-cut masks: for windows and precise geometric shapes"
Source Sans Pro Regular 9pt #4A4A4A, bullet list with #5B2D8E filled circles 3px.

**MASKING SEQUENCE TABLE (from 160mm):**
Section heading: "MASKING SEQUENCE" Source Sans Pro SemiBold 10pt #5B2D8E uppercase, with 2px violet underline.

Table columns: | Order | Zone | Masking Type | Instructions | Remove After |

For each zone in {{maskingZones}} (sorted by maskingOrder):

- Order: C013 step circle 16x16mm #C8A838 (gold, not violet, to distinguish masking from painting steps), Bebas Neue Bold 11pt #FFFFFF.
- Zone: Source Sans Pro SemiBold 9pt #1A1A1A.
- Masking Type: pill badge, background #FFFDF0, border 1px #C8A838, Source Sans Pro Regular 8pt #C8A838.
- Instructions: Source Sans Pro Regular 9pt #4A4A4A. If zone.notes is set, include it here.
- Remove After: Source Sans Pro Regular 9pt #4A4A4A. "After step X dries" or "Before clear coat".

Masking zones from PROJECT.yaml:
{{maskingZones}}

**ZOOM DETAIL C012 (below table or in margin):**
For the most complex masking zone (highest detail), render a close-up zoom box:
Box border: 1.5px solid #5B2D8E, border-radius 3px.
Zoom corner indicator: small "Z" icon in #5B2D8E at top-left of box.
Label: "DETAIL: [zone name]" Source Sans Pro SemiBold 8pt #5B2D8E above box.
Content: enlarged view of the zone showing tape placement detail. If not available: [ZOOM PLACEHOLDER - complex zone detail].

**PAINT BLEED WARNING (C008):**
Border-left 4px #D32F2F, background #FFF8F8, padding 8px.
Icon: [!] #D32F2F.
Heading: "PREVENT PAINT BLEED" Source Sans Pro Bold 9pt #D32F2F.
Body: "Press tape edges firmly with a toothpick or burnishing tool. Lift tape at 45 degrees away from the paint edge immediately after painting, while paint is still slightly wet. Never leave masking tape on painted surfaces for more than 24 hours." Source Sans Pro Regular 9pt #4A4A4A.

**REQUIRED ELEMENTS:**
- Annotated render with numbered masking zones
- Masking sequence table from maskingZones[]
- Tape type callout C006
- Paint bleed warning C008
- Zoom detail C012 for complex zone
- Footer with P006

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| All `maskingZones[]` in sequence table | QA-061 |
| Zone numbers use gold C013 variant | `Core/COMPONENT_SYSTEM.md §C013` |
| Paint bleed warning C008 present | `Core/COMPONENT_SYSTEM.md §C008` |
| Zoom C012 present for complex zone | `Core/COMPONENT_SYSTEM.md §C012` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{{project.modelSlug}}/Output/raw/P006_raw.md`

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
