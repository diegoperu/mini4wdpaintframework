# TRACEABILITY_MATRIX.md

**Manuale Operativo — Mini4WD Manual SDK**
**Generato il:** 2026-07-02 · **SDK analizzato:** v2.4.0

Matrice di tracciabilità: per ogni documento del framework, dove viene citato (da altri documenti SDK, tramite `depends_on` in `RepositoryManifest.yaml` o riferimento testuale diretto), quali capitoli del Manuale Operativo dipendono da esso, e il livello di dipendenza.

**Livelli di dipendenza:**
- **Critico** — se il documento cambia senza aggiornare il manuale, il manuale diventa scorretto/fuorviante per un AI o un contributor (bootstrap, Golden Rules, contratti bloccanti)
- **Alto** — usato come Source of Truth di uno o più capitoli
- **Medio** — citato/consultato ma non SoT; il capitolo resta valido anche con modifiche minori
- **Basso** — riferimento di esempio, opzionale, o cartella `Proto_Emperor` (golden project, non specifica)

---

## Parte 1 — Catene di tracciabilità per i documenti principali

### AI_ENTRYPOINT.md
```
AI_ENTRYPOINT.md
↓
01_Introduction   (citato come entrypoint ufficiale)
↓
03_AIEntryPoint   (Source of Truth diretta)
↓
04_Bootstrap      (Bootstrap Contract, required_read_order)
↓
07_TextEngine     (Text Mode: input/output/vincoli)
↓
10_RenderEngine   (Render Mode: input/output/vincoli)
↓
17_BestPractices  (Golden Rules G01–G10 riusate come pratiche raccomandate)
```
**Citato da:** `BOOTSTRAP.md`, `SDK_CONTEXT.yaml` (bootstrap.official_entrypoint), `RepositoryManifest.yaml`, `Docs/LOAD_ORDER.md`
**Capitoli dipendenti:** 01, 03, 04, 07, 10, 17
**Livello:** Critico

---

### SDK_CONTEXT.yaml
```
SDK_CONTEXT.yaml
↓
01_Introduction
↓
02_SDKContext     (Source of Truth diretta)
↓
04_Bootstrap      (load_order.sequence)
↓
13_GoldenProjects (sezione golden_project)
↓
14_Roadmap        (sezione roadmap)
↓
16_GitHubWorkflow (sezione repository)
```
**Citato da:** `AI_ENTRYPOINT.md`, `BOOTSTRAP.md`, `RepositoryManifest.yaml`, `Docs/LOAD_ORDER.md`, `STATUS.md`
**Capitoli dipendenti:** 01, 02, 04, 13, 14, 16
**Livello:** Critico

---

### BOOTSTRAP.md
```
BOOTSTRAP.md
↓
04_Bootstrap  (Source of Truth diretta)
```
**Citato da:** `AI_ENTRYPOINT.md → Cross References`, `SDK_CONTEXT.yaml → bootstrap.entry_point`, `RepositoryManifest.yaml` (`depends_on: ["AI_ENTRYPOINT.md", "SDK_CONTEXT.yaml"]`)
**Capitoli dipendenti:** 04
**Livello:** Critico

---

### Core/AI_OPERATING_RULES.md
```
Core/AI_OPERATING_RULES.md
↓
04_Bootstrap      (100 regole comportamentali, ai_load_order: 3)
↓
07_TextEngine     (Regole 059–100: rendering testo)
↓
17_BestPractices  (regole correlate)
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml → load_order`, `Core/DESIGN_LANGUAGE.md` (depends_on)
**Capitoli dipendenti:** 04, 07, 17
**Livello:** Critico

---

### Config/LANGUAGE_POLICY.yaml
```
Config/LANGUAGE_POLICY.yaml
↓
04_Bootstrap
↓
07_TextEngine  (Source of Truth per la politica linguistica)
↓
11_QA          (Tests/TextValidation.md dipende da questo file)
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml`, `Core/TEXT_ENGINE.md`, `Tests/TextValidation.md`
**Capitoli dipendenti:** 04, 07, 11
**Livello:** Critico

---

### Core/TEXT_ENGINE.md
```
Core/TEXT_ENGINE.md
↓
07_TextEngine   (Source of Truth diretta)
↓
09_ApprovedAssets (schema content.yaml)
↓
10_RenderEngine   (contratto: Render legge solo content.yaml)
↓
11_QA             (Tests/ContentValidation.md dipende da questo)
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml → pipeline.text_engine.spec`, `Core/COMPONENT_SYSTEM.md` (depends_on), `Tests/ContentValidation.md` (depends_on)
**Capitoli dipendenti:** 07, 09, 10, 11
**Livello:** Critico

---

### Core/DESIGN_LANGUAGE.md
```
Core/DESIGN_LANGUAGE.md
↓
08_Assets      (Source of Truth diretta — 65 regole)
↓
10_RenderEngine (Rules 55–65: identità editoriale)
```
**Citato da:** `AI_ENTRYPOINT.md`, `Core/STYLE_GUIDE.md`, `Core/COMPONENT_SYSTEM.md`, `Core/RENDER_GUIDE.md` (tutti in `depends_on`)
**Capitoli dipendenti:** 08, 10
**Livello:** Critico

---

### Core/STYLE_GUIDE.md
```
Core/STYLE_GUIDE.md
↓
08_Assets
```
**Citato da:** `AI_ENTRYPOINT.md`, `Core/COLOR_SYSTEM.md`, `Core/COMPONENT_SYSTEM.md`, `Core/RENDER_GUIDE.md`, `Tests/ColorValidation.md` (tutti `depends_on`)
**Capitoli dipendenti:** 08
**Livello:** Alto

---

### Core/COMPONENT_SYSTEM.md
```
Core/COMPONENT_SYSTEM.md
↓
08_Assets      (Source of Truth diretta — C001–C015)
↓
09_ApprovedAssets (manifest.yaml → components)
```
**Citato da:** `AI_ENTRYPOINT.md`, `Core/PAGE_SYSTEM.md` (depends_on), `PromptEngine/*.md`, `Tests/LayoutValidation.md`
**Capitoli dipendenti:** 08, 09
**Livello:** Critico (Component ID sono permanenti — G07)

---

### Core/PAGE_SYSTEM.md
```
Core/PAGE_SYSTEM.md
↓
08_Assets       (Source of Truth diretta — P001–P010)
↓
07_TextEngine   (PromptEngine/*.md dipende da questo)
```
**Citato da:** `AI_ENTRYPOINT.md`, `MANIFEST.yaml → pages`, tutti i file `PromptEngine/*.md` (`depends_on`), `Tests/LayoutValidation.md`
**Capitoli dipendenti:** 07, 08
**Livello:** Critico (Page ID sono permanenti — G07)

---

### Core/RENDER_GUIDE.md
```
Core/RENDER_GUIDE.md
↓
10_RenderEngine  (Source of Truth diretta)
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml → pipeline.render_engine.spec`
**Capitoli dipendenti:** 10
**Livello:** Alto

---

### Core/QA_SYSTEM.md
```
Core/QA_SYSTEM.md
↓
11_QA  (Source of Truth diretta — 110 item, 45 bloccanti)
```
**Citato da:** `AI_ENTRYPOINT.md`, `MANIFEST.yaml → qa.checklist_file`, `Core/MANUAL_SYSTEM.md`
**Capitoli dipendenti:** 11
**Livello:** Critico

---

### Core/PDF_MASTER.md
```
Core/PDF_MASTER.md
↓
12_PDF  (Source of Truth diretta)
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml → pipeline.pdf_builder.spec`, `Templates/PDF_CONFIG.yaml` (relazione inversa: PDF_MASTER dipende da questo template)
**Capitoli dipendenti:** 12
**Livello:** Alto

---

### Core/WORKFLOW.md
```
Core/WORKFLOW.md
↓
05_Workflow  (Source of Truth diretta)
```
**Citato da:** `RepositoryManifest.yaml` (depends_on: PAGE_SYSTEM.md, COMPONENT_SYSTEM.md), `Build/Pipeline.md`
**Capitoli dipendenti:** 05
**Livello:** Alto

---

### Core/MANUAL_SYSTEM.md
```
Core/MANUAL_SYSTEM.md
↓
05_Workflow    (architettura e ciclo di vita)
↓
15_Versioning  (§7 Version Management)
```
**Citato da:** nessun documento SDK lo referenzia esplicitamente in `depends_on` (documento "foglia")
**Capitoli dipendenti:** 05, 15
**Livello:** Alto

---

### Core/DEFINITION_OF_DONE.md
```
Core/DEFINITION_OF_DONE.md
↓
09_ApprovedAssets
↓
11_QA
```
**Citato da:** `MANIFEST.yaml → qa.definition_of_done`
**Capitoli dipendenti:** 09, 11
**Livello:** Alto

---

### Core/NAMING_CONVENTION.md
```
Core/NAMING_CONVENTION.md
↓
08_Assets
```
**Citato da:** `Core/MANUAL_SYSTEM.md § 3`, `Tests/NamingValidation.md` (depends_on)
**Capitoli dipendenti:** 08
**Livello:** Medio

---

### Core/COLOR_SYSTEM.md
```
Core/COLOR_SYSTEM.md
↓
08_Assets
```
**Citato da:** `Core/STYLE_GUIDE.md` (relazione inversa: COLOR_SYSTEM depends_on STYLE_GUIDE)
**Capitoli dipendenti:** 08
**Livello:** Medio

---

### Core/DOCUMENTATION_STYLE.md
```
Core/DOCUMENTATION_STYLE.md
↓
01_Introduction
```
**Citato da:** nessuno esplicitamente — governa *come* si scrive la documentazione, incluso questo stesso set di file di validazione
**Capitoli dipendenti:** 01
**Livello:** Medio (rilevante anche per il manutentore del Manuale Operativo stesso — vedi `UPDATE_GUIDE.md`)

---

### Config/quality.yaml
```
Config/quality.yaml
↓
11_QA
```
**Citato da:** `MANIFEST.yaml` (indirettamente tramite qa), nessun `depends_on` esplicito in RepositoryManifest
**Capitoli dipendenti:** 11
**Livello:** Alto

---

### Config/render.yaml
```
Config/render.yaml
↓
10_RenderEngine
```
**Citato da:** nessuno esplicitamente
**Capitoli dipendenti:** 10
**Livello:** Medio

---

### Config/pdf.yaml
```
Config/pdf.yaml
↓
12_PDF
```
**Citato da:** nessuno esplicitamente
**Capitoli dipendenti:** 12
**Livello:** Medio

---

### Config/sdk.yaml
```
Config/sdk.yaml
↓
02_SDKContext
```
**Citato da:** nessuno esplicitamente
**Capitoli dipendenti:** 02
**Livello:** Basso

---

### Docs/LOAD_ORDER.md
```
Docs/LOAD_ORDER.md
↓
04_Bootstrap
```
**Citato da:** `AI_ENTRYPOINT.md → Cross References`, `SDK_CONTEXT.yaml → load_order.description`, `RepositoryManifest.yaml` (depends_on: BOOTSTRAP.md, SDK_CONTEXT.yaml)
**Capitoli dipendenti:** 04
**Livello:** Alto

---

### Docs/AI_BOOTSTRAP_PROMPT.md
```
Docs/AI_BOOTSTRAP_PROMPT.md
↓
04_Bootstrap
```
**Citato da:** `AI_ENTRYPOINT.md`, `SDK_CONTEXT.yaml → bootstrap.ai_prompt`
**Capitoli dipendenti:** 04
**Livello:** Medio

---

### Templates/PROJECT.yaml
```
Templates/PROJECT.yaml
↓
06_ProjectYaml  (Source of Truth diretta)
```
**Citato da:** `AI_ENTRYPOINT.md → Project Bootstrap`, `Core/MANUAL_SYSTEM.md § 5-6`, `Projects/PROJECT_BOOTSTRAP.md`
**Capitoli dipendenti:** 06
**Livello:** Critico (mai modificare via AI — regola comportamentale `never_modify_project_yaml`)

---

### ApprovedAssets/index.yaml
```
ApprovedAssets/index.yaml
↓
09_ApprovedAssets  (Source of Truth diretta per lo stato globale)
```
**Citato da:** `AI_ENTRYPOINT.md → Phase 7 Release`, `RepositoryManifest.yaml`
**Capitoli dipendenti:** 09
**Livello:** Alto

---

### Knowledge/EditorialStyle.md / Terminology.md / ForbiddenWords.md / GlossaryIT.md
```
Knowledge/EditorialStyle.md, Terminology.md, ForbiddenWords.md, GlossaryIT.md
↓
07_TextEngine
↓
20_Glossary
```
**Citato da:** `STATUS.md → v2.3.0 Text Engine and Editorial`
**Capitoli dipendenti:** 07, 20
**Livello:** Alto (zero tolleranza linguistica — G01)

---

### Knowledge/BestPractices.md
```
Knowledge/BestPractices.md
↓
17_BestPractices  (Source of Truth diretta)
```
**Capitoli dipendenti:** 17
**Livello:** Medio

---

### Knowledge/Troubleshooting.md
```
Knowledge/Troubleshooting.md
↓
18_Troubleshooting  (Source of Truth diretta)
```
**Capitoli dipendenti:** 18
**Livello:** Medio

---

### Knowledge/FAQ.md
```
Knowledge/FAQ.md
↓
19_FAQ  (Source of Truth diretta)
```
**Capitoli dipendenti:** 19
**Livello:** Basso

---

### ROADMAP.md / STATUS.md
```
ROADMAP.md, STATUS.md
↓
14_Roadmap  (Source of Truth diretta)
```
**Citato da:** `SDK_CONTEXT.yaml → roadmap.see`, `MANIFEST.yaml → roadmap`
**Capitoli dipendenti:** 14
**Livello:** Medio (cambia a ogni release — verifica obbligatoria, vedi `UPDATE_GUIDE.md`)

---

### CHANGELOG.md / VERSION / ReleaseInfo.yaml / STYLE_DECISIONS.md
```
CHANGELOG.md, VERSION, ReleaseInfo.yaml, STYLE_DECISIONS.md
↓
15_Versioning  (Source of Truth diretta)
```
**Capitoli dipendenti:** 15
**Livello:** Critico (ogni release SDK richiede aggiornamento — vedi `UPDATE_GUIDE.md` e `CHANGE_IMPACT.md`)

---

### Projects/Proto_Emperor/ (README.md, PROJECT.yaml)
```
Projects/Proto_Emperor/*
↓
13_GoldenProjects  (Source of Truth diretta — riferimento strutturale)
↓
06_ProjectYaml     (esempio di PROJECT.yaml compilato)
```
**Citato da:** `SDK_CONTEXT.yaml → golden_project`
**Capitoli dipendenti:** 06, 13
**Livello:** Basso (esempio, non specifica normativa — modificarlo non altera il comportamento dello SDK)

---

## Parte 2 — Tabella riassuntiva documenti secondari

Documenti con una singola dipendenza di capitolo diretta e nessuna catena multi-hop rilevante (template, prompt per-pagina, README di sottocartella, singole suite di test).

| Documento | Citato in | Capitoli dipendenti | Livello |
|-----------|-----------|----------------------|---------|
| `README.md` (root) | `RepositoryManifest.yaml` | 01, 16 | Alto |
| `MANIFEST.yaml` | `RepositoryManifest.yaml` | 01 | Medio |
| `RepositoryManifest.yaml` | — (documento radice della mappa) | 01 | Alto |
| `LICENSE` | `RepositoryManifest.yaml` | 16 | Basso |
| `MigrationReport_v2.4.md` | `STATUS.md → CMS Layer` | 15 | Medio |
| `Docs/migration/v1-to-v2.md` | `MANIFEST.yaml → compatibility` | 15 | Medio |
| `Docs/README.md` | — | 04 | Basso |
| `Build/Pipeline.md` | `Core/WORKFLOW.md` (relazione), `SDK_CONTEXT.yaml` | 05 | Alto |
| `Build/README.md` | — | 05 | Basso |
| `Projects/PROJECT_BOOTSTRAP.md` | `AI_ENTRYPOINT.md`, `Docs/LOAD_ORDER.md` | 04, 06 | Medio |
| `Projects/README.md` | — | 06 | Basso |
| `Templates/PROJECT.md` | `Templates/PROJECT.yaml` (coppia) | 06 | Basso |
| `Templates/CHECKLIST.md` | `Core/QA_SYSTEM.md` (uso correlato) | 06, 11 | Basso |
| `Templates/COLOR_SCHEME.yaml` | `Templates/PROJECT.yaml` (campo `paintScheme`) | 06, 08 | Basso |
| `Templates/APPROVED_TEXT.md` | `ApprovedAssets/README.md` | 09 | Basso |
| `Templates/README.md` | — | 06 | Basso |
| `Templates/PDF_CONFIG.yaml` | `Core/PDF_MASTER.md` (depends_on) | 12 | Medio |
| `PromptEngine/README.md` | `SDK_CONTEXT.yaml` (LOAD sequence) | 07 | Medio |
| `PromptEngine/Cover.md` … `FinalChecklist.md` (10 file) | `MANIFEST.yaml → pages[].prompt_file`, `Core/PAGE_SYSTEM.md` | 07 | Medio |
| `ApprovedAssets/README.md` | `AI_ENTRYPOINT.md → Approved Assets` | 09 | Alto |
| `Assets/README.md` | — | 08 | Basso |
| `Assets/DesignSystem/README.md` | `RepositoryManifest.yaml → assets.design_system` | 08 | Medio |
| `Assets/DesignSystem/Tokens/README.md` | — | 08 | Basso |
| `Assets/DesignSystem/Tokens/tokens.example.yaml` | `MANIFEST.yaml → design_tokens.source_file`, `Core/STYLE_GUIDE.md` | 08 | Critico (unico sorgente valori visivi — G06) |
| `Assets/DesignSystem/Tokens/tokens.schema.yaml` | `MANIFEST.yaml → design_tokens.schema_file` | 08 | Alto |
| `Assets/DesignSystem/Components/README.md` | — | 08 | Basso |
| `Assets/DesignSystem/Palette/README.md` | — | 08 | Basso |
| `Assets/DesignSystem/Typography/README.md` | — | 08 | Basso |
| `Assets/DesignSystem/Icons/README.md` | `RepositoryManifest.yaml → status: planned_v2.5.0` | 08, 14 | Basso |
| `Assets/DesignSystem/Layout/README.md` | — | 08 | Basso |
| `Assets/ReferenceModels/README.md` | — | 08, 13 | Basso |
| `Assets/ReferenceModels/Proto_Emperor/README.md` | — | 13 | Basso |
| `Assets/ApprovedManual/README.md` | `Core/MANUAL_SYSTEM.md § 8` | 12 | Medio |
| `Assets/ApprovedManual/Proto_Emperor/README.md` | — | 13 | Basso |
| `Assets/Examples/README.md` | — | 08 | Basso |
| `Config/README.md` | — | 01 | Basso |
| `Knowledge/README.md` | — | 07 | Basso |
| `Knowledge/Glossary.md` | — | 20 | Basso |
| `Knowledge/Paints.md`, `Masking.md`, `Preparation.md`, `Painting.md`, `Decals.md`, `ClearCoat.md` (6 file) | `Core/TEXT_ENGINE.md → input: Knowledge/` | 07 | Basso |
| `Tests/README.md` | — | 11 | Basso |
| `Tests/FrameworkIntegrity.md` | `MANIFEST.yaml → qa.test_suites` | 11 | Alto |
| `Tests/PromptValidation.md` | `PromptEngine/` (depends_on) | 07, 11 | Medio |
| `Tests/LayoutValidation.md` | `Core/COMPONENT_SYSTEM.md`, `Core/PAGE_SYSTEM.md` (depends_on) | 08, 11 | Medio |
| `Tests/NamingValidation.md` | `Core/NAMING_CONVENTION.md` (depends_on) | 08, 11 | Medio |
| `Tests/ColorValidation.md` | `Core/STYLE_GUIDE.md`, `tokens.example.yaml` (depends_on) | 08, 11 | Medio |
| `Tests/PDFValidation.md` | `Core/PDF_MASTER.md` (depends_on) | 11, 12 | Medio |
| `Tests/AssetsValidation.md` | — | 08, 11 | Basso |
| `Tests/ContentValidation.md` | `Core/TEXT_ENGINE.md` (depends_on) | 07, 11 | Alto |
| `Tests/TextValidation.md` | `Config/LANGUAGE_POLICY.yaml` (depends_on) | 07, 11 | Alto |

---

## Parte 3 — Documenti senza capitolo dipendente (gap)

Nessun documento canonico dei 105 catalogati risulta privo di un capitolo di destinazione, con l'eccezione delle esclusioni esplicite elencate in `DOCUMENT_COVERAGE.md` (`GPT.md`). Vedi `REPORT_FINALE.md` per il dettaglio quantitativo.
