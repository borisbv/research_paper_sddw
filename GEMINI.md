# Mandatos Fundacionales del Proyecto (GEMINI.md) - Motor de Generación Científica

Este motor es agnóstico al formato de salida (Paper o Libro). Toda investigación debe estar encapsulada en su carpeta correspondiente (`/paper` o `/book`).

## 0. Principios Fundamentales
- **Encapsulamiento:** Todo el contenido de la investigación (secciones, referencias, figuras, datos) DEBE residir dentro de la carpeta del "Target" (`/paper` o `/book`).
- **Agnosticismo:** Los scripts en `scripts/` y comandos en `.kiro/` deben aceptar un parámetro de dirección para operar sobre el target elegido.
- **SDD/Kiro:** El desarrollo de la investigación sigue el flujo de Spec-Driven Development, donde cada "feature" de la investigación es una especificación técnica.

---

## 1. Workflows de Investigación (Research Init)

### 2.1 Inicializar Investigación (research-init) - OBLIGATORIO
**Objetivo:** Establecer el target del motor de generación.
1. Es **OBLIGATORIO** indicar si el proyecto es un `paper` o un `book`.
2. Si el directorio ya existe, el motor detectará que es una **continuación/iteración** del proyecto actual.
3. Si no existe, se creará la estructura base: `[target]/sections/`, `[target]/references/`, `[target]/figures/`, `[target]/data/`.
4. El resto de la sesión operará sobre este target por defecto.

---

## 2. Validaciones Obligatorias
Cada vez que se edite contenido en el target, se deben ejecutar los scripts con el flag `--dir`:
- `python scripts/validate-structure.py --dir [target]`
- `python scripts/validate-word-count.py --dir [target]`
- `python scripts/validate-citations.py --dir [target]`

---

## 3. Integración SDD/Kiro
Las especificaciones en `.kiro/specs/` deben indicar a qué target pertenecen en su metadata si es necesario, aunque por defecto operarán sobre el target activo definido en `metadata.yaml` del proyecto.