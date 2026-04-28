# Research & Decisiones de Diseño

---
**Propósito**: Capturar hallazgos de investigación y decisiones que informan el diseño del formulario FONIS 2026.
---

## Resumen
- **Feature**: `postulacion-fonis-2026`
- **Alcance de Discovery**: Extensión (completar secciones faltantes de un formulario existente)
- **Hallazgos Clave**:
  1. El formulario ya tiene secciones 1 y 2 sustancialmente completas; falta completar la tabla Gantt del plan de trabajo, la sección 3 completa y la planilla de costos
  2. El equipo tiene un fuerte perfil UX/accesibilidad pero la distribución presupuestaria requiere distinguir entre personal preexistente (UTEM/PUCV) y personal contratado para el proyecto
  3. Las restricciones presupuestarias del concurso son estrictas: topes por persona, overhead 15%, cofinanciamiento 10%

## Research Log

### Estructura del equipo y clasificación presupuestaria
- **Contexto**: Necesidad de clasificar cada miembro del equipo en la categoría correcta de la planilla de costos
- **Fuentes**: CVs en `temp_context/perfil_investigadores/`, bases del concurso, formulario de postulación
- **Hallazgos**:
  - **Personal preexistente (académicos UTEM)**: Erwin Aguirre (Profesor Titular UTEM), María Ferrer (UTEM). Ambos con contrato vigente en la beneficiaria principal. Aplican para "Personal preexistente con pago remuneración" (mín 80 hrs/mes) o "pago adicional" (mín 36 hrs/mes)
  - **Personal preexistente (académicos PUCV)**: Sandra Cano, Nicolás Matus. Son de otra institución, no de la beneficiaria principal. Si PUCV no es beneficiaria secundaria, su aporte sería no incremental o por honorarios
  - **Personal contratado para el proyecto**: Boris Bustos (desarrollador), José Cerón (técnico IoT). No son preexistentes en UTEM
  - **Personal administrativo**: Ayleen Astudillo (gestión financiera)
  - **Ronald Méndez**: Docente en UTEM pero también en otras universidades y Director de Designar. Clasificación depende de su vínculo contractual con UTEM
  - **Daniela Godoy, Janeth Valecillos, Cristhian Figueroa**: Sin CVs disponibles, perfiles por confirmar
- **Implicaciones**: La clasificación presupuestaria afecta directamente los topes salariales aplicables y las categorías de la planilla de costos

### Coherencia metodológica y plan de trabajo
- **Contexto**: El formulario ya contiene una versión narrativa del plan de trabajo (sección 2.5 "VERSIÓN PROPUESTA") pero la tabla Gantt oficial está vacía
- **Hallazgos**:
  - La versión propuesta ya define actividades por objetivo específico con meses asignados
  - Las etapas UX (Empatizar, Definir, Idear, Prototipar, Testear) están mapeadas a rangos de meses
  - Los hitos tecnológicos coinciden: Hito 1 al mes 12, Hito 2 al mes 24
  - Falta incluir actividades transversales: gestión ética, difusión, formación
- **Implicaciones**: La tabla Gantt puede construirse directamente desde la versión propuesta, agregando actividades administrativas y de difusión

### Restricciones presupuestarias clave
- **Contexto**: Validar restricciones de las bases contra la planilla
- **Fuentes**: Bases del concurso FONIS 2026 (secciones 5.3, 7.4)
- **Hallazgos**:
  - Subsidio máximo ANID: $72.000.000
  - Cofinanciamiento mínimo: 10% del subsidio → al menos $7.200.000 si se pide el máximo
  - Overhead máximo: 15% del subsidio → máximo $10.800.000 si se pide el máximo
  - Personal preexistente con remuneración: mín 80 hrs/mes, tope $2.700.000/mes (160 hrs), proporcional
  - Personal preexistente con pago adicional: mín 36 hrs/mes, tope $600.000/mes, no puede superar aporte institucional por remuneraciones
  - No se pueden comprar fungibles ni subcontratar a colaboradoras
  - Viajes internacionales deben justificarse con relación a I+D o transferencia
- **Implicaciones**: El presupuesto debe diseñarse cuidadosamente para maximizar recursos dentro de los topes

### Investigadores en formación
- **Contexto**: Identificar quiénes califican como investigadores en formación
- **Hallazgos**:
  - José Cerón está cursando un Magíster en UTEM → califica como investigador en formación
  - Boris Bustos completó su Magíster recientemente (2024) → podría calificar si se vincula a una tesis o formación adicional
  - Se pueden incluir estudiantes de pregrado/postgrado de UTEM o PUCV que se incorporen al inicio del proyecto
  - Las bases exigen especificar nivel de formación, actividades, tutor y título de tesis
- **Implicaciones**: José Cerón es el candidato natural como investigador en formación. Se pueden incluir perfiles tipo para estudiantes a incorporar

## Decisiones de Diseño

### Decisión: Distribución presupuestaria por categorías
- **Contexto**: Maximizar el subsidio ANID dentro de las restricciones
- **Alternativas Consideradas**:
  1. Concentrar presupuesto en personal contratado (Boris, José, Ayleen) y minimizar pago a preexistentes
  2. Distribuir equitativamente entre personal preexistente (incentivos) y contratado
  3. Maximizar personal contratado + equipamiento tecnológico
- **Enfoque Seleccionado**: Opción 3 — Priorizar personal técnico contratado y equipamiento para el prototipo, con incentivos moderados para investigadores preexistentes
- **Justificación**: El proyecto requiere desarrollo tecnológico intensivo (prototipo funcional), lo que justifica mayor inversión en personal técnico y equipamiento. Los investigadores preexistentes aportan como no incremental (su tiempo de investigación)
- **Trade-offs**: Menor compensación directa a investigadores principales, pero coherente con su dedicación de 48 HH/mes que es compatible con pago adicional

### Decisión: Estructura del plan de trabajo
- **Contexto**: Elegir entre tabla detallada por actividad o agrupación por objetivo
- **Enfoque Seleccionado**: Tabla agrupada por objetivo específico, con actividades detalladas y marcadores mensuales, siguiendo el formato de la versión propuesta existente
- **Justificación**: Coherencia con la sección 2.3 (metodología) y con la estructura solicitada por el formulario

### Decisión: Clasificación de personal PUCV
- **Contexto**: Sandra Cano y Nicolás Matus son de PUCV, no de la beneficiaria principal (UTEM)
- **Enfoque Seleccionado**: Incluirlos como "Personal de entidades beneficiarias que no reciben subsidio" (aporte no incremental), dado que PUCV no aparece como beneficiaria secundaria en el formulario
- **Justificación**: Su participación es como investigadores que aportan expertise sin costo directo al subsidio ANID
- **Trade-off**: No reciben pago del proyecto pero su contribución se contabiliza como aporte institucional no incremental

## Riesgos & Mitigaciones
- **Perfiles sin CV (Daniela Godoy, Janeth Valecillos, Cristhian Figueroa)**: Incluir con información mínima disponible del formulario; solicitar CVs al equipo antes de la presentación final
- **Clasificación presupuestaria incorrecta**: Validar con administración de UTEM el tipo de contrato de cada investigador antes de finalizar la planilla
- **Exceder topes por categoría**: Implementar validación cruzada entre planilla y formulario antes del envío
- **Estudiantes en formación no definidos**: Incluir perfiles tipo con indicación de definición posterior; las bases permiten esta flexibilidad

## Referencias
- Bases FONIS 2026: `temp_context/bases/REX_866-2026_Bases_Fonis2026_c4f9a1b2d8e37f0a6c2b4d9e1f0a3b.md`
- Preguntas Frecuentes: `temp_context/bases/Preguntas_Frecuentes_2026.md`
- Formulario de postulación: `temp_context/Formulario_Postulacion_2026.docx.md`
- CVs del equipo: `temp_context/perfil_investigadores/`
