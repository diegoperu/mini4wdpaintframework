# ApprovedAssets/Images/

Immagini approvate per il rendering del manuale. Organizzate per modello e pagina.

## Struttura

```
Images/
└── {model_slug}/          # e.g. proto_emperor/
    ├── P001/
    │   └── cover_3q_v1.png
    ├── P002/
    │   ├── ortho_front_v1.png
    │   ├── ortho_side_v1.png
    │   └── ortho_top_v1.png
    ├── P006/
    │   └── masking_zoom_v1.png
    └── ...
```

## Convenzioni

- **Slug modello:** snake_case dal `project.modelName` in PROJECT.yaml
  - Esempio: "Proto Emperor" → `proto_emperor`
- **Nome file:** `{role}_v{n}.{ext}` — il numero versione incrementa ad ogni sostituzione
- **Formato:** PNG preferito. JPEG accettato per fotografie. SVG per diagrammi.
- **Risoluzione:**
  - Full-page renders: `2480×3508 px` (A4 a 300 DPI)
  - Zoom panels (C012): `800×800 px`
  - Comparison images (P009): `2480×3508 px`

## Stato approvazione

Ogni immagine deve essere referenziata nel `manifest.yaml` della pagina corrispondente con `approved: true` prima del rendering.

## Note
- Le immagini **non** sono incluse nel repository Git — troppo pesanti.
- Usare Git LFS oppure un asset host esterno (es. Google Drive, CDN).
- Il campo `file:` nel manifest.yaml deve contenere il path relativo dall'SDK root.
