# Color System

This document is the authoritative reference for all colors used in the Mini4WD Manual SDK. Every color that appears on a manual page must be defined here. Colors not in this document are not permitted in SDK output.

See also: `STYLE_GUIDE.md` §1 for a working reference table, `Assets/DesignSystem/Tokens/tokens.example.yaml` for the machine-readable values.

---

## 1. Color Philosophy

Color in this system is not decoration — it is communication. Every color has exactly one role. That role is defined in this document and must not be reinterpreted.

The palette is intentionally minimal. Fewer colors used consistently is more powerful than many colors used loosely. When reviewing a page, ask: does every color here have a reason to be here?

The hierarchy of color roles:
1. **Structural** — defines the identity and layout of the page (primary, white)
2. **Functional** — communicates a specific type of information (red = danger, gold = important, green = complete, blue = info)
3. **Content** — represents real-world data (paint swatches only)

Colors in roles 1 and 2 are fully specified here. Colors in role 3 (paint swatches) must accurately represent real paint colors and are documented per project in `Templates/COLOR_SCHEME.yaml`.

---

## 2. Primary Colors

Derived from the Tamiya "Star Mark" logo (blue star, `#1D95D3`), darkened and
desaturated so it never reads as `BlueInfo` at a glance — see `STYLE_DECISIONS.md`
ADR-023 (supersedes ADR-007, which chose violet specifically to avoid any
manufacturer association; ADR-023 records the tradeoff of adopting a
Tamiya-derived identity instead).

### TamiyaPrimary

The primary brand color and the most important structural color in the system.

| Property | Value |
|---|---|
| Hex | `#114B69` |
| RGB | 17, 75, 105 |
| CMYK | 84, 29, 0, 59 |
| Pantone | Not determined — verify against a physical swatch before print production |
| Token | `{{token.TamiyaPrimary}}` |

**Usage:** Header band (C001), side panel background, step number circles (C013), component borders where a primary-color accent is specified.

**Never use for:** Body text on white, warning indicators, backgrounds other than the defined zones.

---

### TamiyaDark

Used for depth, pressed states, and text rendered within primary-color zones when additional contrast is needed.

| Property | Value |
|---|---|
| Hex | `#0B2F42` |
| RGB | 11, 47, 66 |
| CMYK | 83, 29, 0, 74 |
| Token | `{{token.TamiyaDark}}` |

**Usage:** Monospace paint codes on white background, text shadow on primary-color header, decorative ruled lines in primary-color zones.

---

### TamiyaLight

Used for dividers and secondary elements within primary-color-background zones.

| Property | Value |
|---|---|
| Hex | `#76ABC7` |
| RGB | 118, 171, 199 |
| CMYK | 41, 14, 0, 22 |
| Token | `{{token.TamiyaLight}}` |

**Usage:** Divider lines inside the side panel, secondary borders on primary-color components.

---

## 3. Neutral Colors

### White

The mandatory page background. No page background may deviate from this value.

| Property | Value |
|---|---|
| Hex | `#FFFFFF` |
| RGB | 255, 255, 255 |
| CMYK | 0, 0, 0, 0 |
| Token | `{{token.White}}` |

---

### OffWhite

Used for alternating table rows, code blocks, and component backgrounds that need subtle differentiation from the page background.

| Property | Value |
|---|---|
| Hex | `#F8F8F8` |
| RGB | 248, 248, 248 |
| CMYK | 0, 0, 0, 3 |
| Token | `{{token.OffWhite}}` |

---

### LightGray

Used for dividers, borders, and grid lines on white backgrounds.

| Property | Value |
|---|---|
| Hex | `#E8E8E8` |
| RGB | 232, 232, 232 |
| CMYK | 0, 0, 0, 9 |
| Token | `{{token.LightGray}}` |

---

### MidGray

Used for captions, secondary labels, and inactive states.

| Property | Value |
|---|---|
| Hex | `#9B9B9B` |
| RGB | 155, 155, 155 |
| CMYK | 0, 0, 0, 39 |
| Token | `{{token.MidGray}}` |

---

### DarkGray

Used for secondary body text, notes, and supplementary information.

| Property | Value |
|---|---|
| Hex | `#4A4A4A` |
| RGB | 74, 74, 74 |
| CMYK | 0, 0, 0, 71 |
| Token | `{{token.DarkGray}}` |

---

### Black

The primary text color. Near-black, not pure black.

| Property | Value |
|---|---|
| Hex | `#1A1A1A` |
| RGB | 26, 26, 26 |
| CMYK | 0, 0, 0, 90 |
| Token | `{{token.Black}}` |

> 📝 **Note:** Pure black (#000000) is not used in text. It creates harsh contrast and can appear as a registration mark indicator in some offset printing workflows. #1A1A1A is visually indistinguishable from pure black at reading distance.

---

## 4. Accent Colors

### GoldAccent

The premium highlight color. Used sparingly to draw attention to the most important information.

| Property | Value |
|---|---|
| Hex | `#C8A838` |
| RGB | 200, 168, 56 |
| CMYK | 0, 16, 72, 22 |
| Token | `{{token.GoldAccent}}` |

**Usage:** Tips component (C009) left border, premium page marker (P009), important callout accent.
**Limit:** No more than three gold elements per page. Overuse destroys the signal.

---

### TamiyaAccent

Derived from the Tamiya "Star Mark" logo's red star (`#EC2227`), darkened and
desaturated so it never reads as `RedWarning` at a glance — see
`STYLE_DECISIONS.md` ADR-023. Sparing decorative use only.

| Property | Value |
|---|---|
| Hex | `#851E21` |
| RGB | 133, 30, 33 |
| CMYK | 0, 77, 75, 48 |
| Token | `{{token.TamiyaAccent}}` |

**Usage:** Cover kicker underline, optional decorative brand accent.
**Never use for:** Warning indicators — `RedWarning` is the only red permitted for danger/error signaling. If it signals danger, it must be `RedWarning`, not `TamiyaAccent`.

---

### RedWarning

Exclusive to warnings, errors, and critical information. Never used decoratively.

| Property | Value |
|---|---|
| Hex | `#D32F2F` |
| RGB | 211, 47, 47 |
| CMYK | 0, 78, 78, 17 |
| Token | `{{token.RedWarning}}` |

**Usage:** Warning component (C008) left border and icon, text for safety-critical notices.
**Rule:** If it is red, it is a warning. If it is not a warning, it must not be red.

---

### GreenSuccess

Used for checklist completion, success states, and confirmation markers.

| Property | Value |
|---|---|
| Hex | `#388E3C` |
| RGB | 56, 142, 60 |
| CMYK | 61, 0, 58, 44 |
| Token | `{{token.GreenSuccess}}` |

**Usage:** Completed checklist items in C010 and P010 Final Checklist.

---

### BlueInfo

Used for informational callouts and notes that are neither warnings nor tips.

| Property | Value |
|---|---|
| Hex | `#1976D2` |
| RGB | 25, 118, 210 |
| CMYK | 88, 44, 0, 18 |
| Token | `{{token.BlueInfo}}` |

**Usage:** Callout component (C006) left border and icon.

---

## 5. Color Roles Summary

| Color | Role | May appear in |
|---|---|---|
| TamiyaPrimary | Structural — identity | Header, side panel, step circles |
| TamiyaDark | Structural — depth | Mono codes on white, text shadow |
| TamiyaLight | Structural — secondary | Dividers inside primary-color zones |
| White | Structural — background | Page background (mandatory) |
| OffWhite | Structural — subtle fill | Tables, code blocks |
| LightGray | Structural — dividers | Borders, rules on white |
| MidGray | Functional — secondary text | Captions, labels |
| DarkGray | Functional — tertiary text | Notes, supplementary |
| Black | Functional — primary text | All body text, headings |
| GoldAccent | Functional — important | Tips, premium, max 3 per page |
| TamiyaAccent | Functional — decorative brand accent | Cover kicker underline, sparingly |
| RedWarning | Functional — danger | Warnings only |
| GreenSuccess | Functional — complete | Checklist completion |
| BlueInfo | Functional — information | Informational callouts |

---

## 6. Forbidden Color Combinations

The following combinations are prohibited for accessibility and design integrity reasons:

| Combination | Reason |
|---|---|
| Red text on white at below 14pt | Fails WCAG 2.1 AA contrast at small sizes |
| Gold text on white | Fails WCAG 2.1 AA (ratio 2.3:1) — use Black text with gold border instead |
| TamiyaLight on White body text | Fails WCAG 2.1 AA (ratio 2.5:1) |
| Red on green or green on red | Color blindness failure; cannot be distinguished by deuteranopia |
| TamiyaPrimary on TamiyaDark (or reverse) | Insufficient contrast (ratio 1.5:1) for text |

---

## 7. Dark Background Rules

Dark backgrounds (TamiyaPrimary, TamiyaDark) appear only in these defined zones:
- C001 Header band
- C002 Footer accent line (3px top border only — background is white)
- Side panel (4-column zone on right of content pages)
- C013 Step Number circles

**Text on dark backgrounds must be White (#FFFFFF).** No exceptions. Do not use Black, Gold, or any other color for text on primary-color backgrounds.

---

## 8. Paint Color Mapping

Paint swatches in C003 Palette and C011 Paint Code Box represent real model paint colors. These colors fall outside the SDK palette. The following rules govern their representation:

**Accuracy requirement:** The swatch color must visually represent the actual paint as closely as possible on a calibrated sRGB monitor. The swatch is a communication aid, not a color sample.

**Calibration source:** When available, use the manufacturer's official sRGB hex value. When not available, photograph a painted swatch under Studio Neutral lighting and sample from the center of the painted area.

**Representation in PROJECT.yaml:** Each paint color in the project's color scheme includes an `swatchHex` field. This hex value is used in the C011 Paint Code Box.

**Print note:** Paint swatch colors are printed using the PDF's color profile (CMYK FOGRA39 for print). The CMYK conversion may shift hue significantly for highly saturated paint colors. A print proof is required for any manual that will be physically printed.

**Example documented paint references:**

| Paint Code | Paint Name | Approx. sRGB Hex |
|---|---|---|
| TS-1 | Red | `#CC2222` |
| TS-3 | Yellow | `#FFCC00` |
| TS-14 | Black | `#1A1A1A` |
| TS-15 | Blue | `#1144AA` |
| TS-17 | Gloss Aluminum | `#BBBBCC` |
| TS-18 | Metallic Red | `#992222` |
| TS-19 | Metallic Blue | `#224499` |
| TS-29 | Semi-Gloss Black | `#2A2A2A` |
| TS-30 | Silver Leaf | `#AAAAAA` |
| TS-36 | Fluorescent Red | `#FF3333` |
| TS-37 | Lavender | `#9977BB` |
| TS-53 | Light Metallic Blue | `#5577AA` |
| TS-55 | Dark Copper | `#8B4513` |
| TS-63 | Nato Black | `#222222` |
| TS-76 | Mica Silver | `#C0C0C0` |
| TS-80 | Flat Black | `#1C1C1C` |
| TS-83 | Metallic Silver | `#C8C8CC` |
| TS-86 | Pure White | `#F5F5F5` |
| TS-87 | Titanium Silver | `#B0B0B8` |
| XF-1 | Flat Black | `#1A1A1A` |
| X-11 | Chrome Silver | `#E8E8E8` |

> 📝 **Note:** These hex approximations are for documentation reference only. Do not use them as color standards. Verify each value against a physical paint swatch or manufacturer specification before including in an approved manual.

---

## 9. Color Naming Convention

All colors in the SDK follow the pattern: `{Role}{Descriptor}` in PascalCase.

- Role prefix: `Tamiya`, `Gray`, `Red`, `Green`, `Blue`, `Gold`, `White`, `Black`
- Descriptor suffix (optional): `Primary`, `Dark`, `Light`, `Accent`, `Warning`, `Success`, `Info`

New colors added to the palette (via ADR) must follow this convention. Color names must be unique across the token file. Avoid names that imply a specific use case that might change (e.g., do not name a color `ButtonBackground` — name it by its visual property).

---

## 10. Token Mapping

Every color in this document maps to exactly one Design Token in `Assets/DesignSystem/Tokens/tokens.example.yaml`. The mapping is:

| Color Name | Token Key |
|---|---|
| TamiyaPrimary | `token.TamiyaPrimary` |
| TamiyaDark | `token.TamiyaDark` |
| TamiyaLight | `token.TamiyaLight` |
| White | `token.White` |
| OffWhite | `token.OffWhite` |
| LightGray | `token.LightGray` |
| MidGray | `token.MidGray` |
| DarkGray | `token.DarkGray` |
| Black | `token.Black` |
| GoldAccent | `token.GoldAccent` |
| TamiyaAccent | `token.TamiyaAccent` |
| RedWarning | `token.RedWarning` |
| GreenSuccess | `token.GreenSuccess` |
| BlueInfo | `token.BlueInfo` |

If you need to add a color to the system, you must: (1) add it to this document, (2) add it to `tokens.example.yaml`, (3) add it to `tokens.schema.yaml`, and (4) file an ADR in `STYLE_DECISIONS.md`.
