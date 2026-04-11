# Proyecto: Casa de Paso - Consolidación de Artículo Científico

Este repositorio contiene los materiales para la consolidación y validación del artículo científico **"Casa de paso: Prototipo de vivienda temporal para la población migrante en Chile desde la experiencia del usuario"**, con el objetivo de ser sometido a la revista **Migraciones** (indexada en Scopus Q1/Q2).

## 📄 Documentos Principales
- **[`Casa de paso_septiembre_2024.md`](Casa%20de%20paso_septiembre_2024.md)**: Versión avanzada del manuscrito que describe la investigación exploratoria y la aplicación de la metodología UX en el diseño arquitectónico.
- **[`normas_revista.md`](normas_revista.md)**: Requisitos específicos de la revista *Migraciones* (Instituto Universitario de Estudios sobre Migraciones, Universidad Pontificia Comillas).

## 🖼️ Contexto Visual (Imágenes del Proyecto)
El proyecto utiliza una fuerte base visual para comunicar la metodología UX y el diseño final:

1.  **[Figura 1: Categorías de Análisis](image1.jpg)**: Diagrama conceptual que ilustra los tres pilares derivados de los grupos focales: *Hogar temporal*, *Vivienda modular* y *Vida cívica*.
2.  **[Figura 2: Moodboard / Lienzo de Inspiración](image3.jpg)**: Collage visual con colores vibrantes y texturas que capturan la esencia cultural caribeña y principios de diseño universal, sirviendo como guía estética para el prototipo.
3.  **[Figura 3: Prototipo de Alta Fidelidad](image2.jpg)**: Fotografías de la maqueta física a escala (1:100) que muestra la estructura geodésica, el sistema modular de ensamble y la integración de espacios comunes.

## 🛠️ Plan de Trabajo para la Consolidación

Para adaptar el manuscrito a los estándares de *Migraciones*, se deben ejecutar las siguientes acciones:

### 1. Adaptación Normativa
- **Título**: Ajustar para reflejar un nivel académico superior (ej: "Arquitectura Humanitaria y Experiencia de Usuario: Un Prototipo de Vivienda Transitoria para la Integración Migrante en Chile").
- **Estructura IMRyD**: Asegurar que la transición entre métodos, resultados y discusión cumpla con el rigor interdisciplinar de la revista.
- **Citas y Referencias**: Validar que todas las citas sigan el formato requerido y enriquecer el `.bib` con DOIs faltantes.

### 2. Fortalecimiento Teórico y Crítico
- **Políticas Públicas**: Integrar una sección crítica sobre cómo este prototipo dialoga con las políticas habitacionales actuales en Chile y su impacto en la regularización migratoria.
- **Visión Crítica**: Profundizar en el análisis de la vivienda no solo como objeto físico, sino como herramienta de comunicación y dignidad humana.

### 3. Validación Técnica (Scripts)
Se deben ejecutar los scripts de validación del repositorio para asegurar la calidad:
- `python scripts/validate-structure.py`: Verificar estructura SDD.
- `python scripts/validate-word-count.py`: Asegurar que se mantiene dentro de los límites de la revista.
- `python scripts/validate-prose.py`: Garantizar una redacción fluida (evitar bullets en el cuerpo del manuscrito).
- `python scripts/validate-citations.py`: Confirmar consistencia bibliográfica.

---
*Este proyecto sigue la metodología Spec-Driven Development (SDD) para garantizar la trazabilidad entre requisitos de la revista y el contenido del paper.*
