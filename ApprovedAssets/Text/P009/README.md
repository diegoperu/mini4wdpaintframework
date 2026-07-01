# Page Module: P009 — Variante Premium

**Page ID:** P009 (permanent)
**Page Name:** Variante Premium (Premium Variant)
**SDK Version:** 2.4.0
**Conditional:** YES — generated only when `PROJECT.yaml premiumVariant.enabled: true`

## Purpose
Optional premium variant guide documenting additional materials and special techniques for an enhanced finish beyond the base manual.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `variant_name` | Body text | Yes |
| `description` | C015 Notes Panel | Yes |
| `additional_materials[].name` | Body table | No |
| `special_techniques[].step` | Body text | No |
| `special_techniques[].title` | Body text | No |
| `special_techniques[].description` | Body text | No |
| `comparison_notes` | C006 Callout Box | No |
| `warnings` | C008 Warning Box | No |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P009_premium_comparison.png` — base vs. premium side-by-side (optional)

## Conditional Logic
```
IF PROJECT.yaml premiumVariant.enabled = true → include P009 after P008
IF PROJECT.yaml premiumVariant.enabled = false → skip P009, P010 follows P008
```

## Related
- `PromptEngine/PremiumVariant.md`
- `Core/PAGE_SYSTEM.md §P009`
