# Color Validation Tests

**Test Suite ID:** TEST-CL
**SDK Version:** 2.4.0
**Layer:** Color
**Reference:** `Core/COLOR_SYSTEM.md`, `Core/STYLE_GUIDE.md §1`, `Assets/DesignSystem/Tokens/tokens.example.yaml`, `Knowledge/Paints.md`

## Purpose

Verify that all colors in generated pages, configuration files, and project data match the approved palette and that paint codes are accurate references to real products.

## When to Run
- After Phase 2 (Prompt Engine) — verify no hardcoded hex in output
- After Phase 3 (Render Engine) — verify backgrounds are white
- During Phase 4 (QA) — run as part of full QA pass

---

## TEST-CL-001: Mandatory Colors Present

**Input:** All generated page images
**Success Criteria:** Mandatory colors appear on every page in correct roles

| Color Role | Token Name | Required Hex | Location | Check |
|-----------|------------|--------------|----------|-------|
| Header background | TamiyaPrimary | `#114B69` | C001 Header | [ ] |
| Page background | White | `#FFFFFF` | All pages | [ ] |
| Body text | DarkGray | `#4A4A4A` | All body text | [ ] |
| Warning borders | RedWarning | `#D32F2F` | C008 Warning (when present) | [ ] |
| Tip borders | GoldAccent | `#C8A838` | C009 Tips (when present) | [ ] |

**Output:** ✅ PASS if all mandatory colors present and correct | ❌ FAIL (blocking) if TamiyaPrimary or White are wrong

---

## TEST-CL-002: Token Hex Value Accuracy

**Input:** `Assets/DesignSystem/Tokens/tokens.example.yaml`
**Success Criteria:** Core palette tokens have not been altered from their defined values

Verify exact values (case-insensitive hex):
- [ ] `tokens.colors.primary.TamiyaPrimary` = `#114B69`
- [ ] `tokens.colors.primary.TamiyaDark` = `#0B2F42`
- [ ] `tokens.colors.primary.TamiyaLight` = `#76ABC7`
- [ ] `tokens.colors.neutral.White` = `#FFFFFF` — **any other value is an immediate FAIL**
- [ ] `tokens.colors.neutral.DarkGray` = `#4A4A4A`
- [ ] `tokens.colors.neutral.Black` = `#1A1A1A`
- [ ] `tokens.colors.accent.GoldAccent` = `#C8A838`
- [ ] `tokens.colors.semantic.RedWarning` = `#D32F2F`
- [ ] `tokens.colors.semantic.GreenSuccess` = `#388E3C`

**Output:** ✅ PASS if all exact | ❌ FAIL (blocking) if White ≠ #FFFFFF or TamiyaPrimary ≠ #114B69

---

## TEST-CL-003: Background Color Compliance

**Input:** All generated page image files
**Reference:** `Config/render.yaml §background`, `Config/quality.yaml §thresholds.background_white_tolerance_rgb`
**Rule:** Page backgrounds must be pure white (#FFFFFF), max RGB deviation 5 per channel

For each page image:
- [ ] Background area is #FFFFFF ± 5 per RGB channel
- [ ] Cover page (P001) background under render is white
- [ ] No gradient backgrounds on any page
- [ ] No environmental backgrounds (no floor, studio, desk)
- [ ] TamiyaPrimary side panel is in 4-column panel only — not full-page background

**How to verify:** Sample background pixel in image editor. RGB must be (250–255, 250–255, 250–255) minimum.

**Output:** ✅ PASS if all backgrounds within tolerance | ❌ FAIL (blocking) if any background fails

**Common Errors:**
- AI generates off-white (#FAFAFA = RGB 250,250,250) — borderline, document and monitor
- AI generates light gray (#F0F0F0) — reject and regenerate
- TamiyaPrimary side panel accidentally fills full page width

---

## TEST-CL-004: No Hardcoded Colors in Prompts

**Input:** All `PromptEngine/` files
**Rule:** Colors in prompts must be referenced by token name, never by hardcoded hex value

- [ ] Scan all PromptEngine/ files for bare hex pattern `#[0-9A-Fa-f]{6}`
- [ ] Any hex found in a prompt (outside of a note or example) is a WARN
- [ ] Exception: references to #FFFFFF for "white background" are acceptable when not a component color
- [ ] Exception: `tokens.example.yaml` itself defines hex values — OK

**Output:** ✅ PASS if no hardcoded component colors found | ⚠️ WARNING if any hex found in prompt templates

---

## TEST-CL-005: Paint Code Validation

**Input:** `Projects/{ModelName}/PROJECT.yaml §paintScheme.colors[]`
**Reference:** `Knowledge/Paints.md`
**Rule:** All paint codes must be real, documented product codes from known brands

For each color in `paintScheme.colors`:
- [ ] `paintBrand` is a recognized brand (Tamiya, Mr.Hobby, Vallejo, Citadel, AK Interactive, Gunze)
- [ ] `paintCode` follows brand code format:
  - Tamiya lacquer: `TS-##`
  - Tamiya acrylic: `XF-##` or `X-##`
  - Mr.Hobby: `C-###` or `GX-###`
  - Vallejo: 5-digit numeric code `#####`
- [ ] `paintCode` cross-references with `Knowledge/Paints.md` (if listed there)
- [ ] `finish` field is one of: `gloss`, `matte`, `satin`, `metallic`, `pearl`, `flat`
- [ ] `hex` field (if provided) is a valid hex color

> ⚠️ **Warning:** Never assume a paint code is correct without verifying against `Knowledge/Paints.md` or manufacturer documentation. AI models can hallucinate paint codes.

**Output:** ✅ PASS if all codes valid | ❌ FAIL (blocking) if any code format is invalid or brand unrecognized

---

## TEST-CL-006: Color Contrast for Accessibility

**Input:** Typography color combinations used in generated pages
**Reference:** `Core/COLOR_SYSTEM.md §Accessibility`
**Rule:** Text must meet WCAG AA minimum contrast ratio (4.5:1 for body text)

Key combinations to check:
- [ ] White text on TamiyaPrimary (#114B69): contrast ratio ≥ 4.5:1 ✓ (reference: ~9.4:1)
- [ ] DarkGray (#4A4A4A) on White (#FFFFFF): ≥ 4.5:1 ✓ (reference: ~9.7:1)
- [ ] Black (#1A1A1A) on White (#FFFFFF): ≥ 4.5:1 ✓ (reference: ~17.1:1)
- [ ] White on GoldAccent (#C8A838): ≥ 4.5:1 — **WARN, this combination may fail** (reference: ~2.3:1)

> 📝 **Note:** White text on GoldAccent fails WCAG AA. Never use this combination for body text. GoldAccent is for borders and decorative elements only.

**Output:** ✅ PASS if body text combinations all pass 4.5:1 | ❌ FAIL if white-on-gold used for body text
