#!/usr/bin/env bash
# Prepara un pacchetto di handoff (zip) per generare UNA illustrazione mancante
# (Fase 4, vedi Docs/AI_BOOTSTRAP_PROMPT.md) in ChatGPT Web o altro runtime immagini.
#
# Dal 2026-07-06 il layout/testo di ogni pagina è prodotto da Scripts/render_page.py
# (template deterministico): l'AI non genera più pagine intere, solo illustrazioni
# isolate (copertina, viste ortogonali, foto di dettaglio). Per questo il pacchetto
# NON contiene più Core/COMPONENT_SYSTEM.md, Core/QA_SYSTEM.md, tokens.example.yaml
# né ApprovedText/ — l'AI non deve più leggere layout di pagina o testo, solo stile
# fotografico (RENDER_GUIDE/DESIGN_LANGUAGE/STYLE_GUIDE) e schema colori
# (PROJECT.yaml → paintScheme.colors[]).
#
# Uso:
#   Scripts/package_handoff.sh <Model> <Variant>
#   Scripts/package_handoff.sh Magnum_Saber_Premium Cotton_Candy_Drift

set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Uso: $0 <Model> <Variant>" >&2
  exit 1
fi

MODEL="$1"
VARIANT="$2"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PROJECT_DIR="Projects/${MODEL}/${VARIANT}"

if [[ ! -d "$PROJECT_DIR" ]]; then
  echo "Errore: cartella progetto non trovata: ${PROJECT_DIR}" >&2
  exit 1
fi

if [[ ! -f "$PROJECT_DIR/PROJECT.yaml" ]]; then
  echo "Errore: PROJECT.yaml non trovato in ${PROJECT_DIR}" >&2
  exit 1
fi

# --- Staging ---
STAGE_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGE_DIR"' EXIT

CORE_FILES=(
  "Core/RENDER_GUIDE.md"
  "Core/DESIGN_LANGUAGE.md"
  "Core/STYLE_GUIDE.md"
)

for f in "${CORE_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "Errore: file core mancante: ${f}" >&2
    exit 1
  fi
  mkdir -p "$STAGE_DIR/$(dirname "$f")"
  cp "$f" "$STAGE_DIR/$f"
done

# File di framing/ruolo alla radice dello zip: senza indicare esplicitamente che il
# compito è generare SOLO un'illustrazione (non una pagina intera), un modello che
# vede un mucchio di file di stile può ancora provare a produrre una pagina completa
# con testo — vedi Docs/RENDER_HANDOFF_CONTEXT.md per la cronologia del problema.
if [[ ! -f "Docs/RENDER_HANDOFF_CONTEXT.md" ]]; then
  echo "Errore: file core mancante: Docs/RENDER_HANDOFF_CONTEXT.md" >&2
  exit 1
fi
cp "Docs/RENDER_HANDOFF_CONTEXT.md" "$STAGE_DIR/HANDOFF_CONTEXT.md"

mkdir -p "$STAGE_DIR/$PROJECT_DIR"
cp "$PROJECT_DIR/PROJECT.yaml" "$STAGE_DIR/$PROJECT_DIR/PROJECT.yaml"

# Solo le foto di riferimento del modello fisico (ref_*.jpg) — MAI le illustrazioni
# P00x_*.png/jpg gia' generate in chat precedenti. Scripts/render_page.py (source of
# truth per "File da allegare" in MISSING_IMAGES_PROMPT.md) elenca solo ref_*.jp*g:
# un pacchetto con dentro anche le altre pagine gia' renderizzate e' piu' pesante del
# necessario e mette davanti al modello immagini irrilevanti per il nuovo slot da
# generare — causa sospetta di un'allucinazione totalmente scollegata osservata con
# Gemini (2026-07-08).
if [[ -d "$PROJECT_DIR/Images" ]]; then
  mkdir -p "$STAGE_DIR/$PROJECT_DIR/Images"
  find "$PROJECT_DIR/Images" -maxdepth 1 -type f \( -iname 'ref_*.jpg' -o -iname 'ref_*.jpeg' \) \
    -exec cp {} "$STAGE_DIR/$PROJECT_DIR/Images/" \;
fi

# --- Comprimi le foto di riferimento (JPEG qualità 70%) per ridurre la dimensione
# dello zip: sono foto smartphone ad alta risoluzione, il peso maggiore del pacchetto,
# e non serve qualità originale per la sola forma/sagoma di riferimento del render.
if command -v magick >/dev/null 2>&1; then
  IMAGEMAGICK_CMD=(magick)
elif command -v convert >/dev/null 2>&1; then
  IMAGEMAGICK_CMD=(convert)
else
  echo "Errore: ImageMagick ('magick'/'convert') non trovato, necessario per comprimere le immagini." >&2
  exit 1
fi

IMAGES_DIR="$STAGE_DIR/${PROJECT_DIR}/Images"
if [[ -d "$IMAGES_DIR" ]]; then
  while IFS= read -r -d '' img; do
    "${IMAGEMAGICK_CMD[@]}" "$img" -quality 70 "$img"
  done < <(find "$IMAGES_DIR" -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -print0)
fi

# --- Zip ---
# Salvato dentro la cartella del progetto stesso (non Build/Handoff/), accanto a
# MISSING_IMAGES.md/.json/_PROMPT.md: tutto quello che serve per generare le
# immagini mancanti sta in un unico posto, niente da cercare altrove nel repo.
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_ZIP="${PROJECT_DIR}/${MODEL}_${VARIANT}_${STAMP}.zip"

(cd "$STAGE_DIR" && zip -rq - .) > "$OUT_ZIP"

echo "Pacchetto creato: ${OUT_ZIP}"
echo "Dimensione: $(du -h "$OUT_ZIP" | cut -f1)"
echo ""
echo "Contenuto:"
unzip -l "$OUT_ZIP" | tail -n +4 | head -n -2
