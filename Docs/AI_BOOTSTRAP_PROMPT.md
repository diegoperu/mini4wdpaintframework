# AI_BOOTSTRAP_PROMPT.md
# Mini4WD Manual SDK — Official AI Bootstrap Prompts

**Version:** 2.4.0

> This document contains ready-to-use prompts for starting a Mini4WD manual
> generation session with ChatGPT, Claude, Gemini, or any AI model.
> Copy the relevant prompt and attach or paste the listed files.
> Updated at every release.

---

## Prompt A — Full Session Bootstrap (Recommended)

Use this prompt when starting a full manual generation session from scratch.
Attach or paste the listed files in order.

**Files to attach (in order):**
1. `SDK_CONTEXT.yaml`
2. `BOOTSTRAP.md`
3. `Core/AI_OPERATING_RULES.md`
4. `Config/LANGUAGE_POLICY.yaml`
5. `Core/TEXT_ENGINE.md`
6. `Core/DESIGN_LANGUAGE.md`
7. `Core/STYLE_GUIDE.md`
8. `Core/COMPONENT_SYSTEM.md`
9. `Core/PAGE_SYSTEM.md`
10. `Projects/{ModelName}/PROJECT.yaml`
11. Reference images of the model (photos of the physical Mini4WD)

**Prompt:**

```
Stai operando come motore editoriale del Mini4WD Manual SDK v2.4.0.

Ho allegato i documenti del framework nell'ordine corretto di caricamento.
Leggi tutti i documenti allegati prima di procedere.

Regole fondamentali:
- Tutto il testo editoriale deve essere in italiano.
- content.yaml è la source of truth per ogni pagina.
- Non inventare dati. Se un valore non è in PROJECT.yaml, usa TODO: come placeholder.
- Non modificare la forma fisica del modello nei render.
- Segui le istruzioni di Core/AI_OPERATING_RULES.md per ogni operazione.

Conferma di aver letto tutti i documenti allegati, poi attendi le istruzioni
per la prima pagina da generare.
```

---

## Prompt B — Single Page Generation

Use this prompt when generating a specific page. Assumes the AI has already
loaded the full framework context (Prompt A or equivalent).

**Additional files to attach:**
- `PromptEngine/{page}.md` (e.g., `PromptEngine/Cover.md` for P001)
- `ApprovedAssets/Text/P00x/` directory (if the page has existing sealed content)

**Prompt:**

```
Genera la pagina {PAGINA} ({NOME_PAGINA}) del manuale per il modello {NOME_MODELLO}.

Fase 2a — Text Engine:
1. Leggi il file PromptEngine/{page}.md allegato.
2. Estrai tutti i valori dal PROJECT.yaml caricato in precedenza.
3. Genera il file content.yaml completo per questa pagina.
4. Usa TODO: per qualsiasi valore non disponibile in PROJECT.yaml.
5. Tutto il testo deve essere in italiano.

Non procedere alla fase di rendering fino a che non hai ricevuto
la conferma che il content.yaml è approvato.

Output atteso: content.yaml completo e pronto per la validazione QA.
```

---

## Prompt C — QA Validation

Use this prompt to run QA on a generated content.yaml.

**Files to attach:**
- `Tests/ContentValidation.md`
- `Tests/TextValidation.md`
- The `content.yaml` to validate

**Prompt:**

```
Esegui la validazione QA completa sul content.yaml allegato.

Fase 2b — Content Validation:
Applica tutte e 7 le suite di validazione definite in Tests/ContentValidation.md.
Riporta ogni test: PASS / FAIL / WARNING.
Elenca tutti i FAIL con la riga specifica del content.yaml e la correzione necessaria.

Fase 2c — Text Validation:
Applica tutti e 9 i test di conformità italiana definiti in Tests/TextValidation.md.
Riporta ogni test: PASS / FAIL.
Zero tolleranza per testo in giapponese, inglese nel corpo, o Lorem ipsum.

Output atteso:
- Riepilogo per suite (PASS/FAIL)
- Lista dettagliata di tutti i FAIL con correzioni
- Verdetto finale: APPROVED / REJECTED
- Se REJECTED: lista completa delle correzioni richieste prima del rendering.
```

---

## Prompt D — Render Engine

Use this prompt to generate the illustrated page from a locked content.yaml.
Only use after QA approval.

**Files to attach:**
- `Core/RENDER_GUIDE.md`
- `Core/DESIGN_LANGUAGE.md`
- `Core/STYLE_GUIDE.md`
- `Core/COMPONENT_SYSTEM.md`
- `Assets/DesignSystem/Tokens/tokens.example.yaml`
- The locked `content.yaml` for this page
- Reference images of the model

**Prompt:**

```
Genera l'illustrazione per la pagina {PAGINA} ({NOME_PAGINA}).

Il content.yaml allegato è approvato e bloccato (status: locked).

Regole operative del Render Engine:
- Leggi esclusivamente da content.yaml. Non generare testo non presente in content.yaml.
- Usa solo i valori dei Design Token di tokens.example.yaml. Nessun valore hardcoded.
- La forma fisica del modello deve corrispondere esattamente alle immagini di riferimento.
- Applica tutte le regole di Core/DESIGN_LANGUAGE.md e Core/STYLE_GUIDE.md.
- Posiziona i componenti secondo le specifiche di Core/COMPONENT_SYSTEM.md.
- Lo sfondo è bianco puro. Il pannello header è viola (token.PrimaryViolet).

Output atteso: pagina illustrata completa, pronta per la validazione visiva.
```

---

## Prompt E — Minimal Bootstrap (ZIP or Limited Context)

Use this prompt when the AI receives only the SDK ZIP and must self-orient.

**Files to attach:**
- SDK ZIP (or the full repository)

**Prompt:**

```
Hai ricevuto il Mini4WD Manual SDK v2.4.0.

Leggi i file nell'ordine seguente prima di fare qualsiasi altra cosa:
1. SDK_CONTEXT.yaml
2. BOOTSTRAP.md
3. Core/AI_OPERATING_RULES.md
4. Config/LANGUAGE_POLICY.yaml
5. Core/TEXT_ENGINE.md
6. Core/DESIGN_LANGUAGE.md
7. Core/STYLE_GUIDE.md
8. Core/COMPONENT_SYSTEM.md
9. Core/PAGE_SYSTEM.md

Dopo aver letto tutti questi documenti, conferma:
- La versione dell'SDK che stai utilizzando
- Le 10 regole non negoziabili del BOOTSTRAP.md
- La struttura del content.yaml richiesta dal TEXT_ENGINE.md
- Il nome della lingua obbligatoria per tutto il testo editoriale

Poi attendi il PROJECT.yaml e le immagini di riferimento del modello.
```

---

## Prompt F — Session Continuity

Use this prompt when resuming a session that already loaded the framework.

**Prompt:**

```
Stiamo continuando la sessione di generazione del manuale Mini4WD SDK v2.4.0
per il modello {NOME_MODELLO}.

Stato attuale:
- Pagine completate: {LISTA_PAGINE_COMPLETATE}
- Pagina corrente: {PAGINA_CORRENTE}
- Pagine rimanenti: {LISTA_PAGINE_RIMANENTI}

Tutte le regole del framework rimangono attive:
- Tutto il testo in italiano
- content.yaml come source of truth
- Pipeline: Text Engine → QA → Render → PDF

Continua dalla pagina {PAGINA_CORRENTE}.
```

---

## Notes for All Prompts

- Replace `{NOME_MODELLO}` with the actual model name (e.g., "Proto Emperor")
- Replace `{PAGINA}` with the page ID (e.g., "P001")
- Replace `{NOME_PAGINA}` with the Italian page name (e.g., "Copertina")
- All prompts assume Italian output — do not translate to other languages
- If the AI model has a token limit, use Prompt E (minimal) and load documents incrementally
- For the most reliable results, attach documents as files rather than pasting content

---

## Compatibility

| Model | Tested | Notes |
|-------|--------|-------|
| ChatGPT (GPT-4o, GPT-4) | ✓ | Attach files via file upload |
| Claude (Sonnet, Opus) | ✓ | Paste content or attach files |
| Gemini (1.5 Pro, Ultra) | ✓ | Attach files via Google Drive or paste |
| Future models | Expected ✓ | Prompts use no model-specific syntax |

---

## Cross References

- `BOOTSTRAP.md` → full framework rules and pipeline
- `SDK_CONTEXT.yaml` → machine-readable SDK state
- `Docs/LOAD_ORDER.md` → detailed loading order with rationale
- `Core/AI_OPERATING_RULES.md` → 100 behavioral rules
- `Build/Pipeline.md` → full 8-phase pipeline
