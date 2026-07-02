# REPORT FINALE — Documentation QA System

**Manuale Operativo — Mini4WD Manual SDK**
**Generato il:** 2026-07-02 · **Aggiornato il:** 2026-07-02 (post TODO-D01 + TODO-D05 + TODO-D06 parziale) · **SDK analizzato:** v2.4.0 (codename CMS)

---

## Numeri

| Metrica | Valore |
|---------|--------|
| Capitoli del Manuale Operativo (struttura assunta) | 20 |
| Capitoli effettivamente scritti in `Documentation/OperationalManual/` | **20 / 20** |
| Capitoli PASS su tutti gli 8 criteri di `CONSISTENCY_CHECK.md` Parte 1 | **20 / 20** |
| Documenti del framework analizzati (canonici) | 105 |
| Documenti mappati a un capitolo | 105 / 105 |
| Percentuale di copertura mappata (planning) | **100%** |
| Percentuale di copertura scritta (contenuto reale) | **100%** |
| Documenti del framework non documentabili / esclusi | 1 (`GPT.md` — non-SDK, mantenuto dall'utente) |
| Capitoli privi di riferimenti SDK | 0 |
| Difetti editoriali nei capitoli, scoperti da TODO-D05 e corretti | 3 (nessuno resta aperto) |
| Inconsistenze del framework SDK identificate (C10–C20) | **11** |
| Inconsistenze **risolte alla fonte** (2026-07-02) | **8** (C10, C12, C13, C15, C16, C18, C19, C20) |
| Inconsistenze **parzialmente risolte** | **2** (C11, C14 — parte restante richiede decisione di specifica/restructuring) |
| Inconsistenze **ancora aperte** | **1** (C17 — decisione di prodotto pura) |
| File SDK modificati per le correzioni | 22 |
| Nuove voci ADR aggiunte (`STYLE_DECISIONS.md`) | 1 (ADR-022, copre le 5 modifiche a `Core/`) |
| `documentation.validated` in `DOCUMENTATION_STATUS.yaml` | **true** |

## Cosa esiste oggi vs cosa è stato creato

Il repository non conteneva alcun Manuale Operativo prima di questo task. Quattro passaggi:

1. **Sistema di validazione** (`Documentation/OperationalManual/Validation/`, 8 file) — specifica di riferimento costruita prima che i capitoli esistessero.
2. **I 20 capitoli reali** (`Documentation/OperationalManual/01_Introduction.md` … `20_Glossary.md`, TODO-D01) — scritti da 4 agenti in parallelo, nessun contenuto inventato (disciplina G04).
3. **Consistency check formale** (TODO-D05) — 4 agenti in parallelo hanno verificato ogni capitolo sugli 8 criteri di Parte 1. 3 difetti editoriali nei capitoli corretti; 2 nuove inconsistenze framework trovate (C19, C20).
4. **Correzione dei bug reali** (TODO-D06, su richiesta esplicita dell'utente) — piano di fix presentato per l'approvazione prima di ogni modifica (governance `Core/ → modify_requires_adr: true` rispettata via ADR-022). 4 agenti paralleli hanno applicato le correzioni su file disgiunti, poi verifica indipendente eseguita da me su grep/YAML-parse/git status.

## Documenti del framework non documentati

Nessuno, con l'eccezione dichiarata di `GPT.md`.

## Capitoli privi di riferimenti

Nessuno.

## Difetti editoriali nei capitoli — corretti (TODO-D05)

| Capitolo | Problema | Correzione |
|----------|----------|------------|
| `04_Bootstrap.md` | "sequenza completa a 13 passi" vs propria tabella di 14 righe | Corretto: Step 0 precede i 13 passi di `SDK_CONTEXT.yaml` |
| `04_Bootstrap.md` | RULE-070/085 attribuite anche alla "formattazione date" — non esiste tale regola | Rimosso riferimento alle date |
| `07_TextEngine.md` | "24 sostituzioni" in `ForbiddenWords.md` — conteggio reale 25 | Corretto a 25 |

## Inconsistenze del framework SDK — stato finale (C10–C20)

| # | Documento SDK | Problema | Stato |
|---|----------------|----------|-------|
| C10 | `Core/WORKFLOW.md` § Phase 2 | Flusso pre-CMS, nessuna menzione di `content.yaml`/`ApprovedAssets/` | ✅ **Risolto** — Phase 2 riscritta al flusso CMS v2.4.0 |
| C11 | `PromptEngine/*.md` (10 file) | Output verso `Output/raw/`, mai `content.yaml`; hex hardcoded (viola G06) | ⚠️ **Parziale** — percorso corretto in tutti i 10 file; 248/269 hex sostituiti con token. Restano: 21 hex senza token corrispondente, gradient (RULE-016, separato), mismatch strutturale (prompt Text-mode pieni di layout quando dovrebbero averne zero) |
| C12 | `Core/MANUAL_SYSTEM.md` §5 / `Projects/PROJECT_BOOTSTRAP.md` §Step 2 | Tre schemi `PROJECT.yaml` incompatibili | ✅ **Risolto** — entrambi riscritti per matchare `Templates/PROJECT.yaml` (canonico) |
| C13 | `Core/NAMING_CONVENTION.md` §2.1 | File di esempio inesistente | ✅ **Risolto** — regola divisa Docs/ top-level vs Docs/migration/ |
| C14 | `Config/quality.yaml` + `Knowledge/FAQ.md` | 9 ID bloccanti dichiarati contro 45 attesi; QA-017/QA-021 scambiati | ⚠️ **Parziale** — scambio QA-017/021 corretto in entrambi i file. Resta aperto: `Core/QA_SYSTEM.md` non marca alcun item come bloccante — il "45" in `MANIFEST.yaml` non ha base tracciabile in nessun documento. Non ricostruibile senza specifica del maintainer |
| C15 | `Core/PDF_MASTER.md` | Variante "archive" non documentata | ✅ **Risolto** — 5 sezioni aggiunte/modificate |
| C16 | `Projects/Proto_Emperor/README.md` | 4 file dichiarati "✓ Filled" ma inesistenti | ✅ **Risolto** — anche corretta la stessa collisione C00N trovata indipendentemente nella tabella Paint Scheme dello stesso file |
| C17 | `STATUS.md`/`SDK_CONTEXT.yaml`/`ReleaseInfo.yaml` vs `ROADMAP.md`/`MigrationReport_v2.4.md` | Scope v2.5.0 discorde; date v3.0.0/v2.5.0/2.1.0/2.2.0 in conflitto | ❌ **Aperto** — decisione di prodotto, nessuna priorità oggettiva nel repository. `ROADMAP.md` contiene sezioni v2.2.0/v2.3.0/v3.0.0 duplicate mai riconciliate (probabile causa radice) |
| C18 | `Tests/README.md` | 7 suite dichiarate, 9 presenti | ✅ **Risolto** — righe aggiunte, conteggio corretto |
| C19 | `Templates/PROJECT.yaml` | ID colore vernice `C00N` collide col registro Component ID | ✅ **Risolto** — rinominati `PC00N` in `Templates/PROJECT.yaml` (2) e `Projects/Proto_Emperor/PROJECT.yaml` (17, verificate 0 residue) |
| C20 | `Config/render.yaml` vs `Core/RENDER_GUIDE.md` | Risoluzione P002 discordante | ✅ **Risolto** — `RENDER_GUIDE.md` sincronizzato a 1000×800px/150dpi |

**Bonus, fuori scope originale:** `PromptEngine/README.md` conteneva la stessa istruzione `Output/raw/` obsoleta di C11, trovata durante la verifica finale e corretta.

## File modificati (22)

`Core/WORKFLOW.md`, `Core/MANUAL_SYSTEM.md`, `Core/NAMING_CONVENTION.md`, `Core/PDF_MASTER.md`, `Core/RENDER_GUIDE.md`, `Config/quality.yaml`, `Knowledge/FAQ.md`, `Projects/PROJECT_BOOTSTRAP.md`, `Projects/Proto_Emperor/PROJECT.yaml`, `Projects/Proto_Emperor/README.md`, `Templates/PROJECT.yaml`, `Tests/README.md`, `STYLE_DECISIONS.md` (nuova ADR-022), `PromptEngine/README.md`, e i 10 file `PromptEngine/{Cover,ColorScheme,Materials,Preparation,Painting,Masking,Details,Decals,Premium,FinalChecklist}.md`.

Nessun commit creato — modifiche nel working tree, in attesa di revisione/commit da parte dell'utente.

## TODO

| ID | Descrizione | Priorità | Stato |
|----|-------------|----------|-------|
| ~~TODO-D01~~ | ~~Scrivere i 20 capitoli reali~~ | Alta | ✅ **Completato** |
| ~~TODO-D05~~ | ~~Consistency check formale su tutti i 20 capitoli~~ | Alta | ✅ **Completato** |
| ~~TODO-D06~~ | ~~Risolvere le inconsistenze framework~~ | Alta | ✅ **8/11 completate**, 2 parziali, 1 aperta (vedi tabella sopra) |
| TODO-D02 | Se la struttura a 20 capitoli viene rifiutata/modificata dal maintainer, aggiornare tutti i file di `Validation/` E i 20 capitoli di conseguenza | Alta |
| TODO-D03 | Popolare `ApprovedAssets/Text/` per Proto_Emperor (`STATUS.md` TODO-007) | Media |
| TODO-D08 | C11 residuo: decidere se i prompt PromptEngine devono essere ristrutturati per essere puro Text-mode (zero layout/hex) o se la loro natura ibrida è intenzionale; se ibrida, aggiornare `PromptEngine/README.md` che oggi dichiara il contrario | Alta (decisione architetturale) |
| TODO-D09 | C14 residuo: definire quali dei 110 item di `Core/QA_SYSTEM.md` sono realmente bloccanti (0 oggi marcati); poi ricostruire `Config/quality.yaml` per intero | Alta (decisione di specifica) |
| TODO-D10 | C17: scegliere/fondere lo scope v2.5.0 tra le due liste divergenti; ripulire le sezioni duplicate in `ROADMAP.md`; riconciliare le date 2.1.0/2.2.0 | Alta (decisione di prodotto) |
| TODO-D07 | Decidere se `16_GitHubWorkflow.md` deve restare descrittivo del solo flusso manuale o anticipare una futura pipeline `.github/workflows/` | Bassa |

## Suggerimenti per migliorare ulteriormente il framework SDK

- Aggiungere un campo `manual_chapter:` per documento in `RepositoryManifest.yaml`, per chiudere il cerchio con `DOCUMENT_COVERAGE.md`
- La causa radice più ricorrente in questo giro era: **documenti aggiornati a v2.4.0 (CMS) convivevano con documenti mai migrati.** Un `MigrationReport` per versione dovrebbe includere una checklist esplicita "file X aggiornato? [ ]" per ogni file toccato dal cambio di architettura — avrebbe intercettato C10, C11, C20 prima che arrivassero a questo punto
- `ROADMAP.md` ha bisogno di una pulizia strutturale indipendente da C17: contiene sezioni duplicate/superate (v2.2.0, v2.3.0, v3.0.0) mai rimosse, che è la causa più probabile della divergenza di scope in C17
- Nessun file marca esplicitamente quali delle 100 regole in `Core/AI_OPERATING_RULES.md` sono "G-level"

## Suggerimenti per migliorare il Manuale Operativo

- Il Capitolo 20 (Glossario) resta l'unico non richiesto esplicitamente nella checklist originale — confermare con il maintainer
- Valutare un'appendice "Difetti noti dello SDK" nel manuale stesso, che punti a `Validation/CONSISTENCY_CHECK.md`, così un lettore la vede senza dover consultare la cartella QA
- Prossimo ciclo di manutenzione reale: la prossima release SDK (v2.5.0) — a quel punto seguire `UPDATE_GUIDE.md` dall'inizio, e i TODO-D08/D09/D10 sopra andrebbero risolti prima o durante quel ciclo

---

**Stato finale:** Manuale Operativo completo e validato (20/20 capitoli, `validated: true`). 8 delle 11 inconsistenze framework scoperte durante la stesura sono state corrette alla fonte su richiesta esplicita dell'utente, con piano di modifica presentato e approvato prima dell'esecuzione, e governance ADR rispettata. 2 restano parzialmente aperte (decisioni di specifica/restructuring), 1 completamente aperta (decisione di prodotto) — tutte e 3 tracciate con TODO dedicati per il maintainer SDK.
