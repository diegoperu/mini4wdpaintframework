# QA System

This is the quality assurance checklist for all manuals produced by the Mini4WD Manual SDK. A manual is not approved until every applicable item in this checklist returns PASS.

Items marked with an asterisk (`*`) are automatically not applicable to pages that do not use the referenced component or feature. For example, QA-063 (C003 Palette present on P002) is not applicable if the project does not include P002 — but P002 is required, so QA-063 is effectively always applicable.

Document your QA session in `Projects/{ModelName}/Notes/qa_log.md` using the format:
```
QA-NNN: PASS | FAIL — [description of failure if FAIL]
```

---

## Category 1 — Layout

- [ ] QA-001: Page margins match STYLE_GUIDE.md §3.2 (top 15mm, bottom 20mm, left/right 18mm) — incorrect margins cause content to be cut off in print
- [ ] QA-002: All content elements are aligned to the 12-column grid — off-grid elements look misaligned and unprofessional
- [ ] QA-003: Header (C001) is present on every page and positioned at the top edge of the page — its absence removes the brand identity
- [ ] QA-004: Footer (C002) is present on every page and positioned at the bottom edge — its absence removes page navigation
- [ ] QA-005: Header height is exactly 18mm — deviations break the grid and push content below the correct margin
- [ ] QA-006: Footer height is exactly 12mm — deviations push content above the bottom margin
- [ ] QA-007: No content element overlaps the header or footer zones — overlap creates visual confusion
- [ ] QA-008: Main content area uses 8 of 12 columns — content in the wrong columns shifts the visual balance
- [ ] QA-009: Side panel uses 4 of 12 columns when present — must be the rightmost 4 columns
- [ ] QA-010: No content overlaps another content element without functional reason — overlapping elements are a layout error
- [ ] QA-011: Gutter between columns is exactly 4mm — incorrect gutters alter column widths and break alignment
- [ ] QA-012: Renders have minimum 8px padding from page edge and 8px from any non-render element — renders that touch edges look clipped
- [ ] QA-013: Body text line length does not exceed 75 characters in any column — long lines reduce reading speed
- [ ] QA-014: Print variant includes 3mm bleed for all full-page-edge elements (header, footer, side panel) — insufficient bleed causes white lines at trim
- [ ] QA-015: Safe area (8mm inside trim) is respected by all non-bleed elements — content in the unsafe zone may be trimmed in print

---

## Category 2 — Rendering

- [ ] QA-016: Cover render resolution is minimum 2480×3508px — below-minimum resolution is visible as blur in print
- [ ] QA-017: Full-page body renders are minimum 1240×1754px — same as QA-016 for body pages
- [ ] QA-018: Three-view orthographic renders (P002) are true orthographic projections — perspective distortion invalidates technical accuracy
- [ ] QA-019: Detail/zoom renders are minimum 800×800px — small renders blown up for zoom views look pixelated
- [ ] QA-020: Comparison renders (P009) are minimum 1240×620px per side — must be legible at half-page width
- [ ] QA-021: All render backgrounds are pure white (#FFFFFF) or transparent — non-white backgrounds introduce color casts
- [ ] QA-022: No AI generation artifacts visible in any render (floating geometry, distorted body panels, texture glitches) — artifacts undermine confidence in the manual
- [ ] QA-023: Paint finish in render matches `paintScheme.style` (gloss/flat/metallic) — wrong finish misrepresents the expected outcome
- [ ] QA-024: All colors visible in the render correspond to a color in the color scheme — unaccounted colors confuse the reader
- [ ] QA-025: Render lighting is consistent across all pages of the manual (same rig) — inconsistent lighting makes the manual feel unfinished
- [ ] QA-026: The cover render angle is 3/4 front-left at 15° elevation — per RENDER_GUIDE.md §2
- [ ] QA-027: No renders use environmental backgrounds, bokeh, or surface textures — non-white backgrounds violate ADR-006
- [ ] QA-028: Decals visible in renders are legible at display size — illegible decals in a render are misleading
- [ ] QA-029: No render is cropped tighter than 10% padding around the model body — over-cropping obscures the model shape
- [ ] QA-030: White balance is neutral — no warm or cool color cast on the white background of any render

---

## Category 3 — Typography

- [ ] QA-031: Title font is Bebas Neue or approved fallback (Impact, Arial Narrow Bold) — other fonts deviate from the design language
- [ ] QA-032: Body font is Source Sans Pro or approved fallback (Open Sans, Helvetica Neue) — see STYLE_GUIDE.md §2.1
- [ ] QA-033: Monospace font is JetBrains Mono or approved fallback (Courier New) — used for all paint codes and part numbers
- [ ] QA-034: Display level text (48pt) is used only on the cover — oversized text on body pages wastes space and breaks hierarchy
- [ ] QA-035: H1 (36pt) is used only for the primary title on a page — one H1 per page maximum
- [ ] QA-036: H2 (28pt) is used for section headings — not for body emphasis or decorative use
- [ ] QA-037: H3 (22pt) is used for component headers and sub-section titles — must be distinguishable from H2
- [ ] QA-038: Body text is 11pt — deviations affect readability and line count
- [ ] QA-039: Caption text is 9pt — used for image captions, table labels, supplementary text only
- [ ] QA-040: Label text is 8pt — used for component labels, badge text, all-caps identifiers only
- [ ] QA-041: Line heights match STYLE_GUIDE.md §2.2 per level — incorrect line heights affect reading rhythm
- [ ] QA-042: No orphans in body text (single word on the last line of a paragraph) — orphans are an editorial failure
- [ ] QA-043: No widows in body text (single line of a paragraph at the top of a column) — widows are an editorial failure
- [ ] QA-044: All-caps text used only in component labels and never in body text — all-caps body text is harder to read
- [ ] QA-045: Bold used only for critical information (warnings, required materials, mandatory steps) — overuse of bold eliminates its signal value

---

## Category 4 — Color and Palette

- [ ] QA-046: All structural colors (header, footer, side panel, borders) use token values from tokens.example.yaml — hardcoded colors may drift from the authoritative values
- [ ] QA-047: Page background is pure white (#FFFFFF) on every page — no tint, no OffWhite page background
- [ ] QA-048: Violet-background zones (C001, side panel) use exactly VioletPrimary (#5B2D8E) — any other violet is incorrect
- [ ] QA-049: Text on VioletPrimary is white (#FFFFFF) — no other color is permitted for text on violet
- [ ] QA-050: Text on white is Black (#1A1A1A) for primary text — not #000000, not pure gray
- [ ] QA-051: Red (#D32F2F) appears only in C008 Warning components — no decorative use
- [ ] QA-052: Gold (#C8A838) appears only in C009 Tips components — no decorative use
- [ ] QA-053: No more than 3 gold-accented elements per page — overuse dilutes the importance signal
- [ ] QA-054: Green (#388E3C) appears only in checklist completion states — no decorative use
- [ ] QA-055: Blue (#1976D2) appears only in C006 Callout components — no decorative use
- [ ] QA-056: No color combination in the manual fails WCAG 2.1 AA contrast (minimum 4.5:1 for body text) — inaccessible color combinations are a quality failure
- [ ] QA-057: Gold on white is never used for text (contrast ratio 2.3:1 fails WCAG) — use Black text with gold border instead
- [ ] QA-058: VioletLight (#8B5FBF) is not used for body text on white (contrast ratio 2.7:1 fails WCAG) — use VioletPrimary or Black instead
- [ ] QA-059: Paint swatch hex values in C011 match the `swatchHex` field in COLOR_SCHEME.yaml — inconsistent swatches mislead the reader
- [ ] QA-060: CMYK print variant has been color-proofed (or at minimum, designer has reviewed the CMYK conversion) — RGB-to-CMYK shift can significantly change perceived hue

---

## Category 5 — Components

- [ ] QA-061: C001 Header is present on all 10 pages — see COMPONENT_SYSTEM.md
- [ ] QA-062: C002 Footer is present on all 10 pages
- [ ] QA-063: C003 Palette is present on P002 and P009 (if P009 is included)
- [ ] QA-064: C004 Shopping List is present on P003
- [ ] QA-065: C005 Paint Sequence is present on P004 and P005
- [ ] QA-066: C013 Step Number is used for all numbered steps on P004–P008 — not inline text numbers
- [ ] QA-067: C014 Time Box is present for every step that has a mandatory waiting period
- [ ] QA-068: C008 Warning is used for all safety-critical or damage-risk information
- [ ] QA-069: C011 Paint Code Box accompanies every paint reference in P002, P005, P006, P007
- [ ] QA-070: C015 Notes is present at the bottom of P010

---

## Category 6 — Prompt Compliance

- [ ] QA-071: No unresolved `{{token.X}}` placeholders visible in any page output — placeholder text means the prompt was not fully filled
- [ ] QA-072: No unresolved `{{project.X}}` placeholders visible in any page output
- [ ] QA-073: All `{{project.X}}` values match the corresponding fields in PROJECT.yaml — copy-paste errors can introduce mismatches
- [ ] QA-074: Page type label in C001 right zone matches the page name in PAGE_SYSTEM.md exactly (e.g., "COLOR SCHEME" not "Colors")
- [ ] QA-075: All component IDs referenced in PromptEngine/ prompts exist in COMPONENT_SYSTEM.md
- [ ] QA-076: No page uses components not listed in its "Components Used" section in PAGE_SYSTEM.md without documented justification
- [ ] QA-077: The AI model used for generation is documented in `Projects/{ModelName}/Notes/qa_log.md`
- [ ] QA-078: The PromptEngine/ prompt version used is documented in qa_log.md (with the SDK version)
- [ ] QA-079: Any deviation from the standard prompt has been documented and reviewed
- [ ] QA-080: Re-generated pages (after QA failure) have been re-reviewed from QA-001 — a regenerated page can introduce new failures

---

## Category 7 — Assets

- [ ] QA-081: All render image paths in PROJECT.yaml resolve to existing files in `Projects/{ModelName}/Images/`
- [ ] QA-082: All renders used in the manual are the versions referenced in PROJECT.yaml (correct version suffix)
- [ ] QA-083: No renders from `Assets/ReferenceModels/` appear in manual pages — reference photos are reference only, not final renders
- [ ] QA-084: Approved renders have passed the full render quality checklist in `Core/RENDER_GUIDE.md` §7
- [ ] QA-085: No placeholder or stock images appear in any page output

---

## Category 8 — Workflow

- [ ] QA-086: All 10 required pages (P001–P010 minus optional P009) are present in the manual
- [ ] QA-087: PROJECT.yaml has no empty required fields (validate against Templates/PROJECT.yaml schema comments)
- [ ] QA-088: Manual output files are in `Projects/{ModelName}/Output/approved/` before PDF export
- [ ] QA-089: `Projects/{ModelName}/Notes/qa_log.md` documents this QA session with date and reviewer name
- [ ] QA-090: All previous QA failures documented in qa_log.md have been resolved before this approval

---

## Category 9 — Naming

- [ ] QA-091: Project folder name matches the official Tamiya model name with underscores for spaces (e.g., `Proto_Emperor`) — incorrect naming breaks cross-references
- [ ] QA-092: All output image files follow the naming pattern `{model-slug}_{pageId}_{descriptor}_{version}.{ext}` — per NAMING_CONVENTION.md
- [ ] QA-093: model-slug in file names is all lowercase with hyphens (e.g., `proto-emperor`) — mixed case causes issues on case-sensitive filesystems
- [ ] QA-094: No special characters (spaces, accented letters, ampersands) in any file or folder name — these cause parsing failures in automated pipelines
- [ ] QA-095: Version suffix in file names matches the `manualVersion` field in PROJECT.yaml

---

## Category 10 — PDF

- [ ] QA-096: PDF metadata Title field is populated per PDF_MASTER.md §6
- [ ] QA-097: PDF metadata Author, Subject, and Keywords fields are populated
- [ ] QA-098: PDF metadata Creator field reads "Mini4WD Manual SDK v{sdkVersion}"
- [ ] QA-099: All fonts are embedded as subsets in both PDF variants
- [ ] QA-100: Screen variant includes bookmarks per PDF_MASTER.md §7

---

## Category 11 — Content

- [ ] QA-101: No placeholder or lorem ipsum text appears in any page — any remaining placeholder text is a prompt failure
- [ ] QA-102: All steps on process pages (P004–P008) are numbered using C013
- [ ] QA-103: Every step that references a paint code includes a C011 Paint Code Box
- [ ] QA-104: All paint codes are in the correct format for the brand (e.g., Tamiya format: TS-29, XF-1, X-11)
- [ ] QA-105: The model name on the cover matches `{{project.modelName}}` exactly (including capitalization)
- [ ] QA-106: The paint scheme name on the cover matches `{{project.paintScheme.name}}` exactly
- [ ] QA-107: All materials in P003 correspond to paints and materials actually used in P004–P008
- [ ] QA-108: P010 Final Checklist includes at least 10 specific quality criteria (not generic)
- [ ] QA-109: All C008 Warning components include a specific consequence of ignoring the warning (not just "be careful")
- [ ] QA-110: No step on any page assumes knowledge that was not explained on an earlier page of the same manual
