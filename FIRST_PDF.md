# FIRST_PDF.md — Tutorial: dal Rendering al PDF

**Mini4WD Manual SDK v2.5.0** · Tutorial operatore · Tempo: ~45 minuti

> Da dove parti: tutte le pagine in `status: rendered` (vedi `FIRST_RENDER.md`).
> Dove arrivi: il manuale PDF nelle 3 varianti (screen / print / archive).

---

## PASSO 1 — Verifica che tutte le pagine siano pronte

Per ogni pagina in `Projects/{Modello}/{Variante}/ApprovedText/P00x/metadata.yaml`:

```yaml
status: "rendered"
```

Pagine attese: P001–P008 + P010 (9 pagine), più P009 solo se in PROJECT.yaml hai
`premiumVariant.enabled: true` (10 pagine). Se una pagina non è `rendered`, completa
prima quella.

## PASSO 2 — Prepara la configurazione PDF

```bash
cp Templates/PDF_CONFIG.yaml "Projects/${MODEL}/PDF_CONFIG.yaml"
```

Apri la copia e compila i metadati con i valori del tuo PROJECT.yaml: titolo, autore,
keywords, versione manuale. Non modificare il master in `Templates/`.

## PASSO 3 — Apri una NUOVA chat

Fase diversa, contesto diverso. Allega:

1. `Core/PDF_MASTER.md`
2. `Projects/{Modello}/PDF_CONFIG.yaml` (la tua copia compilata)
3. Le pagine renderizzate (o i loro percorsi in `Projects/{Modello}/{Variante}/ApprovedImages/`)

Usa il **Prompt Fase 5 — PDF** da `Docs/AI_BOOTSTRAP_PROMPT.md`.

> Nota: in v2.4.x l'assemblaggio PDF è un processo guidato, non automatico. L'AI ti
> guida nell'export con lo strumento che preferisci (Affinity Publisher, InDesign,
> Scribus, pandoc+LaTeX — vedi `Core/PDF_MASTER.md §Export Tools`).

## PASSO 4 — Esporta le 3 varianti

| Variante | Uso | Specifiche chiave |
|---|---|---|
| **screen** | Lettura a schermo | sRGB, 150dpi, senza bleed, PDF/A-2b |
| **print** | Stampa | CMYK FOGRA39, 300dpi, bleed 3mm, PDF/X-4 |
| **archive** | Archivio a lungo termine | Vedi `Config/pdf.yaml` |

Output in `Projects/{Modello}/Output/pdf/`:

```
dash-01-shadow-emperor_manual_screen_v1.pdf
dash-01-shadow-emperor_manual_print_v1.pdf
dash-01-shadow-emperor_manual_archive_v1.pdf
```

(naming: `Core/NAMING_CONVENTION.md §2.4`)

## PASSO 5 — QA del PDF

Checklist finale (voci QA-096–QA-100 di `Core/QA_SYSTEM.md` + `Tests/PDFValidation.md`):

- [ ] Ordine pagine corretto: P001 → P010
- [ ] Metadati PDF completi (titolo, autore, keywords)
- [ ] Segnalibri presenti per ogni pagina
- [ ] Font incorporati
- [ ] Bleed corretto per variante (0mm screen, 3mm print)

Poi genera i checksum:

```bash
cd "Projects/${MODEL}/Output/pdf" && sha256sum *.pdf > checksums.sha256
```

## PASSO 6 — Richiedi la pubblicazione

La pubblicazione in `Assets/ApprovedManual/{Modello}/` la fa il **Maintainer**
(niente self-approval — `Core/WORKFLOW.md §4.7`). Consegna:

- I 3 PDF + `checksums.sha256`
- `Notes/qa_log.md` completo
- `PROJECT.yaml` (snapshot)

Quando il Maintainer approva, le pagine passano a `released` e il progetto diventa
un **Golden Project**. Fine del ciclo — vedi `LIFECYCLE.md`.
