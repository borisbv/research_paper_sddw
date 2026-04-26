---
name: ethical-statement-generator
description: Generación automática de declaraciones éticas, conflictos de interés y disponibilidad de datos basándose en la metadata y el contenido del proyecto.
---

# Ethical Statement Generator

Genera las secciones administrativas del paper que suelen ser obligatorias.

## Secciones Generadas

1.  **Ethics Approval**: Declaración de comités de ética.
2.  **Conflict of Interest**: Declaración de transparencia financiera/personal.
3.  **Data Availability Statement**: Cómo acceder a los datos de `data/`.
4.  **Author Contributions**: Basado en `metadata.yaml`.

## Workflow

1.  Leer `paper/metadata.yaml`.
2.  Detectar el uso de datos humanos/animales en `paper/sections/`.
3.  Proponer el texto legal/estándar.