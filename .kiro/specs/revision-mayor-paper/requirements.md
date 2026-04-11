# Requirements Document

## Introduction

Este spec aborda la revisión mayor del paper "Redes sociales y migración: resignificación comunicativa en contextos transnacionales" para resolver las debilidades identificadas en el reporte de peer-review (`paper/review-report.md`). El objetivo es llevar el manuscrito a un estado publicable en REIS, resolviendo inconsistencias de alcance, fortaleciendo la metodología, mejorando la base de evidencia y ajustando el tono epistemológico.

## Requirements

### Requirement 1: Coherencia entre alcance declarado y evidencia disponible

**Objective:** Como autor, quiero que el alcance declarado del paper sea consistente con la evidencia que lo sustenta, para que no haya brecha entre las promesas del abstract/introducción y los hallazgos reportados.

#### Acceptance Criteria

1. The paper shall declarar un alcance de revisión amplio (migración transnacional y redes sociales) con foco interpretativo en el caso chileno (venezolanos/colombianos), sin prometer un análisis exclusivo de esa población.
2. When el abstract menciona la población de estudio, the paper shall indicar que la revisión sintetiza evidencia internacional con énfasis en implicaciones para el corredor Venezuela-Colombia-Chile.
3. When la introducción formula los objetivos, the paper shall distinguir entre el objetivo de síntesis general y el objetivo de identificar lagunas específicas para el contexto chileno.
4. When la conclusión reporta hallazgos, the paper shall usar lenguaje que distinga explícitamente entre evidencia directa (estudios en Chile) y evidencia extrapolada (estudios en otros contextos con implicaciones para Chile).
5. If no existe evidencia directa suficiente sobre una plataforma en el contexto chileno, the paper shall señalarlo como laguna en lugar de extrapolar sin advertencia.

### Requirement 2: Fortalecimiento metodológico con estándares PRISMA 2020

**Objective:** Como autor, quiero que la sección metodológica cumpla con las directrices PRISMA 2020 para revisiones sistemáticas, para que el paper sea aceptable en revistas indexadas.

#### Acceptance Criteria

1. The paper shall incluir un diagrama PRISMA 2020 (como figura o descripción estructurada) con los flujos de identificación, filtrado, elegibilidad e inclusión.
2. The paper shall reportar las cadenas de búsqueda exactas tal como se ingresaron en cada base de datos (Scopus, Web of Science, Google Scholar).
3. The paper shall reportar las fechas exactas en que se realizaron las búsquedas.
4. The paper shall explicitar el método de síntesis utilizado (análisis temático, framework synthesis, o equivalente).
5. The paper shall declarar si hubo más de un revisor en el proceso de selección y cómo se resolvieron discrepancias.
6. The paper shall incluir una evaluación de calidad o riesgo de sesgo de los estudios incluidos, o justificar explícitamente por qué no se realizó.
7. Where se mencione el número total de artículos del corpus (163), the paper shall proporcionar una lista completa como material suplementario o apéndice.

### Requirement 3: Reemplazo de fuentes no académicas por evidencia revisada por pares

**Objective:** Como autor, quiero que todas las claims centrales del paper estén respaldadas por fuentes académicas revisadas por pares, para cumplir los estándares de REIS.

#### Acceptance Criteria

1. The paper shall reemplazar o complementar la referencia "García, en NPR, 2021" con estudios académicos que documenten los mismos fenómenos (uso de Facebook por migrantes para información sobre rutas).
2. The paper shall identificar la referencia completa de "Publicación sobre migrantes colombianos en Chile, s.f." de donde provienen los testimonios de Cecilia y José, o reemplazarla por una fuente verificable.
3. If se mantienen fuentes periodísticas, the paper shall usarlas únicamente como ilustración complementaria, nunca como evidencia principal de una claim.
4. When se cita un testimonio directo de un migrante, the paper shall proveer la referencia académica completa (autor, año, revista, DOI) de donde fue extraído.
5. The paper shall no contener citas del tipo "Publicación sobre X, s.f." ni referencias con datos incompletos en el texto.

### Requirement 4: Análisis bibliométrico del corpus

**Objective:** Como autor, quiero incluir un análisis bibliométrico básico del corpus de 163 artículos, para que el lector pueda evaluar la representatividad de los hallazgos.

#### Acceptance Criteria

1. The paper shall incluir una tabla o figura con la distribución del corpus por año de publicación.
2. The paper shall incluir la distribución del corpus por plataforma estudiada (WhatsApp, Facebook, YouTube, Instagram, TikTok, múltiples).
3. The paper shall incluir la distribución por región geográfica o contexto migratorio (norte global, sur global, intrarregional).
4. The paper shall incluir la distribución por tipo de población migrante (nacionalidad o categoría: refugiados, migrantes económicos, etc.).
5. The paper shall incluir la distribución por metodología empleada en los estudios (cualitativa, cuantitativa, mixta, revisión).
6. When se presentan hallazgos por categoría de análisis, the paper shall indicar cuántos estudios del corpus contribuyen a cada categoría.

### Requirement 5: Reformulación del lenguaje epistemológico

**Objective:** Como autor, quiero que el paper use lenguaje cauteloso apropiado para una revisión de literatura, para evitar afirmaciones que excedan lo que la evidencia permite concluir.

#### Acceptance Criteria

1. The paper shall no usar la formulación "confirma la hipótesis" en ninguna sección; en su lugar usará expresiones como "la evidencia es consistente con", "los hallazgos sugieren que", "la literatura respalda".
2. The paper shall reformular la hipótesis central como pregunta de investigación o como proposición teórica a explorar, no como enunciado a confirmar.
3. When se reportan hallazgos de la revisión, the paper shall distinguir entre evidencia fuerte (múltiples estudios convergentes), evidencia moderada (algunos estudios) y evidencia incipiente (pocos estudios o de un solo contexto).
4. The paper shall no presentar la tipología propuesta como "confirmada" sino como "derivada de la síntesis" o "emergente del análisis".
5. If una claim se basa en un solo estudio o en estudios de un único contexto, the paper shall señalar esta limitación al presentar la claim.

### Requirement 6: Verificación y completitud de referencias

**Objective:** Como autor, quiero que todas las referencias del .bib estén verificadas contra bases de datos bibliográficas y completas, para garantizar la integridad del aparato citacional.

#### Acceptance Criteria

1. When una referencia tiene la nota "pendiente de verificación", the paper shall verificarla contra CrossRef, Semantic Scholar o la fuente correspondiente y actualizar el campo `note`.
2. The paper shall incluir DOI para toda referencia que disponga de uno.
3. The paper shall no contener entradas .bib con campos obligatorios vacíos o incompletos (journal, volume, pages para artículos; publisher para libros).
4. If una referencia no puede ser verificada (no existe en bases de datos), the paper shall eliminarla y reemplazar la cita en el texto por una fuente alternativa verificable.
5. The paper shall asegurar que toda referencia citada en el texto exista en el .bib, y que no haya entradas huérfanas en el .bib sin cita en el texto.
