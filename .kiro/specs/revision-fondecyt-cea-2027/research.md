# Research & Design Decisions

## Summary
- **Feature**: `revision-fondecyt-cea-2027`
- **Discovery Scope**: Extension (integración de documentos temp_context/ en flujo de revisión estructurado)
- **Key Findings**:
  - La propuesta es un documento de ~300 líneas en markdown con 6 etapas metodológicas, carta Gantt y ~50 referencias. El límite FONDECYT es 10 páginas + 5 de referencias.
  - El protocolo de revisión define 23 criterios específicos organizados en dimensiones: coherencia, tono, novedad, Gantt, participantes, técnicas y formato.
  - Las bases FONDECYT Regular 2027 establecen criterios formales estrictos (formato carta, Arial 10, secciones obligatorias) cuyo incumplimiento causa exclusión.

## Research Log

### Estructura del documento fuente
- **Context**: Comprender la organización actual de la formulación para mapear componentes de revisión.
- **Sources Consulted**: `temp_context/27-Mayo-EA-FormulacionRegEsp+CF.md`
- **Findings**:
  - Secciones: (1) Fundamentos teóricos 1.1, (2) Marco teórico 2.1-2.4, (3) Pregunta e hipótesis 3.1, (4) Metodología 4.1-Etapa 6, (5) Novedad científica, (6) Carta Gantt, (7) Referencias
  - Etapas metodológicas: Empatizar, Definir, Exploración interacción, Exploración participativa, Validación, Devolución
  - Productos numerados: 1-11 (con salto: falta 7 y 8, salta de 6 a 9)
  - OE1-OE4 mapeados a etapas 1-5 respectivamente
- **Implications**: La revisión debe verificar alineación OE-Etapa-Producto y señalar inconsistencias de numeración

### Protocolo de evaluación
- **Context**: Definir el alcance de los 23 criterios de revisión.
- **Sources Consulted**: `temp_context/Acción_para_revision.md`
- **Findings**:
  - 23 criterios agrupables en: coherencia metodológica (1-4), tono científico (3,13,18), novedad (5,7,21), calidad textual (8,12,14), Gantt (9,17), participantes (10,22), técnicas (11,16), formato (15,19-20,23)
  - Formato de salida requerido: 4 secciones (A-D)
  - Convención de marcado: +texto nuevo+ para cambios
  - Restricción: no usar guiones (-) ni guiones bajos (_)
- **Implications**: Cada criterio se mapea a un componente de verificación específico

### Requisitos formales FONDECYT
- **Context**: Verificar restricciones de formato que pueden causar exclusión.
- **Sources Consulted**: `temp_context/BASES_FONDECYT_REGULAR_2027.md`, `temp_context/REX_Bases_Fondecyt_Regular_2027.md`
- **Findings**:
  - Extensión máxima: 10 páginas formulación + 5 páginas referencias
  - Formato: carta, Arial 10 o similar
  - Secciones obligatorias: (a) marco teórico, (b) hipótesis/objetivos, (c) metodología, (d) Gantt, (e) antecedentes equipo, (f) novedad
  - No incluir en anexos información que deba estar en formulación
  - Eliminar instrucciones en azul
  - Plazo cierre: 10 junio 2026 (postulación), 24 junio 2026 (patrocinio)
- **Implications**: El componente de verificación formal es bloqueante; incumplimiento = fuera de bases

## Architecture Pattern Evaluation

| Option | Description | Strengths | Risks / Limitations | Notes |
|--------|-------------|-----------|---------------------|-------|
| Pipeline secuencial | Revisión sección por sección en orden del documento | Sistemático, no omite secciones | Puede no capturar contradicciones cross-sección | Adecuado para verificación formal |
| Revisión por criterio | Iterar los 23 criterios sobre todo el documento | Cobertura completa de criterios | Redundancia al revisar misma sección varias veces | Mejor para evaluación cualitativa |
| Híbrido (seleccionado) | Pipeline formal + evaluación por criterios agrupados | Combina cobertura formal y temática | Mayor complejidad de orquestación | Equilibrio entre exhaustividad y eficiencia |

## Design Decisions

### Decision: Enfoque híbrido de revisión
- **Context**: La propuesta requiere tanto verificación formal (bases FONDECYT) como evaluación cualitativa (23 criterios)
- **Alternatives Considered**:
  1. Pipeline secuencial puro: revisar sección por sección
  2. Revisión por criterio: iterar criterios sobre documento completo
- **Selected Approach**: Enfoque híbrido en 3 fases: (1) Verificación formal de bases, (2) Evaluación por criterios agrupados, (3) Generación de reporte estructurado
- **Rationale**: La verificación formal es binaria (cumple/no cumple) y debe ejecutarse primero como gate. La evaluación cualitativa requiere análisis transversal.
- **Trade-offs**: Mayor complejidad de orquestación, pero asegura cobertura completa
- **Follow-up**: Verificar que el reporte final integre hallazgos de ambas fases sin duplicación

### Decision: Marcado de cambios con convención +texto+
- **Context**: El protocolo exige marcar cambios con símbolo + delante y detrás
- **Selected Approach**: Toda reescritura se marca con `+texto nuevo+` inline
- **Rationale**: Permite al investigador identificar rápidamente qué cambió vs. qué se mantuvo

## Risks & Mitigations
- Extensión del documento reescrito puede exceder 10 páginas → Priorizar reducciones antes de adiciones
- Contradicciones entre Gantt y metodología pueden requerir reestructuración profunda → Señalar contradicciones antes de reescribir
- Referencias faltantes pueden no ser verificables sin acceso a bases de datos → Señalar omisiones para verificación manual del investigador

## References
- Bases FONDECYT Regular 2027 (ANID) — criterios formales y de evaluación
- Protocolo de revisión (Acción_para_revision.md) — 23 criterios de evaluación
- Formulación del proyecto — documento base para revisión
