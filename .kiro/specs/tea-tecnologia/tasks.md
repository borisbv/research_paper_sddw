# Implementation Plan — tea-tecnologia (Fase: Marco Teórico)

Esta fase incremental produce exclusivamente el marco teórico del paper. Las tareas siguen el pipeline narrativo definido en el diseño (C1→C9) y los componentes transversales de estilo, citación, referencias y validación. El marcador `(P)` identifica tareas que pueden ejecutarse en paralelo una vez cumplidas sus precondiciones.

## Preparación

- [x] 1. Preparar el entorno documental del paper
- [x] 1.1 Inicializar el artefacto del marco teórico
  - Crear el archivo de trabajo que alojará el marco teórico dentro del directorio `paper/`.
  - Establecer la estructura mínima con un título de sección "Marco teórico" y marcadores internos para los nueve bloques narrativos C1..C9.
  - Fijar el idioma en español y reservar el espacio final para "Referencias bibliográficas" en APA.
  - _Requirements: 1.3, 3.3, 3.6_

- [x] 1.2 Preparar la base bibliográfica del paper
  - Asegurar la existencia del archivo BibTeX consolidado bajo `references/` donde se persistirán las citas verificadas.
  - Definir la convención de `bibKey` (autor_año_palabraclave) para evitar colisiones al añadir entradas.
  - Dejar documentado en un comentario del BibTeX que las fuentes deben priorizar revistas Scopus recientes.
  - _Requirements: 4.3, 4.6_

- [x] 1.3 Definir el presupuesto de palabras por componente narrativo
  - Repartir el objetivo global (aproximadamente 800 a 950 palabras) entre los nueve componentes C1..C9 reservando mayor densidad para C2, C5, C7, C8 y C9.
  - Registrar el presupuesto como anotación interna al inicio del archivo del marco teórico para guiar la redacción sin contaminar la prosa final.
  - _Requirements: 3.1, 3.2_

## Investigación bibliográfica dirigida

- [x] 2. Ejecutar búsqueda bibliográfica Scopus por componente
- [x] 2.1 (P) Recopilar fuentes para la definición general del TEA
  - Buscar literatura reciente sobre definición clínica y criterios diagnósticos del TEA.
  - Seleccionar al menos una fuente Scopus de los últimos años que sustente la definición de apertura.
  - Registrar las entradas verificadas en el archivo BibTeX con su `bibKey`.
  - _Requirements: 2.1, 4.1, 4.2, 4.3_

- [x] 2.2 (P) Recopilar fuentes sobre niños TEA
  - Buscar literatura sobre manifestaciones, necesidades y apoyos para niños TEA.
  - Verificar que cada fuente candidata pueda resolverse contra CrossRef o DOI.
  - Persistir las entradas seleccionadas en el BibTeX.
  - _Requirements: 2.2, 4.1, 4.2, 4.3_

- [x] 2.3 (P) Recopilar fuentes sobre prevalencia global del TEA
  - Reunir cifras recientes de prevalencia mundial y tendencias diagnósticas.
  - Priorizar fuentes epidemiológicas indexadas en Scopus.
  - Añadir entradas al BibTeX evitando duplicados con 2.1 y 2.2.
  - _Requirements: 2.3, 4.1, 4.2, 4.3_

- [x] 2.4 (P) Recopilar fuentes sobre TEA en Latinoamérica
  - Buscar estudios regionales recientes sobre prevalencia, diagnóstico y acceso a servicios.
  - Documentar brechas regionales observadas en la literatura.
  - Persistir entradas verificadas en el BibTeX.
  - _Requirements: 2.4, 4.1, 4.2, 4.3_

- [x] 2.5 (P) Recopilar fuentes sobre TEA en niños en Chile
  - Recolectar estudios nacionales sobre niños TEA en contexto chileno.
  - Incluir evidencia sobre prevalencia local y contexto educativo cuando sea indispensable para la narrativa.
  - Añadir entradas verificadas al BibTeX.
  - _Requirements: 2.5, 4.1, 4.2, 4.3_

- [x] 2.6 (P) Recopilar fuentes sobre modelos pedagógicos excluyentes
  - Buscar literatura que nombre modelos pedagógicos concretos que han dejado fuera a estudiantes TEA.
  - Preferir estudios críticos y revisiones recientes indexados en Scopus.
  - Persistir entradas en el BibTeX.
  - _Requirements: 2.6, 4.1, 4.2, 4.3_

- [x] 2.7 (P) Recopilar fuentes sobre adolescentes y universitarios TEA
  - Reunir literatura que aborde específicamente adolescentes TEA y estudiantes universitarios TEA.
  - Capturar evidencia sobre transiciones educativas y desafíos propios del grupo etario.
  - Añadir entradas verificadas al BibTeX.
  - _Requirements: 2.7, 4.1, 4.2, 4.3_

- [x] 2.8 Recopilar fuentes sobre tres tecnologías concretas con resultados reportados
  - Identificar al menos tres tecnologías o apps específicas con evidencia de resultados para adolescentes TEA.
  - Asegurar que cada tecnología cuente con al menos una cita Scopus reciente que describa sus resultados.
  - Persistir las entradas en el BibTeX manteniendo trazabilidad entre cada `bibKey` y la tecnología descrita.
  - Esta tarea no se marca como paralela porque la elección de las tres tecnologías condiciona la redacción de C8 y del cierre C9.
  - _Requirements: 2.8, 4.1, 4.2, 4.3_

- [x] 2.9 Consolidar la lista de claims pendientes de verificación
  - Revisar el borrador de claims por componente y marcar como pendientes aquellas sin fuente verificable.
  - Bloquear el avance a la fase de redacción final hasta resolver cada pendiente mediante nueva búsqueda o reformulación.
  - _Requirements: 4.4_

## Redacción de los componentes narrativos

- [ ] 3. Redactar el pipeline narrativo de lo general a lo específico
- [x] 3.1 Redactar C1 Definición TEA
  - Escribir el primer bloque con la definición clínica y conceptual del TEA.
  - Anclar la definición con al menos una cita APA verificada proveniente de 2.1.
  - Mantener prosa continua sin listas ni guiones como separadores.
  - _Requirements: 2.1, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.2 Redactar C2 Niños TEA
  - Caracterizar en prosa a la población infantil TEA y las implicancias del diagnóstico.
  - Enlazar con la definición sin repetirla.
  - Incorporar citas verificadas de 2.2.
  - _Requirements: 2.2, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.3 Redactar C3 TEA a nivel mundial
  - Presentar en prosa la prevalencia global y tendencias principales.
  - Convertir cifras en frases argumentales, evitando tablas o listas.
  - Usar las citas verificadas de 2.3.
  - _Requirements: 2.3, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.4 Redactar C4 TEA en Latinoamérica
  - Describir la situación regional contrastando con las cifras globales del bloque previo.
  - Señalar brechas de diagnóstico y atención documentadas en 2.4.
  - _Requirements: 2.4, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.5 Redactar C5 TEA en niños en Chile
  - Aterrizar la discusión al contexto chileno con foco en niños TEA.
  - Incluir evidencia nacional proveniente de 2.5.
  - Preparar el terreno para la discusión de modelos pedagógicos.
  - _Requirements: 2.5, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.6 Redactar C6 Modelos pedagógicos excluyentes
  - Nombrar modelos pedagógicos concretos que han dejado fuera a estudiantes TEA.
  - Sustentar cada señalamiento con citas recientes de 2.6.
  - Articular la transición hacia adolescentes TEA.
  - _Requirements: 2.6, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.7 Redactar C7 Adolescentes y universitarios TEA
  - Discutir adolescentes TEA y estudiantes universitarios TEA como foco del estudio.
  - Justificar el viraje del grupo etario con citas de 2.7.
  - _Requirements: 2.7, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.8 Redactar C8 Tecnologías y apps con tres ejemplos
  - Redactar el bloque breve sobre cómo las tecnologías tipo app pueden apoyar a adolescentes TEA.
  - Nombrar al menos tres tecnologías concretas con resultados reportados según 2.8.
  - Integrar cada tecnología en prosa continua, sin listas ni viñetas.
  - _Requirements: 2.8, 3.3, 3.4, 3.5, 4.1, 4.2_

- [x] 3.9 Redactar C9 Vacíos y propuesta
  - Cerrar el marco teórico enumerando en prosa los vacíos percibidos en la literatura revisada.
  - Articular explícitamente que la propuesta del paper busca evaluar si las tecnologías tipo app podrían ayudar a los adolescentes TEA.
  - Mantener coherencia con los bloques previos sin introducir conceptos nuevos.
  - _Requirements: 2.9, 5.1, 5.2, 5.3, 3.3, 3.4, 3.5_

## Componentes transversales

- [ ] 4. Aplicar estilo, citación y referencias
- [x] 4.1 Aplicar el contrato de estilo y formato
  - Revisar la prosa completa para eliminar guiones usados como separadores entre ideas o párrafos.
  - Convertir cualquier lista decorativa o enumeración con viñetas en prosa orgánica.
  - Asegurar párrafos largos y coherentes en español.
  - _Requirements: 3.3, 3.4, 3.5_

- [x] 4.2 Ajustar la extensión al objetivo de dos páginas
  - Medir el conteo de palabras del marco teórico y contrastar con el presupuesto definido en 1.3.
  - Si la extensión excede significativamente dos páginas, recortar priorizando densidad conceptual sobre enumeración.
  - _Requirements: 3.1, 3.2_

- [x] 4.3 Consolidar las citas APA en el cuerpo del texto
  - Revisar cada claim del marco teórico para confirmar que lleva una cita APA verificable.
  - Normalizar el formato de cita en el texto según reglas APA.
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [x] 4.4 Generar la sección "Referencias bibliográficas"
  - Compilar al final del archivo del marco teórico el listado de referencias utilizadas en formato APA.
  - Verificar que cada entrada de la sección tenga correspondencia uno a uno con el BibTeX consolidado.
  - _Requirements: 4.5, 4.6_

## Validación y cierre de la fase

- [ ] 5. Validar y cerrar la fase incremental del marco teórico
- [x] 5.1 Verificar alcance incremental de la fase
  - Confirmar que el único artefacto producido es el marco teórico y que no se han añadido introducción, metodología, resultados, discusión ni conclusiones.
  - Comprobar que el archivo del marco teórico permanece como unidad entregable independiente y no ha sido reescrito destructivamente.
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [x] 5.2 Ejecutar validaciones hard del framework
  - Correr la suite de validaciones hard del framework sobre el marco teórico.
  - Resolver cualquier cita que no verifique contra CrossRef o DOI antes de continuar.
  - Corregir cualquier violación detectada por la regla anti guiones separadores.
  - _Requirements: 6.1, 6.2, 6.3_

- [x] 5.3 Reportar el estado final de la fase
  - Emitir el reporte de estado del paper usando el comando de estado del framework.
  - Dejar constancia de que todas las validaciones hard han pasado y la fase queda disponible para extensiones futuras.
  - _Requirements: 6.4_
