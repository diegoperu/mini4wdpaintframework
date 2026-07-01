# Page Module: P006 — Guida alla Mascheratura

**Page ID:** P006 (permanent)
**Page Name:** Guida alla Mascheratura (Masking Guide)
**SDK Version:** 2.4.0

## Purpose
Masking zone table and numbered application sequence. Zoom panels show tape placement detail. Warning for paint bleed risk is mandatory.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `zones[].id` | Body table | Yes |
| `zones[].area` | Body table | Yes |
| `zones[].masking_type` | Body table | Yes |
| `zones[].order` | Body table | Yes |
| `sequence[].step` | C013 Step Badge | Yes |
| `sequence[].description` | Body text | Yes |
| `sequence[].tip` | C009 Tip Box | No |
| `callouts[].title` | C006 Callout Box | No |
| `callouts[].body` | C006 Callout Box | No |
| `warnings` | C008 Warning Box | Yes |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- `P006_masking_zoom.png` — close-up masking detail (optional, C012)

## Related
- `PromptEngine/Masking.md`
- `Core/PAGE_SYSTEM.md §P006`
