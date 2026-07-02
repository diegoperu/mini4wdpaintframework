# Capitolo 09 — ApprovedAssets (Livello CMS)

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| README del livello CMS | `ApprovedAssets/README.md` | Source of truth strutturale |
| Registro globale | `ApprovedAssets/index.yaml` | Stato del ciclo di vita di ogni pagina, ogni progetto |
| Criteri di completamento | `Core/DEFINITION_OF_DONE.md` | Definizione di "fatto" a livello pagina/manuale/framework |
| Template testo approvato | `Templates/APPROVED_TEXT.md` | Formato legacy (v2.3.0), mantenuto per compatibilità |

## Cos'è e perché esiste

`ApprovedAssets/` è il livello CMS introdotto nella v2.4.0, la CMS layer del changelog `documentation.cms_layer: "complete"` in `SDK_CONTEXT.yaml`. A differenza di `Projects/`, che è una cartella di lavoro, `ApprovedAssets/` contiene solo contenuto sigillato e approvato, pronto per il rendering e la pubblicazione. Supera (mantenendo compatibilità) `Projects/{ModelName}/ApprovedText/` della v2.3.0.

```
ApprovedAssets/
├── Text/P{NNN}/    ← un modulo per pagina, ID permanenti
├── Images/         ← render approvati
├── Components/     ← istanze di componenti approvate
├── Templates/      ← template di layout (struttura, zero contenuto)
├── References/     ← materiale sorgente
└── index.yaml      ← registro globale
```

## Il modulo pagina: 7 file

Ogni pagina in `ApprovedAssets/Text/P{NNN}/` è un modulo autocontenuto:

| File | Ruolo |
|------|-------|
| `content.yaml` | **PRIMARIO** — dati editoriali strutturati, source of truth |
| `text.md` | Derivato da content.yaml — solo per revisione umana, mai modificato direttamente |
| `metadata.yaml` | Stato del ciclo di vita, approvazione, versione |
| `manifest.yaml` | Componenti, immagini, token, dipendenze, `prompt_file` |
| `changelog.md` | Cronologia delle revisioni |
| `notes.md` | Annotazioni editoriali — non renderizzato |
| `README.md` | Documentazione del modulo |

Se `content.yaml` e `text.md` sono in disaccordo, vince sempre `content.yaml` — non è una linea guida, è la regola operativa esplicita in `Core/TEXT_ENGINE.md §text.md Generation`.

## Ciclo di vita della pagina

```
draft → review → approved → locked → rendered → released → archived
```

| Stato | content.yaml | Render Engine | Significato |
|-------|-------------|----------------|-------------|
| draft | Modificabile | Nessun accesso | Generazione iniziale, lavoro in corso |
| review | Modificabile (tracciato) | Nessun accesso | Sotto revisione editoriale |
| approved | Sigillato* | Accesso in lettura | Ha superato ContentValidation + TextValidation |
| locked | Immutabile | Accesso in lettura | Pronto per produzione, nessuna modifica ammessa |
| rendered | Immutabile | Riferimento read-only | Render generato da questa versione di contenuto |
| released | Immutabile | Riferimento read-only | Pubblicato nel PDF |
| archived | Immutabile | Nessun accesso | Superato da una versione più recente |

*Sigillato: per modificare serve resettare `metadata.yaml → approved: false` con una voce di changelog.

**Implicazione operativa per un'AI:** se `metadata.yaml → status: locked`, si va direttamente in Render Mode — non si rigenera `content.yaml`, non si modifica alcun file nel modulo. Se `status: draft`, si genera `content.yaml` via Text Engine, si esegue la QA, poi si sigilla prima del render (`AI_ENTRYPOINT.md §Approved Assets`).

## Stato attuale del registro (verificato 2026-07-02)

`ApprovedAssets/index.yaml` ha `pages: []`, `manuals: []`, `total_pages: 0` — il registro è vuoto. Questo è coerente con `STATUS.md → TODO-007` ("Populate ApprovedAssets/Text/ for Proto_Emperor project", priorità Alta, stato Active) e `TODO-008` (equivalente per Images/). Il Golden Project Proto_Emperor ha un `PROJECT.yaml` completo (Capitolo 13) ma non ha ancora contenuto sigillato in `ApprovedAssets/Text/P00x/` — è quindi un riferimento per la *struttura* del progetto, non un esempio completo del livello CMS in funzione.

## Riuso dei moduli

Un modulo P002 sigillato per "Proto Emperor v1" può essere copiato e adattato per un nuovo schema colore. Un modulo riusato deve aggiornare `metadata.yaml §revision`, `page.version` e `changelog.md`. Non si riusa mai direttamente un modulo `locked` — si copia sempre e si crea una nuova revisione (`Core/PAGE_SYSTEM.md §Reusability`).

## Errori comuni

| Errore | Conseguenza | Fix |
|--------|-------------|-----|
| Modificare un file in un modulo `locked` | Violazione del contratto di sigillo | Resettare a `approved: false`, loggare in changelog, poi modificare |
| Modificare `text.md` invece di `content.yaml` | La modifica va persa alla prossima rigenerazione derivata | Modificare sempre `content.yaml`, mai `text.md` |
| `approved: true` con `approved_by` vuoto | Fallisce `TEST-CV-004-F` | Compilare sempre `approved_by`/`approved_date` insieme ad `approved` |
| Confondere `ApprovedAssets/` con `Projects/{ModelName}/ApprovedText/` | Uso della pipeline v2.3.0 superata | Usare `ApprovedAssets/Text/P{NNN}/content.yaml` come output primario (v2.4.0) |

## Vedi anche

- Capitolo 07 — TextEngine (genera il content.yaml che questo capitolo ospita)
- Capitolo 10 — RenderEngine (consuma esclusivamente moduli approved/locked)
- Capitolo 11 — QA (Tests/ContentValidation.md valida ogni file del modulo)
