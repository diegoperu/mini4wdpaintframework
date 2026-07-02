# P009 — Premium Variant Prompt

**SDK Version:** 2.4.0
**Page ID:** P009
**Prompt File:** `PromptEngine/Premium.md`
**Dependencies:** `PROJECT.yaml` (`premiumVariant.enabled` must be `true`), `Core/COMPONENT_SYSTEM.md §C006`, `Core/COMPONENT_SYSTEM.md §C009`, `Core/COMPONENT_SYSTEM.md §C011`, `Core/COMPONENT_SYSTEM.md §C015`

---

## Purpose

Generate the premium variant page. This page is conditional — only generated if `premiumVariant.enabled: true` in PROJECT.yaml. The premium variant presents an elevated version of the base paint scheme using advanced techniques: pearl finishes, candy coats, chrome effects, airbrushed gradients, or multi-layer metallics.

The page includes a side-by-side comparison between the base scheme and the premium variant, and documents the additional steps and materials.

---

## Required Inputs (from PROJECT.yaml)

| Token | Field Path | Description | Example |
|-------|-----------|-------------|---------|
| `{{project.modelName}}` | `project.modelName` | Model name | `Proto Emperor` |
| `{{paintScheme.name}}` | `paintScheme.name` | Base scheme name | `Violet Phantom` |
| `{{premiumVariant.name}}` | `premiumVariant.name` | Premium scheme name | `Violet Phantom Pearl Edition` |
| `{{premiumVariant.description}}` | `premiumVariant.description` | Variant description | `Pearl topcoat over violet base` |
| `{{premiumVariant.additionalMaterials}}` | `premiumVariant.additionalMaterials[]` | Extra materials needed | see PROJECT.yaml |
| `{{premiumVariant.specialTechniques}}` | `premiumVariant.specialTechniques[]` | Advanced techniques used | see PROJECT.yaml |

---

## Conditional Check

Before running this prompt, verify: `premiumVariant.enabled: true` in `Projects/{modelSlug}/PROJECT.yaml`.
If `false`, skip this page — P009 is not generated and the manual goes directly from P008 to P010.

---

## Prompt Template

--- START PROMPT ---

You are generating the PREMIUM VARIANT page (P009) of a Mini4WD painting manual for "{{project.modelName}}".

This page presents the "{{premiumVariant.name}}" — an advanced version of the base scheme "{{paintScheme.name}}" that uses specialized techniques for a superior finish. Assume the reader has already completed the base manual and is ready to elevate their work.

**Page Layout: A4 (210x297mm), white background White**

**HEADER (C001):** Violet band VioletPrimary, 18mm. Left: "Mini4WD Manual". Right: "PREMIUM".
**FOOTER (C002):** LightGray, 12mm. Center: "{{project.modelName}} — Premium Variant  |  P009".

**PREMIUM BADGE (top-right of main area, 20mm from right, 22mm from top):**
Hexagonal badge shape (or pill), background: gradient from GoldAccent to #E8C84A, border 2px GoldAccent, border-radius 8px, padding 6px 12px.
Text: "PREMIUM" Bebas Neue Bold 14pt White, letter-spacing 3px.

**PAGE TITLE (22mm from top, left margin):**
"{{premiumVariant.name}}" in Bebas Neue Bold 32pt VioletPrimary.
Subtitle: "{{premiumVariant.description}}" Source Sans Pro Light Italic 13pt DarkGray, 34mm from top.

**COMPARISON PANEL (40mm to 140mm, full width):**
Two-column comparison layout. Violet divider line (2px VioletPrimary) in center at 105mm.

Left column (18mm to 97mm): BASE SCHEME
- Column heading: "BASE: {{paintScheme.name}}" Source Sans Pro SemiBold 10pt MidGray uppercase.
- Render: 3/4 view of model in base scheme. If not available: [BASE RENDER PLACEHOLDER]
- Caption: Source Sans Pro Regular 8pt MidGray italic, centered below render.

Right column (113mm to 192mm): PREMIUM VARIANT
- Column heading: "PREMIUM: {{premiumVariant.name}}" Source Sans Pro SemiBold 10pt VioletPrimary uppercase.
- Render: 3/4 view of model in premium scheme. If not available: [PREMIUM RENDER PLACEHOLDER]
- Caption: Source Sans Pro Regular 8pt VioletPrimary italic, centered below render.

**WHAT MAKES IT PREMIUM callout C006 (144mm from top, full width minus margins):**
Violet-left-border callout: border-left 4px VioletPrimary, background #F5F0FA, border-radius 0 4px 4px 0, padding 12px.
Heading: "WHAT ELEVATES THIS SCHEME" Source Sans Pro Bold 10pt VioletPrimary.
Body: List all specialTechniques from {{premiumVariant.specialTechniques}}, one per line, Source Sans Pro Regular 10pt DarkGray, bullet VioletPrimary 4px circle.
If no techniques defined: "Pearl topcoat adds depth and iridescence to the base color, creating a finish that changes character under different lighting conditions."

**ADDITIONAL MATERIALS (from 170mm, if additionalMaterials non-empty):**
Section heading: "ADDITIONAL MATERIALS REQUIRED" Source Sans Pro SemiBold 10pt VioletPrimary uppercase, violet underline.

For each item in {{premiumVariant.additionalMaterials}}, render a compact row:
- Code Box mini C011: brand 6pt above code 8pt Bebas Neue VioletPrimary, violet border 1px, width 30mm.
- Name: Source Sans Pro SemiBold 9pt Black.
- Purpose: Source Sans Pro Regular 8pt DarkGray.
Row separator: 1px LightGray.

**TECHNIQUE STEPS (from 200mm or below materials):**
Section heading: "PREMIUM TECHNIQUE SEQUENCE" Source Sans Pro SemiBold 10pt VioletPrimary uppercase, violet underline.

For each technique in {{premiumVariant.specialTechniques}}, render a compact numbered step (same style as preparation steps, but with gold step circles C013 in GoldAccent to indicate premium content).

**TIPS C009 (full width, before footer):**
Gold-left-border box: border-left 4px GoldAccent, background #FFFDF0, padding 8px.
Icon: [*] GoldAccent.
Heading: "PREMIUM FINISHING TIPS" Source Sans Pro Bold 9pt GoldAccent.
Body: "The difference between a good finish and a premium finish is preparation and patience. Never rush a pearl or candy coat — thin coats, long dry times, controlled environment. Humidity above 60% will cause cloudiness in clear coats. Temperature should be 18-24 degrees Celsius. Practice the technique on a spare body before applying to your finished model." Source Sans Pro Regular 9pt DarkGray.

**NOTES C015 (if applicable):**
Background OffWhite, border 1px LightGray, border-radius 3px, padding 8px.
Content: any premium-specific notes not covered above.

**REQUIRED ELEMENTS:**
- Premium badge
- Comparison panel (base vs premium)
- What makes it premium callout C006
- Additional materials list (if additionalMaterials non-empty)
- Technique steps from specialTechniques[]
- Premium tips C009
- Footer with P009

--- END PROMPT ---

---

## Post-Generation Validation

| Check | Reference |
|-------|-----------|
| `premiumVariant.enabled: true` before generating | PROJECT.yaml |
| Comparison panel present (base vs premium) | Prompt spec |
| C006 callout explains premium techniques | `Core/COMPONENT_SYSTEM.md §C006` |
| C009 tips present | `Core/COMPONENT_SYSTEM.md §C009` |
| Additional materials listed if defined | Prompt spec |
| Page level DoD | `Core/DEFINITION_OF_DONE.md` |

Save output to: `ApprovedAssets/Text/P009/content.yaml`

---

*Part of Mini4WD Manual SDK v2.4.0 — PromptEngine. Page is conditional on `premiumVariant.enabled: true`.*
