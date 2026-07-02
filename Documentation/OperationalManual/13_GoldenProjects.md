# Capitolo 13 — GoldenProjects

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Proto Emperor README | `Projects/Proto_Emperor/README.md` | Descrizione del progetto di riferimento |
| Proto Emperor PROJECT.yaml | `Projects/Proto_Emperor/PROJECT.yaml` | Esempio compilato dello schema |
| Reference Models README | `Assets/ReferenceModels/Proto_Emperor/README.md` | Placeholder per immagini di riferimento fisiche |
| Approved Manual README | `Assets/ApprovedManual/Proto_Emperor/README.md` | Placeholder per il manuale approvato (non ancora esistente) |
| SDK Context | `SDK_CONTEXT.yaml` (sezione `golden_project`) | Dichiarazione ufficiale dello stato "reference" |

---

## 1. Cos'è un golden project

Un "golden project" è il progetto che l'SDK usa come riferimento strutturale ufficiale: non un esempio qualsiasi, ma quello contro cui ogni altro `PROJECT.yaml` va confrontato per capire quali campi sono richiesti, quale forma deve avere ogni sezione, e come appare un flusso di lavoro completo. `SDK_CONTEXT.yaml → golden_project` lo dichiara esplicitamente:

```yaml
golden_project:
  available: true
  name: "Proto_Emperor"
  path: "Projects/Proto_Emperor/"
  status: "reference"
  notes: "Use as structural reference for PROJECT.yaml layout and folder organization"
```

Lo stato `reference` implica un vincolo preciso: **Proto_Emperor non va modificato** per adattarlo a un nuovo progetto. Va copiato come punto di partenza, oppure semplicemente consultato mentre si compila un `PROJECT.yaml` nuovo.

---

## 2. Il progetto: Proto Emperor — Violet Phantom

Proto Emperor è uno chassis Mini4WD con layout motore anteriore-centrale e styling aerodinamico aggressivo. Lo schema colore dimostrativo, "Violet Phantom", usa una base viola profonda con accenti metallizzati argento e dettagli in nero metallico. Una variante premium ("Violet Phantom Pearl Edition", topcoat perlato) è inclusa come pagina `P009` opzionale.

Il progetto è stato scelto come riferimento perché copre deliberatamente l'intera superficie dello schema `PROJECT.yaml`:

- Schema colore multi-tinta (4 colori: `C001`–`C004`)
- Tutte e 10 le pagine (`P001`–`P010`), inclusa la variante premium `P009`
- `PROJECT.yaml` completo, nessun campo vuoto
- Sequenza di preparazione e verniciatura realistica, con tempi di asciugatura, avvertenze e suggerimenti per ogni step

---

## 3. Come usarlo come riferimento

`Projects/Proto_Emperor/README.md` § How to Use This as a Reference indica il flusso previsto:

1. Studiare `PROJECT.yaml` per capire come compilare la configurazione del proprio progetto
2. Confrontarlo con `Templates/PROJECT.yaml` per distinguere i campi obbligatori da quelli opzionali
3. Eseguire i prompt di `PromptEngine/` contro questo `PROJECT.yaml` per generare pagine di esempio
4. Usare le pagine generate come riferimento visivo di cosa produce un manuale generato correttamente

Un dettaglio strutturale utile: i campi `preparationSteps`, `paintSequence`, `maskingZones` e `detailAreas` in `Projects/Proto_Emperor/PROJECT.yaml` mostrano il livello di granularità atteso per ogni voce (durata, attrezzi, avvertenza, suggerimento) — informazione che `Templates/PROJECT.yaml` da solo, con i suoi commenti inline, non rende altrettanto concreta.

---

## 4. Stato di completamento reale (importante)

> ⚠️ **Warning:** nonostante sia il progetto di riferimento ufficiale, Proto Emperor **non ha ancora contenuti generati**. Verifica diretta della struttura:

```text
Projects/Proto_Emperor/
├── PROJECT.yaml       ✓ presente e compilato
├── README.md          ✓ presente
├── Images/             (vuota — nessun render)
├── Output/raw/         (vuota)
├── Notes/               (vuota)
└── ApprovedText/raw/   (vuota)
```

`Projects/Proto_Emperor/README.md` § Project Structure dichiara con segni di spunta (✓) anche `PROJECT.md`, `CHECKLIST.md`, `COLOR_SCHEME.yaml` e `PDF_CONFIG.yaml` come "Filled" — **questi quattro file non esistono nella directory**. Solo `PROJECT.yaml` e `README.md` sono realmente presenti. Trattare quella tabella nel README come descrizione dell'intento originale del progetto esempio, non come inventario accurato dello stato attuale.

Questo è coerente con `STATUS.md` § TODO:

| ID | Descrizione | Priorità | Target |
|----|-------------|----------|--------|
| TODO-007 | Populate `ApprovedAssets/Text/` for Proto_Emperor project | High | Active |
| TODO-008 | Populate `ApprovedAssets/Images/` for Proto_Emperor project | High | Active |

Coerentemente, `Assets/ReferenceModels/Proto_Emperor/README.md` dichiara ogni immagine di riferimento come `MISSING — placeholder`, e `Assets/ApprovedManual/Proto_Emperor/README.md` è esplicitamente uno stato "Placeholder (no approved manual yet)" — nessun file `.png` o `.pdf` esiste ancora in quella cartella, e la tabella "Approved Manuals Index" in `Assets/ApprovedManual/README.md` mostra solo una riga segnaposto per Proto Emperor senza versione né data.

**In sintesi:** Proto Emperor è un riferimento *strutturale* completo (`PROJECT.yaml` è un esempio a tutti gli effetti utilizzabile) ma un riferimento *visivo/produttivo* ancora vuoto. Chi lo usa per generare pagine di prova sta effettivamente producendo per primo il contenuto che TODO-007/TODO-008 richiedono.

---

## 5. Cosa NON fare con il golden project

- Non modificare `Projects/Proto_Emperor/PROJECT.yaml` per adattarlo al proprio modello — copiarlo con un nuovo nome di cartella
- Non trattare le immagini placeholder in `Assets/ReferenceModels/Proto_Emperor/` come riferimenti reali — sostituirle con fotografia con licenza propria prima di generare render per un progetto diverso
- Non presumere che esista un manuale approvato di Proto Emperor da consultare come esempio visivo finale — non esiste ancora (§4)

---

## Vedi anche

- Capitolo 06 — ProjectYaml (schema completo, Proto Emperor come esempio compilato)
- Capitolo 09 — ApprovedAssets (TODO-007/008 riguardano proprio questo layer)
- Capitolo 12 — PDF (Assets/ApprovedManual/Proto_Emperor/ è ancora vuoto)
- Capitolo 14 — Roadmap (stato dei TODO aperti)
