#!/bin/bash
# Auto-implementación de tareas kiro con /clear entre cada una

FEATURE="${1:?Uso: auto-impl.sh <feature>}"

echo "🚀 Iniciando auto-implementación de: $FEATURE"
echo "=================================================="

while true; do
  # Obtener próxima tarea pendiente
  TASK=$(claude /kiro:spec-status "$FEATURE" 2>/dev/null | grep -oP "pending.*?ID: \K[a-z0-9\-]+' | head -1)

  if [ -z "$TASK" ]; then
    echo "✅ Todas las tareas completadas"
    break
  fi

  echo ""
  echo "📋 Ejecutando tarea: $TASK"
  echo "=================================================="

  # Ejecutar tarea con /clear antes
  claude /clear
  claude /kiro:spec-impl "$FEATURE" "$TASK"

  sleep 1
done

echo ""
echo "🎉 Auto-implementación completada"
