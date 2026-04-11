# Task List: Paper Finalization and Delivery

## Milestone 1: Spanish Manuscript Consolidation
1.1 Descargar `apa.csl` desde el repositorio oficial de Zotero a `references/`.
1.2 Crear `paper/manuscript_es.md` integrando el YAML de `paper/metadata.yaml`.
1.3 Concatenar secciones (`abstract`, `introduction`, `methodology`, `results`, `discussion`, `conclusion`) en `manuscript_es.md`.
1.4 Insertar referencias a figuras en formato Pandoc con sus captions.

## Milestone 2: DOCX Generation (ES)
2.1 Ejecutar comando Pandoc para generar `paper/manuscript_es.docx` con estilo APA 7.
2.2 Verificar visualmente (vía logs/conteo) que las imágenes y bibliografía se integraron correctamente.

## Milestone 3: Academic Translation (EN)
3.1 Traducir metadatos (Title, Abstract, Keywords) al inglés.
3.2 Traducir secciones individuales de `paper/sections/*.md` y guardar en `paper/sections_en/`.
3.3 Consolidar `paper/manuscript_en.md` siguiendo la misma estructura que la versión en español.
3.4 Traducir los pies de figura (captions) en el manuscrito consolidado.

## Milestone 4: DOCX Generation (EN) and Final Validation
4.1 Ejecutar comando Pandoc para generar `paper/manuscript_en.docx`.
4.2 Ejecutar validación final de conteo de palabras en ambas versiones.
4.3 Verificar anonimización final en los cuatro archivos entregables.
4.4 Generar reporte de cierre del proyecto.
