# Quality Management System — README

**Mini4WD Manual SDK** · Quality Management System · Documento 19

| Campo | Valore |
|-------|--------|
| Scopo | Introdurre la cartella QualityManagement: perché esiste, come si usa, chi ne è responsabile |
| Destinatario | Tutti (primo documento da leggere di questa cartella) |
| Source of Truth | Questo documento per l'organizzazione del QMS; `20_INDEX.md` per la navigazione |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## 1. Perché esiste

Dalla v2.4.1 il Mini4WD Manual SDK è considerato **STABLE** (vedi `08_DECISION_LOG.md`, DEC-001). Il framework funziona; il rischio principale non è più "manca qualcosa" ma "qualcuno lo modifica senza motivo e rompe la coerenza".

Questo QMS esiste per una regola sola:

> **Ogni modifica al framework deve essere giustificata da evidenze documentate.**
> Bug confermati, UAT, Golden Project non realizzabili, cambiamenti nei modelli AI, o nuovi requisiti approvati. Le modifiche "a sentimento" sono vietate.

Il QMS è un layer documentale separato: **non modifica** Prompt Engine, Text Engine, Rendering Engine né la pipeline, e non entra nel load order di bootstrap dell'AI.

## 2. Come viene utilizzato

Il ciclo è questo:

```
Utilizzo reale (manuali, test)
        │
        ▼
Raccolta feedback ──── 03 User Report · 04 UAT · 05 Bug · 06 Feature
        │              13 Post-Mortem · 14 Retrospettiva
        ▼
Registri ───────────── 07 Known Issues · 09 Test History · 10 Golden Projects · 12 Metrics
        │
        ▼
Valutazione ────────── 15 Change Proposal → 11 Roadmap (stati) → 08 Decision Log
        │
        ▼
Release ────────────── 01 Release Policy · 02 Release Criteria → CHANGELOG + 17 Version History
```

I documenti 01–02 e 18 sono **normativi** (regole), 03–06 e 13–15 sono **template** (si copiano e si compilano), 07–12 e 17 sono **registri** (si aggiornano nel tempo).

I documenti compilati vivono nelle sottocartelle: `Reports/`, `Bugs/`, `Features/`, `PostMortems/`, `Retrospectives/`, `Changes/`. Gli UAT restano in `UAT/` alla root (DEC-003).

## 3. Quando compilare i documenti

| Situazione | Documento |
|------------|-----------|
| Ho trovato un errore riproducibile | `05_BUG_REPORT_TEMPLATE.md` → `Bugs/` |
| Ho finito una sessione di lavoro | `03_USER_REPORT_TEMPLATE.md` → `Reports/` |
| Ho completato un manuale | `14_RETROSPECTIVE_TEMPLATE.md` → `Retrospectives/` |
| Ho abbandonato un manuale | `13_POST_MORTEM_TEMPLATE.md` → `PostMortems/` |
| Mi è stato chiesto un test formale | `04_UAT_TEMPLATE.md` → `UAT/` (root) |
| Ho un'idea di miglioramento | `06_FEATURE_REQUEST_TEMPLATE.md` → `Features/` |
| Voglio proporre una modifica al framework | `15_CHANGE_PROPOSAL_TEMPLATE.md` → `Changes/` |

Il dettaglio (quando è obbligatorio, come consegnare) è in `16_OPERATOR_FEEDBACK.md`.

## 4. Chi è responsabile

| Ruolo | Nel QMS |
|-------|---------|
| **Operatore** | Compila template di feedback. NON aggiorna i registri, NON modifica il framework. |
| **Reviewer** | Prima analisi dei report: completezza, deduplica, richiesta chiarimenti. |
| **Maintainer** | Proprietario del QMS: conferma i bug, aggiorna i registri (07, 09, 10, 11, 12, 17), valuta le Change Proposal, decide le release secondo 01–02, mantiene il Decision Log. |
| **Developer** | Implementa le modifiche approvate; non decide cosa entra in release. |

Le definizioni dei ruoli sono in `OPERATOR_PROFILE.md` (root); questo documento ne definisce solo le responsabilità QMS.

## 5. Da dove iniziare

- Sei un **operatore** e hai appena finito (o interrotto) un manuale → §3 qui sopra.
- Sei il **Maintainer** e devi valutare una release → `02_RELEASE_CRITERIA.md`.
- Vuoi **proporre una modifica** → `15_CHANGE_PROPOSAL_TEMPLATE.md` (ma prima raccogli le evidenze).
- Vuoi solo **navigare** → `20_INDEX.md`.
