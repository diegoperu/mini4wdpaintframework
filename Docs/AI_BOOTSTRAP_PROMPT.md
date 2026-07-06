# AI_BOOTSTRAP_PROMPT.md — Prompt Ufficiali per Fase

**Mini4WD Manual SDK v2.5.0**

> Un prompt pronto per ogni fase della pipeline. Per ogni fase trovi: **Input**
> (cosa allegare), **Output** (cosa aspettarti), **Prompt** (da copiare), **Nuova
> chat SÌ/NO**. Verificato con ChatGPT (GPT-4o) e Claude (Sonnet/Opus).
> Gemini: supportato solo per Fase 4 (generazione illustrazione singola, non
> testi/bootstrap) — vedi §Compatibilità e `UAT/UAT-004.md`.
>
> La pipeline: **Bootstrap → Generazione Testi → QA → Rendering → PDF**
> Mappa completa degli stati: `WORKFLOW.md` (root).

---

## FASE 1 — Bootstrap

*(ex Prompt A)*

**Nuova chat: SÌ** — è l'inizio della sessione.

> ⚙️ **La procedura di caricamento dipende dal runtime.**
> Segui la sezione corretta per il tuo ambiente.
> Runtime non ancora scelto? → `Docs/RUNTIMES.md`

---

### FASE 1 · ChatGPT Web

**Input (carica come allegati nella nuova chat):**
1. `Mini4WDFramework.zip` — il repository scaricato da GitHub, **allegato così com'è, non estratto**
2. Il tuo `PROJECT.yaml` compilato — file separato, non dentro il ZIP
3. Le tue foto di riferimento — file separati (ChatGPT deve vederle come immagini)

⚠️ Non allegare singolarmente `SDK_CONTEXT.yaml`, `BOOTSTRAP.md`, `Core/`, ecc.:
sono già contenuti nel ZIP. Allegare duplicati genera conflitti di contesto.

**Prompt:** usa il **Prompt E — Bootstrap Minimo** nella sezione §Prompt di servizio qui sotto.

Guida completa passo-passo: `OperatorGuide/Runtimes/ChatGPT_Web.md`

---

### FASE 1 · Claude Code

**Input (file accessibili direttamente nel repository locale):**
1. `AI_ENTRYPOINT.md`
2. `SDK_CONTEXT.yaml`
3. `BOOTSTRAP.md`
4. `Core/AI_OPERATING_RULES.md`
5. `Config/LANGUAGE_POLICY.yaml`
6. `Core/TEXT_ENGINE.md`
7. `Core/DESIGN_LANGUAGE.md`
8. `Core/STYLE_GUIDE.md`
9. `Core/COMPONENT_SYSTEM.md`
10. `Core/PAGE_SYSTEM.md`
11. `Projects/{Modello}/PROJECT.yaml` ← il TUO
12. `Projects/{Modello}/Images/` ← le TUE foto

**Prompt:**

```
Stai operando come motore editoriale del Mini4WD Manual SDK v2.5.0.

Leggi i seguenti file del repository nell'ordine indicato:
1. AI_ENTRYPOINT.md
2. SDK_CONTEXT.yaml
3. BOOTSTRAP.md
4. Core/AI_OPERATING_RULES.md
5. Config/LANGUAGE_POLICY.yaml
6. Core/TEXT_ENGINE.md
7. Core/DESIGN_LANGUAGE.md
8. Core/STYLE_GUIDE.md
9. Core/COMPONENT_SYSTEM.md
10. Core/PAGE_SYSTEM.md
11. Projects/{Modello}/PROJECT.yaml
12. Projects/{Modello}/Images/ (immagini di riferimento)

Regole fondamentali:
- Tutto il testo editoriale deve essere in italiano.
- content.yaml è la source of truth per ogni pagina.
- Non inventare dati. Se un valore non è in PROJECT.yaml, usa TODO: come placeholder.
- Nomi commerciali delle vernici, codici prodotto (TS-xx, X-xx, PS-xx) e chiavi YAML
  sono language-neutral: non vanno tradotti né segnalati come violazioni.
- Non modificare la forma fisica del modello nei render.
- Segui Core/AI_OPERATING_RULES.md per ogni operazione.

Produci ora il Bootstrap Report nel formato definito da AI_ENTRYPOINT.md,
poi fermati e attendi la mia approvazione esplicita.
```

Guida completa passo-passo: `OperatorGuide/Runtimes/Claude_Code.md`

---

**Output atteso (entrambi i runtime):** Bootstrap Report (formato in `AI_ENTRYPOINT.md`)
e STOP in attesa della tua approvazione. Nessun contenuto generato prima dell'approvazione.

**Dopo l'output:** verifica il report (tuo modello, tuoi colori, pagine in `draft`) e
rispondi «Bootstrap approvato. Inizia dalla pagina P001.»

---

## FASE 2 — Generazione Testi (una pagina alla volta)

*(ex Prompt B)*

**Nuova chat: NO** — stessa chat del Bootstrap.

**Input (aggiungi agli allegati):**
- `PromptEngine/{pagina}.md` (es. `PromptEngine/Cover.md` per P001)
- `Projects/{Model}/{Variant}/ApprovedText/P00x/` solo se la pagina ha già contenuto sigillato

**Output atteso:** `content.yaml` completo per la pagina, in italiano, con `TODO:` per
i dati mancanti. Nessuna immagine, nessuna decisione di layout.

**Prompt:**

```
Fase 2 — Text Engine.
Genera la pagina {PAGINA} ({NOME_PAGINA}) del manuale per il modello {NOME_MODELLO}.

1. Leggi il file PromptEngine/{page}.md allegato.
2. Estrai tutti i valori dal PROJECT.yaml caricato in precedenza.
3. Risolvi i riferimenti per ID: se paintSequence usa colorId, cerca il colore
   corrispondente in paintScheme.colors (dove id == colorId) ed estrai paintCode,
   paintName, finish, hex. Non lasciare TODO: per valori raggiungibili tramite
   riferimento — usa TODO: solo per dati genuinamente assenti nel PROJECT.yaml.
4. Genera il file content.yaml e scrivilo in
   Projects/{Model}/{Variant}/ApprovedText/{PAGINA}/content.yaml
   dove {Model} = cartella PascalCase_Underscore del modello,
   {Variant} = cartella PascalCase_Underscore della variante (da paintScheme.slug).
5. Usa TODO: per qualsiasi valore non disponibile in PROJECT.yaml — non inventare nulla.
6. Tutto il testo editoriale in italiano; codici e nomi commerciali restano invariati.

Non procedere al rendering: siamo in Text Mode. Output atteso: solo il content.yaml,
pronto per la validazione QA.
```

---

## FASE 3 — QA (valida la pagina appena generata)

*(ex Prompt C)*

**Nuova chat: NO** — stessa chat, subito dopo la Fase 2.

**Input (aggiungi agli allegati):**
- `Tests/ContentValidation.md`
- `Tests/TextValidation.md`
- il `content.yaml` da validare (se non già in chat)

**Output atteso:** esito per suite (PASS/FAIL), lista dei FAIL con correzione,
verdetto finale APPROVED / REJECTED.

**Prompt:**

```
Fase 3 — QA. Esegui la validazione completa sul content.yaml appena generato.

Ambito: questo è CONTENUTO GENERATO (status: review), non un template. Applica
Tests/ContentValidation.md §Validation Scope.

Content Validation: applica tutte e 7 le suite di Tests/ContentValidation.md.
Text Validation: applica tutti e 9 i test di Tests/TextValidation.md.

Ricorda le eccezioni language-neutral (LANGUAGE_POLICY §exceptions): codici vernice
(TS-37, X-10, PS-1…), nomi commerciali (Chrome Silver, Gun Metal, Semi Gloss Black,
Flat Black, Primer, Topcoat, Masking Tape…), chiavi YAML e valori di schema
(finish: gloss, status: draft, Header, Footer) NON sono violazioni linguistiche.

Riporta:
- Esito per suite: PASS / FAIL / WARNING
- Ogni FAIL con riga e correzione necessaria
- Verdetto finale: APPROVED / REJECTED
- Se REJECTED: lista completa delle correzioni richieste.
```

**Dopo l'output:**
- REJECTED → fai applicare le correzioni e rilancia questa fase.
- APPROVED → conferma il seal: «Approvato. Sigilla la pagina: metadata.yaml →
  status: locked, con riga di changelog.» Poi torna alla Fase 2 per la pagina
  successiva. Quando TUTTE le pagine sono locked → Fase 4.

---

## FASE 4 — Rendering

*(ex Prompt D — riscritta 2026-07-06: layout/testo ora deterministico, l'AI genera
solo le illustrazioni mancanti)*

> ⚠️ **Cambio di meccanismo.** Fino al 2026-07-06 questa fase chiedeva a un'AI
> generativa di produrre l'intera pagina (testo, tabelle, layout, illustrazione)
> in un colpo solo. Test estesi su un progetto reale hanno mostrato che un modello
> diffusivo non può garantire fedeltà di testo/tabelle/hex dentro un'immagine
> generata — vedi `Docs/LOCAL_RENDER_NODE.md` per l'evidenza completa. Il layout e
> il testo di ogni pagina sono ora prodotti da un template deterministico
> (`Scripts/render_page.py`), che legge `content.yaml` direttamente: zero
> allucinazioni possibili su hex, nomi, aree o lingua. Il compito che resta per
> un'AI generativa (qui o su un futuro nodo locale, vedi `Docs/LOCAL_RENDER_NODE.md`)
> è molto più piccolo: produrre **solo l'illustrazione** del modellino per gli slot
> immagine ancora vuoti — nessun testo, nessuna tabella, nessuna certificazione di
> conformità pixel-esatta da dichiarare.

**Nuova chat: SÌ** — il rendering usa un contesto diverso (design, non testi).

### 4a — Genera tutte le pagine con il template (nessuna AI coinvolta)

```bash
pip install -r Scripts/requirements.txt   # una tantum
playwright install chromium                # una tantum
Scripts/render_page.py {Model} {Variant}
```

Un solo comando per l'intero progetto — gira in automatico su tutte le
`ApprovedText/P0xx` esistenti. Genera `Build/Preview/{Model}_{Variant}_{PageID}.png`
per ciascuna pagina e scrive `Projects/{Model}/{Variant}/MISSING_IMAGES.md` con
l'elenco di tutte le immagini ancora mancanti, col path esatto atteso. Se il report
è vuoto, tutte le pagine sono già complete — vai a Fase 5. Altrimenti continua con
4b per ciascuno slot elencato.

### 4b — Genera SOLO l'illustrazione mancante (una alla volta)

> ⚠️ **Il prompt non è più scritto qui a mano.** Duplicarlo in più documenti ha
> già causato una divergenza reale in passato (due copie del prompt Fase 4 che si
> sono scollegate durante un ciclo di test). Il prompt, i file da allegare e il
> path di destinazione sono generati **automaticamente** da `Scripts/render_page.py`
> (4a) dentro `Projects/{Model}/{Variant}/MISSING_IMAGES_PROMPT.md` — uno già
> pronto da copiare per ciascuno slot mancante, compilato dai dati reali del
> progetto (non placeholder da riempire a mano). Apri quel file, copia il blocco
> del prompt e l'elenco file da allegare per lo slot che ti serve.

**Output atteso:** un singolo file immagine (nessun testo, nessuna tabella, nessun
logo, nessun pannello header/footer) da salvare esattamente al path indicato in
`MISSING_IMAGES_PROMPT.md` per quello slot (es. `Images/P002_front.png`).

Dopo aver ricevuto l'immagine: salvala al path esatto, poi ripeti 4a per
confermare che il template la incorpori (lo slot non comparirà più in
`MISSING_IMAGES.md`/`MISSING_IMAGES_PROMPT.md`).

### 4c — Nodo locale (quando disponibile)

Stesso identico contratto input/output di 4b (foto reference + colors[] in,
un'immagine al path esatto out) — vedi `Docs/LOCAL_RENDER_NODE.md` § Contratto.
Nessuna differenza di procedura per l'operatore: cambia solo dove gira la
generazione.

`Projects/{Model}/{Variant}/MISSING_IMAGES.json` (generato da 4a insieme al `.md`)
è già nel formato pensato per questo: un array di entry `{page_id, slot,
output_path, prompt, reference_files}` — un batch runner futuro può iterarci sopra
direttamente senza fare parsing di markdown.

**Guida passo-passo:** `FIRST_RENDER.md`

---

## FASE 5 — PDF

**Nuova chat: SÌ.**

**Input (file da allegare):**
1. `Core/PDF_MASTER.md`
2. `Projects/{Modello}/{Variante}/PDF_CONFIG.yaml` (copia compilata di `Templates/PDF_CONFIG.yaml`)
3. le pagine renderizzate (o i percorsi in `Projects/{Modello}/{Variante}/ApprovedImages/`)

**Output atteso:** guida all'export delle 3 varianti (screen / print / archive) con
verifica di metadati, segnalibri, font e bleed.

**Prompt:**

```
Fase 5 — PDF Builder.
Tutte le pagine del manuale {NOME_MODELLO} sono in status: rendered.

1. Verifica l'ordine pagine P001–P010 (P009 solo se premium abilitato).
2. Guidami nell'export delle tre varianti secondo Core/PDF_MASTER.md e la
   PDF_CONFIG.yaml allegata:
   - screen  (sRGB, 150dpi, no bleed, PDF/A-2b)
   - print   (CMYK FOGRA39, 300dpi, bleed 3mm, PDF/X-4)
   - archive (specifiche in Config/pdf.yaml)
3. Al termine, esegui la checklist QA-096–QA-100: metadati, segnalibri,
   font incorporati, bleed corretto per variante.
```

**Guida passo-passo:** `FIRST_PDF.md`

---

## Prompt di servizio

### Prompt E — Bootstrap Minimo (ChatGPT Web / ZIP)

**Nuova chat: SÌ.** Prompt ufficiale per **ChatGPT Web**: carica il framework come ZIP,
allega PROJECT.yaml e immagini separatamente, poi incolla questo prompt.

```
Hai ricevuto il Mini4WD Manual SDK v2.5.0.

Leggi i file in questo ordine prima di qualsiasi altra cosa:
1. AI_ENTRYPOINT.md
2. SDK_CONTEXT.yaml
3. BOOTSTRAP.md
4. Core/AI_OPERATING_RULES.md
5. Config/LANGUAGE_POLICY.yaml
6. Core/TEXT_ENGINE.md
7. Core/DESIGN_LANGUAGE.md
8. Core/STYLE_GUIDE.md
9. Core/COMPONENT_SYSTEM.md
10. Core/PAGE_SYSTEM.md

Ho allegato anche il mio PROJECT.yaml e le immagini di riferimento del modello.
Leggi PRIMA tutti i file del framework, POI analizza PROJECT.yaml e le immagini.

Poi produci il Bootstrap Report nel formato definito da AI_ENTRYPOINT.md
e fermati: attendi la mia approvazione prima di generare qualsiasi contenuto.
```

### Prompt F — Continuità di Sessione

**Nuova chat: SÌ** (è il suo scopo: riprendere dopo una chat degenerata o chiusa).
Riallegare i file della fase in corso.

```
Stiamo continuando la sessione Mini4WD Manual SDK v2.5.0
per il modello {NOME_MODELLO}.

Stato attuale:
- Fase corrente: {FASE}            (es. Fase 2 — Generazione Testi)
- Pagine completate: {LISTA}
- Pagina corrente: {PAGINA}

Tutte le regole del framework restano attive: testo editoriale in italiano,
content.yaml come source of truth, pipeline Bootstrap → Testi → QA → Render → PDF,
QA bloccante, TODO: per i dati mancanti.

Continua dalla pagina {PAGINA} nella fase {FASE}.
```

---

## Note per tutti i prompt

- Sostituisci `{NOME_MODELLO}`, `{PAGINA}`, `{NOME_PAGINA}` con i valori reali
  (es. "Dash 01 Shadow Emperor", "P001", "Copertina").
- Allega i documenti come file quando possibile (più affidabile dell'incolla).
- Tutto l'output editoriale è in italiano; non chiedere traduzioni.
- Contesto limitato? Prompt E + caricamento incrementale.

## Tabella riassuntiva

| Fase | Prompt | Nuova chat | Runtime | Input chiave | Output |
|---|---|---|---|---|---|
| 1 Bootstrap | Fase 1 · Claude Code | SÌ | Claude Code | File repo (diretti) + foto | Bootstrap Report |
| 1 Bootstrap | Prompt E | SÌ | ChatGPT Web | ZIP + PROJECT.yaml + foto | Bootstrap Report |
| 2 Testi | Fase 2 (B) | NO | Entrambi | PromptEngine/{pagina}.md | content.yaml |
| 3 QA | Fase 3 (C) | NO | Entrambi | Tests/ + content.yaml | APPROVED/REJECTED |
| 4 Rendering | Fase 4 (D) | SÌ | Entrambi | Design + content.yaml locked + foto | Pagina illustrata |
| 5 PDF | Fase 5 | SÌ | Entrambi | PDF_MASTER + config + pagine | 3 PDF |
| — Continuità | F | SÌ | Entrambi | Stato sessione | Ripresa |

## Compatibilità

| Modello | Testato | Note |
|---|---|---|
| ChatGPT (GPT-4o, GPT-4) | ✓ | Allegati via file upload |
| Claude (Sonnet, Opus) | ✓ | Allegati o incolla |
| Gemini | ⚠️ Solo Fase 4 | Fallito UAT-002 sulla generazione whole-page (Fase 3/4 vecchio scope). Ri-testato con successo per la Fase 4 a scope ristretto (solo illustrazione singola, § 4b) in UAT-004. Fase 1-3 non verificate. Vedi `UAT/UAT-002.md` e `UAT/UAT-004.md`. |
| Modelli futuri | Atteso ✓ | Nessuna sintassi model-specific |

## Riferimenti

- `WORKFLOW.md` (root) — state machine completa
- `START_HERE.md` — onboarding operatore
- `OperatorGuide/02_Workflow.md` — fasi e chat in versione compatta
- `Docs/LOAD_ORDER.md` — ordine di caricamento con motivazioni
- `Core/AI_OPERATING_RULES.md` — 100 regole comportamentali
