# Assets/DesignSystem/Tokens/

**Version:** 2.1.0
**Authoritative spec:** Core/STYLE_GUIDE.md
**Schema:** tokens.schema.yaml
**Example:** tokens.example.yaml

---

## Purpose

Design Tokens are the **atomic visual values** of the Mini4WD Manual SDK. Every color, font, spacing value, shadow, and size used anywhere in the system is defined here as a named token. Components reference tokens; tokens reference nothing — they are the leaf nodes of the design system.

This directory contains two files:

| File | Purpose |
|------|---------|
| `tokens.example.yaml` | Complete, filled token file — the SDK default |
| `tokens.schema.yaml` | JSON Schema (in YAML) for validating any token file |

---

## Why Tokens?

Without tokens, a color change from `#5B2D8E` to a slightly different violet would require searching and replacing every prompt file, every component spec, and every export config. With tokens, you change one line in `tokens.example.yaml` and every reference is resolved correctly at generation time.

---

## Token Categories

| Category | Key Prefix | Description |
|----------|------------|-------------|
| Colors — Primary | `colors.primary.*` | Brand violet palette |
| Colors — Neutral | `colors.neutral.*` | Grays, white, black |
| Colors — Accent | `colors.accent.*` | Gold, highlight colors |
| Colors — Semantic | `colors.semantic.*` | Warning red, success green, info blue |
| Colors — Panel | `colors.panel.*` | Violet side panel colors |
| Colors — Callout | `colors.callout.*` | Callout box colors and arrow colors |
| Typography — Fonts | `typography.fonts.*` | Font family stacks |
| Typography — Scale | `typography.scale.*` | Size and line-height per level |
| Spacing | `spacing.*` | Base unit, scale steps, page margins |
| Sizing | `sizing.*` | Header/footer heights, grid columns, page dimensions |
| Borders | `borders.*` | Border radius, thickness |
| Shadows | `shadows.*` | Shadow definitions at three levels |
| Render | `render.*` | Lighting rig, background, resolution requirements |

---

## Reference Syntax

In prompt files and component specs, reference tokens with:

```
{{token.TokenName}}
```

Examples:

```
{{token.VioletPrimary}}         → "#5B2D8E"
{{token.HeaderHeight}}          → "18mm"
{{token.BodyFont}}              → "Source Sans Pro, Open Sans, Helvetica Neue, sans-serif"
{{token.ShadowSubtle}}          → "0 1px 3px rgba(0,0,0,0.12)"
{{token.CoverResolution}}       → "2480x3508px"
```

Token resolution is performed **before** submitting any prompt to an AI model. See `Core/WORKFLOW.md §Phase 2` for the substitution procedure.

---

## Custom Project Tokens

Projects may define additional tokens for model-specific values. Place them in a `tokens.override.yaml` file within the project directory:

```
Projects/Proto_Emperor/tokens.override.yaml
```

Custom token structure:

```yaml
tokens:
  custom:
    accentStripe: "#C0C0C0"      # Silver racing stripe color
    wheelFinish: "metallic-gold"  # Wheel finish description
    cockpitTint: "#1A237E"        # Interior cockpit tint
```

Custom tokens must use the `custom.` prefix. Reference them as `{{token.custom.accentStripe}}`.

---

## Validation

To validate a token file against the schema:

```bash
# Using ajv-cli (Node.js)
npx ajv validate -s tokens.schema.yaml -d tokens.example.yaml

# Using yajsv
yajsv -s tokens.schema.yaml tokens.example.yaml

# Using Python jsonschema
python -c "
import yaml, jsonschema
schema = yaml.safe_load(open('tokens.schema.yaml'))
data = yaml.safe_load(open('tokens.example.yaml'))
jsonschema.validate(data, schema)
print('Valid')
"
```

Required fields are enforced by the schema. Optional fields produce warnings, not errors.

---

## Extending the Token Set

To add a new SDK-level token:

1. Add the field to `tokens.schema.yaml` with `type`, `description`, and whether it is `required`
2. Add an example value to `tokens.example.yaml` with an inline comment explaining usage
3. Update `Core/STYLE_GUIDE.md` to document the new value
4. Update any component in `Core/COMPONENT_SYSTEM.md` that should use the new token
5. Add entry to `CHANGELOG.md` under the appropriate version

Do not add new tokens without updating the schema. Undocumented tokens are not portable between SDK versions.

---

## Token Immutability Policy

Token **names** are stable across minor versions. Token **values** may change in minor versions if the change is additive or a bug fix. Token name changes are breaking changes and require a major version bump.

| Change Type | Version Impact |
|------------|----------------|
| Add new token | Minor (2.x.0) |
| Change token value | Minor (2.x.0) |
| Rename token | Major (3.0.0) |
| Remove token | Major (3.0.0) |

---

## Files in This Directory

- [`tokens.example.yaml`](tokens.example.yaml) — Complete example with all SDK tokens and inline documentation
- [`tokens.schema.yaml`](tokens.schema.yaml) — JSON Schema (YAML format) for validation
