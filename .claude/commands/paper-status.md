# /paper:status — Estado del paper

Muestra el estado de progreso del paper científico.

## Uso
```
/paper:status
```

## Instrucciones

Eres un monitor de progreso de paper científico. Lee todos los archivos del proyecto y genera un reporte de estado.

### Proceso

1. **Lee `paper/metadata.yaml`** para obtener:
   - Título provisional
   - Revista objetivo
   - Límites de palabras por sección
   - Estado actual

2. **Para cada sección en `paper/sections/`**:
   - Cuenta palabras actuales (excluye headers `#` y comments `<!-- -->`)
   - Calcula % completitud vs target
   - Detecta estado: `empty` / `draft` / `complete`
   - Cuenta citaciones `[N]` o `\cite{}` presentes

3. **Analiza `references/references.bib`**:
   - Cuenta total de entradas
   - Cuenta entradas con DOI
   - Identifica entradas sin campos críticos

4. **Verifica validaciones pendientes**:
   - Lee `.kiro/specs/` para ver tasks completadas vs pendientes
   - Chequea claims sin citar (oraciones sin referencia)

5. **Genera el reporte de estado**:

```
╔══════════════════════════════════════════════════════════╗
║         ESTADO DEL PAPER — <fecha>                      ║
║  Título: <título provisional>                           ║
║  Revista: <nombre>           Estado: <DRAFT/IN PROGRESS>║
╠══════════════════════════════════════════════════════════╣
║ SECCIONES                                               ║
╠══════════════════════════════════════════════════════════╣
║ Abstract        [████░░░░░░]  150/250 palabras   60%   ║
║ Introduction    [██░░░░░░░░]  200/800 palabras   25%   ║
║ Related Work    [░░░░░░░░░░]    0/600 palabras    0%   ║
║ Methodology     [░░░░░░░░░░]    0/700 palabras    0%   ║
║ Results         [░░░░░░░░░░]    0/600 palabras    0%   ║
║ Discussion      [░░░░░░░░░░]    0/500 palabras    0%   ║
║ Conclusion      [░░░░░░░░░░]    0/300 palabras    0%   ║
╠══════════════════════════════════════════════════════════╣
║ TOTAL           [█░░░░░░░░░]  350/3750 palabras    9%  ║
╠══════════════════════════════════════════════════════════╣
║ REFERENCIAS                                             ║
║  Entradas en .bib: X   Con DOI: Y   Sin campos: Z      ║
║  Claims citadas: A%   Claims sin citar estimadas: B    ║
╠══════════════════════════════════════════════════════════╣
║ VALIDACIONES                                            ║
║  [PASS] Estructura de revista                           ║
║  [WARN] X claims sin citación detectadas               ║
║  [FAIL] Y referencias sin DOI                          ║
╠══════════════════════════════════════════════════════════╣
║ PRÓXIMOS PASOS                                          ║
║  1. Completar sección: Related Work (prioridad alta)   ║
║  2. Citar X claims en Introduction                     ║
║  3. Verificar DOIs de Y referencias                    ║
╚══════════════════════════════════════════════════════════╝
```

6. **Si el paper está en estado temprano** (< 20% completitud):
   - Sugiere ejecutar `/paper:outline` para refinar el outline
   - Recomienda empezar por la sección más estructurada (Methodology)

7. **Si hay validaciones fallando**:
   - Lista las acciones correctivas con los comandos exactos a usar

### Cálculo de % de claims citadas

Una "claim" es cualquier oración que:
- Hace una afirmación factual sobre el mundo
- Compara métodos o resultados
- Cita estadísticas o números específicos
- Describe trabajo previo

Una claim está "citada" si termina con o contiene `[N]`, `\cite{}`, `[@key]`, etc.

Estima el % como: (oraciones con citación) / (oraciones que son claims) × 100
