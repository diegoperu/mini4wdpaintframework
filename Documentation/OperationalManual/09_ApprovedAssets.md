# Capitolo 09 — Moduli Pagina Approvati (per progetto)

> ⚠️ **Riscritto 2026-07-07.** `ApprovedAssets/` (livello CMS globale, v2.4.0) è
> stato **rimosso in v2.5.0**, sostituito dalla struttura per-progetto descritta
> qui sotto. Se trovi ancora riferimenti ad `ApprovedAssets/Text/`,
> `ApprovedAssets/Images/` o `ApprovedAssets/index.yaml` in altri documenti, sono
> residui non aggiornati — vedi `Documentation/QualityManagement/07_KNOWN_ISSUES.md`
> KI-004. La struttura reale è `Projects/{Model}/{Variant}/ApprovedText/`.

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Panoramica cartella progetto | `Projects/README.md` | Source of truth strutturale |
| Criteri di completamento | `Core/DEFINITION_OF_DONE.md` | Definizione di "fatto" a livello pagina/manuale/framework |
| Convenzione path immagini | `Scripts/render_page.py` → `image_slots()` | Path esatto per ogni slot illustrazione |

## Cos'è e perché esiste

Ogni pagina di un progetto vive come modulo autocontenuto dentro
`Projects/{Model}/{Variant}/ApprovedText/P{NNN}/` — non più in una cartella CMS
globale condivisa tra progetti, ma isolata per variante. Due varianti dello stesso
modello (es. `Proto_Emperor/Violet_Phantom/` e `Proto_Emperor/Midnight_Blue/`)
coesistono come cartelle sorelle senza conflitto, ognuna col proprio set completo
di pagine.

```
Projects/{Model}/{Variant}/
├── PROJECT.yaml              ← configurazione progetto, incl. paintScheme.colors[]
├── ApprovedText/P{NNN}/      ← un modulo per pagina, ID permanenti
├── Images/                   ← foto di riferimento (ref_*.jpg) E illustrazioni
│                                generate (cover_3q.png, P002_front.png, ecc.) —
│                                stessa cartella, non separate come in v2.4.0
├── MISSING_IMAGES.md          ← generato da Scripts/render_page.py
├── MISSING_IMAGES_PROMPT.md   ← generato da Scripts/render_page.py
└── MISSING_IMAGES.json        ← generato da Scripts/render_page.py
```

## Il modulo pagina: 7 file

Ogni pagina in `ApprovedText/P{NNN}/` è un modulo autocontenuto — stessi 7 file
della v2.4.0, solo percorso diverso:

| File | Ruolo |
|------|-------|
| `content.yaml` | **PRIMARIO** — dati editoriali strutturati, source of truth |
| `text.md` | Derivato da content.yaml — solo per revisione umana, mai modificato direttamente |
| `metadata.yaml` | Stato del ciclo di vita, approvazione, versione |
| `manifest.yaml` | Componenti, immagini, token, dipendenze |
| `changelog.md` | Cronologia delle revisioni |
| `notes.md` | Annotazioni editoriali — non renderizzato |
| `README.md` | Documentazione del modulo |

Se `content.yaml` e `text.md` sono in disaccordo, vince sempre `content.yaml` — non
è una linea guida, è la regola operativa esplicita in `Core/TEXT_ENGINE.md §text.md
Generation`.

## Ciclo di vita della pagina

```
draft → review → approved → locked → rendered → released → archived
```

| Stato | content.yaml | Template (`render_page.py`) | Significato |
|-------|-------------|----------------|-------------|
| draft | Modificabile | Nessun accesso | Generazione iniziale, lavoro in corso |
| review | Modificabile (tracciato) | Nessun accesso | Sotto revisione editoriale |
| approved | Sigillato* | Accesso in lettura | Ha superato ContentValidation + TextValidation |
| locked | Immutabile | Accesso in lettura | Pronto per produzione, nessuna modifica ammessa |
| rendered | Immutabile | Riferimento read-only | Pagina generata (testo dal template, illustrazione se presente in Images/) |
| released | Immutabile | Riferimento read-only | Pubblicato nel PDF |
| archived | Immutabile | Nessun accesso | Superato da una versione più recente |

*Sigillato: per modificare serve resettare `metadata.yaml → approved: false` con una
voce di changelog.

**Implicazione operativa per un'AI:** se `metadata.yaml → status: locked`,
`Scripts/render_page.py` genera la pagina direttamente da `content.yaml` — nessuna
AI coinvolta in questo passo. Se `status: draft`, si genera `content.yaml` via Text
Engine, si esegue la QA, poi si sigilla prima di lanciare il template
(`AI_ENTRYPOINT.md §Approved Assets`).

## Registro globale — non ancora implementato

`AI_ENTRYPOINT.md` menziona un `Projects/{Model}/{Variant}/index.yaml` per il
tracciamento dello stato `released` (Golden Rule / Fase 7). **Non esiste ancora come
file reale** in nessun progetto di test (verificato 2026-07-07,
`Magnum_Saber_Premium/Cotton_Candy_Drift`) — è una funzionalità dichiarata ma non
implementata. Se ti serve lo stato di ogni pagina oggi, usa
`Scripts/render_page.py {Model} {Variant}` (rigenera `MISSING_IMAGES.md`) insieme a
un controllo manuale dei `metadata.yaml` di ogni pagina.

## Riuso dei moduli

Un modulo P002 sigillato per una variante può essere copiato e adattato per un
nuovo schema colore (nuova variante dello stesso modello, o modello diverso). Un
modulo riusato deve aggiornare `metadata.yaml §revision`, `page.version` e
`changelog.md`. Non si riusa mai direttamente un modulo `locked` — si copia sempre
e si crea una nuova revisione (`Core/PAGE_SYSTEM.md §Reusability`).

## Errori comuni

| Errore | Conseguenza | Fix |
|--------|-------------|-----|
| Modificare un file in un modulo `locked` | Violazione del contratto di sigillo | Resettare a `approved: false`, loggare in changelog, poi modificare |
| Modificare `text.md` invece di `content.yaml` | La modifica va persa alla prossima rigenerazione derivata | Modificare sempre `content.yaml`, mai `text.md` |
| `approved: true` con `approved_by` vuoto | Fallisce `TEST-CV-004-F` | Compilare sempre `approved_by`/`approved_date` insieme ad `approved` |
| Cercare `ApprovedAssets/` (v2.4.0, rimossa) | Cartella non esiste più | Usare `Projects/{Model}/{Variant}/ApprovedText/P{NNN}/content.yaml` |
| Aspettarsi `ApprovedImages/P{NNN}/` per le illustrazioni | Cartella non usata da `render_page.py` | Le illustrazioni vanno in `Projects/{Model}/{Variant}/Images/` insieme alle foto reference, path esatto per `Scripts/render_page.py` → `image_slots()` |

## Vedi anche

- Capitolo 07 — TextEngine (genera il content.yaml che questo capitolo ospita)
- Capitolo 10 — RenderEngine (consuma esclusivamente moduli approved/locked)
- Capitolo 11 — QA (Tests/ContentValidation.md valida ogni file del modulo)
- `FIRST_RENDER.md` — tutorial passo-passo aggiornato al flusso attuale
