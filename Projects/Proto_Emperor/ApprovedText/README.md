# ApprovedText — Proto Emperor

**Project:** Proto Emperor
**SDK Version:** 2.4.0
**Status:** Vuoto (progetto di esempio — testo non ancora generato)

## Scopo

Questa directory contiene il testo approvato per ciascuna pagina del manuale Proto Emperor. Il testo è generato dal Text Engine (vedi `Core/TEXT_ENGINE.md`), validato tramite `Tests/TextValidation.md`, e approvato prima di essere consegnato al Render Engine.

Il Render Engine legge esclusivamente da questa directory. Non genera testo autonomamente.

## Contenuto atteso

| File | Pagina | Stato |
|------|--------|-------|
| `P001.md` | Copertina | In attesa |
| `P002.md` | Schema Colori | In attesa |
| `P003.md` | Materiali | In attesa |
| `P004.md` | Preparazione | In attesa |
| `P005.md` | Verniciatura | In attesa |
| `P006.md` | Mascheratura | In attesa |
| `P007.md` | Dettagli | In attesa |
| `P008.md` | Decalcomanie | In attesa |
| `P009.md` | Variante Premium | In attesa |
| `P010.md` | Lista di Controllo Finale | In attesa |

## Struttura directory

```
ApprovedText/
├── README.md          ← questo file
├── raw/               ← output grezzo AI, prima della QA
│   ├── P001_raw.md
│   ├── P002_raw.md
│   └── ...
├── P001.md            ← approvato (approved: true)
├── P002.md
└── ...
```

## Workflow

1. Eseguire `PromptEngine/{NomePagina}.md` con la sequenza LOAD completa
2. Salvare l'output grezzo in `raw/P{NNN}_raw.md`
3. Eseguire `Tests/TextValidation.md` sull'output grezzo
4. Correggere i blocchi ❌, ripetere se necessario
5. Impostare `approved: true` nel frontmatter YAML
6. Salvare il file approvato come `P{NNN}.md`
7. Procedere alla fase Render Engine

## Regole

- Solo testo italiano (vedi `Config/LANGUAGE_POLICY.yaml`)
- Nessun testo fittizio, lorem ipsum, kanji, hiragana, katakana
- Tutti i `{{token}}` devono essere risolti prima dell'approvazione
- Il campo `approved_by` deve contenere il nome del revisore
- I file in `raw/` non sono mai consegnati al Render Engine

## Documenti correlati

- `Core/TEXT_ENGINE.md`
- `Config/LANGUAGE_POLICY.yaml`
- `Tests/TextValidation.md`
- `Templates/APPROVED_TEXT.md`
- `Build/Pipeline.md §Phase 2`
