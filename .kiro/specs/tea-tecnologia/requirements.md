# Requirements Document

## Project Description (Input)
Paper científico incremental 'tea-tecnologia'. Primera etapa: construir únicamente el marco teórico (2 páginas) sobre Trastorno del Espectro Autista (TEA) y el potencial de las tecnologías/apps para apoyar a adolescentes TEA. Estructura de lo general a lo específico: qué es TEA, niños TEA, TEA a nivel mundial, TEA en Latinoamérica, TEA en Chile (niños), modelos pedagógicos que han excluido a los TEA, adolescentes TEA y estudiantes universitarios TEA, breve mención de cómo las apps/tecnologías pueden ayudar con ejemplos de tres tecnologías con resultados. Cierre identificando vacíos en la literatura y explicando que la propuesta busca evaluar si las tecnologías tipo app podrían ayudar a los adolescentes TEA. Requisitos: citas APA de revistas Scopus recientes, referencias bibliográficas, sin usar guiones (-) entre párrafos, párrafos largos y orgánicos. Instrucciones detalladas en temp_context/instrucciones.md. Spec incremental: esta fase cubre solo el marco teórico; secciones posteriores del paper se irán agregando en fases futuras.

## Introduction
Este spec cubre la primera fase de un paper científico incremental sobre el Trastorno del Espectro Autista (TEA) y el uso potencial de tecnologías tipo app para apoyar a adolescentes TEA. En esta etapa se construirá únicamente el marco teórico, de aproximadamente dos páginas, redactado en español, siguiendo normas APA y sustentado exclusivamente en literatura científica reciente indexada en Scopus. El marco teórico debe desplegar un recorrido argumental de lo general a lo específico, identificar explícitamente los vacíos de la literatura y cerrar articulando la pregunta que guiará las fases siguientes del paper. Las secciones posteriores (introducción extendida, metodología, resultados, discusión, conclusiones) se abordarán en fases incrementales futuras y están fuera del alcance de este spec.

## Requirements

### Requirement 1: Alcance incremental del paper
**Objective:** Como investigador que escribe un paper de forma incremental, quiero que esta fase se limite estrictamente al marco teórico, para poder validar la base conceptual antes de avanzar a las siguientes secciones.

#### Acceptance Criteria
1. The paper writing process shall producir únicamente la sección "Marco teórico" durante esta fase del spec.
2. If se solicita redactar introducción, metodología, resultados, discusión o conclusiones en esta fase, the paper writing process shall rechazar la solicitud e indicar que corresponden a fases futuras del spec incremental.
3. The paper writing process shall registrar en un archivo del directorio `paper/` el artefacto del marco teórico como una unidad entregable e independiente.
4. Where existan fases futuras del paper, the paper writing process shall preservar el marco teórico sin reescrituras destructivas para permitir iteración aditiva.

### Requirement 2: Estructura argumental de lo general a lo específico
**Objective:** Como lector académico, quiero que el marco teórico siga un recorrido de lo general a lo específico, para comprender progresivamente el fenómeno TEA y su relación con el contexto chileno y adolescente.

#### Acceptance Criteria
1. The marco teórico shall iniciar con una definición conceptual y clínica de TEA sustentada en literatura reciente.
2. When se introduzca la población infantil, the marco teórico shall caracterizar a los niños TEA y las implicancias del diagnóstico.
3. The marco teórico shall describir la situación del TEA a nivel mundial, incluyendo prevalencia y tendencias globales.
4. When se aborde el contexto regional, the marco teórico shall presentar evidencia sobre TEA en Latinoamérica.
5. The marco teórico shall describir la situación del TEA en niños en Chile.
6. The marco teórico shall identificar los modelos pedagógicos que históricamente han dejado por fuera a estudiantes TEA.
7. When se avance al grupo etario central del estudio, the marco teórico shall abordar a los adolescentes TEA y a los estudiantes universitarios TEA.
8. The marco teórico shall incluir una sección breve sobre cómo las tecnologías tipo app pueden apoyar a adolescentes TEA, citando al menos tres tecnologías concretas con resultados reportados.
9. The marco teórico shall cerrar explicitando los vacíos que el investigador identifica en la literatura y articulando que la propuesta busca evaluar si las tecnologías tipo app podrían ayudar a los adolescentes TEA.

### Requirement 3: Extensión y formato del documento
**Objective:** Como editor del paper, quiero que el marco teórico respete una extensión y formato definidos, para asegurar que encaje en la estructura global del manuscrito.

#### Acceptance Criteria
1. The marco teórico shall tener una extensión objetivo de dos páginas en formato estándar académico.
2. If la extensión redactada excede significativamente dos páginas, the paper writing process shall ajustar el contenido priorizando densidad conceptual sobre enumeración.
3. The marco teórico shall estar redactado íntegramente en español.
4. The marco teórico shall estructurarse en párrafos largos y orgánicos, sin usar guiones (-) como separadores entre ideas o párrafos.
5. If aparecen listas con viñetas o guiones decorativos dentro del cuerpo del marco teórico, the paper writing process shall convertirlas en prosa continua.
6. The marco teórico shall persistirse como archivo markdown dentro del directorio `paper/`.

### Requirement 4: Citación científica con normas APA y fuentes Scopus
**Objective:** Como revisor académico, quiero que toda afirmación no trivial esté respaldada por citas APA verificables provenientes de revistas Scopus recientes, para garantizar la calidad y trazabilidad del marco teórico.

#### Acceptance Criteria
1. The marco teórico shall aplicar normas APA en todas las citas dentro del cuerpo del texto.
2. The marco teórico shall sustentar cada afirmación empírica con al menos una cita científica verificable.
3. The paper writing process shall priorizar fuentes publicadas en revistas indexadas en Scopus y preferentemente de los últimos años.
4. If una afirmación no cuenta con respaldo verificable en Scopus o bases equivalentes, the paper writing process shall marcarla como pendiente de verificación antes de aceptarla en el marco teórico.
5. The paper writing process shall consolidar todas las referencias citadas en una sección final de "Referencias bibliográficas" siguiendo formato APA.
6. The paper writing process shall almacenar las referencias también en `references/references.bib` para permitir validaciones automáticas posteriores.

### Requirement 5: Identificación de vacíos y articulación con la propuesta
**Objective:** Como investigador, quiero que el cierre del marco teórico exponga con claridad los vacíos de la literatura y conecte con la pregunta de investigación, para establecer la base justificativa del paper.

#### Acceptance Criteria
1. The marco teórico shall incluir un cierre explícito que enumere en prosa los vacíos percibidos en la literatura revisada.
2. The marco teórico shall articular, a partir de esos vacíos, que la propuesta del paper busca evaluar si las tecnologías tipo app podrían ayudar a los adolescentes TEA.
3. When se formule el cierre, the marco teórico shall mantener coherencia argumental con las secciones previas sin introducir conceptos no desarrollados.

### Requirement 6: Validación previa al cierre de la fase
**Objective:** Como responsable del proceso SDD, quiero que el marco teórico pase validaciones hard antes de considerarse terminado, para alinear esta fase con la disciplina del framework.

#### Acceptance Criteria
1. Before marcar la fase como completada, the paper writing process shall ejecutar las validaciones hard del framework sobre el archivo del marco teórico.
2. If alguna cita del marco teórico no resuelve contra CrossRef, DOI u otra base verificable, the paper writing process shall bloquear la aceptación hasta corregirla o sustituirla.
3. If el marco teórico contiene guiones (-) usados como separadores de párrafos o ideas, the paper writing process shall reportar la violación de estilo y exigir su corrección.
4. The paper writing process shall reportar el estado de la fase mediante `/paper:status` una vez completadas las validaciones.
