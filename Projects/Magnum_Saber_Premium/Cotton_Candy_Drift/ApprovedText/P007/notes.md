# Notes — P007 Verniciatura dei Dettagli

**Non renderizzato. Solo uso editoriale.**

## Note di design
- Pagina per dettagli fini: interni, bordi, elementi decorativi
- Ogni area ha colore proprio da P002 — riferimento via color_id (no duplicazione codici)
- Zoom Panel (C012) per mostrare il dettaglio a close-up

## TODO
- [ ] Inserire aree di dettaglio da PROJECT.yaml detailAreas[]
- [ ] Verificare technique per ogni area (pennello|aerografo|bomboletta)
- [ ] Verificare che color_id referenzi correttamente P002/content.yaml colors[]

## Decisioni
- 2026-07-01: Dettagli dopo sequenza principale — P007 sempre dopo P005
- 2026-07-01: Tecnica "pennello" più comune per dettagli piccoli
