# Task List: Paper Adaptation 'Casa de Paso'

## Milestone 1: Initialization and Foundation
1.1 Configurar estructura de directorios `paper/sections/`, `references/`, `figures/`. (P)
1.2 Generar `paper/metadata.yaml` alineado con la revista *Migraciones*.
1.3 Inicializar `references/references.bib` con las citas básicas del manuscrito original.
1.4 Ejecutar validación inicial de estructura (`validate-structure.py`).

## Milestone 2: Core Manuscript Transformation (IMRaD)
2.1 Redactar el nuevo Título y Abstract (máx. 250 palabras) con enfoque en políticas públicas.
2.2 Transformar la Introducción: integrar PNME 2024-2025 y déficit habitacional.
2.3 Adaptar la Metodología: detallar etapas UX con estilo de prosa fluida (8-15 líneas por párrafo).
2.4 Refinar Resultados: integrar verbatim cualitativos y referenciación cruzada a figuras/tablas.
2.5 Redactar Discusión y Conclusiones: visión crítica y recomendaciones de política pública.

## Milestone 3: Scientific Styling and Formatting
3.1 Aplicar reglas de énfasis visual (negritas para categorías, cursivas para tecnicismos). (P)
3.2 Formatear citas cualitativas como párrafos independientes y anónimos.
3.3 Revisar y limpiar el archivo BibTeX (`tidy-bib.py`) y agregar DOIs faltantes.
3.4 Mapear y validar figuras (`image1.jpg`, `image2.jpg`, `image3.jpg`) en el texto.

## Milestone 4: Final Validation and Review
4.1 Ejecutar validación de prosa (`validate-prose.py`) para asegurar fluidez y densidad.
4.2 Verificar conteo de palabras (`validate-word-count.py`) según límites de la revista.
4.3 Validar citas y bibliografía (`validate-citations.py`).
4.4 Realizar revisión de anonimización para el sistema doble ciego.
4.5 Generar reporte final de estado del paper (`paper-status`).
