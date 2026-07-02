# Known Issues

**Mini4WD Manual SDK** · Quality Management System · Documento 07

| Campo | Valore |
|-------|--------|
| Scopo | Registro vivo dei problemi noti del framework |
| Destinatario | Operatore (consultazione), Maintainer (aggiornamento) |
| Source of Truth | Questo documento per le issue aperte; `CHANGELOG.md` per le correzioni rilasciate |
| Versione | 1.0.0 · SDK v2.4.1 · 2026-07-02 |

---

## Come usare questo registro

- **Prima di aprire un bug**, controlla se il problema è già qui: usa il workaround indicato.
- Il Maintainer aggiunge una riga per ogni bug confermato non ancora risolto, e la chiude alla release che lo corregge.
- Stati: `Aperto` → `In correzione` → `Risolto in vX.Y.Z` → `Chiuso`. Le issue chiuse restano nel registro (sezione §Archivio) per tracciabilità.

---

## Issue aperte

| ID | Descrizione | Versioni interessate | Workaround | Stato | Planned Fix |
|----|-------------|----------------------|------------|-------|-------------|
| KI-001 | `Templates/PROJECT.yaml` mantiene il campo LEGACY `text.approved_text_dir` (compatibilità v2.3.0); può confondere nuovi operatori sul percorso di output corretto | 2.4.0 – 2.4.1 | Ignorare il campo LEGACY; usare il percorso v2.4.x documentato nel template stesso | Aperto | Rimozione in v3.0.0 (breaking) |
| KI-002 | Pipeline PDF manuale: nessuna automazione pandoc/LaTeX; l'assemblaggio del PDF dipende dall'operatore | 2.x | Seguire `FIRST_PDF.md` passo-passo | Aperto | Pianificato post-v2.5.0 (roadmap) |

---

## Archivio (issue risolte)

| ID | Descrizione | Versioni interessate | Risolto in | Riferimento |
|----|-------------|----------------------|------------|-------------|
| KI-A01 | Validation FAIL su template non generati (Template/Draft/Approved non distinti) | ≤ 2.4.0 | 2.4.1 | UAT-001 Errore 1; `Tests/ContentValidation.md §Validation Scope` |
| KI-A02 | Falsi positivi linguistici su codici colore e nomi commerciali (TS-37, Chrome Silver…) | ≤ 2.4.0 | 2.4.1 | UAT-001 Errore 2; `Config/LANGUAGE_POLICY.yaml §exceptions` |
| KI-A03 | Posizione immagini di riferimento ambigua (due convenzioni concorrenti) | ≤ 2.4.0 | 2.4.1 | UAT-001 Errore 3; convenzione unica `Projects/{Model}/Images/` |
| KI-A04 | Nessun entry point per l'operatore umano | ≤ 2.4.0 | 2.4.1 | UAT-001 Errore 8; `START_HERE.md`, `OperatorGuide/` |
