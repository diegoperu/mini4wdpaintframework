# DOCUMENT_COVERAGE.md

**Manuale Operativo — Mini4WD Manual SDK**
**Generato il:** 2026-07-02 · **SDK analizzato:** v2.4.0 (codename CMS) · **Manual version:** 1.0.0 (baseline)

---

## ⚠️ Nota metodologica (leggere prima di tutto)

Al momento della generazione di questo sistema di validazione, **la directory `Documentation/OperationalManual/` non contiene ancora i capitoli del manuale** (nessun file `01_Introduction.md`, `04_Bootstrap.md`, ecc. esiste nel repository). Lo SDK a v2.4.0 documenta se stesso (`Core/`, `Docs/`, `Knowledge/`), ma non esiste ancora un "Manuale Operativo" separato per il manutentore/contributor.

Questo file adotta quindi una **struttura di capitoli assunta** (20 capitoli), derivata:

1. dalla checklist di esempio fornita nella richiesta (18 voci: AI EntryPoint → FAQ),
2. dall'ordine di lettura reale definito in `SDK_CONTEXT.yaml → load_order` e `Docs/LOAD_ORDER.md`,
3. dalla mappa di dipendenze in `RepositoryManifest.yaml → dependency_graph`.

Quando i capitoli reali verranno scritti in `Documentation/OperationalManual/`, dovranno usare questa numerazione (o il file va aggiornato di conseguenza — vedi `UPDATE_GUIDE.md`). Questo documento resta valido come **mappa di copertura target**: cosa ogni capitolo deve citare, non cosa cita oggi.

### Elenco capitoli assunto

| # | Capitolo | Corrisponde a (checklist richiesta) |
|---|----------|--------------------------------------|
| 01 | Introduction | (introduzione generale, non in checklist ma richiesta come ancora nell'esempio di traceability) |
| 02 | SDKContext | SDK Context |
| 03 | AIEntryPoint | AI EntryPoint |
| 04 | Bootstrap | Bootstrap |
| 05 | Workflow | Workflow |
| 06 | ProjectYaml | PROJECT.yaml |
| 07 | TextEngine | Text Engine |
| 08 | Assets | Assets |
| 09 | ApprovedAssets | Approved Assets |
| 10 | RenderEngine | Render Engine |
| 11 | QA | QA |
| 12 | PDF | PDF |
| 13 | GoldenProjects | Golden Projects |
| 14 | Roadmap | Roadmap |
| 15 | Versioning | Versioning |
| 16 | GitHubWorkflow | GitHub Workflow |
| 17 | BestPractices | Best Practices |
| 18 | Troubleshooting | Troubleshooting |
| 19 | FAQ | FAQ |
| 20 | Glossary | (non in checklist esplicita, ma citato come artefatto impattato in `CHANGE_IMPACT.md` — necessario per Terminology/GlossarioIT) |

---

## Capitolo 01 — Introduction

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 01 | `README.md` | documentation | Sì | 2026-07-02 |
| 01 | `AI_ENTRYPOINT.md` | bootstrap | Sì | 2026-07-02 |
| 01 | `SDK_CONTEXT.yaml` | bootstrap | Sì | 2026-07-02 |
| 01 | `MANIFEST.yaml` | manifest | Sì | 2026-07-02 |
| 01 | `RepositoryManifest.yaml` | manifest | Sì | 2026-07-02 |
| 01 | `Core/DOCUMENTATION_STYLE.md` | specification | Sì | 2026-07-02 |
| 01 | `STATUS.md` | status | No | 2026-07-02 |
| 01 | `Config/README.md` | documentation | No | 2026-07-02 |

- **Cartelle consultate:** root, `Core/`, `Config/`
- **File YAML utilizzati:** `SDK_CONTEXT.yaml`, `MANIFEST.yaml`, `RepositoryManifest.yaml`
- **README utilizzati:** `README.md` (root), `Config/README.md`
- **Source of Truth:** `SDK_CONTEXT.yaml` (identità SDK), `AI_ENTRYPOINT.md` (contratto di bootstrap)

---

## Capitolo 02 — SDKContext

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 02 | `SDK_CONTEXT.yaml` | bootstrap | Sì | 2026-07-02 |
| 02 | `ReleaseInfo.yaml` | release | Sì | 2026-07-02 |
| 02 | `Config/sdk.yaml` | configuration | Sì | 2026-07-02 |
| 02 | `VERSION` | metadata | Sì | 2026-07-02 |

- **Cartelle consultate:** root, `Config/`
- **File YAML utilizzati:** `SDK_CONTEXT.yaml`, `ReleaseInfo.yaml`, `Config/sdk.yaml`
- **README utilizzati:** nessuno
- **Source of Truth:** `SDK_CONTEXT.yaml`

---

## Capitolo 03 — AIEntryPoint

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 03 | `AI_ENTRYPOINT.md` | bootstrap | Sì | 2026-07-02 |

- **Cartelle consultate:** root
- **File YAML utilizzati:** nessuno (il file contiene un blocco YAML front-matter "Bootstrap Contract" incorporato)
- **README utilizzati:** nessuno
- **Source of Truth:** `AI_ENTRYPOINT.md` — assoluta, definisce Golden Rules G01–G10 e First Response Policy

---

## Capitolo 04 — Bootstrap

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 04 | `BOOTSTRAP.md` | bootstrap | Sì | 2026-07-02 |
| 04 | `AI_ENTRYPOINT.md` | bootstrap | Sì | 2026-07-02 |
| 04 | `SDK_CONTEXT.yaml` | bootstrap | Sì | 2026-07-02 |
| 04 | `Docs/LOAD_ORDER.md` | documentation | Sì | 2026-07-02 |
| 04 | `Docs/AI_BOOTSTRAP_PROMPT.md` | documentation | Sì | 2026-07-02 |
| 04 | `Docs/README.md` | documentation | No | 2026-07-02 |
| 04 | `Core/AI_OPERATING_RULES.md` | specification | Sì | 2026-07-02 |
| 04 | `Config/LANGUAGE_POLICY.yaml` | configuration | Sì | 2026-07-02 |
| 04 | `Projects/PROJECT_BOOTSTRAP.md` | guide | Sì | 2026-07-02 |

- **Cartelle consultate:** root, `Docs/`, `Core/`, `Config/`, `Projects/`
- **File YAML utilizzati:** `SDK_CONTEXT.yaml`, `Config/LANGUAGE_POLICY.yaml`
- **README utilizzati:** `Docs/README.md`
- **Source of Truth:** `BOOTSTRAP.md` per la sequenza operativa; `AI_ENTRYPOINT.md` per il contratto

---

## Capitolo 05 — Workflow

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 05 | `Core/WORKFLOW.md` | specification | Sì | 2026-07-02 |
| 05 | `Build/Pipeline.md` | documentation | Sì | 2026-07-02 |
| 05 | `Build/README.md` | documentation | No | 2026-07-02 |
| 05 | `Core/MANUAL_SYSTEM.md` | specification | Sì | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Build/`
- **File YAML utilizzati:** nessuno
- **README utilizzati:** `Build/README.md`
- **Source of Truth:** `Core/WORKFLOW.md` (workflow end-to-end), `Build/Pipeline.md` (8 fasi, Phase 0–7)

---

## Capitolo 06 — ProjectYaml

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 06 | `Templates/PROJECT.yaml` | template | Sì | 2026-07-02 |
| 06 | `Templates/PROJECT.md` | template | No | 2026-07-02 |
| 06 | `Templates/README.md` | documentation | No | 2026-07-02 |
| 06 | `Templates/CHECKLIST.md` | template | No | 2026-07-02 |
| 06 | `Templates/COLOR_SCHEME.yaml` | template | No | 2026-07-02 |
| 06 | `Templates/APPROVED_TEXT.md` | template | No | 2026-07-02 |
| 06 | `Projects/PROJECT_BOOTSTRAP.md` | guide | Sì | 2026-07-02 |
| 06 | `Projects/README.md` | documentation | No | 2026-07-02 |
| 06 | `Projects/Proto_Emperor/PROJECT.yaml` | project data | No (esempio) | 2026-07-02 |
| 06 | `Projects/Proto_Emperor/README.md` | documentation | No (esempio) | 2026-07-02 |

- **Cartelle consultate:** `Templates/`, `Projects/`, `Projects/Proto_Emperor/`
- **File YAML utilizzati:** `Templates/PROJECT.yaml`, `Templates/COLOR_SCHEME.yaml`, `Projects/Proto_Emperor/PROJECT.yaml`
- **README utilizzati:** `Templates/README.md`, `Projects/README.md`, `Projects/Proto_Emperor/README.md`
- **Source of Truth:** `Templates/PROJECT.yaml` (schema completo, campi `required: true`)

---

## Capitolo 07 — TextEngine

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 07 | `Core/TEXT_ENGINE.md` | specification | Sì | 2026-07-02 |
| 07 | `Config/LANGUAGE_POLICY.yaml` | configuration | Sì | 2026-07-02 |
| 07 | `PromptEngine/README.md` | documentation | Sì | 2026-07-02 |
| 07 | `PromptEngine/Cover.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/ColorScheme.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Materials.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Preparation.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Painting.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Masking.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Details.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Decals.md` | prompt | Sì | 2026-07-02 |
| 07 | `PromptEngine/Premium.md` | prompt | No (pagina condizionale P009) | 2026-07-02 |
| 07 | `PromptEngine/FinalChecklist.md` | prompt | Sì | 2026-07-02 |
| 07 | `Knowledge/EditorialStyle.md` | knowledge | Sì | 2026-07-02 |
| 07 | `Knowledge/Terminology.md` | knowledge | Sì | 2026-07-02 |
| 07 | `Knowledge/ForbiddenWords.md` | knowledge | Sì | 2026-07-02 |
| 07 | `Knowledge/GlossaryIT.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Glossary.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Paints.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Masking.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Preparation.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Painting.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/Decals.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/ClearCoat.md` | knowledge | No | 2026-07-02 |
| 07 | `Knowledge/README.md` | documentation | No | 2026-07-02 |
| 07 | `Tests/ContentValidation.md` | test_suite | Sì | 2026-07-02 |
| 07 | `Tests/TextValidation.md` | test_suite | Sì | 2026-07-02 |
| 07 | `Tests/PromptValidation.md` | test_suite | Sì | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Config/`, `PromptEngine/`, `Knowledge/`, `Tests/`
- **File YAML utilizzati:** `Config/LANGUAGE_POLICY.yaml`
- **README utilizzati:** `PromptEngine/README.md`, `Knowledge/README.md`
- **Source of Truth:** `Core/TEXT_ENGINE.md` (schema `content.yaml`, contratto Render Engine)

---

## Capitolo 08 — Assets (Design System)

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 08 | `Core/DESIGN_LANGUAGE.md` | specification | Sì | 2026-07-02 |
| 08 | `Core/STYLE_GUIDE.md` | specification | Sì | 2026-07-02 |
| 08 | `Core/COLOR_SYSTEM.md` | specification | Sì | 2026-07-02 |
| 08 | `Core/COMPONENT_SYSTEM.md` | specification | Sì | 2026-07-02 |
| 08 | `Core/PAGE_SYSTEM.md` | specification | Sì | 2026-07-02 |
| 08 | `Core/NAMING_CONVENTION.md` | specification | Sì | 2026-07-02 |
| 08 | `Assets/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/README.md` | documentation | Sì | 2026-07-02 |
| 08 | `Assets/DesignSystem/Tokens/tokens.example.yaml` | design_token | Sì | 2026-07-02 |
| 08 | `Assets/DesignSystem/Tokens/tokens.schema.yaml` | schema | Sì | 2026-07-02 |
| 08 | `Assets/DesignSystem/Tokens/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/Components/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/Palette/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/Typography/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/Icons/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/DesignSystem/Layout/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/ReferenceModels/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/ReferenceModels/Proto_Emperor/README.md` | documentation | No | 2026-07-02 |
| 08 | `Assets/Examples/README.md` | documentation | No | 2026-07-02 |
| 08 | `Tests/LayoutValidation.md` | test_suite | Sì | 2026-07-02 |
| 08 | `Tests/ColorValidation.md` | test_suite | Sì | 2026-07-02 |
| 08 | `Tests/NamingValidation.md` | test_suite | Sì | 2026-07-02 |
| 08 | `Tests/AssetsValidation.md` | test_suite | Sì | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Assets/`, `Assets/DesignSystem/*`, `Assets/ReferenceModels/`, `Assets/Examples/`, `Tests/`
- **File YAML utilizzati:** `tokens.example.yaml`, `tokens.schema.yaml`
- **README utilizzati:** tutti i README di `Assets/` e sottocartelle (9 file)
- **Source of Truth:** `Core/DESIGN_LANGUAGE.md` (65 regole) + `Assets/DesignSystem/Tokens/tokens.example.yaml` (unico sorgente di valori visivi — nessun hex/px hardcoded)

---

## Capitolo 09 — ApprovedAssets

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 09 | `ApprovedAssets/README.md` | documentation | Sì | 2026-07-02 |
| 09 | `ApprovedAssets/index.yaml` | registry | Sì | 2026-07-02 |
| 09 | `Core/DEFINITION_OF_DONE.md` | specification | Sì | 2026-07-02 |
| 09 | `Templates/APPROVED_TEXT.md` | template | No | 2026-07-02 |

- **Cartelle consultate:** `ApprovedAssets/`, `ApprovedAssets/Text/P00x/` (struttura di modulo, non contenuto per-progetto)
- **File YAML utilizzati:** `ApprovedAssets/index.yaml` + schema modulo (`content.yaml`, `metadata.yaml`, `manifest.yaml` — per pagina)
- **README utilizzati:** `ApprovedAssets/README.md`
- **Source of Truth:** `ApprovedAssets/Text/P00x/content.yaml` per-pagina (primario); `ApprovedAssets/index.yaml` per lo stato del ciclo di vita globale

---

## Capitolo 10 — RenderEngine

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 10 | `Core/RENDER_GUIDE.md` | specification | Sì | 2026-07-02 |
| 10 | `Config/render.yaml` | configuration | Sì | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Config/`
- **File YAML utilizzati:** `Config/render.yaml`
- **README utilizzati:** nessuno
- **Source of Truth:** `Core/RENDER_GUIDE.md` — vincolo: legge solo `content.yaml`, mai `text.md`

---

## Capitolo 11 — QA

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 11 | `Core/QA_SYSTEM.md` | specification | Sì | 2026-07-02 |
| 11 | `Config/quality.yaml` | configuration | Sì | 2026-07-02 |
| 11 | `Core/DEFINITION_OF_DONE.md` | specification | Sì | 2026-07-02 |
| 11 | `Tests/FrameworkIntegrity.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/ContentValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/TextValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/PromptValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/LayoutValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/NamingValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/ColorValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/PDFValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/AssetsValidation.md` | test_suite | Sì | 2026-07-02 |
| 11 | `Tests/README.md` | documentation | No | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Config/`, `Tests/` (9 suite)
- **File YAML utilizzati:** `Config/quality.yaml`
- **README utilizzati:** `Tests/README.md`
- **Source of Truth:** `Core/QA_SYSTEM.md` — 110 item, 45 bloccanti (vedi `MANIFEST.yaml → qa`)

---

## Capitolo 12 — PDF

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 12 | `Core/PDF_MASTER.md` | specification | Sì | 2026-07-02 |
| 12 | `Templates/PDF_CONFIG.yaml` | template | Sì | 2026-07-02 |
| 12 | `Config/pdf.yaml` | configuration | Sì | 2026-07-02 |
| 12 | `Tests/PDFValidation.md` | test_suite | Sì | 2026-07-02 |
| 12 | `Assets/ApprovedManual/README.md` | documentation | Sì | 2026-07-02 |

- **Cartelle consultate:** `Core/`, `Templates/`, `Config/`, `Tests/`, `Assets/ApprovedManual/`
- **File YAML utilizzati:** `Templates/PDF_CONFIG.yaml`, `Config/pdf.yaml`
- **README utilizzati:** `Assets/ApprovedManual/README.md`
- **Source of Truth:** `Core/PDF_MASTER.md`

---

## Capitolo 13 — GoldenProjects

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 13 | `Projects/Proto_Emperor/README.md` | documentation | Sì | 2026-07-02 |
| 13 | `Projects/Proto_Emperor/PROJECT.yaml` | project data | Sì | 2026-07-02 |
| 13 | `Assets/ReferenceModels/Proto_Emperor/README.md` | documentation | No | 2026-07-02 |
| 13 | `Assets/ApprovedManual/Proto_Emperor/README.md` | documentation | No | 2026-07-02 |
| 13 | `SDK_CONTEXT.yaml` (sezione `golden_project`) | bootstrap | Sì | 2026-07-02 |

- **Cartelle consultate:** `Projects/Proto_Emperor/`, `Assets/ReferenceModels/Proto_Emperor/`, `Assets/ApprovedManual/Proto_Emperor/`
- **File YAML utilizzati:** `Projects/Proto_Emperor/PROJECT.yaml`, `SDK_CONTEXT.yaml`
- **README utilizzati:** i 3 README elencati sopra
- **Source of Truth:** `Projects/Proto_Emperor/` — riferimento strutturale ufficiale (`SDK_CONTEXT.yaml → golden_project.status: reference`)

---

## Capitolo 14 — Roadmap

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 14 | `ROADMAP.md` | documentation | Sì | 2026-07-02 |
| 14 | `STATUS.md` | status | Sì | 2026-07-02 |
| 14 | `SDK_CONTEXT.yaml` (sezione `roadmap`) | bootstrap | No | 2026-07-02 |

- **Cartelle consultate:** root
- **File YAML utilizzati:** `SDK_CONTEXT.yaml`
- **README utilizzati:** nessuno
- **Source of Truth:** `ROADMAP.md`; `STATUS.md` per stato TODO corrente (TODO-001…TODO-008)

---

## Capitolo 15 — Versioning

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 15 | `VERSION` | metadata | Sì | 2026-07-02 |
| 15 | `CHANGELOG.md` | documentation | Sì | 2026-07-02 |
| 15 | `ReleaseInfo.yaml` | release | Sì | 2026-07-02 |
| 15 | `STYLE_DECISIONS.md` | documentation | Sì | 2026-07-02 |
| 15 | `MigrationReport_v2.4.md` | documentation | Sì | 2026-07-02 |
| 15 | `Docs/migration/v1-to-v2.md` | documentation | Sì | 2026-07-02 |
| 15 | `Core/MANUAL_SYSTEM.md` (§7 Version Management) | specification | Sì | 2026-07-02 |

- **Cartelle consultate:** root, `Docs/migration/`, `Core/`
- **File YAML utilizzati:** `ReleaseInfo.yaml`
- **README utilizzati:** nessuno
- **Source of Truth:** `VERSION` (numero corrente) + `CHANGELOG.md` (storico) + `STYLE_DECISIONS.md` (ADR-001–021, motivazioni delle decisioni)

---

## Capitolo 16 — GitHubWorkflow

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 16 | `README.md` (§ Contributing, § Quick Start) | documentation | Sì | 2026-07-02 |
| 16 | `LICENSE` | legal | Sì | 2026-07-02 |
| 16 | `SDK_CONTEXT.yaml` (sezione `repository`) | bootstrap | No | 2026-07-02 |

- **Cartelle consultate:** root
- **File YAML utilizzati:** `SDK_CONTEXT.yaml`
- **README utilizzati:** `README.md`
- **Source of Truth:** `README.md` — nessuna pipeline CI/CD presente nel repository (`.github/` assente); il workflow è solo di contribuzione (fork/branch/PR manuale), non automazione GitHub Actions

---

## Capitolo 17 — BestPractices

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 17 | `Knowledge/BestPractices.md` | knowledge | Sì | 2026-07-02 |
| 17 | `Core/AI_OPERATING_RULES.md` | specification | No (regole correlate) | 2026-07-02 |

- **Cartelle consultate:** `Knowledge/`, `Core/`
- **File YAML utilizzati:** nessuno
- **README utilizzati:** nessuno
- **Source of Truth:** `Knowledge/BestPractices.md`

---

## Capitolo 18 — Troubleshooting

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 18 | `Knowledge/Troubleshooting.md` | knowledge | Sì | 2026-07-02 |
| 18 | `STATUS.md` (§ Known Issues) | status | No | 2026-07-02 |

- **Cartelle consultate:** `Knowledge/`, root
- **File YAML utilizzati:** nessuno
- **README utilizzati:** nessuno
- **Source of Truth:** `Knowledge/Troubleshooting.md`

---

## Capitolo 19 — FAQ

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 19 | `Knowledge/FAQ.md` | knowledge | Sì | 2026-07-02 |

- **Cartelle consultate:** `Knowledge/`
- **File YAML utilizzati:** nessuno
- **README utilizzati:** nessuno
- **Source of Truth:** `Knowledge/FAQ.md`

---

## Capitolo 20 — Glossary (appendice)

| Capitolo | Documento SDK | Tipo | Obbligatorio | Ultima verifica |
|----------|---------------|------|--------------|-----------------|
| 20 | `Knowledge/Glossary.md` | knowledge | Sì | 2026-07-02 |
| 20 | `Knowledge/GlossaryIT.md` | knowledge | Sì | 2026-07-02 |
| 20 | `Knowledge/Terminology.md` | knowledge | Sì | 2026-07-02 |

- **Cartelle consultate:** `Knowledge/`
- **File YAML utilizzati:** nessuno
- **README utilizzati:** nessuno
- **Source of Truth:** `Knowledge/GlossaryIT.md` (italiano è l'unica lingua editoriale — vedi `Config/LANGUAGE_POLICY.yaml`)

---

## Esclusioni esplicite

| Documento | Motivo esclusione |
|-----------|--------------------|
| `GPT.md` | Marcato in `RepositoryManifest.yaml` come `"Not SDK-generated. Maintained by the user."` — fuori perimetro del manuale operativo |
| `.claude/` | Configurazione dello strumento AI locale, non parte dello SDK |
| `Assets/ApprovedManual/Proto_Emperor/manual.pdf` (se presente) | Output binario, non documento di specifica |
| Contenuti per-progetto in `ApprovedAssets/Text/P00x/*` (istanze) | Dati generati, non documenti di framework — la loro *struttura* è coperta al Cap. 09 |

**Totale documenti framework canonici catalogati:** 105 (vedi `TRACEABILITY_MATRIX.md` per l'elenco completo con dipendenze).
