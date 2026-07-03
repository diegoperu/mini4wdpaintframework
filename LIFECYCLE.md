# LIFECYCLE.md — Ciclo di Vita di un Manuale

**Mini4WD Manual SDK v2.5.0** · Documento operatore

> Due cicli di vita convivono nell'SDK: quello del **manuale** (macro) e quello di
> **ogni singola pagina** (micro, tracciato in `metadata.yaml`). Questo documento li
> descrive entrambi. La state machine operativa completa è in `WORKFLOW.md`.

---

## Ciclo di vita del manuale (macro)

```
NUOVO
  │   Operatore crea Projects/{Modello}/ + PROJECT.yaml + Images/
  ▼
BOOTSTRAP
  │   AI carica il framework → Bootstrap Report → approvazione operatore
  ▼
TEXT
  │   AI genera content.yaml pagina per pagina (P001 → P010)
  │   QA testi bloccante su ogni pagina
  ▼
APPROVED
  │   Tutte le pagine locked (testo sigillato, changelog aggiornato)
  ▼
RENDER
  │   Nuova chat — AI genera le pagine illustrate dai content.yaml locked
  ▼
QA
  │   Checklist Core/QA_SYSTEM.md su ogni render — FAIL → si ri-renderizza
  ▼
PDF
  │   Nuova chat — assemblaggio 3 varianti (screen / print / archive)
  ▼
GOLDEN PROJECT
      Maintainer pubblica in Assets/ApprovedManual/ — il progetto diventa riferimento
```

| Stato | Output che chiude lo stato | Responsabile |
|---|---|---|
| NUOVO | PROJECT.yaml completo + foto in Images/ | Operatore |
| BOOTSTRAP | Bootstrap Report approvato | Operatore + AI |
| TEXT | content.yaml validati per tutte le pagine | AI |
| APPROVED | metadata.yaml → `locked` per tutte le pagine | Reviewer/Operatore |
| RENDER | Immagini pagina in ApprovedAssets/Images/ | AI |
| QA | qa_log.md senza FAIL | Operatore/Reviewer |
| PDF | 3 PDF validati e checksummati | Operatore |
| GOLDEN PROJECT | Manuale in Assets/ApprovedManual/, pagine `released` | Maintainer |

---

## Ciclo di vita della singola pagina (micro)

Tracciato in `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml → status`:

```
draft → review → approved → locked → rendered → released → archived
```

| Status | Significato | Chi può portarla qui |
|---|---|---|
| `draft` | Template o contenuto in lavorazione. **Non validabile come contenuto finale.** | Stato iniziale |
| `review` | content.yaml generato, in attesa di QA | AI |
| `approved` | QA testi PASS | Reviewer |
| `locked` | Sigillata: il testo non si tocca più senza changelog | Reviewer |
| `rendered` | Pagina illustrata generata e QA visuale PASS | AI + Reviewer |
| `released` | Nel manuale pubblicato | Maintainer |
| `archived` | Storicizzata | Maintainer |

Regole:

1. **Mai saltare stati.** `draft → locked` diretto non esiste.
2. **`locked` è un sigillo.** Riaprire una pagina locked richiede una riga in
   `changelog.md` e il ritorno a `review`.
3. **Il Render Engine parte solo da `locked`.**
4. **`draft` non è un errore.** I moduli P001–P010 dell'SDK nascono `draft` con campi
   vuoti: sono template in attesa del tuo progetto, non contenuto difettoso
   (vedi `Tests/ContentValidation.md §Validation Scope`).

---

## Dove si vede lo stato

| Cosa | Dove |
|---|---|
| Stato di ogni pagina | `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml → status` |
| Registro globale | `Projects/{Modello}/{Variante}/index.yaml` |
| Stato QA del progetto | `Projects/{Modello}/PROJECT.yaml → qa.status` + `Notes/qa_log.md` |
| Storia delle revisioni | `Projects/{Modello}/{Variante}/ApprovedText/P00x/changelog.md` |
