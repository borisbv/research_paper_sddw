# Research & Design Decisions — mejora-postulacion-fonis

## Summary
- **Feature**: `mejora-postulacion-fonis`
- **Discovery Scope**: Extension (edición editorial de documento existente)
- **Key Findings**:
  - El formulario tiene una estructura de secciones bien definida (1.1, 1.2, 2.1–2.5, 3.1–3.3) que permite intervenciones quirúrgicas por sección sin reestructurar el documento completo.
  - Los requerimientos tienen dependencias cruzadas: la búsqueda bibliográfica (R1) alimenta al menos 5 de los otros 8 requerimientos (R3, R4, R6, R7, R8).
  - El documento fuente es markdown convertido desde docx, lo que implica que la estructura de tablas puede ser frágil y debe editarse con cuidado.

## Research Log

### Estructura del documento fuente
- **Context**: Necesidad de entender los puntos de edición antes de diseñar la estrategia.
- **Sources Consulted**: `temp_context/Formulario_Postulacion_2026.docx.md`
- **Findings**:
  - Sección 1.1 (Planteamiento del problema y estado del arte): líneas 29–47. Contiene las referencias desactualizadas y el argumento del vacío de conocimiento.
  - Sección 1.2.1 (Solución): líneas 49–65. Descripción genérica del prototipo.
  - Sección 1.2.2 (Resultados esperados): líneas 68–144. Tablas de resultados tecnológicos con indicadores.
  - Sección 2.1 (Pregunta e hipótesis): líneas 166–182. Hipótesis y supuestos a fortalecer.
  - Sección 2.3 (Metodología): líneas 198–293. Plan de análisis y variables.
  - Sección 2.4 (Ética): líneas 297–316. Sección a ampliar con protección de datos.
  - Tablas de resultado tecnológico (líneas 106–124): contienen indicadores a justificar.
- **Implications**: Las ediciones se pueden mapear directamente a rangos de líneas. Las tablas markdown requieren preservar formato de columnas.

### Dependencias entre requerimientos
- **Context**: Optimizar el orden de ejecución para evitar retrabajo.
- **Findings**:
  - **R1 (literatura)** es prerrequisito de R3 (tabla comparativa), R6 (datos epidemiológicos), R7 (justificación indicadores).
  - **R2 (detalle tecnológico)** es independiente, pero la tabla comparativa (R3) necesita saber el enfoque tecnológico para diferenciarlo.
  - **R4 (hipótesis)** depende parcialmente de R7 (efecto esperado justificado) para cuantificar.
  - **R8 (redundancia)** y **R9 (typos)** son transversales y deben ejecutarse al final para evitar conflictos con ediciones previas.
- **Implications**: Orden óptimo: R1 → R6 → R2 → R3 → R7 → R4 → R5 → R8 → R9.

### Herramientas disponibles para búsqueda bibliográfica
- **Context**: Los requirements 1, 3, 6 y 7 requieren búsqueda de literatura y datos.
- **Findings**:
  - Skills disponibles: `research-lookup`, `citation-management`, `literature-review`
  - Bases de datos accesibles: PubMed, Semantic Scholar, Google Scholar, arXiv
  - Para datos epidemiológicos chilenos: INE, CASEN, DEIS (MINSAL), reportes SENAMA
- **Implications**: La búsqueda de literatura se ejecuta mediante skills especializados. Los datos epidemiológicos chilenos pueden requerir WebFetch a fuentes gubernamentales.

## Design Decisions

### Decision: Estrategia de edición por bloques vs. reescritura completa
- **Context**: El documento tiene ~400 líneas. Se puede reescribir completamente o editar por bloques preservando estructura.
- **Alternatives Considered**:
  1. Reescritura completa del formulario — mayor coherencia pero alto riesgo de alterar secciones correctas.
  2. Edición por bloques quirúrgicos — menor riesgo, más trazable a requirements.
- **Selected Approach**: Edición por bloques, interviniendo secciones específicas del formulario.
- **Rationale**: Minimiza riesgo de alterar contenido correcto. Permite validación incremental por sección. El formulario tiene secciones bien delimitadas.
- **Trade-offs**: Puede quedar menor coherencia estilística entre secciones editadas y no editadas. Se mitiga con R8 (reducción de redundancia) al final.

### Decision: Búsqueda bibliográfica como fase previa consolidada
- **Context**: Múltiples requerimientos necesitan referencias bibliográficas.
- **Selected Approach**: Ejecutar una fase de research consolidada antes de comenzar las ediciones, generando un pool de referencias verificadas que alimenten R1, R3, R6, R7.
- **Rationale**: Evita búsquedas duplicadas y garantiza consistencia de citas.

### Decision: Preservación de estructura de tablas
- **Context**: El documento tiene tablas markdown complejas (resultados tecnológicos, plan de trabajo, equipo).
- **Selected Approach**: Editar solo las celdas específicas que requieren cambio, preservando la estructura de filas/columnas.
- **Rationale**: Las tablas markdown convertidas desde docx pueden tener formato frágil. Ediciones minimales reducen riesgo de corrupción.

## Risks & Mitigations
- **Ruptura de tablas markdown**: Editar tablas complejas puede corromper formato → usar Edit tool con strings exactos, no reescribir tablas completas.
- **Referencias no verificables**: La literatura encontrada puede no tener DOI o estar retracted → usar citation-management para validar cada referencia.
- **Inconsistencia de tono**: Secciones editadas pueden contrastar con secciones intactas → ejecutar R8 al final como pasada de homogeneización.
- **Nombre real de la fundación**: "Fundación Comunida" puede ser el nombre real, no un typo → verificar antes de corregir (R9.1 requiere confirmación).
