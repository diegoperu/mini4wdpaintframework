# AI Operating Rules

**Document ID:** CORE-AIR-001
**SDK Version:** 2.2.0
**Status:** Mandatory
**Applies To:** All AI models used in Phase 2 (Prompt Engine) and Phase 3 (Render Engine)

---

## Purpose

This document defines the non-negotiable behavioral rules for any AI model (ChatGPT, Claude, Gemini, or any other instruction-following LLM) operating within the Mini4WD Manual SDK. These rules exist to ensure consistency, accuracy, and professional quality across all generated manuals.

**These rules are constraints, not suggestions.** An AI-generated output that violates any rule in this document is considered non-compliant and must be regenerated.

The prompt templates in `PromptEngine/` are designed to inject these rules into each generation session. However, manual authors should verify compliance using `Tests/PromptValidation.md` and `Core/QA_SYSTEM.md`.

---

## Rule Categories

1. **[DATA]** — Rules about data accuracy and sourcing
2. **[DESIGN]** — Rules about visual and design compliance
3. **[LAYOUT]** — Rules about page composition and structure
4. **[COLOR]** — Rules about color usage
5. **[CONTENT]** — Rules about written content and language
6. **[RENDER]** — Rules about illustration generation
7. **[COMPONENT]** — Rules about SDK component usage
8. **[TOKEN]** — Rules about Design Token compliance
9. **[OUTPUT]** — Rules about output format and structure

---

## [DATA] Data Accuracy Rules

**RULE-001 [DATA] Never invent paint codes.**
All paint codes (e.g., TS-57, Mr.Color C-5) must come exclusively from `PROJECT.yaml §paintScheme.colors[].paintCode`. If a paint code is not in PROJECT.yaml, it does not exist for this manual. Use `TODO: [PAINT CODE MISSING]` as a placeholder and alert the author.

**RULE-002 [DATA] Never invent Tamiya product references.**
Do not generate references to Tamiya products, tools, or accessories not listed in `PROJECT.yaml §materials`. If a tool is needed but not listed, use `TODO: [TOOL REQUIRED — add to materials]`.

**RULE-003 [DATA] Never assume missing fields.**
If a required PROJECT.yaml field is empty, do not guess its value. Insert `TODO: [FIELD: project.fieldName — VALUE REQUIRED]` and proceed with the rest of the content. Do not silently fill missing fields with plausible-sounding invented data.

**RULE-004 [DATA] Never create non-existent decals.**
Only reference decals listed in `PROJECT.yaml §decals`. Do not add decorative decals, sponsor logos, or sticker designs not explicitly specified.

**RULE-005 [DATA] Never modify the model's official name.**
Use `project.modelName` exactly as written in PROJECT.yaml. Do not translate, abbreviate, or creatively reinterpret the name.

**RULE-006 [DATA] Never change paint brand assignments.**
If PROJECT.yaml specifies Tamiya TS-57 for the body, do not suggest a substitute from Mr.Hobby or Vallejo without an explicit instruction in `notes` field.

**RULE-007 [DATA] Never invent drying times.**
If `preparationSteps[].duration` or `paintSequence[].dryingTime` is not specified, use the value `TODO: [DRYING TIME — consult paint brand specs]`. Do not invent a plausible-sounding time.

**RULE-008 [DATA] Never add colors not in the scheme.**
The `paintScheme.colors` array is the complete and authoritative color list. Do not add "accent" colors, "touch-up" colors, or "optional" colors not in the array.

**RULE-009 [DATA] Always cite source for any technical claim.**
If a claim is not derivable from PROJECT.yaml or Knowledge/ documents, do not make it. Technical accuracy over creative completeness.

**RULE-010 [DATA] Never invent color hex values.**
If `paintScheme.colors[].hex` is empty, do not guess. Use `TODO: [HEX — approximate from paint name]` and leave it to the author to verify.

---

## [DESIGN] Design Compliance Rules

**RULE-011 [DESIGN] Always follow the Design Language.**
All generated content must comply with `Core/DESIGN_LANGUAGE.md`. The 54 rules in that document are non-negotiable. When in doubt, refer to the design language before generating.

**RULE-012 [DESIGN] Never deviate from the Style Guide.**
Font choices, sizes, weights, colors, and spacing must match `Core/STYLE_GUIDE.md`. Do not use fonts not in the approved stack.

**RULE-013 [DESIGN] Never modify the color palette.**
Use only the colors defined in `Assets/DesignSystem/Tokens/tokens.example.yaml`. Do not introduce new brand colors, gradient treatments, or off-palette values.

**RULE-014 [DESIGN] Never alter the body proportions of the model.**
In render descriptions, never suggest modifications to the physical proportions of the Mini4WD car body. Render the model as it is, not as an idealized or "improved" version.

**RULE-015 [DESIGN] Never use decorative fonts.**
Only `TitleFont` (Bebas Neue), `BodyFont` (Source Sans Pro), and `MonoFont` (JetBrains Mono) are permitted. No script fonts, novelty fonts, or style-specific typefaces.

**RULE-016 [DESIGN] Never use gradients as backgrounds.**
All backgrounds must be solid colors. The only valid page background is White (#FFFFFF). Violet panels use solid VioletPrimary (#5B2D8E). No gradient-to-transparent, radial gradients, or textured backgrounds.

**RULE-017 [DESIGN] Maintain visual hierarchy at all times.**
Title > Subtitle > Section Header > Body > Caption. Do not use body-sized text for titles or title-sized text for captions.

**RULE-018 [DESIGN] The violet header band is mandatory on every page.**
C001 Header must appear on every page (P001–P010) without exception. Never omit, resize below 18mm, or recolor it.

**RULE-019 [DESIGN] Never place sponsor logos or external branding.**
Manuals may only contain Tamiya branding for the model (from official reference) and the Mini4WD Manual SDK mark. No third-party brand logos unless explicitly in PROJECT.yaml.

**RULE-020 [DESIGN] Shadows must follow the approved scale.**
Only three shadow levels are permitted: Subtle, Medium, Strong as defined in `Assets/DesignSystem/Tokens/tokens.example.yaml §shadows`. Do not invent shadow values.

---

## [LAYOUT] Layout Rules

**RULE-021 [LAYOUT] Never change page margins.**
Margins are: top 15mm, bottom 20mm, left 18mm, right 18mm. These are locked. Do not adjust for "better fit."

**RULE-022 [LAYOUT] Never reorder pages.**
The page order P001–P010 is fixed. Never swap, merge, or split pages.

**RULE-023 [LAYOUT] Never change page IDs.**
P001 is always Cover. P010 is always Final Checklist. IDs are permanent per `Core/PAGE_SYSTEM.md`.

**RULE-024 [LAYOUT] Content must not intrude into header or footer zones.**
The 18mm top zone (C001) and 12mm bottom zone (C002) are reserved. No content may overlap these zones.

**RULE-025 [LAYOUT] Use the 12-column grid.**
All layout decisions must be based on the 12-column grid defined in `Core/STYLE_GUIDE.md §4`. Do not position elements arbitrarily.

**RULE-026 [LAYOUT] Side panel is always 4 columns wide.**
When a violet side panel is used, it occupies exactly 4 of the 12 columns. Never resize to 3 or 5 columns.

**RULE-027 [LAYOUT] Step numbers (C013) must be sequential and unambiguous.**
In any page with numbered steps, steps must be numbered starting from 1 and must be sequential. Never skip a number, never restart numbering mid-page.

**RULE-028 [LAYOUT] Time boxes (C014) must be right-aligned.**
C014 Time Box is always placed at the right edge of its containing column. Never float it arbitrarily.

---

## [COLOR] Color Rules

**RULE-029 [COLOR] White is always #FFFFFF — never off-white.**
Page backgrounds must be exactly #FFFFFF. Any value including #FEFEFE, #FAFAFA, or #F8F8F8 is non-compliant for page backgrounds (OffWhite may be used only for alternating table rows).

**RULE-030 [COLOR] VioletPrimary must be exactly #5B2D8E.**
Never approximate with nearby purples. The header band, violet panels, and primary brand elements must use this exact value.

**RULE-031 [COLOR] RedWarning (#D32F2F) is reserved for warnings only.**
Do not use red for decorative purposes, section dividers, or general highlighting. Red means danger/caution exclusively.

**RULE-032 [COLOR] GoldAccent (#C8A838) is reserved for tips only.**
Gold is the visual language of helpful tips (C009). Do not use it for decoration or other semantic purposes.

**RULE-033 [COLOR] Never use pure black (#000000) for body text.**
Body text uses DarkGray (#4A4A4A). Pure black is reserved for maximum-contrast situations only (e.g., small text on colored background).

**RULE-034 [COLOR] Color on color must pass readability check.**
White text on VioletPrimary: ✅ (contrast ratio 7.2:1). Black text on GoldAccent: ✅. White text on GoldAccent: ❌. Check contrast before specifying any text-on-color combination.

**RULE-035 [COLOR] Paint colors in renders must match PROJECT.yaml.**
The rendered model must use the exact finish and approximate color of each `paintScheme.colors[]` entry. Do not render a glossy finish as matte, or a pearl as solid.

---

## [CONTENT] Content Rules

**RULE-036 [CONTENT] Use the primary language specified in PROJECT.yaml.**
`project.language` determines the language for all generated text. Italian (`it`) means all body text, labels, and instructions are in Italian. Do not mix languages within a page.

**RULE-037 [CONTENT] Technical terms must be consistent across pages.**
If "carrozzeria" is used for "body" in P002, it must be "carrozzeria" in P005 and P006. Do not alternate between synonyms.

**RULE-038 [CONTENT] Instructions must be imperative.**
Step descriptions use the imperative voice: "Applica il primer" not "Il primer va applicato." Active, direct, imperative.

**RULE-039 [CONTENT] Never use vague quantity descriptors.**
Do not write "some paint," "a bit of thinner," or "a few coats." Write specific values from PROJECT.yaml or use `TODO: [QUANTITY — specify in PROJECT.yaml]`.

**RULE-040 [CONTENT] No placeholder text in final output.**
"Lorem ipsum," "[TEXT HERE]," "PLACEHOLDER," and similar strings are strictly forbidden in any page output intended for QA or publication.

**RULE-041 [CONTENT] Warnings must use W0XX pattern for internal tracking.**
Any warning box (C008) content should be written as a self-contained safety instruction. Avoid vague warnings like "be careful."

**RULE-042 [CONTENT] Tips must be actionable.**
Tip boxes (C009) must contain specific, actionable advice — not generic platitudes. "Apply masking tape at room temperature to prevent adhesive failure" not "Be careful with masking tape."

**RULE-043 [CONTENT] Glossary terms must link to Knowledge/Glossary.md.**
When a technical term is first introduced in a page, note it for inclusion in `Knowledge/Glossary.md`. Do not define terms inline in the manual body.

**RULE-044 [CONTENT] Do not include SDK metadata in output.**
References to "Mini4WD Manual SDK," "PromptEngine," "PROJECT.yaml," or other SDK internals must not appear in generated page content visible to end users.

---

## [RENDER] Render Rules

**RULE-045 [RENDER] All render backgrounds must be pure white.**
No exceptions. Background = #FFFFFF. No shadows on background, no vignettes, no floor reflections.

**RULE-046 [RENDER] Render angles must match RENDER_GUIDE.md §2.**
Do not generate renders at arbitrary angles. Use only the documented angles: cover (3/4 front-left, 15°), orthographic (0°/90°), detail (45°, 30° elevation).

**RULE-047 [RENDER] Render lighting must use an approved rig.**
Only Studio Neutral, Drama, or Detail lighting rigs are permitted. See `Config/render.yaml §lighting_rigs`.

**RULE-048 [RENDER] Render resolution must meet minimums.**
Cover: 2480×3508px. Body: 1240×1754px. Detail: 800×800px. Undersized renders are rejected and must be regenerated.

**RULE-049 [RENDER] No motion blur in static renders.**
These are product photography renders, not action shots. All renders must be crisp with no motion blur, depth-of-field bokeh on the model, or artistic camera effects.

**RULE-050 [RENDER] No environmental context in renders.**
Do not place the model on a racetrack, tabletop, diorama, or any surface. White background only. The model floats in neutral product-photography space.

---

## [COMPONENT] Component Rules

**RULE-051 [COMPONENT] Component IDs are permanent — never rename.**
C001 is always Header. C015 is always Notes. IDs do not change between SDK versions. Do not use deprecated names like COMP_HEADER.

**RULE-052 [COMPONENT] Use only approved components.**
Only C001–C015 (and future approved IDs from `Config/sdk.yaml §components.next_available_id`) may be used. Do not invent new visual components without filing an SDK issue and receiving an ID.

**RULE-053 [COMPONENT] Every page must have C001 and C002.**
Header and Footer are mandatory on every generated page. No exceptions.

---

## [TOKEN] Design Token Rules

**RULE-054 [TOKEN] All visual values must use Design Tokens.**
Never hardcode a color hex, font size, spacing value, or shadow value. Always reference by token name: `{{token.VioletPrimary}}` not `#5B2D8E`.

**RULE-055 [TOKEN] Tokens are in tokens.example.yaml — do not override.**
Design Tokens are set globally. Per-project token overrides are not permitted in v2.2.0. Do not create project-level token files.

---

## [OUTPUT] Output Format Rules

**RULE-056 [OUTPUT] Raw output goes to Output/raw/ — not to Images/.**
Phase 2 text output (page descriptions) goes to `Projects/{ModelName}/Output/raw/`. Phase 3 render images go to `Projects/{ModelName}/Images/`. These directories have different purposes.

**RULE-057 [OUTPUT] All TODO markers must be resolved before QA.**
Any `TODO:` marker in the output indicates an authoring gap. All TODOs must be resolved before running the QA checklist (`Core/QA_SYSTEM.md`).

**RULE-058 [OUTPUT] Page ID must appear in footer.**
Every generated page description must specify that C002 Footer contains the correct page ID (P001–P010). This is verified in QA-062.

---

## Compliance Summary

| Category | Rules | Blocking |
|----------|-------|----------|
| DATA | RULE-001 to RULE-010 | All |
| DESIGN | RULE-011 to RULE-020 | All |
| LAYOUT | RULE-021 to RULE-028 | All |
| COLOR | RULE-029 to RULE-035 | All |
| CONTENT | RULE-036 to RULE-044 | RULE-040 (no placeholders) |
| RENDER | RULE-045 to RULE-050 | RULE-045, RULE-048 |
| COMPONENT | RULE-051 to RULE-053 | RULE-053 |
| TOKEN | RULE-054 to RULE-055 | RULE-054 |
| OUTPUT | RULE-056 to RULE-058 | RULE-057 |

---

## Related Documents
- `Core/DESIGN_LANGUAGE.md` — design philosophy rules
- `Core/STYLE_GUIDE.md` — visual specifications
- `Core/QA_SYSTEM.md` — compliance verification checklist
- `Core/PAGE_SYSTEM.md` — page-level requirements
- `Core/COMPONENT_SYSTEM.md` — component specifications
- `Assets/DesignSystem/Tokens/tokens.example.yaml` — approved token values
- `Config/render.yaml` — render configuration
- `PromptEngine/README.md` — how rules are injected into prompts
- `Tests/PromptValidation.md` — prompt compliance tests
