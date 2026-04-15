# Research & Design Decisions — libro-marketing-creadores

---

## Summary

- **Feature**: `libro-marketing-creadores`
- **Discovery Scope**: New Feature (proyecto editorial greenfield)
- **Key Findings**:
  - La arquitectura editorial debe adaptarse al patrón de "capas progresivas" (Comprender → Conectar → Distribuir → Convertir → Escalar), donde cada capa presupone la anterior.
  - El recurso narrativo "Anatomía de una publicación" funciona como interfaz unificadora entre capítulos, garantizando consistencia de experiencia de lectura.
  - El mayor riesgo del proyecto es la obsolescencia de datos de plataformas; se requiere un sistema de fechado y modularidad que permita actualizaciones parciales.

---

## Research Log

### Estructura editorial para libros de nivel intermedio en marketing digital

- **Context**: Determinar qué estructura editorial maximiza retención y aplicación para creadores de contenido con experiencia previa.
- **Sources Consulted**: Análisis de las dos propuestas base (esquema.md, esquema2.md), convenciones editoriales de libros aplicados (no académicos).
- **Findings**:
  - Los libros que combinan teoría con casos prácticos tienen mayor retención según estudios de diseño instruccional.
  - La estructura de 5 partes con 25 capítulos ofrece un equilibrio entre profundidad y manejabilidad (vs. 38 capítulos del esquema 1 que arriesga abandono).
  - Cada capítulo debe ser autocontenido pero referenciado cruzadamente (el lector puede leer de forma no lineal).
- **Implications**: La estructura de capítulo de 5 bloques (caso, concepto, aplicación, errores, ejercicio) se adopta como patrón estándar. La extensión objetivo por capítulo es 4.000-6.000 palabras.

### Integración tridimensional como principio de diseño

- **Context**: Ambas propuestas originales tratan las dimensiones (emocional, estratégica, negocio) por separado. Se necesita un mecanismo de integración.
- **Sources Consulted**: Spec integrado (temp/spec-libro-marketing-creadores.md), análisis comparativo de esquemas.
- **Findings**:
  - La integración no debe ser forzada: cada capítulo tiene un eje dominante pero incluye conexiones explícitas con los otros dos.
  - El mecanismo de "Anatomía de una publicación" permite analizar un mismo caso desde las tres dimensiones.
  - Las "notas de conexión" al final de cada capítulo (ej: "Esto conecta con el capítulo X") refuerzan la tridimensionalidad sin sobrecargar cada sección.
- **Implications**: Se definen tres tipos de conexión inter-capítulo: (1) referencia directa, (2) caso compartido analizado desde otro eje, (3) nota de conexión explícita.

### Gestión de obsolescencia en contenido de plataformas

- **Context**: Los algoritmos de Instagram, TikTok y YouTube cambian frecuentemente. El libro necesita un diseño que resista obsolescencia.
- **Sources Consulted**: Prácticas editoriales de libros técnicos con contenido volátil.
- **Findings**:
  - Los principios subyacentes (señales de calidad, retención, engagement) cambian menos que las tácticas específicas.
  - Un sistema de "fecha de referencia" por dato específico permite al lector evaluar vigencia.
  - Los capítulos de la Parte III (Distribuir) son los más vulnerables a obsolescencia.
- **Implications**: La Parte III se diseña con separación explícita entre principios (estables) y datos específicos (fechados). Se recomienda que el libro incluya un recurso digital actualizable como complemento.

### Mercado editorial competidor

- **Context**: Necesario validar que el posicionamiento diferencial (marco tridimensional) sea real.
- **Sources Consulted**: Análisis conceptual de libros existentes en el espacio.
- **Findings**:
  - Libros de marketing emocional (ej: *Contagious* de Berger) no abordan creación de contenido.
  - Libros de creadores (ej: guías de YouTube/Instagram) son tácticos y no integran psicología.
  - Libros de monetización para creadores son recientes pero no cubren la dimensión emocional.
  - No se identifica un competidor directo que integre las tres dimensiones para el mercado hispanohablante.
- **Implications**: El posicionamiento diferencial se confirma. El riesgo de competencia directa es bajo; el riesgo mayor es la competencia indirecta de cursos online y contenido gratuito.

---

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos / Limitaciones | Notas |
|--------|-------------|-----------|------------------------|-------|
| Estructura lineal pura (como esquema 2) | 5 fases secuenciales estrictas | Clara progresión, fácil de seguir | Limita lectura no lineal; temas aislados entre sí | Buena base pero insuficiente para integración tridimensional |
| Estructura modular por tema (como esquema 1) | 10 partes temáticas independientes | Profundidad por tema, permite saltar | Fragmentación excesiva; pierde visión sistémica | Demasiados capítulos, riesgo de abandono |
| **Estructura híbrida progresiva** | 5 partes como fases + integración transversal mediante recurso narrativo y conexiones explícitas | Combina progresión con profundidad; soporta lectura lineal y por consulta | Requiere diseño cuidadoso de conexiones cruzadas | **Seleccionada** — mejor equilibrio entre las fortalezas de ambos esquemas |

---

## Design Decisions

### Decision: Estructura de 5 partes con 25 capítulos

- **Context**: Esquema 1 propone 38 capítulos (excesivo) y Esquema 2 propone 20 (insuficiente en algunas áreas).
- **Alternatives Considered**:
  1. 38 capítulos en 10 partes (esquema 1 original)
  2. 20 capítulos en 5 fases (esquema 2 original)
  3. 25 capítulos en 5 partes (síntesis)
- **Selected Approach**: 25 capítulos en 5 partes, agrupando temas fragmentados y eliminando redundancias.
- **Rationale**: 25 capítulos permite cubrir todos los temas clave sin diluir ni sobrecargar. La distribución 5-6-6-5-3 refleja el peso relativo de cada eje.
- **Trade-offs**: Algunos temas del esquema 1 (ej: capítulos dedicados a cada emoción individual) se comprimen en secciones dentro de capítulos más amplios.
- **Follow-up**: Validar la extensión estimada total (100.000-150.000 palabras) con el perfil editorial del proyecto.

### Decision: Recurso narrativo "Anatomía de una publicación"

- **Context**: El esquema 1 propone este recurso como apertura de capítulo. Se evalúa su viabilidad como patrón transversal.
- **Alternatives Considered**:
  1. Apertura con dato estadístico impactante
  2. Apertura con "Anatomía de una publicación"
  3. Apertura mixta (alternar entre caso y dato)
- **Selected Approach**: Apertura con "Anatomía de una publicación" en todos los capítulos, complementada con un dato de investigación dentro del cuerpo.
- **Rationale**: El caso concreto ancla cada capítulo en la realidad del creador, haciendo tangible lo conceptual desde la primera línea.
- **Trade-offs**: Requiere curación de 25 casos (reales o ficticios bien construidos), lo que demanda investigación adicional.
- **Follow-up**: Definir criterios de selección de casos y banco de casos candidatos durante la fase de investigación.

### Decision: Sistema de conexiones inter-capítulo

- **Context**: El requerimiento 1 exige integración tridimensional. Se necesita un mecanismo que no sobrecargue cada capítulo.
- **Alternatives Considered**:
  1. Repetir las tres dimensiones en cada capítulo (exhaustivo pero pesado)
  2. Notas al margen con conexiones (sutil pero fácil de ignorar)
  3. Sistema mixto: eje dominante + conexiones explícitas + casos compartidos
- **Selected Approach**: Cada capítulo tiene un eje dominante. Al final incluye una sección "Conexiones" (2-3 bullets) que enlaza con capítulos de otros ejes. Algunos casos de "Anatomía" se retoman en capítulos posteriores desde otra dimensión.
- **Rationale**: Mantiene la profundidad por capítulo sin sacrificar la visión integradora. El lector puede seguir los hilos transversales o ignorarlos.
- **Trade-offs**: Requiere planificación editorial precisa para que las conexiones sean orgánicas, no forzadas.

### Decision: Separación principios vs. datos fechados (Parte III)

- **Context**: La Parte III (Distribuir) contiene información de algoritmos que caduca rápidamente.
- **Alternatives Considered**:
  1. Evitar datos específicos de algoritmos (pierde utilidad)
  2. Incluir datos con fechas de referencia (útil pero envejece)
  3. Separar principios estables de datos específicos + recurso digital complementario
- **Selected Approach**: Opción 3 — cada capítulo de Parte III separa "principios" (estables) de "estado actual" (fechado). Se recomienda un recurso digital actualizable como complemento.
- **Rationale**: Maximiza la vida útil del libro físico mientras ofrece valor actualizado vía digital.
- **Trade-offs**: Requiere mantener un recurso digital post-publicación.

---

## Risks & Mitigations

- **Obsolescencia de datos de plataformas** — Diseño modular con separación principios/datos + recurso digital actualizable.
- **Extensión excesiva del manuscrito** — Límite estricto de 4.000-6.000 palabras por capítulo; total objetivo 100.000-150.000 palabras.
- **Falta de fuentes para mercado LATAM** — Incluir como tarea de investigación prioritaria; considerar datos propios si las fuentes son insuficientes.
- **Dificultad para calibrar el tono** — Definir guía de estilo antes de redactar; testear capítulo piloto con lectores beta antes de escribir el resto.
- **Competencia de cursos online gratuitos** — El libro se posiciona como recurso de profundidad y sistema (no tips sueltos); los anexos descargables agregan valor diferencial.

---

## References

- Spec integrado del proyecto: `temp/spec-libro-marketing-creadores.md`
- Propuesta original 1 (emocional): `temp/esquema.md`
- Propuesta original 2 (estratégica): `temp/esquema2.md`
- Berger, J. (2013). *Contagious: Why Things Catch On*
- Eyal, N. (2014). *Hooked: How to Build Habit-Forming Products*
- Miller, D. (2017). *Building a StoryBrand*
- Cialdini, R. (2006). *Influence: The Psychology of Persuasion*
