# Requirements: Revisión metodológica del paper HabiTAR

## Contexto

El paper "HabiTAR: Impacto de las tecnologías digitales en la autorregulación emocional y su relación con la inclusión académica de estudiantes universitarios con CEA" (Versión 3) ha recibido observaciones del revisor (marcadas con `$`) que se concentran en la sección de **Metodología**. El cuerpo teórico y la introducción no requieren cambios estructurales mayores.

### Fuentes de referencia
- **Borrador**: `temp_context/Marco teórico V3 -10 Mayo (CF).docx.md` — paper con comentarios del revisor (`$`)
- **Referente metodológico**: `temp_context/Refente-FormulacionIniEsp.docx.md` — se toma únicamente la arquitectura de la metodología (etapas secuenciales, productos, vinculación con objetivos)

### Principio rector
**No se deben realizar cambios mayores al contenido existente del paper.** Solo se abordan las observaciones explícitas del revisor y la reestructuración metodológica.

---

## Requisitos funcionales

### REQ-1: Reestructuración de la metodología con enfoque de ciencias sociales
**Prioridad**: Alta
- Reformular las herramientas de UX Research como procedimientos de investigación social consolidados
- Reemplazar la nomenclatura de design thinking (Empatizar, Definir, Idear, Prototipar, Testear) por etapas de investigación secuenciales numeradas
- Mantener el contenido y sentido de cada fase, pero presentarlo con terminología de ciencias sociales y educación inclusiva

### REQ-2: Especificación de instrumentos de recolección de datos
**Prioridad**: Alta
- Cada etapa debe especificar el tipo de técnica: entrevistas semiestructuradas (individuales o grupales, presenciales o virtuales), grupos focales, talleres participativos, observación participante, card sorting como técnica participativa dentro de entrevistas, sesiones de co-diseño, validación experta
- Indicar los temas o ejes temáticos que cubrirá cada instrumento
- Describir el procedimiento de análisis de información (análisis temático inductivo, transcripción, codificación)

### REQ-3: Explicitación del reclutamiento y participantes
**Prioridad**: Alta
- Cada etapa debe indicar: quiénes participan, por qué fueron seleccionados, de dónde provienen (unidad institucional, fundación, etc.), cómo se contactan, qué características tienen
- Fuentes de reclutamiento sugeridas por el revisor: Unidad de Inclusión y Acompañamiento Estudiantil, Área de Inclusión, Componente de Acompañamiento Psicoeducativo del Área de Acompañamiento Integral
- Indicar criterios de inclusión/exclusión

### REQ-4: Participación de expertos
**Prioridad**: Alta
- Mencionar explícitamente la participación de expertos en las distintas etapas
- Señalar su vínculo institucional y experiencia: especialistas del Centro de Investigación y Fundación de Personas CEA, expertos en psicología vinculada a CEA, especialistas en educación inclusiva, profesionales en accesibilidad y participación comunitaria
- Indicar quién asesora metodológicamente cada instancia

### REQ-5: Vinculación explícita etapas-objetivos
**Prioridad**: Alta
- Cada etapa debe indicar explícitamente a qué objetivo específico responde (OE1, OE2, OE3, OE4)
- Seguir la arquitectura del paper de referencia: etapas secuenciales numeradas con subtítulos descriptivos y vinculación a objetivos

### REQ-6: Productos por etapa
**Prioridad**: Media
- Cada etapa debe cerrar con un producto concreto y verificable
- Los productos configuran insumos para etapas posteriores, mostrando la secuencialidad del diseño

### REQ-7: Incorporación de etapas adicionales del revisor
**Prioridad**: Alta
- Incorporar las 6 etapas sugeridas por el revisor: (1) Empatiza/Descubrimiento, (2) Definir/Análisis, (3) Artículo científico, (4) Idear/Co-diseño, (5) Testear/Evaluación, (6) Devolución/Difusión
- La Etapa 3 (artículo científico) y la Etapa 6 (devolución: seminarios, material para fundaciones, material para política pública) son nuevas respecto al borrador original

### REQ-8: Card sorting como técnica integrada
**Prioridad**: Media
- Presentar card sorting como técnica participativa de categorización y organización conceptual dentro de las entrevistas, no como herramienta aislada
- Explicar que permite comprender cómo las personas estructuran y relacionan información relevante

### REQ-9: Ajustes menores en introducción
**Prioridad**: Baja
- El revisor sugiere terminar la introducción antes del párrafo sobre limitaciones estructurales (línea 17 del borrador) y mover el contenido restante al marco teórico o comprimirlo
- Este es el único cambio estructural fuera de la metodología

### REQ-10: Preservación del contenido teórico
**Prioridad**: Alta (restricción)
- No modificar el planteamiento del problema, marco teórico, pregunta de investigación, hipótesis ni objetivos
- Solo se permite reorganizar texto si el revisor lo indicó explícitamente
- Las referencias bibliográficas se mantienen intactas

---

## Requisitos no funcionales

### RNF-1: Consistencia terminológica
- Usar CEA (no TEA) consistentemente en todo el documento
- Usar "participantes" en lugar de "usuarios" cuando se refiera a contextos de investigación social
- Mantener el lenguaje académico formal

### RNF-2: Formato
- Archivos en Markdown (`.md`) en el directorio `paper/`
- Estructura IMRaD adaptada al paper
- Idioma español para todo el contenido

### RNF-3: Trazabilidad de cambios
- Cada cambio debe poder vincularse a una observación específica del revisor
- Documentar qué comentario `$` se aborda en cada modificación
