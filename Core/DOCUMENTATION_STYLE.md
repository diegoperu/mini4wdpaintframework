# Documentation Style

This document specifies how to write documentation for the Mini4WD Manual SDK. Contributors who add or modify documents in `Core/`, `Docs/`, or directory READMEs must follow these rules.

This document applies to SDK documentation — not to manual content. Manual content style (what to write inside a manual page) is governed by `Core/DESIGN_LANGUAGE.md`.

---

## 1. Voice

**Use the second person** when giving instructions: "You must," "The component requires," "You should verify."

**Use the active voice** for all normative statements: "The header must span the full page width" — not "The full page width must be spanned by the header."

**Be direct.** SDK documentation is a reference, not a tutorial. Readers are looking for answers, not encouragement. Avoid filler phrases like "it is important to note that," "please be aware," or "you may want to consider."

**Be precise.** Avoid approximation in normative statements. Write "exactly 18mm" not "around 18mm" or "approximately 18mm." If a range is intended, specify the range: "between 16mm and 20mm."

**Avoid hedging** in specifications: "should" implies optional; "must" implies required; "may" implies permitted. Use each word deliberately according to RFC 2119:
- `MUST` / `must` — absolute requirement
- `MUST NOT` / `must not` — absolute prohibition
- `SHOULD` / `should` — recommended but not required
- `MAY` / `may` — optional

---

## 2. Tense

Use **present tense** for specification statements:
> "The header background is VioletPrimary."
> "Each step requires a C013 Step Number."

Use **imperative mood** for procedural instructions:
> "Copy Templates/PROJECT.yaml to your project folder."
> "Fill in all required fields before generating prompts."

Use **past tense** only when describing decisions that have already been made (e.g., in ADRs):
> "In v1, components were identified by COMP_ prefixes."

---

## 3. Headings

**Title Case** for H1 (document title only):
> `# Component System`

**Sentence case** for H2 and lower:
> `## Required render angles`
> `### Cover render`

H1 must appear exactly once per document, as the document title.

Use heading levels sequentially — do not skip from H2 to H4. Maximum heading depth is H4.

---

## 4. Lists

Use **ordered lists** (`1.`, `2.`, `3.`) for:
- Step sequences where order matters
- Ranked priorities
- Numbered rules

Use **unordered lists** (`-`) for:
- Sets of items where order does not matter
- Feature lists
- Requirements that have no inherent sequence

Do not use list items for content that should be a table. If you find yourself writing more than 3 attributes per list item, use a table instead.

---

## 5. Code Blocks

Always specify the language for syntax highlighting:

```yaml
# Correct
```yaml
sdkVersion: "2.1.0"
```

```
# Incorrect (no language specified)
```
sdkVersion: "2.1.0"
```
```

Languages used in this SDK:
- `yaml` — for YAML examples
- `bash` — for shell commands
- `markdown` — for Markdown examples (rare)
- `text` — for generic text output, file paths, or plain examples
- `css` — for CSS values (colors, spacing)

Use **inline code** (single backticks) for:
- File names: `PROJECT.yaml`
- Directory paths: `Assets/DesignSystem/Tokens/`
- Token references: `{{token.VioletPrimary}}`
- Values: `#5B2D8E`, `18mm`
- Identifiers: `P001`, `C013`, `QA-046`

---

## 6. Cross-References

Always use relative paths for cross-references within the SDK:

| Correct | Incorrect |
|---|---|
| `Core/STYLE_GUIDE.md §2` | `https://github.com/.../STYLE_GUIDE.md` |
| `[RENDER_GUIDE.md](../Core/RENDER_GUIDE.md)` | `[RENDER_GUIDE](RENDER_GUIDE)` |
| `See §3 below` | `See the section below` |

When referencing a specific section, use the section number (e.g., `§3.2`) or the section heading in backtick format (e.g., `§ Required render angles`).

When referencing a page ID: `P002` (inline code).
When referencing a component: `C001 Header` (inline code + name).
When referencing a QA item: `QA-046` (inline code).

---

## 7. Abbreviations

Define an abbreviation on its first use in each document:
> "Architecture Decision Record (ADR)"

After definition, use the abbreviation freely within the same document. Do not redefine in the same document.

Standard abbreviations that do not need definition:
- SDK, PDF, RGB, CMYK, YAML, CSS, dpi, pt (typographic point)

Abbreviations that must always be defined:
- ADR, GFM (GitHub-Flavored Markdown), DoD (Definition of Done), QA (Quality Assurance)

---

## 8. Tables

Use tables for:
- Comparisons between options (with clear column headers)
- Sets of related values (tokens, colors, dimensions)
- Correct vs. incorrect examples
- QA checklists and requirement lists

Table headers must be concise (one to three words). Do not use full sentences as column headers.

Avoid very wide tables. If a table has more than 5 columns, consider splitting it into two tables or using a definition list instead.

---

## 9. Notices

Use these prefixes for notices embedded in running text:

**Warning** (safety-critical or irreversible action):
```markdown
> ⚠️ **Warning:** [description of specific risk and consequence]
```

**Note** (supplementary information):
```markdown
> 📝 **Note:** [supplementary information]
```

Do not use `> **Important:**` or `> **Tip:**` — use the Warning or Note format. Tips and callouts are components (C008, C009) for manual content; they are not used in SDK documentation prose.

---

## 10. Examples

Every specification statement must have at least one example. Examples must be concrete — no "YourModelNameHere" or "SomeColor" placeholders. Use the Proto Emperor project as the reference example throughout the SDK documentation:

```yaml
# Good example — concrete values
modelName: "Proto Emperor"
paintScheme:
  name: "Midnight Violet"

# Poor example — placeholders obscure the format
modelName: "YourModelName"
paintScheme:
  name: "YourSchemeName"
```

When showing correct vs. incorrect, use the Do / Don't table format:

| Do | Don't |
|---|---|
| `{{token.VioletPrimary}}` | `#5B2D8E` (hardcoded) |
| `C001 Header` | `the purple bar at the top` |

---

## 11. File Structure

Every documentation file in `Core/` and all directory READMEs must include:

1. **Title** (H1) — the document name
2. **Introduction** — one paragraph explaining what this document is and what it covers
3. **"See also" line** — cross-references to related documents (where applicable)
4. **Body** — the content, organized by numbered sections (H2)

Files in `Docs/guides/` may use a more informal structure, but must still start with a clear title and purpose statement.

---

## 12. What Not to Write

**Do not document the obvious.** If a reader can determine the answer by reading the code or the file structure, do not repeat it in prose.

**Do not apologize.** "Unfortunately, X is not yet supported" → "X is not supported in this version."

**Do not forecast.** "In the future, we plan to…" belongs in `ROADMAP.md`, not in specification documents. Specification documents describe the current version.

**Do not attribute.** "This decision was made because of user feedback from the 2023 community survey" — attribution belongs in an ADR if it is important, not in the specification text.

**Do not pad.** Every sentence in a specification document must earn its place. If removing a sentence does not reduce the reader's understanding, remove it.
