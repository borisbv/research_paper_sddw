# Contexto Temporal de Investigación: IA y Accesibilidad Web

Este directorio contiene los insumos base para el desarrollo del artículo científico o capítulo de libro enfocado en la relación entre la Inteligencia Artificial y las pautas de accesibilidad web (WCAG 2.2).

## Contenido del Directorio

### 1. Dataset de Tecnologías (`AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv`)
Un archivo CSV que detalla 41 tecnologías de IA (Chat GPT, Copilot, Gemini, Neuralink, etc.) caracterizadas bajo los siguientes criterios:
- **Identificación:** Nombre, descripción, URL y modalidad de pago.
- **Caracterización Técnica:** Fortalezas, oportunidades, debilidades y versión.
- **Categorización por Accesibilidad:** Tipo de producto, tecnología IA y tipo de discapacidad asociada.
- **Evaluación de Usabilidad (ISO/W3C):** Precisión, sensibilidad, tiempo de respuesta y compatibilidad multidispositivo.
- **Cumplimiento WCAG:** Evaluación de Robustez y Operabilidad (Navegación por teclado, comandos de voz).

### 2. Guía de Trabajo (`instrucciones.md`)
Documento que define los requerimientos específicos para el producto académico final:
- Argumentación teórica basada en autores de alto impacto (Scopus/WoS Q1-Q2, últimos 5 años).
- Categorización de tecnologías por tipo de discapacidad.
- Selección de las 5 mejores tecnologías como referentes de buenas prácticas.
- Debate sobre el vacío de conocimiento (teórico y práctico) en el área.

## Uso en el Proyecto
Estos archivos deben ser utilizados como fuente primaria por el motor de generación (`scripts/` y `.kiro/`) para la construcción de las secciones de Metodología, Resultados y Discusión del documento objetivo (`/paper` o `/book`).
