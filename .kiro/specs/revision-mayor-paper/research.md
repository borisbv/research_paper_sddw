# Research & Design Decisions

## Summary
- **Feature**: `revision-mayor-paper`
- **Discovery Scope**: Extension (modificación de manuscrito existente)
- **Key Findings**:
  - REIS requiere adherencia a PRISMA 2020 para revisiones sistemáticas; el checklist tiene 27 ítems obligatorios
  - La fuente "Publicación sobre migrantes colombianos en Chile, s.f." probablemente corresponde a un estudio empírico propio de los autores aún no publicado — requiere decisión sobre cómo citarlo
  - El paper tiene ~5,500 palabras actualmente; REIS permite hasta 8,000, dejando margen para agregar análisis bibliométrico y detalles metodológicos

## Research Log

### Estándares PRISMA 2020 para revisiones sistemáticas
- **Context**: El review report identifica ausencia de diagrama PRISMA y falta de transparencia metodológica
- **Sources Consulted**: PRISMA 2020 Statement (Page et al., 2021, BMJ); guía de autores REIS
- **Findings**:
  - PRISMA 2020 requiere: diagrama de flujo con números en cada etapa, registro del protocolo (PROSPERO recomendado pero no obligatorio), cadenas de búsqueda exactas, evaluación de certeza de la evidencia
  - Para revisiones narrativas/de alcance (scoping reviews), PRISMA-ScR es alternativa válida
  - El paper tiene estructura de revisión sistemática pero sin todos los elementos formales
- **Implications**: Decidir si reposicionar como scoping review (menos exigente) o completar requisitos de revisión sistemática completa

### Naturaleza de los testimonios sin referencia
- **Context**: Los testimonios de "Cecilia" y "José" no tienen referencia académica verificable
- **Sources Consulted**: Texto del paper, referencias.bib
- **Findings**:
  - Los testimonios parecen provenir de un estudio empírico propio (entrevistas a migrantes colombianos en Chile)
  - Si es trabajo propio no publicado, puede citarse como "datos no publicados" o integrarse como estudio piloto
  - Si proviene de otro autor, debe identificarse la fuente exacta
- **Implications**: Requiere consulta al humano para determinar el origen de estos datos

### Guía de autores REIS
- **Context**: Verificar requisitos específicos de formato y extensión
- **Sources Consulted**: Normas para autores REIS (reis.cis.es)
- **Findings**:
  - Máximo 8,000 palabras (incluidas notas y referencias)
  - Resumen: máximo 150 palabras en español e inglés
  - Sistema de citas: Harvard (autor-año)
  - Requiere: declaración de conflicto de intereses, contribución de cada autor
  - Acepta material suplementario online
- **Implications**: El formato actual es compatible; hay margen de ~2,500 palabras para expansiones

## Architecture Pattern Evaluation

| Opción | Descripción | Fortalezas | Riesgos | Notas |
|--------|-------------|-----------|---------|-------|
| Revisión sistemática completa (PRISMA 2020) | Mantener el paper como revisión sistemática y completar todos los requisitos PRISMA | Mayor rigor, mejor recepción en REIS | Requiere más trabajo metodológico, posiblemente PROSPERO | Opción recomendada dado que ya se declara como revisión sistemática |
| Reposicionar como scoping review | Cambiar de revisión sistemática a scoping review (PRISMA-ScR) | Menos exigente en protocolo, admite síntesis narrativa | Puede percibirse como downgrade, cambia el frame del paper | Alternativa viable si el protocolo no fue pre-registrado |
| Revisión narrativa con elementos sistemáticos | Marco híbrido que usa búsqueda sistemática pero síntesis narrativa | Flexible, común en ciencias sociales | Menos riguroso que PRISMA, algunos revisores lo cuestionan | Opción pragmática |

## Design Decisions

### Decision: Mantener como revisión sistemática con PRISMA 2020
- **Context**: El paper ya se declara como revisión sistemática y la metodología describe un proceso de selección formal
- **Alternatives Considered**:
  1. Reposicionar como scoping review — menos exigente pero cambia el encuadre
  2. Mantener como revisión narrativa — no resuelve las objeciones del reviewer
- **Selected Approach**: Completar los elementos PRISMA 2020 faltantes manteniendo el encuadre actual
- **Rationale**: El proceso descrito (847 → 312 → 163) ya es compatible con PRISMA; solo faltan elementos de reporte
- **Trade-offs**: Más trabajo, pero mayor rigor y mejor recepción
- **Follow-up**: Verificar si el protocolo puede registrarse retrospectivamente en PROSPERO

### Decision: Reformular alcance como "revisión con foco interpretativo"
- **Context**: Brecha entre promesa (Chile, venezolanos/colombianos) y evidencia (internacional)
- **Alternatives Considered**:
  1. Eliminar toda mención a Chile del título/abstract — pierde el anclaje empírico
  2. Agregar más estudios chilenos — puede no haber suficientes disponibles
- **Selected Approach**: Reformular como revisión internacional con foco interpretativo en el corredor Chile, distinguiendo evidencia directa de extrapolada
- **Rationale**: Permite mantener la relevancia del contexto chileno sin prometer lo que la evidencia no sustenta
- **Trade-offs**: El título puede perder especificidad, pero gana honestidad epistemológica
- **Follow-up**: Buscar estudios adicionales sobre migrantes en Chile para fortalecer la evidencia directa

### Decision: Lenguaje epistemológico cauteloso
- **Context**: El paper formula una "hipótesis" y luego la "confirma", lo cual es inapropiado para una revisión de literatura
- **Selected Approach**: Reformular como pregunta de investigación y usar lenguaje de síntesis ("la evidencia sugiere", "los hallazgos son consistentes con")
- **Rationale**: Una revisión de literatura no confirma hipótesis; sintetiza evidencia
- **Trade-offs**: Ninguno significativo; es una corrección epistemológica necesaria

## Risks & Mitigations
- Los testimonios pueden ser de estudio propio no publicado → consultar a autores; si es así, citar como "datos preliminares de investigación en curso"
- Referencias pendientes de verificación pueden no existir → buscar en CrossRef/Semantic Scholar y reemplazar si no se encuentran
- Agregar análisis bibliométrico puede exceder límite de palabras → usar tablas compactas y mover detalle a material suplementario
- La búsqueda de fuentes académicas alternativas a NPR puede no encontrar equivalentes exactos → buscar estudios sobre uso de Facebook por migrantes para información de rutas (existen en la literatura)

## References
- Page, M.J. et al. (2021). The PRISMA 2020 statement. BMJ, 372:n71. DOI: 10.1136/bmj.n71
- Tricco, A.C. et al. (2018). PRISMA Extension for Scoping Reviews (PRISMA-ScR). Annals of Internal Medicine, 169(7), 467-473.
- REIS Normas para autores: https://reis.cis.es/REIS/jsp/REIS.jsp?opcion=revistas&numero=normas
