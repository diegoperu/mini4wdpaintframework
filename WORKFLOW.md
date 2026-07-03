# WORKFLOW.md — State Machine Operativa

**Mini4WD Manual SDK v2.5.0** · Documento operatore
**Prerequisito:** `START_HERE.md`

> Questo documento descrive il ciclo di vita di un manuale come macchina a stati.
> Per ogni stato: obiettivo, input, output, prossimo stato.
> È la mappa di riferimento: se non sai "a che punto sono?", la risposta è qui.
>
> Nota: `Core/WORKFLOW.md` è la specifica tecnica interna del framework.
> Questo file è la versione operativa per chi usa l'SDK.

---

## La State Machine

```
┌─────────────────┐
│  SCELTA RUNTIME │  Operatore: ChatGPT Web o Claude Code?
└────────┬────────┘
         ▼
┌─────────────────┐
│ NUOVO PROGETTO  │  Operatore: cartella + PROJECT.yaml + immagini
└────────┬────────┘
         ▼
┌─────────────────┐
│   BOOTSTRAP     │  AI: carica il framework, produce il Bootstrap Report
└────────┬────────┘
         ▼
┌─────────────────┐
│  BOOTSTRAP OK   │  Operatore: approva il report
└────────┬────────┘
         ▼
┌─────────────────┐
│ GENERAZIONE     │  AI: genera content.yaml per una pagina (P001, poi P002…)
│ TESTI           │
└────────┬────────┘
         ▼
┌─────────────────┐
│   QA TESTI      │  AI: ContentValidation + TextValidation
└────────┬────────┘
         │ FAIL → torna a GENERAZIONE TESTI (correggi, rigenera)
         ▼ PASS
┌─────────────────┐
│ APPROVED TEXT   │  metadata.yaml → status: locked
└────────┬────────┘
         │ (ripeti Testi→QA→Approved per tutte le pagine, poi ▼)
         ▼
┌─────────────────┐
│   RENDERING     │  AI (nuova chat): genera la pagina illustrata da content.yaml
└────────┬────────┘
         ▼
┌─────────────────┐
│  QA RENDERING   │  Checklist Core/QA_SYSTEM.md
└────────┬────────┘
         │ FAIL → torna a RENDERING
         ▼ PASS
┌─────────────────┐
│ APPROVED IMAGES │  metadata.yaml → status: rendered
└────────┬────────┘
         ▼
┌─────────────────┐
│      PDF        │  AI (nuova chat): assembla le 10 pagine, 3 varianti
└────────┬────────┘
         ▼
┌─────────────────┐
│ GOLDEN PROJECT  │  Manuale in Assets/ApprovedManual/ — status: released
└─────────────────┘
```

---

## Dettaglio degli stati

### 0. SCELTA RUNTIME
- **Obiettivo:** scegliere l'ambiente di esecuzione prima di iniziare.
- **Chi:** Operatore.
- **Input:** nessuno — è una scelta dell'Operatore.
- **Output:** runtime scelto (ChatGPT Web o Claude Code).
- **Prossimo stato:** NUOVO PROGETTO.
- **Guida:** `Docs/RUNTIMES.md`, `OperatorGuide/Runtimes/`

### 1. NUOVO PROGETTO
- **Obiettivo:** preparare tutti i dati prima di coinvolgere l'AI.
- **Chi:** Operatore (nessuna chat AI).
- **Input:** nome ufficiale Tamiya, codici vernici, foto del modello.
- **Output:** `Projects/{Modello}/` con `PROJECT.yaml` compilato e foto in `Images/`.
- **Prossimo stato:** BOOTSTRAP.
- **Guida:** `FIRST_PROJECT.md`

### 2. BOOTSTRAP
- **Obiettivo:** l'AI carica il framework e verifica il progetto.
- **Chi:** Operatore + AI (chat nuova).
- **Input:** dipende dal runtime — vedi `Docs/AI_BOOTSTRAP_PROMPT.md §FASE 1`.
  - *ChatGPT Web:* `Mini4WDFramework.zip` + PROJECT.yaml + immagini (allegati)
  - *Claude Code:* file del repository (accesso diretto) + PROJECT.yaml + immagini
- **Output:** Bootstrap Report (formato in `AI_ENTRYPOINT.md`).
- **Prossimo stato:** BOOTSTRAP OK (dopo la tua approvazione esplicita).
- **Nuova chat:** SÌ — è l'inizio della sessione.

### 3. BOOTSTRAP OK
- **Obiettivo:** confermare che l'AI ha capito progetto e regole.
- **Chi:** Operatore.
- **Input:** Bootstrap Report.
- **Output:** tua approvazione in chat («Approvato, inizia da P001»).
- **Prossimo stato:** GENERAZIONE TESTI.
- **Se il report segnala problemi:** correggi PROJECT.yaml o le immagini, rilancia il bootstrap.

### 4. GENERAZIONE TESTI
- **Obiettivo:** produrre `content.yaml` per una pagina alla volta (P001 → P010).
- **Chi:** AI (Prompt Fase 2).
- **Input:** PROJECT.yaml (già in sessione) + `PromptEngine/{pagina}.md`.
- **Output:** `Projects/{Modello}/{Variante}/ApprovedText/P00x/content.yaml` — tutto in italiano, `TODO:` per i dati mancanti.
- **Prossimo stato:** QA TESTI.
- **Nuova chat:** NO — stessa chat del bootstrap.

### 5. QA TESTI
- **Obiettivo:** validare il content.yaml appena generato.
- **Chi:** AI (Prompt Fase 3).
- **Input:** `Tests/ContentValidation.md` + `Tests/TextValidation.md` + il content.yaml.
- **Output:** verdetto APPROVED / REJECTED con lista correzioni.
- **Prossimo stato:** APPROVED TEXT se PASS; GENERAZIONE TESTI se FAIL.
- **Nuova chat:** NO.
- **Importante:** il QA valuta solo contenuto generato (status `draft`/`review`). I template
  con campi vuoti NON sono contenuto finale — vedi `Tests/ContentValidation.md §Validation Scope`.

### 6. APPROVED TEXT
- **Obiettivo:** sigillare la pagina.
- **Chi:** AI (su tua conferma).
- **Input:** content.yaml validato.
- **Output:** `metadata.yaml → status: locked` + riga in `changelog.md`.
- **Prossimo stato:** pagina successiva (torna a 4) — oppure RENDERING quando tutte le pagine sono locked.

### 7. RENDERING
- **Obiettivo:** generare la pagina illustrata.
- **Chi:** AI (Prompt Fase 4).
- **Input:** content.yaml locked + immagini di riferimento + specifiche di design.
- **Output:** immagine pagina in `Projects/{Modello}/{Variante}/ApprovedImages/P00x/`.
- **Prossimo stato:** QA RENDERING.
- **Nuova chat:** **SÌ** — il rendering usa un contesto diverso (design, non testi).
- **Guida:** `FIRST_RENDER.md`

### 8. QA RENDERING
- **Obiettivo:** verificare la pagina illustrata.
- **Chi:** Operatore + AI.
- **Input:** render + `Core/QA_SYSTEM.md` (checklist 110 voci).
- **Output:** esito PASS/FAIL nel `Notes/qa_log.md` del progetto.
- **Prossimo stato:** APPROVED IMAGES se PASS; RENDERING se FAIL.

### 9. APPROVED IMAGES
- **Obiettivo:** registrare le pagine approvate.
- **Chi:** Operatore (o AI su conferma).
- **Output:** `metadata.yaml → status: rendered` per ogni pagina.
- **Prossimo stato:** PDF quando tutte le pagine sono rendered.

### 10. PDF
- **Obiettivo:** assemblare il manuale.
- **Chi:** Operatore + AI (Prompt Fase 5).
- **Input:** 10 pagine rendered + `Templates/PDF_CONFIG.yaml` + `Core/PDF_MASTER.md`.
- **Output:** 3 PDF (screen / print / archive) in `Projects/{Modello}/Output/pdf/`.
- **Prossimo stato:** GOLDEN PROJECT.
- **Nuova chat:** SÌ.
- **Guida:** `FIRST_PDF.md`

### 11. GOLDEN PROJECT
- **Obiettivo:** pubblicare.
- **Chi:** Maintainer (approvazione finale — non self-service).
- **Output:** manuale in `Assets/ApprovedManual/{Modello}/`, pagine `released`,
  `Projects/{Modello}/{Variante}/index.yaml` aggiornato.
- **Stato finale.** Il progetto diventa riferimento per i futuri manuali.

---

## Regole trasversali

1. **Una pagina alla volta.** Mai chiedere all'AI di generare tutte le 10 pagine insieme.
2. **QA è bloccante.** Nessun rendering prima del PASS sui testi.
3. **Mai saltare stati.** Ogni output è l'input dello stato successivo.
4. **In caso di FAIL** si torna sempre allo stato precedente, mai avanti.
5. **Chat lunga o confusa?** Nuova chat con il Prompt di Continuità (Prompt F).

Ciclo di vita per singola pagina: `LIFECYCLE.md`
Chi modifica cosa: `WHO_MODIFIES_WHAT.md`
