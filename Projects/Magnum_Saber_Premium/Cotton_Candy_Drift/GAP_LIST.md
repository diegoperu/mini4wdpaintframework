# GAP_LIST.md — Magnum Saber Premium / Cotton Candy Drift → Golden Project

**Data:** 2026-07-09
**Scopo:** elenco di quanto manca per portare questo progetto allo stato di Golden
Project certificato, per il team di analisi/QA. Verificato contro
`Documentation/QualityManagement/10_GOLDEN_PROJECTS.md` e
`Documentation/QualityManagement/01_RELEASE_CRITERIA.md §4`.

---

## Nota preliminare — collisione di nomi

`SDK_CONTEXT.yaml → golden_project` dichiarava `Projects/Proto_Emperor/` come
riferimento strutturale ufficiale per la forma di `PROJECT.yaml` (schema-shape
reference). `Projects/Proto_Emperor/` è stato rimosso dal repository (2026-07-09,
progetto vuoto/mai popolato — vedi `Documentation/OperationalManual/13_GoldenProjects.md
§4`). Questo lascia quel puntatore e l'intero Capitolo 13 dell'Operational Manual
senza target.

**Attenzione:** "golden_project" (`SDK_CONTEXT.yaml` — riferimento di schema, che
qualunque progetto può ricoprire) e "Golden Project" (`10_GOLDEN_PROJECTS.md` — un
manuale certificato e rilasciato) sono due concetti diversi che condividono lo stesso
nome. Decidere se Magnum Saber diventa il nuovo `golden_project` di schema è una
scelta indipendente dal certificarlo come Golden Project QMS — non vanno confusi nel
briefing al team. `SDK_CONTEXT.yaml` e il Capitolo 13 non sono ancora stati
aggiornati: repointing da decidere separatamente.

---

## Elenco dei gap

| # | Gap | Stato attuale |
|---|---|---|
| 1 | Project-level QA gate non aperto | `PROJECT.yaml → qa.status = "draft"`, `reviewer`/`reviewDate`/`approvedDate` tutti vuoti |
| 2 | Nessun QA log | `qaLogPath: "Notes/qa_log.md"` — file inesistente, `Notes/` vuota |
| 3 | Metadata per-pagina non aggiornata | Tutte le 9 pagine: `status: "locked"` (dovrebbe essere `"rendered"` — renderizzano pulite, 0 immagini mancanti), `rendered: false`, `rendered_date: ""`, `rendered_images: []` — PASSO 7 di `FIRST_RENDER.md` mai eseguito |
| 4 | Nessuna evidenza QA | Ogni pagina ha `qa_status: "passed"` ma `qa_log: ""` — nessuna registrazione di cosa abbiano effettivamente verificato `Tests/ContentValidation.md` (8 suite) / `Tests/TextValidation.md` (9 suite) |
| 5 | Nessun export PDF | `Output/` vuota, nessuna copia di `PDF_CONFIG.yaml` nel progetto, nessuna variante screen/print/archive, nessun `checksums.sha256` — `FIRST_PDF.md` mai eseguito, nemmeno l'anteprima rapida a comando singolo |
| 6 | `ApprovedImages/` vuota | Ambiguo, non necessariamente un gap reale — da confermare col team se questa cartella sia ancora rilevante o una convenzione legacy superata dalla struttura flat `Images/` (nota architetturale 2026-07-08) prima di inseguirla |
| 7 | Nessuna Retrospettiva | Istanza di `14_RETROSPECTIVE_TEMPLATE.md` — attesa solo a fine percorso, non bloccante ora, ma da pianificare |
| 8 | Nessuna approvazione/pubblicazione Maintainer | `Assets/ApprovedManual/Magnum_Saber_Premium/` non esiste ancora — ultimo passo, `FIRST_PDF.md` PASSO 6 |
| 9 | Voce di registro mancante | `10_GOLDEN_PROJECTS.md` → Registro mostra ancora solo la riga segnaposto vuota |

**Non è un gap:** `premiumVariant.enabled: false` → P009 correttamente saltato, 9
pagine (P001–P008+P010) sono l'insieme completo atteso.
