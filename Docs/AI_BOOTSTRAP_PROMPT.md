# AI_BOOTSTRAP_PROMPT.md — Prompt Ufficiali per Fase

**Mini4WD Manual SDK v2.5.0**

> Un prompt pronto per ogni fase della pipeline. Per ogni fase trovi: **Input**
> (cosa allegare), **Output** (cosa aspettarti), **Prompt** (da copiare), **Nuova
> chat SÌ/NO**. Verificato con ChatGPT (GPT-4o) e Claude (Sonnet/Opus).
> Gemini: non supportato — fallito UAT-002 (vedi §Compatibilità).
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

*(ex Prompt D)*

**Nuova chat: SÌ** — il rendering usa un contesto diverso (design, non testi).

**Input (file da allegare):**
1. `Core/RENDER_GUIDE.md`
2. `Core/DESIGN_LANGUAGE.md`
3. `Core/STYLE_GUIDE.md`
4. `Core/COMPONENT_SYSTEM.md`
5. `Assets/DesignSystem/Tokens/tokens.example.yaml`
6. il `content.yaml` **locked** della pagina
7. le foto da `Projects/{Modello}/Images/`

**Output atteso:** pagina illustrata completa, pronta per la validazione visiva
(`Core/QA_SYSTEM.md`). Da salvare in `Projects/{Model}/{Variant}/ApprovedImages/P00x/`.

**Prompt:**

```
Fase 4 — Render Engine.
Genera l'illustrazione per la pagina {PAGINA} ({NOME_PAGINA}).

Il content.yaml allegato è approvato e bloccato (status: locked).

Regole operative:
- Leggi ESCLUSIVAMENTE da content.yaml. Non generare, modificare o riformulare testo.
- Usa solo i Design Token di tokens.example.yaml. Nessun valore hardcoded.
- La forma fisica del modello (sagoma, proporzioni, componenti meccanici) deve
  corrispondere esattamente alle immagini di riferimento. Colori, livrea, fiamme,
  decal e grafica NON derivano dalle immagini di riferimento — sono quasi sempre
  box-art stock con schema colori diverso da quello da documentare. Palette e aree
  di applicazione provengono ESCLUSIVAMENTE da content.yaml → colors[]. Se la livrea
  della foto reference è in conflitto con lo schema colori, scarta completamente la
  livrea della foto e ridipingi secondo colors[] — non mescolare o "tingere" i colori
  esistenti. Non inventare grafiche (fiamme, strisce) assenti dallo schema colori.
- Applica Core/DESIGN_LANGUAGE.md e Core/STYLE_GUIDE.md.
- Componenti secondo Core/COMPONENT_SYSTEM.md. Non fondere componenti diversi in un
  unico elemento: es. C010 Paint Legend (tabella, senza badge) e C011 Paint Code Box
  (box indipendente con badge finitura) sono componenti separati con collocazioni
  diverse — non unirli in un'unica card.
- Se un componente ha altezza variabile, il box deve espandersi per contenere tutto
  il testo. Non troncare mai il testo per farlo entrare in uno spazio fisso.
- Sfondo bianco puro. Pannello header viola (token.PrimaryViolet).

Output atteso: pagina illustrata completa. Poi esegui la checklist visiva di
Core/QA_SYSTEM.md sulle voci applicabili e riporta PASS/FAIL per ciascuna — per la
voce colori, verifica ogni colors[].hex contro i pixel del render singolarmente, non
per impressione generale.
```

**Guida passo-passo:** `FIRST_RENDER.md`

---

## FASE 5 — PDF

**Nuova chat: SÌ.**

**Input (file da allegare):**
1. `Core/PDF_MASTER.md`
2. `Projects/{Modello}/PDF_CONFIG.yaml` (copia compilata di `Templates/PDF_CONFIG.yaml`)
3. le pagine renderizzate (o i percorsi in `ApprovedAssets/Images/`)

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
| Gemini | ❌ Non supportato | Fallito UAT-002: allucinazioni Fase 3/4, metadati leaked nel render, risposta scollegata. Vedi `UAT/UAT-002.md`. |
| Modelli futuri | Atteso ✓ | Nessuna sintassi model-specific |

## Riferimenti

- `WORKFLOW.md` (root) — state machine completa
- `START_HERE.md` — onboarding operatore
- `OperatorGuide/02_Workflow.md` — fasi e chat in versione compatta
- `Docs/LOAD_ORDER.md` — ordine di caricamento con motivazioni
- `Core/AI_OPERATING_RULES.md` — 100 regole comportamentali
