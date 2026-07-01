# Notes — P005 Sequenza di Verniciatura

**Non renderizzato. Solo uso editoriale.**

## Note di design
- Pagina a sequenza ordinata: colore più chiaro → colore più scuro
- Ogni step include: Paint Code Box (C011) + Badge step (C013) + Timer asciugatura (C014)
- Avvertenza drying time obbligatoria — rischio colature se non rispettato

## TODO
- [ ] Inserire sequenza da PROJECT.yaml paintSequence[]
- [ ] Verificare ordine corretto: base bianca/argento prima, colori scuri dopo
- [ ] Inserire tempi di asciugatura per ogni mano

## Decisioni
- 2026-07-01: Sequenza rispetta principio "light before dark" — documentato in STYLE_DECISIONS.md
- 2026-07-01: Ogni step richiama color_id da P002/content.yaml (no duplicazione dati)
