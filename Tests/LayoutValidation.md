# Layout Validation Tests

**Test Suite ID:** TEST-LY
**SDK Version:** 2.4.0
**Layer:** Visual Layout
**Reference:** `Core/STYLE_GUIDE.md §4`, `Assets/DesignSystem/Layout/README.md`, `Core/COMPONENT_SYSTEM.md`, `Config/render.yaml §resolution`

## Purpose

Verify that generated pages conform to the grid system, margin requirements, spacing specifications, and component placement rules defined in the SDK style system.

## When to Run
- After Phase 2 (Prompt Engine) to verify page layout descriptions
- After Phase 3 (Render Engine) to verify visual page images
- Before Phase 4 (QA) as a pre-flight check

---

## TEST-LY-001: Page Dimensions

**Input:** Generated page image files in `Projects/{ModelName}/Images/` and `Output/`
**Reference:** `Config/render.yaml §resolution`

For each generated page image:
- [ ] Print variant: Width = 2480px (±10px), Height = 3508px (±10px)
- [ ] Screen variant: Width = 1240px (±5px), Height = 1754px (±5px)
- [ ] Aspect ratio = 1:1.414 (A4 portrait) — tolerance ±0.005
- [ ] Color space = sRGB (verify with image inspector)

**Output:** ✅ PASS if all dimensions within tolerance | ❌ FAIL (blocking) if any page wrong size

---

## TEST-LY-002: Header Zone Integrity (C001)

**Input:** All 10 generated page images
**Reference:** `Core/COMPONENT_SYSTEM.md §C001`, `Assets/DesignSystem/Tokens/tokens.example.yaml §sizing.HeaderHeight`

For each page:
- [ ] Header band present at top of page
- [ ] Header height = 18mm (212px @300dpi / 106px @150dpi) — tolerance ±4px
- [ ] Header background = VioletPrimary (`#5B2D8E`) — no other color accepted
- [ ] "Mini4WD Manual" wordmark visible on left side
- [ ] Page type label visible on right side (e.g., "COVER", "COLOR SCHEME")
- [ ] No content from page body bleeds into header zone

**Output:** ✅ PASS if all headers correct | ❌ FAIL (blocking) if any header missing or wrong color

---

## TEST-LY-003: Footer Zone Integrity (C002)

**Input:** All 10 generated page images
**Reference:** `Core/COMPONENT_SYSTEM.md §C002`, `Assets/DesignSystem/Tokens/tokens.example.yaml §sizing.FooterHeight`

For each page:
- [ ] Footer band present at bottom of page
- [ ] Footer height = 12mm (142px @300dpi / 71px @150dpi) — tolerance ±4px
- [ ] Page number visible (P001 through P010) and correct for that page
- [ ] No content from page body bleeds into footer zone
- [ ] Footer background is LightGray (`#E8E8E8`) or White (`#FFFFFF`)

**Output:** ✅ PASS if all footers correct | ❌ FAIL (blocking) if page numbers incorrect or footer missing

---

## TEST-LY-004: Content Area Margins

**Input:** All 10 generated page images
**Reference:** `Core/STYLE_GUIDE.md §4`, `Assets/DesignSystem/Tokens/tokens.example.yaml §spacing`

Measure from page edge (not header/footer edge):
- [ ] Left margin ≥ 18mm from page edge
- [ ] Right margin ≥ 18mm from page edge
- [ ] Top content starts ≥ 15mm below header bottom edge
- [ ] Bottom content ends ≥ 20mm above footer top edge
- [ ] No text, renders, or component elements outside margin bounds

**Output:** ✅ PASS if all margins respected | ⚠️ WARNING (non-blocking) for minor violations (±2mm)

---

## TEST-LY-005: Layout Pattern Correctness

**Input:** All generated pages
**Reference:** `Assets/DesignSystem/Layout/README.md §Layout Patterns`

Identify the layout type for each page and verify the correct pattern is used:

| Page | Expected Layout Pattern | Violet Side Panel | Two Columns | Check |
|------|------------------------|-------------------|-------------|-------|
| P001 Cover | Full-bleed render | No | No | [ ] |
| P002 Color Scheme | Two-column (8+4) | Yes | Yes | [ ] |
| P003 Materials | Two-column (8+4) | Yes | Yes | [ ] |
| P004 Preparation | Three-panel | No | No | [ ] |
| P005 Painting | Three-panel | No | No | [ ] |
| P006 Masking | Two-column (8+4) | Yes | Yes | [ ] |
| P007 Details | Two-column (8+4) | Yes | Yes | [ ] |
| P008 Decals | Two-column (8+4) | Yes | Yes | [ ] |
| P009 Premium Variant | Two-column (8+4) | Yes | Yes | [ ] |
| P010 Final Checklist | Two-column checklist | No | Yes | [ ] |

**Output:** ✅ PASS if all pages use correct layout | ⚠️ WARNING (non-blocking) for minor deviations

---

## TEST-LY-006: Violet Side Panel

**Input:** Pages using two-column layout (P002, P003, P006, P007, P008, P009)
**Reference:** `Assets/DesignSystem/Layout/README.md`

For each two-column page:
- [ ] Side panel is in RIGHT column (4 of 12 grid columns)
- [ ] Side panel background = VioletPrimary (`#5B2D8E`) — not VioletLight, not VioletDark
- [ ] Side panel extends full height of content area
- [ ] Text in side panel is white (`#FFFFFF`)
- [ ] Side panel does NOT extend to full page width

**Output:** ✅ PASS if all panels correct | ❌ FAIL (blocking) if full-page violet background used

---

## TEST-LY-007: Component Spacing and Style

**Input:** All generated pages
**Reference:** `Core/COMPONENT_SYSTEM.md`, `Assets/DesignSystem/Tokens/tokens.example.yaml §borders`

- [ ] All callout boxes (C006) have 4px corner radius (`{{token.BorderRadius}}`)
- [ ] All warning boxes (C008) have 4px left border in `RedWarning (#D32F2F)`
- [ ] All tip boxes (C009) have 4px left border in `GoldAccent (#C8A838)`
- [ ] Step numbers (C013) visually separated from step text (minimum 8px gap)
- [ ] Time boxes (C014) right-aligned within their column
- [ ] Paint code boxes (C011) use `MonoFont` (JetBrains Mono or fallback)

**Output:** ✅ PASS if all spacing correct | ⚠️ WARNING (non-blocking) for minor spacing deviations

**Common Errors:**
- Content area touching header band with no gap
- Footer displaying wrong page ID
- Violet side panel using VioletLight (#8B5FBF) instead of VioletPrimary (#5B2D8E)
- Warning box using gold border instead of red
