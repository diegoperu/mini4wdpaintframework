# 01 — Il Tuo Primo Manuale

**OperatorGuide · Mini4WD Manual SDK v2.5.5**

> Il percorso completo, dall'inizio alla fine, in un'unica pagina. Ogni tappa rimanda
> al tutorial dettagliato. Se è la prima volta che usi l'SDK, segui questo documento
> dall'alto verso il basso senza saltare nulla.

---

## Il percorso in 6 tappe

```
TAPPA 1          TAPPA 2         TAPPA 3          TAPPA 4        TAPPA 5      TAPPA 6
Prepara     →    Bootstrap  →    Testi + QA  →    Rendering  →   PDF     →    Pubblica
(tu, no AI)      (chat #1)       (chat #1)        (script + chat solo   (Maintainer)
                                                    per illustrazioni)
```

---

## TAPPA 1 — Prepara il progetto (senza AI)

Cosa fai: cartella progetto, PROJECT.yaml compilato, foto in `Images/`.

- Guida completa: **`../FIRST_PROJECT.md`** (PASSO 1–5)
- Struttura e posizioni: `../PROJECT_STRUCTURE.md`
- Checklist: `05_Checklist.md §Setup`

Esito atteso: `Projects/{TuoModello}/` completo, nessun altro file toccato.

## TAPPA 2 — Bootstrap (chat #1)

Cosa fai: apri una chat, alleghi i file della Fase 1, incolli il prompt, leggi il
Bootstrap Report e lo approvi.

- Prompt e file da allegare: `../Docs/AI_BOOTSTRAP_PROMPT.md → Fase 1`
- Guida: `../FIRST_PROJECT.md` (PASSO 6–7)

Esito atteso: Bootstrap Report con i TUOI dati, tua approvazione esplicita in chat.

## TAPPA 3 — Testi + QA, una pagina alla volta (stessa chat #1)

Per **ogni pagina** P001 → P010, in quest'ordine:

1. **Genera** — allega `PromptEngine/{pagina}.md`, usa il prompt Fase 2.
   → L'AI produce `content.yaml`.
2. **Valida** — allega i due file di test, usa il prompt Fase 3.
   → Verdetto APPROVED / REJECTED.
3. **Se REJECTED** — l'AI elenca le correzioni: falle applicare e rivalida.
   Se il problema è un dato sbagliato in PROJECT.yaml, correggi il file e riallegalo.
4. **Sigilla** — a verdetto APPROVED, conferma il seal: `metadata.yaml → locked`.

Ordine pagine e prompt: `../BOOTSTRAP.md §Pages`. P009 solo se hai il premium abilitato.

⚠️ **Non validare mai una pagina che non hai ancora generato**: i moduli in
`Projects/{Model}/{Variant}/ApprovedText/` nascono come template vuoti in stato `draft` — il QA sui
template dà FAIL per costruzione. Prima si genera, poi si valida.

Esito atteso: tutte le pagine con `status: locked`.

## TAPPA 4 — Rendering (template locale + chat solo per le illustrazioni)

Il testo e il layout di ogni pagina si generano **senza AI**, con un comando:
`Scripts/render_page.py {Modello} {Variante}`. Solo per le illustrazioni ancora
mancanti (copertina, viste ortogonali, foto di dettaglio) serve una chat nuova —
una per ciascuna illustrazione, mai la stessa chat per due immagini diverse.

- Guida completa: **`../FIRST_RENDER.md`**

Esito atteso: tutte le pagine `status: rendered`, illustrazioni in
`Projects/{Modello}/{Variante}/Images/` (stessa cartella delle foto di riferimento).

## TAPPA 5 — PDF (script + processo guidato per l'export di produzione)

`Scripts/render_page.py {Modello} {Variante} pdf` produce già un'anteprima unica
(tutte le pagine unite in un PDF, in `Projects/{Modello}/{Variante}/`). Per le 3
varianti di produzione (screen/print/archive, CMYK, bleed) serve ancora il
processo guidato in chat nuova.

- Guida completa: **`../FIRST_PDF.md`**

Esito atteso: 3 PDF + checksum in `Projects/{Modello}/Output/pdf/`.

## TAPPA 6 — Pubblicazione

Consegni PDF + qa_log al Maintainer, che pubblica in `Assets/ApprovedManual/`.
Il tuo progetto diventa un Golden Project.

---

## Le 5 regole che ti salvano

1. **Una pagina alla volta.** Mai "generami tutto il manuale".
2. **Genera prima di validare.** Il QA sui template vuoti fallisce sempre.
3. **Tocca solo `Projects/{TuoModello}/`.** Tutto il resto è sola lettura.
4. **Una chat nuova per ogni illustrazione** (TAPPA 4) e a ogni cambio di motore
   (testi → rendering → PDF di produzione).
5. **`TODO:` invece di inventare.** Un dato mancante marcato è recuperabile, un dato
   inventato è un manuale sbagliato.
