# Knowledge/

**Role in framework:** Technical reference library for Mini4WD painting techniques, materials, and processes.

**SDK Version:** 2.2.0

Knowledge/ is the SDK's technical knowledge base. It contains objective, factual information about painting, masking, preparation, and finishing techniques for Mini4WD scale models. This information is used by:

- Manual authors to make accurate content decisions
- AI models as reference material (via prompt injection or RAG)
- QA reviewers to verify technical accuracy of generated content

## Critical Distinction

| Knowledge/ | PromptEngine/ |
|-----------|---------------|
| Factual reference — what is true | Prompt templates — what to generate |
| Timeless technical content | SDK-version-specific instructions |
| Authored by domain experts | Designed by SDK architects |
| No project-specific data | Driven by PROJECT.yaml |

**Never put prompts in Knowledge/. Never put factual reference in PromptEngine/.**

## Contents

| File | Topic | Description |
|------|-------|-------------|
| `Paints.md` | Paint products | Brands, product lines, code formats, finish types |
| `Masking.md` | Masking techniques | Tape types, liquid masking, pre-cut masks, application |
| `Preparation.md` | Surface preparation | Cleaning, priming, sanding, degreasing |
| `Painting.md` | Painting techniques | Brush, airbrush, spray can, layering |
| `Decals.md` | Decal application | Water-slide, dry transfer, clear coat interaction |
| `ClearCoat.md` | Clear coat & finishing | Gloss, matte, satin top coats, UV protection |
| `Troubleshooting.md` | Problem solving | Common defects, causes, remedies |
| `Glossary.md` | Terminology | Definitions for all technical terms |
| `FAQ.md` | Common questions | Frequently asked questions with answers |
| `BestPractices.md` | Expert guidance | Compiled best practices from experienced painters |

## Using Knowledge/ with AI Models

When executing prompts from PromptEngine/, you may optionally prepend relevant sections from Knowledge/ to provide the AI model with technical context. Example:

```
[KNOWLEDGE CONTEXT]
{paste relevant section from Knowledge/Masking.md}

[PROMPT]
{paste resolved PromptEngine/Masking.md prompt}
```

This technique (Retrieval-Augmented Generation) improves accuracy of AI-generated technical content.

## Maintenance

- Knowledge/ documents are updated independently of the SDK version
- Technical inaccuracies should be filed as issues with label `knowledge-error`
- Do not add product-specific information (e.g., "Proto Emperor uses TS-57") — that belongs in Projects/
- Brand-specific product information should be verified against manufacturer documentation

## Dependencies
- Referenced by: `PromptEngine/` (optional context injection)
- Referenced by: `Core/AI_OPERATING_RULES.md` (RULE-001 to RULE-010)
- Referenced by: `Tests/ColorValidation.md TEST-CL-004`

## Related Documents
- `Core/AI_OPERATING_RULES.md`
- `PromptEngine/README.md`
- `Core/QA_SYSTEM.md`
