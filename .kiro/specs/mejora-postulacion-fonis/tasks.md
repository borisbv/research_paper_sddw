# Implementation Plan

## Fase 1: Research consolidado

- [x] 1. Búsqueda y validación de literatura científica reciente (2022-2026)
- [x] 1.1 (P) Buscar literatura sobre health literacy digital en adultos mayores
  - Buscar en PubMed y Semantic Scholar con términos: "health literacy" AND ("older adults" OR "elderly") AND "digital intervention"
  - Seleccionar al menos 3 referencias publicadas entre 2022 y 2026 que aborden intervenciones digitales de health literacy en personas mayores
  - Validar DOI y metadatos de cada referencia
  - Registrar autor, año, título, revista, DOI y hallazgo principal relevante para el proyecto
  - _Requirements: 1.1, 1.2_

- [x] 1.2 (P) Buscar literatura sobre NLP e IA aplicados a simplificación de textos médicos
  - Buscar en PubMed y Google Scholar con términos: "NLP" OR "large language model" AND "health information" AND "simplification" OR "plain language"
  - Seleccionar al menos 2 referencias de 2022-2026 sobre uso de NLP o modelos de lenguaje para simplificar información en salud
  - Incluir al menos 1 referencia sobre riesgos o limitaciones de simplificación automática (para sección de ética)
  - Validar DOI y metadatos
  - _Requirements: 1.1, 1.3_

- [x] 1.3 (P) Buscar experiencias de salud digital en Chile y América Latina
  - Buscar referencias sobre Hospital Digital Chile, programas de telemedicina en APS, salud digital en LATAM
  - Seleccionar al menos 2 referencias documentadas de experiencias de salud digital en la región
  - Incluir al menos 1 referencia específica del contexto chileno
  - Validar fuentes y accesibilidad de cada referencia
  - _Requirements: 1.1, 1.4_

- [x] 1.4 Consolidar pool de referencias y generar archivo de research
  - Compilar todas las referencias de 1.1, 1.2 y 1.3 en un archivo único `temp_context/research_refs_fonis.md`
  - Organizar por temática: (a) health literacy digital, (b) NLP/IA en salud, (c) salud digital LATAM/Chile
  - Verificar que el total sea ≥10 referencias de 2022-2026
  - Formatear cada entrada con: autor, año, título, revista, DOI, relevancia para el proyecto
  - Requiere completar 1.1, 1.2 y 1.3
  - _Requirements: 1.1, 1.6_

- [x] 2. (P) Obtener datos epidemiológicos actualizados de Chile
  - Buscar en fuentes oficiales (INE, CASEN 2022, DEIS-MINSAL, SENAMA) datos sobre: proporción y número absoluto de personas ≥60 años en Chile, volumen de atención de personas mayores en APS (inscritos o consultas), prevalencia de baja health literacy en adultos mayores (dato chileno o latinoamericano)
  - Registrar cada dato con su fuente exacta, año y URL de acceso
  - Verificar que los datos sean los más recientes disponibles
  - Producir un bloque de texto listo para insertar en sección 1.1
  - _Requirements: 6.1, 6.2, 6.3, 6.4_

- [x] 3. (P) Investigar y definir la propuesta técnica del prototipo
  - Investigar arquitecturas de referencia para sistemas de simplificación de textos médicos (web apps con módulo NLP/LLM)
  - Definir arquitectura coherente con el perfil técnico del equipo (Node.js, React, APIs RESTful, ML): frontend React accesible, backend Node.js con API REST, módulo de procesamiento NLP/LLM
  - Describir flujo de procesamiento de documentos en 4-5 etapas: ingreso → preprocesamiento → simplificación NLP/LLM → revisión de fidelidad clínica → visualización accesible
  - Identificar al menos 4 soluciones existentes comparables para la tabla comparativa (OpenNotes, MedlinePlus Easy-to-Read, herramientas de simplificación por IA, intervenciones locales) con sus características, limitaciones y diferencias con la propuesta
  - Producir descripción técnica y tabla comparativa como bloques listos para insertar
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3_

## Fase 2: Ediciones por sección

- [x] 4. Editar sección 1.1 — Estado del arte y planteamiento del problema
- [x] 4.1 Integrar nueva literatura y datos epidemiológicos en el estado del arte
  - Leer la sección 1.1 actual (líneas 29–47) del formulario
  - Insertar las referencias del pool bibliográfico (task 1.4) de forma orgánica en el texto, manteniendo las referencias existentes (Berkman, Nutbeam, Sørensen, WHO, MINSAL, SENAMA)
  - Reemplazar frases genéricas ("ha aumentado sostenidamente", "persisten brechas relevantes") por afirmaciones con cifras concretas del research epidemiológico (task 2)
  - Incorporar breve descripción de la estrategia de búsqueda utilizada (bases consultadas, términos clave) para respaldar la afirmación de evidencia limitada
  - Requiere completar tasks 1.4 y 2
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 6.1, 6.2, 6.3, 6.4_

- [x] 4.2 Agregar tabla comparativa de soluciones existentes
  - Insertar en la sección 1.1 la tabla comparativa producida en task 3, con ≥4 soluciones existentes
  - La tabla debe comparar: enfoque tecnológico, población objetivo, contexto de implementación, validación empírica, limitaciones
  - Agregar párrafo de síntesis posterior a la tabla que explicite el valor diferencial de la propuesta
  - Requiere completar task 3
  - _Requirements: 3.1, 3.2, 3.3_

- [x] 5. (P) Editar sección 1.2.1 — Descripción de la solución tecnológica
  - Leer la sección 1.2.1 actual (líneas 49–65) del formulario
  - Reescribir la descripción especificando: arquitectura web (frontend React accesible + backend Node.js), módulo de procesamiento (NLP/LLM + reglas de accesibilidad cognitiva), flujo de procesamiento en 4-5 etapas
  - Diferenciar explícitamente los componentes por nivel de innovación: módulo de ingreso (estándar), módulo de procesamiento (núcleo innovador), interfaces (frontend accesible)
  - Reemplazar términos genéricos ("procesamiento", "adaptación") por descripciones concretas de las técnicas empleadas
  - Actualizar las celdas relevantes en tablas de resultado tecnológico (líneas 106–124) para reflejar los componentes detallados
  - Requiere completar task 3
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 6. (P) Editar tablas de resultado tecnológico — Justificación de indicadores de éxito
  - Leer las tablas de resultado tecnológico (líneas 106–124) del formulario
  - Justificar el indicador de comprensión (≥20% de incremento) citando al menos un estudio comparable del pool bibliográfico
  - Justificar el indicador de usabilidad (≥70 SUS) referenciando la interpretación estándar de la escala SUS (Bangor et al., 2009 o Lewis & Sauro, 2018)
  - Especificar el instrumento concreto para medir valoración positiva (≥70%), indicando la escala
  - Editar las celdas de indicadores y atributos en las tablas preservando el formato markdown
  - Requiere completar task 1.4
  - _Requirements: 7.1, 7.2, 7.3_

- [x] 7. Editar sección 2.1 — Fortalecer hipótesis y pregunta de investigación
  - Leer la sección 2.1 actual (líneas 166–182) del formulario
  - Reformular la hipótesis de investigación incluyendo una cuantificación del efecto esperado (e.g., magnitud de mejora en comprensión), coherente con los indicadores justificados en task 6
  - Reformular la hipótesis operacional agregando al menos una variable moderadora (nivel educativo, tipo de documento clínico, o familiaridad digital)
  - Revisar los supuestos de investigación: reformular aquellos que constituyen preguntas de investigación en sí mismos (e.g., "la implementación es factible y aceptable") diferenciándolos de los supuestos propiamente tales
  - Verificar coherencia entre pregunta de investigación, hipótesis y diseño metodológico descrito en sección 2.3
  - Requiere completar task 6
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [x] 8. (P) Editar sección 2.4 — Protección de datos y seguridad de información clínica
  - Leer la sección 2.4 actual (líneas 297–316) del formulario
  - Agregar un apartado sobre protección de datos personales mencionando la Ley 19.628 y la Ley 21.719 sobre datos personales
  - Describir medidas de seguridad para el almacenamiento, procesamiento y eliminación de documentos clínicos ingresados al prototipo
  - Agregar un apartado sobre el riesgo de que la simplificación automática distorsione el sentido médico original, incluyendo medidas de mitigación (revisión por profesional de salud, disclaimers, validación clínica)
  - Describir las medidas de anonimización o pseudonimización de datos de participantes en el estudio
  - Tarea independiente, no requiere outputs de otras tareas
  - _Requirements: 5.1, 5.2, 5.3, 5.4_

## Fase 3: Ediciones transversales

- [x] 9. Reducir redundancia y mejorar concisión del documento
  - Buscar y contar las apariciones de frases clave repetidas en todo el documento: "intervención digital accesible, materializada en un prototipo funcional" y "accesibilidad cognitiva, lenguaje claro y diseño centrado en el usuario"
  - Reducir cada frase a un máximo de 3 apariciones, reemplazando las demás por variaciones, abreviaciones o referencias cruzadas a la sección donde se define por primera vez
  - Identificar secciones que repiten contenido íntegro de secciones anteriores y reemplazar por referencias cruzadas
  - Identificar frases genéricas restantes ("contextos reales de atención primaria", "mejora significativa", "alto potencial de implementación") y sustituir por datos concretos o referencias específicas donde sea posible
  - Requiere que todas las tareas de Fase 2 estén completadas
  - _Requirements: 8.1, 8.2, 8.3, 8.4_

- [x] 10. Correcciones tipográficas y unificación de nomenclatura
  - Verificar el nombre real de la fundación colaboradora (¿"Fundación Comunida" o "Fundación Comunidad"?) y corregir todas las apariciones para que sean consistentes
  - Buscar y verificar que todos los nombres de instituciones (UTEM, PUCV, SENADIS), personas y programas estén escritos de forma consistente en todo el documento
  - Unificar la nomenclatura de los componentes del sistema entre la sección 1.2.1 y las tablas de resultado tecnológico
  - Requiere que task 9 esté completada
  - _Requirements: 9.1, 9.2, 9.3_

## Fase 4: Auditoría de planilla de costos

- [x] 12. Auditoría y corrección de planilla de costos FONIS 2026
- [x] 12.1 Verificar aritmética de todas las secciones de la planilla de costos
  - Verificar cálculos de personal contratado, preexistente con pago adicional, personal sin subsidio, equipos, operación y overhead
  - Verificar subtotales y totales generales
  - Confirmar cuadratura ANID = $72,000,000
  - Resultado: aritmética correcta en todas las secciones
  - _Requirements: Planilla de costos_

- [x] 12.2 Corregir ANTECEDENTES: agregar PUCV y corregir nombre de fundación
  - Corregir "Fundación Comunida" → "Fundación Comunidad"
  - Agregar PUCV como entidad asociada (Sandra Cano y Nicolás Matus aportan $46,080,000)
  - _Requirements: 9.1, Admisibilidad bases FONIS (1-5 entidades colaboradoras)_

- [x] 12.3 Desglosar gastos de operación y agregar ítems faltantes
  - Reemplazar renglón genérico de $3,000,000 "Gastos generales" por 7 ítems específicos:
    - Material de oficina e insumos talleres ($500,000)
    - Viáticos nacionales CESFAM ($800,000)
    - Licencias software UX/desarrollo ($400,000)
    - Hosting cloud e infraestructura API LLM ($1,200,000)
    - Incentivos participantes del estudio ($900,000)
    - Seguro equipos financiados ANID ($150,000)
    - Producción cápsula audiovisual ($350,000)
  - Mantener pasaje ($700,000) y viático internacional ($500,000) sin cambios
  - Nuevo subtotal operación: $5,500,000
  - _Requirements: Bases FONIS 7.5.4, 7.5.2 (seguro obligatorio)_

- [x] 12.4 Ajustar overhead para mantener cuadratura ANID
  - Reducir overhead de $4,750,000 (6.6%) a $3,450,000 (4.8%) para compensar aumento en operación
  - Verificar que se mantiene bajo el máximo 15%
  - Total ANID verificado: $72,000,000 (sin cambios)
  - _Requirements: Bases FONIS 7.5.5_

## Validación

- [x] 11. Validación final del formulario editado
  - Contar las referencias 2022-2026 en el documento (verificar ≥10)
  - Verificar que la sección 1.2.1 nombre tecnologías y flujo concretos
  - Verificar presencia de tabla comparativa con ≥4 soluciones y 5 dimensiones
  - Verificar que la hipótesis incluya cuantificación y variable moderadora
  - Verificar mención de Ley 19.628/21.719, medidas de seguridad y riesgo de distorsión en sección 2.4
  - Verificar presencia de ≥3 datos numéricos con fuente en sección 1.1
  - Verificar que cada indicador de éxito tenga cita o justificación técnica
  - Contar apariciones de frases clave (verificar ≤3 cada una)
  - Buscar "Comunida" sin "d" final y verificar consistencia de nombres de instituciones
  - Verificar que las referencias originales (Berkman, Nutbeam, Sørensen, WHO, MINSAL, SENAMA) no hayan sido eliminadas
  - Verificar que las tablas markdown mantengan formato correcto
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3_
