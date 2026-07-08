# Page System

This document specifies all permanent pages in the Mini4WD Manual SDK. Pages are identified by permanent IDs in the format `P###`. These IDs never change. The logical order of pages in a PDF is defined by `Templates/PDF_CONFIG.yaml`, not by the IDs.

For the extension mechanism (adding P011+), see the final section of this document.

---

## Page ID Registry

| ID | Name | Required | Side Panel |
|---|---|---|---|
| P001 | Cover | Yes | No |
| P002 | Color Scheme | Yes | Yes |
| P003 | Materials | Yes | Yes |
| P004 | Preparation | Yes | Yes |
| P005 | Painting | Yes | Yes |
| P006 | Masking | Yes | Yes |
| P007 | Details | Yes | Yes |
| P008 | Decals | Yes | Yes |
| P009 | Premium Variant | No | Yes |
| P010 | Final Checklist | Yes | No |

A manual that omits P009 is valid. All other pages are required. A manual that omits any other page fails the QA check QA-086.

---

## P001 — Cover

**Purpose:** Creates the first visual impression. Establishes the model identity, paint scheme name, and SDK brand. The cover must communicate quality and craft before the reader opens the manual.

**Input (from PROJECT.yaml):**
- `{{project.modelName}}` — full model name, displayed at Display size (48pt minimum)
- `{{project.series}}` — chassis or series name, displayed at H3
- `{{project.paintScheme.name}}` — paint scheme name, displayed as subtitle
- `{{project.renders.cover}}` — path to approved cover render image

**Output:** Single full-bleed illustration page. The render fills the page from the bottom of the header to the top of the footer. Title information overlays the lower quarter of the render on a semi-transparent TamiyaPrimary band.

**Dependencies:**
- `C001` Header (TamiyaPrimary band, top)
- `C002` Footer (page reference, bottom)
- `RENDER_GUIDE.md` §2 (cover angle: 3/4 front-left, elevated 15°)
- `RENDER_GUIDE.md` §3 (Studio Neutral or Drama lighting)

**Components Used:** C001, C002

**Checklist:**
- [ ] Model name at minimum 48pt, TitleFont, white
- [ ] Paint scheme name visible as subtitle, H3, white
- [ ] Series name present, Caption size, white
- [ ] Cover render is 3/4 front-left angle per RENDER_GUIDE.md §2
- [ ] Render background is white or transparent
- [ ] TamiyaPrimary header band present (C001)
- [ ] Footer contains page identifier P001 (C002)
- [ ] Render minimum resolution: 2480×3508px (A4 @300dpi)

**Best Practice:** The cover render should show the model with its most visually striking angle. The TamiyaPrimary title band at the bottom must not obscure more than 25% of the render. If the render is too dark in the lower quarter, choose Drama lighting which concentrates illumination on the upper two-thirds.

**Common Errors:**
- Using a render with a gray or gradient background
- Missing the series name
- Using BodyFont instead of TitleFont for the model name
- Render resolution below minimum

---

## P002 — Color Scheme

**Purpose:** Documents the complete paint scheme in a three-view orthographic layout. This page is the technical reference for the color scheme — a reader must be able to reproduce the scheme from this page alone.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.name}}`
- `{{project.paintScheme.colors}}` — array of paint colors with code, name, finish, swatch hex
- `{{project.renders.colorFront}}` — orthographic front view render
- `{{project.renders.colorSide}}` — orthographic side view render
- `{{project.renders.colorTop}}` — orthographic top view render

**Output:** Three-view orthographic layout (front, side, top) with color legend sidebar.

**Dependencies:**
- `C001`, `C002`
- `C003` Palette (color swatches)
- `C010` Paint Legend (color-to-area mapping)
- `C011` Paint Code Box (per-color code reference)
- `RENDER_GUIDE.md` §2 (orthographic angles)

**Components Used:** C001, C002, C003, C010, C011

**Checklist:**
- [ ] All three views present: front, side, top
- [ ] All render angles are true orthographic (no perspective distortion)
- [ ] C003 Palette shows all colors in the scheme
- [ ] Each color in C010 has a corresponding C011 Paint Code Box
- [ ] Paint codes are in monospace font (MonoFont)
- [ ] Swatch hex values match COLOR_SCHEME.yaml `swatchHex` field
- [ ] Side panel contains the full color legend (C010)

**Best Practice:** Number the colors in the scheme (Color 1, Color 2, …) and reference the same numbers in the three-view renders. This creates an unambiguous link between the diagram and the legend.

**Common Errors:**
- Using perspective renders instead of orthographic
- Missing a color from the legend that appears in the render
- Swatch colors that do not match the actual paint

---

## P003 — Materials

**Purpose:** Lists all materials required to complete the paint scheme. This is the shopping list page. A reader must be able to use this page to gather all materials before starting.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.colors}}` — generates paint list
- `{{project.materials}}` — additional materials array (masking tape, primer, varnish, etc.)
- `{{project.tools}}` — optional tools array

**Output:** Organized materials list with paint codes, quantities, and supplier notes.

**Dependencies:**
- `C001`, `C002`
- `C004` Shopping List
- `C008` Warning (if hazardous materials are listed)
- `C009` Tips (for material substitution suggestions)

**Components Used:** C001, C002, C004, C008 (conditional), C009 (conditional)

**Checklist:**
- [ ] Every paint used in P005 and P006 is listed
- [ ] All paints include: code, full name, finish type (gloss/flat/metallic/etc.)
- [ ] Masking materials listed if P006 Masking is present
- [ ] Primer listed if preparation requires it (P004)
- [ ] Topcoat/varnish listed if P007 Details references it
- [ ] At least one C008 Warning if any material is flammable or requires ventilation
- [ ] C004 Shopping List component used (not a freeform list)

**Best Practice:** Organize materials by phase: (1) preparation materials, (2) base coat materials, (3) detail and masking materials, (4) finishing materials. This mirrors the sequence of later pages.

**Common Errors:**
- Omitting primer when the paint scheme requires it
- Missing safety warning for aerosol paints
- Listing tools on the materials page (tools belong in a separate section)

---

## P004 — Preparation

**Purpose:** Documents the preparation process: cleaning, sanding, priming. Steps must be numbered and illustrated. This page must be completable by a hobbyist with no prior experience.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.requiresPrimer}}` — boolean, drives primer section
- `{{project.body.material}}` — polycarbonate or ABS, drives cleaning procedure

**Output:** Numbered step sequence with renders/photographs for each preparation stage.

**Dependencies:**
- `C001`, `C002`
- `C005` Paint Sequence (adapted for preparation steps)
- `C006` Callout
- `C008` Warning
- `C009` Tips
- `C013` Step Number
- `C014` Time Box

**Components Used:** C001, C002, C005, C006, C008, C009, C013, C014

**Checklist:**
- [ ] Steps are numbered using C013 (not inline numbers)
- [ ] Each step has an accompanying render or photograph
- [ ] C014 Time Box present on at least the primer drying step
- [ ] C008 Warning present if sanding generates dust
- [ ] Primer section included if `{{project.paintScheme.requiresPrimer}}` is true
- [ ] Steps are in chronological sequence with no gaps

**Common Errors:**
- Skipping the cleaning step (common but essential)
- Omitting drying times (the reader does not know how long to wait)
- Generic steps not specific to the model's material

---

## P005 — Painting

**Purpose:** The primary technical page. Documents the base coat and main color application in numbered steps. This is the page most readers will reference most often.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.colors}}` — drives step sequence
- `{{project.renders.painting}}` (optional) — in-progress renders

**Output:** Sequential painting steps with color call-outs and time boxes.

**Dependencies:**
- `C001`, `C002`
- `C005` Paint Sequence
- `C006` Callout
- `C008` Warning
- `C009` Tips
- `C011` Paint Code Box
- `C013` Step Number
- `C014` Time Box

**Components Used:** C001, C002, C005, C006, C008, C009, C011, C013, C014

**Checklist:**
- [ ] Each color application is a separate numbered step
- [ ] Each step references the paint code in a C011 Paint Code Box
- [ ] Drying time specified via C014 for each coat
- [ ] Number of coats specified per step (e.g., "2 thin coats")
- [ ] C008 Warning present for aerosol application
- [ ] Coat direction specified where relevant (horizontal, vertical)

**Common Errors:**
- Combining multiple color steps into one step
- Missing coat count — reader doesn't know how many coats to apply
- No drying time guidance

---

## P006 — Masking

**Purpose:** Documents the masking process for two-tone or multi-color schemes. If the paint scheme has only one color, this page may be abbreviated to a single note. If the scheme has complex masking, this page may expand to include multiple step sequences.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.maskingRequired}}` — boolean
- `{{project.paintScheme.maskingSequence}}` — array of masking steps

**Output:** Masking layout diagram + numbered steps for tape placement.

**Dependencies:**
- `C001`, `C002`
- `C006` Callout
- `C007` Exploded View (for masking diagram)
- `C008` Warning
- `C009` Tips
- `C012` Zoom
- `C013` Step Number

**Components Used:** C001, C002, C006, C007, C008, C009, C012, C013

**Checklist:**
- [ ] Top-view diagram shows masking tape placement
- [ ] Critical edges highlighted with C012 Zoom
- [ ] Tape removal step documented (often forgotten)
- [ ] C009 Tip for sharp-edge masking technique
- [ ] If single-color scheme: page present but notes "No masking required"

**Common Errors:**
- Omitting the tape removal step
- No diagram showing tape placement (purely verbal instructions are insufficient)

---

## P007 — Details

**Purpose:** Documents detail painting: window frames, wheel arches, small accents, and any hand-painted elements. These are precision steps that require more care than base coat application.

**Input (from PROJECT.yaml):**
- `{{project.paintScheme.details}}` — array of detail elements

**Output:** Close-up renders of each detail area with step instructions.

**Dependencies:**
- `C001`, `C002`
- `C009` Tips
- `C011` Paint Code Box
- `C012` Zoom
- `C013` Step Number
- `C014` Time Box

**Components Used:** C001, C002, C009, C011, C012, C013, C014

**Checklist:**
- [ ] Each detail element has its own numbered step
- [ ] C012 Zoom present for any element smaller than 5mm
- [ ] Hand-painted elements noted with "fine brush recommended" tip
- [ ] All paint codes referenced with C011

**Common Errors:**
- Treating details as a footnote rather than their own step sequence
- Missing zoom views for small parts

---

## P008 — Decals

**Purpose:** Documents decal placement. If the paint scheme includes no decals, this page must still be present and must state that clearly.

**Input (from PROJECT.yaml):**
- `{{project.decals}}` — array of decal positions and identifiers

**Output:** Top-view and side-view diagrams with numbered decal placement positions.

**Dependencies:**
- `C001`, `C002`
- `C008` Warning (for decal setting solution)
- `C009` Tips (for air bubble prevention)
- `C012` Zoom
- `C013` Step Number

**Components Used:** C001, C002, C008, C009, C012, C013

**Checklist:**
- [ ] Diagram shows every decal position by number
- [ ] Decal alignment references visible in diagram (panel lines, edge positions)
- [ ] Decal setting solution mentioned if applicable
- [ ] If no decals: page states "This scheme does not use decals"

**Common Errors:**
- Ambiguous decal placement (no alignment reference)
- Missing decal numbering that corresponds to the diagram

---

## P009 — Premium Variant

**Purpose:** Optional page documenting a premium or special-edition variant of the paint scheme. This may include metallic finishes, candy coats, additional decals, or upgraded materials.

**Required:** No. If omitted, the manual is still valid. When present, this page is inserted between P008 and P010 in PDF_CONFIG.yaml.

**Input (from PROJECT.yaml):**
- `{{project.premiumVariant}}` — optional block; if absent, omit this page

**Output:** Variant description with comparison renders (standard vs. premium).

**Dependencies:**
- `C001`, `C002`
- `C003` Palette
- `C009` Tips
- `C011` Paint Code Box
- `C013` Step Number

**Components Used:** C001, C002, C003, C009, C011, C013

**Checklist:**
- [ ] Comparison render shows standard and premium variant side-by-side
- [ ] Premium materials listed separately from P003
- [ ] Difficulty upgrade clearly noted (if premium requires advanced techniques)
- [ ] Page labeled "PREMIUM VARIANT" in C001 header right section

---

## P010 — Final Checklist

**Purpose:** The closing page of every manual. Provides a step-by-step quality review checklist that the hobbyist uses after completing the paint job. Also serves as the "done" moment — a reader who completes this page has finished the manual.

**Input (from PROJECT.yaml):**
- `{{project.modelName}}`
- `{{project.paintScheme.name}}`

**Output:** Structured checklist with print/digital checkbox for each quality criterion.

**Dependencies:**
- `C001`, `C002`
- `C015` Notes (for personal notes section)

**Components Used:** C001, C002, C015

**Checklist:**
- [ ] At least 10 checklist items covering: surface quality, color accuracy, decal placement, varnish coat, overall finish
- [ ] Items are specific to the model and scheme (not generic)
- [ ] C015 Notes block present for personal annotations
- [ ] Page labeled "FINAL CHECKLIST" in C001 header

**Best Practice:** End the checklist with a positive completion statement. The reader has invested time and craft. Acknowledge it.

**Common Errors:**
- Generic checklist not adapted to the model
- Missing the notes section (readers always want to annotate)

---

## Extension Mechanism: Adding Pages P011+

New pages can be added to the system without modifying existing pages. Follow this procedure:

1. **Reserve an ID:** Increment from the highest existing ID (currently P010 → next is P011)
2. **Create the specification:** Add a section to this document following the exact format of P001–P010
3. **Assign components:** Specify which components the new page uses. Use existing components where possible.
4. **Create the prompt:** Add a corresponding file to `PromptEngine/` (e.g., `PromptEngine/NewPageName.md`)
5. **Update PDF_CONFIG.yaml:** Add the new page to the page order specification in `Templates/PDF_CONFIG.yaml`
6. **File an ADR:** Record the decision in `STYLE_DECISIONS.md`
7. **Update CHANGELOG.md:** Add to the `[Unreleased]` section, then include in the next MINOR release

> ⚠️ **Warning:** New pages added in a MINOR release must not be required in existing projects. New pages are always optional until a MAJOR release makes them mandatory. Required pages can only be added in MAJOR releases with a migration guide.

---

## v2.4.0 — Page as Content Module

*Added in SDK v2.4.0. Each page is now a self-contained content module with structured data, versioning, and lifecycle management.*

### Module Architecture

Each page (P001–P010) is no longer just a generated image. It is a module stored in `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/` containing:

```
P{NNN}/
├── content.yaml    ← PRIMARY: structured editorial data
├── text.md         ← DERIVED: human-readable (from content.yaml)
├── metadata.yaml   ← Lifecycle state, approval, QA status
├── manifest.yaml   ← Asset list, components, dependencies
├── changelog.md    ← Revision history
├── notes.md        ← Editorial annotations (not rendered)
└── README.md       ← Page module documentation
```

### Page Lifecycle States

| State | content.yaml | Render Engine | Description |
|-------|-------------|---------------|-------------|
| `draft` | Editable | No access | Initial generation, work in progress |
| `review` | Editable (tracked) | No access | Under editorial review |
| `approved` | Sealed* | Read access | Passed ContentValidation + TextValidation |
| `locked` | Immutable | Read access | Production-ready, no changes allowed |
| `rendered` | Immutable | Read-only reference | Render generated from this content |
| `released` | Immutable | Read-only reference | Published in PDF manual |
| `archived` | Immutable | No access | Superseded by newer version |

*Sealed: requires resetting `metadata.yaml §approved: false` to edit, with changelog entry.

### Reusability

Page modules are designed to be reusable:
- A locked P002 for "Proto Emperor v1" can be copied and adapted for a new color scheme
- Reused modules must update: `metadata.yaml §revision`, `page.version`, and `changelog.md`
- Never reuse a locked module directly — always copy and create a new revision

### Extension: Adding New Pages (P011+)

When adding pages beyond P010:
1. Assign next available ID: `P011`, `P012`, etc.
2. Add to `Config/sdk.yaml §pages`
3. Create `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/` with all required files
4. Create `PromptEngine/{PageName}.md`
5. Add ADR in `STYLE_DECISIONS.md`
6. Update `MANIFEST.yaml §pages`
