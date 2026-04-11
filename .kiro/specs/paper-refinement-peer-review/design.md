# Technical Design: Peer Review Refinement

## Modification Scope (By Section)

| Section | Planned Changes |
| :--- | :--- |
| **Metodología** | - Sustituir "UTEM" y "UW-Milwaukee" por descriptores genéricos.<br>- Añadir párrafo sobre **Análisis Temático Reflexivo** (Braun & Clarke) y uso de **Atlas.ti**.<br>- Describir el proceso de codificación y triangulación. |
| **Resultados** | - Asegurar que las citas de participantes mantengan el formato anónimo independiente.<br>- Verificar consistencia de negritas en categorías. |
| **Discusión** | - Integrar mención al **Decreto 181 (PNME 2024-2025)**.<br>- Analizar el vacío en "infraestructura de acogida" y cómo la "Casa de paso" operativiza el eje de habitabilidad.<br>- Discutir el empadronamiento biométrico como barrera vs. regularización humanitaria. |
| **Global** | - Unificar citas: formato narrativo "Autor (Year)" y parentético `\cite{key}`.<br>- Eliminar archivo `paper/sections/related-work.md` para limpiar estructura (integrado en Intro). |

## Interface and Convention Rules
1. **Anonymization Rule:** No se permite el uso de siglas institucionales (UTEM, UWM) ni nombres de autores en el cuerpo del texto.
2. **Citation Convention:** Seguir APA 7th Edition. Si la frase inicia con el autor, usar formato manual `Autor (Year)`. Si es al final, usar `\cite{key}`.
3. **Density Rule:** Mantener párrafos de 8-15 líneas para preservar la fluidez académica.

## Technical Risks and Mitigations
- **Script Failure:** Los scripts de validación pueden fallar por codificación (ya resuelto con `utf-8`). Se mantendrá la vigilancia sobre Unicode.
- **Reference Desync:** La modificación de citas manuales ("Autor, Year") podría desvincularse del `.bib`. Se ejecutará `validate-citations.py` tras cada cambio mayor.

## Final Acceptance Workflow
1. Apply text refinements (Implementation).
2. Run `validate-prose.py` (Style check).
3. Run `validate-citations.py` (Bib consistency).
4. Run `validate-word-count.py` (Length check).
5. Generate updated `paper-status` report.
