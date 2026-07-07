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
import json
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
PAGE_WIDTH_PX = round(210 * PX_PER_MM)
PAGE_HEIGHT_PX = round(297 * PX_PER_MM)

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


# File di stile sempre allegati alla generazione di un'illustrazione (path relativi
# alla root del repo). Non piu' Core/COMPONENT_SYSTEM.md/QA_SYSTEM.md: l'AI non
# tocca layout di pagina, solo stile fotografico/illuminazione.
STYLE_REFERENCE_FILES = [
    "Core/RENDER_GUIDE.md",
    "Core/DESIGN_LANGUAGE.md",
    "Core/STYLE_GUIDE.md",
]

# Fonte unica del prompt Fase 4 (vedi Docs/AI_BOOTSTRAP_PROMPT.md § FASE 4 -> 4b,
# che ora rimanda qui invece di duplicarlo): genera SOLO l'illustrazione, mai testo
# o layout di pagina (quello lo fa il template). Lo schema colori e' inline nel
# prompt (non richiede che chi genera l'immagine legga PROJECT.yaml a parte) - utile
# soprattutto per un futuro nodo locale, dove non esiste un concetto di "allegato in
# chat" da cui l'AI possa leggere un file a parte.
#
# Il path di destinazione NON e' nel testo del prompt: ChatGPT Web non puo' scrivere
# su un filesystem, restituisce solo l'immagine in chat - istruirlo a "salvare a un
# path" e' un'istruzione a cui non puo' dare seguito. Il path resta fuori dal
# prompt copiabile: campo output_path nel JSON (per un futuro nodo batch) e riga
# "Salva come:" nel .md (per l'operatore umano).
PROMPT_TEMPLATE = """Genera SOLO un'illustrazione fotorealistica del modellino Mini4WD — {tipo_slot}.
Nessun testo, nessuna tabella, nessun logo, nessun pannello colorato: solo il
soggetto isolato su sfondo bianco puro. Questa immagine viene inserita in un
template gia' pronto che aggiunge testo/tabelle/header per conto suo — se aggiungi
tu del testo o una cornice, il risultato finale avra' doppioni o elementi in
conflitto col template.

Regole:
- Forma fisica (sagoma, proporzioni, componenti meccanici) il piu' fedele possibile
  alle foto di riferimento allegate.
- Colori, livrea, fiamme, decal e grafica NON derivano dalle foto di riferimento —
  sono quasi sempre box-art stock con schema colori diverso da quello da
  documentare. Palette e aree di applicazione vengono SOLO dallo schema colori
  sotto. Se la livrea della foto reference e' in conflitto, ignora la livrea della
  foto e ridipingi secondo lo schema sotto — non mescolare o "tingere" i colori
  esistenti. Non aggiungere grafiche (fiamme, strisce, numeri di gara) assenti
  dallo schema colori.
- Applica Core/DESIGN_LANGUAGE.md e Core/STYLE_GUIDE.md per stile fotografico/
  illuminazione, non per layout di pagina (quello lo fa il template).

Schema colori ({scheme_name}):
{colors_block}

Dettaglio specifico per questo slot: {descrizione_slot}
"""

# P004 (Preparazione) precede la verniciatura (Fase 5/P005): il modello a questo
# stadio NON e' ancora colorato con lo schema finale. Usare PROMPT_TEMPLATE
# (con lo schema colori) qui produrrebbe foto con la carrozzeria gia' verniciata,
# sbagliato per uno step di lavaggio/carteggiatura/primer. Corretto 2026-07-06 dopo
# user testing su GPT Web: errore trovato nelle immagini generate per questa pagina.
PROMPT_TEMPLATE_UNPAINTED = """Genera SOLO un'illustrazione fotorealistica del modellino Mini4WD — {tipo_slot}.
Nessun testo, nessuna tabella, nessun logo, nessun pannello colorato: solo il
soggetto isolato su sfondo bianco puro. Questa immagine viene inserita in un
template gia' pronto che aggiunge testo/tabelle/header per conto suo — se aggiungi
tu del testo o una cornice, il risultato finale avra' doppioni o elementi in
conflitto col template.

Regole:
- Forma fisica (sagoma, proporzioni, componenti meccanici) il piu' fedele possibile
  alle foto di riferimento allegate.
- IMPORTANTE — questa e' una fase di PREPARAZIONE, precedente alla verniciatura:
  {stato_colore} Non mostrare NESSUNO dei colori dello schema di verniciatura
  finale del progetto (niente azzurro, rosa, o altri colori — quelli vengono
  applicati solo a partire dalla Fase 5, non in questa pagina). Se le foto di
  riferimento mostrano una livrea box-art colorata, ignorala: qui il soggetto deve
  apparire neutro/non verniciato, non nella sua colorazione finale.
- Applica Core/DESIGN_LANGUAGE.md e Core/STYLE_GUIDE.md per stile fotografico/
  illuminazione, non per layout di pagina (quello lo fa il template).

Dettaglio specifico per questo slot: {descrizione_slot}
"""


def is_primer_step(step: dict) -> bool:
    text = f"{step.get('title', '')} {step.get('description', '')}".lower()
    return "primer" in text


def colors_block(colors_by_id: dict) -> str:
    lines = []
    for c in colors_by_id.values():
        lines.append(
            f"- {c.get('paintName', c.get('name', '?'))} ({c.get('paintCode', '?')}, "
            f"{finish_it(c.get('finish', ''))}) — hex {c.get('hex', '?')}"
            + (f" — {c['notes']}" if c.get("notes") else "")
        )
    return "\n".join(lines) if lines else "(nessuno schema colori trovato in PROJECT.yaml)"


def slot_description(page_id: str, slot: str, content: dict) -> tuple[str, str]:
    """Ritorna (tipo_slot, descrizione_slot) per un singolo slot immagine mancante,
    compilati dai dati reali del content.yaml — non lasciati come placeholder."""
    if page_id == "P001":
        r = content["render"]
        return "copertina", f"vista {r.get('angle', '3/4 front-left')}, illuminazione {r.get('lighting', 'studio-neutral')}. {r.get('alt', '')}"

    if page_id == "P002":
        names = {"front": "frontale", "side": "laterale", "top": "dall'alto"}
        r = content["renders"][slot]
        return f"vista ortogonale {names.get(slot, slot)}", f"nessuna prospettiva, sfondo bianco. {r.get('alt', '')}"

    if page_id == "P004" and slot.startswith("step"):
        step_id = int(slot.removeprefix("step"))
        step = next(s for s in content["steps"] if s["id"] == step_id)
        return "foto di dettaglio/preparazione", f"Step {step_id} — {step['title']}: {step['description']}"

    if page_id == "P006" and slot.startswith("zone_"):
        zone_id = slot.removeprefix("zone_")
        zone = next(z for z in content["zones"] if z["id"] == zone_id)
        return "foto di dettaglio/mascheratura", f"Zona {zone_id} — {zone['area']} ({zone['masking_type']}). {zone.get('notes', '')}"

    if page_id == "P007" and slot.startswith("area_"):
        area_id = slot.removeprefix("area_")
        area = next(a for a in content["areas"] if a["id"] == area_id)
        return "foto di dettaglio", f"{area['name']}: {area['description']} {area.get('notes', '')}"

    if page_id == "P008" and slot.startswith("decal"):
        idx = int(slot.removeprefix("decal"))
        decal = content["decals"][idx - 1]
        return "foto di dettaglio/decal", str(decal)

    return "illustrazione", "(descrizione non disponibile — verifica manualmente content.yaml)"


def build_prompt_entries(variant_dir: Path, model: str, variant: str, project: dict, colors_by_id: dict,
                          page_id: str, content: dict, missing: list) -> list:
    scheme_name = project.get("paintScheme", {}).get("name", "") if project else ""
    colors_txt = colors_block(colors_by_id)

    images_dir = variant_dir / "Images"
    ref_photos = sorted(p.name for p in images_dir.glob("ref_*.jp*g")) if images_dir.is_dir() else []
    project_prefix = f"Projects/{model}/{variant}"
    reference_files = STYLE_REFERENCE_FILES + [f"{project_prefix}/PROJECT.yaml"]
    reference_files += [f"{project_prefix}/Images/{name}" for name in ref_photos]

    entries = []
    for slot, rel_path in missing:
        tipo_slot, descrizione_slot = slot_description(page_id, slot, content)

        if page_id == "P004" and slot.startswith("step"):
            step_id = int(slot.removeprefix("step"))
            step = next(s for s in content["steps"] if s["id"] == step_id)
            stato_colore = (
                "Il corpo e' ricoperto da un primer bianco opaco uniforme — nessun colore dello schema di verniciatura ancora applicato."
                if is_primer_step(step)
                else "Il corpo e' plastica ABS grezza non verniciata, nel colore naturale di stampo (bianco/neutro/traslucido) — nessuna vernice applicata."
            )
            prompt = PROMPT_TEMPLATE_UNPAINTED.format(
                tipo_slot=tipo_slot,
                stato_colore=stato_colore,
                descrizione_slot=descrizione_slot,
            )
        else:
            prompt = PROMPT_TEMPLATE.format(
                tipo_slot=tipo_slot,
                scheme_name=scheme_name,
                colors_block=colors_txt,
                descrizione_slot=descrizione_slot,
            )

        entries.append({
            "page_id": page_id,
            "slot": slot,
            "output_path": f"{project_prefix}/{rel_path}",
            "tipo_slot": tipo_slot,
            "descrizione_slot": descrizione_slot,
            "reference_files": reference_files,
            "prompt": prompt,
        })
    return entries


def write_prompt_files(md_path: Path, json_path: Path, model: str, variant: str, entries: list) -> None:
    json_path.write_text(
        json.dumps({"model": model, "variant": variant, "generated_at": datetime.now().isoformat(timespec="minutes"),
                    "entries": entries}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [
        "# Prompt per le immagini mancanti",
        "",
        "> File generato automaticamente da `Scripts/render_page.py` — non modificare a mano,",
        f"> viene riscritto ad ogni run. Ultimo aggiornamento: {datetime.now():%Y-%m-%d %H:%M}.",
        "> Versione machine-readable (stessi dati, per un futuro nodo di generazione locale in batch): "
        f"`{json_path.name}`.",
        "",
        f"Progetto: `{model}/{variant}`",
        "",
    ]
    if not entries:
        lines.append("Nessuna immagine mancante — niente da generare.")
    else:
        for e in entries:
            lines.append(f"## {e['page_id']} — {e['slot']}")
            lines.append("")
            lines.append(f"**Salva come:** `{e['output_path']}`")
            lines.append("")
            lines.append("**File da allegare:**")
            for f in e["reference_files"]:
                lines.append(f"- `{f}`")
            lines.append("")
            lines.append("**Prompt:**")
            lines.append("```")
            lines.append(e["prompt"].rstrip())
            lines.append("```")
            lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def mm(value: float) -> str:
    return f"{round(value * PX_PER_MM)}px"


def finish_it(value: str) -> str:
    return FINISH_IT.get(value, value.upper())


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg")


def resolve_images(variant_dir: Path, slots: dict) -> dict:
    """Per ogni slot: {"path": path_relativo, "data_uri": stringa o None se il file non esiste}.

    Il path dichiarato (in content.yaml o nella convenzione fissa) usa sempre
    estensione .png, ma accetta anche .jpg/.jpeg allo stesso nome file — l'AI che
    genera l'immagine puo' restituire l'uno o l'altro formato indifferentemente."""
    resolved = {}
    for slot, rel_path in slots.items():
        stem_path = Path(rel_path).with_suffix("")
        candidates = [rel_path] + [f"{stem_path}{ext}" for ext in IMAGE_EXTENSIONS]
        found_path = next((c for c in dict.fromkeys(candidates) if (variant_dir / c).exists()), None)

        data_uri = None
        if found_path:
            full_path = variant_dir / found_path
            ext = full_path.suffix.lstrip(".").lower()
            mime = "jpeg" if ext == "jpg" else ext
            encoded = base64.b64encode(full_path.read_bytes()).decode("ascii")
            data_uri = f"data:image/{mime};base64,{encoded}"
        resolved[slot] = {"path": found_path or rel_path, "data_uri": data_uri}
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
    project = {}
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
    prompt_entries = []

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
            browser_page = browser.new_page(viewport={"width": PAGE_WIDTH_PX, "height": PAGE_HEIGHT_PX})
            browser_page.set_content(html)
            browser_page.wait_for_timeout(100)
            if fmt == "pdf":
                # I nostri px CSS sono pensati a 150dpi (PX_PER_MM), ma Chromium converte
                # i CSS px in mm usando lo standard browser (96dpi) quando genera il PDF -
                # 1240px a 96dpi sono ~328mm, non 210mm: il contenuto sconfina ben oltre la
                # pagina dichiarata e Chromium apre una seconda pagina per il residuo.
                # scale=96/150 compensa esattamente questo scarto di densita'.
                browser_page.pdf(
                    path=str(output_path), width="210mm", height="297mm", print_background=True,
                    margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                    scale=96 / 150,
                )
            else:
                browser_page.screenshot(path=str(output_path), full_page=True)
            browser_page.close()

            rendered_count += 1
            print(f"Generato: {output_path}")

            missing = [(slot, v["path"]) for slot, v in images.items() if v["data_uri"] is None]
            if missing:
                missing_by_page[page_id] = missing
                prompt_entries += build_prompt_entries(
                    variant_dir, model_name, variant_name, project, colors_by_id, page_id, content, missing
                )

        browser.close()

    if skipped_pages:
        print(f"Pagine saltate (nessun template): {', '.join(skipped_pages)}")

    report_path = variant_dir / "MISSING_IMAGES.md"
    write_missing_report(report_path, model_name, variant_name, missing_by_page, skipped_pages)

    prompt_md_path = variant_dir / "MISSING_IMAGES_PROMPT.md"
    prompt_json_path = variant_dir / "MISSING_IMAGES.json"
    write_prompt_files(prompt_md_path, prompt_json_path, model_name, variant_name, prompt_entries)

    total_missing = sum(len(v) for v in missing_by_page.values())
    print(f"\n{rendered_count} pagine renderizzate. {total_missing} immagini mancanti.")
    print(f"Report: {report_path}")
    print(f"Prompt pronti: {prompt_md_path} ({prompt_json_path} per uso batch)")


if __name__ == "__main__":
    main()
