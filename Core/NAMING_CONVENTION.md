# Naming Convention

This document defines the naming rules for all files, folders, and identifiers in the Mini4WD Manual SDK. Consistent naming is essential for automated tooling, cross-platform compatibility, and long-term maintainability.

Violations are tracked in `Core/QA_SYSTEM.md` §9 (QA-091 to QA-095).

---

## 1. General Principles

- Names communicate purpose — a reader should understand what a file contains without opening it
- Names are stable — once a file is committed, its name should not change unless there is a structural reason
- Names are ASCII-safe — no accented characters, no spaces, no special symbols
- Names are cross-platform — valid on Linux (case-sensitive), macOS (case-insensitive), and Windows (case-insensitive)
- When in doubt, use kebab-case for human-readable identifiers and PascalCase for schema identifiers

---

## 2. File Naming by Category

### 2.1 Documentation Files (Markdown)
**Format:** `SCREAMING_SNAKE_CASE.md` for top-level specification documents; `kebab-case.md` for guide and article files.

| Context | Format | Examples |
|---|---|---|
| Core specification documents | `SCREAMING_SNAKE_CASE.md` | `DESIGN_LANGUAGE.md`, `QA_SYSTEM.md` |
| Project READMEs | `README.md` (exact case) | `README.md` |
| Top-level guides in Docs/ | `SCREAMING_SNAKE_CASE.md` | `LOAD_ORDER.md`, `AI_BOOTSTRAP_PROMPT.md` |
| Migration guides in Docs/migration/ | `kebab-case.md` | `v1-to-v2.md` |
| Changelog and meta-docs | `SCREAMING_SNAKE_CASE.md` | `CHANGELOG.md`, `ROADMAP.md` |

### 2.2 Configuration Files (YAML)
**Format:** `SCREAMING_SNAKE_CASE.yaml` for templates and schemas; `kebab-case.yaml` for project-specific instances.

| Context | Format | Examples |
|---|---|---|
| Templates | `SCREAMING_SNAKE_CASE.yaml` | `PROJECT.yaml`, `PDF_CONFIG.yaml` |
| Schema files | `kebab-case.schema.yaml` | `tokens.schema.yaml` |
| Example files | `kebab-case.example.yaml` | `tokens.example.yaml` |
| Project instances | `kebab-case.yaml` | `color_scheme.yaml` |

### 2.3 Image Files (renders, references)
**Format:** `{model-slug}_{pageId}_{descriptor}_{version}.{ext}`

All components:
- `{model-slug}`: model name in kebab-case (see §3.1)
- `{pageId}`: permanent page ID (P001, P002, …)
- `{descriptor}`: short description of the image content in kebab-case
- `{version}`: `v` followed by integer, starting at v1
- `{ext}`: `png` for renders (preferred), `jpg` for reference photos

| Correct | Incorrect |
|---|---|
| `proto-emperor_P001_cover_v1.png` | `Proto_Emperor_Cover.png` |
| `proto-emperor_P002_colorscheme-front_v1.png` | `colorFront.png` |
| `proto-emperor_P007_detail-wheel-arch_v2.png` | `detail2.png` |
| `proto-emperor_reference_front_v1.jpg` | `reference.jpg` |

### 2.4 PDF Files
**Format:** `{model-slug}_manual_{variant}_{version}.pdf`

| Correct | Incorrect |
|---|---|
| `proto-emperor_manual_screen_v1.pdf` | `ProtoEmperor.pdf` |
| `proto-emperor_manual_print_v1.pdf` | `manual_print.pdf` |

### 2.5 PromptEngine Files
**Format:** `PascalCase.md`

| Correct | Incorrect |
|---|---|
| `Cover.md` | `cover.md`, `COVER.md`, `p001-cover.md` |
| `ColorScheme.md` | `color_scheme.md`, `color-scheme.md` |
| `FinalChecklist.md` | `final_checklist.md` |

---

## 3. Folder Naming by Category

### 3.1 Project Folders (in Projects/)
**Format:** `PascalCase` matching the official Tamiya model name, spaces replaced with underscores.

The model slug (used in file names) is derived from the folder name: lowercase all characters, replace underscores with hyphens.

| Official Name | Folder Name | Model Slug |
|---|---|---|
| Proto Emperor | `Proto_Emperor` | `proto-emperor` |
| Avante Mk III | `Avante_Mk_III` | `avante-mk-iii` |
| Dash-1 Emperor | `Dash-1_Emperor` | `dash-1-emperor` |
| Hurricane Sonic | `Hurricane_Sonic` | `hurricane-sonic` |

> ⚠️ **Warning:** The folder name and the model slug are different. The folder name is `Proto_Emperor` (underscores, PascalCase). The model slug is `proto-emperor` (hyphens, lowercase). Use each in its correct context.

### 3.2 SDK Directory Structure Folders
**Format:** `PascalCase` for semantic SDK directories.

| Correct | Incorrect |
|---|---|
| `Core/` | `core/`, `CORE/` |
| `PromptEngine/` | `prompts/`, `prompt_engine/` |
| `Templates/` | `templates/` |
| `Assets/` | `assets/` |
| `DesignSystem/` | `design_system/`, `designSystem/` |

### 3.3 Asset Subdirectories
**Format:** `PascalCase` for SDK-defined subdirectories; `lowercase` for project-generated asset subfolders (e.g., `raw/`, `approved/`).

| Correct | Incorrect |
|---|---|
| `Assets/DesignSystem/Tokens/` | `Assets/design_system/tokens/` |
| `Projects/{Model}/Output/raw/` | `Projects/{Model}/Output/Raw/` |
| `Projects/{Model}/Notes/` | `Projects/{Model}/notes/` |

---

## 4. Identifier Naming

### 4.1 Page IDs
**Format:** `P` followed by three-digit zero-padded integer.

```
P001, P002, P003, ... P010, P011
```

### 4.2 Component IDs
**Format:** `C` followed by three-digit zero-padded integer.

```
C001, C002, C003, ... C015, C016
```

### 4.3 Design Token Keys
**Format:** `PascalCase` noun or noun+adjective.

| Correct | Incorrect |
|---|---|
| `VioletPrimary` | `violet_primary`, `violetPrimary`, `VIOLET_PRIMARY` |
| `HeaderHeight` | `header-height`, `header_h` |
| `FontScaleBody` | `bodyFontSize`, `body_font` |

### 4.4 QA Item IDs
**Format:** `QA-` followed by three-digit zero-padded integer.

```
QA-001, QA-002, ... QA-110
```

### 4.5 ADR IDs (in STYLE_DECISIONS.md)
**Format:** `ADR-` followed by three-digit zero-padded integer.

```
ADR-001, ADR-002, ... ADR-010
```

---

## 5. Version Suffix Convention

Version suffixes in file names follow these rules:
- Format: `v` followed by a non-zero integer (`v1`, `v2`, not `v01` or `v1.0`)
- Increment the version when the file content changes and the old version must be preserved
- Do not use `_final`, `_FINAL`, `_v2_FINAL`, `_revised`, or similar informal markers

| Correct | Incorrect |
|---|---|
| `proto-emperor_P001_cover_v1.png` | `proto-emperor_P001_cover_v1_FINAL.png` |
| `proto-emperor_P001_cover_v2.png` | `proto-emperor_P001_cover_updated.png` |
| `proto-emperor_manual_screen_v1.pdf` | `proto-emperor_manual_screen_final.pdf` |

---

## 6. Forbidden Characters

The following characters must never appear in any file or folder name in this SDK:

| Character | Reason |
|---|---|
| Space (` `) | Requires quoting in shell; breaks many tools |
| `&` | Shell operator; URL encoding issues |
| `#` | URL fragment; markdown header indicator |
| `%` | URL encoding character |
| `@` | Email/mention character in many tools |
| `!` | Shell history expansion |
| `$` | Shell variable expansion |
| `(` `)` | Shell subshell characters |
| `[` `]` | Shell glob characters |
| `{` `}` | Shell brace expansion |
| `'` `"` | Shell quoting characters |
| `\` | Path separator on Windows; escape character |
| `:` | NTFS incompatible; URL separator |
| `*` `?` | Shell glob wildcards |
| `<` `>` | Shell redirection operators |
| `|` | Shell pipe operator |

Accented characters (é, ü, ñ, etc.) are forbidden in file and folder names. They may appear in file content but not in names. The only permitted non-ASCII sequence is a hyphen-connected identifier (see model slugs in §3.1).

---

## 7. Examples Summary Table

| Item | Correct Name | Incorrect Name |
|---|---|---|
| Core specification | `COMPONENT_SYSTEM.md` | `ComponentSystem.md` |
| Project folder | `Proto_Emperor` | `proto emperor`, `protoEmperor` |
| Model slug | `proto-emperor` | `Proto_Emperor`, `ProtoEmperor` |
| Cover render | `proto-emperor_P001_cover_v1.png` | `Cover.png`, `cover_final.png` |
| Color scheme render (front) | `proto-emperor_P002_colorscheme-front_v1.png` | `front.png` |
| Screen PDF | `proto-emperor_manual_screen_v1.pdf` | `manual.pdf` |
| PromptEngine file | `ColorScheme.md` | `color-scheme.md` |
| Token key | `VioletPrimary` | `violet-primary` |
| QA item | `QA-046` | `QA46`, `qa-046` |
