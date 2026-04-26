# 🏗️ Arquitectura del SRGE (Scientific Research Generation Engine)

Este sistema utiliza un enfoque de **Desacoplamiento de Contenido y Lógica**.

## Capas del Sistema

### 1. Capa de Contenido (Target-Specific)
Reside en `/paper` o `/book`. Estas carpetas son contenedores aislados que contienen la "verdad" de la investigación:
- **Metadata**: Define autores, objetivos y configuración del manuscrito.
- **Sections**: Archivos Markdown modulares (ej: `01-intro.md`, `02-methods.md`).
- **Assets**: Figuras (`figures/`), Referencias (`references/`) y Datos (`data/`).

### 2. Capa de Lógica (Scientific Logic)
Reside en `scripts/`. Contiene el motor determinista:
- **Validation Suite**: Scripts que aplican reglas estrictas sobre el contenido (ej. "Toda figura en `figures/` debe ser citada en `sections/`").
- **Orchestration**: El `manager.py` centraliza estas tareas para evitar duplicidad de esfuerzos y gasto innecesario de tokens de IA.

### 3. Capa Cognitiva (AI Skills & SDD)
Reside en `.gemini/skills/` y `.kiro/`. Proporciona la inteligencia necesaria para:
- Análisis de Gaps científico.
- Refinamiento de tono académico.
- Generación de hipótesis.
- Gestión de cumplimiento de estándares (PRISMA, CONSORT).

## Flujo de Datos
1. La IA utiliza las **Skills** para generar borradores en `/sections`.
2. El usuario o la IA ejecutan el **Manager** para validar.
3. El **Manager** invoca a **Quarto** para transformar Markdown en el formato de publicación final.