# Research & Design Decisions

## Summary
- **Feature**: `habitar-autorregulacion-cea`
- **Discovery Scope**: Extension (revisión y mejora de borrador existente V2→V3)
- **Key Findings**:
  1. El documento fuente ya contiene ~80% del contenido; la tarea principal es reestructurar, aplicar correcciones del revisor y agregar la sección metodológica UX.
  2. El revisor enfatiza consistencia terminológica (CEA, tecnologías móviles, autorregulación emocional) y eliminación de lenguaje de negación como patrón transversal.
  3. La sección de Metodología UX es contenido nuevo que requiere fundamentación bibliográfica en diseño participativo con poblaciones neurodivergentes.

## Research Log

### Correcciones del Revisor (Sesión 3)
- **Context**: Retroalimentación verbal transcrita del tutor/revisor experto.
- **Sources Consulted**: `temp_context/Nota de Revisor -3 SESIÓN_.md`
- **Findings**:
  - Evitar negaciones ("no X sino Y") → reformular en positivo
  - Usar CEA consistentemente; justificar elección sobre TEA
  - Mover objetivos hacia arriba (después del segundo párrafo del planteamiento)
  - No presentar literatura como "revisiones" → usar "los autores X detectaron..."
  - Eliminar negritas excepto 3 términos clave en la intro
  - Cerrar cada sección teórica vinculando con la propuesta propia
  - Reducir peso de adolescencia → recorrer ciclo vital brevemente, foco en universitarios
  - Usar verbos no absolutistas: "explorar" en vez de "determinar"
  - "Trabajos situados en Latinoamérica" (no "trabajos regionales")
  - Sección modelos educativos Chile → mover al final del marco teórico
- **Implications**: Son criterios de aceptación transversales que aplican a todas las secciones del manuscrito.

### Estructura del Manuscrito
- **Context**: Definir el orden final de secciones post-corrección.
- **Sources Consulted**: Documento fuente V2, instrucciones del revisor.
- **Findings**:
  - Orden final: Planteamiento del problema → Objetivo general (temprano) → Argumentación → Objetivos específicos → Metodología UX → Marco teórico (CEA/Prevalencia → Apps para CEA → Modelos educativos Chile) → Referencias.
  - La pregunta de investigación queda como una sola (eliminar la segunda).
  - La hipótesis se mantiene pero se limpia de floreo.
- **Implications**: El diseño debe reflejar este orden como secuencia de componentes/tareas.

### Metodología UX para Neurodivergencia
- **Context**: Sección completamente nueva que debe desarrollarse con respaldo bibliográfico.
- **Sources Consulted**: Conocimiento del dominio UX Research + diseño participativo.
- **Findings**:
  - El enfoque UX participativo se alinea con el paradigma de apoyo centrado en la persona (Pellicano & den Houting, 2022).
  - Fases apropiadas: Descubrimiento/Empatía (entrevistas contextuales) → Análisis (categorización de apps) → Co-diseño (card sorting, workshops participativos) → Evaluación (juicio de expertos, heurísticas).
  - Cada fase mapea directamente a un OE.
  - Requiere citas de: Norman (2013), IDEO (2015), Spinuzzi (2005) para diseño participativo; Fletcher-Watson et al. para co-diseño con población autista.
- **Implications**: La sección debe escribirse en prosa fluida, vinculando cada fase con su OE correspondiente.

## Design Decisions

### Decision: Orden de secciones del marco teórico
- **Context**: El revisor indicó mover "Modelos educativos en Chile" al final del marco teórico.
- **Alternatives Considered**:
  1. Mantener orden original (CEA → Modelos educativos → Apps)
  2. Reordenar: CEA/Prevalencia → Apps para CEA → Modelos educativos Chile
- **Selected Approach**: Opción 2 — CEA/Prevalencia → Apps para CEA → Modelos educativos Chile
- **Rationale**: El revisor argumenta que los modelos educativos funcionan mejor como cierre porque sitúan la brecha específica chilena justo antes de la metodología.
- **Trade-offs**: Requiere reescribir transiciones entre secciones.

### Decision: Terminología CEA vs TEA
- **Context**: El campo está en transición; TEA es más conocido pero CEA es preferido por el paradigma de neurodivergencia.
- **Selected Approach**: Usar CEA consistentemente con justificación explícita en el primer párrafo.
- **Rationale**: Alineamiento con el paradigma de neurodivergencia y recomendación directa del revisor.
- **Trade-offs**: Algunos lectores pueden no reconocer CEA inmediatamente; se mitiga con la justificación en la introducción.

## Risks & Mitigations
- Citas faltantes en afirmaciones clave → marcar con [CITA PENDIENTE] para búsqueda posterior con `/paper:cite`
- Sección metodológica sin validación empírica → fundamentar con literatura metodológica reconocida
- Extensión excesiva del documento → respetar límites de páginas indicados en el documento fuente
