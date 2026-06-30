# Docs/

**Version:** 2.1.0
**Relationship to Core/:** Supplementary — does NOT override Core/

---

## Purpose

`Docs/` contains supplementary documentation for the Mini4WD Manual SDK. Where `Core/` provides authoritative technical specifications, `Docs/` provides guides, tutorials, migration instructions, and explanatory content written in a more conversational style.

If `Core/` and `Docs/` ever conflict, **`Core/` wins**. `Docs/` is always a derivative of `Core/`, not the other way around. When `Core/` specifications change, the relevant `Docs/` content must be updated in the same release.

---

## Docs/ vs Core/

| Content Type | Belongs In | Example |
|-------------|------------|---------|
| Authoritative page specification | Core/PAGE_SYSTEM.md | "P002 requires components C001, C002, C003, C010, C011" |
| How to read a page specification | Docs/ | "Getting started: your first color scheme page" |
| Component dimensions | Core/COMPONENT_SYSTEM.md | "C001 Header height: 18mm" |
| Workflow walkthrough | Docs/ | Step-by-step tutorial for first-time users |
| SDK version history | CHANGELOG.md (root) | "v2.1.0 added Design Tokens" |
| Migration instructions | Docs/migration/ | "Upgrading from v1 to v2" |
| Design philosophy | Core/DESIGN_LANGUAGE.md | "Rule 12: The violet panel is the SDK's signature" |
| Why the philosophy matters | Docs/ | "Understanding the design language" |

---

## Current Contents

| File | Description | Last Updated |
|------|-------------|-------------|
| `migration/v1-to-v2.md` | Complete migration guide from SDK v1.x to v2.x | v2.0.0 |

---

## Planned Contents (v2.2.0+)

The following documents are planned for future releases:

| File | Description | Target Version |
|------|-------------|----------------|
| `tutorial/first-manual.md` | End-to-end tutorial: create your first Mini4WD manual | v2.2.0 |
| `tutorial/render-generation.md` | How to generate renders using free and paid AI tools | v2.2.0 |
| `tutorial/pdf-export.md` | Step-by-step PDF export in Affinity Publisher, InDesign, Scribus | v2.2.0 |
| `faq.md` | Frequently asked questions | v2.2.0 |
| `contributing.md` | How to contribute to the SDK | v2.2.0 |
| `glossary.md` | Definitions of SDK-specific terms | v2.2.0 |
| `migration/v2-to-v3.md` | Migration guide for v3.0.0 (when released) | v3.0.0 |

---

## Writing Style for Docs/

Content in `Docs/` follows `Core/DOCUMENTATION_STYLE.md` but with a more tutorial-oriented register:

- Use second person ("You can...", "First, open...")
- Prefer numbered steps for sequential procedures
- Include screenshots or terminal output examples where possible
- Cross-reference `Core/` documents when citing specifications
- Do not restate specifications — link to them instead

**Example (correct):**
> Open `Templates/PROJECT.yaml` and fill in the `modelName` field. For the field format, see `Core/NAMING_CONVENTION.md §Project naming`.

**Example (incorrect — restates the spec):**
> Fill in the `modelName` field. Model names must match the official Tamiya model name with spaces replaced by underscores.

---

## Adding New Documents

To add a new document to `Docs/`:

1. Create the file in the appropriate subdirectory (create the subdirectory if needed)
2. Add the file to the **Current Contents** table above
3. If the document covers a new topic, consider whether a corresponding `Core/` spec is also needed
4. Add an entry to `CHANGELOG.md`
5. Add a line to `ROADMAP.md` marking the feature as shipped (if it was previously planned)
