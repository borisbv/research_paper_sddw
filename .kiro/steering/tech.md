# Stack Técnico y Normas Editoriales

## Formato del Manuscrito

- **Procesador**: Word (entrega final) / Markdown + LaTeX (desarrollo)
- **Tipografía**: Times New Roman 12, interlineado 1.5, márgenes 2.5 cm, carta
- **Notas al pie**: Times New Roman 10, espacio sencillo
- **Extensión**: 7.000–10.000 palabras totales (incluye resúmenes, bibliografía, notas)

## Resumen Extendido

- 250–300 palabras en idioma original + inglés
- Debe contener: objetivo/contexto, metodología, conclusiones, originalidad
- Sin citaciones ni abreviaciones

## Palabras Clave

- 4–6 palabras clave en español e inglés
- Deben reflejar temáticas precisas y áreas de conocimiento

## Sistema de Citación

- **Formato**: Chicago Manual of Style, Author-Date (última edición)
- **En texto**: (Apellido año, página) — e.g., (Bachelard 1957, 45)
- **Bibliografía**: listado alfabético, relación 1:1 con citas en texto
- **Nombres completos** de autores/editores obligatorios
- **DOI obligatorio** cuando exista
- **Prohibido**: op. cit., ibid., ibidem
- Citas textuales >4 renglones: formato cita larga (espacio sencillo, letra 11, márgenes reducidos)

## Siglas

Primera vez: fórmula completa + sigla entre paréntesis en mayúscula. Después: solo sigla.

## Material Visual

- Cuadros/tablas/imágenes numerados al final del documento
- Imágenes en archivo aparte: JPG o TIFF, 300 dpi, 240 px
- Indicar ubicación en texto: `[Insertar Cuadro 1 aquí]`
- Permisos de publicación gestionados por los autores

## Herramientas de Desarrollo

- **Escritura**: Markdown (draft) → Word (entrega)
- **Referencias**: BibTeX (.bib) → conversión a Chicago Author-Date
- **Validación**: scripts en `scripts/` para verificar estructura, citas, extensión
- **Figuras**: `figures/` (dibujos de casas del investigador y participantes)

## Decisiones Técnicas Clave

| Decisión | Razón |
|---|---|
| Markdown para drafts | Versionado con git, compatible con el framework SDD |
| Chicago Author-Date | Requisito obligatorio de la RES |
| BibTeX como fuente de verdad | Permite validación automática contra CrossRef/DOI |

---
_Actualizado: 2026-03-31_
