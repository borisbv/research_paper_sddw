# Investigación y decisiones de diseño

## Resumen
- **Feature**: `paper-neurodivergencia-xr-sigradi`
- **Alcance del descubrimiento**: Nuevo artículo científico (greenfield)
- **Hallazgos clave**:
  - El posicionamiento como modelo metodológico (no solo caso de estudio) es la decisión estratégica más importante para la competitividad en SIGraDi
  - La tabla de 5 etapas UX → criterios de diseño funciona como la contribución tangible y transferible del artículo
  - El extracto de Siervo Briones (2026) sobre predictibilidad y estructura visual provee respaldo teórico directo para el hallazgo de anticipación/señalética

## Registro de investigación

### Formato y normas SIGraDi
- **Contexto**: Determinar requisitos formales de publicación para SIGraDi 2026
- **Fuentes consultadas**: Instrucciones del autor proporcionadas en temp_context
- **Hallazgos**:
  - Extensión: 2.500–3.500 palabras
  - Idioma: español (título y cuerpo)
  - Formato de citas: APA 7a edición
  - Se valoran aportes metodológicos y criterios de diseño transferibles
- **Implicaciones**: La estructura debe priorizar la contribución metodológica sobre la narrativa descriptiva

### Ejes conceptuales del marco teórico
- **Contexto**: Identificar cómo articular los 6 ejes (neurodivergencia, UX, co-creación, XR, arte, composición arquitectónica) sin caer en definiciones enciclopédicas
- **Fuentes consultadas**: Resumen existente del paper, referencias validadas, extracto del libro
- **Hallazgos**:
  - Neurodivergencia: marco no patologizante (Baron-Cohen, 2017; Gonzales-Otarola et al., 2023)
  - UX: metodología de 5 etapas como proceso cíclico de co-creación
  - XR: recurso que requiere contextualización pedagógica, no solución inclusiva per se
  - Arte: mediador entre composición arquitectónica y exploración sensorial
  - Predictibilidad y estructura visual: vínculo con Siervo Briones (2026)
- **Implicaciones**: El marco teórico debe construir una discusión que muestre la brecha, no definir conceptos aislados

### Datos empíricos disponibles
- **Contexto**: Evaluar qué evidencia empírica existe para sostener los hallazgos de Resultados
- **Fuentes consultadas**: Resumen del paper, instrucciones del autor
- **Hallazgos**:
  - 52 estudiantes, 2 secciones de Arquitectura, 2 años de implementación
  - Tipos de neurodivergencia encontrados: TDAH, TEA, neurotípicos
  - 5 hallazgos principales: hiperfoco, preferencias sensoriales, anticipación, moodboard, arte como mediador
  - Límites metodológicos reconocidos: perfiles de usuario no capturan complejidad de la neurodivergencia
- **Implicaciones**: Los resultados deben presentarse como hallazgos del proceso UX, no como datos cuantitativos estadísticos

### Referencias base verificadas
- **Contexto**: Evaluar el corpus de referencias disponibles
- **Fuentes consultadas**: Sección de referencias del resumen existente
- **Hallazgos**:
  - 9 referencias ya validadas que cubren: gobernanza educativa, design thinking, neurodivergencia, UX adaptativo, XR en diseño
  - Siervo Briones (2026): fuente clave para predictibilidad y estructura visual en autismo
  - Se necesitarán referencias adicionales para la Discusión (comparación con otros estudios)
- **Implicaciones**: El artículo debe buscar 3-5 referencias adicionales verificables para fortalecer la Discusión

## Evaluación de patrones arquitectónicos

| Opción | Descripción | Fortalezas | Riesgos / Limitaciones | Notas |
|--------|-------------|-----------|---------------------|-------|
| Caso de estudio descriptivo | Narrar DirexLab como experiencia | Más sencillo de escribir | Menor fuerza científica, no transferible | Descartado por instrucciones del autor |
| Modelo metodológico transferible | Proponer criterios de diseño derivados de hallazgos UX | Mayor contribución científica, dialoga con línea SIGraDi | Requiere abstracción más rigurosa | **Seleccionado** |
| Artículo mixto (caso + modelo) | Describir caso y proponer modelo | Cubre ambos ángulos | Riesgo de extensión excesiva en 3.500 palabras | Variante viable pero el foco debe estar en el modelo |

## Decisiones de diseño

### Decisión: Posicionamiento como modelo metodológico
- **Contexto**: El resumen existente (~800 palabras) describe un caso de estudio; el artículo debe ser ~4x más largo y competitivo
- **Alternativas consideradas**:
  1. Expandir el caso de estudio con más detalles narrativos
  2. Proponer un modelo metodológico transferible con criterios de diseño
- **Enfoque seleccionado**: Modelo metodológico con flujo UX → Hallazgos → Criterios → Implementación XR → Aprendizaje
- **Justificación**: SIGraDi valora aportes metodológicos transferibles; la contribución gana fuerza científica
- **Compromisos**: Requiere mayor rigor en la abstracción de hallazgos a criterios generalizables
- **Seguimiento**: Validar que cada criterio propuesto tenga respaldo empírico directo

### Decisión: Integración del extracto de Siervo Briones (2026)
- **Contexto**: Se dispone de un extracto sobre predictibilidad, estructura visual y autonomía en autismo
- **Alternativas consideradas**:
  1. Citar solo en Marco Teórico como definición
  2. Integrar como respaldo teórico del hallazgo de anticipación/señalética
- **Enfoque seleccionado**: Doble integración — Marco Teórico (fundamento) y Resultados (respaldo del hallazgo de anticipación)
- **Justificación**: Fortalece la triangulación teórica del hallazgo más distintivo del estudio
- **Compromisos**: Evitar redundancia entre ambas menciones

### Decisión: Estructura de la tabla síntesis
- **Contexto**: Las instrucciones proponen una tabla de 5 filas (etapas UX) con 4 columnas
- **Enfoque seleccionado**: Mantener la tabla tal como fue propuesta: Etapa UX | Hallazgo | Decisión de diseño | Resultado
- **Justificación**: Sintetiza la contribución de forma visual y transferible; permite a otros investigadores replicar el marco

## Riesgos y mitigaciones
- Extensión insuficiente en Resultados → Mitigación: es la sección más larga (900 palabras), desarrollar cada hallazgo como subsección
- Afirmaciones sin respaldo en Discusión → Mitigación: buscar referencias adicionales verificables antes de redactar
- Redundancia entre resumen existente y artículo → Mitigación: usar el resumen como base pero reescribir completamente, no copiar párrafos

## Referencias
- Instrucciones del autor: `temp_context/instrucciones.md`
- Resumen existente del paper: `temp_context/paper-resumen.md`
- Extracto libro Siervo Briones: `temp_context/extracto-libro.md`
- Referencias validadas: ver sección 8 de requirements.md (9 referencias con DOI)
