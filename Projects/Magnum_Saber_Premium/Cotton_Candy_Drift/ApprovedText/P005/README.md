# Page Module: P005 — Sequenza di Verniciatura

**Page ID:** P005 (permanent)
**Page Name:** Sequenza di Verniciatura (Paint Sequence)
**SDK Version:** 2.4.0

## Purpose
Ordered step-by-step painting sequence. Light colors before dark. Each step references a color from P002 via color_id — no duplicate paint codes.

## Content Fields

| Field | Component | Required |
|-------|-----------|----------|
| `title` | C001 Header | Yes |
| `sequence[].step` | C013 Step Badge | Yes |
| `sequence[].color_id` | C011 Paint Code Box | Yes |
| `sequence[].area` | Body text | Yes |
| `sequence[].technique` | Body text | Yes |
| `sequence[].coats` | Body text | Yes |
| `sequence[].drying_time` | C014 Timer Badge | Yes |
| `sequence[].notes` | C015 Notes Panel | No |
| `warnings` | C008 Warning Box | Yes |
| `tips` | C009 Tip Box | No |
| `footer.*` | C002 Footer | Yes |

## Render Dependencies
- No render images required — sequential step layout

## Related
- `PromptEngine/PaintSequence.md`
- `Core/PAGE_SYSTEM.md §P005`
- `Projects/Magnum_Saber_Premium/Cotton_Candy_Drift/ApprovedText/P002/content.yaml` — color_id must resolve here
