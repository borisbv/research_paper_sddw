# Research & Design Decisions — Memorias de casas con piernas

## Summary
- **Feature**: memorias-casas-piernas
- **Discovery Scope**: Extension (paper borrador existente → manuscrito RES completo)
- **Key Findings**:
  1. El paper de Erwin tiene estructura narrativa sólida pero requiere reestructuración IMRaD completa, expansión argumentativa y citaciones formales Chicago Author-Date
  2. La convocatoria RES #100 ofrece dos ejes de encaje directo: "migración, desplazamiento y frontera" y "metodologías clásicas y emergentes"
  3. La bibliografía actual (7 referencias) necesita ampliarse a 20-30, incorporando investigación-creación latinoamericana, fenomenología del habitar y estudios migratorios contemporáneos

## Research Log

### Estructura editorial RES vs. estado actual
- **Context**: Verificar qué tan lejos está el borrador de cumplir las normas RES
- **Sources Consulted**: normas.md, convocatoria RES, metadata.yaml, paper_Erwin_23_Junio_2025.md
- **Findings**:
  - El borrador tiene ~1.500 palabras; el target es 7.000-10.000
  - Falta resumen extendido bilingüe (250-300 palabras cada uno)
  - Falta marco teórico como sección independiente
  - La sección de resultados está como "resultados esperados (supuesto)" — debe formalizarse con evidencia real
  - No hay notas a pie de página ni formato de citas Chicago Author-Date
  - Faltan: título en inglés, palabras clave en inglés, archivo de datos del autor, información de procedencia
- **Implications**: Cada sección necesita escritura desde cero, usando el borrador como fuente de ideas y fragmentos pero no como texto base

### Formato de citación Chicago Author-Date
- **Context**: La RES exige estrictamente Chicago Author-Date (última edición). El borrador usa APA 7
- **Sources Consulted**: normas.md (ejemplos detallados de formato)
- **Findings**:
  - En texto: (Apellido año, página) — ej: (Bachelard 1957, 56)
  - En bibliografía: Apellido, Nombre. Año. *Título*. Ciudad: Editorial.
  - Artículos: Apellido, Nombre. Año. "Título". *Revista* volumen (No.): páginas. DOI.
  - Prohibido: op. cit., ibid., ibidem
  - Nombres completos obligatorios
  - DOI obligatorio cuando disponible
  - Relación 1:1 entre citas en texto y bibliografía
- **Implications**: Todas las entradas .bib deben revisarse para completar campos (DOI, ciudad, páginas). Las citas en texto deben convertirse de APA a Chicago

### Convocatoria RES #100 — Ejes de encaje
- **Context**: Maximizar pertinencia para la convocatoria
- **Sources Consulted**: Convocatoria revista.md
- **Findings**:
  - Eje principal: "Problemas contemporáneos: migración, desplazamiento y frontera"
  - Eje secundario: "Metodologías clásicas y emergentes" (investigación-creación como metodología emergente)
  - Eje terciario: "Tensiones entre teoría y práctica" (la investigación-creación encarna esta tensión)
  - La convocatoria valora explícitamente: enfoque transdisciplinar, reflexión sobre hacer ciencias sociales desde América Latina, diálogos entre lo local y lo global
- **Implications**: La introducción y discusión deben vincular explícitamente con estos ejes. La investigación-creación como metodología emergente es un argumento fuerte de pertinencia

### Material visual — Dibujos "Casa de paso"
- **Context**: Integración de 5 PDFs de dibujos como figuras formales
- **Sources Consulted**: temp_context/Dibujos casas/, normas RES sobre figuras
- **Findings**:
  - 5 archivos PDF disponibles: Casa de paso 1-5
  - RES requiere: JPG o TIFF, 300 dpi, 240 px, al final del documento
  - Deben referenciarse como [Insertar Figura N aquí] en el texto
  - Se necesitan permisos de publicación
  - Los dibujos deben ser parte constitutiva del argumento, no mera ilustración
- **Implications**: Se necesita un paso de conversión PDF→JPG/TIFF. Los dibujos se integran en la sección de Resultados y se interpretan en la Discusión

### Gap bibliográfico
- **Context**: La bibliografía actual tiene 7 referencias; se necesitan 20-30
- **Sources Consulted**: references.bib, requirements.md
- **Findings**:
  - Referencias actuales cubren: Bachelard, Ahmed, Bajani, De Certeau/Giard, Sturken, Taylor, Tronto
  - Faltan áreas temáticas: Heidegger (habitar), Brah (diáspora), investigación-creación en Latinoamérica, estudios migratorios en Chile, dibujo proyectivo, metodologías artísticas en ciencias sociales
  - Se necesitan al menos 8-13 referencias adicionales con DOI verificable
- **Implications**: Se requiere búsqueda bibliográfica dirigida antes de la escritura de cada sección

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos/Limitaciones | Notas |
|--------|-------------|-----------|---------------------|-------|
| IMRaD estricto | Estructura clásica con secciones separadas | Cumple norma RES, familiar para evaluadores | Puede rigidizar el tono artístico del paper | Adaptado con "Marco teórico" como sección propia |
| Narrativo-ensayístico | Estructura más libre, tipo ensayo | Más afín al tono del borrador | No cumple norma RES para artículos de investigación | Descartado |
| IMRaD adaptado con voz artística | IMRaD con registro que integre lo poético | Cumple norma + mantiene identidad del paper | Requiere balance cuidadoso | **Seleccionado** |

## Design Decisions

### Decision: Estructura IMRaD adaptada con voz artística
- **Context**: El paper es investigación-creación, no investigación cuantitativa pura. El borrador tiene un tono poético-narrativo valioso.
- **Alternatives Considered**:
  1. IMRaD estricto con tono académico formal puro
  2. Estructura ensayística libre
- **Selected Approach**: IMRaD adaptado que mantiene rigor académico pero incorpora fragmentos narrativos y poéticos del borrador en puntos estratégicos (epígrafes, citas de bitácoras, transiciones)
- **Rationale**: La RES acepta artículos de investigación-creación. El tono artístico es parte constitutiva del argumento, no un adorno. Mantenerlo demuestra coherencia metodológica.
- **Trade-offs**: Requiere más revisión para asegurar que el tono poético no comprometa la claridad académica
- **Follow-up**: Validar con el autor que el equilibrio tonal es adecuado

### Decision: Distribución de palabras por sección
- **Context**: 7.000-10.000 palabras totales incluyendo resúmenes, bibliografía y notas
- **Selected Approach**:
  - Resumen ES + EN: ~600 palabras
  - Introducción: ~1.500 palabras
  - Marco teórico: ~1.500 palabras
  - Metodología: ~1.500 palabras
  - Resultados: ~2.000 palabras
  - Discusión: ~1.500 palabras
  - Conclusión: ~500 palabras
  - Bibliografía + notas: ~900 palabras
  - **Total estimado: ~10.000 palabras** (máximo permitido)
- **Rationale**: Resultados necesita más espacio por los 5 arquetipos + fragmentos de bitácoras + referencias a figuras
- **Trade-offs**: Puede requerir recortes si las notas al pie se extienden

### Decision: Estrategia de ampliación bibliográfica
- **Context**: De 7 a 20-30 referencias
- **Selected Approach**: Búsqueda dirigida por sección, priorizando:
  1. Marco teórico: Heidegger, Brah, autores de investigación-creación latinoamericana
  2. Metodología: dibujo proyectivo, cartografía afectiva, ética de investigación con migrantes
  3. Discusión: estudios migratorios en Chile, arte y memoria en Latinoamérica
- **Rationale**: Las referencias deben servir al argumento, no rellenar bibliografía
- **Follow-up**: Verificar cada referencia contra CrossRef/DOI antes de incluir en .bib

## Risks & Mitigations
- **Riesgo 1: Extensión insuficiente** — El borrador tiene ~1.500 palabras para un target de 7.000-10.000. Mitigación: el outline detallado por sección asegura cobertura temática suficiente.
- **Riesgo 2: Tono inconsistente** — Mezclar registro poético y académico puede resultar disonante. Mitigación: definir reglas claras de cuándo y dónde usar cada registro.
- **Riesgo 3: Referencias no verificables** — Algunas fuentes del borrador podrían no tener DOI. Mitigación: verificar cada referencia contra CrossRef antes de incluir; marcar las no verificables.
- **Riesgo 4: Material visual insuficiente** — Los PDFs podrían no cumplir requisitos técnicos de resolución. Mitigación: convertir y verificar calidad antes de enviar.
- **Riesgo 5: Deadline agosto 2026** — Amplio pero requiere coordinación con el autor para datos faltantes (afiliación, consentimientos). Mitigación: crear checklist de información pendiente del autor.

## References
- Normas RES: `temp_context/normas.md`
- Convocatoria RES #100: `temp_context/Convocatoria revista.md`
- Paper borrador Erwin: `temp_context/paper_Erwin_23_Junio_2025.md`
- Chicago Manual of Style Author-Date: formato detallado en normas.md
