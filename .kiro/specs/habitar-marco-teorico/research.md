# Research & Design Decisions

## Summary
- **Feature**: `habitar-marco-teorico`
- **Discovery Scope**: Extension (enriquecimiento de documento existente)
- **Key Findings**:
  - El documento original tiene 3 secciones con contenido desarrollado y 2 secciones placeholder que requieren escritura completa
  - El directorio `paper/` existe pero no contiene archivos Markdown aún; el nuevo documento será el primero
  - El archivo `references.bib` existe en `references/` pero contiene referencias de otro paper; las nuevas referencias se gestionan dentro del propio documento Markdown

## Research Log

### Análisis del documento original
- **Context**: Determinar el estado actual del marco teórico y las áreas que requieren intervención
- **Sources Consulted**: `temp_context/Marco teórico - Tea Tecnologia + CF.docx.md`, `temp_context/2_mentoría.md`
- **Findings**:
  - Secciones con contenido: Planteamiento del problema (~4 párrafos), Adolescentes TEA (~5 párrafos), Referencias bibliográficas (15 entradas)
  - Secciones placeholder: "Modelos educativos en Chile" (solo encabezado + 1 línea), "Uso de apps para TEA" (solo encabezados + 3 líneas)
  - Inconsistencias identificadas por mentor: uso de plural con cita singular (al menos 4 instancias), frases fuertes sin cita (al menos 3), transiciones abruptas (al menos 2 quiebres), referencia a "países de ingresos bajos y medios" inconsistente con caso chileno
- **Implications**: El trabajo se divide naturalmente en dos tipos: (a) enriquecimiento incremental de secciones existentes (insertar citas, transiciones) y (b) escritura completa de secciones nuevas

### Estrategia de búsqueda bibliográfica
- **Context**: Definir cómo se encontrarán las ~30-50 referencias nuevas necesarias
- **Sources Consulted**: Skills disponibles (`research-lookup`, `citation-management`, `literature-review`)
- **Findings**:
  - El skill `research-lookup` permite búsquedas en bases académicas (Semantic Scholar, PubMed, etc.)
  - El skill `citation-management` valida citas y genera BibTeX
  - Las búsquedas deben filtrarse por año (2020–2026) y verificar indexación Scopus
  - Áreas temáticas de búsqueda: TEA + adolescentes, TEA + tecnologías/apps, TEA + autorregulación emocional, modelos educativos Chile + inclusión, TEA + educación superior
- **Implications**: La búsqueda bibliográfica es la tarea más intensiva y debe ejecutarse por sección temática para mantener coherencia

### Formato de inserción entre corchetes
- **Context**: Definir convención clara para distinguir texto original de mejoras
- **Findings**:
  - El README especifica formato `[ ]` para todo texto nuevo
  - Las inserciones pueden ser: citas adicionales `[; Autor, Año; Autor, Año]`, oraciones de transición `[Oración completa nueva.]`, párrafos completos para secciones placeholder `[Párrafo completo nuevo.]`
  - Las correcciones de redacción (e.g., cambiar "países de ingresos bajos" por región) requieren marcar tanto la eliminación como la inserción
- **Implications**: Se necesita una convención para correcciones que modifiquen texto original: usar `[ORIGINAL: "texto viejo" → "texto nuevo"]` o simplemente insertar la versión corregida entre corchetes después del texto original

## Design Decisions

### Decision: Convención de marcado para correcciones
- **Context**: Algunas mejoras no son adiciones sino correcciones del texto original (e.g., reformulación regional)
- **Alternatives Considered**:
  1. Tachado + inserción: ~~texto viejo~~ [texto nuevo]
  2. Nota entre corchetes: [CORRECCIÓN: cambiar "X" por "Y"]
  3. Inserción directa con nota: texto original [→ Reformulación sugerida: "texto nuevo"]
- **Selected Approach**: Opción 2 — nota entre corchetes con instrucción clara
- **Rationale**: Mantiene el texto original intacto (requisito 1.2), es inequívoco para el investigador, y es consistente con el formato de corchetes del resto de inserciones
- **Trade-offs**: Algo más verboso, pero prioriza claridad sobre concisión

### Decision: Estructura del documento de salida
- **Context**: Definir nombre y ubicación del archivo nuevo
- **Alternatives Considered**:
  1. `paper/marco-teorico-habitar.md`
  2. `paper/habitar-marco-teorico-enriquecido.md`
  3. `paper/01-marco-teorico.md`
- **Selected Approach**: `paper/habitar-marco-teorico-enriquecido.md`
- **Rationale**: Nombre descriptivo que indica tanto el proyecto (HabiTAR) como que es la versión enriquecida, sin usar prefijo numérico que implique orden de capítulos aún no definido
- **Trade-offs**: Nombre largo pero autoexplicativo

### Decision: Gestión de referencias nuevas
- **Context**: Dónde colocar las entradas bibliográficas completas de las nuevas citas
- **Alternatives Considered**:
  1. En `references/references.bib` (formato BibTeX)
  2. Dentro del propio documento Markdown al final
  3. En ambos lugares
- **Selected Approach**: Dentro del propio documento Markdown, en la sección "Referencias bibliográficas" existente, siguiendo el formato del original
- **Rationale**: El documento original ya tiene sus referencias en formato APA al final del Markdown. Mantener consistencia. El `.bib` pertenece a otro paper
- **Trade-offs**: No se integra con pipeline BibTeX, pero es coherente con el formato del documento fuente

## Risks & Mitigations
- **Riesgo 1**: Referencias inventadas o inexistentes → Mitigación: usar `research-lookup` y `citation-management` para verificar cada referencia contra bases reales (Semantic Scholar, CrossRef)
- **Riesgo 2**: Ruptura del tono al insertar texto nuevo → Mitigación: validar cada inserción contra las reglas de estilo del README antes de escribir
- **Riesgo 3**: Exceso de inserciones que dificulten la lectura → Mitigación: limitar cada inserción a lo estrictamente necesario; preferir citas compactas sobre párrafos largos cuando sea posible
- **Riesgo 4**: DOIs incorrectos o enlaces rotos → Mitigación: verificar cada DOI con WebFetch antes de incluirlo en el documento

## References
- [EARS Format](../../settings/rules/ears-format.md) — formato de requisitos
- [Estilo académico](../../../temp_context/README.md) — guía de tono y formato del documento
- [Paper de referencia](../../../temp_context/FormulacionIniEsp_CF.docx.md) — modelo de estructura y profundidad
