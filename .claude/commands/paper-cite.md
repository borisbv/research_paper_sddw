# /paper:cite — Buscar y agregar citación

Busca papers relevantes para una claim, verifica su existencia y agrega al .bib.

## Uso
```
/paper:cite "<claim o descripción del concepto a citar>"
```

## Parámetros
- `$ARGUMENTS` — La claim o concepto que necesita citación

## Instrucciones

Eres un asistente de gestión de referencias científicas. Usa los skills `research-lookup` y `citation-management` de `.claude/skills/` como metodología.

### Proceso

1. **Analiza la claim** en `$ARGUMENTS`:
   - Identifica los conceptos clave
   - Determina qué tipo de evidencia necesita (trabajo seminal, review, estudio empírico, etc.)
   - Identifica el contexto si el usuario menciona una sección

2. **Busca referencias relevantes** usando tu conocimiento y las APIs disponibles:
   - Prioriza papers con DOI verificable
   - Busca en: Semantic Scholar, CrossRef, PubMed (según el dominio)
   - Objetivo: encontrar 3-5 candidatos relevantes

3. **Para cada candidato, verifica**:
   - Que el DOI/URL sea válido
   - Que el paper sea relevante para la claim específica
   - Que sea de una fuente confiable (peer-reviewed)
   - Año de publicación (preferir recientes para claims de estado del arte)

4. **Presenta los candidatos** al usuario:
   ```
   📚 Referencias encontradas para: "<claim>"

   [1] Apellido et al. (Año) — "Título completo"
       DOI: 10.xxxx/xxxxx
       Relevancia: [Alta/Media] — <explicación en 1 oración>

   [2] ...

   ¿Cuál(es) deseas agregar? (ej: 1, 2,3 o "todas")
   ```

5. **Cuando el usuario confirme**, para cada referencia seleccionada:
   - Genera la entrada BibTeX correcta con todos los campos requeridos
   - Usa el `citation_style` de `paper/metadata.yaml`
   - Agrega al final de `references/references.bib`
   - Genera la clave de citación en el formato correcto (ej: `smith2023llms`)

6. **Reporta al usuario**:
   - Entradas agregadas al .bib con sus claves
   - Cómo insertar la citación en el texto (ej: `\cite{smith2023llms}` o `[1]`)
   - Si hay alguna referencia que no pudo ser verificada, indícalo claramente

### Formato BibTeX estándar

```bibtex
@article{key,
  title={Título completo del paper},
  author={Apellido, Nombre and Apellido2, Nombre2},
  journal={Nombre de la revista},
  volume={X},
  number={Y},
  pages={Z--ZZ},
  year={YYYY},
  publisher={Editorial},
  doi={10.xxxx/xxxxx}
}
```

Para otros tipos: `@inproceedings`, `@book`, `@techreport`, `@misc` según corresponda.
