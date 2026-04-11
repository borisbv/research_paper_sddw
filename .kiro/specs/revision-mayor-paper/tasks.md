# Implementation Plan

- [x] 1. Verificación y completitud de referencias bibliográficas
- [x] 1.1 (P) Verificar referencias marcadas como pendientes
  - Buscar `bell2015` en CrossRef por título "Limited but Enduring Transnational Ties"; completar DOI si existe
  - Buscar `torres2018` en CrossRef/Dialnet; si no se encuentra, identificar fuente alternativa sobre uso de redes sociales en América Latina (ej: Hootsuite Digital Report, We Are Social, o estudio académico equivalente)
  - Verificar `zhao2023` en CrossRef/Palgrave Macmillan; confirmar DOI y editorial
  - Buscar `eito2011` en Dialnet por título "Migración y comunicación"; completar volumen y páginas
  - Actualizar campo `note` de cada entrada verificada de "pendiente de verificación" a "verificado: [fuente]"
  - _Requirements: 6.1, 6.2, 6.3_

- [x] 1.2 (P) Completar DOIs faltantes y eliminar entradas huérfanas
  - Buscar DOI para `bourdieu1986`, `putnam2000`, `silverstone1996` (si existen como DOI de capítulo/libro)
  - Verificar que toda entrada en .bib esté citada en al menos un archivo de `paper/`
  - Verificar que toda cita en los archivos de `paper/` tenga entrada correspondiente en .bib
  - Si se detectan entradas huérfanas, eliminarlas del .bib
  - Si se detectan citas sin entrada, agregar la entrada faltante
  - _Requirements: 6.2, 6.4, 6.5_

- [x] 2. Expansión metodológica con estándares PRISMA 2020
- [x] 2.1 (P) Agregar subsecciones metodológicas faltantes
  - Agregar subsección "Registro y protocolo" declarando que no se pre-registró en PROSPERO y justificando (naturaleza exploratoria, ciencias sociales)
  - Expandir "Protocolo de búsqueda" con cadenas exactas por base de datos y fechas de ejecución
  - Expandir "Proceso de selección" declarando número de revisores y método de resolución de discrepancias
  - Agregar subsección "Evaluación de calidad" justificando la ausencia de evaluación formal de riesgo de sesgo (corpus heterogéneo en métodos y disciplinas)
  - Agregar subsección "Método de síntesis" declarando el enfoque de análisis temático y describiendo el proceso de codificación
  - Agregar referencia a material suplementario (lista completa de artículos del corpus)
  - _Requirements: 2.2, 2.3, 2.4, 2.5, 2.6, 2.7_

- [x] 2.2 (P) Crear diagrama de flujo PRISMA 2020
  - Generar diagrama en `figures/prisma_flow.md` con formato Mermaid o texto estructurado
  - Incluir las 4 fases: Identificación (847 registros), Filtrado (eliminar 203 duplicados), Elegibilidad (312 evaluados → 154 excluidos con razones), Inclusión (163 + 5 bola de nieve)
  - Incluir razones de exclusión categorizadas (migración tangencial, sin perspectiva comunicativa, etc.)
  - Referenciar el diagrama desde la sección metodológica como "Figura 1"
  - _Requirements: 2.1_

- [x] 3. Búsqueda de fuentes académicas para reemplazar evidencia no académica
- [x] 3.1 Buscar estudios académicos que reemplacen la referencia NPR
  - Buscar estudios peer-reviewed sobre uso de Facebook por migrantes para información de rutas migratorias (candidatos: Alencar 2018, Gillespie et al. 2016, Leurs 2017, Smets 2018)
  - Buscar estudios sobre documentación de trayectos migratorios en YouTube (candidatos: Leurs y Smets, Diminescu)
  - Verificar cada fuente encontrada en CrossRef y obtener DOI
  - Agregar las nuevas entradas al .bib con todos los campos completos
  - Documentar qué claims específicas del paper cubrirá cada nueva fuente
  - _Requirements: 3.1, 3.3_

- [x] 3.2 Resolver la fuente de los testimonios de Cecilia y José
  - Consultar a los autores sobre el origen de "Publicación sobre migrantes colombianos en Chile, s.f."
  - Si es estudio propio no publicado: reformular la cita como "(Autores, en preparación)" con nota al pie explicativa
  - Si es de otro autor: obtener referencia completa y agregarla al .bib
  - Si no se puede identificar: buscar estudios cualitativos sobre migrantes colombianos en Chile con testimonios equivalentes y reemplazar
  - Eliminar toda referencia del tipo "Publicación sobre X, s.f." del texto
  - _Requirements: 3.2, 3.4, 3.5_

- [x] 4. Revisión de la sección de resultados y discusión
- [x] 4.1 Agregar subsección de análisis bibliométrico del corpus
  - Crear nueva subsección al inicio de resultados titulada "Características del corpus" o "Perfil bibliométrico del corpus"
  - Incluir Tabla 1: distribución por año de publicación (2021-2026)
  - Incluir Tabla 2: distribución por plataforma estudiada (WhatsApp, Facebook, YouTube, Instagram, TikTok, múltiples)
  - Incluir Tabla 3: distribución por región geográfica/contexto migratorio (Europa, Norteamérica, América Latina, Asia, África, múltiples)
  - Incluir Tabla 4: distribución por metodología (cualitativa, cuantitativa, mixta, revisión teórica)
  - Indicar en cada subsección de resultados cuántos estudios del corpus contribuyen a esa categoría
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_

- [x] 4.2 Reemplazar fuentes no académicas en el texto de resultados
  - Sustituir "García, en NPR, 2021" como evidencia principal por las fuentes académicas identificadas en tarea 3.1; mantener NPR solo como ilustración complementaria entre paréntesis
  - Resolver los testimonios de Cecilia y José según la decisión tomada en tarea 3.2
  - Verificar que no queden citas del tipo "Publicación sobre X, s.f." en ninguna parte de la sección
  - Asegurar que toda claim central tenga al menos una fuente académica peer-reviewed como respaldo principal
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 4.3 Ajustar lenguaje epistemológico en resultados
  - Reemplazar formulaciones absolutas ("demuestra", "confirma", "prueba") por cautelosas ("sugiere", "es consistente con", "la evidencia indica")
  - Agregar indicadores de fuerza de evidencia cuando se presentan hallazgos (ej: "múltiples estudios coinciden en...", "evidencia incipiente sugiere...", "un único estudio reporta...")
  - Cuando una claim se basa en evidencia de un solo contexto geográfico, señalarlo explícitamente
  - Distinguir entre evidencia directa sobre Chile y evidencia extrapolada de otros contextos
  - _Requirements: 5.3, 5.4, 5.5_

- [x] 5. Reformulación de la introducción
- [x] 5.1 Reformular hipótesis como pregunta de investigación
  - Reemplazar "La hipótesis central de este trabajo sostiene que..." por una formulación tipo "Este trabajo explora la proposición de que..." o "La pregunta que guía este trabajo es..."
  - Eliminar el carácter confirmatorio del enunciado; presentar como proposición teórica a explorar mediante la revisión
  - Mantener el contenido sustantivo de la proposición (resignificación, transformación de herramientas genéricas en canales de capital)
  - _Requirements: 5.1, 5.2_

- [x] 5.2 Reformular objetivos y alcance declarado
  - Reformular los tres objetivos para distinguir entre síntesis general (evidencia internacional) y foco específico (implicaciones para Chile)
  - Agregar caveat explícito: la revisión sintetiza evidencia internacional con énfasis interpretativo en el corredor Venezuela-Colombia-Chile
  - El tercer objetivo debe reconocer que la comparación es entre usos genéricos documentados y usos migrantes documentados en la literatura, no necesariamente en Chile
  - No exceder la extensión actual en más de 200 palabras
  - _Requirements: 1.3, 5.2_

- [x] 6. Reformulación de las conclusiones
- [x] 6.1 Eliminar lenguaje confirmatorio y reconocer brechas
  - Reemplazar "La evidencia confirma que" por "La evidencia revisada es consistente con la proposición de que"
  - Reformular la presentación de la tipología: no es "confirmada" sino "derivada de la síntesis" o "emergente del análisis"
  - Agregar párrafo breve reconociendo que la evidencia directa sobre el contexto chileno es limitada y que la tipología requiere validación empírica
  - Señalar explícitamente cuándo se extrapola de otros contextos al formular implicaciones para Chile
  - Distinguir entre hallazgos con respaldo fuerte (múltiples estudios) y hallazgos incipientes
  - _Requirements: 1.4, 1.5, 5.1, 5.4_

- [x] 7. Reformulación del abstract
- [x] 7.1 Ajustar alcance y tono del resumen bilingüe
  - En español: reemplazar "analiza cómo" → "explora cómo"; "confirman que" → "sugieren que"
  - Agregar matiz de alcance: "sintetiza evidencia internacional con foco en las implicaciones para migrantes venezolanos y colombianos en Chile"
  - Aplicar los mismos cambios al abstract en inglés manteniendo equivalencia semántica
  - Verificar que cada versión no exceda 150 palabras
  - Asegurar que el abstract refleje fielmente el contenido actualizado de introducción y conclusiones
  - _Requirements: 1.1, 1.2_

- [x] 8. Validación cruzada y verificación final
- [x] 8.1 Verificar coherencia entre secciones modificadas
  - Confirmar que el alcance declarado en abstract, introducción y conclusiones es consistente
  - Verificar que el lenguaje epistemológico es uniformemente cauteloso en todas las secciones
  - Confirmar que las tablas bibliométricas de resultados son referenciadas en metodología y conclusiones
  - Verificar que el diagrama PRISMA es consistente con los números reportados en el texto
  - Ejecutar validación de citas: toda referencia en texto tiene entrada en .bib y viceversa
  - _Requirements: 1.1, 1.4, 2.1, 5.1, 6.5_

- [x] 8.2 Verificar cumplimiento de límites de formato REIS
  - Conteo total de palabras < 8,000 (incluidas notas y referencias)
  - Resumen en español ≤ 150 palabras
  - Abstract en inglés ≤ 150 palabras
  - Formato de citas Harvard (autor-año) consistente
  - Todas las figuras y tablas referenciadas en el texto
  - _Requirements: 2.1, 4.1, 4.2, 4.3, 4.4, 4.5_
