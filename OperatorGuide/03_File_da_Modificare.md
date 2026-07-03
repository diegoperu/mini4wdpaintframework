# 03 — File da Modificare

**OperatorGuide · Mini4WD Manual SDK v2.5.0**

> Gli UNICI file che l'Operatore modifica. Tutto ciò che non è in questa pagina è in
> `04_File_da_NON_Modificare.md`. Matrice completa: `../FILE_MATRIX.md`.

---

## Dentro `Projects/{TuoModello}/` — tutto tuo

### 1. `PROJECT.yaml` — il file più importante

- **Quando:** al setup del progetto; poi solo per correggere dati dopo un QA FAIL.
- **Come:** editor di testo; segui i commenti campo per campo.
- **Regole:** codici vernice reali, `TODO:` per i dati mancanti, `modelSlug` in
  kebab-case, date ISO (YYYY-MM-DD).
- Dopo una modifica: riallega il file in chat, l'AI deve rileggerlo.

### 2. `Images/` — le tue foto

- **Quando:** al setup (foto di riferimento); in fase render (render approvati).
- **Regole:** min 2048px, sfondo neutro, nomi file per il naming convention.
- **Unica posizione valida.** Mai in `Assets/`.

### 3. `Notes/` — appunti e QA log

- `qa_log.md`: esiti dei QA, data, revisore. Lo aggiorni tu a ogni ciclo QA.
- Qualsiasi altro appunto libero.

### 4. `Output/` — output di lavorazione

- `raw/`: output grezzi delle generazioni (li salvi dalla chat).
- `pdf/`: i PDF esportati in fase 5.

### 5. Copie dei template (opzionali)

`PROJECT.md`, `CHECKLIST.md`, `COLOR_SCHEME.yaml`, `PDF_CONFIG.yaml`, `README.md` —
**le copie** nel tuo progetto sono tue; i master in `Templates/` no.

---

## Modifiche indirette (via prompt, mai a mano)

Questi file cambiano durante il lavoro, ma **li scrive l'AI attraverso i prompt**:

| File | Fase | Tu cosa fai |
|---|---|---|
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/content.yaml` | Testi | Approvi/rifiuti in chat |
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml` | QA/Seal | Confermi il passaggio di stato |
| `Projects/{Modello}/{Variante}/ApprovedText/P00x/changelog.md` | Ogni revisione | Verifichi che la riga ci sia |
| `Projects/{Modello}/{Variante}/ApprovedImages/P00x/` | Render | Salvi il file col nome giusto |
| `Projects/{Modello}/{Variante}/index.yaml` | Seal/Release | Con ruolo Reviewer/Maintainer |

Se ti accorgi di un errore in questi file: **non correggerlo a mano** — rientra in
chat, fai correggere all'AI e fai registrare la revisione nel changelog di pagina.
