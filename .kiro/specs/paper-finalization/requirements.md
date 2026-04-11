# Requirements Document: Paper Finalization and Translation

## Introduction
Este documento define los requisitos para el cierre y entrega final del proyecto "Arquitectura Humanitaria y Experiencia de Usuario". El objetivo es consolidar el trabajo realizado en un formato profesional listo para envío (Word), integrando todos los recursos visuales y bibliográficos, y proporcionando una versión traducida al inglés para aumentar su alcance internacional.

## Requirements

### Requirement 1: Consolidación y Preparación del Manuscrito (ES)
**Objective:** Como autor, quiero un archivo único consolidado, para facilitar la conversión a formatos finales.

#### Acceptance Criteria
1.1 El sistema shall consolidar todas las secciones de `paper/sections/*.md` en un único archivo `paper/manuscript_es.md`.
1.2 El sistema shall integrar el título, abstract y palabras clave de `paper/metadata.yaml` al inicio del manuscrito consolidado.
1.3 El sistema shall verificar que todas las referencias a figuras (`figure1`, `figure2`, `figure3`) estén correctamente vinculadas a los archivos en `figures/`.

### Requirement 2: Generación de Documento Word (ES)
**Objective:** Como autor, quiero un archivo DOCX, para cumplir con el formato de envío de la revista.

#### Acceptance Criteria
2.1 El sistema shall convertir `paper/manuscript_es.md` a `paper/manuscript_es.docx` utilizando Pandoc (o herramienta equivalente).
2.2 El documento Word shall incluir las imágenes de `figures/` con sus respectivos pies de figura (captions) definidos en los metadatos.
2.3 El documento shall generar automáticamente la sección de **Referencias Bibliográficas** en estilo APA 7th Edition a partir del archivo `.bib`.

### Requirement 3: Traducción Académica al Inglés (EN)
**Objective:** Como investigador, quiero una versión en inglés de alta calidad, para facilitar el envío a revistas internacionales.

#### Acceptance Criteria
3.1 El sistema shall traducir íntegramente el contenido de `paper/sections/*.md` al inglés, manteniendo el estilo científico y la densidad narrativa.
3.2 El sistema shall crear el archivo consolidado `paper/manuscript_en.md` con metadatos traducidos (Title, Abstract, Keywords).
3.3 El sistema shall asegurar que los términos técnicos (*User Experience*, *Design Thinking*) se mantengan en el formato correcto en inglés.

### Requirement 4: Generación de Documento Word (EN)
**Objective:** Como autor, quiero el archivo final en inglés en formato Word.

#### Acceptance Criteria
4.1 El sistema shall convertir `paper/manuscript_en.md` a `paper/manuscript_en.docx`.
4.2 El documento Word en inglés shall incluir las mismas figuras y la bibliografía en formato APA 7.
4.3 El sistema shall verificar que la traducción de los pies de figura sea precisa y profesional.

### Requirement 5: Validación Final de Entrega
**Objective:** Como responsable del proyecto, quiero asegurar la integridad de los archivos finales.

#### Acceptance Criteria
5.1 El sistema shall verificar la existencia de los cuatro archivos finales: `manuscript_es.md/docx` y `manuscript_en.md/docx`.
5.2 El sistema shall ejecutar una validación final de conteo de palabras en ambas versiones.
5.3 El sistema shall confirmar que no existen marcas institucionales (anonimización) en ninguna de las versiones finales.
