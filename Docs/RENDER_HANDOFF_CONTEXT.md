# Contesto Handoff — Illustrazione singola (Fase 4)

Questo pacchetto contiene SOLO i file necessari per generare **una singola
illustrazione** del modellino Mini4WD (copertina, vista ortogonale, o foto di
dettaglio/mascheratura) — non una pagina intera di manuale.

> ⚠️ **Cambio di ruolo (2026-07-06).** Fino a questa data, questo pacchetto chiedeva
> di generare l'intera pagina (testo, tabelle, layout, illustrazione). Test estesi
> hanno mostrato che un modello generativo non può garantire fedeltà di testo/tabelle
> dentro un'immagine — vedi `Docs/LOCAL_RENDER_NODE.md` per l'evidenza completa. Il
> layout e il testo di ogni pagina sono ora prodotti da un template deterministico
> (`Scripts/render_page.py`) che legge `content.yaml` direttamente. Il tuo compito in
> questa chat è molto più piccolo e specifico.

## Il tuo ruolo in questa chat

Genera **direttamente**, usando lo strumento di generazione immagini disponibile in
questa interfaccia, **solo l'illustrazione richiesta** nel prossimo messaggio
dell'utente — un'immagine isolata su sfondo bianco, senza testo, senza tabelle,
senza loghi, senza pannelli colorati o header. Quell'immagine verrà inserita da un
template già pronto che aggiunge testo/tabelle/header per conto suo: se aggiungi tu
del testo o una cornice, il risultato finale avrà doppioni o elementi in conflitto
con il template.

## Cosa trovi in questo pacchetto

- `Core/RENDER_GUIDE.md`, `Core/DESIGN_LANGUAGE.md`, `Core/STYLE_GUIDE.md` — regole
  di stile fotografico/illuminazione (non layout di pagina — quello non ti riguarda)
- `Projects/{Model}/{Variant}/PROJECT.yaml` — dati del modello, incluso
  `paintScheme.colors[]` (fonte primaria per i colori, non modificare)
- `Projects/{Model}/{Variant}/Images/` — foto di riferimento del modello fisico reale
  (forma/sagoma). NON la palette colori: quella viene solo da
  `PROJECT.yaml → paintScheme.colors[]` — le foto reference sono quasi sempre
  box-art stock con uno schema colori diverso da quello da documentare

## Dopo la generazione

Non serve alcuna checklist QA testuale (niente più tabelle/hex da verificare a
parole — quelli li disegna il template dai dati, non tu). Basta confermare
visivamente che forma e colori corrispondano a quanto richiesto prima di consegnare
il file.
