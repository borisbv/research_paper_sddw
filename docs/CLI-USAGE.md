# 🛠️ Manual de Uso del Research Manager CLI

El `scripts/manager.py` es la interfaz central del motor.

## Inicialización
Para comenzar una nueva sesión de investigación o crear un nuevo proyecto:
```bash
python scripts/manager.py init paper
# o para un libro
python scripts/manager.py init book
```
*Si la carpeta ya existe, el script detectará la continuidad automáticamente.*

## Validación Completa
Realiza un escaneo exhaustivo de la integridad de la investigación:
```bash
python scripts/manager.py validate --dir paper
```
**Valida:**
- Estructura de carpetas y archivos base.
- Sincronización de citas con el archivo `.bib`.
- Existencia y citación de figuras.
- Conteo de palabras por sección y total.

## Renderizado de Manuscrito
Genera el PDF o Docx final:
```bash
python scripts/manager.py render --dir paper --format pdf
```
*Requiere que Quarto esté instalado en el sistema.*

## Sincronización de Bibliografía
Sincroniza referencias desde la nube (Zotero) hacia el archivo local:
```bash
python scripts/manager.py sync --dir paper
```