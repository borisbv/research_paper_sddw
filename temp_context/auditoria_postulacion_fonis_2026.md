# Auditoría Crítica — Postulación FONIS 2026

**Proyecto:** Desarrollo y evaluación de una intervención digital accesible para mejorar la comprensión de información en salud en personas mayores  
**Fecha de auditoría:** 2026-04-26  
**Auditor:** Boris Bustos (asistido por IA)

---

## 1. Resumen ejecutivo

La propuesta aborda un problema relevante (comprensión de información en salud en personas mayores) y se alinea con los Objetivos Sanitarios de la Década 2021–2030. Sin embargo, presenta debilidades importantes en la fundamentación metodológica, la justificación del tamaño muestral, la especificidad de la solución tecnológica, la actualización del estado del arte y la redundancia en la redacción. A continuación se detallan las falencias identificadas organizadas por sección.

---

## 2. Estado del arte y planteamiento del problema (Sección 1.1)

### 2.1 Referencias desactualizadas

Las referencias centrales del marco teórico son antiguas:

| Referencia | Año | Antigüedad |
|:-----------|:----:|:----------:|
| Nutbeam | 2008 | 18 años |
| Berkman et al. | 2011 | 15 años |
| Sørensen et al. | 2012 | 14 años |
| WHO | 2017 | 9 años |
| MINSAL Chile | 2020 | 6 años |
| SENAMA | 2022 | 4 años |

**Problema:** Las bases de FONIS esperan un estado del arte actualizado. No se citan trabajos posteriores a 2022, ni se menciona la abundante literatura reciente sobre health literacy digital, intervenciones con IA para simplificación de textos médicos (e.g., ChatGPT y large language models aplicados a patient education), ni herramientas existentes como OpenNotes, MedlinePlus Easy-to-Read, o proyectos de plain language en salud.

**Recomendación:** Incorporar al menos 10-15 referencias de 2022-2026, especialmente en:
- Intervenciones digitales de health literacy en adultos mayores
- Uso de NLP/IA para simplificación de textos médicos
- Evaluaciones de accesibilidad cognitiva en sistemas de salud latinoamericanos
- Experiencias chilenas recientes en salud digital (e.g., Hospital Digital, Salud Responde)

### 2.2 Vacío de conocimiento poco convincente

El texto afirma que existe un "vacío de conocimiento" en intervenciones digitales accesibles para personas mayores en atención primaria. Sin embargo:

- No se presenta una búsqueda sistemática que respalde esta afirmación (no hay estrategia de búsqueda, ni bases consultadas, ni criterios de inclusión/exclusión)
- Existen múltiples intervenciones internacionales documentadas que el texto no menciona ni diferencia de la propuesta
- La afirmación de que "la investigación en esta área es aún incipiente" a nivel nacional requiere evidencia concreta (¿se hizo una búsqueda en repositorios chilenos? ¿cuántos estudios se encontraron?)

**Recomendación:** Incluir una mini-revisión estructurada que demuestre el vacío, o al menos mencionar los estudios existentes y explicar por qué son insuficientes.

### 2.3 Falta de diferenciación con soluciones existentes

No se menciona ninguna herramienta o intervención comparable existente. El evaluador se preguntará: ¿por qué no usar herramientas de simplificación de lenguaje ya disponibles? ¿Qué hace esta propuesta diferente de un prompt de ChatGPT que simplifique textos médicos?

**Recomendación:** Incluir una tabla comparativa de soluciones existentes vs. la propuesta, destacando el valor agregado específico.

---

## 3. Solución propuesta (Sección 1.2)

### 3.1 Vaguedad tecnológica

La descripción de la solución es extremadamente genérica. Se menciona un "prototipo funcional" que "procesa documentos clínicos" para generar "versiones adaptadas", pero no se especifica:

- **¿Qué tecnología se usará?** ¿Reglas de simplificación? ¿NLP? ¿Modelos de lenguaje? ¿Procesamiento manual asistido?
- **¿Cómo se procesan los documentos?** El mecanismo de "procesamiento" es una caja negra
- **¿Qué arquitectura tendrá el sistema?** Web, app móvil, desktop, integración con sistemas hospitalarios
- **¿Qué nivel de automatización se espera?** ¿Totalmente automático, semi-automático, asistido?

**Problema grave:** Un evaluador técnico no puede juzgar la factibilidad sin saber qué se va a construir. La descripción podría aplicarse a cualquier cosa, desde un formulario web simple hasta un sistema con IA generativa.

**Recomendación:** Describir explícitamente el stack tecnológico, el flujo de procesamiento de documentos, y mostrar al menos un wireframe o diagrama de arquitectura conceptual.

### 3.2 Componentes del sistema poco detallados

La tabla de resultado tecnológico menciona 4 componentes:
1. Módulo de ingreso de documentos
2. Módulo de procesamiento y adaptación
3. Interfaz para profesionales
4. Interfaz para personas mayores

Pero no se detalla la complejidad de cada uno. El componente (2) es el núcleo de la innovación y recibe la misma descripción superficial que un formulario de carga de archivos.

### 3.3 Indicadores de éxito cuestionables

- **"Incremento ≥20% en comprensión"**: ¿Respecto a qué baseline? ¿Medido con qué instrumento? ¿20% es clínicamente significativo? No se justifica este umbral.
- **"Usabilidad ≥70 en SUS"**: Un SUS de 70 es "aceptable" pero apenas sobre el promedio (68). Para una herramienta diseñada específicamente para accesibilidad, se esperaría un umbral más alto (≥75-80).
- **"≥70% de valoración positiva"**: Métrica vaga sin instrumento definido.

**Recomendación:** Justificar cada umbral con literatura, y definir los instrumentos específicos desde la propuesta.

---

## 4. Metodología (Sección 2.3)

### 4.1 Tamaño muestral insuficientemente justificado

**Este es probablemente el punto más débil de la propuesta.**

La justificación del tamaño muestral (n=60, 30+30) es:

> "El tamaño propuesto permite realizar análisis comparativos preliminares y es consistente con estudios aplicados en contextos reales de atención primaria, priorizando la viabilidad del estudio."

**Problemas:**
- No hay cálculo de potencia estadística (power analysis)
- No se especifica el tamaño del efecto esperado
- No se menciona el nivel de significancia ni la potencia deseada
- No se cita ningún estudio comparable que justifique el n=60
- "Priorizando la viabilidad" es una justificación pragmática, no científica
- Con n=30 por grupo y variables de comprensión, la potencia estadística será baja para detectar diferencias moderadas

**Recomendación:** Realizar un cálculo de potencia formal. Ejemplo: si se espera un efecto medio (d=0.5) con α=0.05 y potencia=0.80, se necesitan ~64 por grupo (128 total). Si el presupuesto no alcanza, se debe reconocer explícitamente esta limitación y ajustar las conclusiones esperadas.

### 4.2 Diseño cuasi-experimental sin especificar

- **¿Cómo se asignan los grupos?** No se describe el mecanismo de asignación al grupo intervención vs. comparación. ¿Por centro de salud? ¿Por orden de llegada? ¿Por conveniencia?
- **¿Hay matching?** No se menciona si se emparejarán los grupos por variables confusoras (edad, nivel educativo, condición de salud)
- **¿Hay cegamiento?** No se menciona si los evaluadores serán ciegos a la condición experimental
- **¿Qué diseño cuasi-experimental específico?** Pre-post con grupo control no equivalente, series de tiempo interrumpidas, regression discontinuity... no se especifica
- **¿Mediciones pre y post o solo post?** El resumen dice "pre y post" pero la metodología dice "comprensión posterior a la exposición"

**Recomendación:** Especificar el diseño exacto (e.g., "diseño pre-post con grupo control no equivalente"), describir la asignación de grupos, las estrategias de control de confusores y el plan de análisis detallado.

### 4.3 Instrumentos de medición indefinidos

Se mencionan genéricamente:
- "Pruebas de comprensión de información en salud" — ¿Cuáles? ¿NVS? ¿TOFHLA? ¿Instrumento ad hoc? ¿Validado en Chile?
- "Escala de usabilidad (SUS o equivalente)" — ¿SUS u otra? La indefinición sugiere que no se ha decidido
- "Cuestionarios de percepción" — completamente indefinido
- "Entrevistas semiestructuradas" — sin guion temático

**Problema:** FONIS espera que los instrumentos estén definidos o al menos se presente un plan de desarrollo y validación si serán ad hoc.

### 4.4 Plan de análisis insuficiente

"Estadística descriptiva y pruebas de comparación de medias" es demasiado genérico. No se especifica:
- Qué prueba estadística se usará (t-test, Mann-Whitney, ANCOVA)
- Cómo se manejarán datos faltantes
- Si se controlará por covariables
- Software estadístico a utilizar
- Análisis de sensibilidad

### 4.5 Componente cualitativo subdimensionado

- 10-15 participantes para el componente cualitativo sin justificación de saturación teórica
- No se especifica el método de análisis cualitativo más allá de "análisis de contenido"
- No se describe cómo se integrarán los hallazgos cualitativos con los cuantitativos (mixed methods integration)

---

## 5. Pregunta de investigación e hipótesis (Sección 2.1)

### 5.1 Hipótesis con resultado predecible

La hipótesis es esencialmente: "si le damos información más fácil de entender a la gente, la entenderán mejor". Esto es casi tautológico. El evaluador puede cuestionar si realmente hay una hipótesis que pueda ser refutada.

**Recomendación:** Reformular para que sea más específica y falsificable. Por ejemplo: cuantificar el efecto esperado, especificar para qué tipos de documentos, o incluir hipótesis sobre mediadores/moderadores (edad, nivel educativo, tipo de documento).

### 5.2 Supuestos no verificados

El supuesto "la implementación de herramientas digitales accesibles en contextos de atención primaria es factible y aceptable" es en sí mismo una pregunta de investigación, no un supuesto. Si no se cumple, todo el proyecto falla.

---

## 6. Equipo de investigación (Sección 3)

### 6.1 Fortalezas del equipo

- Equipo multidisciplinario (UX, informática, estadística, electrónica)
- Experiencia demostrada en UX y accesibilidad
- Publicaciones indexadas relevantes
- Colaboración interinstitucional (UTEM, PUCV)

### 6.2 Debilidades del equipo

- **No hay profesionales de salud en el equipo.** Para un proyecto FONIS (investigación en salud), es llamativo que ningún investigador sea profesional de la salud (médico, enfermera, kinesiólogo, etc.). Esto puede ser un factor de rechazo.
- **No hay epidemiólogo ni bioestadístico.** Nicolás Matus tiene formación en estadística, pero su perfil es más cercano a analítica educativa que a bioestadística o epidemiología.
- **Sandra Cano y Nicolás Matus son "aporte institucional PUCV"** (sin costo), lo que puede generar dudas sobre su compromiso real con el proyecto.
- **Boris Bustos a 20 HH/mes** para desarrollar un prototipo funcional completo parece insuficiente. Si el prototipo es el resultado tecnológico principal, el recurso de desarrollo debería ser mayor.
- **José Cerón a 10 HH/mes** para toda la infraestructura tecnológica es muy limitado.

### 6.3 Dedicación acumulada

La tabla de disponibilidad (sección 3.1) muestra que varios investigadores tienen compromisos significativos en otras instituciones y proyectos. María de los Ángeles Ferrer, por ejemplo, tiene 30 HH/mes comprometidas en otros proyectos durante 2026. Sumando las 48 HH/mes del proyecto FONIS, esto implicaría al menos 78 HH/mes, lo que excede una jornada laboral estándar.

**Recomendación:** Verificar la factibilidad de las dedicaciones declaradas y considerar incluir al menos un co-investigador del área de salud pública o medicina familiar.

---

## 7. Plan de trabajo (Sección 2.5)

### 7.1 Aprobación ética optimista

La gestión de autorizaciones éticas se planifica para los meses 1-3. En la práctica, obtener la aprobación de un Comité de Ética Científico en Chile puede tomar 3-6 meses o más, especialmente cuando involucra población vulnerable y centros de salud públicos. Si se retrasa, arrastra todo el cronograma.

### 7.2 Solapamiento de fases

- La fase "Definir" (meses 4-8) se solapa con "Idear" (meses 6-10) y "Prototipar" (meses 8-16). Esto es coherente con un enfoque iterativo, pero el cronograma detallado no refleja buffers para iteraciones reales.
- El diseño del estudio cuasi-experimental (meses 12-14) ocurre muy tarde si se necesita aprobación ética adicional para la fase experimental.

### 7.3 Desarrollo del prototipo comprimido

El prototipo funcional se desarrolla entre los meses 10-16 (7 meses), pero con un desarrollador a 20 HH/mes. Esto equivale a ~140 horas-hombre totales para un sistema con 4 módulos, múltiples interfaces y procesamiento de documentos. Es ajustado.

---

## 8. Implementación y transferencia (Sección 1.2.3)

### 8.1 Cartas de apoyo no mencionadas

Se menciona la participación de Fundación Comunida y una profesional de SENADIS, pero no se indica si se cuentan con cartas de apoyo o compromiso formal. FONIS generalmente las exige.

### 8.2 CESFAM no identificados

No se nombra ningún CESFAM específico donde se implementará el estudio. Esto genera incertidumbre sobre la factibilidad del reclutamiento y la implementación en terreno.

### 8.3 Inconsistencia en el nombre de la fundación

El texto alterna entre "Fundación Comunida" y "Fundación Comunid**a**" (con la "a" pegada a la siguiente palabra). Parece un error tipográfico recurrente que debe corregirse.

---

## 9. Ética (Sección 2.4)

### 9.1 Aspectos positivos
- Aborda los principios bioéticos fundamentales
- Considera la vulnerabilidad de la población
- Contempla manejo de situaciones emergentes

### 9.2 Aspectos faltantes
- No se menciona la **protección de datos personales** (Ley 19.628 o la nueva ley de datos personales en Chile)
- No se describe el **manejo de datos clínicos** que ingresarán al sistema
- No se aborda el **riesgo de que la herramienta genere información incorrecta o simplificada de manera que distorsione el sentido clínico**
- No se menciona el **almacenamiento y seguridad de la información** procesada por el prototipo

---

## 10. Redacción y presentación

### 10.1 Redundancia excesiva

El documento repite las mismas ideas en múltiples secciones con variaciones mínimas. Por ejemplo, la frase "intervención digital accesible, materializada en un prototipo funcional" aparece al menos 8 veces. "Accesibilidad cognitiva, lenguaje claro y diseño centrado en el usuario" se repite de forma casi idéntica al menos 10 veces.

**Impacto:** El evaluador, que debe leer decenas de propuestas, puede percibir la redundancia como falta de contenido sustantivo o como relleno.

### 10.2 Lenguaje excesivamente genérico

Frases como "contextos reales de atención primaria", "mejora significativa", "alto potencial de implementación" se usan sin sustento concreto. El texto privilegia la descripción formal sobre el contenido técnico.

### 10.3 Falta de datos duros

No se presentan estadísticas concretas sobre:
- Prevalencia de baja health literacy en adultos mayores chilenos
- Número de adultos mayores en APS
- Tasas de adherencia actuales
- Datos demográficos de la comuna donde se implementará

---

## 11. Presupuesto (observaciones preliminares)

De los archivos CSV de costos no se incluyen en esta auditoría, pero se observa que:
- El costo por HH varía significativamente entre miembros del equipo ($12.500 vs. $25.000)
- Dos investigadores son "aporte institucional" sin costo directo
- No se menciona presupuesto para infraestructura tecnológica (servidores, hosting, licencias)
- No se menciona presupuesto para incentivos a participantes

---

## 12. Resumen de hallazgos por severidad

### Críticos (pueden causar rechazo)
1. **Ausencia de profesionales de salud en el equipo** para un proyecto FONIS
2. **Tamaño muestral sin cálculo de potencia estadística**
3. **Vaguedad en la descripción tecnológica** de la solución
4. **Diseño cuasi-experimental no especificado** (asignación de grupos, control de confusores)
5. **Instrumentos de medición no definidos**

### Importantes (debilitan significativamente la propuesta)
6. Estado del arte desactualizado (referencias mayoritariamente pre-2020)
7. Hipótesis con bajo potencial de refutación
8. CESFAM no identificados para la implementación
9. Horas de desarrollo insuficientes para la complejidad del prototipo
10. Plan de análisis estadístico insuficiente
11. No se menciona protección de datos personales ni seguridad de información clínica

### Menores (mejoras recomendables)
12. Redundancia excesiva en la redacción
13. Inconsistencia en nombre "Fundación Comunida/Comunidad"
14. Cartas de apoyo no mencionadas
15. Falta de datos epidemiológicos concretos
16. Indicadores de éxito sin justificación basada en literatura

---

## 13. Recomendaciones prioritarias

1. **Incorporar un co-investigador del área de salud** (médico familiar, enfermera de APS, o salubrista público)
2. **Realizar y presentar un cálculo de potencia estadística** formal
3. **Detallar la solución tecnológica**: arquitectura, tecnologías, flujo de procesamiento, diagramas
4. **Actualizar el estado del arte** con literatura 2022-2026
5. **Especificar el diseño cuasi-experimental** completamente
6. **Definir los instrumentos de medición** o describir el plan de desarrollo/validación
7. **Identificar los CESFAM** y obtener cartas de apoyo
8. **Reducir la redundancia** y reemplazar frases genéricas con datos concretos
9. **Abordar protección de datos y seguridad** de información clínica
10. **Revisar la factibilidad de las horas-hombre** del equipo técnico
