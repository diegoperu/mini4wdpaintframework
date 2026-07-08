# Changelog — P002

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0 | 2026-07-01 | SDK Init | Page module created from template |
| 1 | 2026-07-03 | Text Engine | content.yaml populated from Projects/Magnum_Saber/PROJECT.yaml. 6 colori risolti (PC001–PC006) con paint_code/paint_brand/finish/hex/area estratti direttamente da paintScheme.colors[]. Render front/side/top: path presenti (paths.colorSchemeRender*), file fisici non ancora prodotti (Phase 3 pending). Nessun TODO: — tutti i dati richiesti erano raggiungibili in PROJECT.yaml. |
| 2 | 2026-07-03 | diego.peruselli@polimi.it | QA passed (ContentValidation 7/7, TextValidation 9/9, 0 blocking FAIL). Page sealed: status → locked, approved: true. sdk_version corrected to 2.4.1, page_name compilato. |
| 3 | 2026-07-08 | diego.peruselli@polimi.it (Claude Code) | Bug di contenuto: colors[PC006].area/notes descrivevano "ingranaggi visibili, boccole e dettagli meccanici del motore" — parti mobili/funzionali, la vernice ne comprometterebbe il funzionamento (vedi `Knowledge/MechanicalSafety.md`, `TEST-CV-008`). Corretto in "Cover ingranaggi esterna (guscio Super-II)", stesso colore/tecnica. Stessa correzione applicata a monte in `PROJECT.yaml paintScheme.colors[PC006]`. Page riaperta: status → review, approved: false, revision 1 → 2. |
