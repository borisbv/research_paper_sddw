# Design: Revisión metodológica del paper HabiTAR

## Visión general

La sección de Metodología se reestructura desde un modelo de design thinking (Empatizar-Definir-Idear-Prototipar-Testear) hacia un diseño secuencial de **seis etapas** numeradas, siguiendo la arquitectura del paper de referencia. Se mantiene el enfoque UX participativo pero se presenta con terminología y procedimientos consolidados en ciencias sociales.

## Arquitectura de la metodología reestructurada

### Introducción metodológica (sin cambios sustantivos)
- Se conserva el encuadre epistemológico: enfoque constructivista, diseño participativo, UX Research
- Se agregan referencias a la tradición cualitativa en ciencias sociales (Mason, 2002; diseño abductivo-inductivo)
- Se explicita el diseño secuencial de seis etapas con vinculación a objetivos

### Etapa 1: Descubrimiento y caracterización contextual (OE1)
**Antes**: "Empatiza" con entrevistas contextuales y journey maps
**Ahora**: Entrevistas semiestructuradas individuales + card sorting integrado

| Elemento | Descripción |
|----------|-------------|
| **Técnica** | Entrevistas semiestructuradas individuales, presenciales, en dependencias de la universidad patrocinante o colaboradora |
| **Card sorting** | Actividad de categorización participativa integrada dentro de la entrevista |
| **Participantes** | Estudiantes universitarios con CEA, reclutados vía Unidad de Inclusión y Acompañamiento Estudiantil |
| **Criterios de selección** | Diagnóstico formal de CEA, matrícula vigente en educación superior, consentimiento informado |
| **Ejes temáticos** | Barreras y facilitadores de autorregulación emocional, experiencias sensoriales en el contexto académico, estrategias actuales de regulación, uso de tecnologías |
| **Análisis** | Transcripción íntegra, codificación en software especializado (NVivo), análisis temático inductivo |
| **Asesoría** | Especialistas en psicología vinculada a CEA y en educación inclusiva |
| **Producto** | Catastro de barreras, facilitadores y estrategias de autorregulación de universitarios con CEA |

### Etapa 2: Análisis y categorización de aplicaciones móviles (OE2)
**Antes**: "Definir" con análisis sistemático + evaluación heurística
**Ahora**: Revisión sistemática de aplicaciones + evaluación heurística con participación de expertos

| Elemento | Descripción |
|----------|-------------|
| **Técnica** | Revisión sistemática de aplicaciones en plataformas móviles (App Store, Google Play) + evaluación heurística (Nielsen, 1994) adaptada a perfiles CEA |
| **Participantes-expertos** | Panel de expertos en tecnología educativa, accesibilidad y CEA del Centro de Investigación y Fundación de Personas CEA |
| **Criterios de categorización** | Funcionalidades, fundamentos teóricos, evidencia de efectividad, accesibilidad sensorial y cognitiva |
| **Análisis** | Matrices de categorización funcional y pedagógica, análisis heurístico con rúbrica de usabilidad adaptada |
| **Producto** | Categorización de aplicaciones móviles según pertinencia técnica y pedagógica para universitarios con CEA |

### Etapa 3: Elaboración de artículo científico (OE1 + OE2)
**Nueva etapa** (solicitada por el revisor)

| Elemento | Descripción |
|----------|-------------|
| **Actividad** | Consolidación de hallazgos de Etapas 1 y 2 en artículo para revista indexada (WoS/Scopus) |
| **Producto** | Artículo científico enviado a revista indexada |

### Etapa 4: Co-diseño participativo de requerimientos funcionales (OE3)
**Antes**: "Idear" con card sorting + talleres de co-diseño + prototipos de baja fidelidad
**Ahora**: Talleres participativos con dinámicas de categorización colectiva y sesiones de co-diseño

| Elemento | Descripción |
|----------|-------------|
| **Técnica** | Talleres participativos con dos componentes: (a) dinámicas de categorización colectiva (card sorting grupal), (b) sesiones de co-diseño con elaboración de prototipos de baja fidelidad |
| **Participantes** | Estudiantes universitarios con CEA que participaron en Etapa 1 + nuevos participantes reclutados por las mismas vías |
| **Criterios de selección** | Mismos que Etapa 1 |
| **Ejes temáticos** | Priorización de funcionalidades, organización de categorías de apoyo emocional, expectativas de diseño sensorial |
| **Adaptaciones** | Flexibilidad en formatos de comunicación, previsibilidad en estructura de actividades, respeto por necesidades sensoriales del entorno (Benton et al., 2012) |
| **Análisis** | Transcripción de sesiones, análisis temático inductivo, triangulación con hallazgos de Etapas 1-2 |
| **Asesoría** | Especialistas en accesibilidad y participación comunitaria |
| **Producto** | Requerimientos funcionales priorizados para una propuesta de tecnología móvil |

### Etapa 5: Evaluación mediante juicio de expertos y usuarios clave (OE4)
**Antes**: "Prototipar/Testear" con panel de expertos + consultas a usuarios
**Ahora**: Validación experta + grupos focales con usuarios clave

| Elemento | Descripción |
|----------|-------------|
| **Técnica** | (a) Validación experta mediante rúbrica estructurada, (b) grupos focales con usuarios clave |
| **Panel de expertos** | Profesionales de tecnología educativa, psicología del desarrollo y educación inclusiva; se indica vínculo institucional y experiencia |
| **Usuarios clave** | Estudiantes universitarios con CEA participantes de etapas previas |
| **Criterios de evaluación** | Pertinencia, viabilidad, coherencia teórica, correspondencia con expectativas de usuarios |
| **Análisis** | Triangulación entre perspectiva experta y experiencia de usuarios |
| **Producto** | Propuesta de tecnología móvil evaluada y ajustada |

### Etapa 6: Devolución y difusión (transversal)
**Nueva etapa** (solicitada por el revisor)

| Elemento | Descripción |
|----------|-------------|
| **Actividades** | Seminarios de difusión, elaboración de material para fundaciones de personas CEA, documentos orientados a política pública |
| **Participantes** | Comunidad académica, fundaciones, entidades de política pública |
| **Producto** | Material de difusión y recomendaciones de política para integración de tecnologías de apoyo en educación superior |

## Cambio en introducción (REQ-9)

- Cortar la introducción después del párrafo que termina en "situación que adquiere especial relevancia en los procesos de transición educativa" (línea 15 del borrador)
- Agregar cierre que remarque la relevancia
- Mover los párrafos sobre limitaciones estructurales y tecnologías al inicio del marco teórico o comprimir como transición

## Restricciones de diseño

1. **No se modifica**: planteamiento del problema (salvo corte de introducción), marco teórico, pregunta de investigación, hipótesis, objetivos, referencias
2. **Se mantiene**: el enfoque UX participativo como marco general, pero presentado con terminología de ciencias sociales
3. **Se preserva**: la secuencia lógica OE1→OE2→OE3→OE4
4. **Se agrega**: trazabilidad explícita de cada cambio a un comentario `$` del revisor

## Archivos afectados

| Archivo | Acción |
|---------|--------|
| `paper/metodologia.md` (nuevo) | Sección de metodología reestructurada |
| `paper/introduccion.md` (si existe) | Ajuste menor: corte y reubicación de párrafos |
| `paper/marco-teorico.md` (si existe) | Posible recepción de párrafos movidos desde introducción |
