# Implementation Plan

## Requirements Coverage

| Requirement | Tareas |
|-------------|--------|
| 1 (Conformidad editorial RES) | 1.1, 10.1, 10.2 |
| 2 (Resumen extendido) | 9.1 |
| 3 (Introducción) | 3.1 |
| 4 (Marco teórico) | 4.1 |
| 5 (Metodología) | 5.1 |
| 6 (Resultados) | 6.1, 6.2 |
| 7 (Discusión) | 7.1 |
| 8 (Conclusión) | 8.1 |
| 9 (Referencias) | 2.1, 2.2, 10.2 |
| 10 (Material visual) | 6.2, 10.1 |
| 11 (Coherencia y convocatoria) | 3.1, 7.1, 10.1, 10.2 |

## Tasks

- [x] 1. Preparación de metadatos y estructura base
- [x] 1.1 Actualizar metadatos del paper y preparar estructura de archivos
  - Completar `metadata.yaml` con título bilingüe, palabras clave (4-6 en español e inglés), datos del autor y configuración Chicago Author-Date
  - Verificar que existen todos los archivos de secciones en `paper/sections/` según la estructura IMRaD adaptada del diseño
  - Crear el directorio `figures/` para el material visual
  - Establecer el orden de secciones y la plantilla base de cada archivo con encabezados y marcadores de extensión objetivo
  - _Requirements: 1.2, 1.4, 1.9_

- [x] 2. Construcción de la base bibliográfica
- [x] 2.1 Investigar y recopilar referencias verificables para el marco teórico
  - Buscar en bases de datos académicas (CrossRef, Semantic Scholar, Google Scholar) referencias de los tres campos disciplinares: antropología del habitar, estudios de migración y afecto, memoria/archivo/performance
  - Incluir autores clave del borrador: Bachelard, Bajani, Ahmed, De Certeau/Giard, Taylor, Sturken, Tronto
  - Buscar autores latinoamericanos de investigación-creación y estudios de migración en Chile
  - Asegurar balance geográfico: al menos 40% autores latinoamericanos
  - _Requirements: 9.1, 9.5, 9.6, 9.7_

- [x] 2.2 Construir el archivo references.bib con formato Chicago Author-Date
  - Crear entradas BibTeX con clave `Apellido_año` para las 25+ referencias recopiladas
  - Incluir nombres completos de autores y editores en todas las entradas
  - Agregar DOI cuando exista, verificado contra CrossRef
  - Validar formato Chicago Author-Date (última edición)
  - Asegurar que no se use op. cit., ibid., ni ibidem en ninguna convención de clave
  - Requiere: finalización de 2.1
  - _Requirements: 1.5, 1.6, 1.7, 1.8, 9.1, 9.2, 9.3, 9.4, 9.5_

- [x] 3. Redacción de la Introducción
- [x] 3.1 Escribir la sección de Introducción (~1.200 palabras)
  - Contextualizar la migración en América Latina y Chile como fenómeno con dimensión afectiva y simbólica, incluyendo datos estadísticos relevantes
  - Identificar el gap en la literatura: insuficiencia de aproximaciones artísticas y sensibles al estudio del habitar migrante
  - Formular la pregunta de investigación: ¿Cómo se reconstituye la memoria del habitar en la experiencia migrante a través de prácticas artísticas y narrativas?
  - Presentar la metáfora de "casas con piernas" como dispositivo analítico central, con apoyo conceptual en Bachelard y Bajani
  - Enunciar las tres contribuciones: metodología de investigación-creación sensible, arquetipos de casas narrativas, obra visual colectiva
  - Posicionar el artículo dentro de la convocatoria RES #100 y los ejes de migración y metodologías emergentes
  - Todas las afirmaciones teóricas respaldadas por citas Chicago Author-Date verificables
  - Reutilizar contenido conceptual del borrador original (`temp_context/paper_Erwin_23_Junio_2025.md`)
  - Agregar a references.bib las nuevas citas utilizadas (si las hay)
  - Requiere: tarea 2 completada
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 11.2, 11.3, 11.5_

- [x] 4. Redacción del Marco teórico y estado del arte
- [x] 4.1 Escribir la sección de Marco teórico (~1.500 palabras)
  - Articular tres campos disciplinares: (a) antropología del habitar y la casa (Bachelard, De Certeau/Giard), (b) estudios de migración y afecto (Ahmed), (c) memoria, archivo y performance (Taylor, Sturken)
  - Incluir revisión de la investigación-creación como metodología reconocida en ciencias sociales latinoamericanas
  - Situar la ética del cuidado (Tronto) como marco para el trabajo con testimonios migrantes
  - Posicionar el artículo en la intersección arte-antropología-narrativa visual, distinguiéndolo de estudios puramente sociológicos o artísticos
  - Incluir al menos 15 referencias verificables con balance geográfico
  - Mantener relación 1:1 entre citas en texto y entradas en references.bib
  - Construir esta sección desde cero (no existe en borrador), redistribuyendo autores del borrador original
  - Agregar a references.bib las nuevas citas utilizadas
  - Requiere: tarea 3 completada (conceptos introducidos en la Introducción)
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.6, 11.1_

- [x] 5. Redacción de la Metodología
- [x] 5.1 Escribir la sección de Metodología (~1.200 palabras)
  - Describir el enfoque como investigación-creación con metodología cualitativa mixta
  - Describir la muestra: 60 personas migrantes de diversas procedencias y edades, residentes en Santiago de Chile
  - Describir los tres instrumentos de recolección: (a) bitácoras con 5 preguntas abiertas, (b) entrevistas sensibles / diálogos simbólicos, (c) dibujo proyectivo
  - Incluir textualmente las 5 preguntas de las bitácoras: definición de casa, casa antes de partir, qué llevó consigo, casa ahora, casa soñada
  - Describir el proceso de análisis: ensamblaje simbólico y cartografía afectiva
  - Explicitar consideraciones éticas: consentimiento informado y ética del cuidado
  - Explicitar el rol del investigador como artista-participante con posición reflexiva
  - Fundamentar teóricamente cada instrumento con citas verificables (Taylor 2003, Tronto 1993, etc.)
  - Expandir la sección del borrador original (~300 palabras) a ~1.200 palabras
  - Consultar bitácoras en `temp_context/Dibujos casas/` para verificar las 5 preguntas exactas
  - Agregar a references.bib las nuevas citas utilizadas
  - Requiere: tarea 4 completada (marco conceptual que justifica instrumentos)
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8_

- [x] 6. Redacción de los Resultados
- [x] 6.1 Escribir los 5 arquetipos de casas narrativas (~1.750 palabras)
  - Desarrollar cada casa narrativa con ~350 palabras: Casa Posguerra, Casa de los Espíritus, Casa Contemporánea, Casa Padre/Madre, Casa Universo Paralelo
  - Para cada arquetipo incluir: (a) descripción del arquetipo, (b) tipo de experiencia migratoria que representa, (c) ejemplos concretos de las bitácoras o dibujos
  - Articular la relación entre palabra, dibujo y memoria como dimensiones complementarias del dato cualitativo
  - Referenciar la obra visual (dibujos) como parte integral de los hallazgos, no como mera ilustración
  - Incluir marcadores `[Insertar Imagen N aquí]` para los dibujos pertinentes con descripción contextual
  - Expandir los 5 arquetipos del borrador (actualmente listados sin desarrollo)
  - Vincular ejemplos concretos de las bitácoras reales
  - Requiere: tarea 5 completada (instrumentos que producen los datos)
  - _Requirements: 6.1, 6.2, 6.4, 6.5, 6.6, 10.1, 10.3_

- [x] 6.2 Escribir hallazgos transversales y cerrar la sección de Resultados (~50-100 palabras introductoria + integración)
  - Presentar hallazgos transversales que emergen del análisis: patrones comunes, tensiones y recurrencias simbólicas entre los 5 arquetipos
  - Escribir un párrafo introductorio que enmarque los resultados antes de los arquetipos
  - Verificar la extensión total de la sección (objetivo: ~1.800 palabras)
  - Requiere: tarea 6.1 completada
  - _Requirements: 6.3, 6.5_

- [x] 7. Redacción de la Discusión
- [x] 7.1 Escribir la sección de Discusión (~1.200 palabras)
  - Interpretar las casas narrativas como "tecnologías sensibles de memoria" en diálogo con Sturken y Taylor
  - Abordar las migraciones invisibles (desplazamientos internos no censados) como hallazgo emergente
  - Analizar los "objetos de orientación afectiva" (Ahmed) presentes en bitácoras y dibujos
  - Articular el arte como espacio de archivo, cura y denuncia en contextos migratorios
  - Discutir contribuciones al campo de las ciencias sociales latinoamericanas, enfoque transdisciplinar
  - Incluir explícitamente limitaciones: alcance de la muestra, contexto geográfico específico, subjetividad del análisis artístico
  - Proponer líneas de trabajo futuro
  - Retomar los conceptos del marco teórico (simetría argumentativa con sección 4)
  - Separar contenido interpretativo del borrador original (mover lo descriptivo a Resultados)
  - Agregar a references.bib las nuevas citas utilizadas
  - Requiere: tareas 4 y 6 completadas
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 11.1, 11.2, 11.4, 11.5_

- [x] 8. Redacción de la Conclusión
- [x] 8.1 Escribir la sección de Conclusión (~400 palabras)
  - Sintetizar la tesis central: migrar es una transformación profunda del habitar, no solo un desplazamiento territorial
  - Resumir la contribución metodológica: investigación-creación con bitácoras, entrevistas sensibles y dibujo proyectivo
  - Articular implicaciones prácticas para comunidades migrantes, educadores, terapeutas y artistas
  - No introducir información nueva ni citas no presentadas previamente
  - Extensión aproximada de 400 palabras (máximo 500)
  - Requiere: tarea 7 completada
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 9. Redacción del Resumen extendido bilingüe
- [x] 9.1 Escribir el abstract en español e inglés (250-300 palabras cada uno)
  - Redactar resumen extendido en español con secuencia: objetivo/contexto → metodología → conclusiones → originalidad
  - Traducir al inglés manteniendo estructura idéntica y verificando terminología académica
  - Comunicar la metáfora central de "casas con piernas" como dispositivo analítico
  - No incluir citaciones ni abreviaciones
  - Incluir palabras clave (4-6) en español e inglés
  - Incluir título bilingüe
  - Se escribe al final, como síntesis de todas las secciones del cuerpo
  - Requiere: tareas 3-8 completadas
  - _Requirements: 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 10. Validación integral y ajustes finales
- [x] 10.1 (P) Integrar material visual y verificar referencias de figuras
  - Definir la selección de 4-6 figuras: 1 bitácora escrita + 2-3 dibujos de participantes + 1-2 dibujos del investigador
  - Verificar que cada figura está referenciada en el texto con `[Insertar Imagen N aquí]`
  - Incluir descripción contextual de cada figura
  - Documentar requisitos técnicos: JPG o TIFF, 300 dpi, 240 px, archivo aparte
  - Verificar que los dibujos del investigador articulen la metáfora de "casas con piernas"
  - Verificar consentimientos informados (nota: los dibujos no incluyen rostros; bitácoras con nombres requieren autorización o anonimización)
  - Puede ejecutarse en paralelo con 10.2 (no comparten archivos)
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 1.11_

- [x] 10.2 (P) Validar coherencia, formato editorial y completitud bibliográfica
  - Verificar extensión total entre 7.000 y 10.000 palabras
  - Verificar conteo de palabras por sección (dentro de rangos del presupuesto de diseño)
  - Verificar relación 1:1 entre citas en texto y entradas en references.bib
  - Verificar formato Chicago Author-Date correcto en todas las citas
  - Verificar ausencia de op. cit., ibid., ibidem
  - Verificar presencia de DOI en referencias que lo tienen
  - Verificar coherencia argumentativa: la Discusión retoma el Marco teórico, los Resultados responden a la Metodología, la Conclusión se soporta en los Resultados
  - Verificar consistencia terminológica: hogar, habitar, casa, migración, archivo, memoria
  - Verificar lenguaje académico accesible a públicos de diferentes disciplinas
  - Verificar que el manuscrito dialoga con al menos dos ejes de la convocatoria RES #100
  - Aplicar correcciones necesarias en todas las secciones
  - Puede ejecutarse en paralelo con 10.1 (no comparten archivos)
  - _Requirements: 1.1, 1.5, 1.6, 1.7, 1.8, 1.10, 9.2, 9.3, 9.7, 11.1, 11.2, 11.3, 11.4, 11.5_
