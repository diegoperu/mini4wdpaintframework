# CHANGE_IMPACT.md

**Manuale Operativo — Mini4WD Manual SDK**
**Generato il:** 2026-07-02 · **SDK analizzato:** v2.4.0

Matrice di impatto: per ogni documento del framework, quali parti del Manuale Operativo devono essere riviste quando quel documento cambia. Complementare a `TRACEABILITY_MATRIX.md` (che risponde "chi dipende da cosa"); questo file risponde "cosa devo controllare *quando* cambio X".

---

## Parte 1 — Catene di impatto per i documenti ad alta volatilità o alta autorità

### AI_ENTRYPOINT.md
```
AI_ENTRYPOINT.md
↓
Capitolo 01 (Introduction)
↓
Capitolo 03 (AIEntryPoint)
↓
Capitolo 04 (Bootstrap)
↓
Capitolo 07 (TextEngine)
↓
Capitolo 10 (RenderEngine)
↓
Capitolo 17 (BestPractices)
↓
COVERAGE_CHECKLIST.md — voci "AI EntryPoint", "Bootstrap"
↓
CONSISTENCY_CHECK.md — controlli C8 (Source of Truth), C6 (workflow)
```
**Cosa verificare in caso di modifica:** Golden Rules (G01–G10) citate correttamente ovunque, First Response Policy, sequenza `editorial_pipeline.sequence`.

---

### SDK_CONTEXT.yaml
```
SDK_CONTEXT.yaml
↓
Capitolo 01, 02, 04, 13, 14, 16
↓
DOCUMENTATION_STATUS.yaml → documentation.sdk_version (deve combaciare)
↓
CONSISTENCY_CHECK.md — controllo C1 (versione), C8
```
**Cosa verificare:** numero di versione ovunque citato, `roadmap.next_planned` (voci spostate a implementate?), `golden_project`.

---

### Core/TEXT_ENGINE.md
```
Core/TEXT_ENGINE.md
↓
Capitolo 07 (TextEngine)
↓
Capitolo 09 (ApprovedAssets) — schema content.yaml
↓
Capitolo 11 (QA) — Tests/ContentValidation.md
↓
Checklist QA (COVERAGE_CHECKLIST.md riga "Text Engine")
↓
Capitolo 20 (Glossary) — se cambiano termini/campi
```
**Cosa verificare:** schema `content.yaml`, contratto "Render Engine legge solo content.yaml", coerenza con `Config/LANGUAGE_POLICY.yaml`.

---

### Core/DESIGN_LANGUAGE.md
```
Core/DESIGN_LANGUAGE.md
↓
Capitolo 08 (Assets)
↓
Capitolo 10 (RenderEngine)
↓
Tests/ColorValidation.md, Tests/LayoutValidation.md (rieseguire)
```
**Cosa verificare:** numero di regole citato (attualmente 65), coerenza con `Core/STYLE_GUIDE.md` e token in `tokens.example.yaml`.

---

### Core/COMPONENT_SYSTEM.md
```
Core/COMPONENT_SYSTEM.md
↓
Capitolo 08 (Assets)
↓
Capitolo 09 (ApprovedAssets) — manifest.yaml → components
↓
PromptEngine/*.md (10 file — verificare se il prompt referenzia componenti rimossi/rinominati)
```
**Cosa verificare:** C001–C015 invariati o `next_available_component_id` aggiornato; nessun ID riassegnato (G07).

---

### Core/PAGE_SYSTEM.md
```
Core/PAGE_SYSTEM.md
↓
Capitolo 07 (TextEngine) — PromptEngine/{page}.md
↓
Capitolo 08 (Assets)
↓
MANIFEST.yaml → pages (verificare sync)
```
**Cosa verificare:** P001–P010 invariati (G07); se una pagina diventa condizionale/opzionale, aggiornare `MigrationReport` e Capitolo 07.

---

### Core/QA_SYSTEM.md
```
Core/QA_SYSTEM.md
↓
Capitolo 11 (QA)
↓
Config/quality.yaml (soglie bloccanti — verificare coerenza numero item)
↓
CONSISTENCY_CHECK.md Parte 1 — rieseguire su tutti i capitoli (la QA è trasversale)
```
**Cosa verificare:** conteggio item (attualmente 110, 45 bloccanti in `MANIFEST.yaml → qa`), nuove suite in `Tests/`.

---

### Core/RENDER_GUIDE.md
```
Core/RENDER_GUIDE.md
↓
Capitolo 10 (RenderEngine)
↓
Config/render.yaml
```

---

### Core/PDF_MASTER.md
```
Core/PDF_MASTER.md
↓
Capitolo 12 (PDF)
↓
Templates/PDF_CONFIG.yaml, Config/pdf.yaml
↓
Assets/ApprovedManual/README.md (policy archiviazione)
```

---

### Config/LANGUAGE_POLICY.yaml
```
Config/LANGUAGE_POLICY.yaml
↓
Capitolo 04 (Bootstrap)
↓
Capitolo 07 (TextEngine)
↓
Capitolo 11 (QA) — Tests/TextValidation.md
↓
Capitolo 20 (Glossary) — GlossaryIT.md, Terminology.md, ForbiddenWords.md
```
**Cosa verificare:** zero tolleranza giapponese/inglese resta invariata; eventuale aggiunta di lingue supportate impatta TUTTI i capitoli editoriali.

---

### Templates/PROJECT.yaml
```
Templates/PROJECT.yaml
↓
Capitolo 06 (ProjectYaml)
↓
Capitolo 13 (GoldenProjects) — Projects/Proto_Emperor/PROJECT.yaml deve restare compatibile
↓
Core/MANUAL_SYSTEM.md § 5-6 (schema minimo documentato lì)
```
**Cosa verificare:** nuovi campi `required: true` devono comparire nel Capitolo 06 e nel Golden Project di riferimento.

---

### ROADMAP.md / STATUS.md
```
ROADMAP.md, STATUS.md
↓
Capitolo 14 (Roadmap)
↓
CONSISTENCY_CHECK.md — controllo "nessun riferimento a funzionalità future come implementate" (rieseguire su TUTTI i capitoli, non solo 14, perché una feature che passa da planned a implemented tocca il suo capitolo di destinazione finale)
```

---

### VERSION / CHANGELOG.md / ReleaseInfo.yaml
```
VERSION, CHANGELOG.md, ReleaseInfo.yaml
↓
Capitolo 15 (Versioning)
↓
DOCUMENTATION_STATUS.yaml → documentation.sdk_version, generated_from_sdk
↓
UPDATE_GUIDE.md § 5 (incremento versione manuale — da eseguire ad ogni release)
```

---

## Parte 2 — Tabella riassuntiva impatto per documenti secondari

| Documento SDK | Capitoli da rivedere | Checklist da rieseguire | Note |
|---------------|------------------------|--------------------------|------|
| `Core/STYLE_GUIDE.md` | 08 | Tests/ColorValidation.md | Verifica palette e tipografia |
| `Core/COLOR_SYSTEM.md` | 08 | Tests/ColorValidation.md | — |
| `Core/NAMING_CONVENTION.md` | 08 | Tests/NamingValidation.md | Verifica pattern `{model-slug}_{page-id}_{descriptor}_{version}` |
| `Core/WORKFLOW.md` | 05 | — | — |
| `Core/MANUAL_SYSTEM.md` | 05, 15 | UPDATE_GUIDE.md § 5 | Politica SemVer manuale/progetto |
| `Core/DEFINITION_OF_DONE.md` | 09, 11 | CONSISTENCY_CHECK.md | — |
| `Core/DOCUMENTATION_STYLE.md` | 01 | — | Impatta anche *come* si scrivono i futuri capitoli |
| `Config/render.yaml` | 10 | — | — |
| `Config/pdf.yaml` | 12 | Tests/PDFValidation.md | — |
| `Config/quality.yaml` | 11 | Core/QA_SYSTEM.md sync | — |
| `Config/sdk.yaml` | 02 | — | — |
| `Docs/LOAD_ORDER.md` | 04 | — | Deve restare sincronizzato con `SDK_CONTEXT.yaml → load_order.sequence` |
| `Docs/AI_BOOTSTRAP_PROMPT.md` | 04 | — | Prompt A–F per ChatGPT/Claude/Gemini |
| `PromptEngine/*.md` (10 file) | 07 | Tests/PromptValidation.md | Un cambiamento in un prompt impatta solo la pagina corrispondente |
| `Tests/*.md` (9 suite) | 07, 08, 11, 12 | COVERAGE_CHECKLIST.md riga "QA" | Numero totale item deve restare coerente con `MANIFEST.yaml → qa.total_items` |
| `ApprovedAssets/README.md`, `index.yaml` | 09 | — | Ciclo di vita pagina |
| `Assets/DesignSystem/Tokens/tokens.example.yaml` | 08 | Tests/ColorValidation.md, LayoutValidation.md | Ogni token rimosso rompe qualunque riferimento nei capitoli 07–12 |
| `Assets/DesignSystem/Tokens/tokens.schema.yaml` | 08 | — | — |
| `Projects/Proto_Emperor/*` | 06, 13 | — | Golden project — modifiche qui sono esempi, non specifica |
| `Knowledge/EditorialStyle.md`, `Terminology.md`, `ForbiddenWords.md` | 07, 20 | Tests/TextValidation.md | — |
| `Knowledge/GlossaryIT.md`, `Glossary.md` | 20 | — | **Glossario** — impattato anche da `Core/TEXT_ENGINE.md` (vedi esempio sotto) |
| `Knowledge/BestPractices.md` | 17 | — | — |
| `Knowledge/Troubleshooting.md` | 18 | — | — |
| `Knowledge/FAQ.md` | 19 | — | — |
| `Knowledge/Paints.md`, `Masking.md`, `Preparation.md`, `Painting.md`, `Decals.md`, `ClearCoat.md` | 07 | — | Contenuto tecnico di supporto, basso impatto strutturale |
| `README.md` (root) | 01, 16 | — | Sezione Contributing |
| `LICENSE` | 16 | — | — |
| `STYLE_DECISIONS.md` | 15 | — | ADR — nuova decisione = nuova riga in Capitolo 15 |
| `MigrationReport_v2.4.md`, `Docs/migration/v1-to-v2.md` | 15 | — | — |

### Esempio richiesto esplicitamente (TEXT_ENGINE.md)

```
Core/TEXT_ENGINE.md
↓
Capitolo 07
↓
Capitolo 11 (Checklist QA — Tests/ContentValidation.md, Tests/TextValidation.md)
↓
Glossario (Capitolo 20 — se cambia terminologia o campi di content.yaml)
```

---

## Parte 3 — Documenti a impatto trasversale (toccano quasi tutti i capitoli)

| Documento | Perché è trasversale | Azione richiesta |
|-----------|------------------------|-------------------|
| `Core/AI_OPERATING_RULES.md` (100 regole) | Ogni capitolo operativo cita almeno una regola comportamentale | Rileggere l'intero manuale se cambia una regola G-level o se il numero totale di regole cambia |
| `Config/LANGUAGE_POLICY.yaml` | Ogni capitolo con testo editoriale in italiano ne dipende | Rieseguire `CONSISTENCY_CHECK.md` su tutti i capitoli con contenuto editoriale (04, 07, 20) |
| `SDK_CONTEXT.yaml` | Identity card letta da ogni capitolo bootstrap-correlato | Rieseguire controllo C1 (versione) su tutto il manuale |
| `Core/QA_SYSTEM.md` | La QA è bloccante su ogni fase della pipeline | Rieseguire `COVERAGE_CHECKLIST.md` completa |
