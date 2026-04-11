# Technical Design: Adaptation of 'Casa de Paso'

## Architecture and Structure (IMRaD)
El paper seguirá la estructura estándar de la revista *Migraciones*, adaptando el contenido original a un formato académico riguroso.

| Section | Content Strategy |
| :--- | :--- |
| **Title** | "Arquitectura Humanitaria y Experiencia de Usuario: Un Prototipo de Vivienda Transitoria para la Integración Migrante en Chile". |
| **Abstract** | Refuerzo del impacto metodológico y el enfoque en políticas públicas. Máximo 250 palabras. |
| **Introduction** | Integración de la Política Nacional de Migración y Extranjería (PNME) 2024-2025 y el contexto del déficit habitacional en Chile. |
| **Methods** | Descripción detallada de la Metodología UX aplicada al diseño arquitectónico (5 etapas), destacando el rigor interdisciplinar. |
| **Results** | Presentación de las tres categorías (hogar temporal, vivienda modular, vida cívica) y el prototipo final, integrando verbatim cualitativos. |
| **Discussion** | Análisis crítico sobre la desconexión entre la arquitectura de emergencia y las políticas públicas de integración a largo plazo. |
| **Conclusions** | Recomendaciones para replicabilidad y escalamiento del prototipo en contextos de crisis migratoria global. |

## Content Transformation Rules
Para cumplir con los requisitos de estilo de prosa fluida y técnica:
1. **Densidad Narrativa:** Transformar listas y bullets del manuscrito original en párrafos continuos de 8-15 líneas.
2. **Conectores Lógicos:** Insertar transiciones académicas obligatorias al inicio de cada bloque temático.
3. **Formatos Visuales:** Aplicar negrita para categorías (**hogar temporal**) y cursiva para tecnicismos (*User Experience*).
4. **Citas de Participantes:** Sangrado independiente y formato anónimo: "(Hombre inmigrante, entre 40-50 años)".

## Interface Contracts (Paper Components)
- **Metadata:** `paper/metadata.yaml` debe incluir los nuevos descriptores de la revista *Migraciones*.
- **Citations:** Uso exclusivo de BibTeX gestionado por el script `tidy-bib.py`.
- **Validation Pipeline:**
  - `python scripts/validate-prose.py`
  - `python scripts/validate-word-count.py`
  - `python scripts/validate-citations.py`

## Risks and Mitigations (Design Specific)
- **Anonymization Risk:** La fase de diseño exige la eliminación de marcas institucionales en el texto (UTEM, UW-Milwaukee) para cumplir con el protocolo de revisión doble ciego.
- **Critical Vision Balance:** Se utilizará el skill `scientific-critical-thinking` para asegurar que el análisis de políticas públicas no opaque la contribución técnica de arquitectura.
