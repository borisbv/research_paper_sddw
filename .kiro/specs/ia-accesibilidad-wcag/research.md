# Research & Design Decisions

---
**Purpose**: Hallazgos de descubrimiento y decisiones arquitectónicas para el paper IA-Accesibilidad-WCAG.
---

## Summary
- **Feature**: `ia-accesibilidad-wcag`
- **Discovery Scope**: New Feature (paper científico desde cero)
- **Key Findings**:
  - El dataset contiene 41 tecnologías con evaluaciones en 3 dimensiones WCAG (usabilidad, robustez, operabilidad) y 4 tipos de discapacidad
  - La estructura IMRaD requiere 8 secciones en archivos Quarto separados con pipeline de build existente
  - Las referencias deben ser verificables (DOI/CrossRef) y de alto impacto (Q1-Q2, 2021-2026)

## Research Log

### Estructura del dataset fuente
- **Context**: Necesidad de entender la estructura del CSV para diseñar el pipeline de análisis
- **Sources Consulted**: `temp_context/AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv`
- **Findings**:
  - 41 tecnologías (filas), no 42 como indicaban las instrucciones
  - Variables de identificación: nombre, descripción, URL, modalidad de pago, opción para desarrolladores
  - Variables FODA: fortalezas, oportunidades, debilidades
  - Categorización: tipo de producto, tipo de tecnología IA, tipo de discapacidad
  - Usabilidad: precisión (Baja/Media/Alta), sensibilidad (Baja/Media/Alta), tiempo de respuesta (Lento/Moderado/Rápido)
  - Robustez: multidispositivo, multi-navegador, multi-OS
  - Operabilidad: configuración previa (Manual/Automática), navegación por teclado (Total/Parcial/No), comandos de voz (Sí/Parcial/No)
  - Las evaluaciones son categóricas (no numéricas 1-5 como indicaban las instrucciones); se requiere mapeo a escala numérica
- **Implications**: El script de análisis debe transformar variables categóricas a numéricas para generar rankings y estadísticas descriptivas

### Categorías de tecnologías identificadas en el dataset
- **Context**: Mapear los tipos de producto para la categorización
- **Findings**:
  - Asistentes conversacionales/voz: ChatGPT, Copilot, Gemini, Alexa, Google Assistant, Siri, DeepSeek
  - Interfaces cerebro-computadora (BCI): Neuralink, BrainGate, NextMind, CTRL-labs, OpenBCI, Emotiv, Neurable
  - Seguimiento ocular: Tobii Dynavox, EyeSpeak, Irisbond, EyeControl, GazeSpeak
  - Control de cursor alternativo: eViacam, Sesame Phone, HeadMouse Nano, Quha Zono, GlassOuse, Jouse3, Tecla
  - Lectores de pantalla: NVDA, JAWS, BrailleSurf
  - Navegación/reconocimiento por voz: Voice Control, LipSurf, Dragon NaturallySpeaking, Voiceitt
  - Herramientas de evaluación web: Accessibility Insights, UserWay, WAVE
  - Subtitulado automático: Otter.ai, AVA, Web Captioner
  - Experimental: Project Mariner
- **Implications**: 9 categorías de producto; la distribución por discapacidad es desigual (dominan motora y visual)

### Distribución por tipo de discapacidad
- **Context**: Análisis preliminar para anticipar hallazgos del paper
- **Findings**:
  - Motora: ~25 tecnologías (la más cubierta, incluye BCI, control de cursor, voz)
  - Visual: ~15 tecnologías (lectores de pantalla, asistentes, evaluación web)
  - Cognitiva: ~12 tecnologías (asistentes conversacionales, simplificación)
  - Auditiva: ~5 tecnologías (subtitulado, Voiceitt — la menos cubierta)
- **Implications**: Brecha significativa en discapacidad auditiva; esto es un hallazgo clave para la discusión sobre vacío de conocimiento

### Pipeline de producción del paper
- **Context**: El proyecto ya tiene infraestructura Quarto configurada
- **Findings**:
  - Build scripts existentes en `scripts/build-book.sh`
  - Convención de archivos en `paper/` (Markdown/Quarto)
  - Referencias en `references/references.bib`
  - Figuras en `figures/`
  - Datos procesados en `data/` (dentro de paper)
  - Screenshot pipeline para revisión visual
- **Implications**: Se reutiliza la infraestructura existente; los archivos del paper se crean dentro de `paper/`

## Architecture Pattern Evaluation

| Option | Description | Strengths | Risks / Limitations | Notes |
|--------|-------------|-----------|---------------------|-------|
| Monolito Quarto | Un solo archivo .qmd con todo el paper | Simple, fácil de compilar | Difícil de editar en paralelo, archivos grandes | No recomendado para papers complejos |
| Multi-archivo Quarto | Secciones separadas en archivos .qmd individuales | Modular, versionable, editable por sección | Requiere configuración _quarto.yml | Alineado con steering y convenciones del proyecto |
| LaTeX directo | Archivos .tex con compilación directa | Control total de formato | Mayor curva de aprendizaje, menos portable | No alineado con el stack actual |

## Design Decisions

### Decision: Multi-archivo Quarto con secciones IMRaD
- **Context**: El paper requiere estructura IMRaD con múltiples secciones editables independientemente
- **Alternatives Considered**:
  1. Monolito — un solo archivo grande
  2. Multi-archivo Quarto — una sección por archivo
  3. LaTeX directo — archivos .tex
- **Selected Approach**: Multi-archivo Quarto, un archivo .qmd por sección del paper
- **Rationale**: Alineado con la infraestructura existente del proyecto, permite edición modular y versionado granular
- **Trade-offs**: Requiere mantener `_quarto.yml` actualizado; compilación depende de Quarto instalado
- **Follow-up**: Verificar que `_quarto.yml` incluya los nuevos archivos del paper

### Decision: Mapeo categórico a numérico para ranking
- **Context**: El dataset usa escalas categóricas (Baja/Media/Alta, Sí/Parcial/No) pero los requirements piden un ranking numérico
- **Alternatives Considered**:
  1. Análisis puramente cualitativo — sin puntuaciones numéricas
  2. Mapeo simple (Baja=1, Media=3, Alta=5) — transformación directa
  3. Mapeo ponderado con pesos por dimensión — más riguroso
- **Selected Approach**: Mapeo simple con pesos justificados por dimensión
- **Rationale**: Permite ranking cuantitativo mientras se mantiene la transparencia metodológica
- **Trade-offs**: Simplifica la variabilidad; debe documentarse como limitación
- **Follow-up**: Definir tabla de mapeo exacta en la sección de Metodología del paper

### Decision: Búsqueda bibliográfica con skills especializados
- **Context**: Se requieren ≥30 referencias Q1-Q2 verificables
- **Selected Approach**: Usar skills `citation-management`, `research-lookup` y `literature-review` del proyecto para búsqueda y verificación
- **Rationale**: El proyecto ya tiene skills configurados para búsqueda académica
- **Trade-offs**: Depende de la disponibilidad de APIs externas (Semantic Scholar, CrossRef)

## Risks & Mitigations
- Datos categóricos no numéricos en dataset → Definir tabla de mapeo transparente y documentar como limitación metodológica
- Referencias no verificables → Usar skill de citation-management con verificación DOI/CrossRef antes de inclusión
- Brecha en cobertura de discapacidad auditiva → Convertirlo en hallazgo positivo del paper (vacío identificado)
- Dataset con información de 2023-2025 → Documentar temporalidad como limitación; algunas tecnologías pueden haber cambiado

## References
- [WCAG 2.2 W3C Recommendation](https://www.w3.org/TR/WCAG22/) — estándar normativo base del estudio
- [WAI - Web Accessibility Initiative](https://www.w3.org/WAI/) — marco institucional de accesibilidad
- [Quarto Documentation](https://quarto.org/docs/guide/) — sistema de publicación del proyecto
