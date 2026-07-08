# Assets/DesignSystem/

**Version:** 2.1.0
**Depends on:** Core/STYLE_GUIDE.md (authoritative)
**Implemented by:** All PromptEngine/ prompts, all PDF export pipelines

---

## Purpose

`DesignSystem/` is the concrete implementation of the abstract specifications defined in `Core/STYLE_GUIDE.md`. Where `STYLE_GUIDE.md` says "the header height is 18mm", this directory contains the YAML token file where that value lives as a resolvable token: `{{token.HeaderHeight}}`.

This directory is the **single source of truth for all visual values** used when generating manual pages. No prompt, no component, and no export config should hardcode a visual value — they must all reference a token from `Tokens/`.

---

## Subdirectory Overview

| Directory | Purpose |
|-----------|---------|
| `Tokens/` | Design token YAML files — the atomic values for every visual property |
| `Components/` | Wireframe specifications and dimension tables for components C001–C015 |
| `Palette/` | Color swatch documentation, usage rules, forbidden combinations |
| `Typography/` | Font family documentation, type scale specimens, licensing |
| `Icons/` | SVG icon library (v2.2.0+), interim Unicode symbol reference |
| `Layout/` | Grid system diagrams, layout pattern reference, header/footer zones |

---

## Relationship to Core/STYLE_GUIDE.md

`Core/STYLE_GUIDE.md` is the **specification**. `DesignSystem/` is the **implementation**.

```
Core/STYLE_GUIDE.md          Assets/DesignSystem/
─────────────────────        ──────────────────────────────
"Header background:          Tokens/tokens.example.yaml:
 TamiyaPrimary"          →     colors.primary.TamiyaPrimary: "#114B69"

"Header height: 18mm"    →   sizing.HeaderHeight: "18mm"

"Body text: Source         Typography/README.md:
 Sans Pro 11pt"          →     Specimen: Source Sans Pro, 11pt, line-height 1.6
```

**Synchronization rule:** When `Core/STYLE_GUIDE.md` is updated, `DesignSystem/` must be updated in the **same commit or same PR**. A `STYLE_GUIDE.md` change that is not reflected in the token file is a broken state and must not be merged.

---

## Token Reference Syntax

All PromptEngine/ prompts and component specifications reference tokens using double-brace syntax:

```
{{token.TamiyaPrimary}}        → resolves to "#114B69"
{{token.HeaderHeight}}         → resolves to "18mm"
{{token.TitleFont}}            → resolves to "Bebas Neue, Impact, Arial Black, sans-serif"
{{token.ShadowMedium}}         → resolves to "0 4px 6px rgba(0,0,0,0.16)"
```

Token resolution happens at prompt runtime: before submitting a prompt to an AI model, substitute all `{{token.*}}` references with values from `Tokens/tokens.example.yaml` (or a project-specific override file).

---

## Hardcoding Is Forbidden

The following pattern is **forbidden** in any prompt or configuration file:

```
# WRONG — hardcoded value
Header background: #114B69

# CORRECT — token reference
Header background: {{token.TamiyaPrimary}}
```

This rule ensures that if the brand color ever changes, updating one YAML file updates every page in every future manual.

---

## Custom Tokens

Projects may define custom tokens for model-specific values. Custom tokens must:

1. Use the `custom.` prefix: `custom.accentStripe`, `custom.wheelFinish`
2. Be defined in the project's own token override file (e.g., `Projects/Proto_Emperor/tokens.override.yaml`)
3. Not conflict with any SDK token name
4. Be documented in the project's `PROJECT.yaml` under a `customTokens:` key

---

## Contribution Guidelines

To add a new token to the SDK:

1. Open `Tokens/tokens.schema.yaml` and add the field definition with type and description
2. Open `Tokens/tokens.example.yaml` and add a concrete example value
3. Update `Core/STYLE_GUIDE.md` to reference the new token
4. Update any components in `Core/COMPONENT_SYSTEM.md` that use this value
5. File an ADR in `STYLE_DECISIONS.md` if the addition changes visual behavior
6. Update `CHANGELOG.md`

---

## Dependencies

- `Core/STYLE_GUIDE.md` — specification this directory implements
- `Core/COMPONENT_SYSTEM.md` — consumes tokens from this directory
- `PromptEngine/` — all prompts resolve token references at runtime
- `Templates/PDF_CONFIG.yaml` — PDF export config may reference token values
