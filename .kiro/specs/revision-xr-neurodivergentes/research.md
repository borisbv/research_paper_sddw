# Research & Design Decisions

---
**Purpose**: Captura de hallazgos de análisis y decisiones de diseño que informan el plan de revisión del artículo.

---

## Summary

- **Feature**: `revision-xr-neurodivergentes`
- **Discovery Scope**: Revisión de documento existente (extensión/corrección de manuscrito científico)
- **Key Findings**:
  - El manuscrito presenta una tensión estructural entre el marco teórico de neurodiversidad (amplio) y los objetivos/conclusiones que se centran en TEA, cuando la muestra es 70 % TDAH y solo 28,57 % con diagnóstico de TEA.
  - La inconsistencia entre "control de estímulos" como criterio de diseño y el 40 % de participantes que reporta sobrecarga sensorial es tratable teóricamente: la heterogeneidad de perfiles neurodivergentes implica umbrales sensoriales distintos, y no constituye un error metodológico sino un hallazgo relevante.
  - La ausencia de base pedagógica explícita (DUA u otro marco) es la crítica de mayor peso estructural, ya que sin ella el artículo queda como un estudio de usabilidad sin valor pedagógico argumentado.

---

## Research Log

### Análisis de composición de la muestra vs. enfoque declarado

- **Context**: La editora señala que los objetivos, título y conclusiones se enfocan en TEA, mientras que solo 1 de los 3 user-personas representa TEA y el 70 % de participantes tiene TDAH.
- **Findings**:
  - Muestra: 70 % TDAH, 28,57 % de ese grupo también con TEA = ≈ 20 % TEA puro, 10 % Trastorno de Ansiedad, 20 % sin diagnóstico.
  - El artículo ya declara en la metodología: "estudio se desarrolló desde una perspectiva de neurodiversidad... incorporando la participación de estudiantes universitarios con distintos perfiles cognitivos".
  - Sin embargo, el título ("para estudiantes neurodivergentes") ya está bien orientado; el problema está en los objetivos internos y las conclusiones que vuelven a mencionar TEA como foco.
- **Implications**: Las modificaciones deben ser quirúrgicas: reformular objetivos específicos y depurar conclusiones de afirmaciones que generalicen a TEA cuando los datos se refieren a la muestra neurodivergente general.

### Inconsistencia control de estímulos / sobrecarga sensorial

- **Context**: El diseño incorporó estrategias de control de estímulos (colores moderados, transiciones suaves, estructura espacial clara). Sin embargo, 40 % reporta sobrecarga sensorial y colores como distractor.
- **Findings**:
  - Esta aparente contradicción es explicable: las estrategias de control de estímulos fueron diseñadas siguiendo perfiles con alta sensibilidad sensorial (principalmente TEA), pero el 70 % de participantes tiene TDAH, perfil que frecuentemente requiere mayor dinamismo y estímulo para mantener la atención.
  - Marwati et al. (2023) documentan que umbrales sensoriales varían significativamente incluso dentro del mismo diagnóstico.
  - Gonçalves & Monteiro (2023) subrayan que la atención en TEA difiere cualitativamente de la atención en TDAH.
- **Implications**: El diseño debe reencuadrar este hallazgo como evidencia de la necesidad de personalización sensorial adaptativa, no como fallo del diseño. Requiere añadir texto teórico sobre variabilidad sensorial inter-perfil.

### Ausencia de base pedagógica explícita

- **Context**: La editora señala que el texto prioriza interfaz/usabilidad pero descuida fundamentos pedagógicos. No se justifica por qué se seleccionaron los elementos ni qué competencias desarrollan.
- **Findings**:
  - El DUA (Universal Design for Learning) está mencionado en la Introducción pero no desarrollado como marco estructurante del diseño.
  - Las tres dimensiones DUA (representación, acción/expresión, participación) pueden mapearse directamente a los elementos del entorno XR: contenidos disciplinares 3D → representación; navegación activa → acción/expresión; co-diseño y evaluación participativa → participación.
  - El entorno trabaja contenidos de Forma, Color, Espacio y Composición (disciplinas de Arquitectura/Diseño): esto permite articular objetivos de aprendizaje específicos y no solo de accesibilidad.
- **Implications**: Requiere añadir una subsección en Fundamentación Teórica dedicada a DUA aplicado a XR, y reformular la descripción de las fases de ideación/prototipado para incluir la justificación pedagógica de cada elemento.

---

## Architecture Pattern Evaluation

| Opción de estructura de revisión | Descripción | Fortalezas | Riesgos |
|---|---|---|---|
| Revisión lineal sección por sección | Recorrer el manuscrito en orden y aplicar cambios | Simple de ejecutar | Puede introducir inconsistencias entre secciones si no se planifica globalmente |
| Revisión por eje de cambio | Primero resolver el eje conceptual (neurodiversidad vs TEA), luego pedagógico (DUA), luego formal (APA/normas) | Garantiza coherencia argumentativa antes de detalles formales | Requiere múltiples pasadas |
| Revisión modular por Requirement | Tratar cada Req como una tarea atómica con validación propia | Alta trazabilidad, más fácil de revisar por el editor | Puede generar redundancia si los Reqs afectan las mismas secciones |

**Selección**: Revisión modular por Requirement (Reqs 1–4 abordan contenido; Req 5–6 abordan forma), con una pasada de coherencia global al final.

---

## Design Decisions

### Decision: Orden de intervención en el manuscrito

- **Context**: Los 6 Reqs tienen dependencias entre sí: resolver el enfoque de neurodiversidad (Req 1) impacta en cómo se redactan los demás; la base pedagógica (Req 4) sostiene la justificación de necesidades (Req 2).
- **Alternatives Considered**:
  1. Orden de aparición en el texto (Intro → Fundamentos → Metodología → Resultados → Conclusiones)
  2. Orden por criticidad editorial (primero las observaciones del editor, luego las formales)
- **Selected Approach**: Orden de dependencia lógica: Req 4 (DUA) → Req 1 (coherencia) → Req 2 (justificación necesidades) → Req 3 (inconsistencia estímulos) → Req 5 (normas formales) → Req 6 (referencias).
- **Rationale**: El marco pedagógico DUA (Req 4) proporciona el vocabulario que se usará en Req 1, 2 y 3. Sin ese fundamento, las demás correcciones no tienen andamiaje teórico.
- **Trade-offs**: Implica modificar la Fundamentación Teórica antes que la Introducción, lo que puede requerir ajuste posterior de la Introducción.

### Decision: Tratamiento de la contradicción estímulos/sobrecarga (Req 3)

- **Context**: Dos opciones: (a) reconocer el hallazgo como limitación del diseño, o (b) reencuadrarlo como hallazgo teórico sobre heterogeneidad de perfiles.
- **Selected Approach**: Opción (b) — reencuadre teórico — con reconocimiento explícito de la tensión, no ocultarla.
- **Rationale**: La editora pide que "no termine de justificarse"; la solución es justificarlo explícitamente con teoría de variabilidad sensorial inter-perfil. Tratarlo solo como limitación debilitaría el argumento sin aportar conocimiento nuevo.

---

## Risks & Mitigations

- **Riesgo**: Las modificaciones al título y objetivos pueden requerir ajuste del Abstract y Keywords — Mitigación: incluir revisión de Abstract/Keywords como paso de verificación en Req 5.
- **Riesgo**: Agregar una subsección DUA puede exceder el límite de páginas de la revista (4–8 páginas) — Mitigación: la subsección DUA debe integrar/reemplazar texto ya existente sobre aprendizaje inclusivo, no sumarse como bloque adicional.
- **Riesgo**: Referencias nuevas sobre TDAH en educación superior pueden no estar disponibles con DOI verificable — Mitigación: priorizar fuentes ya citadas en el artículo (Cage & McManemy, 2022; Gonçalves & Monteiro, 2023) y ampliar su argumento antes de agregar referencias externas.

---

## References

- Marwati, A., Dewi, O. C., Wiguna, T., & Aisyah, A. (2023). Journal of Accessibility and Design for All — variabilidad sensorial en diseño de salas inclusivas.
- Gonçalves & Monteiro (2023). Journal of Neural Transmission — atención en TEA a lo largo del ciclo vital.
- CAST (2018). Universal Design for Learning Guidelines 2.2 — marco de referencia para DUA en diseño instruccional.
- Revista Gráfica UAB — Normas de estilo y directrices para autores (versión consultada: temp_context/normas_revista.md).
