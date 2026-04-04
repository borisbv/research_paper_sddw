#!/bin/bash
# install-hooks.sh -- Instala git hooks para el proyecto Paper SDD
# Uso: bash scripts/install-hooks.sh

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$BASE_DIR/.git/hooks"
SOURCE_DIR="$BASE_DIR/scripts/hooks"

if [ ! -d "$HOOKS_DIR" ]; then
    echo "ERROR: No se encontro $HOOKS_DIR"
    echo "Asegurese de estar en un repositorio git."
    exit 1
fi

# Pre-commit hook
if [ -f "$SOURCE_DIR/pre-commit" ]; then
    cp "$SOURCE_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
    chmod +x "$HOOKS_DIR/pre-commit"
    echo "OK: pre-commit hook instalado"
else
    echo "WARN: scripts/hooks/pre-commit no encontrado"
fi

echo ""
echo "Hooks instalados. Se ejecutaran automaticamente en cada commit."
echo "Para desactivar: rm .git/hooks/pre-commit"
