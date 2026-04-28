# Tasks — Incorporación de Cristhian Figueroa y Daniela Godoy al equipo FONIS 2026

> **Decisión del equipo (2026-04-27):** Se confirma Escenario A — incorporar a ambos (Daniela Godoy y Cristhian Figueroa).
> Valor hora adoptado: $12.500/HH (consistente con personal preexistente UTEM existente).
> Horas mínimas ajustadas a 36 HH/mes para ambos (mínimo requerido por la categoría).

---

## Tarea 1 — Actualizar planilla de costos (Daniela Godoy)

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code (con aprobación humana)
**Archivo:** `temp_context/planilla_costos/Planilla_costos_2026.xlsx - DETALLE GASTOS.csv`

**Acciones:**
- [ ] Agregar fila en sección "PERSONAL PREEXISTENTE CON PAGO ADICIONAL":
  - Daniela Godoy | Co-investigadora participación | UTEM | 36 | $0 | $450.000 | 12 | $5.400.000 | $0 | $5.400.000 | $0 | $0 | $0 | $5.400.000 | Validado
- [ ] Actualizar subtotal de la sección
- [ ] Actualizar COSTO TOTAL DEL PROYECTO (sección PERSONAL: ANID sin cambio, UTEM incremental +$5.400.000)
- [ ] Verificar que ANID siga en $72.000.000

**Criterio de éxito:** La planilla suma correctamente y ANID no supera $72M.

---

## Tarea 2 — Actualizar formulario de postulación: tabla de equipo

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code (con aprobación humana)
**Archivo:** `temp_context/Formulario_Postulacion_2026.docx.md`

**Acciones:**
- [ ] Localizar la tabla del equipo en el formulario
- [ ] Agregar fila para Daniela Godoy con: nombre, cargo (co-investigadora), institución (UTEM), grado (Msc. Urban Regeneration), rol específico, dedicación (36 HH/mes, 12 meses)
- [ ] Verificar que no quede inconsistencia con otras secciones que mencionan el equipo

**Criterio de éxito:** El equipo listado en el formulario incluye a Daniela Godoy con datos coherentes con la planilla.

---

## Tarea 3 — Actualizar formulario: secciones metodológicas OE1 y OE2

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code (con aprobación humana)
**Archivo:** `temp_context/Formulario_Postulacion_2026.docx.md`

**Acciones:**
- [ ] Localizar descripción de OE1 (diagnóstico participativo) — agregar mención a expertise de Daniela Godoy en metodologías participativas
- [ ] Localizar descripción de OE2 (co-diseño de la intervención) — agregar referencia a su liderazgo metodológico del proceso co-participativo
- [ ] Verificar tono académico y coherencia con el resto del texto (no romper el hilo narrativo)

**Criterio de éxito:** Las secciones OE1 y OE2 mencionan explícitamente la metodología de participación ciudadana y asocian su liderazgo a Daniela Godoy.

---

## Tarea 4 — [Escenario A] Incorporar a Cristhian Figueroa en planilla

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code (si el equipo confirma Escenario A)
**Archivo:** `temp_context/planilla_costos/Planilla_costos_2026.xlsx - DETALLE GASTOS.csv`

**Acciones (solo si Escenario A):**
- [ ] Agregar fila para Cristhian Figueroa en la misma sección de personal preexistente con pago adicional:
  - Cristhian Figueroa | Investigador asociado entorno | UTEM | 24 | $0 | $300.000 | 6 | $1.800.000 | $0 | $1.800.000 | $0 | $0 | $0 | $1.800.000 | Validado
- [ ] Actualizar subtotales y total del proyecto

---

## Tarea 5 — [Escenario A] Incorporar a Cristhian Figueroa en formulario

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code (si el equipo confirma Escenario A)
**Archivo:** `temp_context/Formulario_Postulacion_2026.docx.md`

**Acciones (solo si Escenario A):**
- [ ] Agregar fila para Cristhian Figueroa en tabla de equipo
- [ ] Agregar mención breve en la descripción de OE1 sobre el análisis del entorno construido/accesibilidad CESFAM

---

## Tarea 6 — Actualizar backlog y README

**Estado:** Completado (2026-04-27)
**Responsable:** Claude Code
**Archivos:** `temp_context/backlog_revision_manual_fonis.md`, `temp_context/README.md`

**Acciones:**
- [ ] En backlog item #1: actualizar estado indicando que la incorporación de Daniela Godoy fortalece la metodología participativa pero que la necesidad de profesional APS sigue activa
- [ ] En `temp_context/README.md`: verificar y ajustar la descripción de roles de Cristhian y Daniela en la tabla de perfiles para que refleje los roles definitivos

**Criterio de éxito:** Backlog y README coherentes con las decisiones tomadas.

---

## Orden de ejecución

```
Decisión del equipo (Esc. A o B)
         │
         ▼
    Tarea 1 (planilla Daniela)
    Tarea 2 (formulario equipo)   ← ejecutar en paralelo
    Tarea 3 (formulario OE1/OE2)
         │
         ├─── Si Escenario A:
         │       Tarea 4 (planilla Cristhian)
         │       Tarea 5 (formulario Cristhian)
         │
         ▼
    Tarea 6 (backlog + README)
```
