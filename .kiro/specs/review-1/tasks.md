# Implementation Plan — review-1

> **Presupuesto global de palabras:** ~580 palabras de expansión sobre el estado actual (~9.420) para no superar el techo de 10.000 de RES. Cada tarea tiene un presupuesto asignado en sus bullets de detalle.
>
> **Orden de ejecución:** Las tareas 1 y 2 son secuenciales (bloqueantes). Las tareas 3, 4 y 6 pueden ejecutarse en paralelo con ellas o entre sí. La tarea 5 debe esperar a que la tarea 2 libere `discussion.md`. La tarea 7 es la verificación final.

---

- [x] 1. Resolver la inconsistencia del caso "Daniel" entre Resultados y Discusión
- [x] 1.1 Confirmar con el autor el número de participante correspondiente a "Daniel" y el fragmento empírico que será citado
  - Obtener del autor el número exacto de participante y la transcripción literal del fragmento de bitácora o diálogo simbólico.
  - Verificar que el fragmento describe un desplazamiento sin cruce de frontera internacional (migración interna, cambio de barrio, desplazamiento doméstico).
  - Confirmar el instrumento correcto (bitácora o diálogo simbólico) para la etiqueta de citación.
  - _Requirements: 1.1, 1.2_
- [x] 1.2 Insertar el fragmento del participante en la subsección Casa Contemporánea de Resultados
  - Ubicar la inserción inmediatamente después del testimonio del Participante 35 y antes del párrafo analítico de cierre de la subsección.
  - Presentar el fragmento en formato blockquote con etiqueta estandarizada `(Participante N, bitácora)` o `(Participante N, diálogo simbólico)`.
  - Mantener el volumen entre 40 y 80 palabras para no alterar el presupuesto global.
  - _Requirements: 1.2, 1.5, 5.5_
- [x] 1.3 Reemplazar el nombre propio "Daniel" por el número de participante en toda la Discusión
  - Sustituir todas las ocurrencias de "Daniel" y "la madre de Daniel" por la fórmula "la madre de la Participante N" (o equivalente gramatical).
  - Verificar que tras la sustitución ningún nombre propio no anonimizado permanece en la subsección "Migraciones invisibles".
  - _Requirements: 1.1, 1.4_
- [x] 1.4 Validar la trazabilidad bidireccional Resultados ↔ Discusión
  - Comprobar que cada mención del Participante N en la Discusión tiene su fragmento empírico ya presente en Resultados.
  - Ejecutar una búsqueda global del nombre "Daniel" en todos los archivos del manuscrito para asegurar cero ocurrencias residuales.
  - _Requirements: 1.4, 1.5_

- [x] 2. Desarrollar el concepto de "migraciones invisibles" con definición precisa y soporte empírico
- [x] 2.1 Redactar la definición conceptual de "migraciones invisibles" en la Discusión
  - Añadir 2 o 3 oraciones que definan el concepto distinguiéndolo de la migración internacional convencional.
  - Articular la definición en diálogo con Grimson (2011) y De Certeau, Giard y Mayol (1998), ya citados en el marco teórico.
  - Integrar la definición en el flujo argumentativo existente sin reescribir la subsección completa.
  - _Requirements: 4.2_
- [x] 2.2 Reforzar el soporte empírico del concepto con al menos un fragmento adicional
  - Identificar en el corpus un segundo fragmento (de otro participante o del propio Participante N de la tarea 1) que ilustre un desplazamiento sin cruce de frontera internacional.
  - Si el corpus solo contiene un caso, reconocerlo explícitamente como limitación dentro de la propia subsección o en la sección de limitaciones de la Discusión.
  - Asegurar que el concepto ya no dependa exclusivamente del caso del Participante N y que lo enunciado en el Abstract sea reproducible desde el cuerpo del artículo.
  - Mantener el volumen total de las adiciones en esta subsección entre 80 y 120 palabras.
  - _Requirements: 4.1, 4.3, 4.4, 4.5_

- [x] 3. (P) Hacer transparente el proceso analítico y añadir nota de doble naturaleza del material visual en Metodología
- [x] 3.1 (P) Redactar un párrafo que describa las etapas del ensamblaje simbólico y sensible
  - Incluir al menos cuatro etapas: lectura y familiarización, identificación de patrones simbólicos, agrupación en arquetipos provisionales, y revisión frente al corpus completo.
  - Especificar cómo se integraron los dibujos proyectivos respecto a las bitácoras y transcripciones (análisis paralelo, integrado o secuencial).
  - Añadir una oración sobre el mecanismo de reflexividad empleado por el investigador-creador para distinguir interpretación artística de patrones emergidos del corpus.
  - Insertar el párrafo dentro de la subsección "Método de análisis" tras el primer párrafo de definición del método.
  - Mantener el volumen del párrafo en 80-100 palabras.
  - _Requirements: 2.1, 2.2, 2.3, 2.5_
- [x] 3.2 (P) Añadir nota de doble naturaleza del material visual antes de Consideraciones éticas
  - Redactar 2 a 4 oraciones que distingan explícitamente los dibujos de participantes (evidencia empírica) de las ilustraciones del investigador (dispositivo artístico-conceptual).
  - Situar la nota inmediatamente antes del encabezado "Consideraciones éticas" de Metodología.
  - Mantener el volumen entre 30 y 50 palabras.
  - _Requirements: 3.4_
- [x] 3.3 (P) Verificar la cobertura de limitaciones sobre triangulación analítica
  - Revisar la subsección de Limitaciones de Metodología para confirmar que ya reconoce la ausencia de triangulación externa o revisión por pares del análisis.
  - Si la cobertura es insuficiente, añadir una oración complementaria sin exceder 20 palabras.
  - Verificar que el conteo total de Metodología queda dentro del rango 1.500-1.700 palabras tras todas las adiciones.
  - _Requirements: 2.4, 2.6_

- [x] 4. (P) Ampliar el Marco teórico hasta cumplir el target de palabras
  - Añadir 130-150 palabras sustantivas dentro de la subsección "Investigación-creación como producción legítima de conocimiento" o de "Vacío de investigación".
  - Priorizar el desarrollo del estado de la investigación-creación en ciencias sociales chilenas contemporáneas o la articulación novedosa del dispositivo "casas con piernas".
  - No introducir referencias bibliográficas nuevas sin verificación DOI; si se añaden, marcarlas para verificación posterior del autor.
  - Verificar que tras la adición el conteo de Marco teórico es ≥ 1.450 palabras y que el contenido añadido aporta argumentación sin relleno.
  - _Requirements: 5.1, 5.4_

- [x] 5. Diferenciar epistémicamente las ilustraciones del investigador de los dibujos de participantes
- [x] 5.1 Actualizar los pies de figura de las ilustraciones del autor con frase estandarizada
  - Modificar el pie de la Figura 4 en Introducción para añadir al final: "No constituye dato empírico del trabajo de campo."
  - Modificar los pies de las Figuras 5 y 6 en Discusión aplicando el mismo cierre.
  - Simplificar redundancias con la frase "Archivo plástico del investigador" ya presente, consolidando en una sola oración por pie.
  - _Requirements: 3.1, 3.6_
- [x] 5.2 Verificar y reforzar las etiquetas empíricas de los dibujos de participantes
  - Comprobar que los pies de las Figuras 1, 2 y 3 en Resultados incluyen la fórmula "Reproducido con consentimiento informado" y la identificación por participante.
  - Si alguna etiqueta es inconsistente con el patrón, normalizarla sin modificar el contenido descriptivo.
  - _Requirements: 3.2, 3.6_
- [x] 5.3 Revisar las oraciones de encuadre en Introducción y Discusión que presentan las figuras autorales
  - Confirmar que cada aparición de las Figuras 4, 5 y 6 en el cuerpo del texto está introducida por una oración que las enmarca explícitamente como archivo plástico del investigador.
  - Si alguna introducción textual es ambigua, reforzarla con una frase breve sin aumentar más de 10 palabras por figura.
  - Documentar la decisión del autor sobre reubicar o no la Figura 4 en Introducción; si decide mantenerla, asegurar que la oración de encuadre compensa la interrupción del flujo argumentativo.
  - _Requirements: 3.3, 3.5_

- [x] 6. (P) Completar los metadatos y requisitos formales pre-envío
- [x] 6.1 (P) Completar los campos de procedencia del manuscrito
  - Reemplazar los valores `[PENDIENTE]` del bloque `procedencia` con el nombre del proyecto de investigación y la institución financiadora (o indicación de ausencia de financiamiento si aplica).
  - Mantener el resto de metadatos del manuscrito sin modificar.
  - _Requirements: 6.1_
- [x] 6.2 (P) Confirmar el año de creación de las ilustraciones del autor
  - Verificar en el catálogo de figuras el año de creación de las Figuras 4, 5 y 6 y actualizarlo si está pendiente.
  - Sincronizar los pies de figura del manuscrito con el año confirmado si difieren.
  - _Requirements: 6.5_
- [x] 6.3 (P) Añadir statement de conflicto de intereses al manuscrito
  - Insertar una declaración corta de conflicto de intereses en la ubicación que la revista requiere (nota al pie de la primera página o sección dedicada).
  - Si no existe conflicto, usar la fórmula estándar "El autor declara no tener conflictos de intereses en relación con este trabajo".
  - _Requirements: 6.2_
- [x] 6.4 (P) Preparar el checklist de materiales de envío fuera del manuscrito Markdown
  - Registrar en una lista de verificación pre-envío: conversión de Figuras 1-3 de PNG a JPG o TIFF a 300 dpi, verificación de resolución de Figuras 4-6, preparación de formularios de consentimiento como anexos si la revista lo requiere.
  - No ejecutar las conversiones dentro del manuscrito Markdown; dejar constancia para el autor.
  - _Requirements: 6.3, 6.4_

- [x] 7. Validar el conteo global de palabras y la coherencia integral del manuscrito
  - Contar el total de palabras del manuscrito tras todas las ediciones anteriores y confirmar que el resultado está dentro del rango 7.000-10.000 palabras exigido por RES.
  - Confirmar que Marco teórico ≥ 1.450 palabras y que Resultados ≥ 1.900 palabras tras las adiciones de las tareas 1 y 4.
  - Si el total supera 10.000 palabras, ajustar reduciendo en la Discusión o la Conclusión sin afectar las adiciones críticas de las tareas 1, 2 y 3.
  - Ejecutar una lectura final de coherencia entre Abstract, Resultados y Discusión para confirmar que ninguna mención del caso del Participante N ni del concepto de "migraciones invisibles" quedó sin soporte.
  - Confirmar la ausencia de cualquier nombre propio no anonimizado en el manuscrito completo.
  - _Requirements: 1.5, 2.6, 4.5, 5.2, 5.3, 5.4_
