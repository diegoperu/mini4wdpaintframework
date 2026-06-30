# Framework Integrity Tests

**Test Suite ID:** TEST-FW
**SDK Version:** 2.2.0
**Layer:** Framework
**Reference:** All Core/ documents, `Config/sdk.yaml`

## Purpose

Verify that the SDK itself is internally consistent: all referenced documents exist, all cross-references are valid, all page IDs and component IDs are consistently registered across `Core/`, `Config/`, and `PromptEngine/`.

## When to Run
- After any Core/ document is added or modified
- After any SDK version bump
- Before publishing a new SDK release
- When onboarding to a new environment (verify clone integrity)

---

## TEST-FW-001: All Required Documents Present

**Input:** Filesystem at project root
**Success Criteria:** Every file listed below exists and is non-empty

### Root Files
- [ ] `README.md`
- [ ] `CHANGELOG.md`
- [ ] `VERSION`
- [ ] `LICENSE`
- [ ] `STYLE_DECISIONS.md`
- [ ] `ROADMAP.md`
- [ ] `MANIFEST.yaml`

### Core/ Documents
- [ ] `Core/README.md`
- [ ] `Core/DESIGN_LANGUAGE.md`
- [ ] `Core/STYLE_GUIDE.md`
- [ ] `Core/COLOR_SYSTEM.md`
- [ ] `Core/PAGE_SYSTEM.md`
- [ ] `Core/COMPONENT_SYSTEM.md`
- [ ] `Core/RENDER_GUIDE.md`
- [ ] `Core/MANUAL_SYSTEM.md`
- [ ] `Core/PDF_MASTER.md`
- [ ] `Core/QA_SYSTEM.md`
- [ ] `Core/WORKFLOW.md`
- [ ] `Core/NAMING_CONVENTION.md`
- [ ] `Core/DOCUMENTATION_STYLE.md`
- [ ] `Core/DEFINITION_OF_DONE.md`
- [ ] `Core/AI_OPERATING_RULES.md`

### PromptEngine/ Files
- [ ] `PromptEngine/README.md`
- [ ] `PromptEngine/Cover.md`
- [ ] `PromptEngine/ColorScheme.md`
- [ ] `PromptEngine/Materials.md`
- [ ] `PromptEngine/Preparation.md`
- [ ] `PromptEngine/Painting.md`
- [ ] `PromptEngine/Masking.md`
- [ ] `PromptEngine/Details.md`
- [ ] `PromptEngine/Decals.md`
- [ ] `PromptEngine/Premium.md`
- [ ] `PromptEngine/FinalChecklist.md`

### Config/ Files
- [ ] `Config/README.md`
- [ ] `Config/sdk.yaml`
- [ ] `Config/render.yaml`
- [ ] `Config/pdf.yaml`
- [ ] `Config/quality.yaml`

### Build/ Files
- [ ] `Build/README.md`
- [ ] `Build/Pipeline.md`

### Tests/ Files
- [ ] `Tests/README.md`
- [ ] `Tests/FrameworkIntegrity.md`
- [ ] `Tests/PromptValidation.md`
- [ ] `Tests/LayoutValidation.md`
- [ ] `Tests/NamingValidation.md`
- [ ] `Tests/ColorValidation.md`
- [ ] `Tests/PDFValidation.md`
- [ ] `Tests/AssetsValidation.md`

### Knowledge/ Files
- [ ] `Knowledge/README.md`
- [ ] `Knowledge/Paints.md`
- [ ] `Knowledge/Masking.md`
- [ ] `Knowledge/Preparation.md`
- [ ] `Knowledge/Painting.md`
- [ ] `Knowledge/Decals.md`
- [ ] `Knowledge/ClearCoat.md`
- [ ] `Knowledge/Troubleshooting.md`
- [ ] `Knowledge/Glossary.md`
- [ ] `Knowledge/FAQ.md`
- [ ] `Knowledge/BestPractices.md`

### Directory READMEs
- [ ] `Build/README.md`
- [ ] `Config/README.md`
- [ ] `Tests/README.md`
- [ ] `Knowledge/README.md`
- [ ] `Templates/README.md`
- [ ] `Projects/README.md`
- [ ] `Assets/README.md`
- [ ] `Docs/README.md`
- [ ] `Assets/DesignSystem/README.md`
- [ ] `Assets/DesignSystem/Tokens/README.md`
- [ ] `Assets/DesignSystem/Components/README.md`
- [ ] `Assets/DesignSystem/Palette/README.md`
- [ ] `Assets/DesignSystem/Typography/README.md`
- [ ] `Assets/DesignSystem/Icons/README.md`
- [ ] `Assets/DesignSystem/Layout/README.md`
- [ ] `Assets/ReferenceModels/README.md`
- [ ] `Assets/ApprovedManual/README.md`
- [ ] `Assets/Examples/README.md`

**Output:** ✅ PASS if all present and non-empty | ❌ FAIL (blocking) if any missing

---

## TEST-FW-002: Page ID Registry Consistent

**Input:** `Core/PAGE_SYSTEM.md`, `Config/sdk.yaml §pages`, `PromptEngine/` directory, `Config/pdf.yaml §page_order`
**Success Criteria:** Every page ID appears consistently in all four sources

| Page ID | PAGE_SYSTEM.md | Config/sdk.yaml | PromptEngine file | Config/pdf.yaml |
|---------|---------------|-----------------|-------------------|-----------------|
| P001 | [ ] | [ ] | [ ] Cover.md | [ ] |
| P002 | [ ] | [ ] | [ ] ColorScheme.md | [ ] |
| P003 | [ ] | [ ] | [ ] Materials.md | [ ] |
| P004 | [ ] | [ ] | [ ] Preparation.md | [ ] |
| P005 | [ ] | [ ] | [ ] Painting.md | [ ] |
| P006 | [ ] | [ ] | [ ] Masking.md | [ ] |
| P007 | [ ] | [ ] | [ ] Details.md | [ ] |
| P008 | [ ] | [ ] | [ ] Decals.md | [ ] |
| P009 | [ ] | [ ] | [ ] Premium.md | [ ] |
| P010 | [ ] | [ ] | [ ] FinalChecklist.md | [ ] |

**Output:** ✅ PASS if all rows complete | ❌ FAIL (blocking) if any mismatch

---

## TEST-FW-003: Component ID Registry Consistent

**Input:** `Core/COMPONENT_SYSTEM.md`, `Config/sdk.yaml §components`, `Assets/DesignSystem/Components/README.md`
**Success Criteria:** All C001–C015 documented in all three sources

| Component ID | Name | COMPONENT_SYSTEM.md | Config/sdk.yaml | Components/README.md |
|-------------|------|--------------------|-----------------|-----------------------|
| C001 | Header | [ ] | [ ] | [ ] |
| C002 | Footer | [ ] | [ ] | [ ] |
| C003 | Palette | [ ] | [ ] | [ ] |
| C004 | Shopping List | [ ] | [ ] | [ ] |
| C005 | Paint Sequence | [ ] | [ ] | [ ] |
| C006 | Callout | [ ] | [ ] | [ ] |
| C007 | Exploded View | [ ] | [ ] | [ ] |
| C008 | Warning | [ ] | [ ] | [ ] |
| C009 | Tips | [ ] | [ ] | [ ] |
| C010 | Paint Legend | [ ] | [ ] | [ ] |
| C011 | Paint Code Box | [ ] | [ ] | [ ] |
| C012 | Zoom | [ ] | [ ] | [ ] |
| C013 | Step Number | [ ] | [ ] | [ ] |
| C014 | Time Box | [ ] | [ ] | [ ] |
| C015 | Notes | [ ] | [ ] | [ ] |

**Output:** ✅ PASS if all rows complete | ❌ FAIL (blocking) if any mismatch

---

## TEST-FW-004: Design Token Coverage

**Input:** `Assets/DesignSystem/Tokens/tokens.example.yaml`, `Assets/DesignSystem/Tokens/tokens.schema.yaml`
**Success Criteria:** All required tokens in schema are present in example file with correct values

- [ ] All `required` keys in `tokens.schema.yaml` exist in `tokens.example.yaml`
- [ ] `tokens.colors.primary.VioletPrimary` = `#5B2D8E` (exact)
- [ ] `tokens.colors.neutral.White` = `#FFFFFF` (exact — any other value is FAIL)
- [ ] All color token values match hex pattern `^#[0-9A-Fa-f]{6}$`
- [ ] All size tokens include unit (pt or px or mm)
- [ ] No `null` values for required tokens

**Output:** ✅ PASS if all checks pass | ❌ FAIL (blocking) if White ≠ #FFFFFF or required tokens missing

---

## TEST-FW-005: Version Consistency

**Input:** `VERSION`, `CHANGELOG.md`, `MANIFEST.yaml`, `Config/sdk.yaml`
**Success Criteria:** All version references agree

- [ ] `VERSION` file content follows SemVer `X.Y.Z`
- [ ] `Config/sdk.yaml sdk.version` = content of `VERSION`
- [ ] `MANIFEST.yaml sdk.version` = content of `VERSION`
- [ ] Latest entry in `CHANGELOG.md` matches content of `VERSION`

**Output:** ✅ PASS if all match | ❌ FAIL (blocking) if any mismatch

**Common Error:** Bumping `VERSION` without updating `Config/sdk.yaml` or `MANIFEST.yaml`.

---

## TEST-FW-006: Templates Completeness

**Input:** `Templates/` directory

- [ ] `Templates/PROJECT.yaml` exists and is non-empty
- [ ] `Templates/PROJECT.md` exists and is non-empty
- [ ] `Templates/CHECKLIST.md` exists and is non-empty
- [ ] `Templates/COLOR_SCHEME.yaml` exists and is non-empty
- [ ] `Templates/PDF_CONFIG.yaml` exists and is non-empty
- [ ] `Templates/README.md` exists and is non-empty

**Output:** ✅ PASS if all present | ⚠️ WARNING (non-blocking) if optional templates missing
