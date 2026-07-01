# ApprovedAssets/References/

Materiali di riferimento approvati per la produzione del manuale: campioni di colore, schede tecniche, foto di riferimento.

## Struttura

```
References/
└── {model_slug}/
    ├── paint_samples/         # Foto campioni colore Tamiya approvati
    ├── technical_sheets/      # Schede tecniche (PDF Tamiya, se disponibili)
    └── inspiration/           # Foto di riferimento per il rendering
```

## Tipi di materiale

### Campioni colore
Foto dei colori Tamiya reali, usate per calibrare i valori hex nelle palette e verificare la fedeltà cromatica dei render.

### Schede tecniche
PDF ufficiali Tamiya con specifiche vernice: tempo di asciugatura, diluizione, compatibilità.

### Ispirazioni di rendering
Foto di modelli verniciati di riferimento (non necessariamente lo stesso modello) usate come input per i prompt di rendering AI.

## Note
- I materiali di riferimento **non** sono inclusi nel repository Git.
- File di grandi dimensioni: usare Git LFS o storage esterno.
- Aggiornare `ApprovedAssets/index.yaml` quando si aggiungono nuovi riferimenti.

## Riferimento normativo
- `Projects/{project_slug}/PROJECT.yaml` — codici colore Tamiya autorizzati
- `Knowledge/GlossaryIT.md` — terminologia italiana per i nomi colore
