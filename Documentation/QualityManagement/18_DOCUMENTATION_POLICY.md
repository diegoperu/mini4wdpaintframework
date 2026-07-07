# Documentation Policy

**Mini4WD Manual SDK** · Quality Management System · Documento 18

| Campo | Valore |
|-------|--------|
| Scopo | Definire le regole minime che ogni nuovo documento del repository deve rispettare |
| Destinatario | Maintainer, Developer, Contributor |
| Source of Truth | Questo documento per i requisiti di intestazione; `Core/DOCUMENTATION_STYLE.md` per lo stile di scrittura |
| Versione | 1.0.0 · SDK v2.5.5 · 2026-07-02 |

---

## 1. Rapporto con le regole esistenti

Questa policy NON sostituisce `Core/DOCUMENTATION_STYLE.md` (voce, tempo verbale, heading, RFC 2119): la integra con requisiti di **tracciabilità**. Un documento può essere scritto perfettamente e restare ingovernabile se non dichiara a cosa serve, per chi, e chi comanda in caso di conflitto. UAT-001 lo ha dimostrato: metà degli errori nasceva da documenti che si sovrapponevano senza dichiarare quale fosse autoritativo.

---

## 2. Intestazione obbligatoria

Ogni **nuovo documento** aggiunto al repository deve dichiarare, in testa, questi quattro campi:

| Campo | Cosa dichiarare |
|-------|-----------------|
| **Scopo** | Cosa fa questo documento, in una frase. Se servono due frasi, probabilmente sono due documenti. |
| **Destinatario** | Chi lo legge: Operatore / Reviewer / Maintainer / Developer / modello AI. Determina linguaggio e livello di dettaglio. |
| **Source of Truth** | Se questo documento È autoritativo per la sua materia, dirlo. Se NON lo è, indicare quale documento comanda in caso di conflitto. |
| **Versione** | Versione del documento e/o versione SDK di riferimento, con data. |

Formato raccomandato: la tabella usata dai documenti di questa cartella (vedi qualsiasi `Documentation/QualityManagement/*.md`).

---

## 3. Regole di coerenza

1. **Un fatto, una casa.** Ogni informazione normativa vive in UN solo documento; gli altri la referenziano con il path, non la ripetono. Le ripetizioni divergono (UAT-001, Errore 3: due convenzioni per le immagini).
2. **Niente documenti orfani.** Ogni nuovo documento deve essere raggiungibile da almeno un indice (README di cartella, `20_INDEX.md`, `RepositoryManifest.yaml` quando applicabile).
3. **Dichiarare le eccezioni.** Se un documento deroga a una regola generale, la deroga va dichiarata nel documento che deroga E in quello derogato.
4. **Lingua.** Documenti per l'Operatore e il QMS: italiano. Documenti autoritativi del framework e machine-readable (YAML): inglese, coerente con lo stato attuale del repository. Non mescolare le due lingue nello stesso documento oltre ai termini tecnici.
5. **Aggiornamento tracciato.** Modificare un documento autoritativo richiede Change Proposal (`15`); il CHANGELOG registra la modifica; la Version History registra la release.

---

## 4. Ciclo di vita di un documento

| Stato | Significato |
|-------|-------------|
| Bozza | In scrittura; non referenziabile da altri documenti |
| Attivo | Normativo; qualsiasi conflitto si risolve secondo la source-of-truth hierarchy |
| LEGACY | Mantenuto solo per compatibilità; dichiara quale documento lo sostituisce |
| Ritirato | Rimosso dal repository (solo in Major Release), registrato nel CHANGELOG |

---

## 5. Checklist per un nuovo documento

- □ intestazione con Scopo / Destinatario / Source of Truth / Versione
- □ stile conforme a `Core/DOCUMENTATION_STYLE.md`
- □ nessuna informazione normativa duplicata da altri documenti
- □ referenziato da almeno un indice
- □ lingua corretta per il destinatario
- □ modifica registrata in CHANGELOG (e Change Proposal, se documento autoritativo)
