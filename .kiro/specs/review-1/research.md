# Research & Design Decisions — review-1

---
**Feature**: `review-1` — Revisión mayor del paper *Memorias de casas con piernas*
**Discovery Scope**: Extension (revisión de contenido de un manuscrito académico existente)
**Key Findings**:
- Todos los problemas a resolver son ediciones en archivos Markdown ya existentes; no se requieren nuevas dependencias ni herramientas externas.
- El estado actual del manuscrito (total ~9.420 palabras según `notas-revision.md`) tiene margen limitado para expansión antes de alcanzar el techo de 10.000 palabras de RES: el espacio disponible es ~580 palabras distribuibles entre todas las adiciones requeridas.
- La resolución del Requisito 1 (Daniel) es prerequisito bloqueante para los Requisitos 4 y 5, porque el fragmento empírico de ese participante es simultáneamente la evidencia que falta en Casa Contemporánea (Req 5) y el soporte empírico de "migraciones invisibles" (Req 4).

---

## Research Log

### Inventario de archivos del manuscrito

- **Context**: Identificar exactamente qué archivos modificar y sus conteos actuales.
- **Findings**:
  - `paper/sections/introduction.md` — ~1.480 palabras — Contiene Figura 4 (ilustración del autor)
  - `paper/sections/marco-teorico.md` — 1.323 palabras (target 1.500; déficit ~177 palabras)
  - `paper/sections/methodology.md` — 1.524 palabras (target 1.500; ~24 palabras sobre target)
  - `paper/sections/results.md` — 1.744 palabras (target 2.000; déficit ~256 palabras)
  - `paper/sections/discussion.md` — 1.512 palabras — Contiene referencia a "Daniel" sin respaldo empírico
  - `paper/sections/conclusion.md` — 527 palabras
  - `paper/sections/abstract.md` — ~288 palabras ES / ~271 palabras EN
  - `paper/metadata.yaml` — campos `procedencia` marcados como `[PENDIENTE]`
  - `figures/catalogo-figuras.md` — año de Figuras 4-6 pendiente de confirmar
- **Implications**: Las adiciones de palabras en Metodología deben ser mínimas (~50 palabras) para no superar la banda 1.500-1.700 establecida en el Requisito 2.6. Las adiciones en Resultados y Marco teórico tienen más margen pero están acotadas por el techo de 10.000 palabras del total.

### Restricción de palabras totales

- **Context**: El manuscrito tiene ~9.420 palabras totales; el límite de RES es 10.000.
- **Findings**:
  - Presupuesto de expansión disponible: ~580 palabras en total para todas las adiciones.
  - Distribución recomendada:
    - Req 1 + 4 (fragmento Daniel + desarrollo "migraciones invisibles"): ~150 palabras en Results + ~100 palabras en Discussion = 250 palabras
    - Req 2 (transparencia analítica en Metodología): ~100 palabras
    - Req 3 (etiquetas figuras + nota en Metodología): ~80 palabras
    - Req 5 (ampliación Marco teórico): ~150 palabras restantes
    - Total estimado: ~580 palabras — dentro del presupuesto
- **Implications**: No hay espacio para expansión generosa; cada adición debe ser precisa y sin relleno. Si al implementar se supera el presupuesto, se deberá compensar reduciendo en secciones más largas (discussion.md o conclusion.md).

### Dependencias entre requisitos

- **Context**: Determinar el orden seguro de implementación para evitar retrabajo.
- **Findings**:
  - **Req 1 → Req 4**: La evidencia empírica de "migraciones invisibles" en Discussion depende del fragmento de Daniel que se añade en Results (Req 1).
  - **Req 1 → Req 5**: El fragmento de Daniel añadido en Casa Contemporánea cuenta parcialmente hacia el déficit de palabras en Results.
  - **Req 2, Req 3, Req 5 (marco-teorico), Req 6**: Son independientes entre sí y pueden implementarse en paralelo.
- **Implications**: El orden de implementación seguro es: [Req 1 primero] → [Req 4 segundo] → [Req 2, Req 3, Req 5, Req 6 en cualquier orden].

### Patrón de pies de figura existente

- **Context**: Entender el formato actual de los pies de figura para diseñar la diferenciación epistémica (Req 3).
- **Findings**:
  - Figuras de participantes (1-3): incluyen nombre o número de participante, instrumento ("Dibujo proyectivo"), materiales, año y "Reproducido con consentimiento informado."
  - Figuras del autor (4-6): incluyen título de la obra, nombre del autor, técnica y "Archivo plástico del investigador." Sin indicación explícita de que no son dato empírico.
- **Implications**: La diferenciación se logra añadiendo una frase estandarizada al final de los pies de Figuras 4-6: "Pertenece al archivo plástico del investigador; no constituye dato empírico del trabajo de campo." Esta frase es consistente con el lenguaje ya usado en `discussion.md` para introducir esas figuras.

---

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos |
|--------|-------------|------------|---------|
| Edición local por sección | Modificar cada archivo `.md` de forma independiente | Bajo riesgo, reversible con git | Posible falta de coherencia entre secciones si no se revisan juntas |
| Reescritura de secciones completas | Reemplazar secciones enteras | Control total | Alto riesgo de perder texto aprobado; exceso de cambios |
| Edición quirúrgica en puntos precisos | Insertar/modificar solo los párrafos afectados | Mínimo impacto, alta trazabilidad | Requiere instrucciones de posicionamiento muy precisas |

**Seleccionado**: Edición quirúrgica en puntos precisos. Cada intervención tiene una ubicación textual definida, un volumen de palabras presupuestado y deja intacto el resto del texto aprobado.

---

## Design Decisions

### Decisión: Anonimización de Daniel por número de participante

- **Context**: El autor confirma que "Daniel" es un participante numerado del corpus.
- **Alternatives Considered**:
  1. Mantener "Daniel" como pseudónimo con nota de consentimiento explícita.
  2. Reemplazar "Daniel" por el número de participante (ej. "Participante X").
- **Selected Approach**: Reemplazar el nombre propio por número de participante, consistente con el patrón de anonimización ya usado en el resto del corpus.
- **Rationale**: El protocolo ético del estudio usa anonimización por número; usar un pseudónimo crearía inconsistencia con los 60 participantes restantes y podría requerir documentación adicional de consentimiento.
- **Trade-offs**: El número de participante es menos "legible" narrativamente que un nombre, pero garantiza coherencia metodológica.
- **Follow-up**: El autor debe confirmar el número de participante exacto antes de la implementación.

### Decisión: Posición del fragmento de Daniel en Results

- **Context**: El fragmento debe aparecer antes de la mención en Discussion para que haya trazabilidad.
- **Selected Approach**: Insertar el fragmento dentro de la subsección **Casa Contemporánea** de `results.md`, después del último testimonio actual (Participante 35) y antes del párrafo analítico que cierra esa subsección.
- **Rationale**: Casa Contemporánea ya incluye desplazamientos recientes sin especificidad de trauma histórico; el caso de migración interna de Daniel encaja en ese arquetipo.
- **Follow-up**: Verificar que el fragmento tenga etiqueta de instrumento correcto (bitácora o diálogo simbólico).

### Decisión: Nota de diferenciación epistémica de figuras

- **Context**: Dos tipos de material visual (evidencia empírica vs. obra autoral) están entremezclados en el texto.
- **Selected Approach**: Añadir una frase estandarizada en los pies de Figuras 4-6 + una nota corta en la sección de Metodología (antes de la subsección de Consideraciones éticas).
- **Rationale**: Es la intervención mínima que resuelve la ambigüedad sin restructurar el texto. No requiere mover la Figura 4 de la Introducción (el autor puede tomar esa decisión; el requisito 3.5 es condicional).
- **Trade-offs**: No cambia el diseño visual del paper, solo añade texto aclaratorio.

---

## Risks & Mitigations

- **Riesgo: Superación del techo de 10.000 palabras** — Mitigación: presupuesto de ~580 palabras distribuido explícitamente en el diseño; implementar con conteo incremental.
- **Riesgo: Número de participante de "Daniel" desconocido** — Mitigación: el diseño bloquea Req 1 en gate de autor; sin ese dato no se puede ejecutar la tarea.
- **Riesgo: Fragmento de Daniel no disponible digitalmente** — Mitigación: si el fragmento no está transcrito, el autor debe transcribirlo del corpus físico antes de la tarea de implementación.
- **Riesgo: Figura 4 en Introducción interrumpe flujo argumentativo** — Mitigación: el Requisito 3.5 es condicional ("the Paper shall evaluar"); la decisión de moverla o no queda al criterio del autor.

---

## References

- `paper/review-report.md` — Reporte de revisión que originó este spec (7 de abril de 2026)
- `paper/sections/notas-revision.md` — Validación técnica previa (5 de abril de 2026)
- `paper/metadata.yaml` — Metadatos del manuscrito y requisitos formales de RES
- Requisitos RES #100: extensión 7.000-10.000 palabras, resúmenes 250-300 palabras, Chicago Author-Date, formato figuras JPG/TIFF 300 dpi
