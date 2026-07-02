# Migration Report — v2.4.0 → v2.4.1
# UX & Operator Workflow Update

**Data:** 2026-07-02 · **Tipo:** patch (solo UX/documentazione)
**Origine:** UAT-001 — primo test con operatore esterno (`UAT/UAT-001.md`)

---

## Principio della release

Il framework NON è cambiato: architettura, Prompt Engine, Text Engine, Component
System, Page System e struttura degli ApprovedAssets sono identici a v2.4.0.
È cambiata la documentazione: un operatore che non conosce gli inner working deve
poter arrivare dal clone al primo manuale seguendo solo i documenti del repository.

**Azioni richieste ai progetti esistenti: nessuna.**

---

## 1. Documenti creati

### Layer operatore (root)
| File | Contenuto |
|---|---|
| `START_HERE.md` | Primo documento per un nuovo utente: checklist, diagramma, tabella do/don't, mappa delle chat |
| `WORKFLOW.md` | State machine operativa (11 stati, con obiettivo/input/output/prossimo stato) |
| `LIFECYCLE.md` | Ciclo di vita macro (manuale) e micro (pagina) |
| `PROJECT_STRUCTURE.md` | Cartelle da creare/non creare; convenzione unica immagini |
| `FILE_MATRIX.md` | Ogni file: modificabile SÌ/NO, quando, da chi, in quale fase |
| `WHO_MODIFIES_WHAT.md` | Tabella artefatto → ruolo |
| `OPERATOR_PROFILE.md` | Ruoli: Operatore, Reviewer, Maintainer, Developer |
| `FIRST_PROJECT.md` | Tutorial: dal clone al Bootstrap OK (esempi reali) |
| `FIRST_RENDER.md` | Tutorial: da Approved Text alla prima pagina illustrata |
| `FIRST_PDF.md` | Tutorial: dal rendering al PDF (3 varianti) |
| `MigrationReport_v2.4.1.md` | Questo documento |

### OperatorGuide/
`01_Primo_Manuale.md`, `02_Workflow.md`, `03_File_da_Modificare.md`,
`04_File_da_NON_Modificare.md`, `05_Checklist.md`, `06_Errori_Comuni.md`,
`07_FAQ.md`, `README.md`

### UAT/
`UAT-001.md` — 8 errori documentati con descrizione / causa / correzione applicata /
documento aggiornato.

## 2. Documenti modificati

| File | Modifica |
|---|---|
| `Projects/PROJECT_BOOTSTRAP.md` | Riscritto: operativo, PASSO 1–8, italiano |
| `Docs/AI_BOOTSTRAP_PROMPT.md` | Riorganizzato per fasi (Bootstrap→Testi→QA→Render→PDF) con Input/Output/Prompt/Nuova chat SÌ-NO |
| `Config/LANGUAGE_POLICY.yaml` | §exceptions in 5 categorie language-neutral + §validation_scope |
| `Tests/ContentValidation.md` | Nuova §Validation Scope (Template vs Draft vs Approved) |
| `Tests/TextValidation.md` | Idem + target v2.4.x chiarito + TX-001-K esteso |
| `Core/WORKFLOW.md` §0.4 | Convenzione unica immagini |
| `Build/Pipeline.md` §Phase 1 | Convenzione unica immagini |
| `AI_ENTRYPOINT.md` | required_read_order: path immagini allineato |
| `Templates/PROJECT.yaml` | Campi `approved_text_dir` marcati LEGACY |
| `README.md` | Banner ingresso operatore, v2.4.1 |
| `Projects/README.md` | Set minimo file + nota convenzione immagini |
| 13 README di cartella | Header standard: a cosa serve / chi la modifica / quando |
| `CHANGELOG.md`, `VERSION`, `SDK_CONTEXT.yaml`, `MANIFEST.yaml`, `ReleaseInfo.yaml` | Release 2.4.1 |

## 3. Ambiguità eliminate

1. **Posizione immagini** — convenzione unica: `Projects/{Modello}/Images/` per
   l'operatore; `Assets/ReferenceModels/` solo Maintainer.
2. **Template vs contenuto finale** — i moduli `draft` con campi vuoti non si
   validano; ordine "genera → valida" esplicito ovunque.
3. **Falsi positivi linguistici** — nomi commerciali, codici vernice, termini tecnici,
   chiavi YAML e metadati dichiarati language-neutral.
4. **Nome cartella vs slug** — cartella con underscore, slug con trattini, con esempi.
5. **Set minimo di progetto** — PROJECT.yaml + Images/ + Output/ + Notes/.
6. **Placeholder** — `TODO:` per dati mancanti; `[TITOLO]`-style solo marcatori
   interni dei template.
7. **Fase → prompt → chat** — mappa esplicita con Nuova chat SÌ/NO per ogni fase.
8. **Entry point umano** — START_HERE.md distinto dall'entry point AI.

## 4. Compatibilità

- PROJECT.yaml: schema invariato
- Page ID / Component ID / token: invariati
- PromptEngine: invariato
- ApprovedAssets: struttura invariata
- Progetti v2.4.0: nessuna azione richiesta

## 5. TODO residui (fuori scope v2.4.1)

- README dei singoli moduli pagina (`ApprovedAssets/Text/P00x/README.md`) non ancora
  uniformati all'header standard (bassa priorità: documentazione interna al modulo)
- `Documentation/OperationalManual/` (20 capitoli): da riallineare alla convenzione
  unica immagini e alla §Validation Scope in una passata dedicata
- UAT-002: ripetere il test con secondo operatore partendo da `START_HERE.md`
- v2.5.0: Compiler/, Prompt Orchestrator, tutorial automatizzati
