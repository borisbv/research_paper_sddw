#!/usr/bin/env python3
"""
validate-metadata.py — Valida paper/metadata.yaml contra el JSON Schema.
Uso: python scripts/validate-metadata.py
"""

import json
import sys
from pathlib import Path

import yaml

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "paper-metadata.schema.json"
METADATA_PATH = Path(__file__).parent.parent / "paper" / "metadata.yaml"


def validate_metadata(base_path: Path) -> tuple[bool, list[str]]:
    errors = []
    metadata_file = base_path / "paper" / "metadata.yaml"
    schema_file = base_path / "schemas" / "paper-metadata.schema.json"

    if not metadata_file.exists():
        print("[WARN] paper/metadata.yaml no encontrado — skip")
        return True, []

    if not schema_file.exists():
        errors.append("FAIL: schemas/paper-metadata.schema.json no encontrado")
        print(f"[FAIL] Metadata: schema no encontrado")
        return False, errors

    # Cargar metadata
    with open(metadata_file, encoding='utf-8') as f:
        metadata = yaml.safe_load(f)

    if not metadata:
        errors.append("FAIL: paper/metadata.yaml está vacío")
        print("[FAIL] Metadata: archivo vacío")
        return False, errors

    # Cargar schema
    with open(schema_file, encoding='utf-8') as f:
        schema = json.load(f)

    if not HAS_JSONSCHEMA:
        # Validación básica sin jsonschema
        print("[WARN] Metadata: jsonschema no instalado — validación básica")
        required = schema.get("required", [])
        missing = [f for f in required if f not in metadata]
        if missing:
            errors.append(f"FAIL: Campos requeridos faltantes: {', '.join(missing)}")
            print(f"[FAIL] Metadata: faltan {', '.join(missing)}")
            return False, errors
        print(f"[PASS] Metadata: {len(required)} campos requeridos presentes (validación básica)")
        return True, []

    # Validación completa con jsonschema
    validator = jsonschema.Draft7Validator(schema)
    validation_errors = list(validator.iter_errors(metadata))

    if validation_errors:
        for err in validation_errors:
            path = ".".join(str(p) for p in err.absolute_path) if err.absolute_path else "(raíz)"
            errors.append(f"FAIL: {path}: {err.message}")

        print(f"[FAIL] Metadata: {len(validation_errors)} error(es) de validación")
        for e in errors[:5]:
            print(f"  - {e}")
        if len(errors) > 5:
            print(f"  - ... y {len(errors) - 5} mas")
        return False, errors

    # Contar campos validados
    field_count = len(metadata.keys())
    print(f"[PASS] Metadata: {field_count} campos validados contra schema")
    return True, []


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_metadata(base)
    sys.exit(0 if ok else 1)
