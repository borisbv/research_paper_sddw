# Task List: Subsanar Hallazgos de Revisión

## Overview
Este documento detalla las tareas atómicas para implementar las correcciones del Peer Review, siguiendo el ciclo RED-GREEN-REFACTOR y los mandatos fundacionales de GEMINI.md.

## Tasks

### Phase 1: Preparation & Testing (RED)
- **Task 1.1**: Crear un script de test `scripts/test_review_fix.py` que valide el conteo de palabras del abstract (min 200) y la existencia de los 5 archivos de figuras en `figures/`.
- **Task 1.2**: Ejecutar `scripts/validate-citations.py` para identificar todos los testimonios sin cita en `paper/sections/results.md`.

### Phase 2: Implementation (GREEN)
- **Task 2.1 (P)**: Redactar la versión expandida del Abstract en `paper/sections/abstract.md` siguiendo la estructura definida en el diseño (~250 palabras).
- **Task 2.2 (P)**: Actualizar `paper/sections/results.md` con las citas bibliográficas correspondientes para Cecilia, Jackie, José y Patricia (Pavez 2020).
- **Task 2.3 (P)**: Insertar párrafo sobre "silos informativos" y salud pública en `paper/sections/discussion.md` (Sección 5.2).
- **Task 2.4**: Generar `figures/graphical_abstract.png` (1200x600px) mediante script o descripción visual.
- **Task 2.5**: Generar `figures/prisma_flowchart.png` con el flujo de información de la SLR (n=160 incluidos).
- **Task 2.6**: Generar los 3 esquemas conceptuales restantes: `conceptual_framework.png`, `comparison_matrix.png`, y `social_capital_functions.png`.

### Phase 3: Validation & Polish (REFACTOR)
- **Task 3.1**: Actualizar `paper/sections/tables.md` para incluir pies de figura y referencias cruzadas a los nuevos activos visuales.
- **Task 3.2**: Ejecutar todos los scripts de validación mandatorios (`validate-structure.py`, `validate-citations.py`, `validate-metadata.py`, `validate-word-count.py`, `validate-prose.py`).
- **Task 3.3**: Corregir cualquier inconsistencia de estilo Chicago-Author-Date en las nuevas ediciones.

## Parallelism Strategy (P)
Las tareas marcadas con (P) pueden ejecutarse en paralelo una vez superada la Phase 1, ya que modifican secciones independientes del manuscrito.
