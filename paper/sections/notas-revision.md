# Notas de Revisión y Validación (Post-Bibliografía)

<!-- STATUS: pending-author-review -->
<!-- Estas notas se han generado automáticamente tras la validación técnica del paper el 2026-04-05 -->
<!-- Actualización 2026-04-07: añadidas observaciones de /paper:validate y estado actualizado de figuras -->

## 1. Observaciones Críticas (Bloqueantes)

*   **Inconsistencia de "Daniel" (Discusión vs. Resultados):** 
    *   En la sección `discussion.md` (línea 19), se menciona específicamente "El caso de la madre de Daniel" para ilustrar las migraciones invisibles.
    *   **Problema:** En la sección `results.md`, todos los participantes están anonimizados mediante números (ej: Participante 7, Participante 50) y no existe ninguna referencia a un caso llamado "Daniel" o "la madre de Daniel".
    *   **Acción requerida:** El autor debe decidir si:
        1. Se identifica el número de participante correspondiente a "Daniel" y se cambia el nombre en la discusión por dicho número (ej: "El caso de la madre de la Participante 50").
        2. Se añade el fragmento del relato de "Daniel" en la sección de Resultados para que la cita en la Discusión tenga sustento empírico previo.

## 2. Pendientes de Formato y Estructura

*   **Metadatos de Procedencia:** 
    *   En `paper/metadata.yaml`, los campos bajo `procedencia:` (nombre del proyecto e institución financiadora) están marcados como `[PENDIENTE]`.
    *   **Acción requerida:** Completar antes del envío final para cumplir con el requisito 1.8 de la RES.

*   **Conversión de Figuras (actualizado 2026-04-07):**
    *   Los archivos ya fueron copiados a `figures/` con nomenclatura final:
        - `figura-1.png`, `figura-2.png`, `figura-3.png` (dibujos de participantes, exportados desde los PDF de `temp_context/Dibujos casas/`).
        - `figura-4.jpg`, `figura-5.jpg`, `figura-6.jpg` (ilustraciones del autor, copiadas desde `temp_context/arte-autor/`).
    *   **Acción requerida pendiente:** verificar que cada archivo cumpla las normas RES (JPG o TIFF, 300 dpi, 240 píxeles). Las Figuras 1-3 están en PNG y deberán convertirse a JPG/TIFF antes del envío final; las Figuras 4-6 deben verificarse en resolución y reexportarse si no alcanzan los 300 dpi. Los marcadores `[Insertar Figura X aquí]` ya están correctamente posicionados en el texto.

*   **Conteo de palabras por sección bajo target (validación 2026-04-07):**
    *   `marco-teorico.md`: 1.323/1.500 palabras (88% del target). Espacio natural para ampliar el cierre del "Vacío de investigación" o el eje de Investigación-creación latinoamericana.
    *   `results.md`: 1.744/2.000 palabras (87% del target). Espacio natural para añadir uno o dos fragmentos adicionales de bitácora en Casa Contemporánea o Casa Universo Paralelo, o ampliar el análisis transversal.
    *   **Nota:** ambas secciones están sobre el umbral del 50% y el conteo total del manuscrito (~9.420 palabras) sigue dentro del rango RES (7.000-10.000), por lo que no son bloqueantes.

*   **Metadato pendiente en figuras:** confirmar con el autor el año de creación de las Figuras 4, 5 y 6 (`Caminante`, `Casa_Padre`, `La_mudanza`) antes del envío final, según lo registrado en `figures/catalogo-figuras.md`.

## 3. Resumen de Validaciones Exitosas (Hard Specs)

*   **Conteo de Palabras:** 8.200 palabras totales (Cumple el rango 7.000-10.000).
*   **Abstracts:** Versiones en español e inglés dentro de los límites (250-300 palabras).
*   **Referencias:** 24 entradas en `references.bib`, todas citadas correctamente en el texto siguiendo el estilo Chicago Author-Date.
*   **Estructura:** Las 7 secciones requeridas por la RES están completas y alineadas con el `outline.md`.

---
**Fecha de validación:** 5 de abril de 2026
**Estado del manuscrito:** Draft con observaciones pendientes.
