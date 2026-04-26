#!/usr/bin/env bash
# build-book.sh — Compilar "La Moneda Emocional" con Quarto
# Uso: ./scripts/build-book.sh [html|pdf|docx|all]
#
# Prerequisitos: quarto >= 1.4  (https://quarto.org/docs/get-started/)
# Para PDF: quarto install tinytex

set -euo pipefail

FORMAT="${1:-html}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

check_quarto() {
  if ! command -v quarto &>/dev/null; then
    echo "ERROR: quarto no está instalado."
    echo "Descarga desde: https://quarto.org/docs/get-started/"
    exit 1
  fi
}

build() {
  local fmt="$1"
  echo "▶ Compilando formato: $fmt"
  quarto render "$ROOT" --to "$fmt"
  echo "✓ Output en: $ROOT/_book/"
}

screenshot() {
  echo "▶ Generando screenshots para revisión LLM..."
  if ! command -v node &>/dev/null; then
    echo "AVISO: Node.js no disponible, omitiendo screenshots."
    return
  fi
  node "$ROOT/scripts/screenshot-book.js"
  echo "✓ Screenshots en: $ROOT/_book/screenshots/"
}

check_quarto

case "$FORMAT" in
  html)
    build html
    screenshot
    ;;
  pdf)
    build pdf
    ;;
  docx)
    build docx
    ;;
  all)
    build html
    build pdf
    build docx
    screenshot
    ;;
  preview)
    quarto preview "$ROOT"
    ;;
  *)
    echo "Uso: $0 [html|pdf|docx|all|preview]"
    exit 1
    ;;
esac