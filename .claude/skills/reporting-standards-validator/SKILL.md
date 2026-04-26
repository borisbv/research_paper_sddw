---
name: reporting-standards-validator
description: Verificación de cumplimiento de guías internacionales de reporte (PRISMA, CONSORT, STROBE). Asegura que el manuscrito contenga todos los elementos obligatorios según el tipo de estudio.
---

# Reporting Standards Validator

Valida que el paper cumpla con los estándares metodológicos requeridos por las revistas.

## Estándares Soportados

- **PRISMA**: Systematic reviews and meta-analyses.
- **CONSORT**: Randomized controlled trials.
- **STROBE**: Observational studies (cohort, case-control, cross-sectional).

## Uso

1.  Identificar el tipo de estudio.
2.  Comparar el `outline.md` y las secciones en `paper/sections/` con la checklist en `references/checklists.md`.
3.  Generar un reporte de cumplimiento con `scripts/validate_standards.py`.

## Recursos

- `references/checklists.md`: Checklists oficiales simplificadas.
- `scripts/validate_standards.py`: Script de escaneo de texto para keywords obligatorias.