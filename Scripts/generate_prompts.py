#!/usr/bin/env python3
"""
Mini4WD Manual SDK v2.4.1 — Generatore Prompt Precompilati
===========================================================
Legge PROJECT.yaml e genera tutti i prompt Fase 2 / QA / Sigillatura
pronti per il copia-incolla, per le sole pagine attive del progetto.

Utilizzo:
    python generate_prompts.py <percorso/PROJECT.yaml> [opzioni]

Opzioni:
    --runtime claude      Prompt per Claude Code (default)
    --runtime chatgpt     Prompt per ChatGPT Web (ZIP)
    --output FILE.txt     Salva su file invece di stampare a schermo

Richiede Python 3.7+ e PyYAML:
    pip install pyyaml
"""

import sys
import os
import argparse

try:
    import yaml
except ImportError:
    print("Errore: PyYAML non installato.")
    print("Esegui: pip install pyyaml")
    sys.exit(1)

# ============================================================
# DEFINIZIONE PAGINE
# ============================================================

PAGES = [
    {"id": "P001", "name": "Copertina",         "file": "Cover.md",          "required": True},
    {"id": "P002", "name": "Schema Colori",      "file": "ColorScheme.md",    "required": True},
    {"id": "P003", "name": "Materiali",          "file": "Materials.md",      "required": True},
    {"id": "P004", "name": "Preparazione",       "file": "Preparation.md",    "required": True},
    {"id": "P005", "name": "Verniciatura",       "file": "Painting.md",       "required": True},
    {"id": "P006", "name": "Mascheratura",       "file": "Masking.md",        "required": True},
    {"id": "P007", "name": "Dettagli",           "file": "Details.md",        "required": True},
    {"id": "P008", "name": "Decalcomanie",       "file": "Decals.md",         "required": None},  # condizionale
    {"id": "P009", "name": "Variante Premium",   "file": "Premium.md",        "required": False}, # opzionale
    {"id": "P010", "name": "Checklist Finale",   "file": "FinalChecklist.md", "required": True},
]

SEP = "=" * 66
SEP_THIN = "-" * 66

# ============================================================
# INPUT UTENTE
# ============================================================

def ask_yes_no(question, default=None):
    hints = {True: "[S/n]", False: "[s/N]", None: "[s/n]"}
    while True:
        raw = input(f"{question} {hints[default]}: ").strip().lower()
        if raw == "" and default is not None:
            return default
        if raw in ("s", "si", "sì", "y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  Risposta non valida. Digita s (sì) o n (no).")

# ============================================================
# GENERATORI PROMPT
# ============================================================

def prompt_fase2(page, model_name, runtime):
    pid  = page["id"]
    name = page["name"]
    pf   = page["file"]

    if runtime == "claude":
        read_step  = f"Leggi il file PromptEngine/{pf} nel repository."
        write_step = (
            f"Genera il file content.yaml completo per questa pagina e scrivilo in\n"
            f"   ApprovedAssets/Text/{pid}/content.yaml."
        )
    else:
        read_step  = f"Leggi il file PromptEngine/{pf} dallo ZIP che hai già caricato."
        write_step = "Genera il file content.yaml completo per questa pagina."

    return f"""\
[PROMPT FASE 2 — {pid} {name}]

Fase 2 — Text Engine.
Genera la pagina {pid} ({name}) del manuale per il modello {model_name}.

1. {read_step}
2. Estrai tutti i valori dal PROJECT.yaml caricato in precedenza.
3. Risolvi i riferimenti per ID: se paintSequence usa colorId, cerca il colore
   corrispondente in paintScheme.colors (dove id == colorId) ed estrai paintCode,
   paintName, finish, hex. Non lasciare TODO: per valori raggiungibili tramite
   riferimento — usa TODO: solo per dati genuinamente assenti nel PROJECT.yaml.
4. {write_step}
5. Usa TODO: per qualsiasi valore non disponibile in PROJECT.yaml — non inventare nulla.
6. Tutto il testo editoriale in italiano; codici e nomi commerciali restano invariati.

Non procedere al rendering: siamo in Text Mode. Output atteso: solo il content.yaml,
pronto per la validazione QA.
"""


def prompt_qa(page, runtime):
    pid  = page["id"]
    name = page["name"]

    if runtime == "claude":
        target = f"in ApprovedAssets/Text/{pid}/content.yaml"
    else:
        target = "appena generato"

    return f"""\
[PROMPT QA (Fase 3) — {pid} {name}]

Fase 3 — QA. Esegui la validazione completa sul content.yaml {target}.

Ambito: questo è CONTENUTO GENERATO (status: review), non un template. Applica
Tests/ContentValidation.md §Validation Scope.

Content Validation: applica tutte e 7 le suite di Tests/ContentValidation.md.
Text Validation: applica tutti e 9 i test di Tests/TextValidation.md.

Ricorda le eccezioni language-neutral: codici vernice (TS-37, X-10, PS-1…),
nomi commerciali (Chrome Silver, Gun Metal, Flat Black, Primer…), chiavi YAML
e valori di schema NON sono violazioni linguistiche.

Riporta:
- Esito per suite: PASS / FAIL / WARNING
- Ogni FAIL con riga e correzione necessaria
- Verdetto finale: APPROVED / REJECTED
"""


def prompt_sigillatura(page):
    pid  = page["id"]
    name = page["name"]
    return f"""\
[SIGILLATURA — {pid} {name}]

Approvato. Sigilla la pagina {pid}:
ApprovedAssets/Text/{pid}/metadata.yaml → status: locked
Aggiungi riga di changelog in ApprovedAssets/Text/{pid}/changelog.md.
"""

# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Mini4WD Manual SDK — Generatore Prompt Precompilati"
    )
    parser.add_argument("project_yaml", help="Percorso del PROJECT.yaml")
    parser.add_argument(
        "--runtime",
        choices=["claude", "chatgpt"],
        default="claude",
        help="Runtime target: claude (default) o chatgpt",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        help="Salva i prompt su file (default: stampa a schermo)",
    )
    args = parser.parse_args()

    # --- Carica PROJECT.yaml ---
    if not os.path.isfile(args.project_yaml):
        print(f"Errore: file non trovato: {args.project_yaml}")
        sys.exit(1)

    with open(args.project_yaml, encoding="utf-8") as f:
        project = yaml.safe_load(f)

    model_name = (
        project.get("project", {}).get("modelName")
        or project.get("modelName")
        or "NOME_MODELLO"
    )
    decals          = project.get("decals", [])
    premium_enabled = project.get("premiumVariant", {}).get("enabled", False)

    # --- Banner ---
    print()
    print(SEP)
    print("  Mini4WD Manual SDK — Generatore Prompt")
    print(SEP)
    print(f"  Modello : {model_name}")
    print(f"  Runtime : {args.runtime}")
    print(f"  Progetto: {args.project_yaml}")
    print(SEP)
    print()

    # --- Determina pagine attive ---
    active_pages = []
    for page in PAGES:
        if page["required"] is True:
            active_pages.append(page)

        elif page["id"] == "P008":
            if decals:
                active_pages.append(page)
                print(f"  P008 Decalcomanie — INCLUSA (decals definite in PROJECT.yaml)")
            else:
                print(f"  P008 Decalcomanie — decals: [] rilevato in PROJECT.yaml")
                include = ask_yes_no("  Includere P008 Decalcomanie?", default=False)
                if include:
                    active_pages.append(page)

        elif page["id"] == "P009":
            if premium_enabled:
                active_pages.append(page)
                print(f"  P009 Variante Premium — INCLUSA (premiumVariant.enabled: true)")
            else:
                print(f"  P009 Variante Premium — premiumVariant.enabled: false in PROJECT.yaml")
                include = ask_yes_no("  Includere P009 Variante Premium?", default=False)
                if include:
                    active_pages.append(page)

    print()
    print(f"  Pagine attive ({len(active_pages)}):")
    for i, p in enumerate(active_pages, 1):
        print(f"    {i:2}. {p['id']} — {p['name']}")
    print()

    # --- Genera prompt ---
    lines = []
    lines.append(SEP)
    lines.append(f"  PROMPT PRECOMPILATI — {model_name}")
    lines.append(f"  Runtime : {args.runtime}")
    lines.append(f"  Pagine  : {', '.join(p['id'] for p in active_pages)}")
    lines.append(SEP)
    lines.append("")

    for i, page in enumerate(active_pages, 1):
        header = f"  PAGINA {i}/{len(active_pages)} — {page['id']} {page['name']}"
        lines.append(SEP)
        lines.append(header)
        lines.append(SEP)
        lines.append("")

        lines.append(SEP_THIN)
        lines.append(f"  STEP 1 di 3 — Genera content.yaml")
        lines.append(SEP_THIN)
        lines.append(prompt_fase2(page, model_name, args.runtime))

        lines.append(SEP_THIN)
        lines.append(f"  STEP 2 di 3 — QA (invia dopo aver ricevuto content.yaml)")
        lines.append(SEP_THIN)
        lines.append(prompt_qa(page, args.runtime))

        lines.append(SEP_THIN)
        lines.append(f"  STEP 3 di 3 — Sigilla (solo se QA: APPROVED)")
        lines.append(SEP_THIN)
        lines.append(prompt_sigillatura(page))
        lines.append("")

    output_text = "\n".join(lines)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"  Prompt salvati in: {args.output}")
        print()
    else:
        print(output_text)


if __name__ == "__main__":
    main()
