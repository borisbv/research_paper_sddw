# Scientific Paper SDD Framework

## Misión
Framework de desarrollo guiado por especificaciones para la escritura rigurosa de papers científicos. Cada sección del paper es tratada como un módulo de software: tiene una spec, se implementa, se valida y se hace merge solo si pasa todas las validaciones.

## Principios
- Toda afirmación debe tener cita verificable
- La estructura debe cumplir el formato de la revista objetivo antes de escribir contenido
- Las referencias se validan contra bases de datos reales (CrossRef, Semantic Scholar, PubMed)
- El proceso es iterativo: spec → draft → validación → revisión → merge
- El humano aprueba en phase gates, no en cada línea

## Workflow SDD para Papers
steering → requirements (revista + tema) → design (outline + specs por sección) → tasks (secciones como tareas atómicas) → implementation (escritura) → validation (checks automáticos)

## Workflow SDD General (cc-sdd)
- Phase 0 (opcional): `/kiro:steering`, `/kiro:steering-custom`
- Phase 1 (Especificación):
  - `/kiro:spec-init "descripción"`
  - `/kiro:spec-requirements {feature}`
  - `/kiro:validate-gap {feature}` (opcional: para codebase existente)
  - `/kiro:spec-design {feature} [-y]`
  - `/kiro:validate-design {feature}` (opcional: revisión de diseño)
  - `/kiro:spec-tasks {feature} [-y]`
- Phase 2 (Implementación): `/kiro:spec-impl {feature} [tasks]`
  - `/kiro:validate-impl {feature}` (opcional: después de implementación)
- Progreso: `/kiro:spec-status {feature}` (en cualquier momento)

## Reglas de Desarrollo
- Flujo de aprobación en 3 fases: Requirements → Design → Tasks → Implementation
- Revisión humana requerida en cada fase; usa `-y` solo para fast-track intencional
- Mantén el steering actualizado y verifica alineación con `/kiro:spec-status`
- Think in English, generate responses in Spanish. All Markdown content written to project files MUST be written in Spanish unless the paper itself requires English.

## Estructura del Paper (IMRaD por defecto)
- Title & Abstract
- Introduction (gap, hipótesis, alcance)
- Related Work / Literature Review
- Methodology
- Results
- Discussion
- Conclusion
- References

## Validaciones Automáticas (Hard Specs)
- [ ] Estructura cumple template de revista objetivo
- [ ] Toda claim tiene citación [N]
- [ ] Todas las referencias en .bib existen en CrossRef/DOI
- [ ] No hay secciones vacías o bajo mínimo de palabras
- [ ] Consistencia terminológica (glosario respetado)
- [ ] Formato de citas correcto (APA/IEEE/Vancouver según revista)
- [ ] Figuras y tablas referenciadas en el texto
- [ ] Abstract dentro del límite de palabras

## Validaciones de Revisión (Soft Specs - requieren humano)
- [ ] Coherencia argumentativa entre secciones
- [ ] Contribución claramente articulada
- [ ] Metodología reproducible
- [ ] Discusión aborda limitaciones
- [ ] Conclusiones soportadas por resultados

## Convenciones
- Archivos del libro/paper en `paper/` (markdown `.md` o Quarto `.qmd`)
- Configuración Quarto en `_quarto.yml` (raíz del proyecto)
- Output compilado en `_book/` (ignorado por git)
- Screenshots de revisión en `_book/screenshots/`
- Specs en `.kiro/specs/` (generadas por cc-sdd)
- Steering en `.kiro/steering/`
- Referencias en `references/references.bib`
- Figuras en `figures/`
- Datos en `data/`
- Scripts de build/validación en `scripts/`
- Skills científicos en `.claude/skills/`

## Pipeline Quarto (libro actual: "La Moneda Emocional")
- **Build HTML**: `./scripts/build-book.sh html` → genera `_book/` + screenshots
- **Build PDF**: `./scripts/build-book.sh pdf` (requiere TinyTeX: `quarto install tinytex`)
- **Build DOCX**: `./scripts/build-book.sh docx`
- **Build todo**: `./scripts/build-book.sh all`
- **Preview en vivo**: `./scripts/build-book.sh preview` o `quarto preview`
- **Screenshot capítulo**: `node scripts/screenshot-book.js --chapter 01`
- **Instalar deps Playwright**: `npm install playwright && npx playwright install chromium`

### Loop de revisión visual LLM
1. Editar `paper/parte-X/XX-capitulo.md`
2. `quarto render --to html` (rápido, solo HTML)
3. `node scripts/screenshot-book.js --chapter XX`
4. LLM lee `_book/screenshots/XX-slug.png` con la herramienta Read (multimodal)
5. Correcciones → repetir

## Comandos disponibles
- `/paper:init <tema> <revista>` — Inicia un nuevo paper con specs
- `/paper:validate` — Ejecuta todas las validaciones hard
- `/paper:review` — Genera reporte de revisión (soft specs)
- `/paper:status` — Muestra progreso por sección
- `/paper:cite <claim>` — Busca y agrega citación verificada
- `/paper:outline` — Genera/actualiza el outline desde specs

## Configuración de Steering
- Carga completa de `.kiro/steering/` como memoria del proyecto
- Archivos por defecto: `product.md`, `tech.md`, `structure.md`
- Archivos custom soportados (via `/kiro:steering-custom`)
