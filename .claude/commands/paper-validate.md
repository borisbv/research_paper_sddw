# /paper:validate — Validar el paper científico

Ejecuta todas las validaciones automáticas (hard specs) del paper.

## Uso
```
/paper:validate
```

## Instrucciones

Eres un validador de papers científicos. Ejecuta estas validaciones en secuencia y reporta resultados:

### 1. Validación de Estructura

Lee `paper/metadata.yaml` para obtener la revista objetivo. Luego verifica:
- Que existan los archivos de secciones requeridos en `paper/sections/`
- Que ninguna sección esté completamente vacía (solo header/comments)
- Que el outline en `paper/outline.md` esté actualizado

**Output esperado:** `[PASS/FAIL] Estructura: X/Y secciones completas`

### 2. Validación de Citaciones

Para cada archivo en `paper/sections/`:
- Busca patrones de citación: `[1]`, `[Smith, 2023]`, `\cite{key}`, `[@key]`
- Cuenta claims sin citar (oraciones que hacen afirmaciones sin citación)
- Verifica que cada clave citada exista en `references/references.bib`

**Output esperado:** `[PASS/FAIL] Citaciones: X refs citadas, Y huérfanas, Z claims sin citar`

### 3. Validación de Formato de Citas

Lee el `citation_style` de `paper/metadata.yaml`. Verifica que el formato en el texto y en el .bib sea consistente con ese estilo.

**Output esperado:** `[PASS/FAIL] Formato de citas: estilo <nombre>`

### 4. Validación de Conteo de Palabras

Lee los límites de `paper/metadata.yaml`. Para cada sección:
- Cuenta palabras actuales (excluyendo headers y comments)
- Compara con target mínimo y máximo
- Alerta si está por debajo del 50% del target o por encima del 120%

**Output esperado:**
```
[PASS/FAIL] Conteo de palabras:
  Abstract: XXX/YYY palabras [OK/LOW/HIGH]
  Introduction: XXX/YYY palabras [OK/LOW/HIGH]
  ...
```

### 5. Validación de Referencias en .bib

Lee `references/references.bib` y verifica:
- Que cada entrada tenga los campos obligatorios (title, author, year)
- Que las entradas citadas en el texto no tengan campos vacíos críticos
- Que haya DOI o URL cuando sea posible

**Output esperado:** `[PASS/FAIL] Referencias .bib: X entradas, Y con DOI, Z con campos faltantes`

### 6. Validación de Figuras y Tablas

Busca referencias a figuras (`Figure X`, `Fig. X`, `Table X`) en el texto. Verifica:
- Que los archivos de figuras existan en `figures/`
- Que no haya figuras en `figures/` sin referencias en el texto

**Output esperado:** `[PASS/FAIL] Figuras/Tablas: X referenciadas, Y archivos encontrados`

### Reporte Final

Genera un reporte consolidado:
```
========================================
VALIDACIÓN DEL PAPER — <fecha>
Revista: <nombre>
========================================
[PASS] Estructura: ...
[FAIL] Citaciones: ...
[PASS] Formato de citas: ...
[WARN] Conteo de palabras: ...
[PASS] Referencias .bib: ...
[PASS] Figuras/Tablas: ...
========================================
RESULTADO: X/6 checks pasados
BLOQUEANTES: Y items requieren atención
========================================
```

Si hay FAILs, lista las acciones concretas requeridas para resolverlos.
