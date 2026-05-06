# Research & Design Decisions

## Summary
- **Feature**: `paper-memorias-casas-piernas-res100`
- **Discovery Scope**: Extension (esbozo existente → manuscrito completo para RES)
- **Key Findings**:
  - El esbozo actual tiene ~1.200 palabras; necesita expandirse a 7.000-10.000 (factor 6-8x)
  - Las referencias actuales son 7; se necesitan al menos 20 verificables, con énfasis en autores latinoamericanos
  - El formato de citas del esbozo es APA 7; debe migrarse a Chicago autor-fecha (RES)
  - El material visual disponible (5 carpetas de dibujos + 3 obras del autor) es suficiente para 3-6 figuras

## Research Log

### Análisis del gap entre esbozo actual y requisitos RES
- **Context**: Evaluar qué secciones del esbozo necesitan mayor desarrollo
- **Sources Consulted**: `temp_context/paper_Erwin_23_Junio_2025.md`, `temp_context/normas.md`
- **Findings**:
  - Título: existe en español, falta versión en inglés
  - Resumen: existe (~120 palabras), necesita expandirse a 250-300 y traducirse al inglés
  - Introducción: existe (~200 palabras), necesita gap explícito, hipótesis, alcance, más citas
  - Marco teórico: no existe como sección independiente; está mezclado con la introducción y discusión
  - Metodología: existe (~250 palabras), necesita más detalle (criterios de selección, ética, fundamentación teórica de técnicas)
  - Resultados: etiquetados como "esperados (supuesto)", necesitan convertirse en resultados reales con evidencia
  - Discusión: existe (~300 palabras), necesita limitaciones, más diálogo con literatura, contribución explícita
  - Conclusión: existe (~100 palabras), necesita mayor desarrollo
  - Referencias: 7 en APA, necesitan migrar a Chicago autor-fecha y expandirse a ≥20
- **Implications**: Se requiere un trabajo sustancial de expansión y reestructuración, no solo edición cosmética

### Formato de citas Chicago autor-fecha (RES)
- **Context**: La RES usa Chicago Manual of Style "Author-Date", no APA
- **Sources Consulted**: `temp_context/normas.md` (sección "Reglas de edición")
- **Findings**:
  - Cita en texto: (Apellido año, página) → ej. (Bachelard 1957, 34)
  - Bibliografía: Apellido, Nombre. Año. *Título*. Ciudad: Editorial.
  - No se permite op. cit., ibid. ni ibidem
  - DOI obligatorio cuando existe
  - Relación 1:1 entre citas en texto y bibliografía
  - Nombres completos de autores/editores obligatorios
- **Implications**: Todas las referencias del esbozo deben reformatearse; las nuevas deben crearse directamente en Chicago

### Material visual disponible
- **Context**: Evaluar el material visual para seleccionar figuras del manuscrito
- **Sources Consulted**: `temp_context/README.md`, carpetas `Dibujos casas/` y `arte-autor/`
- **Findings**:
  - 5 "casas de paso" con bitácoras y dibujos de participantes (variedad de perfiles: Daniel, Isabel, Norma Romero)
  - 3 obras del autor: Caminante (metáfora central), Casa_Padre (herencia habitacional), La_mudanza (acto de mudarse)
  - Formatos originales: PDF convertidos a PNG (participantes), JPG (autor)
  - RES requiere: JPG o TIFF, 300 DPI, 240 píxeles mínimo
- **Implications**: Seleccionar 4-5 figuras representativas; verificar resolución; preparar pies de figura descriptivos

### Alineación con convocatoria RES #100
- **Context**: Maximizar pertinencia temática para la convocatoria
- **Sources Consulted**: `temp_context/Convocatoria revista.md`
- **Findings**:
  - Eje directo: "migración, desplazamiento y frontera" como problema contemporáneo
  - Eje metodológico: "metodologías clásicas y emergentes" (investigación-creación como metodología emergente)
  - Eje epistémico: "producción del conocimiento" desde América Latina (Santiago como laboratorio migratorio)
  - La convocatoria valora enfoques transdisciplinares (arte + antropología + ciencias sociales)
- **Implications**: El paper debe posicionarse explícitamente como contribución desde las ciencias sociales latinoamericanas, no solo como proyecto artístico

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos / Limitaciones | Notas |
|--------|-------------|-----------|---------------------|-------|
| IMRaD estándar | Estructura clásica de artículo científico | Compatible con RES, familiar para evaluadores | Puede limitar la dimensión artística/creativa | Opción seleccionada; el marco teórico se integra como sección separada antes de metodología |
| Narrativa artística | Estructura libre siguiendo la metáfora de las casas | Coherente con investigación-creación | Riesgo de rechazo por no cumplir estándares académicos | Descartada para la revista; viable para publicación artística |
| Híbrida IMRaD+visual | IMRaD con secciones visuales intercaladas | Combina rigor y creatividad | Puede exceder el límite de palabras | Elementos visuales se integran como figuras dentro de IMRaD |

## Design Decisions

### Decisión: Estructura del manuscrito
- **Context**: El esbozo mezcla secciones; necesita reorganización para cumplir IMRaD
- **Alternatives Considered**:
  1. IMRaD puro con marco teórico embebido en introducción
  2. IMRaD extendido con sección de marco teórico/revisión de literatura independiente
- **Selected Approach**: IMRaD extendido con marco teórico como sección propia entre introducción y metodología
- **Rationale**: La investigación-creación requiere fundamentación teórica explícita que no cabe en la introducción sin hacerla excesiva; la RES acepta esta variación
- **Trade-offs**: Mayor extensión, pero mejor fundamentación conceptual
- **Follow-up**: Verificar que el total no exceda 10.000 palabras

### Decisión: Distribución de palabras por sección
- **Context**: Necesitamos planificar la extensión de cada sección dentro del rango 7.000-10.000
- **Selected Approach**: Distribución objetivo (~8.500 palabras total):
  - Título + resúmenes + keywords: ~700 palabras
  - Introducción: ~1.000 palabras
  - Marco teórico: ~1.500 palabras
  - Metodología: ~1.200 palabras
  - Resultados: ~1.800 palabras
  - Discusión: ~1.200 palabras
  - Conclusión: ~400 palabras
  - Referencias: ~700 palabras (~20-25 entradas)
- **Rationale**: Prioriza resultados (sección más débil del esbozo) y marco teórico (inexistente)
- **Trade-offs**: Algunas secciones podrían necesitar ajuste según la evidencia disponible

### Decisión: Selección de figuras
- **Context**: Se dispone de 8 fuentes visuales; la RES permite un número moderado
- **Selected Approach**: 5 figuras seleccionadas:
  1. Caminante (obra autor) — metáfora central del paper
  2. Casa de paso 2 (participante) — contraste casa origen vs. casa soñada
  3. Casa de paso 3 (Isabel, Florón) — hogar como bienestar colectivo
  4. Casa de paso 5 (Norma Romero, venezolana) — identidad y memoria
  5. Casa_Padre (obra autor) — herencia habitacional como carga y raíz
- **Rationale**: Equilibrio entre obras del autor (2) y dibujos de participantes (3); representatividad de perfiles migrantes; pertinencia para los arquetipos de casas narrativas
- **Trade-offs**: Se excluyen Casa de paso 1 (bitácora escrita, no visual) y Casa de paso 4 (similar temática a otros); La_mudanza se reserva como alternativa

## Risks & Mitigations
- Extensión insuficiente: el esbozo es muy breve → mitigación: distribución detallada por sección con mínimos obligatorios
- Referencias no verificables: algunas citas del esbozo podrían no tener DOI → mitigación: validar cada referencia contra CrossRef/Semantic Scholar antes de incluirla
- Resolución de imágenes insuficiente: archivos convertidos de PDF a PNG → mitigación: verificar DPI y dimensiones; solicitar originales si necesario
- Anonimato de participantes: algunas bitácoras incluyen nombres y datos → mitigación: verificar consentimiento; usar pseudónimos donde no haya autorización explícita
- Exceso de palabras: marco teórico nuevo + expansión de resultados → mitigación: monitorear conteo total durante la escritura

## References
- [Chicago Manual of Style Author-Date](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html) — formato de citas requerido por la RES
- [RES Normas para autores](https://res.uniandes.edu.co) — normas editoriales completas
- Bachelard, G. (1957). *La poétique de l'espace* — referencia fundacional sobre habitar
- Taylor, D. (2003). *The Archive and the Repertoire* — marco teórico para arte como archivo
- Ahmed, S. (1999). *Home and away* — objetos de orientación afectiva en migración
