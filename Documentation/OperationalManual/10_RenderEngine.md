# Capitolo 10 — Render Engine

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Specifica render | `Core/RENDER_GUIDE.md` | Source of truth — angoli, illuminazione, risoluzione, template prompt |
| Configurazione runtime | `Config/render.yaml` | Valori numerici che codificano RENDER_GUIDE.md — deve restare sincronizzato |

## Cos'è e perché esiste

Il Render Engine genera l'illustrazione visiva di ogni pagina a partire da `content.yaml` sigillato (Capitolo 09). Non genera mai testo, non modifica mai il testo ricevuto: lo colloca verbatim nei componenti corretti (`Core/TEXT_ENGINE.md §Render Engine Contract`). Lo SDK stesso non genera immagini — specifica come devono apparire e fornisce template di prompt AI model-agnostici; la generazione effettiva usa un modello di immagini AI o software di rendering 3D separato (`Core/RENDER_GUIDE.md §1`).

> ⚠️ **Avvertenza:** il Render Engine non deve mai essere invocato con contenuto non validato. Il contratto v2.4.0 richiede `metadata.yaml §approved == true` e preferibilmente `§locked == true` prima di leggere un `content.yaml`. Se il parsing di content.yaml fallisce, il fallback è `text.md` (con log di errore) — non torna mai a leggere `PROJECT.yaml` direttamente.

## Angoli di ripresa richiesti per pagina

| Pagina | Angolo |
|--------|--------|
| P001 Cover | 3/4 anteriore-sinistra, elevazione 15° |
| P002 ColorScheme | Tre viste ortografiche pure (front 0°, side 90°, top 90° elevazione) — nessuna distorsione prospettica |
| P004 Preparation | 3/4 anteriore-sinistra o laterale, elevazione 0° |
| P005 Painting | Stesso angolo della cover per il render finale |
| P006 Masking | Vista dall'alto ortografica + dettagli a 45° |
| P007 Details | 45° elevazione, il dettaglio deve riempire almeno il 40% del frame |
| P008 Decals | Laterale o dall'alto, quasi ortografico |
| P009 Premium | Confronto side-by-side, stesso angolo per entrambe le varianti |

> ⚠️ **Avvertenza:** le proiezioni ortografiche (P002, vista dall'alto P006) non ammettono alcuna distorsione prospettica — va usata modalità camera ortografica, non prospettica. Un render prospettico "sembra sbagliato" in un layout a tre viste anche quando l'angolo appare simile (`Core/RENDER_GUIDE.md §2`).

## Illuminazione

Tre rig definiti, mai mescolati all'interno dello stesso manuale (QA-041):

| Rig | Rapporto key:fill | Uso |
|-----|---------------------|-----|
| Studio Neutral | 3:1 | Default — P001, P002, P003, schemi metallici/multicolore |
| Drama | 10:1 (quasi buio) | Cover ad alto impatto, non adatto a pagine tecniche a tre viste |
| Detail | 2:1, nessun rim | Render ravvicinati (C012 Zoom), massimizza la leggibilità della texture |

## Risoluzione minima

| Caso d'uso | Risoluzione | DPI |
|------------|-------------|-----|
| Cover (P001) | 2480×3508px | 300 |
| Pagina corpo intera | 1240×1754px | 150 |
| Tre viste (ciascuna) | 800×600px min | 96 min |
| Dettaglio/zoom (C012) | 800×800px | 150 |
| Confronto (P009, per lato) | 1240×620px | 150 |

Un render sotto la soglia minima è un fallimento QA (`QA-016`–`QA-020`), non un'eccezione accettabile.

## Sfondo: regola assoluta

Sempre bianco puro `#FFFFFF` o trasparente (canale alpha). Mai grigio, mai gradiente, mai sfondo ambientale, mai bokeh, mai ombre "cotte" nel render (le ombre si aggiungono a livello di layout, non nel render stesso). `Config/render.yaml → quality.reject_colored_background: true` — qualunque sfondo non bianco è un rigetto automatico, con tolleranza `max_background_rgb_deviation: 5` dal bianco puro.

## Checklist di qualità pre-accettazione

Da `Core/RENDER_GUIDE.md §7`, applicabile a ogni render prima dell'uso in pagina:

- Sfondo bianco puro o trasparente
- Angolo conforme alla pagina (§2 sopra)
- Rig di illuminazione conforme al manuale (§3 sopra)
- Risoluzione minima rispettata
- Nessun artefatto di generazione AI, nessun motion blur
- Forma del corpo riconoscibile come il modello Mini4WD corretto
- Finitura vernice rappresenta accuratamente `paintScheme.style`
- Bilanciamento del bianco neutro, nessuna dominante di colore

## Errori comuni

| Errore | Conseguenza | Fix |
|--------|-------------|-----|
| Sfondo grigio/gradiente | Rigetto automatico QA | Rigenerare con sfondo bianco puro |
| Angolo prospettico su pagina ortografica | Layout "sbagliato" anche se visivamente simile | Usare camera ortografica esplicitamente |
| Mescolare rig di illuminazione nello stesso manuale | QA-041 fallita | Un solo rig per manuale, coerente su tutte le pagine |
| Risoluzione sotto soglia "sembra ok a schermo" | Fallisce in stampa | Verificare sempre contro `Config/render.yaml → resolution` |

## Vedi anche

- Capitolo 07 — TextEngine (fornisce il content.yaml sigillato che il Render Engine legge)
- Capitolo 08 — Assets (Design Tokens e Component System applicati durante il rendering)
- Capitolo 12 — PDF (fase successiva: assemblaggio delle pagine renderizzate)
