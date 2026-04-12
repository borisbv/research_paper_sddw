# Command: spec-gap-analysis

Este comando realiza un análisis de la novedad científica comparando el objetivo del paper con el estado del arte actual.

## Workflow

1.  **Búsqueda**: Usa `research-lookup` para encontrar los 5 papers más recientes sobre el tema.
2.  **Mapeo**: Utiliza `literature-review` para mapear las contribuciones de esos papers.
3.  **Generación**: Crea el documento `.kiro/specs/[feature-name]/gap-analysis.md` usando el template de `settings/templates/specs/gap-analysis.md`.
4.  **Validación**: Ejecuta `scientific-critical-thinking` para evaluar si el "gap" identificado es robusto.

## Uso
`/kiro:spec-gap-analysis`
