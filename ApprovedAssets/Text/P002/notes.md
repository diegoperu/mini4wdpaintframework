# Notes — P002 Schema Colori

**Non renderizzato. Solo uso editoriale.**

## Note di design
- Pagina a schema: 3 viste ortogonali + griglia palette a sinistra
- Ogni swatch di colore mostra: nome, codice Tamiya, finitura, esagono colore
- Palette Strip (C003) occupa fascia verticale sinistra — 60px larghezza token
- Paint Code Box (C011) sotto ogni swatch: Codice + Marca + Finitura

## TODO
- [ ] Inserire colori da PROJECT.yaml paintScheme.colors[]
- [ ] Inserire nome modello nel footer da PROJECT.yaml project.modelName
- [ ] Assegnare render ortogonali approvati (front, side, top)

## Decisioni
- 2026-07-01: Swatch con esagono colore opzionale (hex non sempre disponibile da Tamiya)
- 2026-07-01: Tre viste ortogonali obbligatorie — nessuna vista prospettica su questa pagina
