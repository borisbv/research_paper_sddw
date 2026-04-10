# Research & Design Decisions — tea-tecnologia (Fase: Marco Teórico)

## Summary
- **Feature**: tea-tecnologia — Marco teórico del paper sobre TEA y tecnologías tipo app
- **Discovery Scope**: Extension (dentro del framework Paper SDD existente) / Simple Addition en términos de complejidad arquitectónica
- **Key Findings**:
  - El dominio es documental, no software: "componentes" se mapean a subsecciones argumentativas del marco teórico.
  - La búsqueda exhaustiva de literatura Scopus se realizará en la fase de implementación (cuando se ejecute `/kiro:spec-impl` y los skills `literature-review` / `citation-management`), no durante el diseño.
  - El flujo argumental exigido por el usuario es estrictamente lineal de lo general a lo específico y termina con un cierre que conecta vacíos → propuesta.

## Research Log

### Naturaleza del artefacto y adaptación del template
- **Context**: El template `design.md` asume sistemas de software con componentes, contratos, datos. Esta fase produce un documento académico.
- **Sources Consulted**: `CLAUDE.md` del proyecto (Scientific Paper SDD Framework), `.kiro/settings/templates/specs/design.md`, `.kiro/settings/rules/design-principles.md`.
- **Findings**:
  - El framework declara explícitamente que "cada sección del paper es tratada como un módulo de software".
  - Esto habilita mapear subsecciones narrativas como "componentes", el flujo argumental como "system flow", y las reglas de estilo/citación como "contratos".
- **Implications**: El diseño puede seguir el template sin forzarlo, tratando cada subsección del marco teórico como un componente con responsabilidades, dependencias narrativas previas y cobertura de requisitos.

### Estrategia de búsqueda bibliográfica (diferida a implementación)
- **Context**: Los requisitos exigen citas APA de Scopus reciente y mínimo tres tecnologías con resultados reportados.
- **Sources Consulted**: Skills disponibles en el entorno (`literature-review`, `citation-management`, `research-lookup`).
- **Findings**:
  - `literature-review` soporta búsquedas sistemáticas multi-base; `citation-management` gestiona BibTeX y validación.
  - La validación contra CrossRef/DOI ya está contemplada en las validaciones hard del framework.
- **Implications**: El diseño solo define el contrato ("cada claim → cita Scopus reciente verificable"); la ejecución concreta de búsquedas queda en tasks de implementación.

### Restricciones de estilo (sin guiones como separadores)
- **Context**: El usuario exige párrafos largos orgánicos y prohíbe explícitamente el uso de guiones entre párrafos.
- **Findings**: Esta restricción es no negociable y debe convertirse en una validación automatizable (regex sobre el markdown del marco teórico).
- **Implications**: El diseño incluye una validación de estilo específica como parte del contrato del componente "Estilo y formato".

## Architecture Pattern Evaluation

| Option | Description | Strengths | Risks / Limitations | Notes |
|--------|-------------|-----------|---------------------|-------|
| Monolito narrativo | Escribir el marco teórico como un único bloque continuo sin subdivisión interna | Natural al texto académico; elimina saltos | Difícil trazar requisitos a párrafos; revisión compleja | Riesgo de perder el orden general→específico |
| Subsecciones como componentes | Tratar cada bloque temático (definición, niños, mundo, Latam, Chile, pedagogía, adolescentes, tecnologías, vacíos) como un componente con entrada/salida narrativa | Trazabilidad directa a requisitos; permite validación por bloque; facilita iteración incremental | Requiere cuidado para que las "costuras" no rompan la fluidez | **Seleccionada** |
| Pipeline de escritura en dos etapas | Outline bullet → prosa | Consistente con skill `scientific-writing` | Agrega una fase intermedia no pedida por el usuario para esta primera entrega | Se adopta parcialmente dentro del componente de redacción |

## Design Decisions

### Decision: Tratar cada bloque temático como un componente trazable
- **Context**: El marco teórico debe cubrir nueve bloques argumentales distintos con requisitos específicos.
- **Alternatives Considered**:
  1. Monolito narrativo sin estructura interna explícita
  2. Subsecciones como componentes (seleccionada)
- **Selected Approach**: Definir nueve componentes narrativos con id, intención, requisitos cubiertos y dependencias narrativas lineales.
- **Rationale**: Permite mapear 1:1 a los acceptance criteria de Requirement 2 y facilita validación incremental.
- **Trade-offs**: Añade disciplina estructural; obliga a cuidar transiciones para que el texto final se lea como prosa continua.

### Decision: Formato de salida único en Markdown dentro de `paper/`
- **Context**: El framework permite Markdown o LaTeX. No se definió revista objetivo todavía.
- **Selected Approach**: Usar Markdown (`paper/marco_teorico.md`) hasta que se defina la revista objetivo en una fase futura.
- **Rationale**: Markdown es más barato de iterar y compatible con las validaciones actuales; la conversión a LaTeX puede hacerse después sin pérdida.
- **Trade-offs**: Posible retrabajo menor si la revista final exige LaTeX estricto.

### Decision: Diferir la búsqueda bibliográfica exhaustiva a la fase de implementación
- **Context**: El diseño no debe congelar referencias específicas que aún no se han validado.
- **Selected Approach**: El diseño fija el contrato ("toda claim con cita Scopus reciente en `references.bib`") pero no prescribe las fuentes.
- **Rationale**: Mantiene el diseño estable y libera la búsqueda real para los skills especializados.

## Risks & Mitigations
- **Riesgo**: Saturar 2 páginas con nueve subsecciones argumentales y referencias. **Mitigación**: Presupuestar palabras por componente y priorizar densidad conceptual.
- **Riesgo**: Introducir guiones separadores por inercia de redacción. **Mitigación**: Validación automática con regex durante hard checks.
- **Riesgo**: Citar fuentes no Scopus o desactualizadas. **Mitigación**: Validación CrossRef + política de "preferir publicaciones recientes" en la fase de implementación.
- **Riesgo**: Pérdida de fluidez al coser componentes. **Mitigación**: Componente explícito de "revisión de transiciones" antes de cerrar la fase.

## References
- `CLAUDE.md` — Scientific Paper SDD Framework (principios, validaciones y convenciones)
- `.kiro/settings/templates/specs/design.md` — Plantilla base de diseño
- `temp_context/instrucciones.md` — Instrucciones originales del usuario para el marco teórico
