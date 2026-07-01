---
page_id: "P001"
model: "{{project.modelName}}"
language: "it"
version: "{{project.version}}"
approved: false
approved_by: ""
approved_date: ""
sdk_version: "2.4.0"
text_engine_version: "1.0"
---

<!-- ============================================================
     Mini4WD Manual SDK — ApprovedText Template
     Version: 2.3.0
     Reference: Core/TEXT_ENGINE.md
     Language policy: Config/LANGUAGE_POLICY.yaml

     ISTRUZIONI:
     1. Sostituire tutti i {{token}} con valori da PROJECT.yaml
     2. Generare il contenuto tramite PromptEngine/{NomePagina}.md
     3. Salvare l'output grezzo in raw/P{NNN}_raw.md
     4. Eseguire Tests/TextValidation.md
     5. Correggere tutti i blocchi ❌
     6. Impostare approved: true e compilare approved_by / approved_date
     7. Salvare come P{NNN}.md (senza suffisso _raw)

     LINGUA: tutto il testo deve essere in italiano.
     Nessun kanji, hiragana, katakana, inglese, lorem ipsum.
     Usare i segnaposto approvati se il contenuto è mancante:
       [TITOLO] [SOTTOTITOLO] [TESTO] [AVVERTENZA] [SUGGERIMENTO]
     ============================================================ -->

# [TITOLO PAGINA]

<!-- Sostituire con il titolo della pagina in italiano.
     Esempio per P001: "{{project.modelName}} — {{project.paintScheme.name}}" -->

## [SEZIONE PRINCIPALE]

[TESTO]

<!-- Contenuto specifico della pagina qui sotto.
     La struttura varia per pagina — vedere PromptEngine/{NomePagina}.md
     per il prompt di generazione completo.
     Tutto il testo deve essere in italiano. -->

<!-- TEXT_ENGINE_MARKER: end -->
