# Guida Claude Code — Il Tuo Primo Manuale

**OperatorGuide · Mini4WD Manual SDK v2.5.0 · Runtime: Claude Code**

> Questa guida è autonoma: contiene tutto ciò che ti serve per produrre il tuo primo manuale
> usando Claude Code. Non è necessario leggere altri documenti prima di questa guida.
> Segui i passi nell'ordine esatto.

---

## Cosa è diverso da ChatGPT Web

Con Claude Code l'AI ha accesso diretto al repository clonato localmente:
- Non devi caricare alcun ZIP
- Non devi allegare file manualmente
- L'AI legge direttamente tutti i file del framework
- L'AI **scrive** i file generati (content.yaml, metadata.yaml, ecc.) direttamente nel repository
- Non serve riaprire una nuova sessione per ogni fase: Claude Code mantiene il contesto del repository

> ⚠️ **Claude Code gestisce solo la fase TESTI (Bootstrap → Generazione → QA → Sigillatura).**
> Claude Code **non può generare immagini**. Il rendering (Fase 4) richiede un'AI generativa
> visuale separata: ChatGPT Web (DALL-E) o altro runtime supportato (vedi `Docs/RUNTIMES.md`).
> Quando tutti i content.yaml sono locked, passerai a un runtime immagini — vedi **PASSO 10**.

---

## Cosa ti serve

- [ ] Claude Code installato (`npm install -g @anthropic-ai/claude-code` o pacchetto equivalente)
- [ ] Git installato
- [ ] Repository Mini4WD Manual SDK clonato localmente
- [ ] Nome ufficiale Tamiya del tuo modello (grafia esatta)
- [ ] Codici vernice Tamiya (es. TS-57, PS-1, XF-1)
- [ ] Foto del modello: minimo 5 angolazioni (front, lati, top, 3/4 frontale)

---

## PASSO 1 — Clona il repository

```bash
git clone https://github.com/diegoperu/mini4wdpaintframework.git
cd mini4wdpaintframework
```

Il repository è ora disponibile localmente. Claude Code può leggere e scrivere tutti i file.

---

## PASSO 2 — Crea la cartella progetto

```bash
MODEL="Nome_Modello"        # spazi → underscore, MAI trattini nel nome cartella
mkdir -p "Projects/${MODEL}/Images"
mkdir -p "Projects/${MODEL}/Output/raw" "Projects/${MODEL}/Output/pdf"
mkdir -p "Projects/${MODEL}/Notes"
```

Regole nome cartella (da `Core/NAMING_CONVENTION.md`):

| Modello | Nome cartella corretto |
|---|---|
| Proto Emperor | `Proto_Emperor` |
| Dash 01 Shadow Emperor | `Dash_01_Shadow_Emperor` |

Maiuscole conservate, underscore tra le parole, niente trattini nel nome cartella.

**Non creare altre cartelle**, in particolare niente sotto `Assets/`.

---

## PASSO 3 — Copia e compila PROJECT.yaml

```bash
cp Templates/PROJECT.yaml "Projects/${MODEL}/PROJECT.yaml"
```

Apri la **copia** (MAI il master in `Templates/`) con qualsiasi editor e compila ogni campo marcato `# REQUIRED`. Regole:

1. **Nomi vernici reali** — usa i codici Tamiya reali (TS-57, X-10, PS-1…), mai inventati
2. **Dato mancante** → scrivi `TODO:` — mai un valore inventato
3. **`modelSlug`** in kebab-case: `dash-01-shadow-emperor`
4. I percorsi in `paths:` sono relativi alla cartella progetto: `Images/ref_front.jpg`
5. I valori tecnici (`finish: gloss`, `technique: spray-can`) restano in inglese

Esempio di riferimento già compilato: `Projects/Proto_Emperor/PROJECT.yaml` (sola lettura).

---

## PASSO 4 — Inserisci le immagini di riferimento

Copia le tue foto in `Projects/{Modello}/Images/` — **unica posizione valida**.

| Nome file | Vista | Obbligatoria |
|---|---|---|
| `ref_front.jpg` | Frontale | **SÌ** |
| `ref_side_left.jpg` | Lato sinistro | **SÌ** |
| `ref_side_right.jpg` | Lato destro | **SÌ** |
| `ref_top.jpg` | Dall'alto | **SÌ** |
| `ref_3q_front.jpg` | 3/4 frontale-sinistra | **SÌ** (per la copertina) |
| `ref_rear.jpg` | Posteriore | Consigliata |
| `ref_detail_*.jpg` | Dettagli particolari | Se disponibili |

Requisiti: minimo 2048px sul lato lungo, sfondo bianco o neutro, fuoco nitido.

---

## PASSO 5 — Verifica pre-bootstrap

```
[ ] Projects/{Modello}/ creata con Images/, Output/, Notes/
[ ] PROJECT.yaml compilato, nessun campo REQUIRED vuoto (o TODO: motivato)
[ ] Minimo 5 foto in Projects/{Modello}/Images/
[ ] Nome cartella con underscore, modelSlug in kebab-case
[ ] Nessun file toccato fuori da Projects/{Modello}/
```

---

## PASSO 6 — Avvia Claude Code nel repository

```bash
claude
```

Claude Code si avvia nel contesto del repository. L'AI può leggere tutti i file del framework direttamente — non serve allegare nulla.

---

## PASSO 7 — Usa il Prompt Bootstrap

Incolla il **Prompt Fase 1 — Bootstrap** da `Docs/AI_BOOTSTRAP_PROMPT.md §FASE 1 · Claude Code`.

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

Sostituisci `{Modello}` con il nome reale della cartella progetto.

---

## PASSO 8 — Approva il Bootstrap Report

L'AI produce un Bootstrap Report. Verifica che contenga:

- [ ] Il nome del TUO modello (non un modello di esempio)
- [ ] I TUOI codici vernice
- [ ] Le 10 pagine P001–P010 in stato `draft`
- [ ] Conferma versione SDK 2.4.1

Se corretto, scrivi:

```
Bootstrap approvato. Inizia dalla pagina P001.
```

> Questo messaggio approva il bootstrap e indica da quale pagina partire.
> L'AI **non genera automaticamente** — aspetta il prompt esplicito del PASSO 9a.
> Subito dopo la conferma dell'AI, passa al PASSO 9a con CODICE_PAGINA=P001.

Se il report cita dati sbagliati: correggi `Projects/{Modello}/PROJECT.yaml` e rilancia il prompt.

---

## PASSO 9 — Generazione testi (stessa sessione)

Rimani nella stessa sessione Claude Code. L'AI scrive `content.yaml` direttamente nel repo —
non serve copiare nulla dalla chat.

Il ciclo **9a → 9b → 9c si ripete N volte** — una per ogni pagina attiva.

> **Il numero di pagine dipende dal tuo progetto:**
> - **P008 Decalcomanie** — includi solo se il tuo modello ha decalcomanie (`decals:` non vuoto in PROJECT.yaml). Se `decals: []`, salta P008.
> - **P009 Variante Premium** — includi solo se `premiumVariant.enabled: true` in PROJECT.yaml.
> - Tutte le altre pagine (P001–P007, P010) sono **sempre richieste**.
>
> Minimo: **8 pagine** (P001–P007 + P010). Massimo: **10 pagine**.
>
> 💡 **Power user:** usa `Scripts/generate_prompts.py` per generare automaticamente tutti i prompt precompilati per le pagine del tuo progetto. Lo script legge PROJECT.yaml e chiede interattivamente per P008/P009.

---

### 9a — Genera il content.yaml (una pagina alla volta)

Copia il prompt qui sotto, sostituisci i tre valori in maiuscolo e invialo:

```
Fase 2 — Text Engine.
Genera la pagina CODICE_PAGINA (NOME_PAGINA) del manuale per il modello NOME_MODELLO.

1. Leggi il file PromptEngine/FILE_PROMPT.md nel repository.
2. Estrai tutti i valori dal PROJECT.yaml del progetto.
3. Risolvi i riferimenti per ID: se paintSequence usa colorId, cerca il colore
   corrispondente in paintScheme.colors (dove id == colorId) ed estrai paintCode,
   paintName, finish, hex. Non lasciare TODO: per valori raggiungibili tramite
   riferimento — usa TODO: solo per dati genuinamente assenti nel PROJECT.yaml.
4. Genera il file content.yaml completo per questa pagina e scrivilo in
   Projects/CARTELLA_MODELLO/CARTELLA_VARIANTE/ApprovedText/CODICE_PAGINA/content.yaml.
5. Usa TODO: per qualsiasi valore non disponibile in PROJECT.yaml — non inventare nulla.
6. Tutto il testo editoriale in italiano; codici e nomi commerciali restano invariati.

Non procedere al rendering: siamo in Text Mode. Output atteso: content.yaml scritto nel
repository, pronto per la validazione QA.
```

Sostituisci prima di inviare:

| Placeholder | Cosa scrivere | Esempio |
|---|---|---|
| `CODICE_PAGINA` | ID pagina | `P001` |
| `NOME_PAGINA` | Nome della pagina | `Copertina` |
| `NOME_MODELLO` | Nome del tuo modello | `Magnum Saber Premium` |
| `FILE_PROMPT.md` | File PromptEngine corrispondente (vedi tabella sotto) | `Cover.md` |
| `CARTELLA_MODELLO` | Nome cartella modello (PascalCase_Underscore) | `Magnum_Saber_Premium` |
| `CARTELLA_VARIANTE` | Nome cartella variante (da paintScheme.slug) | `Cotton_Candy_Drift` |

💡 **Power user:** usa `Scripts/generate_prompts.py` — compila automaticamente tutti i placeholder inclusi modello e variante.

Tabella pagine → file PromptEngine:

| Pagina | Nome | FILE_PROMPT.md | Condizione |
|---|---|---|---|
| P001 | Copertina | `Cover.md` | Sempre |
| P002 | Schema Colori | `ColorScheme.md` | Sempre |
| P003 | Materiali | `Materials.md` | Sempre |
| P004 | Preparazione | `Preparation.md` | Sempre |
| P005 | Verniciatura | `Painting.md` | Sempre |
| P006 | Mascheratura | `Masking.md` | Sempre |
| P007 | Dettagli | `Details.md` | Sempre |
| P008 | Decalcomanie | `Decals.md` | Solo se `decals:` non vuoto in PROJECT.yaml |
| P009 | Variante Premium | `Premium.md` | Solo se `premiumVariant.enabled: true` |
| P010 | Checklist Finale | `FinalChecklist.md` | Sempre |

> ⚠️ **`TODO:` nell'output non è un errore.** Significa che quel dato non è presente
> in PROJECT.yaml. Se vedi molti `TODO:` nei campi vernice o sequenze operative, integra
> PROJECT.yaml con quei dati e rigenera la pagina.
> `TODO:` su un campo che HAI compilato = AI non ha letto il file o ha mancato il JOIN colorId → rilanciare il prompt.

---

### 9b — Valida con QA (stessa sessione, subito dopo)

Dopo che l'AI ha scritto il content.yaml, invia questo prompt:

```
Fase 3 — QA. Esegui la validazione completa sul content.yaml appena generato
in Projects/CARTELLA_MODELLO/CARTELLA_VARIANTE/ApprovedText/CODICE_PAGINA/content.yaml.

Ambito: questo è CONTENUTO GENERATO (status: review), non un template. Applica
Tests/ContentValidation.md §Validation Scope.

Content Validation: applica tutte e 7 le suite di Tests/ContentValidation.md.
Text Validation: applica tutti e 9 i test di Tests/TextValidation.md.

Ricorda le eccezioni language-neutral: codici vernice (TS-37, X-10, PS-1…),
nomi commerciali (Chrome Silver, Gun Metal, Flat Black, Primer…), chiavi YAML
e valori di schema NON sono violazioni linguistiche.

Riporta:
- Esito per suite: PASS / FAIL / WARNING
- Ogni FAIL con riga e correzione necessaria
- Verdetto finale: APPROVED / REJECTED
```

Sostituisci `CODICE_PAGINA` con il codice reale (es. `P001`).

---

### 9c — Correggi e sigilla

- **REJECTED** → chiedi all'AI di applicare le correzioni direttamente nel file, poi invia di nuovo il Prompt QA (9b).
- **APPROVED** → invia in chat:

```
Approvato. Sigilla la pagina CODICE_PAGINA:
Projects/CARTELLA_MODELLO/CARTELLA_VARIANTE/ApprovedText/CODICE_PAGINA/metadata.yaml → status: locked
Aggiungi riga di changelog in Projects/CARTELLA_MODELLO/CARTELLA_VARIANTE/ApprovedText/CODICE_PAGINA/changelog.md.
```

---

### 9d — Pagina successiva

Ripeti 9a → 9b → 9c per ogni pagina fino a P010.
Non aprire una nuova sessione tra una pagina e l'altra.

---

## PASSO 10 — Handoff al Runtime Immagini

> ⚠️ **Claude Code non può generare immagini.**
> Il rendering (Fase 4) richiede un'AI generativa visuale: ChatGPT Web (DALL-E) o altro runtime supportato (vedi `Docs/RUNTIMES.md`).
> Questo passo descrive come trasferire tutto il lavoro fatto con Claude Code al runtime immagini.

---

### 10a — Verifica che tutte le pagine siano locked

Prima di passare al rendering, controlla che ogni pagina da P001 a P010 abbia `status: locked`:

```bash
grep -r "status:" Projects/CARTELLA_MODELLO/CARTELLA_VARIANTE/ApprovedText/*/metadata.yaml
```

Ogni riga deve mostrare `status: locked`. Se qualche pagina è ancora `draft` o `review`,
torna al PASSO 9 per completarla.

---

### 10b — Prepara il pacchetto di handoff

> ⚠️ **Repository multi-progetto.** Lo ZIP del repo intero contiene *tutti* i progetti
> (con le rispettive `Images/` di riferimento, il peso maggiore). Con più di un progetto
> attivo diventa rapidamente troppo grande per un allegato ChatGPT Web, e non c'è modo
> di dire a ChatGPT quale progetto renderizzare se ce ne sono più di uno nello ZIP.
> Usa **Opzione C** per un pacchetto mirato a un solo progetto/variante.

**Opzione A — Handoff via GitHub (repo intero, solo se hai un unico progetto attivo):**
1. Esegui `git add . && git commit -m "lock: all pages P001-P010"` e `git push`
2. Scarica il repository aggiornato come ZIP da GitHub (Code → Download ZIP)
3. Il ZIP conterrà già tutti i content.yaml locked in `Projects/{Model}/{Variant}/ApprovedText/`

**Opzione B — Handoff diretto (senza push):**
Per ogni pagina che vuoi renderizzare, copia il file localmente:
- `Projects/{Model}/{Variant}/ApprovedText/P001/content.yaml` → tieni pronto da allegare
- `Projects/{Model}/{Variant}/ApprovedText/P002/content.yaml` → ecc.

**Opzione C — Pacchetto mirato (consigliata, multi-progetto):**
```bash
Scripts/package_handoff.sh {Model} {Variant}
# es: Scripts/package_handoff.sh Magnum_Saber_Premium Cotton_Candy_Drift
```
Lo script valida che tutte le pagine `ApprovedText/P0xx` siano `status: "locked"`
(si blocca altrimenti) e produce uno ZIP in `Build/Handoff/{Model}_{Variant}_{timestamp}.zip`
contenente **solo**:
- i 5 file richiesti dalla Fase 4 (`Core/RENDER_GUIDE.md`, `Core/DESIGN_LANGUAGE.md`,
  `Core/STYLE_GUIDE.md`, `Core/COMPONENT_SYSTEM.md`, `Assets/DesignSystem/Tokens/tokens.example.yaml`)
- `Core/QA_SYSTEM.md` (per la checklist finale)
- `Projects/{Model}/{Variant}/` completo (PROJECT.yaml, ApprovedText/, Images/)
- `HANDOFF_CONTEXT.md` alla radice (da `Docs/RENDER_HANDOFF_CONTEXT.md`) — senza
  `AI_ENTRYPOINT.md` (che forzerebbe un bootstrap report completo, sbagliato per un
  handoff di singola pagina) il pacchetto mirato rischiava di essere letto da ChatGPT
  come corpus documentale da analizzare invece che come istruzione a generare
  un'immagine: riprodotto 2/2 volte un rifiuto ("non posso produrre l'illustrazione
  né verificare i pixel del render") con il pacchetto mirato privo di framing. Questo
  file dichiara esplicitamente il ruolo di Render Engine e ammorbidisce la richiesta
  di verifica colore da "lettura pixel esatta" a "confronto visivo best-effort".

Nessun altro progetto del repo entra nello ZIP — dimensione minima, nessuna ambiguità
su quale progetto stai renderizzando.

---

### 10c — Rendering in ChatGPT Web (una pagina alla volta)

Apri **ChatGPT Web**, nuova chat. Carica:

| File | Come ottenerlo |
|---|---|
| `{Model}_{Variant}_{timestamp}.zip` | Prodotto al punto 10b (Opzione C, consigliata) — oppure `Mini4WDFramework.zip` (Opzioni A/B) |
| `content.yaml` della pagina da renderizzare | Da `Projects/{Model}/{Variant}/ApprovedText/P00x/content.yaml` (allegato separato, solo se non già nello ZIP) |
| Immagini di riferimento | Da `Projects/{Model}/{Variant}/Images/` (solo se non già nello ZIP) |

> Con il pacchetto mirato (Opzione C), `content.yaml`, `Images/` e i 5 file Fase 4 sono
> già dentro — non serve allegarli separatamente. Se usi invece il ZIP del repo intero
> (Opzioni A/B), allega comunque `content.yaml` come file separato e specifica sempre
> `PROGETTO: {Model}/{Variant}` nel prompt (vedi sotto) — con più progetti nello ZIP
> ChatGPT non ha altro modo di sapere quale renderizzare.

Copia il prompt qui sotto, sostituisci i valori in maiuscolo e invialo:

```
Fase 4 — Render Engine.
PROGETTO: MODELLO/VARIANTE
Genera l'illustrazione per la pagina CODICE_PAGINA (NOME_PAGINA).

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

Sostituisci prima di inviare:

| Placeholder | Cosa scrivere | Esempio |
|---|---|---|
| `MODELLO/VARIANTE` | Cartella progetto/variante | `Magnum_Saber_Premium/Cotton_Candy_Drift` |
| `CODICE_PAGINA` | ID pagina | `P001` |
| `NOME_PAGINA` | Nome della pagina | `Copertina` |

---

> ⚠️ **Gemini non è supportato per il rendering** (Fase 3/4). Fallito in 3 tentativi
> su UAT-002 (allucinazioni, metadati leaked, risposte scollegate dal prompt).
> Vedi `UAT/UAT-002.md` e `Docs/RUNTIMES.md`.

---

### 10d — Salva le immagini generate

Per ogni pagina renderizzata:
1. Scarica l'immagine prodotta dall'AI generativa
2. Salvala in `Projects/{Model}/{Variant}/ApprovedImages/P00x/` nel repository locale
3. Aggiorna `Projects/{Model}/{Variant}/ApprovedText/P00x/metadata.yaml → status: rendered`

---

## PASSO 11 — PDF

Con tutte le pagine in `status: rendered`, usa il **Prompt Fase 5** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

Il PDF può essere assemblato con ChatGPT Web (stessa procedura handoff del PASSO 10).
Prerequisito: copia compilata di `Templates/PDF_CONFIG.yaml` in `Projects/{Modello}/PDF_CONFIG.yaml`.

---

## Riepilogo fasi

| Fase | Runtime | Cosa fa l'AI |
|---|---|---|
| Bootstrap | **Claude Code** | Legge dal repo, produce Bootstrap Report |
| Testi P001–P010 | **Claude Code** | Scrive content.yaml nel repo |
| QA Testi | **Claude Code** | Valida content.yaml, APPROVED/REJECTED |
| Sigillatura | **Claude Code** | Imposta metadata.yaml → locked |
| **Rendering** | **AI immagini** (ChatGPT Web) | Genera pagine illustrate da content.yaml |
| PDF | **AI immagini** (ChatGPT Web) | Assembla 3 varianti PDF |

---

## Sessione degenerata o contesto saturo?

Usa il **Prompt F — Continuità** da `Docs/AI_BOOTSTRAP_PROMPT.md §Prompt di servizio`.
Con Claude Code non serve ricaricare i file — l'AI accede di nuovo direttamente al repository.

---

## Errori frequenti

| Errore | Causa | Soluzione |
|---|---|---|
| L'AI valida template vuoti e dà FAIL | Hai saltato la generazione (Fase 2) | Genera prima, poi valida |
| content.yaml con tutti TODO: in paint_sequence | AI non ha risolto il JOIN colorId → paintScheme.colors | Rilancia il Prompt 9a — il punto 3 istruisce il JOIN |
| content.yaml contiene dati inventati | PROJECT.yaml aveva campi vuoti | Correggi PROJECT.yaml, rigenera |
| L'AI modifica file fuori da Projects/ | Istruzioni errate nel prompt | Usa i prompt ufficiali, controlla le modifiche |
| Contesto saturo | Sessione troppo lunga | Prompt F — Continuità (il repo rimane invariato) |
| ChatGPT usa content.yaml sbagliato al rendering | ZIP originale senza locked files, content.yaml non allegato separato | Usa Opzione A (ZIP aggiornato) oppure allega content.yaml separatamente |

Guida errori completa: `OperatorGuide/06_Errori_Comuni.md`

---

## Riferimenti

- `Docs/RUNTIMES.md` — confronto tra tutti i runtime
- `Docs/AI_BOOTSTRAP_PROMPT.md` — tutti i prompt pronti per fase
- `OperatorGuide/01_Primo_Manuale.md` — panoramica delle 6 tappe
- `Projects/PROJECT_BOOTSTRAP.md` — guida rapida creazione progetto
- `OperatorGuide/06_Errori_Comuni.md` — diagnosi degli errori comuni
- `Knowledge/FAQ.md` — domande frequenti
