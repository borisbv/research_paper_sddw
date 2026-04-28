# Requirements Document

## Introducción

Este documento define los requerimientos para la mejora editorial y de contenido del formulario de postulación FONIS 2026 (`temp_context/Formulario_Postulacion_2026.docx.md`). Los requerimientos se derivan de la auditoría crítica (`temp_context/auditoria_postulacion_fonis_2026.md`) y se limitan a mejoras que pueden resolverse editorialmente, sin requerir decisiones del equipo investigador (los puntos que requieren decisión humana están en `temp_context/backlog_revision_manual_fonis.md`).

**Sujeto EARS:** "el formulario" (refiere al documento de postulación FONIS 2026).

**Archivo fuente:** `temp_context/Formulario_Postulacion_2026.docx.md`

---

## Requirements

### Requirement 1: Actualización del estado del arte con literatura reciente

**Objective:** Como evaluador FONIS, quiero que el estado del arte refleje la evidencia científica actual (2022-2026), para que la propuesta demuestre dominio del campo y justifique adecuadamente el vacío de conocimiento.

#### Acceptance Criteria
1. When el estado del arte es revisado (sección 1.1), the formulario shall incluir al menos 10 referencias publicadas entre 2022 y 2026.
2. When se describe el campo de health literacy digital, the formulario shall citar al menos 3 trabajos recientes sobre intervenciones digitales de health literacy en adultos mayores.
3. When se describe el uso de tecnología para simplificación de textos médicos, the formulario shall citar al menos 2 trabajos sobre NLP o modelos de lenguaje aplicados a simplificación de información en salud.
4. When se describe el contexto latinoamericano, the formulario shall citar al menos 2 experiencias documentadas de salud digital en Chile o América Latina (e.g., Hospital Digital, programas de telemedicina en APS).
5. When se argumenta el vacío de conocimiento, the formulario shall describir brevemente la estrategia de búsqueda utilizada (bases consultadas, términos clave) para respaldar la afirmación de evidencia limitada.
6. The formulario shall mantener las referencias existentes (Berkman, Nutbeam, Sørensen, WHO, MINSAL, SENAMA) y complementarlas con la nueva literatura, sin eliminar citas vigentes.

---

### Requirement 2: Detalle de la solución tecnológica

**Objective:** Como evaluador técnico, quiero comprender la arquitectura y el funcionamiento del prototipo propuesto, para que pueda juzgar la factibilidad técnica y la innovación del proyecto.

#### Acceptance Criteria
1. When se describe la solución (sección 1.2.1), the formulario shall especificar la arquitectura general del sistema (aplicación web, componentes frontend/backend, tecnologías principales).
2. When se describe el módulo de procesamiento de documentos, the formulario shall detallar el mecanismo de adaptación de contenidos (e.g., procesamiento mediante NLP, uso de modelos de lenguaje, reglas de simplificación lingüística) con suficiente especificidad para que un evaluador técnico comprenda el enfoque.
3. When se listan los componentes del prototipo en la tabla de resultado tecnológico, the formulario shall describir la complejidad y función específica de cada componente, diferenciando el núcleo innovador (procesamiento) de los componentes estándar (ingreso, visualización).
4. When se presenta la solución, the formulario shall incluir una descripción del flujo de procesamiento de documentos desde el ingreso hasta la entrega al usuario, indicando las etapas principales de transformación.
5. If la descripción tecnológica utiliza términos genéricos como "procesamiento" o "adaptación" sin especificar el mecanismo, then the formulario shall reemplazarlos por descripciones concretas de la técnica empleada.

---

### Requirement 3: Tabla comparativa de soluciones existentes

**Objective:** Como evaluador FONIS, quiero ver cómo se diferencia la propuesta de las soluciones existentes, para que el valor agregado del proyecto quede explícito.

#### Acceptance Criteria
1. When se presenta el estado del arte (sección 1.1), the formulario shall incluir una tabla comparativa de al menos 4 soluciones o intervenciones existentes relevantes (e.g., OpenNotes, MedlinePlus Easy-to-Read, herramientas de simplificación por IA, intervenciones locales).
2. The formulario shall comparar cada solución en al menos las siguientes dimensiones: enfoque tecnológico, población objetivo, contexto de implementación, validación empírica y limitaciones.
3. When se presenta la tabla comparativa, the formulario shall incluir una fila final o párrafo de síntesis que explicite el valor diferencial de la propuesta respecto a las soluciones listadas.

---

### Requirement 4: Fortalecimiento de hipótesis y pregunta de investigación

**Objective:** Como evaluador científico, quiero que la hipótesis sea específica y falsificable, para que el diseño experimental pueda generar evidencia concluyente.

#### Acceptance Criteria
1. When se formula la hipótesis de investigación (sección 2.1), the formulario shall incluir una cuantificación del efecto esperado (e.g., magnitud de la mejora en comprensión).
2. When se formula la hipótesis operacional, the formulario shall especificar al menos una variable moderadora o mediadora (e.g., nivel educativo, tipo de documento clínico, familiaridad digital).
3. When se listan los supuestos de investigación, the formulario shall reformular aquellos que constituyen preguntas de investigación en sí mismos, diferenciándolos claramente de los supuestos propiamente tales.
4. The formulario shall mantener coherencia entre la pregunta de investigación, la hipótesis y el diseño metodológico descrito.

---

### Requirement 5: Mejora de la sección de ética — protección de datos y seguridad

**Objective:** Como comité de ética, quiero que la propuesta aborde explícitamente la protección de datos personales y la seguridad de información clínica, para que los riesgos asociados al manejo de datos sensibles estén mitigados.

#### Acceptance Criteria
1. When se analizan las implicancias éticas (sección 2.4), the formulario shall mencionar la normativa chilena de protección de datos personales aplicable (Ley 19.628 y/o la Ley 21.719 sobre datos personales).
2. When se describe el manejo de información clínica, the formulario shall especificar las medidas de seguridad para el almacenamiento, procesamiento y eliminación de documentos clínicos ingresados al sistema.
3. When se describe el prototipo en el contexto ético, the formulario shall abordar el riesgo de que la simplificación automática de información clínica distorsione el sentido médico original, y las medidas de mitigación (e.g., revisión profesional, disclaimers).
4. The formulario shall describir las medidas de anonimización o pseudonimización de los datos de participantes en el estudio.

---

### Requirement 6: Datos epidemiológicos concretos de Chile

**Objective:** Como evaluador FONIS, quiero ver cifras concretas sobre la problemática en Chile, para que la relevancia del problema esté sustentada con datos duros y no solo con afirmaciones genéricas.

#### Acceptance Criteria
1. When se describe el envejecimiento poblacional (sección 1.1), the formulario shall incluir datos numéricos actualizados del INE o CASEN sobre la proporción y número absoluto de personas mayores en Chile.
2. When se describe la situación en atención primaria, the formulario shall incluir al menos un dato sobre el volumen de atención de personas mayores en APS (consultas, inscritos, o proporción de la demanda).
3. When se argumenta la relevancia del problema, the formulario shall incluir al menos un dato de prevalencia de baja health literacy en adultos mayores (chileno o latinoamericano, con cita).
4. If se utilizan frases genéricas como "ha aumentado sostenidamente", "persisten brechas relevantes" o "alto potencial de implementación", then the formulario shall acompañarlas con cifras específicas o reemplazarlas por afirmaciones cuantificadas.

---

### Requirement 7: Justificación de indicadores de éxito con literatura

**Objective:** Como evaluador, quiero que los umbrales de éxito propuestos estén respaldados por evidencia, para que los criterios de logro sean técnicamente defendibles.

#### Acceptance Criteria
1. When se define el indicador de comprensión (≥20% de incremento), the formulario shall citar al menos un estudio comparable que respalde la magnitud del efecto esperado o justificar el umbral con un argumento técnico explícito.
2. When se define el indicador de usabilidad (≥70 SUS), the formulario shall justificar el umbral elegido con referencia a la escala SUS y su interpretación estándar (Bangor et al., 2009 o Lewis & Sauro, 2018), considerando que para herramientas de accesibilidad se podría esperar un umbral superior.
3. When se define el indicador de valoración positiva (≥70%), the formulario shall especificar el instrumento y la escala mediante la cual se medirá este porcentaje.

---

### Requirement 8: Reducción de redundancia y mejora de redacción

**Objective:** Como evaluador que lee decenas de propuestas, quiero un texto conciso y sustantivo, para que cada sección aporte información nueva sin repetir contenido de secciones previas.

#### Acceptance Criteria
1. The formulario shall reducir las repeticiones literales de frases clave (e.g., "intervención digital accesible, materializada en un prototipo funcional" no deberá aparecer más de 3 veces en todo el documento).
2. The formulario shall reducir las repeticiones de la frase "accesibilidad cognitiva, lenguaje claro y diseño centrado en el usuario" a un máximo de 3 apariciones, utilizando variaciones o referencias cruzadas en las demás.
3. When se reutiliza una descripción ya presentada en una sección anterior, the formulario shall hacer referencia a la sección previa en lugar de repetir el contenido íntegro.
4. If una frase genérica puede ser reemplazada por un dato concreto o una referencia específica, then the formulario shall realizar dicha sustitución.

---

### Requirement 9: Correcciones tipográficas y de consistencia

**Objective:** Como postulante, quiero que el documento esté libre de errores tipográficos y sea consistente en la nomenclatura, para que la propuesta proyecte rigor y profesionalismo.

#### Acceptance Criteria
1. The formulario shall usar consistentemente el nombre correcto "Fundación Comunidad" en todas las apariciones (corrigiendo "Fundación Comunida" y "Fundación Comunid**a**").
2. The formulario shall verificar que todos los nombres de instituciones, personas y programas estén escritos de forma consistente a lo largo del documento.
3. If existen inconsistencias en la nomenclatura de componentes del sistema entre secciones, then the formulario shall unificar la terminología.
