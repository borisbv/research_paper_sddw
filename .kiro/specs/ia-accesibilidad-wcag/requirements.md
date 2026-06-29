# Requirements Document

## Introduction
Paper científico en estructura IMRaD que analiza y categoriza 41 tecnologías de inteligencia artificial según su utilidad para la accesibilidad web bajo las pautas WCAG 2.2 del W3C. El estudio se basa en un dataset propio que evalúa dimensiones de usabilidad, robustez y operabilidad, cruzadas con tipos de discapacidad (visual, motora, cognitiva, auditiva). El paper busca llenar un vacío de conocimiento en la intersección IA-accesibilidad web, fundamentado en literatura reciente de alto impacto (Scopus/WoS Q1-Q2, 2021-2026).

## Requirements

### Requirement 1: Marco teórico y fundamentación bibliográfica
**Objective:** Como investigador, quiero un marco teórico robusto con autores de reconocida trayectoria en accesibilidad web e IA, para que el paper tenga rigor científico y credibilidad en revistas indexadas.

#### Acceptance Criteria
1. The paper shall fundamentar cada concepto clave (IA, accesibilidad web, WCAG 2.2, tecnologías asistivas, diseño universal) con al menos 3 referencias de revistas Scopus/WoS Q1-Q2 publicadas entre 2021 y 2026.
2. The paper shall incluir una revisión de la evolución de las pautas WCAG (1.0 → 2.0 → 2.1 → 2.2) con referencias normativas del W3C.
3. The paper shall definir los 4 principios WCAG (Perceptible, Operable, Comprensible, Robusto) y vincularlos con las capacidades de las tecnologías de IA evaluadas.
4. The paper shall presentar el estado del arte sobre la intersección IA-accesibilidad web, identificando tendencias, enfoques dominantes y brechas investigativas.
5. When se cite un autor o estudio, the paper shall incluir año de publicación, revista y cuartil para garantizar trazabilidad.

### Requirement 2: Metodología de evaluación y categorización
**Objective:** Como investigador, quiero una metodología clara y reproducible para la evaluación de las tecnologías, para que los resultados sean verificables y replicables por otros investigadores.

#### Acceptance Criteria
1. The paper shall describir el diseño metodológico como un estudio documental-descriptivo con enfoque mixto (cualitativo-cuantitativo).
2. The paper shall detallar los criterios de selección de las 41 tecnologías incluidas en el dataset, justificando la muestra.
3. The paper shall definir operacionalmente las 3 dimensiones de evaluación: usabilidad (precisión, sensibilidad, tiempo de respuesta), robustez (multidispositivo, multi-navegador, multi-OS) y operabilidad (navegación por teclado, comandos de voz).
4. The paper shall explicar la escala de evaluación utilizada (1 a 5) y su correspondencia con niveles de cumplimiento WCAG.
5. The paper shall describir el procedimiento de categorización por tipo de discapacidad (visual, motora, cognitiva, auditiva) y tipo de tecnología IA.
6. The paper shall incluir la fuente de datos (dataset en `temp_context/`) y describir su estructura y variables.

### Requirement 3: Categorización por tipo de discapacidad
**Objective:** Como investigador, quiero categorizar las 41 tecnologías según el tipo de discapacidad que atienden, para que se visualice claramente qué áreas están mejor cubiertas y cuáles presentan brechas.

#### Acceptance Criteria
1. The paper shall clasificar cada tecnología en al menos una categoría de discapacidad: visual, motora, cognitiva o auditiva.
2. The paper shall presentar una tabla resumen con la distribución de tecnologías por tipo de discapacidad.
3. The paper shall incluir un análisis de la cobertura por categoría, identificando discapacidades sobrerrepresentadas y subrepresentadas.
4. The paper shall agrupar las tecnologías por tipo de producto (asistentes conversacionales, lectores de pantalla, interfaces cerebro-computadora, seguimiento ocular, control de cursor, navegación por voz, subtitulado automático, herramientas de evaluación).
5. When una tecnología atienda múltiples tipos de discapacidad, the paper shall indicar la discapacidad primaria y las secundarias.

### Requirement 4: Identificación de las 5 mejores tecnologías
**Objective:** Como investigador, quiero identificar las 5 tecnologías que mejor replican los criterios de accesibilidad web como buenas prácticas, para que sirvan como referentes en el campo.

#### Acceptance Criteria
1. The paper shall definir un método de ranking basado en las puntuaciones del dataset (usabilidad, robustez, operabilidad) con pesos justificados.
2. The paper shall presentar las 5 tecnologías mejor puntuadas con su ficha descriptiva: nombre, tipo, discapacidad atendida, puntuación global y justificación.
3. The paper shall analizar por qué estas 5 tecnologías sobresalen, vinculando sus características con los principios WCAG 2.2.
4. The paper shall incluir una tabla comparativa de las 5 tecnologías seleccionadas versus las demás en las dimensiones evaluadas.
5. If dos o más tecnologías obtienen puntuación idéntica, the paper shall aplicar criterios de desempate documentados (e.g., cobertura de discapacidades, gratuidad, disponibilidad de API).

### Requirement 5: Análisis de resultados y visualización de datos
**Objective:** Como investigador, quiero presentar los resultados con visualizaciones claras y análisis estadístico descriptivo, para que los hallazgos sean comprensibles y rigurosos.

#### Acceptance Criteria
1. The paper shall incluir al menos 3 figuras: (a) distribución de tecnologías por tipo de discapacidad, (b) comparativa de puntuaciones por dimensión evaluada, (c) ranking de las top 5.
2. The paper shall incluir al menos 2 tablas: (a) matriz tecnología-discapacidad, (b) tabla comparativa de las 5 mejores tecnologías.
3. The paper shall utilizar estadística descriptiva (media, mediana, desviación estándar) para caracterizar las puntuaciones del dataset.
4. The paper shall referenciar todas las figuras y tablas en el texto con numeración consecutiva.
5. The paper shall generar las figuras con calidad de publicación (300 DPI mínimo) y estilo académico consistente.

### Requirement 6: Discusión del vacío de conocimiento
**Objective:** Como investigador, quiero debatir sobre la existencia de un vacío de conocimiento teórico y práctico en la intersección IA-accesibilidad web, para que el paper aporte una contribución original al campo.

#### Acceptance Criteria
1. The paper shall contrastar los hallazgos del estudio con la literatura existente, identificando convergencias y divergencias.
2. The paper shall argumentar la existencia (o ausencia) de un vacío de conocimiento teórico: falta de marcos conceptuales que integren IA y WCAG.
3. The paper shall argumentar la existencia (o ausencia) de un vacío práctico: brechas en la implementación real de las tecnologías evaluadas.
4. The paper shall discutir las limitaciones del estudio (tamaño de muestra, criterios de selección, temporalidad del dataset).
5. The paper shall proponer líneas futuras de investigación derivadas de los vacíos identificados.
6. The paper shall vincular la discusión con los Objetivos de Desarrollo Sostenible (ODS) relevantes, especialmente ODS 10 (Reducción de desigualdades) y ODS 4 (Educación de calidad).

### Requirement 7: Estructura y formato del manuscrito
**Objective:** Como investigador, quiero que el manuscrito cumpla con el formato IMRaD estándar y esté listo para sometimiento a revista, para que no requiera reformateo posterior.

#### Acceptance Criteria
1. The paper shall seguir la estructura IMRaD: Title, Abstract, Introduction, Methodology, Results, Discussion, Conclusion, References.
2. The paper shall incluir un abstract de máximo 250 palabras con objetivo, metodología, resultados principales y conclusión.
3. The paper shall incluir entre 4 y 6 palabras clave en español e inglés.
4. The paper shall mantener consistencia terminológica a lo largo del manuscrito según un glosario definido.
5. The paper shall utilizar formato de citas consistente (APA 7 o IEEE, según revista objetivo).
6. The paper shall almacenar las referencias en `references/references.bib` en formato BibTeX válido.
7. The paper shall almacenar el contenido del manuscrito en `paper/` en formato Markdown o Quarto (.qmd).

### Requirement 8: Calidad de las referencias bibliográficas
**Objective:** Como investigador, quiero que todas las referencias sean verificables y de alto impacto, para que el paper sea aceptado en revistas indexadas de calidad.

#### Acceptance Criteria
1. The paper shall incluir un mínimo de 30 referencias bibliográficas.
2. The paper shall asegurar que al menos el 60% de las referencias sean de los últimos 5 años (2021-2026).
3. The paper shall incluir referencias de fuentes primarias (artículos originales) y normativas (documentos W3C/WAI).
4. When se incluya una referencia, the paper shall verificar su existencia en CrossRef, DOI o Semantic Scholar.
5. If una referencia no es verificable, the paper shall marcarla con un flag para revisión manual.
6. The paper shall evitar citas de fuentes no académicas (blogs, sitios web comerciales) excepto para documentación técnica oficial.
