# Research & Design Decisions

## Summary
- **Feature**: `resignificacion-migrantes`
- **Discovery Scope**: New Feature (paper greenfield, revisión de literatura)
- **Key Findings**:
  1. El límite de 9.000 palabras de REIS incluye todo (título, resúmenes, palabras clave, tablas, bibliografía, notas y anexos), no solo el cuerpo del texto. Esto impacta significativamente la distribución de palabras por sección.
  2. REIS exige título bilingüe de máximo 10 palabras sin abreviaturas, máximo 3 autores, y declaración explícita de uso de IA en la carta de presentación.
  3. El borrador existente contiene material sustancial pero desestructurado: definiciones de plataformas (Facebook/Meta, WhatsApp, Instagram, TikTok), testimonios de migrantes, fragmentos teóricos de al menos tres libros clave y múltiples fuentes periodísticas que requieren depuración para una revisión sistemática.

## Research Log

### Normas editoriales de REIS
- **Context**: Verificar requisitos formales exactos de la revista de destino para ajustar el diseño del paper.
- **Sources Consulted**: https://reis.cis.es/index.php/reis/about/submissions (consultado 2026-04-10)
- **Findings**:
  - Extensión: 9.000 palabras para artículos, incluyendo todo el contenido del manuscrito.
  - Título: bilingüe (español e inglés), máximo 10 palabras, sin abreviaturas.
  - Resumen: 100-130 palabras en cada idioma, contenido idéntico.
  - Palabras clave: 4-8 términos en español con traducción al inglés.
  - Citas en texto: (Apellido, año: página) para un autor; (Apellido y Apellido, año) para dos; (Apellido et al., año) para más de tres.
  - Bibliografía: formato propio de REIS (similar a APA con variaciones). Libros: Apellido, Nombre (año). *Título*. Lugar: Editorial. Artículos: Apellido, Nombre (año). "Título". *Revista*, volumen(número): páginas. doi: código.
  - Tablas y figuras: al final del documento, una por página, sin líneas verticales. Imágenes en TIF o JPG, 300 ppi, mínimo 10 cm de ancho.
  - Anonimización: se requieren dos versiones del manuscrito (una publicable, una anonimizada).
  - Máximo 3 autores.
  - Uso de IA: declarar en carta de presentación.
  - Tipografía: Times New Roman 12, interlineado sencillo, sin sangría, sin justificación.
  - Notas: únicamente a pie de página.
  - Envío: mediante OJS, no por correo.
- **Implications**: El presupuesto de palabras es más ajustado de lo previsto. Con ~9.000 palabras totales, restando título (~20), resúmenes (~260), palabras clave (~50), y estimando ~1.500 para bibliografía y notas, quedan aproximadamente 7.000-7.200 palabras para el cuerpo del paper. Esto obliga a una distribución muy cuidadosa por sección.

### Estructura del borrador existente
- **Context**: Evaluar el material disponible en `temp_context/1_Resignificación de las comunicaciones - BORRADOR.md` para determinar qué puede reutilizarse.
- **Sources Consulted**: Borrador colaborativo (Manuel, Erwin y colaboradores)
- **Findings**:
  - El borrador contiene material extenso pero no estructurado según IMRaD.
  - Secciones identificables: Introducción (parcial), Hipótesis y objetivos (formulados), Significación de las comunicaciones (extenso material sobre definiciones de plataformas), Usos de redes sociales por migrantes (múltiples fuentes).
  - Fuentes clave identificadas en el borrador: Zhao (Social Media in the lives of young connected migrants), libro sobre uso de redes sociales en migrantes colombianos en Chile, Oxford University (How social media transform migrant networks), NPR (How social media has changed migration to the United States), Dedecek Gertz y Süßer (Migration and education on social media).
  - Testimonios directos de migrantes: Cecilia (23 años, servicios de limpieza) sobre videollamadas; José (35 años, ayudante de cocina) sobre comparación con comunicaciones de su padre hace tres décadas.
  - Estadísticas parciales y desactualizadas: datos de 2017 sobre migración en Chile (1.200.000, 6,1% de la población), datos de 2019 sobre colombianos (~146.000).
  - Notas de los autores marcando secciones incompletas: [meter estadísticas venezolanas], [TODO], referencias marcadas como "buscar estadísticas actualizadas".
- **Implications**: El borrador aporta material argumentativo y fuentes valiosas, pero requiere: (a) reestructuración completa según IMRaD, (b) actualización de estadísticas a 2020-2026, (c) depuración de fuentes periodísticas vs. académicas, (d) integración coherente de los fragmentos teóricos dispersos.

### Marco teórico: corrientes principales
- **Context**: Mapear las corrientes teóricas necesarias para fundamentar el concepto de "resignificación" en contexto migratorio.
- **Sources Consulted**: Borrador, referencias identificadas en el material existente.
- **Findings**:
  - Capital social: Bourdieu (formas de capital), Putnam (bonding vs. bridging). Aplicación: las redes sociales como infraestructura para transferir y generar capital social transnacional.
  - Familia transnacional y "familia imaginada": Bell y Erdal (2015) sobre nuevos códigos temporales y espaciales; Vermot (2015, p.145) sobre adaptación a una "familia imaginada".
  - Intimidad virtual y co-presencia: Katz y González (2016) sobre TIC para mantener intimidad virtual, apoyo emocional y atención transnacional; Francisco (2015) sobre redefinición de relaciones transnacionales.
  - Cultura de la conectividad: van Dijck (2013) sobre el "ecosistema de medios conectivos" y la transformación de conectividad humana en conectividad digital; van Dijck et al. (2018) sobre "sociedad de plataformas".
  - Polisemia de redes sociales: Zhao citando a Hunsinger y Senft (2014), Burgess et al. (2018) sobre definiciones técnicas; Goggin y McLelland (2010) sobre rechazo al enfoque universalista anglófono.
  - Vínculos fuertes, débiles y latentes: Dekker et al. sobre cuatro funciones de redes sociales en migración (vínculos fuertes, débiles, latentes, conocimiento informal); Haythornthwaite (2002) sobre vínculos latentes.
- **Implications**: El marco teórico tiene densidad suficiente, pero debe integrarse de forma articulada, no como catálogo de autores. La propuesta de resignificación debe emerger como síntesis propia de estas corrientes, no como simple yuxtaposición.

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos/Limitaciones | Notas |
|--------|-------------|-----------|---------------------|-------|
| IMRaD estricto | Estructura clásica: Intro, Methods, Results, Discussion | Familiar para revisores, clara separación | Puede forzar la revisión de literatura a encajar en "Results" | Adaptación necesaria para revisiones teóricas |
| IMRaD adaptado para revisión | Intro, Marco teórico, Metodología de revisión, Resultados y discusión integrados, Conclusiones | Permite mayor fluidez argumentativa; común en revisiones de ciencias sociales | Requiere disciplina para no mezclar descripción con interpretación | **Seleccionado**: mejor ajuste para el tipo de paper |
| Estructura temática libre | Secciones organizadas por ejes temáticos sin seguir IMRaD | Máxima flexibilidad argumentativa | Riesgo de percepción de falta de rigor metodológico en revisores | No recomendado para REIS |

## Design Decisions

### Decision: Estructura IMRaD adaptada para revisión de literatura
- **Context**: El paper es una revisión de literatura teórica, no un estudio empírico. La estructura IMRaD clásica no se ajusta directamente.
- **Alternatives Considered**:
  1. IMRaD estricto con "Results" como hallazgos de la revisión
  2. IMRaD adaptado con Marco teórico como sección propia y Resultados+Discusión integrados
  3. Estructura temática libre
- **Selected Approach**: IMRaD adaptado (opción 2). Secciones: Título y metadatos → Resumen bilingüe → Introducción → Marco teórico y conceptual → Metodología de revisión → Resultados y discusión → Conclusiones → Referencias.
- **Rationale**: Las revisiones de literatura en ciencias sociales publicadas en REIS y revistas similares suelen integrar resultados y discusión, permitiendo una argumentación más fluida. El marco teórico como sección separada da espacio para desarrollar el concepto de resignificación antes de presentar la evidencia.
- **Trade-offs**: La integración de resultados y discusión exige más disciplina editorial para no perder la distinción entre lo descriptivo (qué dice la literatura) y lo interpretativo (qué implica para la resignificación).
- **Follow-up**: Definir subsecciones internas claras para Resultados y discusión que separen las tres categorías de análisis.

### Decision: Distribución de presupuesto de palabras
- **Context**: Con ~7.000-7.200 palabras disponibles para el cuerpo (descontando metadatos, resúmenes y bibliografía del total de 9.000), cada sección tiene un límite estricto.
- **Selected Approach**: Distribución ponderada según importancia argumentativa:
  - Introducción: ~1.000 palabras (14%)
  - Marco teórico y conceptual: ~1.800 palabras (25%)
  - Metodología de revisión: ~600 palabras (8%)
  - Resultados y discusión: ~2.800 palabras (39%)
  - Conclusiones: ~800 palabras (11%)
  - Margen de ajuste: ~200 palabras (3%)
- **Rationale**: Resultados y discusión recibe la mayor asignación porque debe cubrir tres categorías de análisis con evidencia. El marco teórico necesita espacio suficiente para articular cuatro corrientes teóricas. La metodología puede ser concisa al ser una revisión sistemática con protocolo estándar.
- **Trade-offs**: El margen es mínimo. Cada sección debe ser disciplinada en extensión.

### Decision: Tres categorías de análisis para organizar resultados
- **Context**: La revisión de ~160 artículos necesita un esquema organizador que permita sintetizar hallazgos de forma coherente.
- **Selected Approach**: Tres categorías derivadas de la hipótesis:
  (a) Conectividad y mantenimiento de vínculos transnacionales
  (b) Contextos de uso de plataformas específicas
  (c) Divergencias entre usos convencionales y usos resignificados por migrantes
- **Rationale**: La categoría (a) establece la base empírica (qué hacen los migrantes), la (b) diferencia por plataforma (dónde lo hacen), y la (c) construye el argumento central de resignificación (cómo difiere del uso convencional). Esta secuencia lleva al lector de lo descriptivo a lo analítico.
- **Trade-offs**: Algunos hallazgos pueden cruzar categorías. Será necesario decidir dónde ubicar cada evidencia para evitar redundancia.

## Risks & Mitigations
- **Presupuesto de palabras ajustado**: El límite de 9.000 palabras incluye todo. Mitigación: distribución rígida por sección con alertas de validación automáticas al superar el 105% del límite asignado.
- **Estadísticas desactualizadas**: El borrador usa datos de 2017-2019. Mitigación: búsqueda específica de fuentes oficiales 2020-2026 (INE Chile, DEM, OIM World Migration Report 2024) durante la fase de implementación.
- **Referencias no verificables**: El borrador contiene enlaces a sitios web periodísticos y corporativos que podrían no ser aceptados como fuentes académicas. Mitigación: clasificar cada referencia como "académica", "institucional" o "periodística" y priorizar fuentes indexadas.
- **Declaración de IA**: REIS requiere declarar uso de IA en carta de presentación. Mitigación: mantener registro de contribuciones de IA al paper desde el inicio.

## References
- [REIS: Normas para autores](https://reis.cis.es/index.php/reis/about/submissions) — Normas editoriales completas de la revista de destino.
- Zhao, Xinyu. *Social Media in the lives of young connected migrants* — Fuente teórica clave sobre conectividad y redes sociales en migrantes.
- Dekker et al. *How social media transform migrant networks and facilitate migration* (Oxford University) — Cuatro funciones de redes sociales en redes migratorias.
- van Dijck, José (2013). *The Culture of Connectivity* — Marco de "ecosistema de medios conectivos".
