# Requirements Document: Peer Review Resolution for 'Casa de Paso'

## Introduction
Este documento define los requisitos para resolver las observaciones del reporte de revisión por pares (`paper/review-report.md`). El objetivo es asegurar que el manuscrito cumpla con el anonimato estricto para la revisión doble ciego, aumente el rigor del análisis cualitativo y profundice la visión crítica sobre la Política Nacional de Migración y Extranjería (PNME) 2024-2025.

## Requirements

### Requirement 1: Anonimización Estricta (Double-Blind Review)
**Objective:** Como autor, quiero eliminar menciones institucionales para cumplir con el proceso de revisión ciega.

#### Acceptance Criteria
1.1 El sistema shall sustituir menciones a "Universidad Tecnológica Metropolitana (UTEM)" por descriptores genéricos (e.g., "una universidad pública chilena").
1.2 El sistema shall sustituir menciones a "Universidad de Wisconsin (UW-Milwaukee)" por descriptores genéricos (e.g., "una universidad estadounidense").
1.3 El sistema shall verificar que no existan nombres de autores o afiliaciones específicas en los archivos `paper/sections/*.md`.

### Requirement 2: Transparencia en el Análisis Cualitativo
**Objective:** Como investigador, quiero detallar el proceso de análisis de datos para aumentar el rigor metodológico.

#### Acceptance Criteria
2.1 El sistema shall explicitar la técnica de análisis de datos utilizada (e.g., análisis temático o teoría fundamentada).
2.2 El sistema shall describir el proceso de codificación de los verbatim (e.g., uso de códigos emergentes, triangulación entre investigadores).
2.3 La sección de **Metodología** shall incluir un párrafo denso (8-15 líneas) dedicado exclusivamente al proceso de síntesis cualitativa.

### Requirement 3: Profundización Crítica de la PNME 2024-2025
**Objective:** Como analista de políticas públicas, quiero identificar vacíos específicos en la normativa actual para fortalecer la discusión.

#### Acceptance Criteria
3.1 El sistema shall integrar al menos dos medidas específicas de la PNME 2024-2025 (Decreto 181) en la **Discusión**.
3.2 El manuscrito shall analizar críticamente cómo el prototipo "Casa de paso" resuelve vacíos en la regularización por razones humanitarias.
3.3 El sistema shall asegurar que la visión crítica mantenga el equilibrio académico sin caer en juicios de valor no fundamentados.

### Requirement 4: Consistencia en el Formato de Citas (APA 7)
**Objective:** Como autor académico, quiero unificar el formato de citas narrativas y parentéticas.

#### Acceptance Criteria
4.1 El sistema shall utilizar formato narrativo "Autor (Year)" cuando la cita forma parte de la estructura gramatical de la oración.
4.2 El sistema shall utilizar formato parentético `\cite{key}` (o el equivalente final `(Autor, Year)`) para respaldar afirmaciones de contexto.
4.3 El sistema shall asegurar que cada cita modificada tenga su entrada correspondiente en `references/references.bib`.

### Requirement 5: Consolidación de Antecedentes
**Objective:** Como autor, quiero resolver el vacío en `related-work.md` para mejorar la estructura del paper.

#### Acceptance Criteria
5.1 El sistema shall reubicar la revisión de literatura de la Introducción a la sección de **Related Work** o eliminar el archivo si la revista prefiere la integración total.
5.2 Si se mantiene la integración en la Introducción, el archivo `related-work.md` shall ser eliminado para evitar falsos positivos en la validación de estructura.
