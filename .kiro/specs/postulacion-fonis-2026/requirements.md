# Requirements Document

## Introducción

Especificación de requisitos para completar la postulación al Concurso FONIS 2026 del proyecto "Desarrollo y evaluación de una intervención digital accesible para mejorar la comprensión de información en salud en personas mayores". El formulario base (`temp_context/Formulario_Postulacion_2026.docx.md`) tiene las secciones 1 y 2 parcialmente completas. Se requiere finalizar: Plan de Trabajo (2.5), Capacidad de Gestión (3.1–3.3) y Planilla de Costos.

**Restricciones globales del concurso:**
- Subsidio máximo ANID: $72.000.000
- Cofinanciamiento mínimo beneficiarias: 10% del subsidio solicitado
- Plazo máximo de ejecución: 24 meses
- Overhead máximo: 15% del subsidio ANID
- Equipo mínimo: Director(a), Director(a) Alterno(a) e Investigador(a)
- Personal preexistente con pago remuneración: mínimo 80 hrs/mes, tope $2.700.000/mes (160 hrs)
- Personal preexistente con pago adicional: mínimo 36 hrs/mes, tope $600.000/mes
- Formato: Arial 11, interlineado 1.15, extensiones máximas por sección
- Idioma: español

**Equipo del proyecto:**
- Director: Erwin Aguirre Villalobos (UTEM, PhD) — 48 HH/mes
- Directora Alterna: María de los Ángeles Ferrer Mavárez (UTEM, PhD) — 48 HH/mes
- Investigadora: Sandra Cano Mazuera (PUCV, PhD) — 48 HH/mes
- Investigador: Ronald Méndez Sánchez (MSc UX) — 48 HH/mes
- Investigador: Nicolás Matus (PhD doble)
- Investigadora: Daniela Godoy
- Investigadora: Janeth Valecillos
- Cristhian Figueroa
- Personal Técnico: Boris Bustos (MSc, Desarrollador digital)
- Personal Técnico: José Cerón (MSc en curso, IoT)
- Gestión financiera: Ayleen Astudillo (Contadora Auditora)

**Fuentes de datos:**
- CVs en `temp_context/perfil_investigadores/`
- Planillas en `temp_context/planilla_costos/`
- Bases del concurso en `temp_context/bases/`
- Formulario en `temp_context/Formulario_Postulacion_2026.docx.md`

## Requirements

### Requirement 1: Plan de Trabajo (Sección 2.5)

**Objetivo:** Como equipo de investigación, queremos un plan de trabajo detallado con tabla Gantt por objetivo específico, para demostrar la viabilidad temporal del proyecto en 24 meses.

#### Acceptance Criteria

1. The documento shall incluir una tabla Gantt con columnas para los 4 objetivos específicos, actividades detalladas y marcadores de meses 1–24 (año 1: meses 1–12, año 2: meses 13–24).
2. When se genere cada actividad del plan, the documento shall vincularla al objetivo específico correspondiente según la sección 2.2.2 del formulario.
3. The plan de trabajo shall ser coherente con las etapas de diseño centrado en el usuario definidas en la metodología (Empatizar: meses 1–6, Definir: meses 4–8, Idear: meses 6–10, Prototipar: meses 8–16, Testear: meses 14–24).
4. The plan de trabajo shall incluir actividades administrativas: gestión de autorizaciones éticas, coordinación con centros de salud (CESFAM), reclutamiento de participantes.
5. The plan de trabajo shall considerar los hitos definidos en los resultados tecnológicos: Hito 1 al mes 12 (prototipo validado en condiciones controladas) e Hito 2 al mes 24 (prototipo evaluado en contexto real).
6. The plan de trabajo shall respetar la extensión máxima de 2 páginas según las instrucciones del formulario.
7. The plan de trabajo shall incluir actividades de producción científica y difusión: elaboración de artículo, presentaciones en congresos, talleres de difusión.

### Requirement 2: Capacidad de Gestión — Equipo de Investigación (Sección 3.1)

**Objetivo:** Como evaluador del concurso, quiero ver la pertinencia de las funciones, capacidades y dedicación de cada integrante, para evaluar que el equipo tiene las competencias necesarias para ejecutar el proyecto.

#### Acceptance Criteria

1. The tabla de equipo de investigación shall incluir para cada integrante: Nombre/RUT, Institución, Cargo en el proyecto, Funciones y capacidades críticas, Dedicación HH/mes, $/HH y Actividades del plan de trabajo.
2. When se asignen funciones, the documento shall reflejar la coherencia entre el perfil académico/profesional de cada investigador (según CVs) y su rol en el proyecto.
3. The tabla shall incluir al Director (Erwin Aguirre), Directora Alterna (María Ferrer) y al menos un investigador, cumpliendo el equipo mínimo exigido por las bases.
4. The funciones del Director shall incluir: coordinación general del proyecto, liderazgo del diseño de la intervención, supervisión del equipo y vinculación con entidades colaboradoras.
5. The funciones de la Directora Alterna shall incluir: co-liderazgo en diseño UX accesible, supervisión del componente de accesibilidad cognitiva y coordinación del co-diseño con usuarios.
6. The funciones de cada investigador shall estar vinculadas a actividades específicas del plan de trabajo (sección 2.5).
7. The tabla de personal técnico shall incluir a Boris Bustos (desarrollo del prototipo digital), José Cerón (infraestructura tecnológica/IoT) y Ayleen Astudillo (gestión financiera del proyecto).
8. The tabla de dedicación en otros proyectos shall completarse para Director, Directora Alterna e investigadores principales, indicando HH/mes comprometidos en otros proyectos para 2026–2029.

### Requirement 3: Antecedentes Curriculares (Sección 3.2)

**Objetivo:** Como evaluador, quiero una síntesis de los antecedentes de cada integrante del equipo de investigación, para valorar la pertinencia y experiencia del equipo.

#### Acceptance Criteria

1. The sección shall incluir un resumen de máximo 5 líneas por cada integrante del equipo de investigación (Director, Directora Alterna e investigadores).
2. When se redacte cada resumen, the texto shall destacar: grado académico máximo, institución actual, área de especialización, publicaciones relevantes y experiencia en proyectos de investigación.
3. The resumen de Erwin Aguirre shall mencionar su Doctorado, su rol como Profesor Titular en UTEM, su experiencia en UX con énfasis en accesibilidad e inclusión digital, y sus publicaciones Scopus (Q1/Q2).
4. The resumen de María Ferrer shall mencionar su Doctorado, su trayectoria de 20+ años en Diseño UX/DCU, sus publicaciones indexadas y la dirección de proyectos de inclusión (ACCEX).
5. The resumen de Sandra Cano shall mencionar su Doctorado, su rol en PUCV, su experiencia en HCI y computación afectiva.
6. The resumen de Ronald Méndez shall mencionar su Maestría, su experiencia en evaluación de usabilidad y UX, y su rol como Director Académico del Diplomado en UX Design.
7. The resumen de Nicolás Matus shall mencionar su doble doctorado, su investigación en experiencia del estudiante y analítica educativa.
8. The sección shall respetar la extensión máxima de 1 página.

### Requirement 4: Participación de Investigadores en Formación (Sección 3.3)

**Objetivo:** Como equipo de investigación, queremos demostrar la contribución del proyecto a la formación de capacidades, para cumplir con los requisitos de resultados de formación del concurso.

#### Acceptance Criteria

1. The tabla shall incluir para cada investigador en formación: Nombre/RUT, Institución, Pregrado/Postgrado, Actividades a desarrollar, Nombre del investigador responsable/tutor y Título de tesis (si aplica).
2. When se identifiquen investigadores en formación, the documento shall considerar estudiantes de pregrado o postgrado vinculados a las universidades participantes (UTEM, PUCV).
3. The actividades de formación shall estar alineadas con los objetivos del proyecto y las actividades del plan de trabajo.
4. The documento shall especificar el nivel de formación (pregrado, magíster, doctorado) de cada investigador en formación.
5. The sección shall respetar la extensión máxima de 1/2 página.
6. If no se dispone de nombres específicos de estudiantes, the documento shall incluir perfiles tipo con indicación de que serán definidos al inicio de la ejecución.

### Requirement 5: Planilla de Costos — Hoja ANTECEDENTES

**Objetivo:** Como equipo de investigación, queremos completar la hoja de antecedentes de la planilla de costos con los datos del proyecto, para que sea coherente con el formulario de postulación.

#### Acceptance Criteria

1. The planilla shall incluir: plazo en meses (24), Director(a) (Erwin Aguirre), Beneficiaria Principal (UTEM).
2. The presupuesto total de aporte ANID shall no exceder $72.000.000.
3. The presupuesto de aporte institucional shall ser al menos el 10% del subsidio solicitado a ANID.
4. The montos declarados en la planilla shall ser coherentes con los montos de la hoja DETALLE GASTOS.

### Requirement 6: Planilla de Costos — Personal

**Objetivo:** Como equipo de investigación, queremos presupuestar correctamente los costos de personal, para cumplir con las restricciones de las bases del concurso.

#### Acceptance Criteria

1. When se presupueste personal preexistente con pago de remuneración, the planilla shall considerar un mínimo de 80 hrs/mes de dedicación y un monto máximo mensual proporcional a la dedicación (tope $2.700.000 para 160 hrs/mes).
2. When se presupueste personal preexistente con pago adicional (ex-incentivo), the planilla shall considerar un mínimo de 36 hrs/mes y un máximo de $600.000 bruto/mes por persona.
3. The pago adicional no shall superar el monto aportado por la institución por concepto de remuneraciones para cada persona.
4. The personal contratado exclusivamente para el proyecto shall incluir al menos: desarrollador digital (Boris Bustos) y personal de apoyo técnico (José Cerón).
5. When se incluya personal de gestión financiera, the planilla shall considerar a Ayleen Astudillo con funciones de control de gestión y rendición de cuentas.
6. The planilla shall incluir la remuneración mensual bruta declarada para cada persona con pago de remuneración.
7. If se incluye un profesional de transferencia tecnológica, the planilla shall presupuestarlo en honorarios (recomendación de las bases).

### Requirement 7: Planilla de Costos — Equipos, Infraestructura y Operación

**Objetivo:** Como equipo de investigación, queremos presupuestar los gastos de equipamiento, infraestructura y operación necesarios para la ejecución del proyecto.

#### Acceptance Criteria

1. The equipos presupuestados shall estar asociados a objetivos específicos del proyecto y ser necesarios para el desarrollo del prototipo digital y la evaluación de la intervención.
2. The planilla shall considerar equipamiento tecnológico: dispositivos para pruebas con personas mayores (tablets, equipos de cómputo para desarrollo).
3. The gastos de operación shall incluir: gastos generales, viáticos nacionales, materiales fungibles para talleres y actividades de co-diseño.
4. If se incluyen viajes internacionales, the planilla shall detallar el objetivo de cada viaje y su relación con actividades de I+D o transferencia tecnológica.
5. The gastos de administración indirectos (overhead) no shall superar el 15% del subsidio ANID solicitado.
6. The planilla no shall incluir compra de fungibles a entidades colaboradoras.
7. The planilla no shall subcontratar servicios de entidades colaboradoras ni tareas sustanciales del proyecto.

### Requirement 8: Coherencia y Validación Cruzada

**Objetivo:** Como equipo de investigación, queremos asegurar la coherencia entre todas las secciones del formulario y la planilla de costos.

#### Acceptance Criteria

1. The actividades del plan de trabajo (2.5) shall ser consistentes con los objetivos específicos (2.2.2), la metodología (2.3) y los hitos de resultados tecnológicos (1.2.2).
2. The personal listado en la tabla de capacidad de gestión (3.1) shall coincidir con el personal presupuestado en la planilla de costos.
3. The dedicación HH/mes declarada en la tabla de gestión (3.1) shall coincidir con las horas declaradas en la planilla de costos.
4. The suma total del presupuesto ANID más el aporte institucional shall ser coherente entre la hoja ANTECEDENTES y la hoja DETALLE GASTOS.
5. When se eliminen las instrucciones en azul del formulario, the documento final shall no contener textos de instrucciones ni placeholders vacíos.
6. The objetivos específicos shall poder ajustarse si se detectan inconsistencias con la metodología o el plan de trabajo, manteniendo el título del proyecto sin cambios.

### Requirement 9: Formato y Presentación Final

**Objetivo:** Como equipo de investigación, queremos que el formulario cumpla con todos los requisitos de formato del concurso.

#### Acceptance Criteria

1. The formulario shall estar en idioma español.
2. The plan de trabajo shall no exceder 2 páginas.
3. The antecedentes curriculares shall no exceder 1 página.
4. The participación de investigadores en formación shall no exceder 1/2 página.
5. The formulario shall eliminar todas las instrucciones en color azul antes de la versión final.
6. The planilla de costos shall expresar todos los montos en pesos chilenos ($), no en miles de pesos (M$).
