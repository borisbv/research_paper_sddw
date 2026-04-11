# Research: Subsanar Hallazgos de Revisión

## 1. Contexto y Objetivos
Este documento registra la investigación realizada para abordar los hallazgos del Peer Review. Los objetivos principales son:
- Validar estándares de citación para testimonios en Revisiones Sistemáticas de Literatura (SLR).
- Identificar mejores prácticas para diagramas PRISMA en contextos cualitativos.
- Definir especificaciones técnicas para los activos visuales mandatorios.

## 2. Hallazgos de Investigación

### 2.1 Citación de Testimonios Secundarios
En una SLR, los testimonios no son datos primarios del autor, sino "hallazgos" de los estudios incluidos en el corpus.
- **Estándar:** Se debe citar al autor original del estudio donde aparece el testimonio. 
- **Formato Sugerido (Chicago):** "Como indica Cecilia (23 años) en el estudio de Pavez (2020)..." o "(Cecilia en Pavez 2020)".
- **Riesgo:** Si un testimonio no tiene fuente en el corpus de 160 artículos, se considera "dato huérfano" y debe eliminarse para mantener el rigor metodológico.

### 2.2 Diagrama de Flujo PRISMA 2020
El estándar PRISMA 2020 es aplicable a revisiones cualitativas.
- **Fases:** Identificación (Scopus + otras), Screening (Título/Abstract), Elegibilidad (Texto completo), Inclusión (Meta-análisis cualitativo).
- **Detalle Crítico:** Se debe reportar el número exacto de artículos excluidos en cada fase y los motivos principales (ej. "no cualitativo", "fuera del rango 2019-2024").

### 2.3 Diseño de Graphical Abstract (Social Sciences)
Para estudios de migración, el diseño debe ser conceptual y humano.
- **Dimensiones:** 1200x600 px (Relación 2:1).
- **Elementos:** Usar siluetas humanas, iconos de conectividad (señal wifi, smartphones) y flujos que conecten el "Origen" con el "Destino".
- **Paleta:** Tonos azules y tierra para denotar neutralidad académica.

### 2.4 Silos Informativos y Salud Pública
Los "silos informativos" (echo chambers) en comunidades migrantes ocurren por la confianza en redes cerradas frente a la desconfianza institucional.
- **Estrategia 1:** "Infomediarios" digitales (líderes comunitarios que replican info oficial).
- **Estrategia 2:** Adaptación transcultural de contenidos (info oficial en formatos consumibles como audios de WhatsApp o videos cortos).

## 3. Decisiones Técnicas
1. **Citación:** Se utilizará el formato "[Nombre en Autor Año]" para todos los testimonios de la sección 4.1.
2. **Visuales:** Se utilizará Python (Matplotlib/Plotly) o herramientas de diseño (Canva/BioRender) para generar los 5 activos. El script `scripts/generate_schematic.py` (si existe en el repo) será la primera opción.
3. **Abstract:** Se redactará una nueva versión en español de ~250 palabras incorporando los términos del corpus (Scopus, 2019-2024) y la síntesis de divergencias.

## 4. Referencias Consultadas
- PRISMA 2020 Statement.
- Elsevier Guidelines for Graphical Abstracts.
- Pavez (2020) - *El uso de redes sociales en migrantes Colombianos en Chile*.
