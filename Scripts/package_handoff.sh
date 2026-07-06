#!/usr/bin/env bash
# Prepara un pacchetto di handoff (zip) per il rendering in ChatGPT Web,
# contenente SOLO i file necessari per un singolo progetto/variante:
# Core files fissi (Design Language/Style/Component/QA/RENDER_GUIDE) +
# tokens.example.yaml + Projects/{Model}/{Variant}/** (ApprovedText, Images,
# PROJECT.yaml, PDF_CONFIG.yaml).
#
# Uso:
#   Scripts/package_handoff.sh <Model> <Variant>
#   Scripts/package_handoff.sh Magnum_Saber_Premium Cotton_Candy_Drift
#
# Blocca se una pagina in ApprovedText/P0xx non ha status: "locked".

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
APPROVED_TEXT_DIR="${PROJECT_DIR}/ApprovedText"

if [[ ! -d "$PROJECT_DIR" ]]; then
  echo "Errore: cartella progetto non trovata: ${PROJECT_DIR}" >&2
  exit 1
fi

if [[ ! -d "$APPROVED_TEXT_DIR" ]]; then
  echo "Errore: cartella ApprovedText non trovata: ${APPROVED_TEXT_DIR}" >&2
  exit 1
fi

# --- Validazione: ogni pagina P0xx deve essere locked ---
UNLOCKED=()
for page_dir in "$APPROVED_TEXT_DIR"/P[0-9][0-9][0-9]; do
  [[ -d "$page_dir" ]] || continue
  metadata_file="${page_dir}/metadata.yaml"
  if [[ ! -f "$metadata_file" ]]; then
    UNLOCKED+=("$(basename "$page_dir") (metadata.yaml mancante)")
    continue
  fi
  if ! grep -q '^status: *"locked"' "$metadata_file"; then
    UNLOCKED+=("$(basename "$page_dir")")
  fi
done

if [[ ${#UNLOCKED[@]} -gt 0 ]]; then
  echo "Errore: pagine non locked in ${APPROVED_TEXT_DIR}:" >&2
  printf '  - %s\n' "${UNLOCKED[@]}" >&2
  echo "Completa il PASSO 9/10a prima di impacchettare." >&2
  exit 1
fi

# --- Staging ---
STAGE_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGE_DIR"' EXIT

CORE_FILES=(
  "Core/RENDER_GUIDE.md"
  "Core/DESIGN_LANGUAGE.md"
  "Core/STYLE_GUIDE.md"
  "Core/COMPONENT_SYSTEM.md"
  "Core/QA_SYSTEM.md"
  "Assets/DesignSystem/Tokens/tokens.example.yaml"
)

for f in "${CORE_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "Errore: file core mancante: ${f}" >&2
    exit 1
  fi
  mkdir -p "$STAGE_DIR/$(dirname "$f")"
  cp "$f" "$STAGE_DIR/$f"
done

mkdir -p "$STAGE_DIR/$(dirname "$PROJECT_DIR")"
cp -R "$PROJECT_DIR" "$STAGE_DIR/$PROJECT_DIR"

# --- Zip ---
OUT_DIR="Build/Handoff"
mkdir -p "$OUT_DIR"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_ZIP="${OUT_DIR}/${MODEL}_${VARIANT}_${STAMP}.zip"

(cd "$STAGE_DIR" && zip -rq - .) > "$OUT_ZIP"

echo "Pacchetto creato: ${OUT_ZIP}"
echo "Dimensione: $(du -h "$OUT_ZIP" | cut -f1)"
echo ""
echo "Contenuto:"
unzip -l "$OUT_ZIP" | tail -n +4 | head -n -2
