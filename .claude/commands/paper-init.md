# /paper:init — Inicializar nuevo paper científico

Inicializa un nuevo paper científico con estructura SDD completa.

## Uso
```
/paper:init "<tema>" "<revista_objetivo>"
```

## Parámetros
- `$ARGUMENTS` — formato: `"<tema>" "<revista_objetivo>"` (ej: `"LLMs en diagnóstico médico" "Nature Medicine"`)

## Instrucciones

Eres un asistente de escritura científica. Cuando el usuario ejecuta este comando:

1. **Parsea los argumentos** desde `$ARGUMENTS`:
   - Primer argumento: tema del paper
   - Segundo argumento: revista objetivo

2. **Consulta el skill venue-templates** (`~/.claude/skills/venue-templates/`) para obtener:
   - Formato y estructura requerida por la revista
   - Límites de palabras por sección y abstract
   - Estilo de citas (APA, IEEE, Vancouver, Nature, etc.)
   - Requisitos especiales

3. **Crea la estructura de directorios** si no existe:
   ```
   paper/
   references/
   figures/
   data/
   scripts/
   ```

4. **Genera `paper/metadata.yaml`** con:
   ```yaml
   title: "[PROVISIONAL] <tema>"
   authors:
     - name: ""
       affiliation: ""
       email: ""
   journal: <revista_objetivo>
   submission_date: <fecha_actual>
   status: draft
   language: en
   citation_style: <estilo_según_revista>
   word_limits:
     abstract: <límite_según_revista>
     total: <límite_según_revista>
     introduction: <estimado>
     methodology: <estimado>
     results: <estimado>
     discussion: <estimado>
   keywords: []
   ```

5. **Genera `paper/outline.md`** con estructura IMRaD adaptada a la revista:
   ```markdown
   # [PROVISIONAL] <tema>

   ## Paper Outline — <revista_objetivo>

   ### Abstract (máx. X palabras)
   - [ ] Background/contexto (1-2 oraciones)
   - [ ] Gap/problema (1 oración)
   - [ ] Objetivo/hipótesis (1 oración)
   - [ ] Métodos principales (1-2 oraciones)
   - [ ] Resultados clave (1-2 oraciones)
   - [ ] Conclusión/implicación (1 oración)

   ### 1. Introduction
   - [ ] Contexto del dominio
   - [ ] Gap en la literatura
   - [ ] Hipótesis/pregunta de investigación
   - [ ] Contribuciones del paper
   - [ ] Estructura del paper

   ### 2. Related Work / Background
   - [ ] Subcategoría 1
   - [ ] Subcategoría 2
   - [ ] Posicionamiento respecto al estado del arte

   ### 3. Methodology
   - [ ] Descripción del dataset/materiales
   - [ ] Diseño experimental
   - [ ] Métricas de evaluación
   - [ ] Detalles de implementación

   ### 4. Results
   - [ ] Resultado principal
   - [ ] Análisis comparativo
   - [ ] Análisis de ablación (si aplica)

   ### 5. Discussion
   - [ ] Interpretación de resultados
   - [ ] Limitaciones
   - [ ] Trabajo futuro

   ### 6. Conclusion
   - [ ] Resumen de contribuciones
   - [ ] Impacto esperado

   ### References
   - [ ] Mínimo X referencias (según revista)
   ```

6. **Crea `references/references.bib`** vacío con header:
   ```bibtex
   % References for: <tema>
   % Journal: <revista_objetivo>
   % Citation style: <estilo>
   % Generated: <fecha>
   ```

7. **Crea las secciones del paper** como archivos vacíos en `paper/sections/`:
   - `abstract.md`
   - `introduction.md`
   - `related-work.md`
   - `methodology.md`
   - `results.md`
   - `discussion.md`
   - `conclusion.md`

   Cada archivo con header:
   ```markdown
   # <Nombre de Sección>

   <!-- STATUS: empty -->
   <!-- TARGET WORDS: X -->
   <!-- CURRENT WORDS: 0 -->

   ```

8. **Inicia las specs SDD** ejecutando:
   ```
   /kiro:spec-init "<tema> para <revista_objetivo>"
   ```

9. **Reporta al usuario**:
   - Estructura creada
   - Formato de la revista (límites, estilo de citas)
   - Próximos pasos recomendados
   - Comando para empezar a escribir la primera sección
