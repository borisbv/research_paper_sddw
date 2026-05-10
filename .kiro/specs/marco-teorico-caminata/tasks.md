# Implementation Plan

- [x] 1. Búsqueda bibliográfica y construcción del corpus de referencias
- [x] 1.1 (P) Buscar referencias sobre conceptualización, beneficios y regulación emocional de la caminata
  - Buscar en PubMed, Scopus y Web of Science: "walking AND emotional regulation", "walking AND physical activity AND well-being", "rhythmic movement AND stress reduction", "embodied cognition AND walking"
  - Buscar en SciELO y Redalyc: "caminata AND regulación emocional", "actividad física AND bienestar AND Latinoamérica"
  - Seleccionar 6-8 referencias candidatas para los bloques B1, B2 y B3
  - Priorizar publicaciones 2020-2026; admitir obras seminales solo con justificación explícita
  - _Requirements: 8.1, 8.2, 8.3_

- [x] 1.2 (P) Buscar referencias sobre caminata en contexto familiar, perspectiva adolescente y CEA
  - Buscar en PubMed, Scopus y Web of Science: "walking AND adolescents AND self-regulation", "family walking AND bonding", "walking AND autism spectrum", "physical activity AND autism AND adolescents"
  - Buscar en SciELO y Redalyc: "caminata AND adolescentes AND Chile", "actividad física AND autismo AND Latinoamérica", "prácticas corporales AND familias"
  - Seleccionar 6-10 referencias candidatas para los bloques B4, B5, B6 y B7
  - Identificar al menos 2-3 fuentes regionales (chilenas o latinoamericanas)
  - _Requirements: 8.1, 8.2, 8.3, 9.1, 9.3_

- [x] 1.3 Validar todas las referencias por DOI/CrossRef y generar entradas BibTeX
  - Verificar cada referencia candidata de 1.1 y 1.2 contra CrossRef o resolver su DOI
  - Excluir referencias que no puedan verificarse por DOI o CrossRef
  - Generar entradas BibTeX con campos obligatorios completos (author, title, year, journal, doi)
  - Usar citekeys en formato `apellido_año` (e.g., `oppezzo2014`, `gross2015`)
  - Agregar las entradas validadas a `references/references.bib`, preservando entradas existentes
  - Verificar que el corpus final contenga entre 12 y 18 referencias distribuidas entre los 7 bloques
  - _Requirements: 8.1, 8.4, 8.5, 8.6_

- [x] 2. Crear archivo QMD base con frontmatter y estructura inicial
  - Crear `paper/marco-teorico-caminata.qmd` con frontmatter YAML (title, bibliography, csl)
  - Configurar la ruta al archivo de referencias (`../references/references.bib`)
  - Verificar que el archivo CSL para APA 7th edition esté disponible o documentar la necesidad
  - Dejar el cuerpo del archivo preparado para recibir la prosa continua de los 7 bloques
  - _Requirements: 2.1, 10.1_

- [x] 3. Redactar bloques 1 a 3: conceptualización, beneficios y regulación emocional
- [x] 3.1 Redactar bloque 1: conceptualización de la caminata como actividad física, práctica social y experiencia situada
  - Definir la caminata integrando sus tres dimensiones de manera afirmativa
  - Contrastar hallazgos internacionales con evidencia regional cuando exista
  - Integrar 2-3 citas en formato APA usando sintaxis Quarto (`@citekey` y `[@citekey]`)
  - Extensión aproximada: ~200 palabras en un párrafo extenso de 8-15 líneas
  - Iniciar con un conector académico apropiado que sitúe el tema
  - _Requirements: 1.1, 1.3, 3.1, 3.2, 3.3, 9.1, 9.2, 10.1, 10.4_

- [x] 3.2 Redactar bloque 2: beneficios documentados a nivel físico, psicológico y emocional
  - Documentar beneficios de la caminata en población general con evidencia empírica
  - Articular la conexión con el bloque anterior mediante un conector académico
  - Integrar 2-3 citas APA, respaldando cada afirmación principal
  - Extensión aproximada: ~250 palabras, párrafo extenso sin guiones ni viñetas
  - _Requirements: 1.2, 1.3, 4.1, 4.4, 9.1, 10.1, 10.4_

- [x] 3.3 Redactar bloque 3: caminata como recurso de regulación emocional
  - Vincular la marcha rítmica con procesos atencionales, sensoriales y de reducción del estrés
  - Integrar conceptos de *embodied cognition* o cognición corporizada
  - Articular la transición desde los beneficios generales hacia la regulación emocional específica
  - Integrar 3-4 citas APA, combinando formato narrativo y parentético
  - Extensión aproximada: ~280 palabras, párrafo extenso fluido
  - _Requirements: 1.2, 1.3, 4.2, 4.3, 4.4, 9.1, 10.1, 10.3, 10.4_

- [x] 4. Redactar bloques 4 y 5: contexto familiar y perspectiva adolescente
- [x] 4.1 Redactar bloque 4: caminata en contexto familiar como práctica vincular
  - Abordar la caminata como práctica vincular entre cuidadores e hijos
  - Poner énfasis en la adolescencia como etapa del desarrollo
  - Contrastar hallazgos internacionales con estudios latinoamericanos o chilenos cuando existan
  - Integrar 2-3 citas APA y mantener la lógica acumulativa con los bloques previos
  - Extensión aproximada: ~220 palabras, párrafo extenso con conector de apertura
  - _Requirements: 1.2, 1.3, 5.1, 5.3, 9.1, 9.2, 10.1, 10.4_

- [x] 4.2 Redactar bloque 5: perspectiva adolescente sobre la caminata
  - Recoger estudios sobre apropiación, motivación y significados que los adolescentes atribuyen a la caminata
  - Mantener la progresión lógica desde el contexto familiar hacia la voz adolescente
  - Integrar contraste geográfico; si no hay evidencia regional, señalar la ausencia como vacío
  - Integrar 2-3 citas APA
  - Extensión aproximada: ~220 palabras, párrafo extenso sin disrupciones
  - _Requirements: 1.2, 1.3, 5.2, 5.3, 9.1, 9.2, 9.3, 10.1, 10.4_

- [x] 5. Redactar bloques 6 y 7: caminata y CEA, vacíos y justificación
- [x] 5.1 Redactar bloque 6: articulación de la caminata con la Condición del Espectro Autista
  - Articular los bloques previos con evidencia sobre adolescentes en el espectro autista y sus necesidades de autorregulación
  - Adoptar la perspectiva autista: describir el autismo como variación natural del neurodesarrollo
  - Mantener coherencia con el glosario del proyecto (CEA, personas en el espectro, adolescentes autistas)
  - Evitar terminología patologizante (trastorno, déficit, padecen)
  - Integrar 3-4 citas APA con contraste geográfico cuando exista
  - Extensión aproximada: ~280 palabras, párrafo extenso con lógica acumulativa
  - _Requirements: 1.2, 1.3, 6.1, 6.2, 6.3, 9.1, 9.2, 10.1, 10.3, 10.4_

- [x] 5.2 Redactar bloque 7: vacíos en la literatura y justificación del estudio HabiTAR
  - Identificar al menos un vacío empírico (ausencia de estudios en la población o contexto específico)
  - Identificar al menos un vacío conceptual (articulaciones teóricas pendientes entre caminata, regulación emocional y CEA)
  - Anclar ambos vacíos en la justificación del estudio HabiTAR
  - Formular la transición hacia la pregunta de investigación
  - Integrar 1-2 citas APA de respaldo
  - Extensión aproximada: ~200 palabras, párrafo de cierre que habilite la pregunta de investigación
  - _Requirements: 1.2, 1.4, 7.1, 7.2, 7.3, 7.4, 9.3, 10.1, 10.4_

- [x] 6. Validación integral del marco teórico
- [x] 6.1 Validar extensión, estructura y formato
  - Verificar que el conteo total de palabras esté entre 1.500 y 1.800
  - Verificar que cada párrafo tenga entre 8 y 15 líneas
  - Confirmar la ausencia de guiones, viñetas o listas dentro de los párrafos
  - Verificar que los párrafos inicien con conectores académicos variados
  - Confirmar que la puntuación se limite a comas y puntos seguidos
  - Verificar la presencia de los 7 bloques temáticos en secuencia lógica acumulativa
  - _Requirements: 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 6.2 Validar referencias y citaciones
  - Verificar que cada `@citekey` en el `.qmd` tenga su entrada correspondiente en `references.bib`
  - Contar las referencias únicas citadas y confirmar que estén en el rango 12-18
  - Verificar que las citas usen formato APA (narrativo y parentético) correctamente
  - Confirmar que cada entrada BibTeX tenga campos obligatorios completos
  - _Requirements: 8.1, 8.4, 8.5_

- [x] 6.3 Validar tono, estilo y perspectiva
  - Verificar ausencia de expresiones artificiales o marcadores de generación automática
  - Confirmar uso correcto de negrita (solo conceptos clave) y cursiva (solo tecnicismos)
  - Verificar perspectiva autista consistente: sin "trastorno", "déficit", formulaciones por negación
  - Confirmar que no hay citas verbatim, corchetes aclaratorios, [sic] ni identificación de perfiles
  - Verificar que las aclaraciones técnicas que rompen el flujo estén en notas al pie
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6_

- [x] 6.4 (P) Validar eje geográfico transversal
  - Revisar cada bloque para confirmar que el contraste geográfico esté integrado dentro de cada subsección
  - Verificar que cuando existe evidencia regional se contraste con hallazgos internacionales en el mismo bloque
  - Confirmar que la ausencia de evidencia regional se señale explícitamente como vacío
  - _Requirements: 9.1, 9.2, 9.3_
