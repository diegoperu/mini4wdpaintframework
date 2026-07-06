#!/usr/bin/env python3
"""Prototipo: renderizza una pagina del manuale da content.yaml usando un template
HTML/CSS statico (Jinja2 + Playwright), invece di chiedere a un'AI generativa di
produrre testo/tabelle dentro un'immagine.

Copre solo il testo/layout deterministico (header, footer, palette, tabelle, callout).
L'illustrazione (render del modellino, viste ortogonali) resta un placeholder finché
non esiste una fonte per quell'immagine (Fase 4 — AI locale o ChatGPT).

Uso:
  Scripts/render_page.py <content.yaml> <output.pdf/png>

Esempio:
  Scripts/render_page.py \\
    Projects/Magnum_Saber_Premium/Cotton_Candy_Drift/ApprovedText/P002/content.yaml \\
    /tmp/P002_preview.pdf
"""

import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
TOKENS_PATH = REPO_ROOT / "Assets/DesignSystem/Tokens/tokens.example.yaml"

PX_PER_MM = 150 / 25.4  # A4 @ 150dpi

# PROJECT.yaml tiene paintScheme.colors[].finish in inglese ("gloss"/"metallic") --
# valore di lavoro interno, mai da mostrare cosi' com'e' in una pagina (Core/
# AI_OPERATING_RULES.md, italiano zero-tolerance). I content.yaml delle pagine di
# testo gia' traducono a mano ("Lucido"/"Metallizzato"); quando il template risolve
# il colore direttamente da PROJECT.yaml (color_id -> colore), serve la stessa resa.
FINISH_IT = {"gloss": "LUCIDO", "metallic": "METALLIZZATO"}


def mm(value: float) -> str:
    return f"{value * PX_PER_MM:.2f}px"


def finish_it(value: str) -> str:
    return FINISH_IT.get(value, value.upper())


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <content.yaml> <output.pdf|output.png>", file=sys.stderr)
        sys.exit(1)

    content_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    content = load_yaml(content_path)
    tokens = load_yaml(TOKENS_PATH)["tokens"]

    # Variant dir: .../{Model}/{Variant}/ApprovedText/{Page}/content.yaml
    variant_dir = content_path.resolve().parents[2]
    project_yaml_path = variant_dir / "PROJECT.yaml"
    colors_by_id = {}
    if project_yaml_path.exists():
        project = load_yaml(project_yaml_path)
        for c in project.get("paintScheme", {}).get("colors", []):
            colors_by_id[c["id"]] = c

    page_id = content["page"]["id"]
    template_name = f"{page_id}.html.jinja"
    if not (TEMPLATES_DIR / template_name).exists():
        print(f"Errore: nessun template per {page_id} in {TEMPLATES_DIR}", file=sys.stderr)
        sys.exit(1)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    env.filters["mm"] = mm
    env.filters["finish_it"] = finish_it
    # anche disponibile come funzione globale nel template (usata per le dimensioni pagina)
    env.globals["mm"] = mm

    template = env.get_template(template_name)
    html = template.render(content=content, tokens=tokens, colors_by_id=colors_by_id)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.wait_for_timeout(100)

        if output_path.suffix.lower() == ".pdf":
            page.pdf(path=str(output_path), width="210mm", height="297mm", print_background=True)
        else:
            page.screenshot(path=str(output_path), full_page=True)

        browser.close()

    print(f"Generato: {output_path}")


if __name__ == "__main__":
    main()
