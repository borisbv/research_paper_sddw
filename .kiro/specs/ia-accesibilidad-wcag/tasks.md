# Implementation Plan

- [x] 1. Configuración del proyecto y pipeline de datos
- [x] 1.1 Configurar estructura Quarto para el paper
  - Crear los 8 archivos .qmd del paper (00-title hasta 07-references) con frontmatter básico
  - Actualizar `_quarto.yml` para incluir los nuevos archivos del paper, configurar bibliografía y formato de citas
  - Crear directorio `paper/data/` para datos procesados exportados
  - Inicializar `references/references.bib` con estructura base
  - Verificar que `quarto render` compila sin errores con los archivos vacíos
  - _Requirements: 7.1, 7.5, 7.6, 7.7_

- [x] 1.2 Crear script de procesamiento del dataset CSV
  - Leer el CSV de 41 tecnologías desde `temp_context/`, limpiando las filas de encabezado irregular
  - Aplicar la tabla de mapeo categórico → numérico definida en el design (precisión, sensibilidad, tiempo de respuesta, navegación por teclado, comandos de voz)
  - Calcular estadísticas descriptivas por dimensión: media, mediana, desviación estándar para usabilidad, robustez y operabilidad
  - Generar la matriz cruzada tecnología × tipo de discapacidad
  - Exportar los archivos procesados a `paper/data/`: tecnologias_procesadas.csv, matriz_discapacidad.csv, estadisticas_descriptivas.json
  - Validar que las 41 tecnologías se cargan completas y alertar si hay valores faltantes
  - _Requirements: 2.3, 2.4, 2.6, 3.1, 3.2, 3.5_

- [x] 1.3 Implementar algoritmo de ranking y selección top 5
  - Calcular puntuación global ponderada por tecnología usando los pesos definidos: usabilidad 0.40, robustez 0.30, operabilidad 0.30
  - Ordenar las tecnologías por puntuación descendente y seleccionar las 5 mejores
  - Implementar criterios de desempate: cobertura de discapacidades > gratuidad > disponibilidad de API
  - Exportar ranking_global.csv con puntuaciones por dimensión y puntuación global
  - Generar ficha descriptiva de cada tecnología del top 5: nombre, tipo, discapacidad atendida, puntuación y justificación
  - _Requirements: 4.1, 4.2, 4.5_

- [x] 2. Generación de visualizaciones académicas
- [x] 2.1 (P) Crear figura de distribución de tecnologías por tipo de discapacidad
  - Generar gráfico de barras mostrando cuántas tecnologías atienden cada tipo de discapacidad (visual, motora, cognitiva, auditiva)
  - Incluir tecnologías con múltiples discapacidades en cada categoría correspondiente
  - Aplicar estilo académico consistente (seaborn whitegrid, 300 DPI)
  - Exportar a `figures/fig-distribucion-discapacidad.png`
  - _Requirements: 5.1, 5.5_

- [x] 2.2 (P) Crear figura comparativa de puntuaciones por dimensión evaluada
  - Generar gráfico que compare las puntuaciones medias de usabilidad, robustez y operabilidad del conjunto de tecnologías
  - Incluir barras de error con desviación estándar
  - Aplicar estilo académico consistente (300 DPI)
  - Exportar a `figures/fig-comparativa-dimensiones.png`
  - _Requirements: 5.1, 5.3, 5.5_

- [x] 2.3 (P) Crear figura de ranking de las top 5 tecnologías
  - Generar gráfico de barras horizontales con las 5 mejores tecnologías y sus puntuaciones globales
  - Incluir desglose por dimensión (usabilidad, robustez, operabilidad) con colores diferenciados
  - Aplicar estilo académico consistente (300 DPI)
  - Exportar a `figures/fig-ranking-top5.png`
  - _Requirements: 5.1, 5.5_

- [x] 2.4 Generar tablas en formato Markdown para inclusión en el manuscrito
  - Exportar tabla de matriz tecnología × discapacidad con indicadores de discapacidad primaria y secundaria
  - Exportar tabla comparativa de las 5 mejores tecnologías versus promedios generales en cada dimensión
  - Guardar tablas en `paper/data/` en formato Markdown para inclusión directa en los archivos .qmd
  - _Requirements: 5.2, 5.4_

- [x] 3. Búsqueda y gestión de referencias bibliográficas
- [x] 3.1 Buscar y compilar referencias sobre accesibilidad web y WCAG
  - Buscar artículos en Scopus/WoS Q1-Q2 (2021-2026) sobre accesibilidad web, WCAG 2.2 y diseño universal
  - Incluir documentos normativos del W3C/WAI sobre la evolución de las pautas WCAG
  - Buscar artículos sobre los 4 principios WCAG (Perceptible, Operable, Comprensible, Robusto) y su implementación
  - Generar entradas BibTeX válidas y agregarlas a `references/references.bib`
  - Verificar existencia de DOI para cada referencia incluida
  - _Requirements: 1.1, 1.2, 1.3, 8.1, 8.2, 8.3, 8.4_

- [x] 3.2 (P) Buscar y compilar referencias sobre IA y tecnologías asistivas
  - Buscar artículos Q1-Q2 (2021-2026) sobre inteligencia artificial aplicada a accesibilidad, tecnologías asistivas basadas en IA
  - Buscar literatura sobre la intersección IA-WCAG, identificando estado del arte y brechas
  - Buscar artículos sobre interfaces cerebro-computadora, seguimiento ocular, reconocimiento de voz y lectores de pantalla con IA
  - Generar entradas BibTeX y agregar a `references/references.bib`
  - Verificar DOI y marcar referencias no verificables con flag para revisión manual
  - _Requirements: 1.4, 1.5, 8.1, 8.2, 8.4, 8.5, 8.6_

- [x] 3.3 Auditar calidad del archivo de referencias
  - Verificar que `references.bib` contiene al menos 30 referencias
  - Confirmar que al menos 60% de las referencias son de 2021-2026
  - Validar que no hay fuentes no académicas excepto documentación técnica oficial
  - Verificar formato BibTeX válido para todas las entradas
  - Identificar y marcar referencias sin DOI verificable
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6_

- [x] 4. Redacción del manuscrito — Secciones preliminares
- [x] 4.1 Redactar portada y abstract
  - Escribir título del paper que refleje el alcance del estudio (categorización de tecnologías IA para accesibilidad web WCAG 2.2)
  - Definir autores y afiliaciones institucionales
  - Redactar abstract de máximo 250 palabras con: objetivo, metodología, resultados principales y conclusión
  - Incluir entre 4 y 6 palabras clave en español e inglés
  - _Requirements: 7.1, 7.2, 7.3_

- [x] 4.2 Redactar introducción y marco teórico
  - Presentar el problema de investigación: la brecha entre el potencial de la IA y su aplicación real en accesibilidad web
  - Fundamentar los conceptos clave (IA, accesibilidad web, WCAG 2.2, tecnologías asistivas, diseño universal) con al menos 3 referencias Q1-Q2 por concepto
  - Describir la evolución de las pautas WCAG (1.0 → 2.0 → 2.1 → 2.2) con referencias normativas W3C
  - Definir los 4 principios WCAG y vincularlos con capacidades de IA
  - Presentar el estado del arte sobre IA-accesibilidad web, identificando tendencias y brechas
  - Formular la hipótesis o pregunta de investigación
  - Definir el alcance del estudio
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 5. Redacción del manuscrito — Secciones centrales
- [x] 5.1 Redactar sección de metodología
  - Describir el diseño metodológico como estudio documental-descriptivo con enfoque mixto
  - Detallar criterios de selección de las 41 tecnologías y justificar la muestra
  - Definir operacionalmente las 3 dimensiones de evaluación con sus indicadores
  - Explicar la escala de evaluación y la tabla de mapeo categórico → numérico
  - Describir el procedimiento de categorización por tipo de discapacidad y tipo de tecnología IA
  - Describir la fuente de datos, su estructura y variables
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_

- [x] 5.2 Redactar sección de resultados
  - Presentar la categorización de las 41 tecnologías por tipo de discapacidad con tabla de distribución
  - Analizar cobertura por categoría: identificar discapacidades sobrerrepresentadas (motora) y subrepresentadas (auditiva)
  - Agrupar tecnologías por tipo de producto con análisis de cada grupo
  - Presentar el ranking global con las 5 mejores tecnologías y sus fichas descriptivas
  - Analizar por qué las top 5 sobresalen, vinculando con principios WCAG 2.2
  - Incluir tabla comparativa top 5 versus promedios generales
  - Insertar las 3 figuras generadas con referencia en el texto y numeración consecutiva
  - Insertar las 2 tablas con referencia en el texto
  - Presentar estadísticas descriptivas del conjunto de datos
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3, 5.4_

- [x] 6. Redacción del manuscrito — Secciones finales
- [x] 6.1 Redactar sección de discusión
  - Contrastar los hallazgos con la literatura existente, identificando convergencias y divergencias
  - Argumentar la existencia de un vacío de conocimiento teórico: ausencia de marcos conceptuales que integren IA y WCAG
  - Argumentar la existencia de un vacío práctico: brechas en la implementación real de las tecnologías
  - Discutir las limitaciones del estudio: tamaño de muestra, criterios de selección, temporalidad del dataset, mapeo categórico simplificado
  - Proponer líneas futuras de investigación derivadas de los vacíos identificados
  - Vincular la discusión con ODS 10 (Reducción de desigualdades) y ODS 4 (Educación de calidad)
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6_

- [x] 6.2 Redactar sección de conclusiones
  - Sintetizar los hallazgos principales del estudio
  - Reafirmar la contribución original del paper al campo
  - Resumir las líneas futuras de investigación propuestas
  - _Requirements: 6.5, 7.1_

- [x] 7. Validación y compilación final
- [x] 7.1 Verificar consistencia terminológica del manuscrito
  - Definir un glosario de términos clave y verificar uso consistente en todas las secciones
  - Revisar que todas las citas en el texto tienen su correspondiente entrada en references.bib
  - Verificar que todas las figuras y tablas están referenciadas en el texto con numeración consecutiva
  - Verificar que el abstract no excede 250 palabras
  - _Requirements: 7.2, 7.4, 5.4_

- [x] 7.2 Compilar y validar el manuscrito completo
  - Ejecutar `quarto render` para generar outputs HTML, PDF y DOCX
  - Verificar que la compilación no produce errores ni warnings
  - Revisar el output visual para detectar problemas de formato
  - Ejecutar `/paper:validate` para verificar todas las validaciones hard del proyecto
  - Confirmar que las figuras se renderizan correctamente a 300 DPI
  - _Requirements: 7.1, 7.5, 7.6, 7.7, 5.5_
