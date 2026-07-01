# ApprovedAssets/Templates/

Template approvati per la generazione di contenuti. Versioni operative dei template in `Templates/` root.

## Scopo

Copie dei template attivi usati nella pipeline v2.4.0. Se un template root viene aggiornato, la versione approvata viene copiata qui dopo review.

## Struttura

```
Templates/
├── content.yaml.template     # Template base per content.yaml di ogni pagina
├── metadata.yaml.template    # Template base per metadata.yaml
├── manifest.yaml.template    # Template base per manifest.yaml
└── text.md.template          # Template base per text.md derivato
```

## Workflow

1. Template master aggiornato in `Templates/` root
2. Review editoriale del cambiamento
3. Copia approvata salvata qui con versione bump
4. Pipeline usa questa copia come sorgente

## Versioni template

| File | Versione | Data approvazione |
|------|----------|-------------------|
| content.yaml.template | 2.4.0 | — |
| metadata.yaml.template | 2.4.0 | — |
| manifest.yaml.template | 2.4.0 | — |
| text.md.template | 2.4.0 | — |

## Riferimento normativo
- `Templates/` — template master (sorgente)
- `Core/TEXT_ENGINE.md` — specifica output template
