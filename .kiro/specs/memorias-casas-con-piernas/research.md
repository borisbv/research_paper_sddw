# Research & Design Decisions — memorias-casas-con-piernas

## Summary
- **Feature**: `memorias-casas-con-piernas`
- **Discovery Scope**: Extension (existe borrador previo en `temp_context/paper_Erwin_23_Junio_2025.md`)
- **Key Findings**:
  - El borrador original tiene ~2.500 palabras, necesita expansión significativa (mínimo 7.000) y reestructuración para cumplir IMRaD
  - Las referencias existentes (7) están en APA 7; deben convertirse a Chicago Author-Date y expandirse a 25+
  - Las 5 bitácoras de muestra confirman la riqueza del material (texto + dibujo), pero el borrador no las integra sistemáticamente
  - La sección de "Resultados esperados (supuesto)" indica que los resultados aún no están completamente formalizados

## Research Log

### Análisis del borrador existente
- **Contexto**: Evaluar qué contenido del borrador original es reutilizable y qué requiere reescritura
- **Fuentes consultadas**: `temp_context/paper_Erwin_23_Junio_2025.md`
- **Hallazgos**:
  - Estructura actual: Resumen → Introducción → Metodología → Discusión → Resultados esperados → Conclusión → Referencias
  - Falta sección de Marco teórico / Related Work (mezcla con Introducción)
  - La Discusión aparece antes de los Resultados (orden invertido)
  - El Resumen actual (~150 palabras) está por debajo del mínimo RES (250-300)
  - Las citas están en APA 7 con formato (Autor, año) — debe convertirse a Chicago Author-Date (Autor año, página)
  - Las 5 "casas narrativas" están listadas pero no desarrolladas en profundidad
  - Los dibujos no están referenciados formalmente en el texto
- **Implicaciones**: Requiere reestructuración completa, no solo expansión. El contenido conceptual es sólido pero la arquitectura argumentativa necesita reconstruirse.

### Análisis del material visual (bitácoras)
- **Contexto**: Evaluar el material de los dibujos disponibles para integración en el paper
- **Fuentes consultadas**: `temp_context/Dibujos casas/Casa de paso 1-5.pdf`
- **Hallazgos**:
  - Casa de paso 1: Bitácora escrita — "Lugar de descanso, de protección". Casa antes: "amplia, cálida, cómoda". Casa ahora: "cómoda, fría". Llevó: "los recuerdos"
  - Casa de paso 2: Dibujos "Mi Casa" (con jardín, toldo) vs. "Mi Casa Soñada" (con cerca, árboles, auto) — contraste entre lo real y lo idealizado
  - Casa de paso 3: Firmado por "Nina" / Zubeida Girón — "Soñada" con lista detallada (4 cuartos, terraza, estudio, parque, biblioteca, piscina, 2 baños). Incluye familia y gatos
  - Casa de paso 4: "Familia" como etiqueta de la casa real. Casa soñada: "Crecimiento, Familia. Amor." Firmado por Glorín
  - Casa de paso 5: Norma Romero, 66 años, venezolana, "Estado civil: feliz - libre". Casa grande con balcones, arcos, flores
- **Implicaciones**: Material visual muy rico para ilustrar los arquetipos. Se recomienda seleccionar 3-5 dibujos representativos que cubran diferentes casas narrativas. Los dibujos necesitan digitalización a 300 dpi.

### Requisitos de formato RES
- **Contexto**: Verificar conformidad del borrador con normas RES
- **Fuentes consultadas**: `temp_context/normas.md`, `temp_context/Convocatoria revista.md`
- **Hallazgos**:
  - Chicago Author-Date obligatorio (no APA)
  - 7.000-10.000 palabras totales (todo incluido)
  - Resumen extendido bilingüe 250-300 palabras con estructura definida
  - 4-6 palabras clave bilingües
  - Título bilingüe
  - Imágenes en archivo aparte, numeradas, con permisos
  - Plataforma de envío: OJS
  - No se permite ibid., op. cit., ibidem
- **Implicaciones**: Conversión de formato de citas es tarea prioritaria. La extensión actual (~2.500 palabras) requiere triplicar el contenido.

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos / Limitaciones | Notas |
|--------|-------------|-----------|---------------------|-------|
| IMRaD estándar | Intro-Método-Resultados-Discusión | Familiar para evaluadores, estructura clara | Puede ser rígido para investigación-creación | Adaptable con Marco teórico separado |
| Narrativo-ensayístico | Estructura libre, flujo argumentativo | Más natural para arte e investigación-creación | Puede ser percibido como menos riguroso por evaluadores | RES acepta "textos reflexivos" (~5.000 palabras) |
| IMRaD adaptado | IMRaD con Marco teórico expandido y Resultados como obra visual | Balance entre rigor y creatividad | Requiere que los "resultados" incluyan obra visual como dato | **Seleccionado** |

## Design Decisions

### Decision: Estructura IMRaD adaptada a investigación-creación
- **Contexto**: El paper es investigación-creación transdisciplinar, no un estudio empírico convencional. Necesita rigor formal pero espacio para la voz artística.
- **Alternativas consideradas**:
  1. IMRaD puro — demasiado rígido, no permite integrar la obra visual como resultado
  2. Ensayo reflexivo (~5.000 palabras) — más libre pero menos posibilidades de aceptación como artículo
  3. IMRaD adaptado con Marco teórico expandido — combina estructura reconocible con flexibilidad
- **Enfoque seleccionado**: IMRaD adaptado: Introducción → Marco teórico → Metodología → Resultados (casas narrativas + obra visual) → Discusión → Conclusión
- **Rationale**: La RES publica artículos transdisciplinares y valora la diversidad metodológica. La estructura IMRaD adaptada es reconocible para evaluadores de diferentes disciplinas mientras permite integrar la dimensión artística.
- **Trade-offs**: Requiere más palabras (7.000-10.000) que un ensayo, pero gana en rigurosidad formal.
- **Seguimiento**: Verificar que la extensión final no exceda 10.000 palabras con todos los componentes.

### Decision: Redistribución del presupuesto de palabras
- **Contexto**: Total disponible: 7.000-10.000 palabras (incluyendo resúmenes, bibliografía, notas). Se necesita distribuir eficientemente.
- **Enfoque seleccionado**:
  - Resúmenes (ES + EN): ~600 palabras
  - Palabras clave: ~50 palabras
  - Introducción: ~1.200 palabras
  - Marco teórico: ~1.500 palabras
  - Metodología: ~1.200 palabras
  - Resultados: ~1.800 palabras (sección más larga: 5 arquetipos + obra visual)
  - Discusión: ~1.200 palabras
  - Conclusión: ~400 palabras
  - Referencias (~30 entradas): ~800 palabras
  - Total estimado: ~8.800 palabras
- **Rationale**: Resultados recibe mayor peso porque es la contribución original (casas narrativas). Introducción y Marco teórico comparten carga conceptual.

### Decision: Estrategia de migración de citas APA → Chicago Author-Date
- **Contexto**: Las 7 referencias del borrador están en APA 7. Se necesitan 25+ en Chicago Author-Date.
- **Enfoque seleccionado**: Reconstruir el archivo .bib desde cero con entradas Chicago-compliant, validando DOI contra CrossRef.
- **Rationale**: Convertir 7 citas es menos trabajo que establecer un pipeline de conversión. Las ~18 citas nuevas se agregarán durante la escritura de cada sección.

## Risks & Mitigations
- **Extensión insuficiente**: El borrador tiene ~2.500 palabras; necesita ~8.800 → Mitigación: escribir sección por sección con targets de palabras
- **Falta de profundidad en resultados**: Los 5 arquetipos están listados pero no desarrollados → Mitigación: dedicar ~350 palabras a cada arquetipo con ejemplos de bitácoras
- **Referencias insuficientes**: Solo 7 de las 25+ necesarias → Mitigación: búsqueda bibliográfica sistemática por campo disciplinar
- **Calidad de imágenes**: Los PDFs de bitácoras pueden no tener 300 dpi → Mitigación: re-escanear originales si es necesario
- **Consentimientos informados**: No se ha verificado si existen → Mitigación: solicitar al investigador (Erwin) constancia de protocolo ético
