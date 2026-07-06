#!/usr/bin/env python3
"""Renderizza tutte le pagine di un progetto/variante da content.yaml usando un
template HTML/CSS statico (Jinja2 + Playwright), invece di chiedere a un'AI
generativa di produrre testo/tabelle dentro un'immagine.

Copre il testo/layout deterministico (header, footer, palette, tabelle, callout) al
100%. Le illustrazioni (render del modellino, viste ortogonali, foto di dettaglio)
vengono agganciate per path fisso da Images/: se il file esiste viene incorporato,
altrimenti resta un placeholder tratteggiato con il path esatto mancante — così un
gap si vede e si corregge subito, non genera un errore silenzioso.

Uso:
  Scripts/render_page.py <Model> <Variant> [png|pdf]

Esegue in automatico su TUTTE le pagine ApprovedText/P0xx del progetto indicato
(nessun input interattivo, nessun path da costruire a mano). {Model} e {Variant}
sono nomi di cartella sotto Projects/ — risolti sempre a partire dalla root del
repository, non dalla directory corrente: lo script funziona da qualunque cwd.

Output:
- Build/Preview/{Model}_{Variant}_{PageID}.png (o .pdf) per ogni pagina
- Projects/{Model}/{Variant}/MISSING_IMAGES.md — report di tutte le immagini
  mancanti in tutto il progetto, riscritto ad ogni run

Esempio:
  Scripts/render_page.py Magnum_Saber_Premium Cotton_Candy_Drift
"""

import base64
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
TOKENS_PATH = REPO_ROOT / "Assets/DesignSystem/Tokens/tokens.example.yaml"
OUTPUT_DIR = REPO_ROOT / "Build/Preview"

PAGE_DIR_PATTERN = re.compile(r"^P\d{3}$")

PX_PER_MM = 150 / 25.4  # A4 @ 150dpi

# PROJECT.yaml tiene paintScheme.colors[].finish in inglese ("gloss"/"metallic") --
# valore di lavoro interno, mai da mostrare cosi' com'e' in una pagina (Core/
# AI_OPERATING_RULES.md, italiano zero-tolerance). I content.yaml delle pagine di
# testo gia' traducono a mano ("Lucido"/"Metallizzato"); quando il template risolve
# il colore direttamente da PROJECT.yaml (color_id -> colore), serve la stessa resa.
FINISH_IT = {"gloss": "LUCIDO", "metallic": "METALLIZZATO"}

# Convenzione path immagini per pagina (relativi alla cartella {Model}/{Variant}/).
# P001/P002 usano i path gia' dichiarati nel content.yaml; le altre pagine non hanno
# ancora una convenzione ufficiale nello schema SDK, quindi la fissiamo qui:
#   P004: Images/P004_step{N}.png   (N = steps[].id)
#   P006: Images/P006_{zone_id}.png (es. P006_M001.png)
#   P007: Images/P007_{area_id}.png (es. P007_D001.png)
#   P008: Images/P008_decal{N}.png  (solo se decals[] non vuoto)


def image_slots(page_id: str, content: dict) -> dict:
    if page_id == "P001":
        return {"cover": content["render"]["file"]}
    if page_id == "P002":
        r = content["renders"]
        return {"front": r["front"]["file"], "side": r["side"]["file"], "top": r["top"]["file"]}
    if page_id == "P004":
        return {f"step{s['id']}": f"Images/P004_step{s['id']}.png" for s in content.get("steps", [])}
    if page_id == "P006":
        return {f"zone_{z['id']}": f"Images/P006_{z['id']}.png" for z in content.get("zones", [])}
    if page_id == "P007":
        return {f"area_{a['id']}": f"Images/P007_{a['id']}.png" for a in content.get("areas", [])}
    if page_id == "P008":
        decals = content.get("decals") or []
        return {f"decal{i}": f"Images/P008_decal{i}.png" for i in range(1, len(decals) + 1)}
    return {}


def mm(value: float) -> str:
    return f"{value * PX_PER_MM:.2f}px"


def finish_it(value: str) -> str:
    return FINISH_IT.get(value, value.upper())


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_images(variant_dir: Path, slots: dict) -> dict:
    """Per ogni slot: {"path": path_relativo, "data_uri": stringa o None se il file non esiste}."""
    resolved = {}
    for slot, rel_path in slots.items():
        full_path = variant_dir / rel_path
        data_uri = None
        if full_path.exists():
            ext = full_path.suffix.lstrip(".").lower()
            mime = "jpeg" if ext == "jpg" else ext
            encoded = base64.b64encode(full_path.read_bytes()).decode("ascii")
            data_uri = f"data:image/{mime};base64,{encoded}"
        resolved[slot] = {"path": rel_path, "data_uri": data_uri}
    return resolved


def write_missing_report(report_path: Path, model: str, variant: str, missing_by_page: dict, skipped_pages: list) -> None:
    lines = [
        "# Immagini mancanti",
        "",
        f"> File generato automaticamente da `Scripts/render_page.py` — non modificare a mano,",
        f"> viene riscritto ad ogni run. Ultimo aggiornamento: {datetime.now():%Y-%m-%d %H:%M}.",
        "",
        f"Progetto: `{model}/{variant}`",
        "",
    ]
    if not missing_by_page:
        lines.append("Nessuna immagine mancante — tutte le pagine sono complete.")
    else:
        total = sum(len(v) for v in missing_by_page.values())
        lines.append(f"**{total} immagini mancanti** su {len(missing_by_page)} pagine:")
        lines.append("")
        for page_id, items in missing_by_page.items():
            lines.append(f"## {page_id}")
            for slot, path in items:
                lines.append(f"- `{slot}` → `{path}`")
            lines.append("")
    if skipped_pages:
        lines.append("## Pagine senza template (saltate)")
        for page_id in skipped_pages:
            lines.append(f"- {page_id}")
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if len(sys.argv) not in (3, 4):
        print(f"Uso: {sys.argv[0]} <Model> <Variant> [png|pdf]", file=sys.stderr)
        sys.exit(1)

    model_name = sys.argv[1]
    variant_name = sys.argv[2]
    fmt = sys.argv[3] if len(sys.argv) == 4 else "png"
    if fmt not in ("png", "pdf"):
        print("Errore: formato deve essere 'png' o 'pdf'", file=sys.stderr)
        sys.exit(1)

    variant_dir = REPO_ROOT / "Projects" / model_name / variant_name
    if not variant_dir.is_dir():
        print(f"Errore: cartella progetto non trovata: {variant_dir}", file=sys.stderr)
        sys.exit(1)

    approved_text_dir = variant_dir / "ApprovedText"
    if not approved_text_dir.is_dir():
        print(f"Errore: cartella ApprovedText non trovata: {approved_text_dir}", file=sys.stderr)
        sys.exit(1)

    tokens = load_yaml(TOKENS_PATH)["tokens"]

    project_yaml_path = variant_dir / "PROJECT.yaml"
    colors_by_id = {}
    if project_yaml_path.exists():
        project = load_yaml(project_yaml_path)
        for c in project.get("paintScheme", {}).get("colors", []):
            colors_by_id[c["id"]] = c

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    env.filters["mm"] = mm
    env.filters["finish_it"] = finish_it
    # anche disponibile come funzione globale nel template (usata per le dimensioni pagina)
    env.globals["mm"] = mm

    page_dirs = sorted(
        d for d in approved_text_dir.iterdir() if d.is_dir() and PAGE_DIR_PATTERN.match(d.name)
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    missing_by_page = {}
    skipped_pages = []
    rendered_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for page_dir in page_dirs:
            content_path = page_dir / "content.yaml"
            if not content_path.exists():
                continue

            content = load_yaml(content_path)
            page_id = content["page"]["id"]
            template_name = f"{page_id}.html.jinja"

            if not (TEMPLATES_DIR / template_name).exists():
                skipped_pages.append(page_id)
                continue

            images = resolve_images(variant_dir, image_slots(page_id, content))
            template = env.get_template(template_name)
            html = template.render(content=content, tokens=tokens, colors_by_id=colors_by_id, images=images)

            output_path = OUTPUT_DIR / f"{model_name}_{variant_name}_{page_id}.{fmt}"
            browser_page = browser.new_page()
            browser_page.set_content(html)
            browser_page.wait_for_timeout(100)
            if fmt == "pdf":
                browser_page.pdf(path=str(output_path), width="210mm", height="297mm", print_background=True)
            else:
                browser_page.screenshot(path=str(output_path), full_page=True)
            browser_page.close()

            rendered_count += 1
            print(f"Generato: {output_path}")

            missing = [(slot, v["path"]) for slot, v in images.items() if v["data_uri"] is None]
            if missing:
                missing_by_page[page_id] = missing

        browser.close()

    if skipped_pages:
        print(f"Pagine saltate (nessun template): {', '.join(skipped_pages)}")

    report_path = variant_dir / "MISSING_IMAGES.md"
    write_missing_report(report_path, model_name, variant_name, missing_by_page, skipped_pages)
    total_missing = sum(len(v) for v in missing_by_page.values())
    print(f"\n{rendered_count} pagine renderizzate. {total_missing} immagini mancanti — report in {report_path}")


if __name__ == "__main__":
    main()
