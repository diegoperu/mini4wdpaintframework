# Page Module: P004 — Preparazione della Superficie

**Page ID:** P004 (permanent)
**Page Name:** Preparazione della Superficie (Surface Preparation)
**SDK Version:** 2.4.0

## Purpose
Step-by-step surface preparation guide before painting: cleaning, sanding, priming. Each step has a numbered badge and optional timer.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `steps[].id` | C013 Step Badge | Yes |
| `steps[].title` | Body text | Yes |
| `steps[].description` | Body text | Yes |
| `steps[].duration` | C014 Timer Badge | No |
| `steps[].warning` | C008 Warning Box | No |
| `steps[].tip` | C009 Tip Box | No |
| `warnings` | C008 Warning Box | No |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P004_exploded.png` — exploded view (optional, C007)

## Related
- `PromptEngine/Preparation.md`
- `Core/PAGE_SYSTEM.md §P004`
