# Capitolo 12 — PDF

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| PDF Master | `Core/PDF_MASTER.md` | Source of Truth — specifica di export |
| PDF Config Template | `Templates/PDF_CONFIG.yaml` | Configurazione per-progetto (v2.4.0) |
| PDF Config globale | `Config/pdf.yaml` | Default globali (v2.2.0) |
| PDF Validation | `Tests/PDFValidation.md` | 8 test tecnici (TEST-PD-001–008) |
| Approved Manual README | `Assets/ApprovedManual/README.md` | Policy di archiviazione e pubblicazione |

---

## 1. Le varianti PDF

Ogni manuale approvato DEVE essere esportato in almeno due varianti prima di poter essere pubblicato:

| Variante | Suffisso | Standard | Uso |
|----------|----------|----------|-----|
| Screen | `_screen` | PDF/A-2b | Distribuzione digitale, download web |
| Print | `_print` | PDF/X-4 | Stampa offset professionale |

`Config/pdf.yaml` e `Templates/PDF_CONFIG.yaml` definiscono anche una terza variante, **archive** (PDF/A-2b, nessuna compressione, per conservazione a lungo termine), assente dalla tabella §1 di `Core/PDF_MASTER.md`.

> ⚠️ **Warning:** `Core/PDF_MASTER.md` §1 — il documento normativo (Source of Truth) — descrive solo le varianti Screen e Print. La variante `archive` esiste in entrambi i file di configurazione (`Config/pdf.yaml → variants.archive`, `Templates/PDF_CONFIG.yaml → pdf.variants.archive`) ma non è mai menzionata in `Core/PDF_MASTER.md`. Trattare `archive` come opzionale/non normativa finché `Core/PDF_MASTER.md` non viene aggiornato per includerla esplicitamente.

Nomi di file di esempio (variante screen/print, contesto di export generale):
```text
proto-emperor_manual_screen_v1.pdf
proto-emperor_manual_print_v1.pdf
```

All'interno di `Assets/ApprovedManual/{ModelName}/` la convenzione è diversa (senza prefisso modello, perché già dentro la cartella del modello): `manual_screen.pdf`, `manual_print.pdf`, con `_v2`, `_v3` aggiunto solo in caso di correzione post-approvazione (vedi §5).

---

## 2. Standard tecnici per variante

### Screen — PDF/A-2b
- Colore: sRGB IEC61966-2.1
- Font: tutti embedded come subset
- Immagini: JPEG qualità 90 per fotografie, PNG lossless per elementi vettoriali
- Nessuna cifratura (PDF/A la vieta)
- Versione PDF 1.7

### Print — PDF/X-4
- Colore: CMYK FOGRA39 (ISO Coated v2 300%)
- Font: tutti embedded come subset
- Immagini: minimo 300 dpi a dimensione finale di stampa, nessun downsampling
- Versione PDF minima: 1.6
- Output intent: ISO Coated v2 300% (FOGRA39)

> ⚠️ **Warning:** l'approssimazione CMYK su base sRGB del colore primario TamiyaPrimary (`#114B69`) è C:84 M:29 Y:0 K:59 (`Core/COLOR_SYSTEM.md`) — non è una conversione color-managed FOGRA39. Richiedere sempre una prova di stampa prima della tiratura; nessun riferimento Pantone è stato verificato per questo colore.

> ⚠️ **Warning:** il nero ricco (`#1A1A1A` per il testo body) converte in circa C:0 M:0 Y:0 K:90 in CMYK — corretto per il testo. NON usare un nero ricco a 4 canali (es. C:60 M:40 Y:40 K:100) per il testo: causa disallineamento e sfrangiatura in stampa offset.

---

## 3. Bleed e area di sicurezza

Solo per la variante print — la variante screen non ha bleed.

| Bordo | Bleed |
|-------|-------|
| Tutti i lati | 3mm |

Gli elementi che raggiungono il bordo pagina (fascia header, fascia footer, pannello laterale) DEVONO estendersi 3mm oltre il segno di taglio. Gli elementi interni devono restare nell'area di sicurezza (8mm dentro il segno di taglio). Eccezione: `P001` Cover può usare un render a bleed pieno.

---

## 4. Ordine pagine e metadata

L'ordine di pagina nel PDF è definito da `Templates/PDF_CONFIG.yaml → pdf.bookmarks.structure` (10 pagine standard, 11 se `premiumVariant.enabled == true`). Deviazioni dal conteggio 10/11 richiedono una nota in `Projects/{ModelName}/Notes/decisions.md`.

Tutti i campi metadata sono obbligatori — la loro assenza è un fallimento QA (`QA-096`–`QA-100`):

| Campo | Template valore | Esempio |
|-------|------------------|---------|
| Title | `{{project.modelName}} — {{project.paintScheme.name}} — Mini4WD Manual` | "Proto Emperor — Midnight Violet — Mini4WD Manual" |
| Creator | `Mini4WD Manual SDK v{{sdkVersion}}` | "Mini4WD Manual SDK v2.4.0" |
| Creation Date | `{{project.createdDate}}` | "2024-01-20" |

La struttura dei bookmark (solo variante screen — la print non li richiede) segue l'ordine pagina e deve puntare esattamente alla pagina, non all'inizio del documento.

---

## 5. Font embedding

Font richiesti, sempre come subset embedded:

- `Bebas Neue` (Title Font) — o sostituto confermato
- `Source Sans Pro` (Body Font) — pesi Regular, SemiBold, Bold
- `JetBrains Mono` (Mono Font) — almeno il peso Regular

> 📝 **Nota:** Bebas Neue e Source Sans Pro sono disponibili con licenza SIL Open Font License, JetBrains Mono con licenza Apache 2.0 — tutti embeddabili liberamente. Verificare comunque la compatibilità di licenza prima di distribuire un PDF pubblico.

Un PDF che referenzia font di sistema senza incorporarli è un fallimento QA automatico.

---

## 6. Strumenti di export validati

| Strumento | Note |
|-----------|------|
| Affinity Publisher 2 | **Raccomandato.** Supporto nativo PDF/X-4 e PDF/A-2b, color management CMYK |
| Adobe InDesign | Supporto PDF/X-4 completo, richiede abbonamento con licenza |
| Scribus (open source) | Gratuito, supporto PDF/X-3 (non X-4) — accettabile per print quando X-4 non è richiesto |
| pandoc + LaTeX | Adatto a variante screen/PDF-A; non raccomandato per print (limiti CMYK) |

Configurazioni dettagliate per ciascuno strumento: `Core/PDF_MASTER.md` §9.

---

## 7. Validazione (Tests/PDFValidation.md)

8 test tecnici, eseguiti dopo la Fase 5 (Generazione PDF) e prima della Fase 6 (Approvazione):

| Test | Verifica | Bloccante |
|------|----------|-----------|
| TEST-PD-001 | Presenza dei file PDF e del checksum | Sì |
| TEST-PD-002 | Completezza metadata | Sì (Title/Creator mancanti) |
| TEST-PD-003 | Font embedding | Sì |
| TEST-PD-004 | Conteggio e ordine pagine | Sì |
| TEST-PD-005 | Struttura bookmark | No (solo variante screen) |
| TEST-PD-006 | Specifica bleed | Sì (per variante print) |
| TEST-PD-007 | Verifica checksum SHA-256 | Sì |
| TEST-PD-008 | Profilo colore | Sì (print in sRGB è un fallimento) |

Comando di verifica checksum:
```bash
sha256sum -c checksums.sha256
```

> ⚠️ **Warning:** un fallimento di checksum significa che il file PDF è stato modificato dopo la registrazione del checksum. Non approvare mai un manuale con checksum fallito — rigenerare il PDF e ricalcolare i checksum.

---

## 8. Archiviazione e pubblicazione

Un manuale entra in `Assets/ApprovedManual/{ModelName}/` solo dopo aver completato tutte le fasi di `Core/WORKFLOW.md` (Capitolo 05) e superato `Core/QA_SYSTEM.md` (Capitolo 11) senza fallimenti. La cartella è **read-only durante la produzione** — modifiche richiedono approvazione del project maintainer.

Regola di versionamento per correzioni post-approvazione (mai sovrascrivere):
1. Creare copie versionate (`P001_v2.png`, `manual_screen_v2.pdf`, …)
2. Aggiornare `Notes/qa_log.md` con una voce che documenta cosa è cambiato e perché
3. Aggiornare il `README.md` del modello per indicare la versione approvata corrente
4. I file v1 restano in sede come registro storico — **mai cancellati**

Ogni approvazione va taggata in git:
```bash
git tag -a "approved/{model-slug}/v{version}" -m "Approved: {Model Name} v{version}"
```

Pubblicazione (rendere il PDF disponibile pubblicamente) richiede stato **Approved** — un manuale in stato Draft o Review non deve mai essere pubblicato. La pubblicazione stessa non è gestita dall'SDK: il ruolo dell'SDK termina allo stato Approved (`Core/MANUAL_SYSTEM.md` §8).

---

## Vedi anche

- Capitolo 05 — Workflow (fasi della pipeline che precedono l'export PDF)
- Capitolo 09 — ApprovedAssets (ciclo di vita pagina, prerequisito per l'export)
- Capitolo 11 — QA (QA-096–QA-100, Tests/PDFValidation.md)
- Capitolo 13 — GoldenProjects (Proto Emperor non ha ancora un manuale approvato — vedi nota in quel capitolo)
