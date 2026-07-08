# Changelog — P003

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0 | 2026-07-01 | SDK Init | Page module created from template |
| 1 | 2026-07-03 | Text Engine | content.yaml populated from Projects/Magnum_Saber/PROJECT.yaml. 6 vernici (paintScheme.colors[]), 5 strumenti (materials.tools[], type tradotto in italiano: airbrush→aerografo, brush→pennello, tool→strumento), 5 consumabili (materials.consumables[]). Safety note tradotta da PromptEngine/Materials.md boilerplate. Nessun TODO: — quantity paints lasciato vuoto (opzionale, dato genuinamente assente in PROJECT.yaml, non richiesto per approvazione). |
| 2 | 2026-07-03 | QA fix | CV-002-G FAIL corretto: safety_notes[0] (riga 117) ora inizia con "Attenzione:" come richiesto per C008. |
| 3 | 2026-07-03 | diego.peruselli@polimi.it | QA passed (ContentValidation 7/7, TextValidation 9/9 dopo fix). Page sealed: status → locked, approved: true. sdk_version corrected to 2.4.1, page_name compilato. |
| 4 | 2026-07-08 | diego.peruselli@polimi.it (Claude Code) | Bug di contenuto: tools[].notes (pennello tondo n.000) citava "meccanica del motore" come area d'uso — stesso framing errato corretto altrove nel progetto (vedi `Knowledge/MechanicalSafety.md`, `TEST-CV-008`). Corretto in "cover ingranaggi esterna". Page riaperta: status → review, approved: false, revision 1 → 2. |
| 5 | 2026-07-08 | diego.peruselli@polimi.it | QA re-passed (ContentValidation 8/8, TextValidation 9/9, 0 blocking FAIL). Page re-sealed: status → locked, approved: true. |
