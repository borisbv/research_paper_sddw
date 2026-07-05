# Implementation Plan

## Tasks

- [x] 1. Diagnóstico del borrador y preparación de estructura
- [x] 1.1 Analizar el manuscrito base e identificar contenido conservable, reorganizable y eliminable
  - Leer el borrador completo y clasificar cada sección según su valor científico
  - Mapear qué información del borrador alimenta cada sección del nuevo manuscrito
  - Identificar vacíos conceptuales, metodológicos, bibliográficos y argumentativos
  - Listar contenido a eliminar (presupuestos, montos, información identificable)
  - _Requirements: 1.4, 10.4_

- [x] 1.2 Crear la estructura de archivos del manuscrito en `paper/`
  - Crear los archivos markdown para cada sección: 00-abstract, 01-introduction, 02-state-of-the-art, 03-methodology, 04-results, 05-discussion, 06-conclusions
  - Configurar `_quarto.yml` para el libro con las secciones en orden IMRaD
  - Establecer el archivo `references/references.bib` con las entradas existentes del borrador (sin duplicados)
  - Crear directorio `figures/` con archivo de especificaciones de las 5 figuras
  - _Requirements: 1.1, 1.2, 1.6_

- [x] 2. Búsqueda y construcción del estado del arte
- [x] 2.1 Buscar literatura reciente (2021-2026) para los 10 dominios temáticos
  - Buscar en bases de datos académicas (Semantic Scholar, Google Scholar, CrossRef) referencias sobre: Virtual Museums, Digital Heritage, Museum Studies, UX, Human-Centred Design, XR, Accessibility, Inclusive Design, Metadata Standards, Community Participation
  - Seleccionar mínimo 3 fuentes recientes verificables por dominio temático
  - Verificar DOI de cada referencia encontrada
  - Registrar entradas BibTeX en `references/references.bib` con formato APA 7
  - _Requirements: 3.1, 3.2, 9.1, 9.3, 9.4_

- [x] 2.2 (P) Integrar los 12 casos de estudio comparativos como evidencia del estado del arte
  - Sintetizar hallazgos de los casos de estudio (Smithsonian, British Museum, Van Gogh, etc.) en patrones analíticos
  - Identificar tendencias, fortalezas y limitaciones transversales de los modelos existentes
  - Conectar los hallazgos comparativos con la brecha de investigación
  - _Requirements: 3.5, 5.5_

- [x] 2.3 Redactar el estado del arte como diálogo crítico internacional (700-900 palabras)
  - Escribir cada subsección temática mostrando evolución del conocimiento (no listas de autores)
  - Integrar comparación entre autores, acuerdos y diferencias
  - Conducir la argumentación hacia la brecha como oportunidad integradora
  - Asegurar que cada afirmación conceptual termine con mínimo 3 citas APA 7 recientes
  - Incorporar los patrones de los casos de estudio como evidencia empírica
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6_

- [x] 3. Redacción de la introducción científica
- [x] 3.1 Escribir la introducción con contexto, brecha, preguntas y objetivos (400-500 palabras)
  - Abrir con contexto internacional sobre museos virtuales y patrimonio digital
  - Articular el problema científico derivado de la literatura del estado del arte
  - Construir la brecha como oportunidad integradora (sin afirmaciones negativas categóricas)
  - Formular preguntas de investigación específicas y verificables
  - Declarar objetivo general y objetivos específicos alineados con las preguntas
  - Explicitar la contribución: marco conceptual y metodológico transferible
  - Incluir referencia a Figura 1 (Research Context and Knowledge Gap)
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6_

- [x] 4. Redacción de la metodología
- [x] 4.1 Escribir la sección de metodología reproducible (500-600 palabras)
  - Justificar el enfoque mixed-methods con fundamentación epistemológica
  - Detallar las 6 etapas con participantes, instrumentos y procedimientos específicos
  - Indicar claramente qué etapas han sido completadas (1-3) y cuáles están en progreso (4-6)
  - Describir criterios de análisis cualitativo y cuantitativo
  - Presentar el equipo interdisciplinario con perfiles y aportes metodológicos (sin montos)
  - Incluir referencias a Figura 2 (Research Design Framework) y Figura 3 (Interdisciplinary Research Ecosystem)
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_

- [x] 5. Redacción de resultados preliminares
- [x] 5.1 Escribir resultados de las etapas completadas (400-500 palabras)
  - Presentar hallazgos del needs assessment (Etapa 1): prioridades, restricciones, experiencias deseadas
  - Presentar hallazgos del análisis comparativo (Etapa 2): patrones de navegación, inmersión, accesibilidad entre los 12 museos
  - Presentar resultados del diseño del framework técnico (Etapa 3): arquitectura, metadatos, accesibilidad
  - Indicar explícitamente que son resultados preliminares e interpretarlos
  - Vincular cada hallazgo con la pregunta de investigación correspondiente
  - No incluir "Expected Outcomes" como resultados finales
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [x] 6. Redacción de discusión y modelo conceptual
- [x] 6.1 Escribir la discusión con el modelo HCVMF (400-500 palabras)
  - Interpretar los hallazgos preliminares en relación con la literatura del estado del arte
  - Presentar y explicar el "Human-Centred Virtual Museum Framework" como contribución principal
  - Describir los componentes del modelo y sus relaciones
  - Discutir limitaciones del estudio de forma constructiva
  - Proponer implicaciones para futuras investigaciones y proyectos
  - Incluir referencia a Figura 4 (Human-Centred Virtual Museum Framework)
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [x] 7. Redacción de conclusiones y abstract
- [x] 7.1 (P) Escribir las conclusiones (200-300 palabras)
  - Responder directamente a las preguntas de investigación planteadas
  - Resumir la contribución científica (marco transferible)
  - Proyectar aplicaciones futuras del modelo
  - Incluir referencia a Figura 5 (Knowledge Transfer Framework)
  - No introducir información nueva que no esté soportada en las secciones anteriores
  - _Requirements: 10.2, 6.4_

- [x] 7.2 (P) Escribir el abstract (máximo 250 palabras)
  - Sintetizar problema, método, hallazgos preliminares y contribución
  - Asegurar coherencia con el contenido final de todas las secciones
  - Definir entre 3 y 5 keywords relevantes
  - _Requirements: 1.5, 1.6_

- [x] 8. Especificación de figuras científicas
- [x] 8.1 (P) Desarrollar las especificaciones conceptuales de las 5 figuras
  - Escribir para cada figura: título, objetivo científico, descripción detallada del contenido, elementos visuales y ubicación en el texto
  - Figura 1: Research Context and Knowledge Gap — ecosistema de conocimiento y oportunidad integradora
  - Figura 2: Research Design Framework — 6 etapas, conexiones y flujo iterativo
  - Figura 3: Interdisciplinary Research Ecosystem — perfiles y aportes del equipo
  - Figura 4: Human-Centred Virtual Museum Framework — modelo conceptual transferible
  - Figura 5: Knowledge Transfer Framework — transferibilidad a otros contextos
  - Asegurar que cada figura sintetiza conocimiento (no ilustra decorativamente)
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_

- [x] 9. Revisión de calidad y coherencia
- [x] 9.1 Revisar calidad del inglés académico y estilo en todo el manuscrito
  - Verificar que no hay traducciones literales del español
  - Asegurar voz analítica, concreta y precisa (un párrafo = una idea)
  - Eliminar afirmaciones absolutas y reemplazar por expresiones moderadas
  - Verificar que la tecnología se presenta como medio (personas y patrimonio como centro)
  - Integrar transversalmente accesibilidad, diseño inclusivo, diversidad cultural y perspectiva de género
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6_

- [x] 9.2 Verificar coherencia argumentativa entre todas las secciones
  - Confirmar progresión: Contexto → Estado del arte → Brecha → Pregunta → Objetivo → Metodología → Hallazgos → Discusión → Contribución → Conclusiones
  - Verificar que título, abstract, keywords, problema, preguntas, objetivos, metodología, resultados, discusión y conclusiones son coherentes entre sí
  - Confirmar que ninguna sección responde a una pregunta diferente del objetivo principal
  - Verificar que no hay contenido de presupuestos ni montos económicos
  - _Requirements: 10.1, 10.2, 10.3, 10.4_

- [x] 10. Validación final
- [x] 10.1 Verificar bibliografía y formato APA 7
  - Confirmar que todas las citas en texto tienen entrada en references.bib
  - Verificar que no hay duplicados bibliográficos
  - Confirmar que los DOI son verificables (CrossRef)
  - Asegurar que no hay autores ni referencias inventadas
  - Confirmar balance temporal (mínimo 40% literatura 2021-2026)
  - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5_

- [x] 10.2 Verificar formato SIGraDi y anonimato
  - Contar palabras por sección y total (2500-3500 excluyendo referencias)
  - Verificar que el abstract no excede 250 palabras
  - Confirmar estructura IMRaD en orden correcto
  - Buscar y eliminar cualquier nombre institucional, personal o ubicación identificable
  - Verificar que las figuras están referenciadas en el texto
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 10.3 Ejecutar revisión simulada de tres revisores internacionales
  - Revisar como Reviewer 1: evaluar solidez metodológica y rigor científico
  - Revisar como Reviewer 2: evaluar contribución, novedad y originalidad
  - Revisar como Reviewer 3: evaluar claridad, estilo y calidad del inglés
  - Identificar debilidades y fortalecer las secciones que lo requieran
  - _Requirements: 10.5_
