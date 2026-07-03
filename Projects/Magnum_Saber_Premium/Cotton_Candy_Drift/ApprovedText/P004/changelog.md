# Changelog — P004

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0 | 2026-07-01 | SDK Init | Page module created from template |
| 1 | 2026-07-03 | Text Engine | content.yaml populated from Projects/Magnum_Saber/PROJECT.yaml. 5 step da preparationSteps[] (id, title, duration, tools, warning, tip tutti risolti). Descrizioni convertite da infinito a imperativo seconda persona (RULE-067) preservando invariati i fatti tecnici. "PRO TIPS" boilerplate di PromptEngine/Preparation.md tradotto in italiano → tips[] generali. Durate normalizzate a "N minuti"/"N ore" (RULE-076). Nessun TODO: — tutti i dati richiesti erano in PROJECT.yaml. warnings[] generale lasciato vuoto (nessun dato distinto dai warning per-step). |
| 2 | 2026-07-03 | QA fix | CV-002-G/H FAIL corretti: 5 steps[].warning ora iniziano con "Attenzione:", 4 steps[].tip + 4 tips[] generali ora iniziano con "Suggerimento:" (righe 26-67). "tack cloth" (WARNING TX-001) italicizzato al primo uso (step 4 description, RULE-066). text.md risincronizzato senza duplicare i lead-in. |
| 3 | 2026-07-03 | diego.peruselli@polimi.it | QA passed (ContentValidation 7/7, TextValidation 9/9 dopo fix). Page sealed: status → locked, approved: true. sdk_version corrected to 2.4.1, page_name compilato. |
