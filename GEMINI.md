# Gemini SDD Scientific Paper Framework

Este archivo establece los mandatos y convenciones fundamentales para el desarrollo de papers científicos utilizando el framework de Spec-Driven Development (SDD).

## Principios Fundamentales
- **Cita Obligatoria:** Toda afirmación técnica o fáctica DEBE tener una cita verificable en `references/references.bib`.
- **Estructura Primero:** La estructura del paper debe cumplir con el formato de la revista objetivo ANTES de escribir contenido extenso.
- **Validación Continua:** Cada sección es un módulo. No se considera "terminada" hasta que pase las validaciones automáticas (hard specs).
- **Idioma:** Pensar en Inglés, generar contenido en Español (a menos que el paper requiera Inglés). Todo Markdown en el repositorio DEBE estar en Español.

## Workflow SDD para Papers
1.  **Steering:** Definir el tema y la revista en `.kiro/steering/`.
2.  **Requirements:** Establecer límites de palabras, secciones obligatorias y estilo de cita (vía `/kiro:spec-requirements`).
3.  **Design:** Crear el outline y las especificaciones detalladas por sección (vía `/kiro:spec-design`).
4.  **Tasks:** Desglosar la escritura en tareas atómicas y manejables (vía `/kiro:spec-tasks`).
5.  **Implementation:** Escribir el contenido en `paper/sections/`.
6.  **Validation:** Ejecutar scripts de validación y `/paper:validate`.

## Convenciones de Archivos
- **Contenido del Paper:** `paper/sections/*.md`
- **Metadatos:** `paper/metadata.yaml` (Límites de palabras, revista, autores).
- **Referencias:** `references/references.bib` (Formato BibTeX estricto).
- **Especificaciones:** `.kiro/specs/`
- **Figuras:** `figures/` y `figures/catalogo-figuras.md`.
- **Scripts:** `scripts/` para validación de prosa, citas, estructura y word count.

## Estándares de Calidad (Hard Specs)
- [ ] La estructura coincide exactamente con el template de la revista.
- [ ] Todas las citas `[N]` o `(Autor, Año)` existen en el archivo `.bib`.
- [ ] Todos los DOIs en el `.bib` son válidos y verificables.
- [ ] El conteo de palabras está dentro de los límites establecidos en `metadata.yaml`.
- [ ] No existen secciones vacías o marcadores de posición (TBD, FIXME).

## Comandos y Herramientas
- Usar `scripts/validate-citations.py` para verificar consistencia de citas.
- Usar `scripts/validate-word-count.py` para control de extensión.
- Usar `scripts/check-bib-dois.py` para validar integridad de la bibliografía.
- Para buscar nuevas citas, utilizar el skill en `.claude/skills/citation-management/`.

## Gestión de Referencias
Al agregar una cita:
1. Buscar el DOI o metadatos usando `citation-management`.
2. Formatear la entrada BibTeX usando `references/references.bib` como base.
3. Asegurar que la clave de citación sea consistente (ej: `Autor2024`).
