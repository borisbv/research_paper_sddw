# Technical Design: Subsanar Hallazgos de Revisión

## 1. Arquitectura de la Solución
La solución se basa en una edición quirúrgica de los archivos de texto (Markdown) y la generación de activos externos (Figuras) que se integrarán en el manuscrito final.

### 1.1 Flujo de Trabajo (SDD-TDD)
1.  **RED:** Crear tests que validen el conteo de palabras del abstract y la presencia de figuras.
2.  **GREEN:** Implementar los cambios en el texto y generar los archivos de imagen.
3.  **REFACTOR:** Ajustar la prosa para fluidez y asegurar cumplimiento de normas Chicago.

## 2. Componentes de Diseño

### 2.1 Módulo 1: Expansión de Abstract (`paper/sections/abstract.md`)
- **Input:** Abstract actual de ~120 palabras.
- **Output:** Abstract de ~250 palabras.
- **Estructura:** Contexto (30w) -> Objetivo (20w) -> Metodología SLR detallada (60w) -> Resultados por categorías (100w) -> Conclusión e impacto (40w).

### 2.2 Módulo 2: Normalización de Citación (`paper/sections/results.md`)
- **Acción:** Identificar testimonios en 4.1.
- **Mapeo:**
    - Cecilia (23) -> Citar [Pavez 2020].
    - Jackie (35) -> Citar [Pavez 2020].
    - José (35) -> Citar [Pavez 2020].
    - Patricia (47) -> Citar [Pavez 2020].
- **Nota:** Si se detectan testimonios sin fuente en el corpus, se marcarán para eliminación o búsqueda de fuente alternativa en `references.bib`.

### 2.3 Módulo 3: Visualización Científica (`figures/`)
Se generarán 5 activos con las siguientes especificaciones:
1.  `figures/graphical_abstract.png`: 1200x600px. Diseño conceptual Origen -> Smartphone -> Resignificación -> Destino.
2.  `figures/prisma_flowchart.png`: Diagrama de flujo vertical siguiendo PRISMA 2020.
3.  `figures/conceptual_framework.png`: Mapa mental de Conectividad, Contexto y Divergencias.
4.  `figures/comparison_matrix.png`: Gráfico de barras o matriz comparativa (Convencional vs. Migrante).
5.  `figures/social_capital_functions.png`: Diagrama radial o circular de las 4 funciones (Vínculos fuertes, débiles, latentes e info interna).

### 2.4 Módulo 4: Implicaciones de Salud Pública (`paper/sections/discussion.md`)
- **Acción:** Insertar párrafo en 5.2.
- **Contenido:** Propuesta de "infomediarios" digitales y adaptación de contenidos institucionales para romper silos informativos.

## 3. Contratos de Interfaz (Archivos)
- `paper/sections/abstract.md`: Texto en prosa fluida (no bullets).
- `paper/sections/results.md`: Texto con citas Chicago-Author-Date integradas.
- `figures/`: Directorio que contendrá los archivos `.png` o `.pdf` finales.

## 4. Riesgos y Mitigación
- **Riesgo:** Incompatibilidad de los testimonios con el corpus. **Mitigación:** Verificar cada cita en `references.bib` antes de la edición.
- **Riesgo:** Falta de herramientas gráficas en el entorno. **Mitigación:** Usar scripts de Python (Matplotlib) para diagramas técnicos y descripciones textuales para el Graphical Abstract si se requiere intervención manual.

## 5. Próximos Pasos
- Generación de tareas (Tasks).
- Implementación de tests de validación pre-edición.
