# Operator Feedback

**Mini4WD Manual SDK** · Quality Management System · Documento 16

| Campo | Valore |
|-------|--------|
| Scopo | Definire quando, come e con quali template raccogliere il feedback degli operatori, e chi lo analizza |
| Destinatario | Operatore, Reviewer, Maintainer |
| Source of Truth | Questo documento |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## 1. Perché

Il framework evolve SOLO sulla base di dati raccolti durante l'utilizzo reale (DEC-001). Gli operatori sono la fonte primaria di questi dati: senza i loro report, il QMS è vuoto e nessuna release è giustificabile. UAT-001 è l'esempio fondativo: un solo test con operatore esterno ha prodotto 8 correzioni per v2.4.1.

---

## 2. Quando raccogliere il feedback

| Momento | Cosa compilare | Obbligatorio |
|---------|----------------|:------------:|
| Durante il lavoro, appena si incontra un errore riproducibile | Bug Report (`05`) | Sì |
| Al termine di ogni sessione significativa | User Report (`03`) | Sì |
| Dopo un manuale COMPLETATO (PDF prodotto) | Retrospettiva (`14`) + User Report finale | Sì |
| Dopo un manuale NON completato / abbandonato | Post-Mortem (`13`) | Sì |
| Su richiesta del Maintainer (test formale di scenario) | UAT (`04`) | Sì |
| In qualsiasi momento, per un'idea di miglioramento | Feature Request (`06`) | No |

Regola pratica: **il feedback si scrive a caldo**. Un report compilato una settimana dopo perde i dettagli che servono (prompt esatti, messaggi di errore, ordine dei tentativi).

---

## 3. Come

1. Copia il template indicato dalla tabella §2.
2. Salva il file compilato nella sottocartella corrispondente:
   - `Reports/UR-{NNN}.md` — User Report
   - `Bugs/BUG-{NNN}.md` — Bug Report
   - `Features/FR-{NNN}.md` — Feature Request
   - `PostMortems/PM-{NNN}.md` — Post-Mortem
   - `Retrospectives/RETRO-{NNN}.md` — Retrospettiva
   - `UAT/UAT-{NNN}.md` (root del repository) — UAT (DEC-003)
3. Numerazione progressiva a tre cifre per tipo (UR-001, BUG-001, …). Controlla l'ultimo numero usato nella cartella.
4. Allega gli screenshot nella stessa sottocartella (`{ID}_screenshot_{n}.png`) e referenziali dal report.
5. Consegna: commit nel repository (branch o PR se il flusso GitHub è attivo, vedi `Documentation/OperationalManual/16_GitHubWorkflow.md`).

L'operatore NON deve: correggere da sé i documenti del framework, aprire Change Proposal per conto proprio senza dati, o modificare i registri (`07`, `09`, `10`, `11`, `17`) — quelli li aggiorna il Maintainer.

---

## 4. Chi analizza il feedback

| Ruolo | Responsabilità |
|-------|----------------|
| **Operatore** | Compila i template a caldo; apre bug con passi riproducibili |
| **Reviewer** | Prima lettura: verifica completezza del report, chiede chiarimenti, deduplica |
| **Maintainer** | Conferma i bug (li riproduce o ne verifica la causa), aggiorna i registri (`07_KNOWN_ISSUES`, `09_TEST_HISTORY`, `12_METRICS`), decide se le soglie dei Release Criteria sono raggiunte, scrive le Change Proposal |

Cadenza di analisi: il Maintainer rivede il feedback accumulato **a ogni chiusura di manuale** e comunque **prima di ogni release**. Nessun report deve restare senza esito: ogni segnalazione finisce confermata, rifiutata (con motivo) o in Known Issues.
