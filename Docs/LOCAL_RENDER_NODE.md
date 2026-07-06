# Nodo di Rendering IA Locale — Stima Preliminare

> Stato: **idea, non pianificata** (nessuna versione assegnata). Vedi `ROADMAP.md` →
> Planned — Unscheduled per il collegamento formale. Questo documento è la stima e il
> ragionamento architetturale dietro alla decisione futura di smettere di dipendere da
> ChatGPT Web per la Fase 4 (Render Engine).

## Perché

La Fase 4 (rendering) dipende oggi da ChatGPT Web (vedi `OperatorGuide/Runtimes/
Claude_Code.md` §10, `Docs/RUNTIMES.md`). I test del 2026-07-06 su Cotton Candy Drift
hanno mostrato limiti strutturali, non risolvibili solo con prompt engineering:

- rifiuti del tutto (richiesta di "certificare" conformità pixel-esatta impossibile
  da garantire onestamente da un modello generativo)
- una volta risolto il rifiuto, **allucinazioni di contenuto**: layout di un'altra
  pagina, tabelle colori (hex, codici) inventate di sana pianta invece di leggere
  `content.yaml`/`PROJECT.yaml`, contaminazione di contesto tra pagine nella stessa chat

Questi fallimenti non sono bug di prompt — sono il limite intrinseco di chiedere a un
modello diffusivo generalista di produrre testo/tabelle/hex esatti dentro un'unica
immagine generata end-to-end. Un nodo locale ben progettato può eliminare questa classe
di errore **architetturalmente**, non probabilisticamente.

## Evidenza — test su set completo (2026-07-06, ChatGPT "Thinking")

Render delle 8 pagine disponibili (P001-P007, P010) di Cotton Candy Drift in un'unica
chat continua (non una chat per pagina). Risultato: **la chat singola risolve la
coerenza visiva tra pagine, non la fedeltà al `content.yaml`.**

**Cosa funziona:**
- Coerenza cross-page: stessa auto, stessa palette, stesso stile di layout su tutte
  le 8 pagine (il problema di "veicolo inventato diverso ogni volta" è sparito)
- P002 (Schema Colori): hex e codici Tamiya **esatti al 100%** (PC001-PC006,
  TS-23/25/14/16/30/38) — per la prima volta zero errori sui dati numerici
- Separazione dei componenti rispettata (niente più C010/C011 fusi in un'unica card)

**Cosa non funziona (grave):**
- **La coerenza è ancorata a un'invenzione, non al content.yaml.** Nella prima pagina
  "densa" (P002) il modello ha inventato una mappatura colore→area leggermente
  sbagliata (es. PC005 Silver Leaf = "Headlight Surround" invece di "Telaio Super-II
  e cover motore" — un errore di fatto, non di forma). Da quel punto in poi, **ogni
  pagina successiva (P005, P007) ripete fedelmente lo stesso errore** invece di
  rileggere il content.yaml specifico della pagina. La chat singola dà consistenza
  interna, non fedeltà alla fonte.
- **Le pagine a contenuto prosa/lista lunga vengono quasi interamente reinventate:**
  P003 (Materiali) ha prodotto un inventario di "parti del kit" (viti, ingranaggi,
  ABS/POM) al posto di vernici/attrezzi/consumabili/sicurezza del content.yaml — zero
  corrispondenza. P004 (Preparazione) ha sostituito i 5 step reali con 5 sezioni
  inventate, perdendo lo step tecnicamente più importante (applicazione primer
  bianco). P006 (Mascheratura) ha inventato 6 zone al posto delle 3 reali (M001-M003).
  P010 (Checklist) ha prodotto voci generiche da manuale di montaggio meccanico
  invece delle voci specifiche sulla vernice del content.yaml.
- **Ordine tecnico perso:** P005 richiede di verniciare PC005 (telaio) per primo per
  evitare overspray sulla carrozzeria — il render lo mette al passo 5 invece che al
  passo 1, perdendo la ragione tecnica dietro la sequenza.
- **Tutto in inglese**, violazione trasversale a tutte le 8 pagine della regola
  zero-tolerance italiano-only (`Config/LANGUAGE_POLICY.yaml`, Golden Rule G01).
- **Un "PAGE X OF Y" inventato** (mai in content.yaml) diventa internamente incoerente
  pagina dopo pagina: "PAGE 1 OF 6" → ... → "PAGE 7 OF 6" (impossibile) → "PAGE 10 OF 10".

**Conclusione:** pagine tabellari/corte (P001, P002) restano abbastanza fedeli ai dati
puntuali; pagine a prosa lunga (P003, P004, P006, P010) vengono ricostruite a memoria
come "un manuale Mini4WD plausibile", non dai dati reali. Conferma diretta della tesi
di questo documento: un generatore di immagini end-to-end ha un tetto strutturale sulla
fedeltà testuale, indipendentemente da chat singola o multipla — il problema non è la
gestione della chat, è chiedere a un modello di generare testo/dati lunghi dentro pixel.

## Hardware disponibile

VM dedicata: NVIDIA A100 48GiB VRAM, 128GiB RAM, 24 core EPYC 7302, 100GiB SSD (OS),
1TiB HDD meccanico (dati/archiviazione).

**Verdetto: l'hardware non è il collo di bottiglia.** È hardware da datacenter, netto
overkill per generazione immagini — gira comodamente SDXL, Flux.1-dev (12B, ~24GB in
bf16) o SD3.5 con ControlNet/IP-Adapter attivi in parallelo, senza vincoli di memoria.
Il tempo di realizzazione lo determina l'ingegneria del pipeline, non l'attesa hardware.

## Decisione architetturale chiave

**Non chiedere all'IA di generare l'intera pagina.** Dividere in due componenti nette:

1. **AI (diffusione)** → genera SOLO l'illustrazione del modellino fisico (il
   veicolo/carrozzeria), condizionata su:
   - **forma**: ControlNet (canny/depth) dalla foto di riferimento reale
     (`Projects/{Model}/{Variant}/Images/ref_*.jpg`)
   - **colore**: regional prompting o color-conditioning da `content.yaml → colors[]`
     (mai dal box-art della foto reference, che ha uno schema colori diverso — stessa
     regola già in vigore nel prompt ChatGPT, vedi `OperatorGuide/Runtimes/
     Claude_Code.md` §10c)

2. **Codice deterministico** → compone testo, tabelle (Paint Legend, Paint Code Box),
   badge, callout numerati, header — letti **direttamente** da `content.yaml` /
   `PROJECT.yaml` / `manifest.yaml` via template HTML/CSS (screenshot con Playwright/
   Puppeteer) o compositing PIL. Zero generazione di testo da parte di un modello:
   è dato strutturato → rendering meccanico. Nessuna allucinazione possibile su hex,
   nomi, codici pagina.

Questa separazione risolve alla radice il problema di fedeltà osservato con ChatGPT,
che non ha (e non può avere, nell'interfaccia chat) questa separazione tra illustrazione
generativa e compositing deterministico.

## Stima per fasi (part-time, con assist Claude Code)

| Fase | Cosa | Tempo | Note |
|---|---|---|---|
| Setup ambiente | ComfyUI + SDXL/Flux.1-dev + ControlNet + IP-Adapter sulla VM | 1-2 giorni | Nessun vincolo hardware |
| R&D illustrazione | Forma coerente da foto reference + colore da content.yaml, iterazione su conditioning | 3-7 giorni | Parte più incerta della stima |
| Motore compositing | Template per i componenti `Core/COMPONENT_SYSTEM.md` (C001-C015) × pagine `Core/PAGE_SYSTEM.md` (P001-P010), letti da content.yaml/manifest.yaml | 5-10 giorni | Lavoro meccanico, prevedibile |
| Pipeline glue | Script: content.yaml → illustrazione AI + composito → pagina finale, sostituisce lo step ChatGPT | 2-3 giorni | |
| QA/test | Confronto contro `Core/QA_SYSTEM.md` su un progetto reale, iterazione | 3-5 giorni | |
| Buffer | Rifiniture da uso reale | 1-2 settimane | |

**Totale stimato: 4-7 settimane part-time, 2-3 settimane full-time.**

Variabile principale di rischio: la qualità del conditioning forma+colore (fase R&D).
Il resto è ingegneria meccanica con tempo prevedibile — building di un generatore di
pagine statiche, non ricerca.

## Vantaggi attesi vs ChatGPT Web

- Nessun limite di quota/tier free
- Fedeltà a colori/testo/tabelle diventa **strutturalmente garantita** (codice, non
  generativa) invece che probabilistica
- Nessuna contaminazione di contesto tra pagine (ogni run è un processo isolato,
  non una chat persistente)
- Compatibile con la clausola di `ROADMAP.md` → Vision: "the SDK must remain
  model-agnostic at the AI layer" — il nodo locale è un runtime aggiuntivo, non un
  requisito

## Prototipo compositing (2026-07-06)

La metà deterministica (punto 2 sopra) ha un primo prototipo funzionante, costruito
prima e indipendentemente dalla parte AI-illustrazione: `Scripts/render_page.py` +
template Jinja2 in `Scripts/templates/` (`P002.html.jinja` per ora). Legge
`content.yaml` + `Assets/DesignSystem/Tokens/tokens.example.yaml`, compone HTML/CSS,
esporta PNG (anteprima) o PDF (Playwright/Chromium headless, `pip install -r
Scripts/requirements.txt` + `playwright install chromium`).

Risultato su P002: hex, codici Tamiya, aree di applicazione e lingua italiana **esatti
al 100%** rispetto al content.yaml — zero possibilità di allucinazione, perché il testo
non è generato da alcun modello. L'illustrazione (viste ortogonali front/side/top) resta
un placeholder tratteggiato finché non esiste una sorgente immagine reale. Noto: il PDF
sconfina su 2 pagine con i placeholder a dimensione demo — tuning di impaginazione,
non un problema concettuale.

Questo decide il punto "compositing" sotto: **HTML/CSS+Playwright**, non PIL diretto.

## Cosa NON è ancora deciso

- Modello di diffusione specifico (SDXL vs Flux.1-dev vs SD3.5) — richiede confronto
  pratico in fase R&D
- Se questo sostituisce del tutto ChatGPT Web o resta un runtime alternativo (vedi
  `Docs/RUNTIMES.md`) mantenendo entrambi supportati
- Se e quando estendere il prototipo alle altre 9 pagine (P001, P003-P010)
- Nessuna versione SDK assegnata — resta in `ROADMAP.md` → Planned — Unscheduled finché
  non si decide di allocarci tempo
