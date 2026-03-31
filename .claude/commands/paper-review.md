# /paper:review — Revisión científica del paper

Genera un reporte de revisión estilo peer-review (soft specs).

## Uso
```
/paper:review
```

## Instrucciones

Eres un revisor científico experto. Usa los skills `peer-review` y `scientific-critical-thinking` de `.claude/skills/` como referencia para tu metodología de revisión.

### Proceso de Revisión

1. **Lee el paper completo** desde `paper/sections/` y el outline en `paper/outline.md`
2. **Lee el metadata** en `paper/metadata.yaml` para conocer la revista objetivo y sus estándares
3. **Aplica criterios de revisión rigurosa**

### Estructura del Reporte

Genera un reporte en `paper/review-report.md` con esta estructura:

```markdown
# Reporte de Revisión — <título provisional>
**Fecha:** <fecha>
**Revista objetivo:** <nombre>
**Revisor:** Claude (AI Reviewer)

---

## Resumen Ejecutivo
[2-3 oraciones sobre el estado actual del paper y recomendación general: Accept/Minor Revision/Major Revision/Reject]

## Fortalezas
1. ...
2. ...
3. ...

## Debilidades Principales
1. **[CRÍTICO]** ...
2. **[IMPORTANTE]** ...
3. **[MENOR]** ...

## Evaluación por Sección

### Abstract
- Claridad: [1-5]
- Completitud: [1-5]
- Comentarios: ...

### Introduction
- Contexto del problema: [1-5]
- Identificación del gap: [1-5]
- Claridad de contribuciones: [1-5]
- Comentarios: ...

### [... resto de secciones ...]

## Claims sin Soporte Suficiente
Lista de afirmaciones que requieren mejor evidencia o citación:
1. "[texto de la claim]" — Sección X — Sugerencia: ...

## Coherencia Argumentativa
- ¿El problema planteado en la intro es resuelto por la metodología? [Sí/Parcialmente/No]
- ¿Los resultados responden la pregunta de investigación? [Sí/Parcialmente/No]
- ¿La discusión interpreta correctamente los resultados? [Sí/Parcialmente/No]
- Notas: ...

## Reproducibilidad
- ¿La metodología es suficientemente detallada para reproducir? [Sí/Parcialmente/No]
- Elementos faltantes: ...

## Preguntas para los Autores
1. ...
2. ...

## Sugerencias Concretas por Sección
### Introduction
- ...
### Methodology
- ...
[...]

## Checklist de Requisitos para la Revista
- [ ] Estructura correcta para <revista>
- [ ] Límite de palabras respetado
- [ ] Formato de citas correcto
- [ ] Figuras de alta calidad
- [ ] Datos disponibles (si es requerido)
- [ ] Statement de conflicto de intereses
- [ ] Agradecimientos

## Decisión Recomendada
**[Accept / Minor Revision / Major Revision / Reject]**

Razón principal: ...
```

4. **Muestra el reporte al usuario** y ofrece discutir cualquier punto específico.
