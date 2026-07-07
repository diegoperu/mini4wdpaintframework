# FIRST_RENDER.md — Tutorial: da Approved Text alla Prima Pagina Illustrata

**Mini4WD Manual SDK v2.5.5** · Tutorial operatore · Tempo: pochi minuti per pagina
(più il tempo di generare le illustrazioni mancanti — vedi PASSO 3)

> ⚠️ **Riscritto 2026-07-07.** Fino al 2026-07-06 questo tutorial chiedeva di
> generare l'intera pagina (testo, tabelle, layout, illustrazione) via ChatGPT in un
> solo turno. Test estesi hanno mostrato che un modello generativo non può
> garantire fedeltà di testo/tabelle dentro un'immagine generata — vedi
> `Docs/LOCAL_RENDER_NODE.md` per l'evidenza completa. Il layout e il testo di ogni
> pagina sono ora prodotti da un template deterministico (`Scripts/render_page.py`);
> un'AI generativa serve solo per le illustrazioni isolate (copertina, viste
> ortogonali, foto di dettaglio).

> Da dove parti: tutte le pagine con `metadata.yaml → status: locked`
> (testo generato e validato — vedi `FIRST_PROJECT.md` e `OperatorGuide/01_Primo_Manuale.md`).
> Dove arrivi: tutte le pagine renderizzate, pronte per l'assemblaggio PDF (`FIRST_PDF.md`).

---

## PASSO 1 — Verifica il punto di partenza

Controlla che ogni pagina abbia `status: "locked"`:

```bash
grep -r "status:" Projects/{Modello}/{Variante}/ApprovedText/*/metadata.yaml
```

Se qualche pagina non è `locked`, fermati: il template legge solo contenuto
sigillato (Golden Rule G08). Torna alla fase QA testi.

## PASSO 2 — Genera tutte le pagine con il template

```bash
pip install -r Scripts/requirements.txt   # una tantum
playwright install chromium                # una tantum

Scripts/render_page.py {Modello} {Variante}
```

Un solo comando per l'intero progetto — nessuna chat, nessun prompt, nessuna AI
coinvolta in questo passo. Genera `Build/Preview/{Modello}_{Variante}_{PageID}.png`
per ogni pagina e scrive, dentro `Projects/{Modello}/{Variante}/`:
- `MISSING_IMAGES.md` — elenco di tutte le immagini ancora mancanti
- `MISSING_IMAGES_PROMPT.md` — per ciascuna, il prompt già pronto da copiare + i
  file da allegare
- `MISSING_IMAGES.json` — stessi dati in forma strutturata (uso futuro: nodo locale)

Se `MISSING_IMAGES.md` dice "nessuna immagine mancante", **tutte le pagine sono già
complete** — salta al PASSO 4.

## PASSO 3 — Genera le illustrazioni mancanti (una alla volta)

> 🛑 **Una chat = una immagine.** Riusare la stessa chat tra una generazione e
> l'altra contamina il risultato successivo col contesto della precedente
> (verificato empiricamente). Chat nuova per ogni illustrazione, zero eccezioni.

Prepara il pacchetto (una volta per progetto, riusabile per tutte le illustrazioni
mancanti):

```bash
Scripts/package_handoff.sh {Modello} {Variante}
```

Produce uno ZIP in `Projects/{Modello}/{Variante}/{Modello}_{Variante}_{timestamp}.zip`
con solo gli stili (`Core/RENDER_GUIDE.md`, `DESIGN_LANGUAGE.md`, `STYLE_GUIDE.md`),
lo schema colori (`PROJECT.yaml`) e le foto di riferimento — niente testo/layout,
l'AI non lo tocca più.

Per ciascuno slot in `MISSING_IMAGES_PROMPT.md`:
1. Apri **ChatGPT Web** (usa **"Thinking"**, non **"Pro"**) o **Gemini**, chat nuova
2. Carica lo ZIP + le foto di riferimento come allegati immagine diretti
3. Copia il blocco prompt di quello slot da `MISSING_IMAGES_PROMPT.md` — è già
   compilato con schema colori e descrizione, niente da riempire a mano
4. Salva l'immagine ricevuta **esattamente** al path indicato nel blocco (es.
   `Projects/{Modello}/{Variante}/Images/P002_front.png`)

Cosa deve fare l'AI (e cosa NON deve fare):

| Deve | Non deve |
|---|---|
| Generare SOLO l'illustrazione isolata | Aggiungere testo, tabelle, loghi, pannelli |
| Riprodurre la forma del modello dalle foto | Modificare forma o proporzioni |
| Usare i colori da `PROJECT.yaml → colors[]` | Copiare la livrea box-art delle foto reference |
| Sfondo bianco puro | Aggiungere grafiche non previste dallo schema colori |

## PASSO 4 — Conferma l'aggancio e ripeti

Rilancia il PASSO 2 (`Scripts/render_page.py {Modello} {Variante}`): ogni slot
salvato correttamente sparisce da `MISSING_IMAGES.md`. Ripeti il PASSO 3 per gli
slot rimanenti, finché il report è vuoto.

## PASSO 5 — Verifica visiva rapida

Apri i PNG in `Build/Preview/` (o il PDF, vedi `FIRST_PDF.md`) e controlla:

- [ ] Il testo su ogni pagina corrisponde a content.yaml (non serve verificarlo,
  lo garantisce il template — controlla solo che non manchi un'illustrazione)
- [ ] Sfondo bianco puro, pannello header viola
- [ ] Il modello nelle illustrazioni somiglia alle foto di riferimento (forma)
- [ ] I colori nelle illustrazioni corrispondono allo schema del progetto, non
  alla livrea box-art delle foto

## PASSO 6 — Problema su un'illustrazione?

- **Problema visivo** (forma, colori sbagliati) → rigenera solo quello slot
  (PASSO 3), non serve toccare le altre pagine né il testo
- **Problema di testo** (refuso nel contenuto) → il testo è locked: si riapre la
  pagina con una riga in `changelog.md`, si corregge via Text Engine, si rifà QA e
  seal, poi si rilancia `render_page.py`. Vedi `LIFECYCLE.md`. Il template non va
  mai modificato per correggere un refuso di un singolo progetto.

## PASSO 7 — Registra l'esito

Aggiorna `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml` per ogni
pagina completata:

```yaml
status: "rendered"
rendered: true
rendered_date: "2026-07-07"
```

**→ Tutte le pagine renderizzate.** Prossimo passo: `FIRST_PDF.md`.
