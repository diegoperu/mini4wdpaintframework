# FIRST_RENDER.md — Tutorial: da Approved Text alla Prima Pagina Illustrata

**Mini4WD Manual SDK v2.5.0** · Tutorial operatore · Tempo: ~30 minuti per pagina

> Da dove parti: almeno una pagina con `metadata.yaml → status: locked`
> (testo generato e validato — vedi `FIRST_PROJECT.md` e `OperatorGuide/01_Primo_Manuale.md`).
> Dove arrivi: la prima pagina illustrata, validata e registrata.

---

## PASSO 1 — Verifica il punto di partenza

Controlla `Projects/{Modello}/{Variante}/ApprovedText/P001/metadata.yaml`:

```yaml
status: "locked"
approved: true
locked: true
```

Se `status` non è `locked`, fermati: il Render Engine parte **solo** da contenuto
sigillato (Golden Rule G08). Torna alla fase QA testi.

## PASSO 2 — Apri una NUOVA chat

Il rendering usa un contesto diverso (design, non generazione testi). **Non riusare
la chat dei testi.**

## PASSO 3 — Allega i file per il rendering

Nell'ordine (lista anche in `Docs/AI_BOOTSTRAP_PROMPT.md → Fase 4`):

1. `Core/RENDER_GUIDE.md`
2. `Core/DESIGN_LANGUAGE.md`
3. `Core/STYLE_GUIDE.md`
4. `Core/COMPONENT_SYSTEM.md`
5. `Assets/DesignSystem/Tokens/tokens.example.yaml`
6. `Projects/{Modello}/{Variante}/ApprovedText/P001/content.yaml` (quello locked)
7. Le foto di riferimento da `Projects/{Modello}/Images/`

## PASSO 4 — Lancia il prompt di rendering

Usa il **Prompt Fase 4 — Rendering** da `Docs/AI_BOOTSTRAP_PROMPT.md`, sostituendo
`{PAGINA}` e `{NOME_PAGINA}` (es. `P001`, `Copertina`).

Cosa deve fare l'AI (e cosa NON deve fare):

| Deve | Non deve |
|---|---|
| Posizionare ESATTAMENTE il testo di content.yaml | Inventare o riformulare testo |
| Usare i Design Token (`token.PrimaryViolet`, ecc.) | Hardcodare colori/dimensioni |
| Riprodurre la forma del modello dalle foto | Modificare forma o proporzioni |
| Sfondo bianco puro, header viola | Aggiungere decorazioni non previste |

## PASSO 5 — QA del render

Nella stessa chat, valida contro la checklist:

```
Esegui la validazione visiva della pagina appena generata secondo
Core/QA_SYSTEM.md. Riporta ogni voce applicabile: PASS / FAIL.
Elenca i FAIL con la correzione necessaria.
```

Verifiche manuali rapide da fare TU:

- [ ] Il testo sulla pagina è identico a content.yaml (nessuna parola cambiata)
- [ ] Sfondo bianco puro, pannello header viola
- [ ] Il modello somiglia alle tue foto (forma, non solo colori)
- [ ] Footer presente: ID pagina + nome modello

## PASSO 6 — FAIL? Correggi e rigenera

- **Problema visivo** (layout, colori, forma) → correggi il prompt di render nella stessa
  chat, rigenera. NON toccare content.yaml.
- **Problema di testo** (refuso nel contenuto) → il testo è locked: si riapre la pagina
  con una riga in `changelog.md`, si corregge via Text Engine, si rifà QA e seal, poi
  si ri-renderizza. Vedi `LIFECYCLE.md`.

## PASSO 7 — Salva e registra

1. Salva l'immagine in `Projects/{Modello}/{Variante}/ApprovedImages/P001/` seguendo il naming
   (`Core/NAMING_CONVENTION.md`): es. `dash-01-shadow-emperor_P001_cover_v1.png`
2. Aggiorna (o fai aggiornare all'AI) `Projects/{Modello}/{Variante}/ApprovedText/P001/metadata.yaml`:

```yaml
status: "rendered"
rendered: true
rendered_date: "2026-07-02"
```

3. Annota l'esito in `Projects/{Modello}/Notes/qa_log.md`.

**→ Prima pagina illustrata completata.** Ripeti PASSO 3–7 per le altre pagine
(stessa chat va bene finché resta ordinata). Poi: `FIRST_PDF.md`.
