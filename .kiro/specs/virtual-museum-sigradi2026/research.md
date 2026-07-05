# Research & Design Decisions

---
**Purpose**: Hallazgos de investigación y decisiones de diseño que informan la estructura del paper SIGraDi 2026.
---

## Summary
- **Feature**: `virtual-museum-sigradi2026`
- **Discovery Scope**: New Feature (paper científico greenfield desde borrador)
- **Key Findings**:
  - SIGraDi 2026 requiere formato IMRaD adaptado, 2500-3500 palabras, APA 7, revisión ciega
  - El borrador existente contiene contenido valioso pero necesita reestructuración científica y fortalecimiento del estado del arte
  - La contribución principal debe ser un marco conceptual transferible (no solo el prototipo del museo virtual)

## Research Log

### Formato y plantilla SIGraDi 2026
- **Context**: Determinar requisitos formales de la venue objetivo
- **Sources Consulted**: Borrador del manuscrito (sección de formato), instrucciones del prompt maestro
- **Findings**:
  - Extensión: 2500-3500 palabras (excluyendo referencias)
  - Formato: Arial 12 bold secciones principales, Arial 10 bold subsecciones, Arial 10 normal cuerpo
  - Citación: APA 7 con DOI verificables
  - Idioma: Inglés académico internacional
  - Revisión: Ciega (anonimato total)
  - Estructura: IMRaD adaptado con estado del arte
- **Implications**: El manuscrito debe condensar información rica en un espacio limitado; cada palabra debe aportar valor científico

### Estado del borrador existente
- **Context**: Diagnóstico del manuscrito base para determinar qué conservar, reorganizar o ampliar
- **Sources Consulted**: `01_569 SIGraDi_2026_FULLPAPER_BLINDREVIEW_on progres v1.0.md`
- **Findings**:
  - Fortalezas: caso de estudio definido, metodología en 6 etapas, equipo interdisciplinario, visión clara
  - Vacíos conceptuales: marco teórico débil (lista de autores sin diálogo crítico), brecha no argumentada
  - Vacíos metodológicos: falta detalle de participantes, instrumentos y procedimientos
  - Vacíos bibliográficos: pocas citas recientes (2021-2026), duplicados, DOI no verificados
  - Vacíos argumentativos: resultados son "esperados" (no reales), discusión superficial
  - Contenido a eliminar: presupuestos, montos, salarios
- **Implications**: La reescritura debe fortalecer científicamente sin reemplazar el contenido existente

### Casos de estudio comparativos disponibles
- **Context**: Material de apoyo para el estado del arte y la metodología
- **Sources Consulted**: `Case Study Research.md`
- **Findings**:
  - 12 casos documentados con pros/contras: Smithsonian (3 exhibiciones), Van Gogh Museum, British Museum, National Gallery (2), Art Institute of Chicago, Hermitage, Dalí Museum (2)
  - Patrones identificados: navegación (lineal vs. libre vs. 360), inmersión vs. accesibilidad, multimedia, metadatos
  - Los casos cubren: slideshows, recorridos 360, galerías interactivas, AR/VR, mapas navegables
- **Implications**: Estos casos sostienen el análisis comparativo (Etapa 2 de la metodología) y fortalecen el estado del arte con evidencia empírica

### Figuras científicas requeridas
- **Context**: El prompt maestro solicita 5 figuras que sinteticen conocimiento
- **Findings**:
  - Fig 1: Research Context and Knowledge Gap — ubicación: Introduction/State of the Art
  - Fig 2: Research Design Framework — ubicación: Methodology
  - Fig 3: Interdisciplinary Research Ecosystem — ubicación: Methodology
  - Fig 4: Human-Centred Virtual Museum Framework — ubicación: Discussion
  - Fig 5: Knowledge Transfer Framework — ubicación: Conclusions
- **Implications**: Las figuras deben diseñarse como diagramas conceptuales que sintetizan el argumento, no como ilustraciones decorativas

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos | Notas |
|--------|-------------|-----------|---------|-------|
| IMRaD estricto | Estructura clásica sin subsecciones adicionales | Universalmente reconocida, compatible con SIGraDi | Puede ser demasiado rígida para el contenido | Adaptada con State of the Art como sección expandida |
| IMRaD + Framework | IMRaD con sección dedicada al modelo conceptual en Discussion | Permite destacar la contribución | Riesgo de exceder palabras | Seleccionada: el framework es la contribución principal |
| Narrative paper | Estructura libre argumentativa | Más fluida | No cumple plantilla SIGraDi | Descartada |

## Design Decisions

### Decision: Estructura del manuscrito
- **Context**: El borrador mezcla secciones de forma inconsistente; necesita reorganización
- **Alternatives Considered**:
  1. IMRaD puro (6 secciones)
  2. IMRaD expandido con State of the Art separado del Introduction
- **Selected Approach**: IMRaD expandido: Title, Abstract, Keywords, Introduction, State of the Art, Methodology, Results, Discussion, Conclusions, References
- **Rationale**: Permite un estado del arte robusto (requisito central del prompt maestro) sin sobrecargar la introducción
- **Trade-offs**: Una sección más requiere gestionar mejor el límite de palabras
- **Follow-up**: Verificar que la plantilla SIGraDi acepta esta variante

### Decision: Tratamiento de resultados
- **Context**: El borrador presenta "Expected Outcomes" pero el proyecto está en etapas iniciales
- **Alternatives Considered**:
  1. Mantener como resultados esperados
  2. Convertir a resultados preliminares de las primeras 3-4 etapas
- **Selected Approach**: Presentar como resultados preliminares de las etapas completadas (needs assessment, comparative analysis, technical framework)
- **Rationale**: Honestidad científica; los resultados parciales son publicables si se interpretan adecuadamente
- **Trade-offs**: Menor impacto que resultados finales, pero mayor credibilidad
- **Follow-up**: Interpretar hallazgos preliminares vinculándolos con las preguntas de investigación

### Decision: Construcción de la brecha
- **Context**: El prompt maestro exige que la brecha sea una oportunidad, no una crítica
- **Selected Approach**: Construir la brecha argumentando que las dimensiones (UX, XR, patrimonio, accesibilidad, comunidad) han avanzado independientemente, generando la oportunidad de un marco integrador
- **Rationale**: Evita afirmaciones negativas; presenta la investigación como avance, no como corrección
- **Trade-offs**: Requiere un estado del arte sólido que demuestre los avances independientes

## Risks & Mitigations
- Exceder límite de palabras (3500) → Priorizar densidad científica sobre extensión; cada párrafo = una idea
- Referencias no verificables → Usar solo citas con DOI confirmado; marcar pendientes de verificación
- Pérdida de anonimato → Revisar todo el manuscrito buscando nombres institucionales antes de finalizar
- Brecha débil → Fortalecer estado del arte con mínimo 3 fuentes recientes por claim principal
- Figuras no reproducibles → Describir contenido conceptual de cada figura para que el equipo las diseñe

## References
- SIGraDi conference proceedings — formato y estilo de publicaciones previas
- APA 7th Edition Manual — normas de citación
- ICOM Virtual Museums guidelines — contexto institucional
- Dublin Core Metadata Initiative — estándares de metadatos
- W3C WCAG 2.1 — accesibilidad web
- IIIF (International Image Interoperability Framework) — interoperabilidad de imágenes digitales
