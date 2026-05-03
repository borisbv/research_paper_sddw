# Requirements Document

## Introduction
Este documento define los requisitos para el enriquecimiento del marco teórico del paper HabiTAR, que aborda el impacto de las tecnologías digitales en la autorregulación emocional y la inclusión académica de estudiantes universitarios con TEA. El trabajo se realiza sobre un documento nuevo en `paper/`, preservando intacto el original en `temp_context/`. Las mejoras se insertan entre corchetes `[ ]` para distinguirlas del texto original, e incluyen: densificación de citas con al menos 5 autores Scopus (2020–2026) por concepto, corrección de inconsistencias señaladas por el mentor, completación de secciones placeholder y mantenimiento del tono académico de prosa continua.

**Sujeto EARS**: "el Documento" (el nuevo archivo en `paper/` que contiene el marco teórico enriquecido).

## Requirements

### Requirement 1: Creación del documento y preservación del original
**Objective:** Como investigador, quiero que el enriquecimiento se realice en un documento nuevo separado del original, para que el texto fuente permanezca intacto como referencia.

#### Acceptance Criteria
1. The el Documento shall ser creado en `paper/` como archivo Markdown independiente replicando íntegramente el contenido de `temp_context/Marco teórico - Tea Tecnologia + CF.docx.md`.
2. When se complete el enriquecimiento, the el Documento shall contener todo el texto original sin alteraciones, con las mejoras insertadas exclusivamente entre corchetes `[ ]`.
3. The el Documento shall no modificar, renombrar ni eliminar ningún archivo dentro de `temp_context/`.
4. When se inserte texto nuevo entre corchetes, the el Documento shall distinguir visualmente las adiciones del texto original mediante el formato `[texto nuevo]`.

### Requirement 2: Densificación bibliográfica (mínimo 5 autores por concepto)
**Objective:** Como investigador, quiero que cada afirmación teórica y concepto clave esté respaldado por al menos 5 referencias de autores distintos, para que el marco teórico sea robusto y pase revisión por pares.

#### Acceptance Criteria
1. When una afirmación teórica o definición conceptual tenga menos de 5 citas, the el Documento shall insertar entre corchetes referencias adicionales hasta alcanzar al menos 5 autores distintos.
2. The el Documento shall utilizar exclusivamente referencias de revistas indexadas en Scopus publicadas entre 2020 y 2026.
3. The el Documento shall citar en formato APA 7ª edición (Autor, Año) dentro del texto.
4. When se agreguen nuevas referencias en el texto, the el Documento shall incluir la entrada bibliográfica completa en la sección "Referencias bibliográficas" al final del documento.
5. If una afirmación usa plural ("los estudios", "las revisiones", "los trabajos"), the el Documento shall respaldarla con al menos tantas citas como implique el plural (mínimo 2, idealmente 5+).

### Requirement 3: Corrección de inconsistencias señaladas por el mentor
**Objective:** Como investigador, quiero que se corrijan las inconsistencias identificadas en la sesión de mentoría, para que el texto sea coherente y no debilite la argumentación.

#### Acceptance Criteria
1. When el texto original use plural ("trabajos regionales", "las revisiones") y cite solo un autor, the el Documento shall insertar entre corchetes citas adicionales que respalden la pluralidad o ajustar la redacción al singular.
2. When una frase fuerte o afirmación categórica carezca de respaldo bibliográfico, the el Documento shall insertar entre corchetes la(s) cita(s) correspondiente(s) de autores Scopus 2020–2026.
3. When exista un quiebre temático abrupto entre párrafos (e.g., salto de "trayectorias educativas" a "modelos pedagógicos" sin vínculo), the el Documento shall insertar entre corchetes una oración de transición que articule la conexión lógica.
4. When el texto mencione "países de ingresos bajos y medios" en referencia a vacíos de investigación, the el Documento shall insertar entre corchetes una reformulación que hable de regiones (e.g., "Latinoamérica") en lugar de niveles de ingreso, para mantener consistencia con el caso chileno.
5. If el texto contiene frases que parecen opinión del autor sin apoyo en literatura, the el Documento shall insertar entre corchetes al menos 3 citas que respalden la afirmación.

### Requirement 4: Completación de secciones placeholder
**Objective:** Como investigador, quiero que las secciones incompletas del marco teórico sean desarrolladas con contenido académico riguroso, para que el documento esté completo y listo para revisión.

#### Acceptance Criteria
1. When la sección "Modelos educativos en Chile" contenga solo un placeholder, the el Documento shall insertar entre corchetes contenido de aproximadamente media página (250–350 palabras) que describa la evolución de los modelos educativos chilenos relevantes para TEA, con al menos 5 referencias Scopus 2020–2026.
2. When la sección "Uso de apps para personas/niños/adolescentes TEA" contenga solo placeholders, the el Documento shall insertar entre corchetes contenido de aproximadamente una página (500–700 palabras) que cubra: (a) apps orientadas a personas TEA en general, (b) apps específicas para adolescentes TEA, con al menos 5 referencias Scopus 2020–2026 por subsección.
3. The el Documento shall mantener en las secciones completadas la misma densidad narrativa y nivel de profundidad que las secciones ya desarrolladas (e.g., "Adolescentes TEA").
4. When se complete una sección placeholder, the el Documento shall integrar transiciones coherentes con los párrafos anterior y posterior.

### Requirement 5: Tono académico y estilo de prosa continua
**Objective:** Como investigador, quiero que todo el texto nuevo siga el estilo académico definido en el README, para que el documento sea estilísticamente uniforme.

#### Acceptance Criteria
1. The el Documento shall usar prosa continua sin guiones (-) ni viñetas dentro de los párrafos; la puntuación se limita a comas, puntos seguidos y puntos aparte.
2. The el Documento shall emplear conectores lógicos académicos para iniciar párrafos o ideas nuevas (e.g., "En este contexto...", "Asimismo...", "Siguiendo esta tendencia...").
3. The el Documento shall escribir en negrita los conceptos clave o categorías emergentes dentro de los párrafos.
4. The el Documento shall escribir en cursiva los términos técnicos en inglés o conceptos metodológicos específicos (e.g., *User Experience*, *pull-out*, *biofeedback*).
5. The el Documento shall mantener un tono formal y científico con equilibrio humanista-técnico, evitando lenguaje coloquial o absolutista.
6. If se incluyen aclaraciones técnicas o legales que podrían romper el flujo, the el Documento shall desplazarlas a notas al pie.

### Requirement 6: Estructura y formato del documento
**Objective:** Como investigador, quiero que el documento mantenga la estructura IMRaD y las convenciones del proyecto, para que sea compatible con el pipeline de validación.

#### Acceptance Criteria
1. The el Documento shall respetar la estructura de secciones del original: Planteamiento del problema → Marco teórico (Adolescentes TEA → Modelos educativos en Chile → Uso de apps para TEA) → Referencias bibliográficas.
2. The el Documento shall estar en formato Markdown compatible con Quarto (`.md`).
3. When se agreguen referencias nuevas, the el Documento shall mantener el orden alfabético en la sección de referencias bibliográficas.
4. The el Documento shall incluir DOI con enlace activo para cada referencia nueva agregada, siguiendo el formato del documento original.

