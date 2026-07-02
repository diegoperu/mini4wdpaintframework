# Capitolo 14 — Roadmap

## Documenti di riferimento

| Documento | Percorso | Ruolo |
|-----------|----------|-------|
| Roadmap | `ROADMAP.md` | Direzione pianificata, non vincolante |
| Status | `STATUS.md` | Stato di implementazione, TODO aperti |
| SDK Context | `SDK_CONTEXT.yaml` (sezione `roadmap`) | Riepilogo machine-readable |
| Release Info | `ReleaseInfo.yaml` (sezione `next_release`) | Anteprima machine-readable della prossima release |

---

## 1. Versione corrente vs prossima

**Corrente:** 2.4.0, codename "CMS" (rilasciata 2026-07-01).
**Prossima pianificata:** 2.5.0.

> ⚠️ **Ogni elemento descritto in questo capitolo come "pianificato" NON è implementato nella versione corrente.** Verificare sempre `VERSION` prima di assumere che una funzionalità qui descritta sia disponibile.

---

## 2. v2.5.0 — cosa è davvero pianificato (attenzione a una discrepanza)

`STATUS.md`, `SDK_CONTEXT.yaml → roadmap.next_planned` e `ReleaseInfo.yaml → next_release` concordano fra loro su questo elenco per v2.5.0:

- `Compiler/` — Project Loader, Context Builder, Page Generator, QA Engine, PDF Assembler
- Prompt Orchestrator — gestisce automaticamente la sequenza LOAD
- Icon Library — **15** icone SVG (oggi si usano fallback Unicode)
- `Docs/tutorial/` — documenti tutorial end-to-end
- Release System — automazione di tagging e aggiornamento manifest

> ⚠️ **Warning — incongruenza tra documenti SDK:** `ROADMAP.md § v2.5.0 — Planned` e `MigrationReport_v2.4.md § Next: v2.5.0` descrivono un elenco **diverso** per la stessa versione: script Python/Shell per generazione e validazione di `content.yaml`, Icon Library da **10** icone (non 15), un runner automatico per `Tests/ContentValidation.md`, esecuzione automatica di `Tests/TextValidation.md`, `Config/environments/` per switching dev/staging/production, una guida CI/CD (`Build/CI.md`), espansione di `Knowledge/` con tecniche airbrush, e un aggiornatore automatico di `ApprovedAssets/index.yaml`. Non menzionano affatto `Compiler/` o "Prompt Orchestrator" come termini. Le due fonti condividono solo il tema generale ("automazione") e il numero di versione, non il contenuto specifico. Chi pianifica il lavoro per v2.5.0 deve trattare `SDK_CONTEXT.yaml`/`STATUS.md`/`ReleaseInfo.yaml` come la versione più autorevole (sono i tre file di bootstrap machine-readable, aggiornati insieme ad ogni release — vedi Capitolo 02) mentre `ROADMAP.md` in questo punto sembra riflettere una bozza precedente non riconciliata. Segnalato per revisione SDK — vedi `CHANGE_IMPACT.md`.

`SDK_CONTEXT.yaml → documentation` conferma questo stato:

```yaml
documentation:
  tutorials: "planned_v2.5.0"
  icon_library: "planned_v2.5.0"
```

---

## 3. TODO aperti (STATUS.md)

| ID | Descrizione | Priorità | Target |
|----|-------------|----------|--------|
| TODO-001 | Creare il sottosistema `Compiler/` | Alta | v2.5.0 |
| TODO-002 | Creare 15 icone SVG in `Assets/DesignSystem/Icons/` | Media | v2.5.0 |
| TODO-003 | Scrivere `Docs/tutorial/first-manual.md` | Media | v2.5.0 |
| TODO-004 | Scrivere `Docs/tutorial/render-generation.md` | Media | v2.5.0 |
| TODO-005 | Scrivere `Docs/tutorial/pdf-export.md` | Media | v2.5.0 |
| TODO-006 | Creare l'automazione del Release System | Bassa | v2.5.0 |
| TODO-007 | Popolare `ApprovedAssets/Text/` per il progetto Proto Emperor | Alta | Attivo (non v2.5.0 — lavoro corrente) |
| TODO-008 | Popolare `ApprovedAssets/Images/` per il progetto Proto Emperor | Alta | Attivo (non v2.5.0 — lavoro corrente) |

TODO-002 usa "15 icone", confermando che `STATUS.md` appartiene al gruppo di documenti coerente con "15 icone" (§2) — un ulteriore indizio che la versione con "10 icone" in `ROADMAP.md` è quella disallineata.

TODO-007 e TODO-008 non riguardano una funzionalità futura: sono lavoro sul progetto di esempio Proto Emperor, disponibile da fare subito (vedi Capitolo 13).

---

## 4. Timeline completa dello scope pianificato (da ROADMAP.md)

`ROADMAP.md` contiene anche scope per versioni oltre la 2.5.0. Questo materiale è utile per capire la direzione a lungo termine, ma **nessuna parte di esso è vincolante** — il documento stesso si definisce "a living document [che] reflects current intentions, not binding commitments".

| Versione | Target | Tema principale |
|----------|--------|-------------------|
| v2.5.0 | Q3 2026 | Automazione e tooling (vedi discrepanza §2) |
| v3.0.0 | 2025* | Piattaforma e community: web prompt runner, sistema plugin, libreria community di manuali approvati |

> 📝 **Nota:** `ROADMAP.md` riporta "Target: 2025" per v3.0.0 in una sezione e "Target: 2025" ripetuto in un'altra sezione più recente dello stesso file, mentre v2.5.0 è targettizzata Q3 2026 — cronologicamente v3.0.0 precederebbe v2.5.0. Questo è quasi certamente un refuso di data non aggiornato in una revisione precedente del documento, non un piano reale. Non usare le date di `ROADMAP.md` per pianificazione — usare solo l'ordine delle versioni (2.5.0 prima di 3.0.0).

Obiettivi a lungo termine senza versione assegnata: Community Model Library (repository pubblico di manuali approvati via PR), Video Manual Support, variante tattile/alto contrasto per accessibilità, CLI tool (`mini4wd-sdk init/qa/export`).

**Esplicitamente fuori scope per l'SDK** (`ROADMAP.md § What Will Not Be Added`): contenuto specifico per modello (vive in `Projects/`), integrazioni dirette con provider AI (l'SDK è testo di prompt, non software), raccomandazioni di marca vernice, contenuto racing/prestazionale.

---

## 5. Come proporre una funzionalità

1. Aprire una GitHub Issue con titolo `[Feature] Breve descrizione`
2. Applicare la label `roadmap`
3. Descrivere: problema, soluzione proposta, componenti SDK coinvolti, se richiede un bump di versione MAJOR
4. Un maintainer effettua il triage e assegna a una milestone (o marca `wontfix` con motivazione)

> 📝 **Nota:** questo flusso presuppone un repository GitHub con issue tracker attivo — vedi Capitolo 16 per lo stato reale del workflow GitHub di questo repository.

---

## Vedi anche

- Capitolo 02 — SDKContext (versione corrente, gerarchia di autorità tra i file di bootstrap)
- Capitolo 13 — GoldenProjects (TODO-007/008 in dettaglio)
- Capitolo 15 — Versioning (storico versioni effettivamente rilasciate)
- Capitolo 16 — GitHubWorkflow (issue tracker e label `roadmap`)
