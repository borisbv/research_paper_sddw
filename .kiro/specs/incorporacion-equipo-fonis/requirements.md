# Requirements — Incorporación de Cristhian Figueroa y Daniela Godoy al equipo FONIS 2026

## Contexto

Se han agregado dos nuevos perfiles de académicos UTEM al directorio `temp_context/perfil_investigadores/`:

- **Cristhian Alfonso Figueroa Martínez** — Arquitecto, Dr. in Transport Studies (UTEM). Líneas: entorno construido, espacio público, barrios y grupos vulnerables.
- **Daniela Godoy Donoso** — Arquitecta, Msc. Urban Regeneration (UTEM). Líneas: regeneración urbana, participación ciudadana en diseño urbano, normativas territoriales.

El proyecto FONIS 2026 busca desarrollar y evaluar una intervención digital accesible para mejorar la comprensión de información en salud en personas mayores. El presupuesto actual tiene ANID al tope ($72.000.000) y UTEM aporte incremental en $43.200.000 (mínimo requerido: 60% del subsidio ANID).

---

## Requerimientos funcionales

### RF-1: Análisis de pertinencia de perfiles

**Criterios de aceptación:**
- [ ] Mapeo explícito entre líneas de investigación de cada académico y los objetivos específicos del proyecto (OE1–OE4 y transferencia T.3/T.5)
- [ ] Identificación de backlog items que su incorporación ayuda a mitigar (ver `backlog_revision_manual_fonis.md`)
- [ ] Calificación de pertinencia: Alta / Media / Baja, con justificación

**Análisis preliminar:**
- Daniela Godoy → Alta pertinencia para OE1 (diagnóstico participativo) y OE2 (co-diseño intervención). Su expertise en metodologías de participación ciudadana aplicadas al diseño es directamente transferible al co-diseño con personas mayores y profesionales de salud. Mitiga parcialmente el backlog item #1 (fortalecer el componente metodológico del equipo).
- Cristhian Figueroa → Pertinencia Media-Baja en relación directa con salud digital. Su expertise en entorno construido y grupos vulnerables puede aportar en el análisis del contexto espacial de CESFAMs y accesibilidad del entorno donde se aplica la intervención.

### RF-2: Definición de roles dentro del proyecto

**Criterios de aceptación:**
- [ ] Cada académico tiene un rol nominado y una descripción de actividades específicas dentro del proyecto
- [ ] Las actividades asignadas corresponden a objetivos específicos existentes (no se crean nuevos OE)
- [ ] La dedicación horaria es coherente con las actividades asignadas y no entra en conflicto con otras obligaciones declaradas
- [ ] Los roles propuestos son aceptables según las bases FONIS 2026 (categoría "co-investigador" o "investigador asociado")

**Propuesta de roles:**
- **Daniela Godoy** → Co-investigadora en metodologías de participación ciudadana. Activa en OE1 y OE2. Horas estimadas: 36 HH/mes durante 12 meses (fases de co-diseño).
- **Cristhian Figueroa** → Investigador asociado en análisis de contexto y accesibilidad. Apoyo en OE1 (diagnóstico de contexto espacial en CESFAMs). Horas estimadas: 24 HH/mes durante 6 meses (fase diagnóstica).

### RF-3: Modificación del presupuesto

**Criterios de aceptación:**
- [ ] ANID no supera $72.000.000 (restricción inamovible: tope del concurso)
- [ ] Ambos académicos se registran en la categoría "Personal preexistente con pago adicional", con costo 100% a UTEM aporte incremental (sin subsidio ANID) dado que ANID está al tope
- [ ] El overhead (4,8%) se recalcula sobre la base de ANID, no sobre el total del proyecto (verificar si aplica)
- [ ] Los montos de UTEM aporte incremental aumentan para reflejar las nuevas incorporaciones
- [ ] Los totales globales del proyecto son correctos y validados

**Cálculo preliminar:**
- Daniela Godoy: 36 HH/mes × $20.000/HH aprox × 12 meses = $8.640.000 (todo UTEM aporte)
  - Alternativamente, si se declara como monto mensual fijo: ~$720.000/mes × 12 = $8.640.000
- Cristhian Figueroa: 24 HH/mes × $20.000/HH aprox × 6 meses = $2.880.000 (todo UTEM aporte)
  - Monto mensual: ~$480.000/mes × 6 = $2.880.000

> **Nota:** Los montos por hora deben ajustarse a los valores declarados para personal preexistente en la planilla (actualmente $600.000/mes a 48 HH equivale a $12.500/HH). Se debe verificar si las bases permiten valor hora diferenciado o si hay una tabla de referencia.

### RF-4: Actualización del formulario de postulación

**Criterios de aceptación:**
- [ ] La tabla de equipo del formulario incluye a ambos académicos con rol, institución, grado académico y dedicación
- [ ] Las secciones de metodología que describen co-diseño (OE1, OE2) mencionan la experticia de Daniela Godoy
- [ ] La sección de equipo refleja la incorporación sin contradecir otras secciones
- [ ] Si Cristhian Figueroa no tiene rol claro en la metodología actual, se evalúa si procede o no incorporarlo al formulario (puede ser solo presupuestario o puede no incorporarse)

### RF-5: Validación contra bases FONIS 2026

**Criterios de aceptación:**
- [ ] Verificar límites de porcentaje de gasto en personal sobre total ANID (bases indican máximo)
- [ ] Confirmar que la categoría de declaración elegida (pago adicional) es compatible con la condición contractual de los académicos UTEM
- [ ] Confirmar que el número total de investigadores/as del equipo no excede límites de las bases

---

## Requerimientos no funcionales

### RNF-1: Coherencia interna
- Las modificaciones no deben crear inconsistencias entre la planilla de costos y el formulario de postulación.
- Toda cifra nueva debe ser trazable a la planilla CSV.

### RNF-2: Actualización del README de temp_context
- El `temp_context/README.md` ya lista a ambos académicos en la tabla de perfiles. Verificar que la descripción de roles sea precisa tras la decisión final.

### RNF-3: Registro en backlog
- Si la incorporación resuelve o cierra parcialmente algún ítem del backlog, actualizar `backlog_revision_manual_fonis.md`.

---

## Restricciones

| Restricción | Valor | Fuente |
|-------------|-------|--------|
| Subsidio ANID máximo | $72.000.000 | Bases FONIS 2026 |
| Aporte institucional mínimo | 60% del ANID = $43.200.000 | Bases FONIS 2026 |
| Overhead máximo | 15% sobre ANID | Bases FONIS 2026 (actual: 4,8%) |
| Plazo del proyecto | 24 meses | Formulario |
| Ambos académicos pertenecen a UTEM | → se declaran como UTEM, no como colaboradores externos | CV |

---

## Decisiones pendientes para el equipo investigador

1. **¿Se incorpora a Cristhian Figueroa?** Su pertinencia es media-baja. Si el equipo considera que el eje de accesibilidad espacial no es prioritario, puede omitirse sin afectar la solidez del proyecto.
2. **¿Cuál es el valor hora oficial declarado para personal preexistente UTEM?** Esto determina el monto mensual a declarar.
3. **¿La incorporación de Daniela Godoy resuelve suficientemente el backlog item #1 (falta de profesional de salud)?** Ella no es profesional de salud, pero fortalece la metodología participativa. La necesidad de un profesional APS sigue vigente.

---

## Estado

- **Fase actual:** Requirements (pendiente aprobación)
- **Siguiente fase:** Design (propuesta detallada de modificaciones)
- **Prioridad:** Alta — afecta directamente la solidez del equipo y el presupuesto de postulación
