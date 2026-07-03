# 02 — Workflow Operativo

**OperatorGuide · Mini4WD Manual SDK v2.5.0**

> Versione compatta del workflow. State machine completa: `../WORKFLOW.md`.

---

## Le fasi e le chat

| # | Fase | Chi | Chat | Prompt (Docs/AI_BOOTSTRAP_PROMPT.md) |
|---|---|---|---|---|
| 0 | Setup progetto | Tu | nessuna | — |
| 1 | Bootstrap | Tu + AI | **Chat #1 (nuova)** | Fase 1 |
| 2 | Generazione testi (per pagina) | AI | Chat #1 | Fase 2 |
| 3 | QA testi (per pagina) | AI | Chat #1 | Fase 3 |
| 3b | Seal (`locked`) | AI su tua conferma | Chat #1 | — |
| 4 | Rendering (per pagina) | AI | **Chat #2 (nuova)** | Fase 4 |
| 4b | QA rendering | Tu + AI | Chat #2 | in Fase 4 |
| 5 | PDF | Tu + AI | **Chat #3 (nuova)** | Fase 5 |
| 6 | Pubblicazione | Maintainer | — | — |

## Quando aprire una nuova chat

**Regola:** nuova chat quando cambia il *motore* (testi → render → PDF), stessa chat
quando cambi solo pagina.

- Bootstrap + tutti i testi + tutti i QA testi → **una sola chat**.
- Tutti i rendering → **una seconda chat**.
- PDF → **una terza chat**.
- Chat degenerata (risposte incoerenti, contesto perso, troppo lunga) → nuova chat con
  il **Prompt F — Continuità** e ripresa da dove eri.

## Il loop per singola pagina (fase testi)

```
 ┌──────────────────────────────────────────────┐
 │  Allega PromptEngine/{pagina}.md             │
 │  Prompt Fase 2 → content.yaml                │
 │        │                                     │
 │        ▼                                     │
 │  Prompt Fase 3 → QA                          │
 │        │                                     │
 │   REJECTED ──► applica correzioni ──┐        │
 │        │                            │        │
 │        │◄───────────────────────────┘        │
 │        ▼                                     │
 │   APPROVED → seal (locked) → pagina dopo     │
 └──────────────────────────────────────────────┘
```

## Cosa produce ogni fase (input → output)

| Fase | Input | Output |
|---|---|---|
| Setup | Template + dati modello | `PROJECT.yaml` + foto in `Images/` |
| Bootstrap | Framework + PROJECT.yaml + foto | Bootstrap Report approvato |
| Testi | PromptEngine/{pagina}.md | `Projects/{Modello}/{Variante}/ApprovedText/P00x/content.yaml` |
| QA testi | content.yaml + Tests/ | Verdetto APPROVED/REJECTED |
| Seal | content.yaml approvato | `metadata.yaml → locked` |
| Rendering | content.yaml locked + foto + design | Immagine pagina |
| QA render | render + QA_SYSTEM.md | PASS/FAIL in qa_log.md |
| PDF | pagine rendered + PDF_CONFIG | 3 PDF + checksum |

## Segnali che stai sbagliando fase

- L'AI ti propone un'illustrazione mentre stai generando testi → riportala in Text Mode
  («Siamo in Fase 2: solo content.yaml, nessuna immagine»).
- L'AI riscrive il testo durante il rendering → violazione: il testo locked non si
  tocca. Rilancia il prompt Fase 4.
- Stai per editare un file in `ApprovedAssets/` a mano → fermati: si fa via prompt.
- Stai per validare P001 senza averla generata → prima Fase 2, poi Fase 3.
