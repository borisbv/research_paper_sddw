# Command: research-init

Este comando es OBLIGATORIO para comenzar cualquier fase de investigación. Define el target del motor de generación científica.

## Workflow

1.  **Selección Mandatoria**: Preguntar al usuario si desea trabajar en un `paper` o un `book`.
2.  **Ejecución**: Ejecutar `python scripts/research-init.py [target]`.
3.  **Detección de Continuidad**: Si la carpeta existe, el script reportará que se está iterando un proyecto existente.
4.  **Configuración de Contexto**: El motor ajustará automáticamente los flags `--dir [target]` para el resto de las validaciones en la sesión.

## Uso
`/kiro:research-init`