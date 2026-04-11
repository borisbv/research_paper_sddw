# Mandatos Fundacionales del Proyecto (GEMINI.md)

Este archivo establece los mandatos operativos, flujos de trabajo y convenciones fundamentales para el desarrollo de papers científicos utilizando el framework de Spec-Driven Development (SDD).

## 0. Principios Fundamentales
- **Cita Obligatoria:** Toda afirmación técnica o fáctica DEBE tener una cita verificable en `references/references.bib`.
- **Estructura Primero:** La estructura del paper debe cumplir con el formato de la revista objetivo ANTES de escribir contenido extenso.
- **Validación Continua:** Cada sección es un módulo. No se considera "terminada" hasta que pase las validaciones automáticas (hard specs).
- **Idioma:** Pensar en Inglés, generar contenido en Español (a menos que el paper requiera Inglés). Todo Markdown en el repositorio DEBE estar en Español.

---

## 1. Reglas Generales y Hooks Automáticos

### 1.1 Validaciones Pre-Commit/Push
Cada vez que se me solicite realizar un `git commit` o `git push`, DEBO ejecutar primero las siguientes validaciones y reportar si fallan:
- `python scripts/validate-structure.py`
- `python scripts/validate-citations.py`
- `python scripts/validate-metadata.py`

### 1.2 Validaciones Post-Edición
- **Secciones del Paper:** Tras editar archivos en `paper/sections/` o `paper/outline.md`, DEBO ejecutar:
  - `python scripts/validate-word-count.py`
  - `python scripts/validate-prose.py`
- **Metadata:** Tras editar `paper/metadata.yaml`, DEBO ejecutar:
  - `python scripts/validate-metadata.py`

---

## 2. Workflows de Gestión de Papers

Cuando el usuario solicite tareas relacionadas con el paper, seguiré estos procedimientos:

### 2.1 Inicializar Paper (paper-init)
**Objetivo:** Crear la estructura SDD completa.
1. Consultar el skill `venue-templates` para obtener el formato de la revista objetivo.
2. Crear directorios: `paper/sections/`, `references/`, `figures/`, `data/`, `scripts/`.
3. Generar `paper/metadata.yaml` y `paper/outline.md` (IMRaD).
4. Crear archivos base en `paper/sections/`.
5. Inicializar specs ejecutando el flujo `kiro:spec-init`.

### 2.2 Citación (paper-cite)
**Objetivo:** Buscar y agregar referencias.
1. Usar `research-lookup` y `citation-management` para encontrar 3-5 papers con DOI.
2. Presentar candidatos al usuario.
3. Tras confirmación, generar entrada BibTeX en `references/references.bib` y proporcionar la clave de citación (ej. `\cite{key}`).

### 2.3 Revisión y Estado (paper-review / paper-status)
- **Review:** Aplicar criterios de peer-review y pensamiento crítico científico para generar `paper/review-report.md`.
- **Status:** Leer `paper/metadata.yaml` y contar palabras/citas en cada sección para generar el reporte visual de progreso.

### 2.4 Validación (paper-validate)
Ejecutar en secuencia:
1. Validación de estructura.
2. Verificación de que cada cita existe en el `.bib`.
3. Validación de límites de palabras.
4. Verificación de existencia de figuras referenciadas.

---

## 3. Workflows de Kiro: Spec-Driven Development (SDD)

### 3.1 Inicialización (spec-init)
Generar nombre de feature único y crear estructura en `.kiro/specs/[feature-name]/`. Crear `spec.json` y `requirements.md` usando los templates en `.kiro/settings/templates/specs/`.

### 3.2 Requisitos (spec-requirements)
Generar requisitos testables en formato EARS basados en la descripción. Los encabezados DEBEN tener IDs numéricos (ej. "1.1"). Cargar siempre el contexto de `.kiro/steering/`.

### 3.3 Diseño Técnico (spec-design)
1. **Discovery:** Ejecutar `design-discovery-full.md` o `light.md` según la complejidad. Realizar búsquedas web de mejores prácticas.
2. **Registro:** Actualizar `research.md` con hallazgos de APIs, riesgos y decisiones.
3. **Documento:** Generar `design.md` con stack tecnológico y contratos de interfaz. No escribir código de implementación.

### 3.4 Tareas y TDD (spec-tasks / spec-impl)
- **Tasks:** Mapear requisitos a tareas de 1-3 horas. Usar IDs numéricos y marcadores `(P)` para paralelismo.
- **Implementation (TDD):** Ciclo obligatorio: RED (Test fallido) -> GREEN (Código mínimo) -> REFACTOR. No implementar nada sin test previo.

---

## 4. Uso de Skills Científicos

Tengo acceso a los siguientes skills en `.gemini/skills/`:
- `citation-management`: Verificación de metadatos y BibTeX.
- `literature-review`: Búsqueda sistemática y síntesis.
- `scientific-writing`: Redacción en párrafos fluidos (prohibido usar bullets en el manuscrito final).
- `research-lookup`: Consultas en tiempo real (Parallel API / Perplexity).
- `scientific-critical-thinking`: Evaluación de rigor y sesgos.
- `venue-templates`: Requisitos de formato por revista/conferencia.

---

## 5. Instrucciones Críticas de Estilo
- **Prosa:** El manuscrito final DEBE ser prosa fluida. Los bullet points son solo para la fase de Outline.
- **Visuales:** Es OBLIGATORIO generar un Graphical Abstract (1200x600px) primero, seguido de esquemas técnicos (mínimo 5 figuras para papers de investigación).
- **Metadata:** Antes de finalizar, DEBO enriquecer el `.bib` buscando volúmenes, páginas o DOIs faltantes en la web.
