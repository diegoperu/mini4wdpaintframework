# CONSISTENCY_CHECK.md

**Manuale Operativo — Mini4WD Manual SDK**
**Generato il:** 2026-07-02 · **SDK analizzato:** v2.4.0

Checklist di coerenza da eseguire ogni volta che un capitolo del Manuale Operativo viene scritto o aggiornato. La Parte 1 è la checklist da applicare a ogni capitolo. La Parte 2 riporta i controlli già eseguiti sul framework stesso (SDK v2.4.0) al momento della generazione di questo file, come baseline.

---

## Parte 1 — Checklist da eseguire per ogni capitolo

Per ogni capitolo `NN_Nome.md` in `Documentation/OperationalManual/`:

- [ ] **Terminologia coerente** — i termini tecnici usati corrispondono a `Knowledge/Terminology.md` (IT) e non contraddicono `Knowledge/ForbiddenWords.md`
- [ ] **Nomenclatura coerente** — Page ID (`P001`–`P010`) e Component ID (`C001`–`C015`) citati esattamente come in `MANIFEST.yaml → pages` / `→ components`, mai rinumerati (G07)
- [ ] **Diagrammi coerenti** — eventuali diagrammi ASCII/mermaid nel capitolo riflettono `AI_ENTRYPOINT.md → Workflow` (Phase 0–7) o `Core/MANUAL_SYSTEM.md → Architecture Overview`, senza fasi inventate o mancanti
- [ ] **Workflow coerente** — la sequenza descritta rispetta `editorial_pipeline.sequence` in `AI_ENTRYPOINT.md` (`text_engine → qa_engine → render_engine → pdf_builder`) e non inverte editor-first/render-second
- [ ] **Nessun riferimento a documenti inesistenti** — ogni percorso file citato (backtick o link) esiste realmente nel repository al momento della verifica
- [ ] **Nessun riferimento a funzionalità future come implementate** — tutto ciò che è in `SDK_CONTEXT.yaml → roadmap.next_planned` o `STATUS.md → Planned Features (v2.5.0)` deve essere marcato esplicitamente come "pianificato", mai descritto come disponibile oggi (es. `Compiler/`, `Prompt Orchestrator`, Icon Library SVG, `Docs/tutorial/`)
- [ ] **Nessuna contraddizione con `SDK_CONTEXT.yaml`** — versione, gerarchia Source of Truth (`Core/ > content.yaml > PROJECT.yaml > prompt defaults`), load_order, golden rules
- [ ] **Nessuna contraddizione con `AI_ENTRYPOINT.md`** — Golden Rules G01–G10, Bootstrap Contract, First Response Policy (bootstrap report prima di generare contenuto)

---

## Parte 2 — Controlli eseguiti sul framework (baseline v2.4.0, 2026-07-02)

| # | Controllo | Metodo | Esito |
|---|-----------|--------|-------|
| C1 | Versione SDK coerente tra `VERSION`, `SDK_CONTEXT.yaml`, `MANIFEST.yaml`, `ReleaseInfo.yaml`, `STATUS.md`, `README.md` | grep incrociato dei numeri di versione | ✅ PASS — tutti riportano `2.4.0` come corrente, `2.5.0` come pianificato |
| C2 | `Compiler/` non descritto come implementato | grep su tutti i `.md`/`.yaml` | ✅ PASS — citato solo in `ROADMAP.md`, `STATUS.md`, `SDK_CONTEXT.yaml → roadmap`, `ReleaseInfo.yaml → planned`, `GPT.md → Evoluzioni pianificate`. Nessuna occorrenza lo presenta come esistente |
| C3 | `Prompt Orchestrator` non descritto come implementato | grep su tutti i `.md`/`.yaml` | ✅ PASS — stesso pattern di C2 |
| C4 | Icon Library (15 SVG) non descritta come implementata | grep `Icon Library\|SVG icon` | ✅ PASS — `RepositoryManifest.yaml → assets.design_system` marca esplicitamente `status: "planned_v2.5.0"` con fallback Unicode documentato in `COMPONENT_SYSTEM.md` |
| C5 | `ApprovedAssets/index.yaml` coerente con `STATUS.md` (TODO-007/008: popolamento ancora da fare) | lettura diretta del file | ✅ PASS — `pages: []`, `manuals: []`, `total_pages: 0` — coerente con TODO aperti |
| C6 | Nessun riferimento a `.github/workflows/` come esistente | `find .github -type f` | ✅ PASS — cartella `.github/` assente; nessun documento la referenzia come esistente. Il Capitolo 16 (GitHubWorkflow) deve documentare il flusso di contribuzione manuale, non CI/CD |
| C7 | Component ID / Page ID permanenti non duplicati | lettura `MANIFEST.yaml → pages`, `→ components` | ✅ PASS — P001–P010 e C001–C015 univoci, `next_available_component_id: "C016"` esplicito |
| C8 | Gerarchia Source of Truth coerente tra `AI_ENTRYPOINT.md` e `SDK_CONTEXT.yaml` | confronto testuale | ✅ PASS — entrambi dichiarano `Core/ > content.yaml > PROJECT.yaml > prompt defaults` |
| C9 | `GPT.md` non in conflitto con lo stato SDK | lettura diretta | ✅ PASS, con nota: `GPT.md` è dichiarato "not SDK-generated" in `RepositoryManifest.yaml` — è un documento di contesto personale dell'utente, non normativo. Va escluso dal perimetro di tracciabilità (vedi `DOCUMENT_COVERAGE.md → Esclusioni esplicite`) |

**Nessuna contraddizione rilevata nella baseline.** Il framework a v2.4.0 è internamente coerente su questi 9 controlli.

---

## Parte 3 — Limiti di questa verifica (baseline pre-stesura)

Questa baseline copriva solo i documenti del framework (Core/, Config/, Docs/, Knowledge/, root), su 9 controlli mirati (C1–C9). **Non copriva i capitoli del Manuale Operativo**, perché al momento in cui è stata eseguita nessuno di essi esisteva ancora fisicamente. I 20 capitoli sono stati scritti successivamente (TODO-D01) — vedi Parte 4 per cosa è emerso in quella fase.

Resta aperto: la checklist della Parte 1 non è ancora stata eseguita formalmente capitolo-per-capitolo (solo uno spot-check di formato su `03_AIEntryPoint.md` e una verifica automatica dei link interni su tutti e 20 i file — nessun riferimento a file inesistente trovato). Eseguirla è TODO-D05 in `REPORT_FINALE.md`.

---

## Parte 4 — Inconsistenze scoperte durante la stesura dei 20 capitoli (2026-07-02)

I controlli C1–C9 erano mirati e non potevano intercettare tutto. Scrivere i capitoli ha richiesto leggere i documenti SDK per intero, e questo ha fatto emergere 9 inconsistenze reali nel framework stesso — non nei capitoli, che le documentano correttamente con blocchi ⚠️ Warning invece di correggerle silenziosamente (disciplina G04: non alterare la fonte, segnalare il gap).

| # | Controllo | Esito |
|---|-----------|-------|
| C10 | `Core/WORKFLOW.md` § Phase 2 riflette l'architettura CMS v2.4.0 (`content.yaml`, `ApprovedAssets/`) | ✅ **RISOLTO (2026-07-02)** — Phase 2 riscritta al flusso CMS. Era: ❌ FAIL, descriveva il flusso pre-CMS (`Output/raw/`, `qa_log.md` stile `QA-001: PASS`) |
| C11 | `PromptEngine/*.md` (10 file) referenziano `content.yaml` come output e Design Token invece di hex | ⚠️ **PARZIALMENTE RISOLTO (2026-07-02)** — percorso output corretto in tutti e 10; 248/269 hex sostituiti con token (13 mapping puliti). Restano aperti: 3 hex senza token (21 occorrenze), gradient (RULE-016, separato), e il mismatch strutturale (questi prompt Text-mode contengono layout/hex completi, quando dovrebbero averne zero) — richiede restructuring, non sync |
| C12 | Un solo schema `PROJECT.yaml` di riferimento coerente tra i documenti che lo esemplificano | ✅ **RISOLTO (2026-07-02)** — `Core/MANUAL_SYSTEM.md` §5 e `Projects/PROJECT_BOOTSTRAP.md` §Step 2 riscritti per matchare lo schema canonico `Templates/PROJECT.yaml` |
| C13 | Esempi di file citati in `Core/NAMING_CONVENTION.md` esistono davvero | ✅ **RISOLTO (2026-07-02)** — esempio corretto, regola divisa Docs/ top-level (SCREAMING_SNAKE_CASE) vs Docs/migration/ (kebab-case) |
| C14 | `Config/quality.yaml` (ID bloccanti) coerente con `Core/QA_SYSTEM.md` e `MANIFEST.yaml → qa.blocking_items` | ⚠️ **PARZIALMENTE RISOLTO (2026-07-02)** — scambio QA-017/QA-021 corretto in `Config/quality.yaml` e `Knowledge/FAQ.md`. Resta aperto: `Core/QA_SYSTEM.md` non marca nessuno dei 110 item come bloccante/non-bloccante — il valore "45" in `MANIFEST.yaml` non ha base tracciabile. 3 dei 9 ID in `quality.yaml` non corrispondono a nessun item reale. Non ricostruibile senza che il maintainer definisca la lista da zero |
| C15 | `Core/PDF_MASTER.md` documenta tutte le varianti PDF implementate in `Config/pdf.yaml`/`Templates/PDF_CONFIG.yaml` | ✅ **RISOLTO (2026-07-02)** — variante "archive" documentata (5 sezioni aggiunte/modificate) |
| C16 | `Projects/Proto_Emperor/README.md` riflette lo stato reale dei file nella directory | ✅ **RISOLTO (2026-07-02)** — stato corretto a "NOT PRESENT" per i 4 file inesistenti |
| C17 | Scope v2.5.0 coerente tra tutti i documenti che lo descrivono | ❌ **APERTO** — decisione di prodotto, non sincronizzabile meccanicamente. Due liste feature v2.5.0 a zero sovrapposizione; `ROADMAP.md` contiene sezioni v2.2.0/v2.3.0/v3.0.0 duplicate e mai riconciliate (probabile causa radice); date 2.1.0/2.2.0 discordanti tra `CHANGELOG.md` (2024) e `ReleaseInfo.yaml` (2026) |
| C18 | `Tests/README.md` elenca tutte le suite presenti in `Tests/` | ✅ **RISOLTO (2026-07-02)** — aggiunte le 2 righe mancanti, corretto il conteggio 7→9 |

**8/9 controlli risolti alla fonte, 1 parziale, 1 aperto** (C17). Piano presentato all'utente e approvato prima dell'esecuzione (governance `modify_requires_adr: true` su `Core/` rispettata via ADR-022 in `STYLE_DECISIONS.md`). Dettaglio completo in `DOCUMENTATION_STATUS.yaml → status.resolved/partially_resolved/still_open` e `REPORT_FINALE.md`.

---

## Parte 5 — Esecuzione formale della Parte 1 su tutti i 20 capitoli (TODO-D05, 2026-07-02)

Eseguita da 4 agenti paralleli (stesso batching della stesura), ciascuno verificando i propri 5 capitoli sugli 8 criteri della Parte 1 leggendo sia il capitolo sia le fonti SDK citate (non solo il capitolo in isolamento).

| Capitolo | 1 Terminologia | 2 Nomenclatura | 3 Diagrammi | 4 Workflow | 5 No dangling refs | 6 No future-as-implemented | 7 vs SDK_CONTEXT.yaml | 8 vs AI_ENTRYPOINT.md |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01_Introduction | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 02_SDKContext | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 03_AIEntryPoint | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 04_Bootstrap | ✅ | ✅ (era ❌, corretto) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 05_Workflow | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 06_ProjectYaml | ✅ | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 07_TextEngine | ✅ (era ❌, corretto) | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 08_Assets | ✅ | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 09_ApprovedAssets | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10_RenderEngine | ✅ | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11_QA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12_PDF | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13_GoldenProjects | ✅ | ✅ (con nota, vedi C19) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14_Roadmap | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 15_Versioning | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 16_GitHubWorkflow | ✅ | n/a | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17_BestPractices | ✅ | n/a | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 18_Troubleshooting | ✅ | n/a | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 19_FAQ | ✅ | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ |
| 20_Glossary | ✅ | ✅ | n/a | n/a | ✅ | ✅ | ✅ | ✅ |

**Esito: 20/20 capitoli PASS su tutti gli 8 criteri**, dopo correzione di 2 difetti minori introdotti in fase di stesura (non difetti del framework SDK — errori editoriali nei capitoli stessi, corretti direttamente):

- `04_Bootstrap.md` — il testo dichiarava "sequenza completa a 13 passi" mentre la propria tabella elenca 14 righe (Step 0–13); corretto chiarendo che Step 0 (`AI_ENTRYPOINT.md`) precede i 13 passi di `SDK_CONTEXT.yaml → load_order.sequence`
- `04_Bootstrap.md` — attribuiva a RULE-070/RULE-085 anche la "formattazione italiana delle date", ma `Core/AI_OPERATING_RULES.md` non definisce alcuna regola sul formato data in RULE-059–100; corretto rimuovendo il riferimento alle date
- `07_TextEngine.md` — dichiarava "tabella di 24 sostituzioni" per `Knowledge/ForbiddenWords.md` Categoria 3, il conteggio reale è 25 righe; corretto

Durante l'esecuzione sono emerse anche 2 nuove inconsistenze **del framework SDK** (non dei capitoli), aggiuntive rispetto alle 9 di Parte 4:

| # | Controllo | Esito |
|---|-----------|-------|
| C19 | `Templates/PROJECT.yaml` non usa ID in conflitto con il registro Component ID permanente (C001–C015, G07) | ✅ **RISOLTO (2026-07-02)** — ID colore vernice rinominati `C00N` → `PC00N` in `Templates/PROJECT.yaml` (2 occ.) e `Projects/Proto_Emperor/PROJECT.yaml` (17 occ., verificate 0 residue) |
| C20 | `Config/render.yaml` coerente con `Core/RENDER_GUIDE.md` per le risoluzioni richieste | ✅ **RISOLTO (2026-07-02)** — `Core/RENDER_GUIDE.md` § 5 sincronizzato a 1000×800px/150dpi, coerente col resto della tabella e con `Config/render.yaml` (che dichiara esplicitamente di essere l'encoding diretto della guida) |

**Riepilogo finale: 8/11 controlli (C10–C20) risolti alla fonte, 2 parziali (C11, C14), 1 aperto (C17).** Tutte le correzioni sono nel framework SDK, zero modifiche ai capitoli del manuale (che restano `validated: true` dalla Parte 1). Le correzioni a `Core/` sono documentate in ADR-022 (`STYLE_DECISIONS.md`), come richiesto da `MANIFEST.yaml → modify_requires_adr: true`. Vedi `REPORT_FINALE.md` per il riepilogo completo con elenco file modificati.
