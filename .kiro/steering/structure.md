# Estructura del Proyecto

## Filosofía de Organización

Estructura orientada al paper: cada carpeta corresponde a un artefacto del manuscrito o del proceso SDD. El paper se desarrolla como módulos independientes (secciones) que se integran en el documento final.

## Patrones de Directorio

### Contenido del Paper
**Ubicación**: `paper/`
**Propósito**: Secciones del manuscrito en Markdown (o LaTeX)
**Patrón**: Un archivo por sección principal (e.g., `introduction.md`, `methodology.md`)

### Referencias Bibliográficas
**Ubicación**: `references/`
**Propósito**: Archivo BibTeX maestro y materiales de soporte bibliográfico
**Archivo principal**: `references.bib`

### Figuras y Material Visual
**Ubicación**: `figures/`
**Propósito**: Dibujos de casas (investigador + participantes), gráficos, imágenes
**Formato**: JPG/TIFF 300 dpi para entrega; originales en cualquier formato

### Datos y Bitácoras
**Ubicación**: `data/`
**Propósito**: Datos procesados de las 60 bitácoras, análisis cualitativos

### Scripts de Validación
**Ubicación**: `scripts/`
**Propósito**: Herramientas automáticas de validación (estructura, citas, extensión, formato)

### Contexto Temporal
**Ubicación**: `temp_context/`
**Propósito**: Material de referencia del autor (convocatoria, normas, borrador original, dibujos)
**Nota**: No forma parte del entregable final

### Especificaciones SDD
**Ubicación**: `.kiro/specs/`
**Propósito**: Specs por sección del paper, generadas por el workflow SDD

### Memoria del Proyecto
**Ubicación**: `.kiro/steering/`
**Propósito**: Contexto persistente sobre el producto, stack técnico y estructura

## Convenciones de Nombrado

- **Archivos del paper**: minúsculas, snake_case (e.g., `related_work.md`, `methodology.md`)
- **Secciones**: nombres en inglés (convención del framework), contenido en español
- **Referencias**: clave BibTeX = `Apellido_año` (e.g., `Bachelard_1957`)

## Estructura del Manuscrito (IMRaD adaptado)

El paper sigue una estructura IMRaD adaptada a investigación-creación:

1. Título + Resumen extendido (español + inglés)
2. Introducción (gap, hipótesis, alcance)
3. Marco teórico / Related Work
4. Metodología (bitácoras, entrevistas sensibles, dibujo proyectivo)
5. Resultados (casas narrativas como arquetipos)
6. Discusión (análisis simbólico, tensiones)
7. Conclusión
8. Referencias (Chicago Author-Date)

---
_Actualizado: 2026-03-31_
