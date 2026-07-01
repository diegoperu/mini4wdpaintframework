# ApprovedAssets/Components/

Snapshot approvati dei componenti UI usati nelle pagine del manuale. Uso editoriale — non per il rendering finale.

## Scopo

Questa directory raccoglie export visivi dei componenti (C001-C015) nello stato approvato, per riferimento durante la review editoriale. Non sostituisce le definizioni normative in `Core/COMPONENT_SYSTEM.md`.

## Struttura

```
Components/
└── {component_id}/        # e.g. C001/, C011/
    ├── preview_v{n}.png   # Snapshot visivo del componente
    ├── spec.yaml          # Override locali (se applicabile)
    └── notes.md           # Note di review
```

## Componenti (C001-C015)

| ID | Nome | Pagine |
|----|------|--------|
| C001 | Header | Tutte |
| C002 | Footer | Tutte |
| C003 | Palette Strip | P002 |
| C004 | Materials Table | P003 |
| C005 | Step Sequence | P005 |
| C006 | Callout Box | P002, P006, P009 |
| C007 | Exploded View | P004 |
| C008 | Warning Box | P003-P009 |
| C009 | Tip Box | P003-P010 |
| C010 | Color Block Grid | P002 |
| C011 | Paint Code Box | P002, P005, P007 |
| C012 | Zoom Panel | P006, P007, P008 |
| C013 | Step Number Badge | P004-P008 |
| C014 | Timer Badge | P004, P005 |
| C015 | Notes Panel | P007-P010 |

## Riferimento normativo
- `Core/COMPONENT_SYSTEM.md` — definizione completa di ogni componente
- `Assets/DesignSystem/Tokens/tokens.example.yaml` — valori di design
