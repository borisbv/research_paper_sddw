# Technical Design: Paper Finalization and Delivery

## Manuscript Consolidation Workflow
El proceso de consolidación unificará los metadatos y las secciones en un único archivo Markdown para facilitar la exportación.

1. **Header (YAML):** Se extraerá de `paper/metadata.yaml`.
2. **Body:** Se concatenarán las secciones en orden IMRyD:
   - `abstract.md`
   - `introduction.md`
   - `methodology.md`
   - `results.md`
   - `discussion.md`
   - `conclusion.md`
3. **Figures Integration:** Se insertarán referencias explícitas en formato Pandoc:
   - `![Categorías de análisis derivadas de la investigación cualitativa.](figures/figure1.jpg){#fig:figure1}`
   - `![Lienzo de inspiración (Moodboard) con enfoque cultural caribeño.](figures/figure2.jpg){#fig:figure2}`
   - `![Prototipo de alta fidelidad: Maqueta física del sistema modular.](figures/figure3.jpg){#fig:figure3}`

## Translation Pipeline (ES -> EN)
1. **Source Sectioning:** Se traducirán los archivos de `paper/sections/` de forma individual para mantener la granularidad.
2. **Technical Dictionary:**
   - *Hogar temporal* -> *Temporary Home*
   - *Vivienda modular* -> *Modular Housing*
   - *Vida cívica* -> *Civic Life*
   - *Análisis Temático Reflexivo* -> *Reflexive Thematic Analysis*
3. **Target Structure:** Los archivos traducidos se guardarán en `paper/sections_en/` antes de la consolidación.

## Word (DOCX) Production Specs
- **Engine:** Pandoc 3.9 + Citeproc.
- **Reference Style:** APA 7th Edition (`apa.csl`).
- **Bibliography:** Se generará al final del documento bajo el encabezado `# References`.
- **Command Template:**
  ```bash
  pandoc manuscript.md -o manuscript.docx --citeproc --bibliography=references.bib --csl=apa.csl
  ```

## File Deliverables
- `paper/manuscript_es.md` / `paper/manuscript_es.docx`
- `paper/manuscript_en.md` / `paper/manuscript_en.docx`
- `references/apa.csl` (Dependency)
