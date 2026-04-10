# Reporte de Revisión — Marco teórico "tea-tecnologia"
**Fecha:** 2026-04-09
**Revista objetivo:** No definida (diferida a fase futura; el spec incremental no fija revista todavía)
**Revisor:** Claude (AI Reviewer)
**Artefacto revisado:** `paper/marco_teorico.md` (fase incremental: sólo marco teórico, ≈950 palabras)

> Nota estructural: este proyecto no utiliza el layout `paper/sections/` + `paper/outline.md` + `paper/metadata.yaml` que asume el comando estándar `/paper:review`. La spec incremental `tea-tecnologia` produce un artefacto único (`paper/marco_teorico.md`). Esta revisión se realiza sobre dicho artefacto más `references/references.bib`, aplicando las soft specs definidas en `CLAUDE.md` y los criterios del skill `peer-review`.

---

## Resumen Ejecutivo
El marco teórico cumple con las *hard specs* del framework (estructura C1..C9, extensión 950 palabras, prosa orgánica sin guiones separadores, citas APA en el cuerpo y sección final de referencias) y exhibe un recorrido argumental legible de lo general a lo específico que aterriza en una propuesta explícita. Sin embargo, presenta tres debilidades científicas relevantes que justifican una **Revisión Mayor**: (i) varios DOI de la bibliografía no han sido verificados contra CrossRef y al menos uno mezcla año de aparición con año del volumen; (ii) el bloque C4 confunde evidencia sobre población **Latinx** en Estados Unidos con evidencia regional **latinoamericana**; y (iii) el bloque C8, que debe ofrecer ejemplos tecnológicos "recientes", se apoya en estudios de 2012 y 2015 que ya no califican como recientes bajo el criterio del propio spec.

**Recomendación:** **Major Revision**.

## Fortalezas
1. **Trazabilidad requisito–componente impecable**. Los nueve bloques C1..C9 mapean uno a uno con los *acceptance criteria* del Requirement 2 y el cierre C9 articula de manera explícita la pregunta guía ("evaluar si las tecnologías tipo app podrían efectivamente ayudar a los adolescentes TEA"), cubriendo Requirements 5.1 y 5.2.
2. **Recorrido argumental coherente y sin saltos lógicos**. Las transiciones de mundial → latinoamericano → chileno → modelos pedagógicos → adolescencia → tecnologías → vacíos son naturales; cada bloque empuja al siguiente sin repeticiones ni retrocesos.
3. **Estilo riguroso y ajustado al contrato**. Prosa en párrafos largos y continuos, cero guiones como separadores, presupuesto de palabras por componente respetado (950 / 950), sin listas decorativas. Las convenciones de cita APA se aplican con consistencia.
4. **Densidad de datos cuantitativos útil** en los bloques epidemiológicos (C3 ~1% global, C5 1,31% bayesiano en Chile vs 0,46% escolar), lo que da al marco teórico sustento empírico concreto y no puramente conceptual.
5. **Bibliografía reciente y mayoritariamente de impacto** para los bloques C1..C7: las fuentes 2022–2025 provienen de revistas indexadas (*Autism*, *Brain Sciences*, *Italian Journal of Pediatrics*, *Frontiers in Psychiatry*, *International Journal of Molecular Sciences*, etc.).

## Debilidades Principales
1. **[CRÍTICO] Verificación de DOI pendiente y potenciales inconsistencias metadata.** Al menos las siguientes entradas requieren validación manual contra CrossRef antes de cerrar la fase:
   - **White et al. (2024)** con DOI `10.1080/15374416.2021.1790379`: el identificador apunta a un artículo publicado originalmente en 2021; el año 2024 probablemente corresponde a la aparición en volumen. Debe conciliarse el campo `year` o reetiquetar la cita como `White et al., 2021`.
   - **Rodríguez-Medina et al. (2024)**, **Valencia et al. (2024)**, **Montenegro-Rueda et al. (2025)**, **Lugo-Marín et al. (2024)** y **Roman-Urrestarazu et al. (2025)**: los DOI fueron redactados a partir de resultados de búsqueda web y no han pasado el hard check CrossRef/DOI definido en Requirement 6.2. Mientras no se validen, deberían marcarse como *pending* conforme al contrato de la sección "Citación APA Scopus" del diseño.
   - **Valencia et al. (2024)** en `references.bib` no tiene el campo `journal` ni `volume`, lo cual infringe la convención mínima de campos documentada en el encabezado del BibTeX.

2. **[CRÍTICO] Ejemplos de tecnologías en C8 no son recientes.** El Requirement 4.3 y el diseño (C8 *Tecnologías y Apps*) exigen fuentes Scopus "preferentemente de los últimos años". Dos de los tres ejemplos son:
   - **Kellems & Morningstar (2012)** — antecedente conceptual de *VidCoach*, no el estudio canónico de la app.
   - **Rice et al. (2015)** — estudio de *FaceSay* con más de diez años de antigüedad.
   Sólo **Kahn et al. (2022)** (Mightier) entra en el rango exigido por el criterio de recencia. El bloque transmite la impresión de que las evidencias son contemporáneas cuando dos tercios de las apps citadas cuentan con evaluaciones de hace más de una década; esto debilita la articulación con C9, que presenta la propuesta como respuesta a una "falta de evidencia reciente".

3. **[CRÍTICO] C4 confunde "Latinoamérica" con "Latinx" (población hispana en EE.UU.).** La cita **Lugo-Marín et al. (2024)** en el *Journal of Autism and Developmental Disorders*, "Barriers to Healthcare for Latinx Autistic Children and Adolescents", se refiere a la experiencia de familias latinas residentes en Estados Unidos, no al acceso a servicios dentro de países latinoamericanos. Extrapolar sus barreras ("culturales, económicas y de alfabetización en salud") a Latinoamérica es una inferencia no sostenida por la fuente. Debe reemplazarse por evidencia regional real (p. ej. Paula et al. en Brasil, estudios del consorcio REAL de Argentina/Uruguay/Chile) o reformularse explícitamente el alcance del párrafo.

4. **[IMPORTANTE] C6 carece de anclaje latinoamericano/chileno.** Las citas de este bloque son **Petersson-Bloom & Holmqvist (2022)** (Suecia) y **Rodríguez-Medina et al. (2024)** (España). El puente argumental entre C5 (Chile) y C7 (adolescentes) se apoya por completo en literatura europea, lo cual rompe la promesa del diseño de "aterrizar al contexto chileno". Se requiere al menos una fuente sobre modelos pedagógicos excluyentes en Latinoamérica o Chile para no dejar C6 argumentalmente suspendido.

5. **[IMPORTANTE] La meta-claim de C9 sobre los vacíos no está citada.** El cierre afirma que "la evidencia latinoamericana y chilena sobre adolescentes TEA es escasa" y que las apps "se han validado en contextos anglosajones y en edades tempranas". Ambas son afirmaciones empíricas que, bajo Requirement 4.2, deberían tener respaldo (típicamente una revisión de alcance o meta-revisión). Actualmente dependen únicamente de la ausencia de fuentes encontradas por el revisor, lo cual no es equivalente a evidencia de ausencia.

6. **[IMPORTANTE] Discrepancia no reconciliada de prevalencia en C3.** El párrafo cita ~1% (Talantseva et al., 2023) y ~0,6% (Salari et al., 2022) sin explicar por qué difieren (metodología de los meta-análisis, años incluidos, criterios diagnósticos). El lector queda con dos cifras oficiales contradictorias y sin herramientas para decidir cuál adoptar como referencia para el paper.

7. **[MENOR] Uso inconsistente de lenguaje persona-primero vs identidad-primero.** El texto alterna "niños TEA", "estudiantes con TEA" y "niños con autismo". La literatura actual recomienda declarar explícitamente la convención adoptada; en contextos editoriales recientes (*Autism*, *JADD*) el lenguaje identidad-primero ("autistic children / adolescentes autistas") es cada vez más frecuente.

8. **[MENOR] Sesgo de publicación no discutido en C8.** Las tres apps se presentan exclusivamente por sus efectos positivos. No se menciona el tamaño muestral reducido de los estudios primarios, la ausencia de réplicas independientes ni la posibilidad de resultados nulos no publicados, todos limitantes habituales en este tipo de literatura.

9. **[MENOR] Definición en C1 acotada al DSM-5.** No se menciona la CIE-11, que es el marco diagnóstico oficial del sistema de salud chileno. Dada la orientación latinoamericana del paper, omitir la CIE-11 es una decisión debatible.

## Evaluación por Sección

No aplica la matriz IMRaD (este entregable es solo el marco teórico). Se evalúan los nueve componentes narrativos definidos en el diseño.

| Componente | Claridad | Sustento empírico | Trazabilidad a Req. | Comentarios |
|---|---|---|---|---|
| **C1 Definición TEA** | 5/5 | 4/5 | 2.1 ✓ | Sólida. Considerar añadir CIE-11. |
| **C2 Niños TEA** | 4/5 | 4/5 | 2.2 ✓ | Bien articulado; podría precisar qué "intervenciones individualizadas". |
| **C3 TEA mundial** | 4/5 | 3/5 | 2.3 ✓ | Reconciliar la discrepancia 1% vs 0,6%. |
| **C4 TEA Latinoamérica** | 3/5 | 2/5 | 2.4 parcial | **Confusión Latinx vs Latinoamérica**. Requiere reemplazo de fuente. |
| **C5 TEA niños en Chile** | 5/5 | 5/5 | 2.5 ✓ | Mejor bloque del texto. Dato bayesiano potente. |
| **C6 Modelos pedagógicos** | 4/5 | 3/5 | 2.6 parcial | Falta anclaje LATAM/Chile; nombra "pull-out" pero no otros modelos concretos. |
| **C7 Adolescentes TEA** | 4/5 | 4/5 | 2.7 ✓ | Coherente. La cita White et al. requiere verificación de año. |
| **C8 Tecnologías** | 4/5 | 3/5 | 2.8 parcial | Tres apps nombradas ✓, pero dos fuentes no son recientes. |
| **C9 Vacíos y propuesta** | 5/5 | 2/5 | 2.9, 5.1, 5.2, 5.3 parcial | Meta-claim del vacío sin cita. |

## Claims sin Soporte Suficiente

1. **"la evidencia latinoamericana y chilena sobre adolescentes TEA es escasa frente a la producción centrada en la infancia"** — C9 — *Sugerencia:* respaldar con una revisión de alcance o con un conteo propio en Scopus que documente la asimetría (p. ej., "*n* publicaciones en población infantil vs *n* en adolescentes TEA entre 2019 y 2025 con filial latinoamericana").
2. **"la mayoría de las experiencias documentadas con tecnologías tipo app se han validado en contextos anglosajones y en edades tempranas"** — C9 — *Sugerencia:* citar explícitamente la revisión sistemática de Valencia et al. (2024) si ésta ya lo documenta, o sustituir por un metaanálisis específico sobre geografía e intervalo etario.
3. **"A esto se suman barreras culturales, económicas y de alfabetización en salud que fragmentan el acceso a servicios especializados para las familias latinas"** — C4 — *Sugerencia:* reemplazar fuente por estudios de Latinoamérica propiamente dicha; como está, la fuente (Lugo-Marín et al., 2024) es sobre familias Latinx en EE.UU.
4. **"ha sido señalada como una forma persistente de exclusión encubierta"** — C6 — *Sugerencia:* la cita soporta la crítica al pull-out, pero en Suecia; añadir evidencia chilena/regional si se quiere sostener el puente argumental con C5.
5. **"revisiones sistemáticas recientes confirman la efectividad de estas tecnologías digitales en el manejo del TEA durante la adolescencia"** — C8 — *Sugerencia:* la afirmación "en la adolescencia" es más fuerte que lo que Valencia et al. (2024) normalmente soporta (su alcance suele incluir "niños y adolescentes"). Moderar el lenguaje o añadir una revisión dedicada a adolescentes.

## Coherencia Argumentativa
- ¿El problema planteado en la apertura (C1..C2) es resuelto por el cierre (C9)? **Parcialmente.** El cierre articula bien la pregunta, pero el problema inicial se enmarca desde lo clínico-general y el cierre lo resuelve desde lo pedagógico-tecnológico, sin un anclaje intermedio que cosa ambos horizontes.
- ¿Los componentes aportan al cierre sin solapamientos? **Sí**, con una pequeña advertencia en C2/C5 donde "niños TEA en general" y "niños TEA en Chile" podrían reforzarse mutuamente más explícitamente.
- ¿La transición C5 → C6 → C7 es fluida? **Parcialmente.** C6 se siente eurocéntrico y rompe la continuidad geográfica establecida en C5.
- ¿C9 introduce conceptos no desarrollados antes? **Casi no.** Aparece "planes de apoyo individualizados" que no había sido explicitado; es un concepto inferible pero no nombrado antes.

## Reproducibilidad
- ¿La metodología de búsqueda bibliográfica está documentada? **No**, y en este entregable no se espera (es marco teórico). Sin embargo, recomiendo registrar en `research.md` las cadenas de búsqueda usadas por componente para que la fase de introducción extendida pueda reproducirlas.
- ¿Existe correspondencia uno a uno entre `references.bib` y la sección APA? **Sí**, verificado: 17 entradas inline ↔ 17 entradas en `references.bib` para el paper (más la entrada heredada `bachelard1957` no utilizada en este marco).

## Preguntas para los Autores
1. ¿Se va a adoptar CIE-11 o DSM-5 como referencia diagnóstica principal, considerando que el estudio mira al contexto chileno?
2. ¿Por qué se eligieron precisamente *VidCoach*, *FaceSay* y *Mightier* frente a alternativas con evaluaciones más recientes en adolescentes (p. ej. *FaceFinder*, *Frame*, *Stress Monitor*, *NDTx-01*)?
3. ¿Existe una definición operativa de "tecnologías tipo app" que acote el alcance del paper (mobile-only vs web-based vs híbridas; apps clínicas validadas vs apps comerciales)?
4. ¿El grupo etario de interés son "adolescentes" en sentido estricto (10–19 años) o se extiende a estudiantes universitarios (hasta ~24 años)? El marco teórico oscila entre ambos y la fase siguiente necesitará fijarlo.
5. ¿Se adoptará lenguaje persona-primero o identidad-primero? La decisión afecta la redacción de todo el manuscrito.

## Sugerencias Concretas por Componente

### C1 Definición TEA
- Añadir una oración breve sobre CIE-11 si el paper tiene orientación latinoamericana.

### C3 TEA a nivel mundial
- Reconciliar 1% vs 0,6%: "Los metaanálisis más recientes convergen en un rango entre 0,6% y 1,1% según los criterios incluidos (Salari et al., 2022; Talantseva et al., 2023)".

### C4 TEA en Latinoamérica
- Reemplazar Lugo-Marín et al. (2024) por estudios regionales genuinos (Montiel-Nava, Paula, Rattazzi, consorcio REAL, OPS/OMS).
- O reformular: "familias latinas migrantes en EE.UU." y trasladar esa mención a una nota secundaria.

### C6 Modelos pedagógicos excluyentes
- Incorporar al menos una fuente chilena o latinoamericana sobre exclusión escolar de estudiantes con TEA (p. ej. estudios sobre el Programa de Integración Escolar chileno).
- Nombrar al menos otro modelo además del *pull-out* (p. ej. pedagogía remedial, enfoque deficitario, integración vs inclusión).

### C8 Tecnologías y apps
- Sustituir Kellems (2012) y Rice (2015) por evaluaciones posteriores a 2020 que existan sobre las mismas apps o por otras apps con evidencia 2021–2025.
- Añadir una frase sobre limitaciones de los estudios citados (tamaño muestral, contextos de alto ingreso, ausencia de réplica).

### C9 Vacíos y propuesta
- Respaldar la meta-claim de escasez con una cita (revisión de alcance o bibliometría).
- Definir operativamente "ayudar" en la frase-propuesta: ¿en qué dimensión (comunicación, regulación, transición educativa)? Esto facilita enlazar con las preguntas/hipótesis de la fase siguiente.

## Checklist de Requisitos del Framework (Hard Specs — ya auditadas)
- [x] Estructura C1..C9 presente
- [x] Cada claim lleva una cita [APA]
- [x] Sección "Referencias bibliográficas" presente en APA
- [x] BibTeX consolidado en `references/references.bib`
- [x] No hay secciones vacías ni bajo mínimo de palabras (950 / 800–950)
- [x] Redacción íntegra en español
- [x] Párrafos largos y orgánicos sin guiones separadores
- [x] Alcance incremental (solo marco teórico en `paper/`)
- [ ] **Todas las referencias verificables contra CrossRef/DOI** — pendiente (ver debilidad crítica #1)
- [ ] **Formato de cita Scopus-reciente en C8** — no cumplido (ver debilidad crítica #2)
- [ ] Glosario de terminología (persona-first vs identity-first) — no existe

## Decisión Recomendada (Revisión 1)
**Major Revision**

**Razón principal:** El marco teórico pasa todas las *hard specs* automatizables del framework y tiene una estructura argumental sólida, pero tres puntos sustantivos (validación CrossRef de DOIs; confusión Latinx/Latinoamérica en C4; antigüedad de las fuentes tecnológicas en C8) afectan directamente la credibilidad académica del entregable. Son problemas corregibles sin reescribir el texto, pero deben resolverse antes de abrir la fase de "introducción extendida" para evitar arrastrar errores aguas abajo.

**Plan mínimo sugerido antes de fast-track a la siguiente fase:**
1. Ejecutar validación CrossRef/DOI sobre las 17 entradas del BibTeX (corregir las que fallen o marcarlas como *pending*).
2. Sustituir Lugo-Marín et al. (2024) en C4 por evidencia latinoamericana auténtica.
3. Refrescar dos de las tres tecnologías en C8 con evaluaciones 2021–2025.
4. Añadir una cita de soporte a la meta-claim de vacíos en C9.
5. Conciliar la discrepancia 1% vs 0,6% en C3 con una frase aclaratoria.

Con esas cinco correcciones, el artefacto podría reevaluarse como **Minor Revision** y avanzar al siguiente hito incremental del paper.

---

## Addendum: Resultado de la Revisión Mayor (2026-04-09)

Se ejecutaron las cinco correcciones solicitadas. Resumen de los cambios:

| # | Problema | Acción | Estado |
|---|----------|--------|--------|
| 1 | DOIs sin verificar / incorrectos | Se corrieron 17 DOIs contra la API CrossRef. Se detectaron 4 DOIs que retornaban 404, 3 DOIs que apuntaban a papers distintos, y 3 años incorrectos. Se reemplazaron todas las entradas con DOIs verificados. | **Corregido** |
| 2 | C4: Lugo-Marín (Latinx en EE.UU.) | Reemplazado por Paula et al. (2020), estudio multicéntrico del consorcio REAL en seis países latinoamericanos. DOI verificado: 10.1177/1362361320940073. | **Corregido** |
| 3 | C8: fuentes de 2012 y 2015 | VidCoach (2012) → Yface (Chung & Chung, 2023, RCT piloto). FaceSay (2015) → Programa metaverso Roblox (Lee et al., 2023, RCT en eClinicalMedicine/Lancet). Mightier corregido a año 2021 (CrossRef). Valencia et al. (DOI incorrecto) → Xu et al. (2024), metaanálisis en JADD. Todas las fuentes de C8 son ahora 2021–2024. | **Corregido** |
| 4 | C9: meta-claim sin cita | Añadida cita a Zainal & Zahri (2025), estudio bibliométrico de 243 artículos Scopus que documenta la concentración de investigación en países anglosajones y la subrepresentación de Latinoamérica. DOI: 10.26803/ijlter.24.9.15. | **Corregido** |
| 5 | C3: discrepancia 1% vs 0,6% | Reescrito como rango convergente "entre el 0,6 y el 1,1 por ciento" con ambas fuentes en una sola cita. | **Corregido** |

### Correcciones adicionales detectadas durante la revisión:
- **C1**: Micai et al. (2023, DOI incorrecto) → Lord et al. (2020), *Nature Reviews Disease Primers*. Fuente canónica para la definición del TEA.
- **C2**: Genovese & Butler (DOI incorrecto para IJMS) → Corregido al artículo real en *Genes* (DOI: 10.3390/genes14030677).
- **C6**: Rodríguez-Medina et al. (autores/DOI fabricados) → Vidal-Esteve et al. (2023), *Int J Developmental Disabilities* (DOI: 10.1080/20473869.2023.2173837). Se añadió framing "europeos como iberoamericanos".
- **C7**: White et al. corregido de 2024 a 2021 (DOI: 10.1080/15374416.2019.1669157). Montenegro-Rueda corregido a 2025 (advance online).
- **Petersson-Bloom & Holmqvist**: DOI corregido de ...221130704 a ...221123429.

### Decisión post-corrección: **Minor Revision**
Las cinco debilidades críticas/importantes han sido resueltas. Quedan pendientes las debilidades menores (#7 convención de lenguaje, #8 sesgo de publicación en C8, #9 CIE-11 en C1) que requieren decisión del autor pero no bloquean el avance a la siguiente fase incremental.

**Conteo final**: 949 palabras | 18 citas inline | 18 entradas APA | 18 entradas BibTeX | 0 guiones separadores.
