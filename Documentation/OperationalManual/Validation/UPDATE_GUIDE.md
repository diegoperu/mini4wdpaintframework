# UPDATE_GUIDE.md

**Manuale Operativo — Mini4WD Manual SDK**
**Audience:** manutentore del Manuale Operativo (umano o AI)
**Generato il:** 2026-07-02

Guida procedurale: cosa fare quando esce una nuova release dello SDK (es. v2.4.0 → v2.5.0).

---

## 1. Quali documenti verificare

Confronta `VERSION`, `CHANGELOG.md` e `ReleaseInfo.yaml` della nuova release con la versione registrata in `DOCUMENTATION_STATUS.yaml → documentation.sdk_version`. Poi, in ordine:

1. `SDK_CONTEXT.yaml` — versione, codename, `load_order`, `roadmap` (voci spostate da "planned" a "implemented"?)
2. `AI_ENTRYPOINT.md` — Golden Rules aggiunte/rimosse, fasi del `Workflow` cambiate, `Cross References` nuove
3. `RepositoryManifest.yaml` — nuovi file aggiunti, `depends_on` modificati, `ai_load_order` cambiato
4. `MANIFEST.yaml` — nuovi Page ID / Component ID (`next_available_component_id`), nuovi `content_formats`
5. Ogni file in `Core/` — diff riga per riga contro la versione precedente (sono la Source of Truth più autorevole)
6. `Config/*.yaml` — soglie, policy, parametri
7. `Tests/*.md` — nuove suite o item aggiunti/rimossi

Usa `git diff v{OLD}..v{NEW} -- Core/ Config/ AI_ENTRYPOINT.md SDK_CONTEXT.yaml RepositoryManifest.yaml MANIFEST.yaml` come primo comando.

## 2. Quali capitoli del manuale controllare

Non rileggere tutti i 20 capitoli. Usa `CHANGE_IMPACT.md`: per ogni file modificato al punto 1, la matrice elenca esattamente quali capitoli sono impattati. Controlla solo quelli.

Se un file modificato **non compare** in `CHANGE_IMPACT.md` (documento nuovo), aggiungilo prima alla mappa (vedi punto 4) e poi determina il capitolo di destinazione per analogia con `DOCUMENT_COVERAGE.md`.

## 3. Quali checklist eseguire

Nell'ordine:

1. `COVERAGE_CHECKLIST.md` — verifica che ogni area del framework abbia ancora un capitolo assegnato (nuove aree introdotte dalla release richiedono una nuova voce)
2. `CONSISTENCY_CHECK.md` (Parte 1) — su ogni capitolo toccato al punto 2
3. `CONSISTENCY_CHECK.md` (Parte 2) — ripeti i controlli C1–C9 sulla baseline aggiornata, aggiorna gli esiti

## 4. Come aggiornare la Traceability Matrix

In `TRACEABILITY_MATRIX.md`:

- **File modificato, nessun nuovo capitolo coinvolto:** aggiorna solo la data implicita (il file non ha timestamp per riga — l'aggiornamento è tracciato da `DOCUMENTATION_STATUS.yaml → documentation.validated`)
- **File nuovo:** aggiungi una nuova catena in Parte 1 (se documento "principale", cioè con `ai_load_order` non nullo in `RepositoryManifest.yaml`, o Source of Truth di un capitolo) oppure una riga in Parte 2 (documento secondario)
- **File rimosso/deprecato:** rimuovi la catena/riga, e verifica in `DOCUMENT_COVERAGE.md` se il capitolo che lo citava come Source of Truth ha bisogno di un nuovo SoT
- **Nuova dipendenza tra documenti esistenti** (es. un nuovo `depends_on` in `RepositoryManifest.yaml`): aggiungi un hop alla catena esistente

## 5. Come incrementare la versione del Manuale Operativo

Il Manuale Operativo ha un proprio numero di versione, indipendente dallo SDK (stesso principio di `manualVersion` in `PROJECT.yaml`, vedi `Core/MANUAL_SYSTEM.md § 7`). Applica SemVer:

- **MAJOR** — la struttura dei capitoli cambia (rinumerazione, capitoli rimossi/uniti) — richiede riscrittura di `DOCUMENT_COVERAGE.md`, `TRACEABILITY_MATRIX.md`, `COVERAGE_CHECKLIST.md`, `CHANGE_IMPACT.md`
- **MINOR** — un nuovo capitolo viene aggiunto, oppure una release SDK MAJOR/MINOR introduce nuove aree da documentare (es. v2.5.0 `Compiler/` diventerà un nuovo capitolo quando passa da "planned" a "implemented")
- **PATCH** — correzioni, aggiornamento riferimenti dopo una release SDK PATCH, correzione di inconsistenze trovate da `CONSISTENCY_CHECK.md`

Aggiorna `DOCUMENTATION_STATUS.yaml → documentation.version` e `generated_from_sdk` a ogni incremento.

## 6. Come verificare che il manuale sia ancora coerente con il framework

Sequenza minima da eseguire prima di considerare l'aggiornamento completo:

1. `CONSISTENCY_CHECK.md` Parte 1 su tutti i capitoli impattati → tutti PASS
2. `COVERAGE_CHECKLIST.md` → nessuna area del framework priva di capitolo
3. Verifica manuale: nessun file citato in un capitolo con path inesistente (`find` per ogni backtick-path citato)
4. `DOCUMENTATION_STATUS.yaml → status.warnings` è vuoto o ogni warning ha un TODO associato
5. Aggiorna `status.reviewed` e `status.validated` in `DOCUMENTATION_STATUS.yaml` con la data del controllo

Se uno di questi step fallisce, il manuale **non va marcato come `validated: true`** — resta in stato `pending_review`.

---

## Checklist rapida per ogni release (riepilogo)

- [ ] Diff dei documenti chiave dello SDK (§1)
- [ ] Identificati i capitoli impattati via `CHANGE_IMPACT.md` (§2)
- [ ] Eseguite le 3 checklist in ordine (§3)
- [ ] `TRACEABILITY_MATRIX.md` aggiornata (§4)
- [ ] Versione del Manuale Operativo incrementata secondo SemVer (§5)
- [ ] `DOCUMENTATION_STATUS.yaml` aggiornato con esito finale (§6)
