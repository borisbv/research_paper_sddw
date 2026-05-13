# Tasks: Revisión metodológica del paper HabiTAR

## Fase preparatoria

### Task 1: Crear estructura de archivos del paper
- [x] Crear directorio `paper/` si no existe
- [x] Migrar el contenido del borrador (`temp_context/Marco teórico V3 -10 Mayo (CF).docx.md`) a archivos separados por sección en `paper/`:
  - `paper/00-titulo-abstract.md`
  - `paper/01-introduccion.md`
  - `paper/02-marco-teorico.md`
  - `paper/03-pregunta-objetivos.md`
  - `paper/04-metodologia.md`
  - `paper/05-referencias.md`
- **Criterio**: cada archivo contiene una sección completa, sin comentarios del revisor mezclados con el texto

### Task 2: Extraer y documentar observaciones del revisor
- [x] Crear `paper/revisiones/observaciones-revisor.md` con todas las observaciones `$` extraídas del borrador
- [x] Cada observación debe tener: ubicación original, texto completo, etapa/sección afectada, requisito asociado (REQ-X)
- **Criterio**: documento de trazabilidad completo que permita verificar que cada observación fue atendida

## Fase de implementación: Introducción (REQ-9)

### Task 3: Ajustar corte de la introducción
- [x] En `paper/01-introduccion.md`, terminar la sección después del párrafo sobre modelos transmisivos y exclusión encubierta
- [x] Agregar un párrafo de cierre que remarque la relevancia del problema
- [x] Mover los párrafos restantes (transición a educación superior, tecnologías) a `paper/02-marco-teorico.md` como transición o comprimirlos
- **Criterio**: la introducción cierra con la relevancia del problema; el contenido no se pierde sino que se reubica
- **Trazabilidad**: comentario del revisor línea 17

## Fase de implementación: Metodología (REQ-1 a REQ-8)

### Task 4: Escribir introducción metodológica
- [x] Redactar párrafo introductorio del enfoque: constructivista, diseño participativo, UX Research articulado con ciencias sociales
- [x] Describir el diseño secuencial de seis etapas con vinculación explícita a objetivos
- [x] Incluir diagrama textual o tabla resumen de etapas-objetivos-técnicas
- **Criterio**: el lector entiende la arquitectura completa antes de leer cada etapa
- **Trazabilidad**: REQ-1, REQ-5

### Task 5: Escribir Etapa 1 — Descubrimiento y caracterización contextual (OE1)
- [x] Describir entrevistas semiestructuradas individuales con ejes temáticos
- [x] Integrar card sorting como técnica participativa dentro de la entrevista
- [x] Especificar: participantes (estudiantes CEA), reclutamiento (Unidad de Inclusión), criterios de selección, modalidad (presencial/virtual), lugar
- [x] Describir análisis: transcripción, codificación en NVivo, análisis temático inductivo
- [x] Indicar asesoría metodológica: especialistas en psicología CEA y educación inclusiva
- [x] Definir producto: catastro de barreras, facilitadores y estrategias de autorregulación
- **Criterio**: cumple todos los elementos que el revisor pidió explicitar (quién, por qué, qué técnica, cómo, quién asesora, relación con OE)
- **Trazabilidad**: REQ-2, REQ-3, REQ-4, REQ-5, REQ-6, REQ-8

### Task 6: Escribir Etapa 2 — Análisis y categorización de aplicaciones móviles (OE2)
- [x] Describir revisión sistemática de aplicaciones en plataformas móviles
- [x] Describir evaluación heurística adaptada a perfiles CEA
- [x] Especificar participación de panel de expertos (Centro de Investigación, Fundación CEA)
- [x] Definir producto: categorización funcional y pedagógica de apps
- **Trazabilidad**: REQ-2, REQ-4, REQ-5, REQ-6

### Task 7: Escribir Etapa 3 — Elaboración de artículo científico (OE1 + OE2)
- [x] Describir consolidación de hallazgos de Etapas 1 y 2
- [x] Definir producto: artículo enviado a revista indexada WoS/Scopus
- **Trazabilidad**: REQ-7 (etapa nueva solicitada por revisor)

### Task 8: Escribir Etapa 4 — Co-diseño participativo (OE3)
- [x] Describir talleres participativos con dos componentes: categorización colectiva + co-diseño
- [x] Especificar adaptaciones para participantes CEA (Benton et al., 2012)
- [x] Indicar participantes, reclutamiento, ejes temáticos
- [x] Describir análisis y triangulación
- [x] Indicar asesoría: especialistas en accesibilidad y participación comunitaria
- [x] Definir producto: requerimientos funcionales priorizados
- **Trazabilidad**: REQ-2, REQ-3, REQ-4, REQ-5, REQ-6, REQ-8

### Task 9: Escribir Etapa 5 — Evaluación mediante juicio de expertos y usuarios clave (OE4)
- [x] Describir validación experta con rúbrica estructurada
- [x] Describir grupos focales con usuarios clave (estudiantes CEA de etapas previas)
- [x] Especificar composición del panel de expertos con vínculo institucional
- [x] Describir triangulación entre perspectiva experta y experiencia de usuarios
- [x] Definir producto: propuesta evaluada y ajustada
- **Trazabilidad**: REQ-2, REQ-4, REQ-5, REQ-6

### Task 10: Escribir Etapa 6 — Devolución y difusión
- [x] Describir actividades: seminarios, material para fundaciones, documentos de política pública
- [x] Definir producto: material de difusión y recomendaciones
- **Trazabilidad**: REQ-7 (etapa nueva solicitada por revisor, línea ~229)

### Task 11: Escribir cierre metodológico
- [x] Párrafo integrador que explique la coherencia del diseño secuencial
- [x] Vincular con tradición del diseño participativo y ciencias sociales
- [x] Mencionar la retroalimentación entre etapas
- **Criterio**: cierra la sección con visión de conjunto

## Fase de validación

### Task 12: Verificación cruzada observaciones-implementación
- [x] Revisar cada observación `$` del revisor en `paper/revisiones/observaciones-revisor.md`
- [x] Marcar como atendida, indicando en qué task y archivo se resolvió
- [x] Verificar que no quedaron observaciones sin atender
- **Criterio**: 100% de observaciones del revisor atendidas o justificadamente descartadas

### Task 13: Validación de coherencia interna
- [x] Verificar que cada etapa indica: participantes, selección, técnica, procedimiento, asesoría, relación con OE
- [x] Verificar que los 4 OE están cubiertos por al menos una etapa
- [x] Verificar consistencia terminológica (CEA, no TEA; participantes, no usuarios)
- [x] Verificar que el contenido del marco teórico y pregunta de investigación no fue alterado
- **Criterio**: pasa la checklist de elementos por etapa sin omisiones
