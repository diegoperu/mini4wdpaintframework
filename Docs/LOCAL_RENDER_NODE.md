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

## Cosa NON è ancora deciso

- Modello di diffusione specifico (SDXL vs Flux.1-dev vs SD3.5) — richiede confronto
  pratico in fase R&D
- Se il compositing usi HTML/CSS+Playwright o PIL diretto
- Se questo sostituisce del tutto ChatGPT Web o resta un runtime alternativo (vedi
  `Docs/RUNTIMES.md`) mantenendo entrambi supportati
- Nessuna versione SDK assegnata — resta in `ROADMAP.md` → Planned — Unscheduled finché
  non si decide di allocarci tempo
