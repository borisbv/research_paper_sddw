#!/usr/bin/env python3
"""
validate-structure.py — Valida que la estructura del paper cumpla el template de la revista.
Uso: python scripts/validate-structure.py
"""

import sys
import yaml
from pathlib import Path

REQUIRED_SECTIONS = [
    "abstract",
    "introduction",
    "related-work",
    "methodology",
    "results",
    "discussion",
    "conclusion",
]

JOURNAL_REQUIRED_SECTIONS = {
    "Nature": ["abstract", "introduction", "results", "discussion"],
    "Nature Medicine": ["abstract", "introduction", "results", "discussion"],
    "Science": ["abstract", "introduction", "results", "discussion"],
    "PLOS ONE": ["abstract", "introduction", "methodology", "results", "discussion"],
    "IEEE": ["abstract", "introduction", "methodology", "results", "discussion", "conclusion"],
    "ACM": ["abstract", "introduction", "methodology", "results", "discussion", "conclusion"],
    # IMRaD adaptado con marco teórico explícito (estructura RES / revistas latinoamericanas)
    "Revista de Estudios Sociales": [
        "abstract", "introduction", "marco-teorico",
        "methodology", "results", "discussion", "conclusion",
    ],
}


def load_metadata(base_path: Path) -> dict:
    metadata_file = base_path / "paper" / "metadata.yaml"
    if not metadata_file.exists():
        print("[WARN] No se encontró paper/metadata.yaml — usando estructura IMRaD por defecto")
        return {}
    with open(metadata_file) as f:
        return yaml.safe_load(f) or {}


def validate_structure(base_path: Path) -> tuple[bool, list[str]]:
    errors = []
    metadata = load_metadata(base_path)
    journal = metadata.get("journal", "default")

    required = JOURNAL_REQUIRED_SECTIONS.get(journal, REQUIRED_SECTIONS)
    sections_dir = base_path / "paper" / "sections"

    if not sections_dir.exists():
        errors.append("FAIL: Directorio paper/sections/ no encontrado")
        return False, errors

    found_sections = {f.stem for f in sections_dir.glob("*.md")}
    missing = [s for s in required if s not in found_sections]
    empty = []

    for section in required:
        section_file = sections_dir / f"{section}.md"
        if section_file.exists():
            content = section_file.read_text()
            # Strip headers and comments
            lines = [
                l for l in content.splitlines()
                if l.strip()
                and not l.strip().startswith("#")
                and not l.strip().startswith("<!--")
                and not l.strip().startswith("-->")
            ]
            if not lines:
                empty.append(section)

    if missing:
        errors.append(f"FAIL: Secciones faltantes: {', '.join(missing)}")
    if empty:
        errors.append(f"WARN: Secciones vacías: {', '.join(empty)}")

    outline = base_path / "paper" / "outline.md"
    if not outline.exists():
        errors.append("WARN: paper/outline.md no encontrado")

    refs = base_path / "references" / "references.bib"
    if not refs.exists():
        errors.append("WARN: references/references.bib no encontrado")

    passed = not any(e.startswith("FAIL") for e in errors)
    total = len(required)
    complete = total - len(missing) - len(empty)

    if passed:
        print(f"[PASS] Estructura: {complete}/{total} secciones completas para '{journal}'")
    else:
        print(f"[FAIL] Estructura: {complete}/{total} secciones completas para '{journal}'")
    for e in errors:
        print(f"  - {e}")

    return passed, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_structure(base)
    sys.exit(0 if ok else 1)
