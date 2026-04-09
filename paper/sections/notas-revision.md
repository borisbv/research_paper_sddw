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

*   **Metadatos de Procedencia (MOCK — REEMPLAZAR ANTES DEL ENVÍO):**
    *   En `paper/metadata.yaml`, los campos bajo `procedencia:` contienen valores **mock en mayúsculas** insertados durante la revisión `review-1` (08-04-2026) para no dejar el manuscrito con marcadores `[PENDIENTE]`:
        - `nota:` `"MOCK — REEMPLAZAR ANTES DEL ENVÍO CON LOS VALORES REALES"`
        - `proyecto:` `"PROYECTO MOCK DE INVESTIGACIÓN-CREACIÓN MEMORIAS DE CASAS CON PIERNAS"`
        - `institucion_financiadora:` `"INSTITUCIÓN FINANCIADORA MOCK"`
    *   **Acción requerida ANTES DEL ENVÍO:** sustituir estos tres valores mock por la información real (nombre exacto del proyecto e institución financiadora, o explícita ausencia de financiamiento). Cumple el requisito 1.8 de la RES solo cuando los valores reales reemplacen los mock.

*   **Conversión de Figuras (actualizado 2026-04-07):**
    *   Los archivos ya fueron copiados a `figures/` con nomenclatura final:
        - `figura-1.png`, `figura-2.png`, `figura-3.png` (dibujos de participantes, exportados desde los PDF de `temp_context/Dibujos casas/`).
        - `figura-4.jpg`, `figura-5.jpg`, `figura-6.jpg` (ilustraciones del autor, copiadas desde `temp_context/arte-autor/`).
    *   **Acción requerida pendiente:** verificar que cada archivo cumpla las normas RES (JPG o TIFF, 300 dpi, 240 píxeles). Las Figuras 1-3 están en PNG y deberán convertirse a JPG/TIFF antes del envío final; las Figuras 4-6 deben verificarse en resolución y reexportarse si no alcanzan los 300 dpi. Los marcadores `[Insertar Figura X aquí]` ya están correctamente posicionados en el texto.

*   **Conteo de palabras por sección bajo target (validación 2026-04-07):**
    *   `marco-teorico.md`: 1.323/1.500 palabras (88% del target). Espacio natural para ampliar el cierre del "Vacío de investigación" o el eje de Investigación-creación latinoamericana.
    *   `results.md`: 1.744/2.000 palabras (87% del target). Espacio natural para añadir uno o dos fragmentos adicionales de bitácora en Casa Contemporánea o Casa Universo Paralelo, o ampliar el análisis transversal.
    *   **Nota:** ambas secciones están sobre el umbral del 50% y el conteo total del manuscrito (~9.420 palabras) sigue dentro del rango RES (7.000-10.000), por lo que no son bloqueantes.

*   **Metadato de figuras (resuelto 08-04-2026):** año de creación confirmado por el autor como **2024-2025** para las Figuras 4, 5 y 6 (`Caminante`, `Casa_Padre`, `La_mudanza`). Actualizado en `figures/catalogo-figuras.md`, `paper/sections/introduction.md` y `paper/sections/discussion.md`.

## 3. Resumen de Validaciones Exitosas (Hard Specs)

*   **Conteo de Palabras:** 8.200 palabras totales (Cumple el rango 7.000-10.000).
*   **Abstracts:** Versiones en español e inglés dentro de los límites (250-300 palabras).
*   **Referencias:** 24 entradas en `references.bib`, todas citadas correctamente en el texto siguiendo el estilo Chicago Author-Date.
*   **Estructura:** Las 7 secciones requeridas por la RES están completas y alineadas con el `outline.md`.

---
**Fecha de validación:** 5 de abril de 2026
**Estado del manuscrito:** Draft con observaciones pendientes.
