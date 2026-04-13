---
name: data-visualization-agent
description: Automatización de figuras y visualización de datos de `data/` para papers científicos. Transforma archivos CSV en gráficos de alta calidad (300 DPI) con estilo académico consistente.
---

# Data Visualization Agent

Esta skill facilita la creación de figuras científicas a partir de conjuntos de datos.

## Flujo de Trabajo

1.  **Exploración**: Identificar el archivo CSV en `data/`.
2.  **Configuración**: Usar `assets/theme.json` para asegurar coherencia visual.
3.  **Generación**: Ejecutar `scripts/generate_plot.py`.
4.  **Anotación**: Generar automáticamente el pie de figura (caption) basado en los datos.

## Herramientas

- `scripts/generate_plot.py`: Generador base usando Seaborn/Matplotlib.
- `assets/theme.json`: Configuración de estilos (fonts, palette, grid).

## Ejemplos

"Genera un gráfico de líneas comparando los resultados de precisión de `data/results.csv` y guárdalo en `figures/fig1.png`."
