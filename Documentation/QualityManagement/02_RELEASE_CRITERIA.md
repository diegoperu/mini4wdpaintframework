# Release Criteria

**Mini4WD Manual SDK** · Quality Management System · Documento 02

| Campo | Valore |
|-------|--------|
| Scopo | Definire le soglie oggettive che autorizzano una nuova release |
| Destinatario | Maintainer |
| Source of Truth | Questo documento |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## 1. Regola generale

Nessuna release può essere creata senza che almeno un criterio della sua categoria sia soddisfatto **con evidenze documentate** (bug report, UAT, report operatore o feature request archiviati in questo QMS). "Mi sembra meglio così" non è un criterio.

Il Maintainer verifica i criteri, compila la checklist di rilascio (§5) e registra la release in `17_VERSION_HISTORY.md`.

---

## 2. Criteri per Patch Release (x.y.Z)

Una Patch può essere rilasciata se vale **almeno una** delle seguenti condizioni:

- □ almeno **1 bug bloccante** confermato (Severità: Blocker — impedisce di completare un manuale)
- □ almeno **3 bug confermati** di severità qualsiasi (Bug ID registrati con `05_BUG_REPORT_TEMPLATE.md`)
- □ almeno **2 UAT** evidenziano lo **stesso problema** (stessa causa radice, anche con sintomi diversi)
- □ almeno **2 User Report** (`03_USER_REPORT_TEMPLATE.md`) segnalano lo stesso documento come poco chiaro E l'ambiguità ha causato un errore operativo
- □ un cambiamento nei modelli AI rende errata un'istruzione esistente (evidenza: test documentato in `09_TEST_HISTORY.md`)

**Vincolo:** la Patch corregge SOLO i problemi che l'hanno giustificata. Niente correzioni "già che ci siamo".

---

## 3. Criteri per Minor Release (x.Y.0)

Una Minor può essere rilasciata se vale **almeno una** delle seguenti condizioni:

- □ **nuovo componente** o tipologia di pagina, approvato in `11_ROADMAP.md` (stato APPROVATO) e motivato da almeno 1 Feature Request o 1 Golden Project non realizzabile
- □ **nuova funzionalità** retrocompatibile con Change Proposal approvata
- □ **modifica della pipeline** retrocompatibile, richiesta da almeno 2 UAT o 1 Golden Project non realizzabile
- □ **deprecazione** pianificata in roadmap (funzionalità marcata LEGACY)
- □ **nuovo sistema documentale** (es. OperatorGuide in v2.4.1, questo QMS)
- □ accumulo di **5+ bug confermati** non bloccanti la cui correzione richiede modifiche oltre l'ambito Patch

**Vincoli aggiuntivi:**

- almeno **1 manuale di test** completato con successo con la versione candidata (registrato in `09_TEST_HISTORY.md`)
- `CHANGELOG.md`, `VERSION`, `MANIFEST.yaml`, `SDK_CONTEXT.yaml`, `ReleaseInfo.yaml` aggiornati

---

## 4. Criteri per Major Release (X.0.0)

Una Major può essere rilasciata SOLO se valgono **tutte** le seguenti condizioni:

- □ la breaking change è comparsa in `11_ROADMAP.md` (stato APPROVATO) almeno una Minor prima
- □ Change Proposal approvata con analisi di impatto e compatibilità
- □ Decision Log aggiornato (`08_DECISION_LOG.md`)
- □ Migration Report scritto e verificato su almeno 1 progetto reale
- □ almeno **1 Golden Project** completato end-to-end con la versione candidata
- □ nessun bug Blocker aperto in `07_KNOWN_ISSUES.md`

---

## 5. Checklist di rilascio (tutte le release)

- □ criteri della categoria soddisfatti, con riferimenti alle evidenze (Bug ID, UAT ID, ecc.)
- □ ogni modifica riconducibile a una Change Proposal o a un bug report
- □ `CHANGELOG.md` aggiornato
- □ `VERSION` aggiornato
- □ `17_VERSION_HISTORY.md` aggiornato con motivazione e documenti modificati
- □ `07_KNOWN_ISSUES.md` aggiornato (issue risolte → stato Chiuso; nuove issue note registrate)
- □ nessun documento modificato fuori dall'ambito dichiarato

---

## 6. Cosa NON giustifica mai una release

- preferenze stilistiche personali senza evidenza di problemi reali
- riscritture "per pulizia" di documenti che funzionano
- funzionalità speculative ("potrebbe servire")
- modifiche richieste da un singolo caso mai riprodotto

Questi casi vanno in `11_ROADMAP.md` sezione BACKLOG o RIFIUTATO, con motivazione.
