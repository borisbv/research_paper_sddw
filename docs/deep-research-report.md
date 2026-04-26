# Escritura científica guiada por especificaciones en Git y CI

## Resumen ejecutivo

Un framework de **Spec-Driven Development (SDD)** adaptado a la escritura de papers (a veces descrito como *PaperOps*, *Research Document Engineering* o *CI/CD para manuscritos*) es **viable hoy**, pero **no existe un estándar único** ni una “batería incluida” universal. En la práctica, el ecosistema se compone de (a) *frameworks de autoría* que ya usan archivos declarativos (YAML/JSON) y automatizan builds, (b) *validadores y linters* (prosa, BibTeX/DOI, LaTeX, enlaces), y (c) *plataformas colaborativas* que aportan edición y/o revisión asistida con IA. citeturn9search32turn9search18turn8search15turn10view0turn25view0

Hallazgos clave:

- Existen varios “núcleos PaperOps” **open source** con rasgos muy cercanos a SDD: **Manubot** (citaciones trazables por identificadores persistentes + automatización), **showyourwork!** (proveniencia fuerte de resultados/código + CI), **Quarto** (publicación técnica basada en proyectos + multi-formato), **MyST (mystmd)**/**Jupyter Book** (motor con especificación y config `myst.yml`), **Stencila** (modelo canónico/Schema para validar y transformar documentos) y **Rxiv-Maker** (preprints en Markdown con compilación automatizada y figuras reproducibles). citeturn9search32turn9search18turn25view0turn10view6turn11view3turn9search19turn7search1
- Para **anti-alucinación y verificación de referencias**, el stack realista hoy se centra en: (1) resolver y normalizar metadatos por DOI (Crossref/DataCite), (2) validar campos/estructura de bibliografía (BibTeX/BibLaTeX + `biber --validate-datamodel`), (3) aplicar linters como Vale/TeXtidote y (4) fallar CI cuando una cita no es resoluble o falta evidencia mínima. citeturn26search0turn26search3turn26search4turn26search7turn28view2turn26search5
- Recomendación pragmática: diseñar una **“especificación de manuscrito”** propia (YAML/JSON Schema) que defina *estructura*, *metadatos*, *políticas de citas* y *reglas de validación*, y ejecutar esa spec en CI como si fuera una suite de tests. Esto se alinea con lo que ya describen los flujos de Manubot (evaluación automática de cambios), showyourwork! (PDF sincronizado con código) y Stencila (schema para validar y transformar). citeturn9search32turn9search18turn8search15turn11view3

## Marco conceptual de SDD aplicado a papers

En software, SDD coloca la **especificación** como *fuente de verdad* y convierte el cumplimiento en **tests/validaciones automatizadas**. Para papers, la “spec” suele descomponerse en:

- **Spec de estructura**: secciones requeridas (Resumen/Abstract, Introducción, Métodos, Resultados, Discusión, Declaraciones, etc.), restricciones de longitud, orden, presencia de figuras/tablas y convenciones de nombres.
- **Spec de metadatos**: título, autores/afiliaciones, ORCID, keywords, funding, data/code availability, licencia.
- **Spec de referencias**: formato permitido (BibTeX/BibLaTeX/CSL JSON), reglas (toda cita debe ser resoluble por DOI/PMID/arXiv cuando aplique), consistencia de claves, prohibición de “referencias inventadas”.
- **Spec de build/publicación**: qué outputs se generan (PDF/HTML/DOCX), dónde se publican (artifact en CI, Pages), y reproducibilidad (ejecución de código/figuras).
- **Spec de asistencia IA** (si existe agente): límites claros: el agente puede proponer texto, pero no puede introducir citas nuevas sin DOI válido y verificado; cambios se revisan por PR como cualquier contribución. Esto está alineado con infraestructuras de revisión asistida integradas con control de versiones descritas en el ecosistema de Manubot AI Editor. citeturn17search23turn18view1

El ecosistema actual ya incluye herramientas donde esta idea es “nativa”, porque tratan manuscritos como **repositorios** (Git) y usan **automatización** para detectar errores (equivalente a test suites). Manubot explícitamente describe repositorios de manuscritos en Git y evaluación automática de cambios, y showyourwork! busca mantener el PDF *“siempre sincronizado”* con el código que produce resultados/figuras usando CI. citeturn9search32turn9search18turn13view0

## Inventario de frameworks, plataformas, plantillas y prototipos

Convenciones en las tablas:

- **Spec**: tipo de archivo declarativo (p.ej., `_quarto.yml`, `myst.yml`, `showyourwork.yml`, YAML/JSON).
- **Val**: validación/lint integrado o recomendado.
- **Citas**: gestión/verificación (resolución DOI, normalización, chequeos de consistencia).
- **Traza**: trazabilidad/proveniencia (vínculo paper ↔ datos/código ↔ outputs).
- **CI**: soporte directo para CI (acciones, guías, plantillas).
- **Git**: workflow orientado a PR/branch/review.
- **IA**: soporte explícito para prompts/agentes (integrado, o extensible).

### Herramientas end-to-end y plataformas (más cercanas a “PaperOps”)

| Nombre | Tipo | URL | Licencia | Spec | Val | Citas | Traza | CI | Git | IA | Formatos | Idioma | Madurez/actividad | Limitaciones/riesgos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| entity["organization","Quarto","scientific publishing sys"] | OSS | `https://github.com/quarto-dev/quarto-cli` | MIT | YAML proyecto (`_quarto.yml`) + front matter | Parcial (depende de linters externos) | Pandoc/CSL (verificación fuerte suele ser externa) | Media (depende de prácticas del repo) | Sí (deploys típicos; integrable) | Sí | No nativo (pero integrable) | MD/QMD → PDF/HTML/DOCX, etc. | Multilingüe (contenido) | ~5.5k⭐; commits recientes (Mar 2026) citeturn25view0turn16view0 | Sin verificación estricta de “cita existe” por defecto; equivalencia exacta multi-formato requiere disciplina. citeturn25view0turn3search3 |
| entity["organization","Manubot Rootstock","manuscript template"] | OSS template | `https://github.com/manubot/rootstock` | Mixta (template + licencias de contenido) | Estructura repo + configs | Sí (CI del template) | Fuerte: citación por identificadores persistentes y automatización | Alta (Git + rebuild automático) | Sí | Sí | Vía AI Editor (opcional) | MD → HTML/PDF/DOCX citeturn17search7turn9search20 | Multilingüe (contenido) | 473⭐; último commit Ene 2026 citeturn12view3turn15view0 | Setup inicial puede ser “fricción”; personalización de journal/plantillas puede requerir experiencia. citeturn17search14turn9search32 |
| entity["organization","Manubot","manuscript workflow"] | OSS (utilidades) | `https://github.com/manubot/manubot` | Apache-2.0 (según LICENSE) | CLI + convenciones | Sí (dev/CI, pre-commit) | `manubot cite` recupera metadatos por DOI/PMID; `process` prepara para Pandoc citeturn18view0turn8search9 | Media-Alta | Sí | Sí | Incluye `ai-revision` (en el ecosistema) citeturn18view0turn20view0 | MD/BibTeX → HTML/PDF/DOCX | Multilingüe (contenido) | 469⭐; commits hasta Ene 2026 citeturn19view0turn20view0 | No es “todo en uno” sin template rootstock; verificación de citas “existencia/DOI” es fuerte, pero la verificación semántica (cita apoya claim) no es automática. citeturn9search32turn26search10 |
| entity["organization","showyourwork!","reproducible article workflow"] | OSS | `https://github.com/showyourwork/showyourwork` | MIT | `showyourwork.yml` + workflow (Snakemake) | Sí (pipeline reproducible) | No central (se integra con LaTeX/Bib) | Muy alta (PDF ↔ código ↔ datos) | Sí (GitHub Actions) citeturn9search18turn9search34 | Sí | No nativo | LaTeX → PDF (principal) | Multilingüe (contenido) | 635⭐; commits Feb 2026 citeturn10view0turn13view0 | Curva de aprendizaje (Snakemake/CI); más orientado a papers computacionales que a papers “texto puro”. citeturn9search18turn9search34 |
| entity["organization","Rxiv-Maker","markdown to preprint pdf"] | OSS + prototipo académico | `https://github.com/HenriquesLab/rxiv-maker` | MIT | YAML/settings + estructura `MANUSCRIPT/` | Sí (incluye “skip-validation”; validación propia) citeturn9search35turn22view1 | BibTeX + resolución DOI inline; multi-estilo; export DOCX citeturn22view1turn9search23 | Alta (figuras ejecutables + caching) citeturn9search19turn22view1 | Integrable (no depende solo de CI, pero calza) | Sí | No nativo (aunque tiene extensión VS Code) citeturn7search9turn9search31 | MD → PDF y DOCX citeturn22view1 | Multilingüe (contenido) | 29⭐; commits Dic 2025 citeturn10view1turn16view4 | Proyecto joven: APIs/UX pueden cambiar; ecosistema más pequeño (riesgo mantenimiento). citeturn10view1turn9search19 |
| entity["organization","MyST Markdown","myst document engine"] | OSS | `https://github.com/jupyter-book/mystmd` | MIT | `myst.yml` + spec/AST | Sí (motor; plugins) | Citas científicas integradas; plantillas journal; export Word citeturn10view6turn9search25 | Media | Sí (deploy/publish) citeturn6search18turn6search6 | Sí | No nativo | MD/MyST → HTML/PDF/LaTeX/DOCX citeturn10view6 | Multilingüe (contenido) | 484⭐; commits Mar 2026 citeturn10view6turn16view3 | Verificación dura de DOI/citas suele ser externa; algunas piezas del ecosistema todavía evolucionan (cambios de config/compat). citeturn6search32turn9search25 |
| entity["organization","Jupyter Book","computational publishing"] | OSS | `https://github.com/jupyter-book/jupyter-book` | BSD-3-Clause | `myst.yml` (en JB2) citeturn9search21turn17search24 | Sí | Citas + crossrefs; ejecuta/cacha celdas citeturn17search2turn21view1 | Media-Alta | Sí (GitHub Pages/RTD) citeturn6search18turn17search16 | Sí | No nativo | MD/ipynb → HTML/PDF citeturn17search2 | Multilingüe (contenido) | 4.2k⭐; commits Feb 2026 citeturn18view2turn21view1 | Transición JB1→JB2: JB1 en “maintenance mode”; el set de features puede diferir y requiere atención a breaking changes. citeturn17search24turn8search26 |
| entity["organization","Stencila","executable documents platform"] | OSS (plataforma) | `https://github.com/stencila/stencila` | Apache-2.0 | **Stencila Schema** (modelo canónico) citeturn8search15turn11view3 | Sí (validación/transformación basada en schema) | Soporta referencias (depende del pipeline) | Alta (documentos semánticos + ejecución) | Integrable | Sí | Sí (incluye “prompts”/IA en repo; tooling “scientific intelligence”) citeturn11view3turn14view2 | Multi-formato (codecs, export) | Multilingüe (contenido) | 875⭐; commits Mar 2026 citeturn11view3turn16view1 | Requiere adoptar su modelo/representación; integración con flujos tradicionales puede implicar “puentes” adicionales. citeturn8search15turn11view3 |
| entity["organization","Living Papers","scholarly authoring toolkit"] | Prototipo investigación (OSS) | `https://github.com/uwdata/living-papers` | BSD-3-Clause | Toolkit + templates | Parcial (depende del template) | Referencias soportadas (vía pipeline) | Media (enfoque en artículos aumentados) citeturn7search19turn10view4 | Sí (repo tiene Actions) | Sí | No nativo | MD → web y PDF (según instalación) citeturn10view4turn23view0 | Multilingüe (contenido) | 157⭐; último commit 2023 citeturn12view2turn16view2 | Menor actividad reciente; explícitamente “research testbed” (riesgo de estabilidad). citeturn10view4turn16view2 |
| entity["organization","Curvenote","scientific writing platform"] | Comercial + OSS (parte) | `https://github.com/curvenote/curvenote` | (ver repo) | MyST-based | Parcial | Citas/crossref en su ecosistema (MyST) | Media | Integrable | Sí | Potencialmente (asistencia) | MD/MyST → web/PDF | Multilingüe (contenido) | Evidencia de enfoque “continuous practices” en publicación académica citeturn5search0turn5search1 | Detalles de licencias/capacidades exactas dependen del producto vs repo; puede haber lock-in si dependes de features SaaS. citeturn5search0turn5search1 |
| entity["organization","Journal of Open Source Software","research software journal"] paper format + acción | Template/workflow | `https://joss.readthedocs.io/en/latest/paper.html` | (depende del uso) | `paper.md` + `paper.bib` | Sí (compilación automática por acción) citeturn27search31turn27search19 | Chequeos típicos (compila PDF; bib) | Media | Sí | Sí | No | MD/BibTeX → PDF | Multilingüe (contenido) | Docs oficiales + acción para compilar paper en GitHub citeturn27search31turn27search19 | No es un framework genérico de autoría, sino un formato/workflow de una venue; útil como “patrón SDD” para replicar. citeturn27search31turn27search19 |
| entity["organization","Whedon","joss submission tool"] | OSS (deprecado) | `https://github.com/openjournals/whedon` | MIT | CLI | Sí (para su propósito) | Indirecto | Media | Sí | Sí | No | Gestión submission/review | N/A | Deprecado a favor de Buffy citeturn27search3 | No recomendable como base nueva (deprecado); sirve para entender automatización editorial. citeturn27search3 |
| entity["company","Overleaf","collaborative latex editor"] | Comercial | `https://www.overleaf.com` | Propietaria | (proyecto LaTeX) | Parcial | Integración con Zotero/BibTeX | Baja-Media | Sí (Git/GitHub sync) citeturn4search1turn4search2 | Sí | No nativo en CI (pero integrable) | LaTeX → PDF | Multilingüe (contenido) | Plataforma estable (empresa) citeturn4search1turn4search2 | CI “real” queda fuera si el build vive en Overleaf; riesgo de divergencia entre Overleaf y repo si no se define “source of truth”. citeturn4search1 |
| entity["company","SciSpace","academic writing platform"] (agente LaTeX) | Comercial | `https://scispace.com/agents/latex-proofreading-rjve4wat` | Propietaria | N/A | Revisión lingüística | No garantiza verificación DOI | N/A | N/A | N/A | Sí (agente) citeturn26search16 | LaTeX (entrada) | Multilingüe parcial (depende del servicio) | Servicio (SaaS) citeturn26search16 | Riesgo de alucinación: requiere guardrails y verificación externa; no reemplaza CI de referencias. citeturn26search16turn26search10 |

**Fuentes base de este inventario**: repositorios oficiales (GitHub), documentación oficial y papers/proceedings cuando están disponibles. citeturn25view0turn15view0turn13view0turn22view1turn10view6turn11view3turn10view4turn27search31turn4search1turn26search16

### Validadores, utilidades y componentes “tipo test” para CI de papers

| Nombre | Tipo | URL | Licencia | Qué valida/aporta | Integración CI/Git | Formatos | Idioma | Madurez/actividad | Limitaciones/riesgos |
|---|---|---|---|---|---|---|---|---|---|
| entity["organization","Zotero","reference manager"] Better BibTeX | Plugin | `https://github.com/retorquere/zotero-better-bibtex` | MIT | Export bib controlado, claves de citación, flujo BibTeX/BibLaTeX para toolchains text-based citeturn27search0turn28view0 | Git-friendly (export estable) | BibTeX/BibLaTeX | Multilingüe | 6.5k⭐; commits Mar 2026 citeturn28view0turn29view0 | Cambios de versiones de Zotero pueden impactar; requiere disciplina en export/commit. citeturn27search4turn27search32 |
| bibtex-tidy | OSS utility | `https://github.com/FlamingTempura/bibtex-tidy` | MIT | Normaliza/ordena BibTeX; remueve duplicados/campos; reduce diffs ruidosos citeturn27search18turn28view1 | Sí (pre-commit/CI) | BibTeX | N/A | 1.1k⭐; commits Mar 2026 citeturn28view1turn30view0 | Formatear ≠ verificar verdad bibliográfica; hay que sumar DOI checks. citeturn27search18turn26search10 |
| entity["organization","Vale","prose linter"] | OSS utility | `https://github.com/vale-cli/vale` | MIT (en repos) | Enforce de guías editoriales sobre texto; reglas como test suite citeturn27search29turn28view2 | Sí (action oficial; LSP) citeturn27search13turn28view2 | MD/Asciidoc/otros (según config) | Multilingüe con reglas adecuadas | 5.3k⭐; commits Mar 2026 citeturn28view2turn27search37 | Requiere configurar reglas (en español puede requerir set propio); no detecta “cita inventada”. citeturn27search29turn26search10 |
| TeXtidote (Textidote) | OSS utility | `https://github.com/sylvainhalle/textidote` | (según distribución; repo público) | Ortografía/gramática/estilo en LaTeX; mapea errores a fuente; se reporta que puede chequear citas/referencias citeturn26search2turn26search5turn26search22 | Sí (CLI) | LaTeX, y otros formatos | Multilingüe parcial (depende del checker) | Proyecto activo (releases) citeturn26search34turn26search5 | Señales “formales” ≠ veracidad; configuración de idioma y falsos positivos en texto técnico. citeturn26search5turn26search22 |
| Biber `--validate-datamodel` | OSS utility | `https://biblatex-biber.sourceforge.net/` | N/A | Valida estructura/campos contra modelo de datos; opción `--dieondatamodel` para fallar build citeturn26search4turn26search11turn26search29 | Sí (ideal como gate en CI) | BibLaTeX/BibTeX (backend) | N/A | Tool estándar en LaTeX/biblatex (docs y manuales) citeturn26search25turn26search4 | Valida *estructura*, no “si el DOI existe”; requiere DOI resolvers aparte. citeturn26search4turn26search0 |
| xu-cheng/latex-action | OSS (GitHub Action) | `https://github.com/xu-cheng/latex-action` | (ver repo) | Compila LaTeX en CI (PDF) citeturn3search0 | GitHub Actions | LaTeX→PDF | Multilingüe | Action popular | No valida citas por sí sola; solo build. citeturn3search0turn26search10 |
| DOI Content Negotiation | Infra/documentación | `https://citation.doi.org/docs.html` | N/A | Resolver metadatos/citas por DOI vía HTTP Accept (base para verificación automática) citeturn26search3turn26search0turn26search27 | Sí (scripts en CI) | BibTeX/CSL-JSON/etc | N/A | Infra estándar DOI | Variabilidad en campos devueltos; casos como “article-number” ausente en BibTeX requieren handling. citeturn26search0turn26search10 |

## Verificación de citas y anti-alucinación en un flujo SDD

Un marco SDD para papers con IA suele fallar por una razón: **las citas** son el punto donde la alucinación es más costosa. Hoy, los enfoques más defendibles combinan **resolución de identificadores persistentes** + **validación estructural** + **políticas de CI**.

### Resolución y normalización de metadatos (DOI-first)

- **Crossref content negotiation** describe cómo usar el header `Accept` contra `https://doi.org/<DOI>` para obtener múltiples formatos, redirigiendo a la agencia correcta (y también a endpoints “transform” de su API). Esto permite verificar automáticamente que un DOI responde y devolver metadatos normalizados. citeturn26search0
- **DOI Content Negotiation** (documentación general) y la explicación de **DataCite** muestran el mismo patrón y ejemplos para obtener BibTeX o citas formateadas, lo que sirve como “backend” para un validador en CI que rehúsa referencias no resolubles. citeturn26search3turn26search27
- En la práctica, hay **diferencias y huecos** en lo que devuelven estos servicios (p.ej., discusión pública sobre BibTeX sin `article-number`), así que tu validador debe contemplar reglas por publisher/venue (o fallback a otros resolvers). citeturn26search10turn26search0

APIs complementarias (útiles para enriquecer o cruzar datos):

- **Crossref REST API** (búsqueda/metadata) para resolver por DOI/título y detectar inconsistencias. citeturn3search0
- **Semantic Scholar API** y **OpenAlex API** como fuentes alternativas (útiles para verificación cruzada y completar metadatos cuando Crossref/DataCite no bastan). citeturn3search1turn3search2

### Higiene y validación estructural de bibliografía

- **bibtex-tidy** ayuda a convertir la bibliografía en un artefacto “determinista” (menos diffs ruidosos, orden estable, limpieza). Esto es importante porque reduce ruido en PRs y hace más visible un cambio real (p.ej., una cita agregada). citeturn27search18turn30view0
- **Biber** aporta `--validate-datamodel` y `--dieondatamodel` para convertir problemas de campos/estructura en fallas de build (equivalente a que no compile el código si rompe el tipo). citeturn26search4turn26search11

### Linters de prosa y “revisores formales” (sin pretender veracidad)

- **Vale** está diseñado para imponer guías de estilo editorial sobre texto (reglas como tests). En paper-ops, esto sirve para consistencia, tono, mayúsculas, términos prohibidos, etc. citeturn27search29turn28view2turn27search13
- **TeXtidote** existe específicamente para soportar chequeos sobre LaTeX sin destruir el markup y se reporta en literatura reciente como herramienta que detecta issues formales y también chequea aspectos de citas/referencias (dependiendo de configuración). citeturn26search2turn26search22turn26search30

### Integración con gestores bibliográficos (para evitar “inventarse” BibTeX)

- **Better BibTeX** conecta el catálogo de referencias (Zotero) con toolchains LaTeX/Markdown, enfatizando el manejo efectivo de bibliografía para autoría basada en texto. Esto se alinea con SDD porque te permite declarar políticas de export y claves reproducibles y versionarlas. citeturn27search0turn29view0

## Stacks recomendados para implementar un framework SDD para papers

Estos stacks están pensados para que puedas tener: **spec declarativa**, **validadores**, **trazabilidad**, **CI gates**, y (si quieres) **agentes IA** bajo control.

### Stack orientado a citación trazable y colaboración abierta

Base:

- Manubot Rootstock + Manubot (build del manuscrito y citación basada en identificadores persistentes). citeturn12view3turn18view0turn9search20turn9search32
- Opcional: Manubot AI Editor, como “bot de refactor” del texto con PRs revisables (integrado al flujo de repos). citeturn18view1turn17search23turn17search34

Validadores recomendados:

- `bibtex-tidy` + checks DOI (Crossref/DataCite content negotiation) + `biber --validate-datamodel`. citeturn30view0turn26search0turn26search27turn26search11
- Vale (reglas de estilo) y/o TeXtidote si hay LaTeX en el pipeline. citeturn28view2turn26search5

Pros: citación fuerte por identificadores persistentes, outputs HTML/PDF/DOCX y un patrón probado de “evaluación automática de cambios” tipo CI. citeturn9search32turn17search7turn18view0  
Contras: el setup inicial puede ser más “ingenieril” que herramientas WYSIWYG; personalización de plantillas puede requerir trabajo. citeturn17search14turn9search32  
Esfuerzo estimado: **medio**.

### Stack multi-formato y “proyecto publicable” (paper como producto)

Base:

- Quarto como sistema de publicación técnica basado en Pandoc, con proyecto y YAML, exportando PDF/HTML/DOCX según necesidad. citeturn25view0turn8search0
- Bibliografía desde Zotero + Better BibTeX para export determinista. citeturn27search0turn29view0

Validadores recomendados:

- `bibtex-tidy` + DOI resolvers; Vale para estilo; compilación en CI (GitHub Actions/GitLab CI). citeturn30view0turn28view2turn26search0

Pros: muy flexible, gran adopción, multi-formato “de fábrica”, y el YAML de proyecto es un ancla natural para una spec SDD. citeturn25view0turn8search0  
Contras: verificación dura de “esta referencia existe” no viene por defecto; necesitas agregar scripts/validadores. citeturn26search10turn25view0  
Esfuerzo estimado: **bajo a medio**.

### Stack de reproducibilidad fuerte (paper ejecutable y sincronizado con resultados)

Base:

- showyourwork! para papers en LaTeX donde quieres garantizar que el PDF está sincronizado con el código/datos mediante Snakemake + tectonic + CI. citeturn9search18turn9search34turn3search1

Validadores recomendados:

- Validación BibLaTeX con biber + TeXtidote (si aplica) + DOI checks.
- Publicación del PDF como artifact; opcional Pages para previsualización.

Pros: excelente para “trazabilidad de evidencia” (figuras/resultados reproducibles) y un modelo CI-first muy cercano al espíritu SDD. citeturn9search18turn13view0  
Contras: curva de aprendizaje y mayor complejidad infra (workflow manager, caching, CI). citeturn9search18turn9search34  
Esfuerzo estimado: **alto**.

## Pipeline recomendado Git+CI para escritura guiada por spec

```mermaid
flowchart TD
  A[Autoría en ramas: contenido + spec] --> B[pre-commit local]
  B -->|lint rápido| C[PR a main]
  C --> D[CI: build matrix]
  D --> D1[Render PDF/HTML/DOCX]
  D --> D2[Validar estructura vs spec\n(JSON Schema/YAML rules)]
  D --> D3[Validar bibliografía\n(bibtex-tidy + biber validate)]
  D --> D4[Resolver DOIs\n(Crossref/DataCite/S2/OpenAlex)]
  D --> D5[Linter de prosa\n(Vale/TeXtidote)]
  D --> E{Gates pasan?}
  E -->|No| F[Feedback en PR\n(reportes + artifacts)]
  E -->|Sí| G[Merge]
  G --> H[Release: artifacts + Pages]
  H --> I[Opcional: agente IA\npropone PRs\n(sujeto a gates)]
```

Componentes que justifican este flujo: evaluación automática de cambios en repositorios de manuscritos (Manubot), sincronización paper↔código con CI (showyourwork!), y uso de schema/modelo para validación consistente (Stencila Schema). citeturn9search32turn9search18turn8search15

### Snippets cortos para integrar validadores en CI

**GitHub Actions (ejemplo genérico, adaptable a Quarto/Manubot/LaTeX):**

```yaml
name: paper-ci

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  validate-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Bibliografía: normalización
      - name: Install bibtex-tidy (node)
        run: |
          npm install -g bibtex-tidy

      - name: BibTeX tidy check
        run: |
          bibtex-tidy --check paper.bib

      # Prosa: Vale (acción oficial; migraciones de org están documentadas)
      - name: Prose lint (Vale)
        uses: vale-cli/vale-action@v2
        with:
          files: content/
```

Ese patrón es coherente con el uso de Vale (CLI para imponer guía editorial) y su action oficial/migrada. citeturn28view2turn27search13

**GitLab CI (fragmento mínimo, idea equivalente):**

```yaml
stages: [lint, build]

bibtex:
  stage: lint
  image: node:20
  script:
    - npm i -g bibtex-tidy
    - bibtex-tidy --check paper.bib

prose:
  stage: lint
  image: vale-cli/vale:v3
  script:
    - vale content/
```

> Nota: la imagen de Vale en GitLab puede reemplazarse por instalación directa si no usas contenedores; el punto es tratar cada validador como un “test job”. citeturn28view2turn27search29

### Repos y plantillas de ejemplo para “arrancar” rápido

- Manubot: Rootstock template `https://github.com/manubot/rootstock` y ejemplos “Try Manubot” `https://github.com/manubot/try-manubot`. citeturn12view3turn17search22
- showyourwork!: repo principal y su action `https://github.com/showyourwork/showyourwork-action`. citeturn10view0turn9search34
- Rxiv-Maker: repo principal y manuscrito demostración `https://github.com/HenriquesLab/manuscript-rxiv-maker`. citeturn7search3turn9search15
- Living Papers: template `https://github.com/uwdata/living-papers-template`. citeturn23view0turn24view0
- JOSS-like: template con validación/preview `https://github.com/openbases/submission-joss`. citeturn27search19turn27search15

También hay recursos en español que muestran adopción y transferencia del enfoque PaperOps, por ejemplo una guía/blog sobre Manubot y una versión en español de un manuscrito que documenta uso de Manubot en un paper. citeturn6search5turn6search25

## Comparación rápida de cobertura de features en los seis candidatos principales

Criterios (máx 7): **Spec**, **Val**, **Citas**, **Traza**, **CI**, **Git**, **IA**.

| Tool | Cobertura (0–7) | Barra | Evidencia base |
|---|---:|---|---|
| Manubot (Rootstock + tooling) | 6 | ██████░ | Repos + paper describen Git+evaluación automática+outputs+citaciones; AI Editor disponible citeturn9search32turn12view3turn18view0turn18view1 |
| Stencila | 6 | ██████░ | Schema canónico para validar/transformar + repo activo citeturn8search15turn11view3turn16view1 |
| showyourwork! | 5 | █████░░ | Pipeline reproducible con Snakemake+tectonic+CI; repo activo citeturn9search18turn13view0turn10view0 |
| Rxiv-Maker | 5 | █████░░ | Markdown→PDF con figuras ejecutables/caching + validación + DOCX citeturn22view1turn9search19turn16view4 |
| Quarto | 4 | ████░░░ | Proyecto YAML, multi-formato, CI integrable; verificación dura de citas requiere extras citeturn25view0turn16view0turn26search10 |
| MyST (mystmd) | 4 | ████░░░ | `myst.yml`, citas + export Word/PDF; verificación fuerte de DOI suele ser externa citeturn10view6turn16view3turn26search10 |

> Interpretación: todos pueden ser base de un framework SDD; la diferencia está en cuánto viene “incluido” vs cuánto debes agregar tú.

## Brechas del ecosistema y direcciones de investigación

Brechas principales:

- **Falta un “Paper Spec estándar”** (equivalente a OpenAPI/JSON Schema para papers) que modele estructura, metadatos, bibliografía y políticas de validación de forma interoperable entre Quarto/Manubot/MyST/Stencila. MyST ya tiene una spec/AST en desarrollo, y Stencila define un Schema canónico; pero no hay convergencia amplia para el caso “paper científico general”. citeturn9search25turn8search15
- **Verificación bibliográfica completa es difícil**: incluso con DOI content negotiation, hay variaciones de campos (p.ej., discusión sobre `article-number` en BibTeX) y edge cases por publisher. Esto obliga a diseñar validadores “con excepciones” y/o verificación cruzada con múltiples fuentes (Crossref/DataCite/OpenAlex/Semantic Scholar). citeturn26search0turn26search10turn3search2turn3search1
- **La verificación semántica “cita apoya el claim”** aún no está resuelta como commodity. Lo más cercano hoy es instrumentar *políticas* (no permitir nuevas citas sin DOI resoluble; exigir “evidence blocks” con links/DOIs) y usar agentes IA solo para edición lingüística, no para inventar bibliografía. citeturn26search3turn18view1turn26search16
- **Multiformato con equivalencia fuerte** (PDF/HTML/DOCX idénticos en numeración, referencias, floats) sigue siendo frágil: herramientas hacen export, pero garantizar equivalencia requiere tests adicionales y convenciones estrictas del repo. citeturn10view6turn22view1turn25view0

Direcciones prometedoras:

- **Documentos más semánticos**: propuestas como SciKGTeX apuntan a anotar contribuciones en LaTeX para extracción y carga en knowledge graphs (idea alineable con “evidence traceability”). citeturn7academia31
- **Papers aumentados/ejecutables**: Living Papers enmarca artículos que abarcan print + web interactiva + APIs para reutilizar contenido/código, que encaja con el objetivo SDD de trazabilidad y automatización. citeturn7search19turn10view4
- **Infra de autoría con IA bajo control de CI**: Manubot AI Editor formaliza una infraestructura de revisión asistida integrada a un flujo con control de versiones, lo que sugiere un patrón general: *el agente propone, el CI valida, los humanos aprueban*. citeturn17search23turn18view1turn9search32