# Guida ChatGPT Web — Il Tuo Primo Manuale

**OperatorGuide · Mini4WD Manual SDK v2.4.1 · Runtime: ChatGPT Web**

> Questa guida è autonoma: contiene tutto ciò che ti serve per produrre il tuo primo manuale
> usando ChatGPT Web. Non è necessario leggere altri documenti prima di questa guida.
> Segui i passi nell'ordine esatto.

---

## Cosa è diverso da Claude Code

Con ChatGPT Web l'AI non ha accesso diretto al repository. Devi:
- Caricare il framework come archivio ZIP (una volta sola per ogni nuova chat)
- Allegare il tuo PROJECT.yaml separatamente
- Allegare le tue immagini di riferimento separatamente

L'AI non scrive file nel repository — produce l'output direttamente in chat. Sei tu a copiare i risultati nei file locali se vuoi salvarli.

---

## Cosa ti serve

- [ ] Account ChatGPT (GPT-4o o superiore — contesto ampio necessario)
- [ ] Il repository Mini4WD Manual SDK scaricato come ZIP da GitHub
- [ ] Nome ufficiale Tamiya del tuo modello (grafia esatta)
- [ ] Codici vernice Tamiya (es. TS-57, PS-1, XF-1)
- [ ] Foto del modello: minimo 5 angolazioni (front, lati, top, 3/4 frontale)

---

## PASSO 1 — Scarica il repository

Vai alla pagina GitHub del Mini4WD Manual SDK.
Clicca **Code → Download ZIP**.

Salva il file scaricato sul tuo computer. Non estrarre il contenuto.
Questo file ZIP è il framework che caricherai in ChatGPT.

> Il file scaricato si chiamerà qualcosa come `mini4wdpaintframework-main.zip`.
> Puoi rinominarlo `Mini4WDFramework.zip` per riconoscerlo facilmente.

---

## PASSO 2 — Estrai SOLO il template di progetto

⚠️ **Non estrarre tutto il repository**: caricherai il ZIP intatto in ChatGPT.

Devi estrarre solamente un file: `Templates/PROJECT.yaml`.

Come fare:
1. Apri il file ZIP con il tuo gestore di archivi (Windows Explorer, 7-Zip, ecc.)
2. Naviga in `Templates/`
3. Estrai solo `PROJECT.yaml` in una cartella locale per il tuo progetto
   (es. `Documenti/MioProgetto/PROJECT.yaml`)

Il resto del ZIP rimane intatto — lo caricherai in ChatGPT così com'è.

---

## PASSO 3 — Crea la struttura del progetto in locale

Crea una cartella locale per il tuo progetto. Struttura consigliata:

```
MioProgetto/
├── PROJECT.yaml          ← estratto dal ZIP al Passo 2
└── Images/               ← le tue foto (Passo 5)
    ├── ref_front.jpg
    ├── ref_side_left.jpg
    ├── ref_side_right.jpg
    ├── ref_top.jpg
    └── ref_3q_front.jpg
```

Non creare altre cartelle — non ti servono per il runtime ChatGPT Web.

---

## PASSO 4 — Compila PROJECT.yaml

Apri `PROJECT.yaml` con un editor di testo (Notepad, VS Code, qualsiasi editor).

Compila ogni campo marcato `# REQUIRED`. Regole fondamentali:

1. **Nomi vernici reali** — usa i codici Tamiya reali (TS-57, X-10, PS-1…), mai inventati
2. **Dato mancante** → scrivi `TODO:` — mai un valore inventato
3. **`modelSlug`** in kebab-case: `dash-01-shadow-emperor` (trattini, tutto minuscolo)
4. **Nome cartella** con underscore: `Dash_01_Shadow_Emperor`
5. I valori tecnici (`finish: gloss`, `technique: spray-can`) restano in inglese
6. Il testo editoriale che finirà nel manuale va in italiano

Esempio corretto:

```yaml
project:
  modelName: "Dash 01 Shadow Emperor"
  modelSlug: "dash-01-shadow-emperor"
  seriesName: "Dash Series"
```

Lascia `sdk_version: 2.4.1` invariato.

---

## PASSO 5 — Prepara le immagini di riferimento

Copia le tue foto nella cartella `MioProgetto/Images/`.

| Nome file | Vista | Obbligatoria |
|---|---|---|
| `ref_front.jpg` | Frontale | **SÌ** |
| `ref_side_left.jpg` | Lato sinistro | **SÌ** |
| `ref_side_right.jpg` | Lato destro | **SÌ** |
| `ref_top.jpg` | Dall'alto | **SÌ** |
| `ref_3q_front.jpg` | 3/4 frontale-sinistra | **SÌ** (per la copertina) |
| `ref_rear.jpg` | Posteriore | Consigliata |
| `ref_detail_*.jpg` | Dettagli particolari | Se disponibili |

Requisiti foto: minimo 2048px sul lato lungo, sfondo bianco o neutro, fuoco nitido.

---

## PASSO 6 — Verifica pre-bootstrap

Prima di aprire ChatGPT, controlla:

```
[ ] Mini4WDFramework.zip — ZIP del repository (non estratto)
[ ] PROJECT.yaml — compilato, nessun campo REQUIRED vuoto (o TODO: motivato)
[ ] ref_front.jpg e almeno altre 4 foto presenti
[ ] modelSlug in kebab-case, nome cartella con underscore
```

---

## PASSO 7 — Apri UNA NUOVA CHAT in ChatGPT

Apri [chat.openai.com](https://chat.openai.com) e clicca **New chat**.

> ⚠️ Ogni nuova fase che richiede un contesto diverso (rendering, PDF)
> richiede una nuova chat. Ogni volta dovrai ricaricare i file necessari.

---

## PASSO 8 — Carica i file nella chat

Nella nuova chat, carica nell'ordine:

1. **`Mini4WDFramework.zip`** — il repository come ZIP, non estratto
2. **`PROJECT.yaml`** — il tuo file compilato
3. **Le tue immagini** — tutte le foto preparate al Passo 5

⚠️ **NON caricare singolarmente:**

| Non caricare | Perché |
|---|---|
| `SDK_CONTEXT.yaml` | È già dentro il ZIP |
| `BOOTSTRAP.md` | È già dentro il ZIP |
| `Core/AI_OPERATING_RULES.md` | È già dentro il ZIP |
| `Core/TEXT_ENGINE.md` | È già dentro il ZIP |
| `Config/LANGUAGE_POLICY.yaml` | È già dentro il ZIP |
| `PromptEngine/Cover.md` (o altri) | È già dentro il ZIP |

Caricare file singoli dal ZIP **oltre** allo ZIP stesso genera contesto duplicato e crea confusione. Carica solo: **ZIP + PROJECT.yaml + immagini**.

---

## PASSO 9 — Incolla il Prompt Bootstrap

Copia il **Prompt E — Bootstrap Minimo** da `Docs/AI_BOOTSTRAP_PROMPT.md §Prompt di servizio` e incollalo nella chat.

```
Hai ricevuto il Mini4WD Manual SDK v2.4.1.

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

Conferma: versione SDK, le 10 regole non negoziabili di BOOTSTRAP.md,
la struttura del content.yaml, la lingua obbligatoria del testo editoriale.

Poi produci il Bootstrap Report nel formato definito da AI_ENTRYPOINT.md
e fermati: attendi la mia approvazione prima di generare qualsiasi contenuto.
```

Invia il messaggio e attendi la risposta dell'AI.

---

## PASSO 10 — Leggi e approva il Bootstrap Report

L'AI produce un Bootstrap Report. Verifica che contenga:

- [ ] Il nome del TUO modello (non un modello di esempio)
- [ ] I TUOI codici vernice (non valori placeholder)
- [ ] Le 10 pagine P001–P010 in stato `draft`
- [ ] Conferma esplicita della versione SDK 2.4.1

Se il report è corretto, scrivi in chat:

```
Bootstrap approvato. Inizia dalla pagina P001.
```

> Questo messaggio approva il bootstrap e indica da quale pagina partire.
> L'AI **non genera automaticamente** — aspetta il prompt esplicito del PASSO 11a.
> Subito dopo la conferma dell'AI, passa al PASSO 11a con CODICE_PAGINA=P001.

Se il report cita dati sbagliati o inventati: correggi il PROJECT.yaml e ricomincia dal Passo 7.

---

## PASSO 11 — Generazione testi (stessa chat)

Rimani nella stessa chat del bootstrap. Non riaprire una nuova chat e non ricaricare file.

Il ciclo **11a → 11b → 11c si ripete 10 volte** — una per ogni pagina da P001 a P010.
Completa P001 prima di passare a P002, e così via.

---

### 11a — Genera il content.yaml (una pagina alla volta)

Copia il prompt qui sotto, sostituisci i tre valori in maiuscolo e invialo in chat:

```
Fase 2 — Text Engine.
Genera la pagina CODICE_PAGINA (NOME_PAGINA) del manuale per il modello NOME_MODELLO.

1. Leggi il file PromptEngine/FILE_PROMPT.md dallo ZIP che hai già caricato.
2. Estrai tutti i valori dal PROJECT.yaml che hai già analizzato.
3. Risolvi i riferimenti per ID: se paintSequence usa colorId, cerca il colore
   corrispondente in paintScheme.colors (dove id == colorId) ed estrai paintCode,
   paintName, finish, hex. Non lasciare TODO: per valori raggiungibili tramite
   riferimento — usa TODO: solo per dati genuinamente assenti nel PROJECT.yaml.
4. Genera il file content.yaml completo per questa pagina.
5. Usa TODO: per qualsiasi valore non disponibile in PROJECT.yaml — non inventare nulla.
6. Tutto il testo editoriale in italiano; codici e nomi commerciali restano invariati.

Non procedere al rendering: siamo in Text Mode. Output atteso: solo il content.yaml,
pronto per la validazione QA.
```

Sostituisci prima di inviare:

| Placeholder | Cosa scrivere | Esempio |
|---|---|---|
| `CODICE_PAGINA` | ID pagina | `P001` |
| `NOME_PAGINA` | Nome della pagina | `Copertina` |
| `NOME_MODELLO` | Nome del tuo modello | `Magnum Saber Premium` |
| `FILE_PROMPT.md` | File PromptEngine corrispondente (vedi tabella sotto) | `Cover.md` |

Tabella pagine → file PromptEngine:

| Pagina | Nome | FILE_PROMPT.md |
|---|---|---|
| P001 | Copertina | `Cover.md` |
| P002 | Schema Colori | `ColorScheme.md` |
| P003 | Materiali | `Materials.md` |
| P004 | Preparazione | `Preparation.md` |
| P005 | Verniciatura | `Painting.md` |
| P006 | Mascheratura | `Masking.md` |
| P007 | Dettagli | `Details.md` |
| P008 | Decalcomanie | `Decals.md` |
| P009 | Variante Premium *(solo se abilitata)* | `Premium.md` |
| P010 | Checklist Finale | `FinalChecklist.md` |

> ⚠️ **`TODO:` nell'output non è un errore.** Significa che quel dato non è presente in PROJECT.yaml.
> Se vedi molti `TODO:` nei campi vernice o sequenze operative, torna a compilare PROJECT.yaml
> con quei dati (colori, codici, sequenza di applicazione), poi rigenera la pagina.
> `TODO:` su un campo che HAI compilato in PROJECT.yaml = AI non ha letto il file → ricomincia dal Passo 7.

---

### 11b — Valida con QA (stessa chat, subito dopo)

Dopo aver ricevuto il content.yaml, invia questo prompt nella stessa chat:

```
Fase 3 — QA. Esegui la validazione completa sul content.yaml appena generato.

Ambito: questo è CONTENUTO GENERATO (status: review), non un template. Applica
Tests/ContentValidation.md §Validation Scope dallo ZIP che hai già caricato.

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

---

### 11c — Correggi e risigilla

- **REJECTED** → chiedi all'AI di applicare le correzioni, poi invia di nuovo il Prompt QA (11b).
- **APPROVED** → invia in chat:

```
Approvato. Sigilla la pagina CODICE_PAGINA: metadata.yaml → status: locked, con riga di changelog.
```

Sostituisci `CODICE_PAGINA` con il codice reale (es. `P001`).

Poi **salva il content.yaml** dalla chat nel file locale corrispondente.

---

### 11d — Pagina successiva

Ripeti 11a → 11b → 11c per ogni pagina fino a P010.
Non aprire una nuova chat tra una pagina e l'altra.

---

## PASSO 12 — Rendering (NUOVA CHAT)

Apri una **nuova chat** in ChatGPT.

Carica:
1. `Mini4WDFramework.zip`
2. Il `content.yaml` **locked** della pagina da renderizzare
3. Le tue immagini di riferimento

Usa il **Prompt Fase 4** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

Ripeti per ogni pagina.

---

## PASSO 13 — PDF (NUOVA CHAT)

Apri una **nuova chat** in ChatGPT.

Carica:
1. `Mini4WDFramework.zip`
2. `Templates/PDF_CONFIG.yaml` (compilato con i dati del tuo progetto)
3. Le pagine renderizzate (o i percorsi salvati localmente)

Usa il **Prompt Fase 5** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

---

## Riepilogo file da caricare per fase

| Fase | Nuova chat | File da caricare |
|---|---|---|
| Bootstrap + Testi + QA | SÌ | ZIP + PROJECT.yaml + immagini |
| Rendering | SÌ | ZIP + content.yaml locked + immagini |
| PDF | SÌ | ZIP + PDF_CONFIG.yaml + pagine renderizzate |
| Continuità (chat degenerata) | SÌ | ZIP + file della fase corrente |

---

## Chat diventata lunga o confusa?

Apri una nuova chat, ricarica i file necessari per la fase corrente e usa il
**Prompt F — Continuità** da `Docs/AI_BOOTSTRAP_PROMPT.md §Prompt di servizio`.

---

## Errori frequenti

| Errore | Causa | Soluzione |
|---|---|---|
| L'AI non trova i file del framework | File caricati singolarmente invece che via ZIP | Ricomincia con ZIP |
| L'AI cita dati sbagliati | PROJECT.yaml incompleto o mal compilato | Correggi e riparti dal Passo 7 |
| L'AI valida template vuoti e dà FAIL | Hai saltato la generazione (Fase 2) | Genera prima, poi valida |
| L'AI dimentica le regole a metà chat | Contesto saturo | Nuova chat + Prompt F |
| Bootstrap Report con dati inventati | PROJECT.yaml aveva campi vuoti non marcati con TODO: | Correggi PROJECT.yaml, riparti dal Passo 7 |

Guida errori completa: `OperatorGuide/06_Errori_Comuni.md`

---

## Riferimenti

- `Docs/RUNTIMES.md` — confronto tra tutti i runtime
- `Docs/AI_BOOTSTRAP_PROMPT.md` — tutti i prompt pronti per fase
- `OperatorGuide/01_Primo_Manuale.md` — panoramica delle 6 tappe
- `OperatorGuide/06_Errori_Comuni.md` — diagnosi degli errori comuni
- `Knowledge/FAQ.md` — domande frequenti
