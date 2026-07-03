# P008 — Decals Placement Prompt

**SDK Version:** 2.4.0
**Page ID:** P008
**Prompt File:** `PromptEngine/Decals.md`
**Dependencies:** `PROJECT.yaml`, `Core/COMPONENT_SYSTEM.md §C008`, `Core/COMPONENT_SYSTEM.md §C009`, `Core/COMPONENT_SYSTEM.md §C012`, `Core/COMPONENT_SYSTEM.md §C015`

---

## Purpose

Generate the decal application guide. Decals are the finishing touch that complete the model's appearance. Incorrect placement is permanent — decals cannot be repositioned once the solvent activates. This page must give the reader precise placement coordinates and application technique.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{decals}}` | `decals[]` | Decal definitions with positions | see PROJECT.yaml |

---

## Prompt Template

--- START PROMPT ---

You are generating the DECALS page (P008) of a Mini4WD painting manual for "{{project.modelName}}".

This page guides the application of all decals: numbers, logos, stripes, sponsor markings. Placement must be shown visually and described precisely. The application technique steps are mandatory.

**Page Layout: A4 (210x297mm), white background White**

**HEADER (C001):** Violet band VioletPrimary, 18mm. Left: "Mini4WD Manual". Right: "DECALS".
**FOOTER (C002):** LightGray, 12mm. Center: "{{project.modelName}} — Decals  |  P008".

**PAGE TITLE (22mm from top):**
"Decal Application Guide" in Bebas Neue Bold 28pt VioletPrimary, left margin 18mm.
Subtitle: "Apply decals only after the top coat is fully cured (minimum 24 hours)." Source Sans Pro Regular 11pt DarkGray, 32mm from top.

**PLACEMENT OVERVIEW RENDER (upper area, 42mm to 140mm):**
Annotated top-view or 3/4 view render of the model showing all decal positions numbered.

Annotation style:
- Each decal position: filled circle 14x14mm BlueInfo, Bebas Neue Bold 11pt White with decal ID number inside.
- Leader lines: 1px BlueInfo, dashed.
- Placement area indicators: dashed rectangle outline BlueInfo, 1.5px, around each decal's approximate footprint on the model.
- Background: white.
- Note: if render not available: [DECAL PLACEMENT OVERVIEW PLACEHOLDER - show model outline with numbered positions]

**DECAL REFERENCE TABLE (from 144mm):**
Section heading: "DECAL REFERENCE" Source Sans Pro SemiBold 10pt VioletPrimary uppercase, violet underline.

Table columns: | # | Decal Name | Position Description | Size | Application Notes |

For each decal in {{decals}}:
- #: filled circle 14x14mm BlueInfo, Bebas Neue Bold 11pt White (matching overview render).
- Decal Name: Source Sans Pro SemiBold 10pt Black.
- Position Description: Source Sans Pro Regular 9pt DarkGray. Use decal.position field.
- Size: Source Sans Pro Regular 9pt DarkGray. Use decal.size field, or "--" if not specified.
- Application Notes: Source Sans Pro Regular 9pt DarkGray. Use decal.notes, or SDK standard: "Soak 30 sec, slide onto surface, position, absorb excess water."

Row separator: 1px LightGray hairline.

Decals from PROJECT.yaml:
{{decals}}

**ZOOM DETAILS C012 (below table, for first 2 decals or most critical):**
Two zoom panels side by side (88mm each, 14mm gutter):
Each panel: border 1.5px BlueInfo, border-radius 3px, label "DETAIL: [decal name]" Source Sans Pro SemiBold 8pt BlueInfo.
Content: close-up of the model surface showing decal placement in context. If not available: [ZOOM PLACEHOLDER: {{decal.name}} placement detail].

**APPLICATION TECHNIQUE STEPS C009 (Tips box, after zoom panels):**
Gold-left-border box: border-left 4px GoldAccent, background #FFFDF0, padding 10px.
Icon: [*] GoldAccent.
Heading: "APPLICATION TECHNIQUE" Source Sans Pro Bold 9pt GoldAccent.
Body (SDK-standard decal application steps, always include):
"Step 1 — PREPARE THE SURFACE: The surface must be clean, dry, and fully cured. Wipe with a lint-free cloth dampened with distilled water.
Step 2 — CUT THE DECAL: Cut close around the decal with sharp scissors. Leave 0.5mm of clear film around the printed area.
Step 3 — SOAK: Immerse the decal in lukewarm distilled water for 20-30 seconds. The decal will release from the backing.
Step 4 — POSITION: Slide the decal off the backing paper onto the model surface using tweezers. Position carefully — you have approximately 30 seconds before the adhesive sets.
Step 5 — ABSORB EXCESS WATER: Use a soft tissue or cotton swab to absorb water from the edges. Work from center outward.
Step 6 — DECAL SOFTENER: Apply a small amount of decal softener (e.g., Tamiya Mark Fit) over the decal with a soft brush. This helps the decal conform to curved surfaces.
Step 7 — WAIT AND SEAL: Allow 12 hours to fully dry. Apply clear top coat over all decals to protect and integrate them with the paint surface."
Source Sans Pro Regular 9pt DarkGray.

**DECAL SOFTENER WARNING C008:**
Border-left 4px RedWarning, background #FFF8F8, padding 8px.
Icon: [!] RedWarning.
Heading: "DECAL SOFTENER CAUTION" Source Sans Pro Bold 9pt RedWarning.
Body: "Do not apply excess decal softener — it will wrinkle and destroy the decal. Use only one thin coat applied with a soft brush. Do not brush over the decal after applying softener — let it work on its own. Do not use decal solvent (a stronger chemical) unless the surface is already sealed." Source Sans Pro Regular 9pt DarkGray.

**NOTES BOX C015 (if any decal has specific notes not covered above):**
Background OffWhite, border 1px LightGray, border-radius 3px, padding 8px.
Heading: "MODEL-SPECIFIC DECAL NOTES" Source Sans Pro SemiBold 9pt DarkGray.
Body: aggregated notes from decals[], or: "No model-specific decal notes."

**REQUIRED ELEMENTS:**
- Annotated placement overview render
- Decal reference table with all decals[]
- Zoom C012 for complex placements
- Application technique steps C009
- Decal softener warning C008
- Notes C015
- Footer with P008

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| All `decals[]` in reference table | QA-061 |
| Placement overview render annotated | QA-016 to QA-030 |
| Application steps C009 complete (7 steps) | `Core/COMPONENT_SYSTEM.md §C009` |
| Decal softener warning C008 present | `Core/COMPONENT_SYSTEM.md §C008` |
| C015 notes present | `Core/COMPONENT_SYSTEM.md §C015` |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `Projects/{Model}/{Variant}/ApprovedText/P008/content.yaml`
(where {Model} = PascalCase_Underscore model folder, {Variant} = PascalCase_Underscore variant folder derived from paintScheme.slug)

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine.*
