---
title: >-
  Categorización de tecnologías de inteligencia artificial según su utilidad
  para la accesibilidad web bajo las pautas WCAG 2.2
author: Boris Bustos
date: today
bibliography: ../references/references.bib
csl: ../apa.csl
lang: es
format:
  gfm:
    variant: +yaml_metadata_block
    toc: true
    number-sections: true
---


- [Categorización de tecnologías de inteligencia artificial según su
  utilidad para la accesibilidad web bajo las pautas WCAG
  2.2](#categorización-de-tecnologías-de-inteligencia-artificial-según-su-utilidad-para-la-accesibilidad-web-bajo-las-pautas-wcag-22)
- [Resumen](#resumen)
  - [Abstract](#abstract)
- [<span class="toc-section-number">1</span>
  Introducción](#introducción)
  - [<span class="toc-section-number">1.1</span> Planteamiento del
    problema](#planteamiento-del-problema)
  - [<span class="toc-section-number">1.2</span> Accesibilidad web y las
    pautas WCAG](#accesibilidad-web-y-las-pautas-wcag)
  - [<span class="toc-section-number">1.3</span> Inteligencia artificial
    y tecnologías
    asistivas](#inteligencia-artificial-y-tecnologías-asistivas)
  - [<span class="toc-section-number">1.4</span> Evaluación y
    herramientas de accesibilidad
    web](#evaluación-y-herramientas-de-accesibilidad-web)
  - [<span class="toc-section-number">1.5</span> Pregunta de
    investigación y objetivos](#pregunta-de-investigación-y-objetivos)
- [<span class="toc-section-number">2</span> Metodología](#metodología)
  - [<span class="toc-section-number">2.1</span> Diseño de
    investigación](#diseño-de-investigación)
  - [<span class="toc-section-number">2.2</span> Muestra y criterios de
    selección](#muestra-y-criterios-de-selección)
  - [<span class="toc-section-number">2.3</span> Fuente de datos y
    estructura del dataset](#fuente-de-datos-y-estructura-del-dataset)
  - [<span class="toc-section-number">2.4</span> Dimensiones e
    indicadores de evaluación](#dimensiones-e-indicadores-de-evaluación)
    - [<span class="toc-section-number">2.4.1</span>
      Usabilidad](#usabilidad)
    - [<span class="toc-section-number">2.4.2</span>
      Robustez](#robustez)
    - [<span class="toc-section-number">2.4.3</span>
      Operabilidad](#operabilidad)
  - [<span class="toc-section-number">2.5</span> Escala de evaluación y
    mapeo
    categórico-numérico](#escala-de-evaluación-y-mapeo-categórico-numérico)
  - [<span class="toc-section-number">2.6</span> Cálculo de puntuaciones
    y método de
    ponderación](#cálculo-de-puntuaciones-y-método-de-ponderación)
  - [<span class="toc-section-number">2.7</span> Categorización por tipo
    de discapacidad](#categorización-por-tipo-de-discapacidad)
  - [<span class="toc-section-number">2.8</span> Procedimiento de
    análisis](#procedimiento-de-análisis)
- [<span class="toc-section-number">3</span> Resultados](#resultados)
  - [<span class="toc-section-number">3.1</span> Distribución de
    tecnologías por tipo de
    discapacidad](#distribución-de-tecnologías-por-tipo-de-discapacidad)
  - [<span class="toc-section-number">3.2</span> Categorización por tipo
    de producto y tecnología de
    IA](#categorización-por-tipo-de-producto-y-tecnología-de-ia)
  - [<span class="toc-section-number">3.3</span> Análisis descriptivo de
    las dimensiones de
    evaluación](#análisis-descriptivo-de-las-dimensiones-de-evaluación)
  - [<span class="toc-section-number">3.4</span> Ranking global y las
    cinco mejores
    tecnologías](#ranking-global-y-las-cinco-mejores-tecnologías)
  - [<span class="toc-section-number">3.5</span> Análisis de las
    características del top
    5](#análisis-de-las-características-del-top-5)
- [<span class="toc-section-number">4</span> Discusión](#discusión)
  - [<span class="toc-section-number">4.1</span> Contraste de hallazgos
    con la literatura
    existente](#contraste-de-hallazgos-con-la-literatura-existente)
  - [<span class="toc-section-number">4.2</span> Vacío de conocimiento
    teórico](#vacío-de-conocimiento-teórico)
  - [<span class="toc-section-number">4.3</span> Vacío de conocimiento
    práctico](#vacío-de-conocimiento-práctico)
  - [<span class="toc-section-number">4.4</span> Limitaciones del
    estudio](#limitaciones-del-estudio)
  - [<span class="toc-section-number">4.5</span> Líneas futuras de
    investigación](#líneas-futuras-de-investigación)
  - [<span class="toc-section-number">4.6</span> Implicaciones para la
    inclusión digital y los Objetivos de Desarrollo
    Sostenible](#implicaciones-para-la-inclusión-digital-y-los-objetivos-de-desarrollo-sostenible)
- [<span class="toc-section-number">5</span>
  Conclusiones](#conclusiones)
- [Referencias](#referencias)

# Categorización de tecnologías de inteligencia artificial según su utilidad para la accesibilidad web bajo las pautas WCAG 2.2

**Autor:** Boris Bustos

**Afiliación:** Universidad de las Américas (UDLA), Quito, Ecuador

**Correo:** boris.bustos@udla.edu.ec

**Palabras clave (ES):** inteligencia artificial, accesibilidad web,
WCAG 2.2, tecnologías asistivas, discapacidad, diseño universal

**Keywords (EN):** artificial intelligence, web accessibility, WCAG 2.2,
assistive technologies, disability, universal design

# Resumen

El presente estudio analiza y categoriza 41 tecnologías de inteligencia
artificial según su utilidad para la accesibilidad web, evaluadas bajo
los criterios de las Pautas de Accesibilidad para el Contenido Web
(WCAG) 2.2 del World Wide Web Consortium. Mediante un enfoque
metodológico documental-descriptivo de carácter mixto, se evaluaron tres
dimensiones: usabilidad, robustez y operabilidad, aplicando un mapeo
categórico-numérico en escala de 1 a 5. Las tecnologías fueron
clasificadas por tipo de discapacidad atendida (visual, motora,
cognitiva y auditiva) y ordenadas mediante un algoritmo de ranking
ponderado. Los resultados revelan una concentración significativa de
tecnologías orientadas a la discapacidad motora, mientras que la
discapacidad auditiva presenta la menor cobertura. La dimensión de
usabilidad obtuvo las puntuaciones más altas (media = 4,25), seguida por
robustez (3,26) y operabilidad (1,70). Las cinco tecnologías mejor
evaluadas fueron DeepSeek, Grid, ChatGPT, Gemini 2.0 y Google Assistant,
destacando por su alta precisión, compatibilidad multiplataforma y
soporte de comandos de voz. El análisis evidencia un vacío de
conocimiento tanto teórico como práctico en la intersección entre
inteligencia artificial y accesibilidad web: no existen marcos
conceptuales consolidados que integren capacidades de IA con los
principios WCAG, y persisten brechas en la implementación real de estas
tecnologías para usuarios con discapacidad. Estos hallazgos contribuyen
al debate sobre la inclusión digital y se alinean con los Objetivos de
Desarrollo Sostenible 4 y 10.

## Abstract

This study analyzes and categorizes 41 artificial intelligence
technologies based on their utility for web accessibility, evaluated
under the Web Content Accessibility Guidelines (WCAG) 2.2 criteria from
the World Wide Web Consortium. Using a mixed-method
documentary-descriptive approach, three dimensions were assessed:
usability, robustness, and operability, applying a
categorical-to-numerical mapping on a 1-to-5 scale. Technologies were
classified by type of disability addressed (visual, motor, cognitive,
and auditory) and ranked through a weighted scoring algorithm. Results
reveal a significant concentration of technologies targeting motor
disabilities, while auditory disability has the lowest coverage. The
usability dimension achieved the highest scores (mean = 4.25), followed
by robustness (3.26) and operability (1.70). The five top-rated
technologies were DeepSeek, Grid, ChatGPT, Gemini 2.0, and Google
Assistant, standing out for their high precision, cross-platform
compatibility, and voice command support. The analysis reveals a
knowledge gap at both theoretical and practical levels at the
intersection of artificial intelligence and web accessibility: no
consolidated conceptual frameworks exist that integrate AI capabilities
with WCAG principles, and gaps persist in the real-world implementation
of these technologies for users with disabilities. These findings
contribute to the digital inclusion debate and align with Sustainable
Development Goals 4 and 10.

# Introducción

## Planteamiento del problema

La accesibilidad web constituye un principio fundamental para garantizar
que todas las personas, independientemente de sus capacidades, puedan
acceder, navegar e interactuar con los contenidos digitales de manera
efectiva. A pesar de los avances normativos impulsados por el World Wide
Web Consortium (W3C) a través de las Pautas de Accesibilidad para el
Contenido Web (WCAG), la brecha entre el cumplimiento teórico de
estándares y la experiencia real de los usuarios con discapacidad sigue
siendo considerable (Martins & Duarte, 2024; Vollenwyder et al., 2023).
En paralelo, la inteligencia artificial (IA) ha experimentado un
crecimiento exponencial en la última década, ofreciendo capacidades de
procesamiento de lenguaje natural, visión por computadora,
reconocimiento de voz y análisis de señales cerebrales que podrían
transformar radicalmente la accesibilidad web (Campoverde-Molina &
Luján-Mora, 2025; Chemnad & Othman, 2024). Sin embargo, la intersección
entre estas dos disciplinas permanece insuficientemente explorada desde
una perspectiva sistemática y evaluativa.

El presente estudio surge de la observación de que, si bien existen
numerosas tecnologías de IA con potencial para mejorar la accesibilidad
web, no se dispone de un marco evaluativo que permita categorizar y
comparar estas tecnologías según su utilidad real para distintos tipos
de discapacidad bajo los criterios WCAG 2.2. Esta carencia representa un
vacío de conocimiento que limita tanto la toma de decisiones informadas
por parte de desarrolladores y diseñadores como la formulación de
políticas públicas de inclusión digital.

## Accesibilidad web y las pautas WCAG

La accesibilidad web se define como la práctica de diseñar y desarrollar
sitios, herramientas y tecnologías web de manera que las personas con
discapacidad puedan utilizarlos de forma autónoma y efectiva (Abascal
et al., 2016; Lazar et al., 2015; Petrie & Kheir, 2007). Este concepto
trasciende la mera conformidad técnica y abarca dimensiones de
usabilidad, equidad y participación social en el entorno digital.

Las Pautas de Accesibilidad para el Contenido Web (WCAG) del W3C
constituyen el estándar internacional de referencia para la
accesibilidad web. Su evolución refleja la creciente complejidad de las
tecnologías web y la diversificación de las necesidades de los usuarios
con discapacidad. La versión 1.0, publicada en 1999, estableció los
fundamentos iniciales centrados en el contenido HTML estático. La
versión 2.0 (2008) amplió el alcance a tecnologías dinámicas mediante
principios tecnológicamente neutrales. WCAG 2.1 (2018) incorporó
criterios específicos para dispositivos móviles, personas con baja
visión y discapacidad cognitiva (World Wide Web Consortium, 2018). La
versión más reciente, WCAG 2.2, publicada en octubre de 2023, introdujo
nueve criterios de éxito adicionales orientados a mejorar la experiencia
de usuarios con discapacidad cognitiva y motora, incluyendo criterios
como *focus not obscured*, *dragging movements* y *accessible
authentication* (World Wide Web Consortium, 2023).

Las pautas WCAG se organizan en torno a cuatro principios fundamentales
que definen las condiciones necesarias para la accesibilidad web:

1.  **Perceptible**: la información y los componentes de la interfaz de
    usuario deben ser presentados de forma que los usuarios puedan
    percibirlos, lo que incluye alternativas textuales para contenido no
    textual, subtítulos para contenido multimedia y adaptabilidad del
    contenido. Las tecnologías de IA contribuyen a este principio
    mediante la generación automática de descripciones de imágenes, el
    subtitulado automático y la síntesis de voz (Das et al., 2024;
    Leotta et al., 2022).

2.  **Operable**: los componentes de la interfaz y la navegación deben
    ser operables por todos los usuarios, lo que implica accesibilidad
    por teclado, tiempo suficiente para interactuar con el contenido y
    navegación predecible. Tecnologías como el seguimiento ocular, las
    interfaces cerebro-computadora y los comandos de voz basados en IA
    amplían las modalidades de interacción disponibles para personas con
    discapacidad motora (Belwafi & Ghaffari, 2024;
    <span class="nocase">Chhimpa et al.</span>, 2024; Fischer-Janzen
    et al., 2024).

3.  **Comprensible**: la información y la operación de la interfaz deben
    ser comprensibles, lo que incluye legibilidad, predictibilidad y
    asistencia en la entrada de datos. La IA aporta a este principio a
    través de herramientas de simplificación de texto, asistentes
    conversacionales y personalización adaptativa del contenido según
    las necesidades cognitivas del usuario (Gartland et al., 2022;
    Moreno et al., 2024; World Wide Web Consortium, 2021).

4.  **Robusto**: el contenido debe ser suficientemente robusto para ser
    interpretado de forma fiable por una amplia variedad de agentes de
    usuario, incluidas las tecnologías asistivas. La compatibilidad
    multiplataforma y multi-navegador de las herramientas basadas en IA
    es un factor determinante en este principio (Ara et al., 2023; Ara
    et al., 2025).

## Inteligencia artificial y tecnologías asistivas

La inteligencia artificial, entendida como la disciplina que desarrolla
sistemas capaces de realizar tareas que tradicionalmente requieren
inteligencia humana, ha abierto nuevas posibilidades para la
accesibilidad web a través de múltiples paradigmas tecnológicos. El
procesamiento de lenguaje natural permite la interacción por voz y la
simplificación de textos complejos; la visión por computadora posibilita
la descripción automática de imágenes y la detección de barreras
visuales; el reconocimiento de voz facilita la navegación manos libres;
y las interfaces cerebro-computadora ofrecen alternativas de interacción
para usuarios con discapacidad motora severa (Giansanti & Pirrera, 2025;
Schaur & Matausch-Mahr, 2025).

Estudios recientes han documentado el potencial de la IA generativa para
la accesibilidad web. Acosta-Vargas, Salvador-Acosta, et al. (2024)
analizaron cómo las herramientas de IA generativa pueden contribuir a un
futuro más inclusivo y sostenible. Campoverde-Molina & Luján-Mora (2025)
realizaron un mapeo sistemático que identificó las principales líneas de
investigación en la intersección IA-accesibilidad web, revelando un
crecimiento exponencial de publicaciones en los últimos cinco años pero
una fragmentación temática que dificulta la consolidación de marcos
teóricos integradores. López-Gil & Pereira (2025) demostraron que los
modelos de lenguaje de gran tamaño (LLM) pueden transformar criterios de
éxito WCAG manuales en evaluaciones automáticas, alcanzando niveles de
precisión prometedores.

En el ámbito de las tecnologías asistivas específicas, la literatura
reciente ha abordado múltiples modalidades. Kuhn et al. (2024) evaluaron
la precisión de soluciones de reconocimiento automático de voz, un
componente crítico para la navegación por voz. Esquivel et al. (2024)
revisaron la evidencia sobre el uso de asistentes de voz por parte de
personas con discapacidad para la vida independiente. Fuglerud et al.
(2024) exploraron el uso de IA para mejorar las pruebas de accesibilidad
de soluciones web. Por su parte, Mowar (2024) examinó la integración de
accesibilidad en el desarrollo web asistido por IA, y Acosta-Vargas,
Acosta-Vargas, et al. (2024) estudiaron el uso de herramientas de IA
generativa para abordar desafíos de accesibilidad web en contextos
educativos.

Sin embargo, estas contribuciones abordan tecnologías de forma
individual o parcial, sin ofrecer una evaluación comparativa y
sistemática que permita identificar cuáles tecnologías de IA replican de
manera más efectiva los criterios de accesibilidad web como buenas
prácticas.

## Evaluación y herramientas de accesibilidad web

La evaluación de la accesibilidad web ha sido abordada desde múltiples
perspectivas metodológicas. Las herramientas automáticas de evaluación
han sido objeto de análisis crítico por parte de diversos
investigadores. Abu Doush et al. (2023) evaluaron hasta qué punto las
herramientas automáticas pueden cubrir los criterios WCAG, concluyendo
que existen limitaciones significativas en la detección de barreras que
requieren juicio humano. Alsaeedi (2020) propuso marcos comparativos
para evaluar herramientas de accesibilidad web, destacando la
heterogeneidad en los resultados entre distintas herramientas. Brajnik
et al. (2011) demostraron que el nivel de experiencia del evaluador
influye significativamente en los resultados de evaluación, un hallazgo
relevante para la estandarización de métodos evaluativos.

Más recientemente, Salehnamadi et al. (2025) desarrollaron métodos de
detección automática de problemas de accesibilidad utilizando IA
generativa, y Ara & Sik-Lányi (2023) aplicaron técnicas de aprendizaje
automático para la evaluación de accesibilidad web, demostrando que los
modelos de clasificación pueden complementar eficazmente las
herramientas de evaluación convencionales. Othman et al. (2023)
investigaron el uso de modelos de lenguaje como ChatGPT para la
remediación automática de problemas de accesibilidad web, abriendo
nuevas perspectivas sobre el rol de la IA no solo en la evaluación sino
también en la corrección de barreras de accesibilidad.

## Pregunta de investigación y objetivos

A partir de la revisión del estado del arte, se identifica que la
literatura existente carece de estudios que categoricen y comparen de
manera integral las tecnologías de IA según su utilidad para la
accesibilidad web, cruzando dimensiones de evaluación con tipos de
discapacidad bajo el marco normativo WCAG 2.2. Este vacío limita la
comprensión del estado actual de la oferta tecnológica en IA accesible y
dificulta la identificación de buenas prácticas transferibles.

El presente estudio busca responder la siguiente pregunta de
investigación: **¿Cuáles tecnologías de inteligencia artificial replican
de manera más efectiva los criterios de accesibilidad web establecidos
por las pautas WCAG 2.2, y qué vacíos de conocimiento teórico y práctico
persisten en esta intersección?**

Para abordar esta pregunta, se definen los siguientes objetivos:

- **Objetivo general**: categorizar y evaluar 41 tecnologías de
  inteligencia artificial según su utilidad para la accesibilidad web
  bajo las pautas WCAG 2.2, identificando las mejores prácticas y los
  vacíos de conocimiento en la intersección IA-accesibilidad web.

- **Objetivos específicos**:

  1.  Clasificar las 41 tecnologías por tipo de discapacidad atendida
      (visual, motora, cognitiva y auditiva) y analizar la distribución
      de cobertura.
  2.  Evaluar las tecnologías en tres dimensiones (usabilidad, robustez
      y operabilidad) e identificar las cinco mejor puntuadas como
      buenas prácticas.
  3.  Debatir la existencia de un vacío de conocimiento teórico y
      práctico en la integración de IA con los principios WCAG.

El alcance del estudio se circunscribe a un análisis
documental-descriptivo de un conjunto de datos de 41 tecnologías de IA
con aplicaciones en accesibilidad web, evaluadas según indicadores de
usabilidad, robustez y operabilidad. No se incluyen pruebas empíricas
con usuarios finales ni desarrollo de software.

# Metodología

## Diseño de investigación

El presente estudio adopta un diseño documental-descriptivo con enfoque
mixto (cualitativo-cuantitativo), orientado a la categorización y
evaluación de tecnologías de inteligencia artificial según su utilidad
para la accesibilidad web bajo las pautas WCAG 2.2. Este enfoque permite
combinar la caracterización cualitativa de las tecnologías con el
análisis cuantitativo de sus capacidades, siguiendo las recomendaciones
metodológicas de la literatura reciente en evaluación de accesibilidad
web (Ara et al., 2023; Chemnad & Othman, 2024).

El diseño documental se justifica por la naturaleza del objeto de
estudio: las tecnologías de IA son productos comerciales y de
investigación cuyas especificaciones técnicas, compatibilidad y
funcionalidades se encuentran documentadas en fuentes públicas
verificables. El componente descriptivo permite sistematizar la
información recopilada en dimensiones comparables, mientras que el
enfoque cuantitativo posibilita la aplicación de un modelo de evaluación
ponderado para la identificación de las tecnologías más destacadas.

## Muestra y criterios de selección

La muestra del estudio comprende 41 tecnologías de inteligencia
artificial con aplicaciones directas o potenciales en accesibilidad web.
La selección se realizó mediante un muestreo intencional basado en los
siguientes criterios de inclusión:

1.  **Relevancia para la accesibilidad web**: la tecnología debe ofrecer
    funcionalidades que contribuyan al cumplimiento de al menos uno de
    los cuatro principios WCAG 2.2 (Perceptible, Operable, Comprensible,
    Robusto).
2.  **Base en inteligencia artificial**: la tecnología debe incorporar
    al menos una técnica de IA, como procesamiento de lenguaje natural,
    visión por computadora, reconocimiento de voz, análisis de EEG o
    *motion tracking*.
3.  **Disponibilidad pública**: la tecnología debe contar con
    documentación técnica accesible, ya sea como producto comercial,
    herramienta de código abierto o prototipo de investigación con
    publicaciones asociadas.
4.  **Vigencia**: la tecnología debe estar activa o haber tenido
    actualizaciones documentadas en los últimos cinco años (2021-2026).

Los criterios de exclusión descartaron tecnologías sin documentación
verificable, proyectos abandonados sin continuidad demostrable y
herramientas exclusivamente orientadas a la evaluación de conformidad
sin componente de IA (como validadores HTML puros).

## Fuente de datos y estructura del dataset

Los datos fueron recopilados en un dataset estructurado que registra las
características técnicas y funcionales de cada tecnología. La base de
datos fue construida a partir de documentación oficial de los productos,
publicaciones académicas asociadas, especificaciones técnicas publicadas
por los desarrolladores y reportes de evaluación independientes.

El dataset contiene las siguientes variables por cada tecnología:

- **Identificación**: nombre, descripción, URL de referencia
- **Caracterización comercial**: modalidad de pago (gratuita, de pago,
  freemium), disponibilidad de API para desarrolladores
- **Clasificación tecnológica**: tipo de producto (asistentes
  conversacionales, lectores de pantalla avanzados, interfaces
  cerebro-computadora, seguimiento ocular, control de cursor
  alternativo, navegación por voz, sistemas de subtitulado automático,
  herramientas de accesibilidad, entre otros), tipo de tecnología de IA
  empleada y tipo de discapacidad atendida (visual, motora, cognitiva,
  auditiva)
- **Variables de evaluación**: ocho indicadores agrupados en tres
  dimensiones, descritos en la siguiente sección

## Dimensiones e indicadores de evaluación

La evaluación de las tecnologías se estructura en tres dimensiones, cada
una compuesta por indicadores específicos que reflejan aspectos
diferenciados del desempeño de la tecnología en el contexto de la
accesibilidad web. La selección de estas dimensiones se fundamenta en
los principios WCAG 2.2 y en la norma ISO 25010 de calidad de producto
de software.

### Usabilidad

La dimensión de usabilidad evalúa la eficacia, eficiencia y satisfacción
con que la tecnología cumple su función asistiva. Se operacionaliza
mediante tres indicadores:

- **Precisión**: grado de exactitud con que la tecnología ejecuta su
  función principal (por ejemplo, la precisión del reconocimiento de voz
  o la fidelidad de la descripción automática de imágenes). Se registra
  en escala categórica: Baja, Media o Alta.
- **Sensibilidad**: capacidad de la tecnología para detectar y responder
  adecuadamente a las necesidades del usuario, incluyendo la adaptación
  a diferentes patrones de entrada. Se registra en escala categórica:
  Baja, Media o Alta.
- **Tiempo de respuesta**: latencia percibida entre la acción del
  usuario y la respuesta del sistema. Se registra como: Lento, Moderado
  o Rápido.

### Robustez

La dimensión de robustez evalúa la solidez técnica de la tecnología y su
capacidad para funcionar de forma fiable en diversos entornos, en
consonancia con el principio Robusto de las WCAG (World Wide Web
Consortium, 2023). Se operacionaliza mediante tres indicadores de
compatibilidad:

- **Compatibilidad multidispositivo**: funcionamiento en computadoras de
  escritorio, portátiles, tabletas y dispositivos móviles.
- **Compatibilidad multi-navegador**: funcionamiento en los principales
  navegadores web (Chrome, Firefox, Safari, Edge).
- **Compatibilidad multi-sistema operativo**: funcionamiento en Windows,
  macOS, Linux, iOS y Android.

Cada indicador de robustez se registra en escala numérica directa de 1 a
5, donde 1 indica compatibilidad mínima (un solo entorno) y 5 indica
compatibilidad máxima (todos los entornos evaluados).

### Operabilidad

La dimensión de operabilidad evalúa la capacidad de la tecnología para
ser controlada mediante modalidades de interacción alternativas,
vinculada directamente con el principio Operable de las WCAG y con la
definición de operabilidad de la norma ISO 25010. Se operacionaliza
mediante dos indicadores:

- **Navegación por teclado**: compatibilidad de la tecnología con la
  navegación exclusiva por teclado. Se registra como: No compatible,
  Parcial o Total.
- **Comandos de voz**: compatibilidad de la tecnología con el control
  mediante comandos de voz. Se registra como: No, Parcial o Sí.

## Escala de evaluación y mapeo categórico-numérico

Para posibilitar el análisis cuantitativo comparativo, las variables
categóricas fueron transformadas a una escala numérica mediante una
tabla de conversión estandarizada. Este mapeo permite calcular
puntuaciones agregadas por dimensión y puntuaciones globales ponderadas.
La <a href="#tbl-mapeo" class="quarto-xref">Tabla 1</a> presenta la
correspondencia entre valores categóricos y numéricos.

<div id="tbl-mapeo">

Tabla 1: Tabla de conversión categórico-numérica para los indicadores de
evaluación

| Variable                 | Valor categórico | Valor numérico |
|--------------------------|------------------|:--------------:|
| Precisión / Sensibilidad | Baja             |       1        |
| Precisión / Sensibilidad | Media            |       3        |
| Precisión / Sensibilidad | Alta             |       5        |
| Tiempo de respuesta      | Lento            |       1        |
| Tiempo de respuesta      | Moderado         |       3        |
| Tiempo de respuesta      | Rápido           |       5        |
| Navegación por teclado   | No compatible    |       0        |
| Navegación por teclado   | Parcial          |       3        |
| Navegación por teclado   | Total            |       5        |
| Comandos de voz          | No               |       0        |
| Comandos de voz          | Parcial          |       3        |
| Comandos de voz          | Sí               |       5        |

</div>

La escala adopta valores de 0 a 5 en lugar de una escala Likert
convencional de 1 a 5, dado que los indicadores de operabilidad admiten
la ausencia total de la funcionalidad (valor 0). Esta decisión
metodológica refleja que la incompatibilidad con navegación por teclado
o comandos de voz representa una barrera de accesibilidad
cualitativamente distinta a un desempeño bajo.

## Cálculo de puntuaciones y método de ponderación

La puntuación por dimensión se calcula como la media aritmética de los
indicadores numéricos que la componen:

- **Puntuación de usabilidad** = (precisión + sensibilidad + tiempo de
  respuesta) / 3
- **Puntuación de robustez** = (multidispositivo + multi-navegador +
  multi-OS) / 3
- **Puntuación de operabilidad** = (navegación por teclado + comandos de
  voz) / 2

La puntuación global ponderada de cada tecnología se obtiene mediante la
siguiente fórmula:

$$P_{global} = 0{,}40 \times P_{usabilidad} + 0{,}30 \times P_{robustez} + 0{,}30 \times P_{operabilidad}$$

Los pesos asignados reflejan la relevancia relativa de cada dimensión
para la accesibilidad web efectiva. La usabilidad recibe el mayor peso
(40%) porque constituye el factor más directamente vinculado con la
experiencia del usuario final con discapacidad: una tecnología que no es
precisa, sensible ni ágil en su respuesta difícilmente cumple su
propósito asistivo, independientemente de su compatibilidad técnica
(Vollenwyder et al., 2023). La robustez y la operabilidad reciben pesos
iguales (30% cada una) en reconocimiento de que tanto la compatibilidad
multiplataforma como las modalidades alternativas de interacción son
igualmente necesarias para garantizar el acceso universal (World Wide
Web Consortium, 2023).

En caso de empate en la puntuación global, se aplican los siguientes
criterios de desempate en orden de prioridad: (1) mayor cobertura de
tipos de discapacidad atendidos, (2) disponibilidad gratuita o
*freemium* y (3) disponibilidad de API para desarrolladores.

## Categorización por tipo de discapacidad

Cada tecnología fue clasificada según el tipo de discapacidad que
atiende de forma primaria, pudiendo atender simultáneamente múltiples
tipos de discapacidad. Las categorías empleadas son:

- **Visual**: tecnologías que asisten a personas con ceguera, baja
  visión o daltonismo (lectores de pantalla, generadores de
  descripciones de imágenes, herramientas de ampliación).
- **Motora**: tecnologías que asisten a personas con limitaciones de
  movilidad en miembros superiores (interfaces cerebro-computadora,
  seguimiento ocular, control de cursor alternativo, navegación por
  voz).
- **Cognitiva**: tecnologías que asisten a personas con discapacidad
  intelectual, trastornos del aprendizaje o dificultades de comprensión
  (simplificadores de texto, asistentes conversacionales, interfaces
  adaptativas) (World Wide Web Consortium, 2021).
- **Auditiva**: tecnologías que asisten a personas con sordera o
  hipoacusia (sistemas de subtitulado automático, transcripción en
  tiempo real).

La clasificación se realizó a partir de la función principal declarada
de cada tecnología y de las discapacidades objetivo identificadas en la
documentación del producto. Cuando una tecnología atiende múltiples
discapacidades, se registraron todas las categorías aplicables,
permitiendo análisis de cobertura cruzada.

## Procedimiento de análisis

El procedimiento de análisis se desarrolló en cuatro fases secuenciales:

1.  **Recopilación y limpieza de datos**: lectura del dataset original,
    verificación de completitud de las 41 tecnologías y limpieza de
    inconsistencias en el formato de registro.
2.  **Transformación cuantitativa**: aplicación de la tabla de mapeo
    categórico-numérico y cálculo de las puntuaciones por dimensión para
    cada tecnología.
3.  **Análisis descriptivo y comparativo**: cálculo de estadísticas
    descriptivas (media, mediana y desviación estándar) por dimensión,
    generación de la matriz cruzada tecnología × tipo de discapacidad y
    análisis de distribución de cobertura.
4.  **Ranking y selección**: cálculo de la puntuación global ponderada,
    ordenamiento descendente, aplicación de criterios de desempate e
    identificación de las cinco tecnologías mejor puntuadas.

Los scripts de procesamiento de datos y generación de visualizaciones
fueron implementados en Python 3.10+ utilizando las bibliotecas pandas
para manipulación de datos, numpy para cálculos estadísticos y
matplotlib con seaborn para la generación de figuras académicas a 300
DPI.

# Resultados

## Distribución de tecnologías por tipo de discapacidad

El análisis de las 41 tecnologías de IA evaluadas revela una
distribución desigual en función del tipo de discapacidad atendida. Del
total de la muestra, 28 tecnologías (68,3%) atienden la discapacidad
motora, posicionándola como la categoría con mayor cobertura. Le sigue
la discapacidad cognitiva con 16 tecnologías (39,0%), la discapacidad
visual con 15 (36,6%) y, con una representación considerablemente menor,
la discapacidad auditiva con solo 4 tecnologías (9,8%). La
<a href="#fig-distribucion" class="quarto-xref">Figura 1</a> ilustra
esta distribución.

<div id="fig-distribucion">

![](../figures/fig-distribucion-discapacidad.png)

Figura 1: Distribución de tecnologías de IA por tipo de discapacidad
atendida. Las barras representan el número de tecnologías que incluyen
cada categoría de discapacidad como objetivo primario o secundario. Una
misma tecnología puede atender múltiples tipos de discapacidad.

</div>

Cabe destacar que 17 de las 41 tecnologías (41,5%) atienden más de un
tipo de discapacidad simultáneamente, lo que indica un grado moderado de
versatilidad en la oferta tecnológica. Sin embargo, la
sobrerrepresentación de la discapacidad motora y la subrepresentación de
la discapacidad auditiva constituyen hallazgos relevantes que serán
discutidos en la sección correspondiente.

La predominancia de tecnologías orientadas a la discapacidad motora se
explica por la diversidad de modalidades de interacción alternativas que
la IA ha posibilitado: desde interfaces cerebro-computadora y
seguimiento ocular hasta control de cursor por movimiento de cabeza y
navegación por voz. En contraste, las tecnologías para discapacidad
auditiva se concentran exclusivamente en sistemas de subtitulado
automático (Otter.ai, AVA y Web Captioner) y una herramienta de
reconocimiento de voz adaptado (Voiceitt).

## Categorización por tipo de producto y tecnología de IA

La <a href="#tbl-matriz" class="quarto-xref">Tabla 2</a> presenta la
matriz cruzada de las 41 tecnologías clasificadas por tipo de
discapacidad atendida, permitiendo visualizar la cobertura y las brechas
existentes.

<div id="tbl-matriz">

Tabla 2: Matriz de tecnologías de IA por tipo de discapacidad atendida.
✓ indica que la tecnología atiende esa categoría de discapacidad.

| Tecnología                                  | Visual | Motora | Cognitiva | Auditiva |
|---------------------------------------------|:------:|:------:|:---------:|:--------:|
| ChatGPT                                     |   ✓    |   ✓    |     ✓     |          |
| Microsoft Copilot (anteriormente Bing Chat) |   ✓    |        |     ✓     |          |
| Gemini 2.0                                  |   ✓    |        |     ✓     |          |
| Alexa                                       |   ✓    |   ✓    |     ✓     |          |
| Google Assistant                            |   ✓    |   ✓    |     ✓     |          |
| Siri                                        |   ✓    |   ✓    |     ✓     |          |
| Neuralink                                   |        |   ✓    |           |          |
| BrainGate                                   |        |   ✓    |           |          |
| NextMind                                    |        |   ✓    |     ✓     |          |
| CTRL-labs (Meta)                            |        |   ✓    |           |          |
| OpenBCI (con la plataforma Galea)           |        |   ✓    |     ✓     |          |
| Emotiv                                      |        |   ✓    |     ✓     |          |
| Neurable                                    |        |   ✓    |     ✓     |          |
| Tobii Dynavox                               |        |   ✓    |           |          |
| EyeSpeak                                    |   ✓    |   ✓    |           |          |
| Enable Viacam (eViacam)                     |        |   ✓    |           |          |
| Sesame Phone                                |        |   ✓    |           |          |
| GazeSpeak (Microsoft)                       |        |   ✓    |           |          |
| Irisbond                                    |        |   ✓    |           |          |
| Accessibility Insights for Web              |   ✓    |        |     ✓     |          |
| UserWay Accessibility Widget                |   ✓    |        |     ✓     |          |
| Voice Control for Browser                   |        |   ✓    |           |          |
| WAVE                                        |   ✓    |        |           |          |
| Voiceitt                                    |        |   ✓    |     ✓     |    ✓     |
| LipSurf                                     |        |   ✓    |           |          |
| Tecla                                       |        |   ✓    |     ✓     |          |
| EyeControl                                  |        |   ✓    |           |          |
| Grid                                        |        |   ✓    |     ✓     |          |
| HeadMouse Nano                              |        |   ✓    |           |          |
| Quha Zono                                   |        |   ✓    |           |          |
| GlassOuse                                   |        |   ✓    |           |          |
| Jouse3                                      |        |   ✓    |           |          |
| NVDA                                        |   ✓    |        |           |          |
| JAWS                                        |   ✓    |        |           |          |
| Dragon NaturallySpeaking                    |        |   ✓    |           |          |
| Project Mariner                             |   ✓    |        |           |          |
| BrailleSurf                                 |   ✓    |        |           |          |
| DeepSeek                                    |   ✓    |        |     ✓     |          |
| Otter.ai                                    |        |        |           |    ✓     |
| AVA                                         |        |        |           |    ✓     |
| Web Captioner                               |        |        |           |    ✓     |

</div>

Las tecnologías evaluadas se distribuyen en diversos tipos de producto,
con una presencia destacada de los dispositivos asistivos inteligentes
(presentes en 24 tecnologías), el control de cursor alternativo (15
tecnologías), el software de comunicación asistiva (14 tecnologías) y
las herramientas de simplificación de texto (9 tecnologías). En menor
proporción se encuentran los asistentes por voz y las herramientas de
navegación por voz (7 cada uno), las interfaces cerebro-computadora (7),
los asistentes conversacionales (5), los sistemas de seguimiento ocular
(5), los lectores de pantalla avanzados (4), los sistemas de subtitulado
automático (3) y los generadores automáticos de descripciones de
imágenes (3).

En cuanto al tipo de tecnología de IA empleada, el procesamiento de
lenguaje natural es la técnica más extendida, presente en la mayoría de
las tecnologías evaluadas. Le siguen la síntesis de voz, el
reconocimiento de voz, el *motion tracking*, el análisis de señales EEG
(*eye-tracking*) y la visión por computadora. Esta distribución refleja
la madurez del procesamiento de lenguaje natural como paradigma
dominante en las aplicaciones de IA para accesibilidad web.

## Análisis descriptivo de las dimensiones de evaluación

Las estadísticas descriptivas de las tres dimensiones evaluadas revelan
diferencias significativas en el desempeño del conjunto de tecnologías.
La <a href="#fig-comparativa" class="quarto-xref">Figura 2</a> presenta
una comparación visual de las puntuaciones medias por dimensión con sus
respectivas barras de error.

<div id="fig-comparativa">

![](../figures/fig-comparativa-dimensiones.png)

Figura 2: Comparación de las puntuaciones medias por dimensión evaluada.
Las barras representan la media del conjunto de 41 tecnologías y las
líneas de error indican la desviación estándar. Escala de 0 a 5.

</div>

La dimensión de **usabilidad** obtuvo la puntuación media más alta (*M*
= 4,25; *Mdn* = 4,33; *SD* = 0,73), indicando que la mayoría de las
tecnologías evaluadas alcanzan niveles satisfactorios de precisión,
sensibilidad y tiempo de respuesta. La baja dispersión (*SD* = 0,73)
sugiere una homogeneidad relativa en el desempeño de usabilidad del
conjunto.

La dimensión de **robustez** presentó una puntuación media moderada (*M*
= 3,26; *Mdn* = 3,00; *SD* = 1,22). La dispersión más elevada respecto a
la usabilidad indica una mayor heterogeneidad: mientras algunas
tecnologías como ChatGPT, Gemini 2.0 y Google Assistant alcanzan
compatibilidad máxima multiplataforma (5,00), otras como Siri, Irisbond
y EyeSpeak presentan compatibilidad limitada a un solo entorno (1,00).

La dimensión de **operabilidad** obtuvo la puntuación media más baja
(*M* = 1,70; *Mdn* = 1,50; *SD* = 1,54), con la mayor dispersión del
conjunto. Este resultado constituye uno de los hallazgos más relevantes
del estudio: la mayoría de las tecnologías de IA evaluadas presentan
limitaciones significativas en su compatibilidad con navegación por
teclado y comandos de voz. Doce tecnologías obtuvieron una puntuación de
operabilidad de 0,00, lo que significa ausencia total de soporte para
modalidades alternativas de interacción. Este dato resulta paradójico,
considerando que muchas de estas tecnologías están diseñadas para
asistir a personas con discapacidad motora pero no ofrecen ellas mismas
mecanismos de operación accesibles.

## Ranking global y las cinco mejores tecnologías

La aplicación del modelo de ponderación descrito en la sección de
Metodología permitió calcular la puntuación global de cada tecnología y
establecer un ranking ordenado. La
<a href="#fig-ranking" class="quarto-xref">Figura 3</a> presenta las
cinco tecnologías con puntuación global más alta.

<div id="fig-ranking">

![](../figures/fig-ranking-top5.png)

Figura 3: Ranking de las cinco tecnologías de IA mejor puntuadas según
el modelo de evaluación ponderado. Las barras muestran la puntuación
global y el desglose por dimensión (usabilidad, robustez y
operabilidad). Pesos: usabilidad 40%, robustez 30%, operabilidad 30%.

</div>

Las cinco tecnologías mejor puntuadas son:

1.  **DeepSeek** (puntuación global: 4,60). Ocupa la primera posición
    gracias a puntuaciones máximas en usabilidad (5,00) y operabilidad
    (5,00), combinadas con una robustez aceptable (3,67). Se clasifica
    como asistente conversacional con capacidades de comunicación
    asistiva y generación automática de descripciones de imágenes,
    empleando procesamiento de lenguaje natural, reconocimiento de voz,
    síntesis de voz y visión por computadora. Atiende discapacidades
    cognitiva y visual. Destaca por su compatibilidad total con
    navegación por teclado y comandos de voz, lo que la distingue de la
    mayoría de las tecnologías evaluadas.

2.  **Grid** (puntuación global: 4,50). Software de comunicación
    asistiva con funcionalidades de teclado virtual predictivo y lectura
    de pantalla. Emplea procesamiento de lenguaje natural, síntesis de
    voz y reconocimiento de voz para atender discapacidades cognitiva y
    motora. Obtiene puntuaciones de usabilidad (5,00) y robustez (4,33)
    superiores a la media, y es una de las pocas tecnologías con
    compatibilidad total de navegación por teclado y parcial de comandos
    de voz (operabilidad: 4,00).

3.  **ChatGPT** (puntuación global: 4,43). Asistente conversacional con
    capacidades de simplificación de texto y asistencia por voz. Alcanza
    la puntuación máxima en robustez (5,00), con compatibilidad total
    multiplataforma y multi-navegador. Atiende tres tipos de
    discapacidad (visual, cognitiva y motora), lo que le otorga la mayor
    cobertura de las tecnologías del top 5. Su operabilidad (4,00)
    refleja compatibilidad parcial con navegación por teclado y total
    con comandos de voz.

4.  **Gemini 2.0** (puntuación global: 4,43). Comparte la tercera
    posición con ChatGPT. Asistente conversacional con generación
    automática de descripciones de imágenes, asistencia por voz y
    simplificación de texto, basado en procesamiento de lenguaje
    natural, reconocimiento de voz, síntesis de voz y visión por
    computadora. Atiende discapacidades visual y cognitiva. Iguala a
    ChatGPT en robustez (5,00) y operabilidad (4,00), con idéntica
    puntuación de usabilidad (4,33).

5.  **Google Assistant** (puntuación global: 4,40). Asistente por voz
    con funcionalidades de navegación por voz y comunicación asistiva.
    Es la única tecnología del top 5 que alcanza puntuación máxima
    simultánea en usabilidad (5,00) y robustez (5,00), lo que refleja su
    alta precisión, rapidez de respuesta y compatibilidad total
    multiplataforma. Atiende tres tipos de discapacidad (motora, visual
    y cognitiva). Su posición en el ranking se ve limitada por una
    operabilidad moderada (3,00), dado que su compatibilidad con
    navegación por teclado es parcial.

La <a href="#tbl-comparativa" class="quarto-xref">Tabla 3</a> presenta
una comparación directa de las puntuaciones de las cinco mejores
tecnologías frente al promedio general del conjunto.

<div id="tbl-comparativa">

Tabla 3: Comparación de puntuaciones de las cinco mejores tecnologías
frente al promedio general del conjunto de 41 tecnologías evaluadas.

| Tecnología           | Usabilidad | Robustez | Operabilidad | Global |
|----------------------|:----------:|:--------:|:------------:|:------:|
| DeepSeek             |    5.00    |   3.67   |     5.00     |  4.60  |
| Grid                 |    5.00    |   4.33   |     4.00     |  4.50  |
| ChatGPT              |    4.33    |   5.00   |     4.00     |  4.43  |
| Gemini 2.0           |    4.33    |   5.00   |     4.00     |  4.43  |
| Google Assistant     |    5.00    |   5.00   |     3.00     |  4.40  |
| **Promedio general** |    4.25    |   3.26   |     1.70     |   —    |

</div>

El análisis comparativo revela que las cinco mejores tecnologías superan
ampliamente el promedio general en todas las dimensiones. La diferencia
más notable se observa en operabilidad, donde el top 5 alcanza
puntuaciones entre 3,00 y 5,00 frente a una media general de 1,70. Este
resultado sugiere que la operabilidad es el factor diferenciador más
determinante: las tecnologías que ofrecen modalidades alternativas de
interacción (navegación por teclado y comandos de voz) tienden a obtener
puntuaciones globales superiores.

## Análisis de las características del top 5

Las cinco tecnologías mejor puntuadas comparten varias características
que explican su posición destacada:

- **Multimodalidad de interacción**: todas ofrecen al menos
  compatibilidad parcial con navegación por teclado y/o comandos de voz,
  a diferencia de muchas tecnologías de la muestra que carecen por
  completo de estas modalidades.
- **Uso intensivo de procesamiento de lenguaje natural**: las cinco
  emplean PLN como tecnología de IA central, frecuentemente combinado
  con reconocimiento de voz y síntesis de voz.
- **Cobertura de múltiples discapacidades**: cada una atiende al menos
  dos tipos de discapacidad, y dos de ellas (ChatGPT y Google Assistant)
  cubren tres categorías.
- **Vinculación con principios WCAG**: las altas puntuaciones en
  usabilidad reflejan contribuciones al principio Perceptible
  (generación de alternativas textuales y síntesis de voz) y
  Comprensible (simplificación de texto). Las puntuaciones de robustez
  se vinculan con el principio Robusto (compatibilidad multiplataforma),
  mientras que la operabilidad se relaciona directamente con el
  principio Operable (accesibilidad por teclado y modalidades
  alternativas de navegación).

Tres de las cinco tecnologías del top 5 son asistentes conversacionales
o por voz de grandes empresas tecnológicas (ChatGPT de OpenAI, Gemini
2.0 de Google, Google Assistant), lo que sugiere que los recursos de
desarrollo y la escala de distribución de estas compañías favorecen
tanto la compatibilidad multiplataforma como la integración de múltiples
modalidades de interacción. Las dos restantes (DeepSeek y Grid)
representan, respectivamente, un modelo de lenguaje emergente y un
software especializado de comunicación asistiva, demostrando que el alto
desempeño en accesibilidad no es exclusivo de los grandes actores del
mercado.

# Discusión

## Contraste de hallazgos con la literatura existente

Los resultados del presente estudio revelan patrones que convergen
parcialmente con la literatura previa sobre IA y accesibilidad web, al
tiempo que identifican divergencias significativas que enriquecen la
comprensión del campo. La concentración de tecnologías de IA orientadas
a la discapacidad motora (68,3% de la muestra) es consistente con los
hallazgos de Campoverde-Molina & Luján-Mora (2025), quienes en su mapeo
sistemático identificaron que la mayoría de las publicaciones sobre IA y
accesibilidad web se concentran en interfaces de interacción alternativa
para usuarios con limitaciones motrices. Del mismo modo, Giansanti &
Pirrera (2025) documentaron que las tecnologías asistivas basadas en IA
han priorizado históricamente las soluciones de control alternativo
—seguimiento ocular, interfaces cerebro-computadora y reconocimiento
gestual— por encima de otras modalidades de asistencia.

Sin embargo, la subrepresentación de la discapacidad auditiva en la
muestra evaluada (9,8%, solo 4 tecnologías) representa una divergencia
respecto a las expectativas derivadas de la literatura. Kuhn et al.
(2024) señalaron que el reconocimiento automático de voz ha alcanzado
niveles de precisión cada vez más competitivos, lo que sugeriría un
ecosistema tecnológico más amplio para la discapacidad auditiva. No
obstante, los resultados de este estudio indican que, si bien la
tecnología subyacente (reconocimiento de voz) ha madurado, su
integración en soluciones específicas de accesibilidad web para personas
con discapacidad auditiva sigue siendo limitada. Las herramientas
disponibles se concentran predominantemente en el subtitulado
automático, dejando sin atender necesidades como la traducción a lengua
de señas, la personalización de alertas visuales o la adaptación de
contenido multimedia.

El hallazgo de que la operabilidad constituye la dimensión con
puntuación más baja (*M* = 1,70) contrasta significativamente con el
énfasis que las pautas WCAG 2.2 otorgan al principio Operable (World
Wide Web Consortium, 2023). Este resultado concuerda con la observación
de Vollenwyder et al. (2023), quienes demostraron que el cumplimiento de
estándares de accesibilidad no garantiza una experiencia de usuario
satisfactoria, especialmente en lo referente a la navegabilidad por
teclado. La paradoja identificada en el presente estudio —tecnologías
diseñadas para asistir a personas con discapacidad motora que no ofrecen
ellas mismas mecanismos operables de forma accesible— amplía esta línea
argumentativa y sugiere que los desarrolladores de tecnologías asistivas
no siempre aplican los principios de accesibilidad a sus propios
productos.

En cuanto al desempeño de las cinco tecnologías mejor puntuadas, los
resultados coinciden con Acosta-Vargas, Salvador-Acosta, et al. (2024)
en que las herramientas de IA generativa presentan un potencial
significativo para la inclusión digital. No obstante, la presencia de
tres asistentes conversacionales de grandes empresas tecnológicas en el
top 5 (ChatGPT, Gemini 2.0 y Google Assistant) introduce una dimensión
no contemplada en la literatura: la relación entre los recursos de
desarrollo corporativo y la capacidad de ofrecer soluciones de
accesibilidad multiplataforma. Martins & Duarte (2024), en su análisis a
gran escala de accesibilidad web, documentaron que la adopción
tecnológica influye en los niveles de conformidad con WCAG, un hallazgo
que se extiende aquí al ámbito de las tecnologías asistivas basadas en
IA.

El predominio del procesamiento de lenguaje natural como técnica de IA
central en las tecnologías mejor evaluadas es consistente con López-Gil
& Pereira (2025), quienes demostraron que los modelos de lenguaje de
gran tamaño pueden transformar criterios WCAG manuales en evaluaciones
automáticas con niveles de precisión prometedores. Este resultado
sugiere que el PLN no solo es útil para la evaluación de conformidad,
sino que constituye la base tecnológica más versátil para la
implementación de soluciones de accesibilidad web.

## Vacío de conocimiento teórico

El análisis realizado permite argumentar la existencia de un vacío de
conocimiento teórico significativo en la intersección IA-accesibilidad
web. A pesar del crecimiento exponencial de publicaciones documentado
por Chemnad & Othman (2024) en su análisis bibliométrico y revisión
sistemática de la accesibilidad digital en la era de la inteligencia
artificial, no se identifican marcos conceptuales consolidados que
integren de manera sistemática las capacidades de la IA con los cuatro
principios WCAG. La literatura existente aborda la relación
IA-accesibilidad de forma fragmentada: por un lado, los estudios sobre
accesibilidad web se centran en la conformidad con estándares sin
incorporar las capacidades emergentes de la IA (Abu Doush et al., 2023;
Ara et al., 2023); por otro, los estudios sobre tecnologías asistivas
basadas en IA evalúan soluciones específicas sin vincularlas con un
marco normativo de referencia (Esquivel et al., 2024; Schaur &
Matausch-Mahr, 2025).

Esta fragmentación teórica tiene consecuencias prácticas directas. La
ausencia de un marco integrador dificulta la evaluación comparativa de
tecnologías —como la propuesta en el presente estudio—, limita la
formulación de políticas públicas de inclusión digital basadas en
evidencia y obstaculiza el desarrollo de estándares técnicos que
orienten la integración de IA en las futuras versiones de las pautas
WCAG. Campoverde-Molina & Luján-Mora (2025) identificaron esta
fragmentación temática en su mapeo sistemático, señalando que las líneas
de investigación en IA y accesibilidad web permanecen inconexas, lo que
impide la consolidación de un cuerpo teórico coherente.

El presente estudio contribuye a este vacío proponiendo un marco
evaluativo que vincula dimensiones de desempeño tecnológico (usabilidad,
robustez, operabilidad) con los principios WCAG, ofreciendo una
estructura replicable para futuras evaluaciones comparativas. Sin
embargo, se reconoce que este marco constituye una aproximación inicial
que requiere validación empírica y refinamiento iterativo.

## Vacío de conocimiento práctico

Más allá del vacío teórico, los resultados evidencian un vacío práctico
igualmente relevante. La baja puntuación media de operabilidad (*M* =
1,70) revela que la mayoría de las tecnologías de IA evaluadas presentan
barreras significativas en su implementación real para usuarios con
discapacidad. Doce tecnologías obtuvieron una puntuación de operabilidad
de 0,00, indicando ausencia total de compatibilidad con navegación por
teclado y comandos de voz. Esta barrera práctica contradice el propósito
declarado de estas herramientas y evidencia una brecha entre el
potencial teórico de la IA para la accesibilidad y su implementación
efectiva.

Mowar (2024), al examinar la integración de accesibilidad en el
desarrollo web asistido por IA, identificó que la accesibilidad suele
ser considerada como un aspecto secundario en el ciclo de desarrollo,
incluso en productos orientados a personas con discapacidad. Los
resultados de este estudio confirman esta observación: las tecnologías
que no ofrecen soporte de navegación por teclado ni comandos de voz no
pueden ser operadas de forma autónoma por una parte significativa de sus
usuarios objetivo, lo que constituye una paradoja funcional que limita
su impacto real.

Asimismo, la brecha entre las puntuaciones del top 5 y el promedio
general —particularmente en operabilidad, donde el rango del top 5
(3,00-5,00) contrasta con la media general (1,70)— sugiere que la
accesibilidad integral es técnicamente viable pero no se ha
generalizado. Las tecnologías mejor puntuadas demuestran que es posible
alcanzar altos niveles de usabilidad, robustez y operabilidad
simultáneamente, por lo que la adopción limitada de prácticas de
accesibilidad en el resto de la muestra responde a factores de
priorización en el diseño, recursos de desarrollo y estrategias
comerciales, más que a limitaciones tecnológicas intrínsecas.

Fuglerud et al. (2024), al explorar el uso de IA para mejorar las
pruebas de accesibilidad, señalaron que las herramientas automatizadas
pueden detectar solo un subconjunto de las barreras existentes, lo que
sugiere que la evaluación de accesibilidad de las propias tecnologías
asistivas requiere métodos complementarios que incluyan pruebas con
usuarios reales. Este hallazgo refuerza la necesidad de estudios
empíricos que complementen el análisis documental-descriptivo del
presente trabajo.

## Limitaciones del estudio

El presente estudio presenta varias limitaciones que deben considerarse
al interpretar los resultados. En primer lugar, el **tamaño de la
muestra** (41 tecnologías) ofrece una visión representativa pero no
exhaustiva del ecosistema de tecnologías de IA para accesibilidad web.
La selección intencional, si bien permite una cobertura diversa de tipos
de producto y discapacidades atendidas, introduce un sesgo de selección
que puede haber excluido tecnologías relevantes no identificadas durante
la fase de recopilación.

En segundo lugar, los **criterios de evaluación** basados en
documentación técnica pública presentan limitaciones inherentes. La
precisión, sensibilidad y tiempo de respuesta reportados por los
desarrolladores pueden diferir del desempeño real experimentado por los
usuarios, y las evaluaciones categóricas (Baja/Media/Alta) implican un
grado de simplificación que reduce la granularidad del análisis. El
mapeo categórico-numérico, aunque necesario para la comparabilidad
cuantitativa, introduce transformaciones que pueden no capturar matices
cualitativos relevantes.

En tercer lugar, la **temporalidad del dataset** constituye una
limitación significativa en un campo tecnológico de evolución acelerada.
Las versiones, funcionalidades y compatibilidades de las tecnologías
evaluadas corresponden al momento de la recopilación de datos, y pueden
haber experimentado cambios sustanciales desde entonces. Esta limitación
es particularmente relevante para las tecnologías basadas en modelos de
lenguaje de gran tamaño, cuyas capacidades se actualizan con frecuencia.

Finalmente, la **ausencia de validación empírica con usuarios finales**
limita la interpretación de las puntuaciones de usabilidad y
operabilidad. Si bien el enfoque documental-descriptivo es
metodológicamente válido para una caracterización inicial del ecosistema
tecnológico, no sustituye las evaluaciones de usabilidad con personas
con discapacidad real, cuyos resultados podrían diferir
significativamente de las especificaciones documentadas.

## Líneas futuras de investigación

A partir de los vacíos identificados y las limitaciones reconocidas, se
proponen las siguientes líneas futuras de investigación:

1.  **Estudios empíricos con usuarios finales**: desarrollar
    evaluaciones de usabilidad con personas con discapacidad para
    contrastar las puntuaciones documentales con la experiencia real de
    uso, siguiendo las recomendaciones de Brajnik et al. (2011) sobre la
    influencia de la experiencia del evaluador en los resultados.

2.  **Desarrollo de un marco teórico integrador**: construir un modelo
    conceptual que vincule formalmente las capacidades de la IA (PLN,
    visión por computadora, reconocimiento de voz, interfaces
    cerebro-computadora) con los criterios de éxito WCAG 2.2,
    permitiendo evaluaciones más precisas y estandarizadas.

3.  **Ampliación de la muestra y actualización longitudinal**: expandir
    el dataset a un mayor número de tecnologías e implementar un
    mecanismo de actualización periódica que capture la evolución del
    campo, particularmente en tecnologías de IA generativa.

4.  **Investigación sobre discapacidad auditiva e IA**: abordar la
    subrepresentación identificada mediante estudios específicos sobre
    la integración de IA en herramientas de accesibilidad web para
    personas con discapacidad auditiva, más allá del subtitulado
    automático.

5.  **Evaluación de la operabilidad como factor diferenciador**:
    profundizar en el análisis de por qué la operabilidad presenta
    puntuaciones tan bajas y desarrollar directrices de diseño accesible
    para los propios desarrolladores de tecnologías asistivas, en línea
    con los hallazgos de Salehnamadi et al. (2025) sobre detección
    automática de problemas de accesibilidad.

6.  **Análisis de factores socioeconómicos**: investigar la relación
    entre el modelo de negocio de las tecnologías (gratuitas vs. de
    pago), los recursos de desarrollo y los niveles de accesibilidad
    alcanzados, dado el predominio de productos de grandes empresas
    tecnológicas en el top 5.

## Implicaciones para la inclusión digital y los Objetivos de Desarrollo Sostenible

Los hallazgos de este estudio tienen implicaciones directas para dos
Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030 de las
Naciones Unidas.

En relación con el **ODS 10 (Reducción de las desigualdades)**, la
brecha identificada en la cobertura de tecnologías de IA por tipo de
discapacidad —con una concentración desproporcionada en discapacidad
motora y una subrepresentación de la discapacidad auditiva— evidencia
una forma de desigualdad digital que reproduce patrones de exclusión
preexistentes. La meta 10.2 del ODS 10, que busca empoderar y promover
la inclusión social, económica y política de todas las personas
independientemente de su condición, requiere que el desarrollo
tecnológico atienda de forma equitativa todos los tipos de discapacidad,
no solo aquellos con mayor visibilidad comercial o investigativa.

En relación con el **ODS 4 (Educación de calidad)**, la accesibilidad
web mediada por IA tiene un potencial transformador para garantizar una
educación inclusiva y equitativa. Las tecnologías evaluadas
—particularmente los asistentes conversacionales, los simplificadores de
texto y los generadores de descripciones de imágenes— pueden facilitar
el acceso a contenidos educativos digitales para estudiantes con
discapacidad, contribuyendo a la meta 4.5 que busca eliminar las
disparidades en la educación (Acosta-Vargas, Acosta-Vargas, et al.,
2024). Sin embargo, la baja operabilidad generalizada de las tecnologías
evaluadas plantea un riesgo: si las herramientas de IA destinadas a
facilitar la educación inclusiva no son ellas mismas accesibles, se
perpetúa un ciclo de exclusión que contradice los objetivos del ODS 4.

Estos vínculos con los ODS subrayan que la accesibilidad web no es un
desafío exclusivamente técnico, sino un imperativo ético y social que
requiere la colaboración entre desarrolladores, investigadores,
organismos de estandarización y formuladores de políticas públicas.

# Conclusiones

El presente estudio analizó y categorizó 41 tecnologías de inteligencia
artificial según su utilidad para la accesibilidad web bajo las pautas
WCAG 2.2, evaluando tres dimensiones —usabilidad, robustez y
operabilidad— y clasificando cada tecnología por tipo de discapacidad
atendida. Los hallazgos principales permiten extraer las siguientes
conclusiones.

En primer lugar, la distribución de tecnologías de IA por tipo de
discapacidad revela una cobertura marcadamente desigual. La discapacidad
motora concentra la mayor proporción de soluciones (68,3%), mientras que
la discapacidad auditiva presenta la menor cobertura (9,8%). Este
desequilibrio evidencia que el desarrollo tecnológico en IA accesible no
responde proporcionalmente a la distribución de necesidades, sino a
factores como la madurez de las técnicas de interacción alternativa, la
visibilidad investigativa y las prioridades comerciales de los
desarrolladores.

En segundo lugar, el análisis de las dimensiones de evaluación
identifica la operabilidad como el factor más crítico y diferenciador.
Con una puntuación media de 1,70 —frente a 4,25 en usabilidad y 3,26 en
robustez—, la operabilidad constituye la principal barrera de
accesibilidad del conjunto evaluado. La paradoja de que tecnologías
diseñadas para asistir a personas con discapacidad no ofrezcan ellas
mismas mecanismos de operación accesibles subraya la necesidad de
incorporar principios de diseño universal en el ciclo de desarrollo de
las propias tecnologías asistivas.

En tercer lugar, las cinco tecnologías mejor evaluadas —DeepSeek, Grid,
ChatGPT, Gemini 2.0 y Google Assistant— demuestran que es técnicamente
viable alcanzar niveles altos de usabilidad, robustez y operabilidad de
forma simultánea. Estas tecnologías comparten características comunes:
multimodalidad de interacción, uso intensivo de procesamiento de
lenguaje natural y cobertura de múltiples tipos de discapacidad. Su
identificación como buenas prácticas ofrece un referente concreto para
orientar el diseño de futuras tecnologías de IA accesible.

La contribución original de este estudio reside en la propuesta de un
marco evaluativo que vincula dimensiones de desempeño tecnológico con
los principios WCAG 2.2, permitiendo una categorización y comparación
sistemática de tecnologías de IA para la accesibilidad web. El análisis
aporta evidencia cuantitativa sobre la existencia de un doble vacío de
conocimiento: un vacío teórico, caracterizado por la ausencia de marcos
conceptuales integradores en la intersección IA-WCAG, y un vacío
práctico, manifestado en las barreras de implementación que limitan el
impacto real de las tecnologías evaluadas.

Las líneas futuras de investigación derivadas de este trabajo incluyen
el desarrollo de estudios empíricos con usuarios finales con
discapacidad, la construcción de un marco teórico integrador IA-WCAG, la
ampliación longitudinal del dataset y la investigación específica sobre
las brechas en la cobertura de la discapacidad auditiva. Asimismo, se
recomienda que los organismos de estandarización y los desarrolladores
de tecnologías asistivas incorporen criterios de operabilidad accesible
como requisito fundamental, alineándose con los Objetivos de Desarrollo
Sostenible 4 y 10 que promueven la educación inclusiva y la reducción de
las desigualdades.

# Referencias

<div id="refs" class="references csl-bib-body hanging-indent"
entry-spacing="0" line-spacing="2">

<div id="ref-abascal2016" class="csl-entry">

Abascal, J., Barbosa, S. D. J., Nicolle, C., & Zaphiris, P. (2016).
Rethinking universal accessibility: a broader approach considering the
digital gap. *Universal Access in the Information Society*, *15*(2),
179-182. <https://doi.org/10.1007/s10209-015-0416-1>

</div>

<div id="ref-doush2023" class="csl-entry">

Abu Doush, I., Sultan, K., Al-Betar, M. A., Alsaeedi, A., & Awwad, A.
(2023). Web accessibility automatic evaluation tools: to what extent can
they be automated? *CCF Transactions on Pervasive Computing and
Interaction*, *5*, 288-320. <https://doi.org/10.1007/s42486-023-00127-8>

</div>

<div id="ref-acosta-vargas2024icedeg" class="csl-entry">

Acosta-Vargas, P., Acosta-Vargas, G., Salvador-Acosta, B., &
Jadán-Guerrero, J. (2024). Addressing Web Accessibility Challenges with
Generative Artificial Intelligence Tools for Inclusive Education.
*Proceedings of the 10th International Conference on eDemocracy and
eGovernment (ICEDEG 2024)*.
<https://doi.org/10.1109/ICEDEG61611.2024.10702085>

</div>

<div id="ref-acostavargas2024" class="csl-entry">

Acosta-Vargas, P., Salvador-Acosta, B., Novillo-Villegas, S., Sarantis,
D., & Salvador-Ullauri, L. A. (2024). Generative Artificial Intelligence
and Web Accessibility: Towards an Inclusive and Sustainable Future.
*Emerging Science Journal*, *8*(4), 1602-1621.
<https://doi.org/10.28991/ESJ-2024-08-04-021>

</div>

<div id="ref-alsaeedi2020" class="csl-entry">

Alsaeedi, A. (2020). Comparing Web Accessibility Evaluation Tools and
Evaluating the Accessibility of Webpages: Proposed Frameworks.
*Information*, *11*(1), 40. <https://doi.org/10.3390/info11010040>

</div>

<div id="ref-ara2023" class="csl-entry">

Ara, J., Sik-Lanyi, C., & Kelemen, A. (2023). Accessibility engineering
in web evaluation process: a systematic literature review. *Universal
Access in the Information Society*, *23*, 233-260.
<https://doi.org/10.1007/s10209-023-00967-2>

</div>

<div id="ref-ara2025" class="csl-entry">

Ara, J., Sik-Lanyi, C., Kelemen, A., & Guzsvinecz, T. (2025). An
inclusive framework for automated web content accessibility evaluation.
*Universal Access in the Information Society*, *24*, 1581-1607.
<https://doi.org/10.1007/s10209-024-01164-5>

</div>

<div id="ref-ara2023coginfo" class="csl-entry">

Ara, J., & Sik-Lányi, C. (2023). Webpage Accessibility Evaluation Using
Machine Learning Technique. *Proceedings of the 14th IEEE International
Conference on Cognitive Infocommunications (CogInfoCom 2023)*, 69-74.
<https://doi.org/10.1109/CogInfoCom59411.2023.10397496>

</div>

<div id="ref-belwafi2024" class="csl-entry">

Belwafi, K., & Ghaffari, F. (2024). Thought-Controlled Computer
Applications: A Brain–Computer Interface System for Severe Disability
Support. *Sensors*, *24*(20), 6759. <https://doi.org/10.3390/s24206759>

</div>

<div id="ref-brajnik2011" class="csl-entry">

Brajnik, G., Yesilada, Y., & Harper, S. (2011). The Expertise Effect on
Web Accessibility Evaluation Methods. *Human–Computer Interaction*,
*26*(3), 246-283. <https://doi.org/10.1080/07370024.2011.601670>

</div>

<div id="ref-campoverde-molina2025" class="csl-entry">

Campoverde-Molina, M., & Luján-Mora, S. (2025). Artificial intelligence
in web accessibility: A systematic mapping study. *Computer Standards &
Interfaces*, *96*, 104055. <https://doi.org/10.1016/j.csi.2025.104055>

</div>

<div id="ref-chemnad2024" class="csl-entry">

Chemnad, K., & Othman, A. (2024). Digital accessibility in the era of
artificial intelligence—Bibliometric analysis and systematic review.
*Frontiers in Artificial Intelligence*, *7*, 1349668.
<https://doi.org/10.3389/frai.2024.1349668>

</div>

<div id="ref-chhimpa2024" class="csl-entry">

<span class="nocase">Chhimpa, G. R., Kumar, A., Garhwal, S.,
et al.</span> (2024). Empowering individuals with disabilities: a
real-time, cost-effective, calibration-free assistive system utilizing
eye tracking. *Journal of Real-Time Image Processing*, *21*, 97.
<https://doi.org/10.1007/s11554-024-01478-w>

</div>

<div id="ref-das2024" class="csl-entry">

Das, M., Fiannaca, A. J., Morris, M. R., Kane, S. K., & Bennett, C. L.
(2024). From Provenance to Aberrations: Image Creator and Screen Reader
User Perspectives on Alt Text for AI-Generated Images. *Proceedings of
the 2024 CHI Conference on Human Factors in Computing Systems*.
<https://doi.org/10.1145/3613904.3642325>

</div>

<div id="ref-esquivel2024" class="csl-entry">

Esquivel, P., Gill, K., Goldberg, M., Sundaram, S. A., Morris, L., &
Ding, D. (2024). Voice Assistant Utilization among the Disability
Community for Independent Living: A Rapid Review of Recent Evidence.
*Human Behavior and Emerging Technologies*, *2024*(1), 6494944.
<https://doi.org/10.1155/2024/6494944>

</div>

<div id="ref-fischer-janzen2024" class="csl-entry">

Fischer-Janzen, A., Wendt, T. M., & Van Laerhoven, K. (2024). A scoping
review of gaze and eye tracking-based control methods for assistive
robotic arms. *Frontiers in Robotics and AI*, *11*, 1326670.
<https://doi.org/10.3389/frobt.2024.1326670>

</div>

<div id="ref-fuglerud2024" class="csl-entry">

Fuglerud, K. S., Halbach, T., Utseth, I., & Waldeland, A. U. (2024).
Exploring the Use of AI for Enhanced Accessibility Testing of Web
Solutions. *Studies in Health Technology and Informatics, Volume 320:
Universal Design 2024*, 453-460. <https://doi.org/10.3233/SHTI241041>

</div>

<div id="ref-gartland2022" class="csl-entry">

Gartland, S., Flynn, P., Carneiro, M. A., Holloway, G., Fialho, J. de
S., Cullen, J., Hamilton, E., Harris, A., & Cullen, C. (2022). The State
of Web Accessibility for People with Cognitive Disabilities: A Rapid
Evidence Assessment. *Behavioral Sciences*, *12*(2), 26.
<https://doi.org/10.3390/bs12020026>

</div>

<div id="ref-giansanti2025" class="csl-entry">

Giansanti, D., & Pirrera, A. (2025). Integrating AI and Assistive
Technologies in Healthcare: Insights from a Narrative Review of Reviews.
*Healthcare*, *13*(5), 556. <https://doi.org/10.3390/healthcare13050556>

</div>

<div id="ref-kuhn2024" class="csl-entry">

Kuhn, K., Kersken, V., Reuter, B., Egger, N., & Zimmermann, G. (2024).
Measuring the Accuracy of Automatic Speech Recognition Solutions. *ACM
Transactions on Accessible Computing*, *16*(4).
<https://doi.org/10.1145/3636513>

</div>

<div id="ref-lazar2015" class="csl-entry">

Lazar, J., Goldstein, D. F., & Taylor, A. (2015). *Ensuring Digital
Accessibility through Process and Policy*. Morgan Kaufmann.
<https://doi.org/10.1016/C2013-0-13367-3>

</div>

<div id="ref-leotta2022" class="csl-entry">

Leotta, M., Mori, F., & Ribaudo, M. (2022). Evaluating the effectiveness
of automatic image captioning for web accessibility. *Universal Access
in the Information Society*, *22*, 1293-1313.
<https://doi.org/10.1007/s10209-022-00906-7>

</div>

<div id="ref-lopezgil2025" class="csl-entry">

López-Gil, J.-M., & Pereira, J. (2025). Turning manual web accessibility
success criteria into automatic: an LLM-based approach. *Universal
Access in the Information Society*, *24*, 837-852.
<https://doi.org/10.1007/s10209-024-01108-z>

</div>

<div id="ref-martins2024" class="csl-entry">

Martins, B., & Duarte, C. (2024). A large-scale web accessibility
analysis considering technology adoption. *Universal Access in the
Information Society*, *23*, 1857-1872.
<https://doi.org/10.1007/s10209-023-01010-0>

</div>

<div id="ref-moreno2024" class="csl-entry">

Moreno, L., Petrie, H., Martínez, P., & Alarcon, R. (2024). Designing
user interfaces for content simplification aimed at people with
cognitive impairments. *Universal Access in the Information Society*,
*23*, 99-117. <https://doi.org/10.1007/s10209-023-00986-z>

</div>

<div id="ref-mowar2024" class="csl-entry">

Mowar, P. (2024). Accessibility in AI-Assisted Web Development.
*Proceedings of the 21st International Web for All Conference (W4A
’24)*, 123-125. <https://doi.org/10.1145/3677846.3679054>

</div>

<div id="ref-othman2023" class="csl-entry">

Othman, A., Dhouib, A., & Al Jabor, A. N. (2023). Fostering websites
accessibility: A case study on the use of the Large Language Models
ChatGPT for automatic remediation. *Proceedings of the 16th
International Conference on PErvasive Technologies Related to Assistive
Environments (PETRA)*. <https://doi.org/10.1145/3594806.3596542>

</div>

<div id="ref-petrie2007" class="csl-entry">

Petrie, H., & Kheir, O. (2007). The relationship between accessibility
and usability of websites. *Proceedings of the SIGCHI Conference on
Human Factors in Computing Systems*, 397-406.
<https://doi.org/10.1145/1240624.1240688>

</div>

<div id="ref-salehnamadi2025" class="csl-entry">

Salehnamadi, N., Mehralian, F., & Malek, S. (2025). Enhancing Web
Accessibility: Automated Detection of Issues with Generative AI.
*Proceedings of the ACM on Software Engineering*, *2*(FSE), FSE101.
<https://doi.org/10.1145/3729371>

</div>

<div id="ref-schaur2025" class="csl-entry">

Schaur, M., & Matausch-Mahr, K. (2025). Assistive technology using
artificial intelligence in the long-term care sector for persons with
disabilities: A systematic literature review. *Technology and
Disability*. <https://doi.org/10.1177/10554181251355420>

</div>

<div id="ref-vollenwyder2023" class="csl-entry">

Vollenwyder, B., Petralito, S., Iten, G. H., Brühlmann, F., Opwis, K., &
Mekler, E. D. (2023). How compliance with web accessibility standards
shapes the experiences of users with and without disabilities.
*International Journal of Human-Computer Studies*, *170*, 102956.
<https://doi.org/10.1016/j.ijhcs.2022.102956>

</div>

<div id="ref-w3c2018wcag21" class="csl-entry">

World Wide Web Consortium. (2018). *Web Content Accessibility Guidelines
(WCAG) 2.1* \[W3C Recommendation\]. W3C. <https://www.w3.org/TR/WCAG21/>

</div>

<div id="ref-w3c2021coga" class="csl-entry">

World Wide Web Consortium. (2021). *Making Content Usable for People
with Cognitive and Learning Disabilities* \[W3C Working Group Note\].
W3C. <https://www.w3.org/TR/coga-usable/>

</div>

<div id="ref-w3c2023wcag22" class="csl-entry">

World Wide Web Consortium. (2023). *Web Content Accessibility Guidelines
(WCAG) 2.2* \[W3C Recommendation\]. W3C. <https://www.w3.org/TR/WCAG22/>

</div>

</div>
