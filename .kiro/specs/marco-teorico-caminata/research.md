# Research & Design Decisions — Marco Teórico Caminata

## Summary
- **Feature**: `marco-teorico-caminata`
- **Discovery Scope**: New Feature (greenfield — no existen archivos de contenido en `paper/`)
- **Key Findings**:
  - La estructura del paper sigue el formato Quarto book con archivos `.qmd` en `paper/`, compilados con `scripts/build-book.sh`
  - Las referencias se gestionan en `references/references.bib` (actualmente solo una entrada no relacionada con caminata)
  - Se requiere búsqueda exhaustiva en bases de datos académicas para poblar 12-18 referencias nuevas verificadas por DOI

## Research Log

### Estructura del proyecto y formato de salida
- **Context**: Determinar dónde se ubicará el marco teórico y en qué formato
- **Sources Consulted**: `CLAUDE.md`, estructura de directorios, `_quarto.yml` (no existe aún)
- **Findings**:
  - El directorio `paper/` existe con subdirectorios `data/` y `figures/`, pero sin archivos de contenido
  - No existe `_quarto.yml` — el proyecto necesita configuración Quarto o el archivo se genera al compilar
  - El formato de archivos es `.md` o `.qmd` según `CLAUDE.md`
  - El build se ejecuta con `scripts/build-book.sh`
- **Implications**: El marco teórico se escribirá como archivo `.qmd` dentro de `paper/`. La configuración Quarto puede necesitar crearse si no existe al momento de la implementación

### Distribución de contenido por bloques
- **Context**: Planificar la distribución de 1.500-1.800 palabras en 7 bloques temáticos
- **Findings**:
  - Con ~1.650 palabras objetivo y 7 bloques, el promedio es ~235 palabras por bloque
  - Los bloques centrales (beneficios, regulación emocional, CEA) requieren mayor extensión por densidad de evidencia
  - Los bloques de apertura (conceptualización) y cierre (vacíos) pueden ser más concisos
  - Distribución estimada:
    - Bloque 1 (conceptualización): ~200 palabras
    - Bloque 2 (beneficios): ~250 palabras
    - Bloque 3 (regulación emocional): ~280 palabras
    - Bloque 4 (contexto familiar): ~220 palabras
    - Bloque 5 (perspectiva adolescente): ~220 palabras
    - Bloque 6 (caminata y CEA): ~280 palabras
    - Bloque 7 (vacíos): ~200 palabras
- **Implications**: Algunos bloques pueden fusionarse en un solo párrafo extenso (8-15 líneas) y otros requerirán dos párrafos. La prioridad es la lógica acumulativa sobre la distribución equitativa

### Estrategia de búsqueda bibliográfica
- **Context**: Identificar las bases de datos y términos de búsqueda para 12-18 referencias
- **Findings**:
  - Términos clave internacionales: "walking AND emotional regulation", "walking AND autism spectrum", "walking AND adolescents AND self-regulation", "rhythmic movement AND stress reduction", "embodied cognition AND walking", "family walking AND bonding"
  - Términos clave regionales: "caminata AND adolescentes AND Chile", "actividad física AND autismo AND Latinoamérica", "regulación emocional AND prácticas corporales"
  - Bases prioritarias: PubMed y Scopus (evidencia clínica/psicológica), SciELO y Redalyc (evidencia regional)
  - Ventana temporal: 2020-2026, con excepciones para obras seminales (e.g., Gross sobre regulación emocional, Thayer sobre activación fisiológica)
- **Implications**: La búsqueda debe ejecutarse en fase de implementación usando los skills `research-lookup` y `citation-management`. Cada referencia se valida por DOI/CrossRef antes de incorporarse al `.bib`

### Perspectiva autista y terminología
- **Context**: Garantizar coherencia terminológica con el enfoque del estudio HabiTAR
- **Findings**:
  - El proyecto adopta la perspectiva autista: el autismo es una variación natural del neurodesarrollo
  - Terminología preferida: "Condición del Espectro Autista (CEA)", "personas en el espectro", "adolescentes autistas"
  - Evitar: "trastorno", "déficit", "padecen", formulaciones por negación
  - Las definiciones se construyen de manera afirmativa
- **Implications**: Toda la sección sobre CEA debe reflejar consistentemente esta perspectiva. Verificar que las fuentes citadas sean compatibles con este enfoque o contextualizarlas adecuadamente

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos / Limitaciones | Notas |
|--------|-------------|-----------|------------------------|-------|
| Prosa continua sin subsecciones explícitas | Un texto fluido sin encabezados internos, solo separación por párrafos | Máxima fluidez, lectura académica natural | Dificulta la navegación y la verificación por bloques | Preferido por las instrucciones (párrafos extensos sin disrupciones) |
| Subsecciones con encabezados | Cada bloque temático con su propio encabezado (###) | Facilita revisión y validación por requirement | Rompe la fluidez exigida; los conectores pierden sentido | Descartado — las instrucciones piden prosa continua |

## Design Decisions

### Decision: Formato del archivo de salida
- **Context**: Determinar si el marco teórico se escribe como `.md` o `.qmd`
- **Alternatives Considered**:
  1. Markdown plano (`.md`) — máxima simplicidad
  2. Quarto markdown (`.qmd`) — permite compilación con Quarto y YAML frontmatter
- **Selected Approach**: `.qmd` con frontmatter YAML mínimo
- **Rationale**: El proyecto usa Quarto como pipeline de compilación. Un archivo `.qmd` permite integración directa con `build-book.sh` y soporte para citas en formato `@citekey`
- **Trade-offs**: Requiere que Quarto esté instalado para compilar, pero el contenido sigue siendo legible como markdown
- **Follow-up**: Verificar si existe `_quarto.yml` al momento de escribir; si no, crearlo o documentar la necesidad

### Decision: Prosa continua sin encabezados internos
- **Context**: Las instrucciones especifican párrafos extensos (8-15 líneas) con conectores académicos, prosa continua sin disrupciones
- **Selected Approach**: El marco teórico será un texto continuo organizado en párrafos, sin encabezados de subsección
- **Rationale**: Respeta las instrucciones explícitas del documento de contexto y produce un resultado académico más natural
- **Trade-offs**: La validación por bloque temático requerirá análisis semántico del contenido, no por estructura de encabezados

### Decision: Estrategia de citación con Quarto
- **Context**: Las citas deben estar en formato APA, usando tanto formato narrativo como parentético
- **Selected Approach**: Usar sintaxis de citación Quarto: `@citekey` para narrativo y `[@citekey]` para parentético, con `references/references.bib` como fuente
- **Rationale**: Quarto genera automáticamente la bibliografía en formato APA a partir del `.bib` y la configuración CSL
- **Follow-up**: Asegurar que el archivo CSL para APA esté configurado en `_quarto.yml`

## Risks & Mitigations
- **Escasez de evidencia regional**: Puede no haber suficientes estudios chilenos/latinoamericanos sobre caminata y CEA → señalar explícitamente como vacío empírico (convierte el riesgo en aporte)
- **Límite de palabras estricto**: 1.800 palabras para 7 bloques es ajustado → priorizar densidad argumentativa y fusionar bloques temáticamente cercanos (4-5 como un párrafo combinado)
- **Referencias no verificables**: Algunas fuentes pueden no tener DOI → excluir según Req 8.6 y reemplazar con alternativas verificadas
- **Coherencia terminológica**: Riesgo de inconsistencia entre la perspectiva autista y la terminología de las fuentes citadas → contextualizar las citas que usen terminología diferente

## References
- Instrucciones del marco teórico: `temp_context.md/Instrucciones Marco Teórico sobre Caminata.md`
- Estructura del proyecto: `CLAUDE.md`
- Pipeline de compilación: `scripts/build-book.sh`
- Referencias existentes: `references/references.bib`
