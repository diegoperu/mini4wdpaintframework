# Capitolo 06 — PROJECT.yaml

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Template principale | `Templates/PROJECT.yaml` | Source of truth dello schema — copiare, mai modificare |
| Brief leggibile | `Templates/PROJECT.md` | Compagno umano di PROJECT.yaml |
| README dei template | `Templates/README.md` | Istruzioni di bootstrap progetto, campi required/optional |
| Checklist progresso | `Templates/CHECKLIST.md` | Traccia le 4 fasi di produzione per progetto |
| Schema colore esteso | `Templates/COLOR_SCHEME.yaml` | Metadati colore completi (RGB, CMYK, Pantone) |
| Template testo approvato | `Templates/APPROVED_TEXT.md` | Frontmatter e struttura per l'output editoriale |
| Guida nuovo progetto | `Projects/PROJECT_BOOTSTRAP.md` | Procedura passo-passo per avviare un progetto |
| README di Projects/ | `Projects/README.md` | Convenzioni cartella progetto, ciclo di vita |
| Esempio compilato | `Projects/Proto_Emperor/PROJECT.yaml` | Golden Project — riferimento reale, non modificabile |
| README del Golden Project | `Projects/Proto_Emperor/README.md` | Come usare Proto Emperor come riferimento |

## Cos'è e perché esiste

`PROJECT.yaml` è l'unica fonte dei dati specifici di un progetto: nome del modello, schema colori, materiali, sequenza di verniciatura, mascherature, dettagli, decalcomanie, variante premium, percorsi dei render. Ogni prompt in `PromptEngine/` e ogni pagina generata dipendono da questo file — mai il contrario. Lo SDK stesso (Core/, PromptEngine/, Templates/) non contiene alcun dato specifico di modello: questa separazione (`Core/DESIGN_LANGUAGE.md` Rule 8) è ciò che permette allo SDK di essere versionato indipendentemente da ogni singolo manuale.

## Schema canonico

Lo schema reale — verificato leggendo `Templates/PROJECT.yaml` e confermato da `Projects/Proto_Emperor/PROJECT.yaml` — è organizzato in blocchi top-level:

```yaml
sdk_version: "2.4.0"          # deve combaciare con VERSION

project:
  modelName: "Proto Emperor"   # nome ufficiale Tamiya
  modelSlug: "proto-emperor"   # kebab-case per naming file
  seriesName: "Championship Series"
  year: "2024"
  language: "it"
  version: "1.0.0"             # versione del manuale, non dello SDK
  author: "Studio Mini4WD"
  createdAt: "2024-01-15"
  updatedAt: "2024-01-15"

paintScheme:
  name: "Violet Phantom"
  description: "..."
  colors:
    - id: "C001"
      name: "Body Base"
      paintBrand: "Tamiya"
      paintCode: "TS-57"
      paintName: "Blue Violet"
      hex: "#4B3A8C"
      finish: "gloss"
  colorNotes: "..."

materials: { paints: [], tools: [...], consumables: [...] }
preparationSteps: [...]
paintSequence: [...]
maskingZones: [...]
detailAreas: [...]
decals: [...]
premiumVariant: { enabled: false, ... }

paths:
  coverRenderPath: "Images/cover_3q.png"
  colorSchemeRenderFront: "Images/P002_front.png"
  colorSchemeRenderSide: "Images/P002_side.png"
  colorSchemeRenderTop: "Images/P002_top.png"
  outputDir: "Output/"
  notesDir: "Notes/"

text: { language: "it", strict_language: true, ... }
qa: { status: "draft", ... }
```

Ogni campo in `Templates/PROJECT.yaml` è annotato `# REQUIRED` o `# OPTIONAL` inline. Un campo REQUIRED vuoto produce prompt con token `{{...}}` non risolti quando eseguiti — l'errore più comune segnalato in `Templates/README.md §Common Mistakes`.

> ⚠️ **Avvertenza:** i colori nello schema colore usano `id` in formato `C001`, `C002` — identico per pattern ai Component ID (`Core/COMPONENT_SYSTEM.md`) ma è una coincidenza di namespace, non lo stesso registro. Un `colors[].id: "C001"` in PROJECT.yaml non ha alcuna relazione con il componente `C001 Header`.

## Come si avvia un nuovo progetto

1. Crea la cartella: `Projects/{ModelName}/` in PascalCase con underscore (`Core/NAMING_CONVENTION.md §3.1`) — es. `Proto_Emperor`.
2. Copia `Templates/PROJECT.yaml`, `PROJECT.md`, `CHECKLIST.md`, `COLOR_SCHEME.yaml` nella nuova cartella.
3. Compila ogni campo REQUIRED. Per valori sconosciuti usa `TODO:` — non inventare mai dati (regola G04 in `AI_ENTRYPOINT.md`).
4. Crea `Images/`, `Output/raw/`, `Notes/` secondo `Projects/README.md §Project Folder Structure`.
5. Procedi con `Core/WORKFLOW.md` per la pipeline di generazione completa.

Guida dettagliata passo-passo: `Projects/PROJECT_BOOTSTRAP.md`.

## La regola più importante: mai modificare in place

`Templates/PROJECT.yaml` non si modifica mai direttamente — si copia. Questo è esplicito sia in `Templates/README.md §Purpose` ("Templates are never edited in place") sia nel Bootstrap Contract di `AI_ENTRYPOINT.md` (`rules.never_modify_project_yaml: true`, riferito al PROJECT.yaml di un progetto attivo una volta sigillato). Un'AI che opera su questo framework non deve mai proporre di modificare `Templates/PROJECT.yaml` per "semplificare" un progetto specifico: la modifica va fatta solo sulla copia in `Projects/{ModelName}/`.

## Errori comuni

| Errore | Conseguenza | Fix |
|--------|-------------|-----|
| Modificare il template invece della copia | Tutti i progetti futuri partono con valori sbagliati | Copiare sempre, mai compilare l'originale |
| Campi REQUIRED lasciati vuoti | Token non risolti nelle pagine generate | Verificare tutti i REQUIRED prima di eseguire i prompt |
| `sdk_version` non allineato a `VERSION` | Mismatch di schema, errori nei token | Allineare `sdk_version` alla versione corrente dello SDK |
| `modelSlug` in formato sbagliato | Errori di naming dei file | Deve essere kebab-case: `proto-emperor`, non `Proto Emperor` |
| `premiumVariant.enabled: true` senza compilare i campi premium | P009 generata vuota | Compilare sempre `premiumVariant.name` e `specialTechniques` se abilitato |

## ⚠️ Incoerenza rilevata nella documentazione SDK

Lo schema di `PROJECT.yaml` documentato sopra (verificato su `Templates/PROJECT.yaml` e `Projects/Proto_Emperor/PROJECT.yaml`, che concordano tra loro) **non corrisponde** agli esempi mostrati in altri due documenti del framework:

- `Core/MANUAL_SYSTEM.md §5` mostra uno schema piatto (`sdkVersion`, `modelName`, `manufacturer`, `renders.cover`) senza il blocco `project:` annidato e senza array `paintScheme.colors[]`.
- `Projects/PROJECT_BOOTSTRAP.md §Step 2` mostra un terzo schema ancora diverso (`project.series`, `project.scale`, `paint_scheme.primary_color.tamiya_code`, `reference_images:` top-level).

Nessuno dei due esempi è eseguibile contro lo schema reale. Questo capitolo documenta lo schema **canonico** (quello di `Templates/PROJECT.yaml`, confermato dal Golden Project). Il maintainer dello SDK dovrebbe correggere gli esempi in `Core/MANUAL_SYSTEM.md` e `Projects/PROJECT_BOOTSTRAP.md` per farli concordare — vedi `Validation/CONSISTENCY_CHECK.md` per il controllo di follow-up.

## Vedi anche

- Capitolo 07 — TextEngine (consuma i campi di PROJECT.yaml per generare `content.yaml`)
- Capitolo 08 — Assets (`paintScheme.colors[].hex` alimenta i design token di rendering)
- Capitolo 13 — GoldenProjects (Proto_Emperor come riferimento strutturale)
- Capitolo 15 — Versioning (`sdk_version` e `project.version` seguono regole SemVer distinte)
