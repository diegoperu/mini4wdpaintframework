# Paints

**Document ID:** KNW-PAI-001
**SDK Version:** 2.2.0
**Category:** Materials Reference

---

## Overview

This document provides reference information for paint products commonly used in Mini4WD painting. It covers major brands, product line structures, code formats, and finish types. All paint codes referenced in `PROJECT.yaml` should be verifiable against this document or the manufacturer's official catalog.

---

## Paint Brands

### Tamiya

**Product Lines:**

| Line | Prefix | Application | Finish |
|------|--------|-------------|--------|
| TS Spray | TS-## | Spray can | Gloss, Semi-gloss, Matte |
| PS Spray | PS-## | Polycarbonate bodies | Gloss |
| X Acrylic | X-## | Brush/airbrush | Gloss |
| XF Acrylic | XF-## | Brush/airbrush | Flat/Matte |
| LP Lacquer | LP-## | Brush/airbrush | Various |

**Code Format:** `TS-57`, `X-11`, `XF-16`, `PS-48`
**Thinner:** Tamiya Lacquer Thinner (for LP), Tamiya Acrylic Thinner (for X/XF), Tamiya Spray (TS/PS are self-propelled)

**Selected TS Colors (Spray):**

| Code | Color | Finish |
|------|-------|--------|
| TS-1 | Red Brown | Gloss |
| TS-6 | Matt Black | Matte |
| TS-14 | Black | Gloss |
| TS-17 | Gloss Aluminum | Metallic |
| TS-26 | Pure White | Gloss |
| TS-29 | Racing Green | Gloss |
| TS-30 | Silver Leaf | Metallic |
| TS-38 | Gun Metal | Metallic |
| TS-40 | Metal Black | Metallic |
| TS-57 | Blue Violet | Gloss |
| TS-58 | Pearl Light Blue | Pearl |
| TS-63 | NATO Black | Matte |
| TS-65 | Pearl Clear | Pearl |
| TS-76 | Mica Red | Metallic |
| TS-83 | Metallic Silver | Metallic |
| TS-84 | Metallic Gold | Metallic |
| TS-86 | Pure Red | Gloss |
| TS-92 | Metallic Orange | Metallic |

---

### Mr. Hobby (GSI Creos)

**Product Lines:**

| Line | Prefix | Application | Finish |
|------|--------|-------------|--------|
| Mr. Color | C-## | Brush/airbrush | Various |
| Aqueous | H-## | Brush/airbrush | Various |
| Mr. Metallic Color | SM-## | Airbrush | Metallic |
| Mr. Color GX | GX-## | Brush/airbrush | Various |

**Code Format:** `C-5`, `H-22`, `SM-01`, `GX-1`

**Selected Mr. Color:**

| Code | Color | Finish |
|------|-------|--------|
| C-1 | White | Gloss |
| C-2 | Black | Gloss |
| C-5 | Red | Gloss |
| C-8 | Silver | Metallic |
| C-14 | Navy Blue | Gloss |
| C-17 | RLM Grey | Semi-gloss |
| C-47 | Red Brown | Gloss |
| C-67 | Indigo Blue | Gloss |
| C-78 | Cobalt Blue | Gloss |
| C-89 | Metallic Black | Metallic |

---

### Vallejo

**Product Lines:**

| Line | Code Format | Application | Finish |
|------|-------------|-------------|--------|
| Model Color | 70.### | Brush | Matte/Gloss variants |
| Game Color | 72.### | Brush | Matte/Gloss variants |
| Model Air | 71.### | Airbrush | Various |
| Mecha Color | 69.### | Brush/airbrush | Various |

**Code Format:** `70.001`, `72.104`, `71.062`

---

## Finish Types

| Finish | Description | Top Coat Required |
|--------|-------------|-------------------|
| Gloss | High shine, reflective | Optional |
| Semi-gloss | Medium shine | Optional |
| Matte/Flat | No shine, diffuse | Often recommended |
| Satin | Midpoint between gloss and matte | Optional |
| Metallic | Contains metallic flake, reflective | Recommended |
| Pearl | Pearlescent sheen, color-shifting | Recommended |
| Chrome | Mirror-like, extremely reflective | No top coat |

---

## Paint Code Validation Rules

When entering paint codes in `PROJECT.yaml`:

1. **Tamiya TS:** Format `TS-##` — verify against official Tamiya catalog
2. **Tamiya X/XF:** Format `X-##` or `XF-##`
3. **Mr. Color:** Format `C-##` — verify against GSI Creos catalog
4. **Vallejo:** Format `##.###` — 2-digit line + 3-digit color
5. **Never invent codes** — see `Core/AI_OPERATING_RULES.md RULE-001`

If a paint is unavailable or discontinued: note in `paintScheme.colors[].notes` and list a verified substitute.

---

## Thinners and Mediums

| Product | Compatible Paints | Ratio |
|---------|------------------|-------|
| Tamiya Lacquer Thinner | Tamiya LP series | 1:1 to 2:1 (paint:thinner) |
| Tamiya Acrylic Thinner | Tamiya X/XF series | 1:1 |
| Mr. Color Thinner | Mr. Color C series | 1:1 to 1:2 |
| Vallejo Airbrush Thinner | Vallejo Model Air | Variable |

---

## Related Documents
- `Knowledge/Preparation.md` — surface prep before painting
- `Knowledge/Painting.md` — application techniques
- `Knowledge/ClearCoat.md` — finishing products
- `Projects/{ModelName}/PROJECT.yaml` — project-specific paint selections
