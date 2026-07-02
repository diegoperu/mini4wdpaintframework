# Quality Management System — Index

**Mini4WD Manual SDK** · Quality Management System · Documento 20

| Campo | Valore |
|-------|--------|
| Scopo | Indice navigabile dell'intero sistema Quality Management |
| Destinatario | Tutti |
| Source of Truth | `19_QMS_README.md` per l'organizzazione; questo documento è solo navigazione |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Documenti normativi (regole)

| # | Documento | Contenuto |
|---|-----------|-----------|
| 01 | [Release Policy](01_RELEASE_POLICY.md) | Cosa può entrare in Patch / Minor / Major, con esempi |
| 02 | [Release Criteria](02_RELEASE_CRITERIA.md) | Soglie oggettive che autorizzano una release; checklist di rilascio |
| 18 | [Documentation Policy](18_DOCUMENTATION_POLICY.md) | Intestazione obbligatoria (Scopo/Destinatario/Source of Truth/Versione) e regole di coerenza |

## Template (da copiare e compilare)

| # | Documento | Quando si usa | Destinazione |
|---|-----------|---------------|--------------|
| 03 | [User Report Template](03_USER_REPORT_TEMPLATE.md) | Fine di ogni sessione significativa | `Reports/UR-NNN.md` |
| 04 | [UAT Template](04_UAT_TEMPLATE.md) | Test formale di scenario | `UAT/UAT-NNN.md` (root) |
| 05 | [Bug Report Template](05_BUG_REPORT_TEMPLATE.md) | Errore riproducibile | `Bugs/BUG-NNN.md` |
| 06 | [Feature Request Template](06_FEATURE_REQUEST_TEMPLATE.md) | Idea di nuova funzionalità | `Features/FR-NNN.md` |
| 13 | [Post-Mortem Template](13_POST_MORTEM_TEMPLATE.md) | Manuale NON completato | `PostMortems/PM-NNN.md` |
| 14 | [Retrospective Template](14_RETROSPECTIVE_TEMPLATE.md) | Manuale completato | `Retrospectives/RETRO-NNN.md` |
| 15 | [Change Proposal Template](15_CHANGE_PROPOSAL_TEMPLATE.md) | Qualsiasi modifica al framework | `Changes/CP-NNN.md` |

## Registri (aggiornati dal Maintainer)

| # | Documento | Contenuto |
|---|-----------|-----------|
| 07 | [Known Issues](07_KNOWN_ISSUES.md) | Problemi noti aperti + archivio risolti, con workaround |
| 08 | [Decision Log](08_DECISION_LOG.md) | Decisioni architetturali e di processo (DEC-NNN) |
| 09 | [Test History](09_TEST_HISTORY.md) | Cronologia di tutti i test eseguiti |
| 10 | [Golden Projects](10_GOLDEN_PROJECTS.md) | Manuali certificati per versione SDK |
| 11 | [Roadmap QMS](11_ROADMAP.md) | Proposte per stato: BACKLOG → … → COMPLETATO / RIFIUTATO |
| 12 | [Metrics](12_METRICS.md) | Definizioni delle metriche M01–M12 e rilevazioni per versione |
| 17 | [Version History](17_VERSION_HISTORY.md) | Storico versioni: motivazione, ambito, compatibilità |

## Processo e organizzazione

| # | Documento | Contenuto |
|---|-----------|-----------|
| 16 | [Operator Feedback](16_OPERATOR_FEEDBACK.md) | Quando, come e con quali template raccogliere feedback; chi lo analizza |
| 19 | [QMS README](19_QMS_README.md) | Perché il QMS esiste, come si usa, responsabilità |
| 20 | Index | Questo documento |

## Riferimenti esterni al QMS

| Documento | Ruolo |
|-----------|-------|
| `CHANGELOG.md` (root) | Dettaglio delle modifiche per versione (Keep a Changelog) |
| `ROADMAP.md` (root) | Visione di lungo periodo del progetto |
| `UAT/` (root) | UAT compilati (UAT-001 già presente) |
| `STATUS.md` (root) | Stato di implementazione del framework |
| `Core/DOCUMENTATION_STYLE.md` | Stile di scrittura della documentazione SDK |
| `OPERATOR_PROFILE.md` (root) | Definizione dei ruoli (Operatore, Reviewer, Maintainer, Developer) |
| `Documentation/OperationalManual/` | Manuale operativo del framework (20 capitoli) |
