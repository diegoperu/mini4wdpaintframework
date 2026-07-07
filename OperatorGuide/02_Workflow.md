# 02 — Workflow Operativo

**OperatorGuide · Mini4WD Manual SDK v2.5.5**

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
| 4a | Rendering testo/layout (tutte le pagine) | `Scripts/render_page.py` | **nessuna, script locale** | — |
| 4b | Illustrazione mancante (per slot) | AI | **chat nuova per ciascuna** | Fase 4 → 4b |
| 4c | Verifica aggancio | Tu | nessuna, script locale | — |
| 5 | PDF (anteprima) | `Scripts/render_page.py ... pdf` | nessuna, script locale | — |
| 5b | PDF (export di produzione) | Tu + AI | **Chat nuova** | Fase 5 |
| 6 | Pubblicazione | Maintainer | — | — |

## Quando aprire una nuova chat

**Regola:** nuova chat quando cambia il *motore* (testi → illustrazione → PDF di
produzione), **e una chat nuova per ogni singola illustrazione** in Fase 4b — non
si riusa la stessa chat per due immagini diverse (contaminazione di contesto
verificata empiricamente: il risultato di un'immagine influenza quella successiva
nella stessa chat).

- Bootstrap + tutti i testi + tutti i QA testi → **una sola chat**.
- Fase 4a (template) → **nessuna chat, un comando da terminale**.
- Ogni illustrazione mancante (Fase 4b) → **una chat a sé**, quante sono gli slot
  in `MISSING_IMAGES.md`.
- PDF di produzione (Fase 5b) → **una chat**.
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

## Il loop per illustrazione mancante (Fase 4)

```
 ┌──────────────────────────────────────────────────┐
 │  Scripts/render_page.py {Model} {Variant}        │
 │  → MISSING_IMAGES.md / _PROMPT.md / .json        │
 │        │                                          │
 │        ▼                                          │
 │  Per ogni slot: chat nuova, copia il blocco       │
 │  prompt gia' pronto da MISSING_IMAGES_PROMPT.md   │
 │        │                                          │
 │        ▼                                          │
 │  Salva l'immagine al path indicato                │
 │        │                                          │
 │        ▼                                          │
 │  Rilancia render_page.py → slot sparito?          │
 │   NO ──► correggi/rigenera solo quello slot ──┐   │
 │        │                                      │   │
 │        │◄─────────────────────────────────────┘   │
 │   SÌ → prossimo slot, finche' il report e' vuoto  │
 └──────────────────────────────────────────────────┘
```

## Cosa produce ogni fase (input → output)

| Fase | Input | Output |
|---|---|---|
| Setup | Template + dati modello | `PROJECT.yaml` + foto in `Images/` |
| Bootstrap | Framework + PROJECT.yaml + foto | Bootstrap Report approvato |
| Testi | PromptEngine/{pagina}.md | `Projects/{Modello}/{Variante}/ApprovedText/P00x/content.yaml` |
| QA testi | content.yaml + Tests/ | Verdetto APPROVED/REJECTED |
| Seal | content.yaml approvato | `metadata.yaml → locked` |
| Rendering (4a) | content.yaml locked (tutte le pagine) | PNG/PDF per pagina + `MISSING_IMAGES.*` |
| Illustrazione (4b) | Foto reference + schema colori + prompt slot | 1 file immagine, path esatto |
| PDF anteprima | Pagine renderizzate | 1 PDF unico (via `pdfunite`) |
| PDF produzione (5b) | pagine rendered + PDF_CONFIG | 3 PDF + checksum |

## Segnali che stai sbagliando fase

- L'AI ti propone un'illustrazione mentre stai generando testi → riportala in Text Mode
  («Siamo in Fase 2: solo content.yaml, nessuna immagine»).
- L'AI genera testo/tabelle durante la Fase 4b → non dovrebbe succedere (il prompt
  chiede solo l'illustrazione isolata): scarta l'output, rigenera in chat nuova.
- Stai per editare un file in `ApprovedText/` a mano, o cerchi `ApprovedImages/`
  (non esiste più — le illustrazioni vanno in `Images/`) → fermati: il testo si
  genera via prompt, le illustrazioni via `Scripts/render_page.py` + chat Fase 4b.
- Stai per validare P001 senza averla generata → prima Fase 2, poi Fase 3.
