#!/usr/bin/env python3
"""
validate-word-count.py — Verifica límites de palabras por sección.
Uso: python scripts/validate-word-count.py
"""

import re
import sys
import yaml
from pathlib import Path

DEFAULT_WORD_LIMITS = {
    "abstract": {"min": 150, "max": 300},
    "introduction": {"min": 400, "max": 1000},
    "related-work": {"min": 400, "max": 800},
    "methodology": {"min": 500, "max": 1000},
    "results": {"min": 400, "max": 800},
    "discussion": {"min": 300, "max": 700},
    "conclusion": {"min": 150, "max": 400},
}

JOURNAL_WORD_LIMITS = {
    "Nature": {
        "abstract": {"min": 100, "max": 150},
        "total": {"max": 3000},
    },
    "Nature Medicine": {
        "abstract": {"min": 150, "max": 200},
        "total": {"max": 4000},
    },
    "PLOS ONE": {
        "abstract": {"min": 200, "max": 300},
        "total": {"max": 10000},
    },
    "IEEE": {
        "abstract": {"min": 150, "max": 250},
        "total": {"max": 8000},
    },
}


def count_words(text: str) -> int:
    """Count words excluding markdown headers and HTML comments."""
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remove markdown headers
    text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
    # Remove markdown formatting
    text = re.sub(r'[*_`#\[\]]', '', text)
    # Count words
    words = text.split()
    return len(words)


def load_metadata(base_path: Path) -> dict:
    metadata_file = base_path / "paper" / "metadata.yaml"
    if not metadata_file.exists():
        return {}
    with open(metadata_file) as f:
        return yaml.safe_load(f) or {}


def validate_word_counts(base_path: Path) -> tuple[bool, list[str]]:
    errors = []
    metadata = load_metadata(base_path)
    journal = metadata.get("journal", "default")
    custom_limits = metadata.get("word_limits", {})

    journal_limits = JOURNAL_WORD_LIMITS.get(journal, {})
    sections_dir = base_path / "paper" / "sections"

    if not sections_dir.exists():
        errors.append("FAIL: paper/sections/ no encontrado")
        return False, errors

    total_words = 0
    section_results = []

    for section_file in sorted(sections_dir.glob("*.md")):
        section_name = section_file.stem
        content = section_file.read_text()
        word_count = count_words(content)
        total_words += word_count

        # Determine limits
        if section_name in custom_limits:
            limits = custom_limits[section_name]
        elif section_name in journal_limits:
            limits = journal_limits[section_name]
        else:
            limits = DEFAULT_WORD_LIMITS.get(section_name, {"min": 100, "max": 1500})

        min_w = limits.get("min", 0)
        max_w = limits.get("max", float("inf"))

        if word_count == 0:
            status = "EMPTY"
        elif word_count < min_w * 0.5:
            status = "LOW"
            errors.append(f"WARN: {section_name} muy corta ({word_count}/{min_w} palabras mínimo)")
        elif word_count > max_w * 1.2:
            status = "HIGH"
            errors.append(f"WARN: {section_name} excede límite ({word_count}/{max_w} palabras máximo)")
        else:
            status = "OK"

        section_results.append((section_name, word_count, min_w, max_w, status))

    # Check total
    total_max = journal_limits.get("total", {}).get("max", float("inf"))
    total_custom = custom_limits.get("total", {})
    if isinstance(total_custom, dict):
        total_max = total_custom.get("max", total_max)

    total_status = "OK"
    if total_words > total_max:
        total_status = "HIGH"
        errors.append(f"FAIL: Total excede límite de revista ({total_words}/{total_max} palabras)")

    passed = not any(e.startswith("FAIL") for e in errors)
    status_label = "PASS" if passed else "FAIL"
    print(f"[{status_label}] Conteo de palabras: {total_words} total ({total_status})")
    for name, count, min_w, max_w, st in section_results:
        target = f"{min_w}-{max_w}" if max_w != float("inf") else f"{min_w}+"
        print(f"  {name:<20} {count:>5} palabras  [target: {target}]  [{st}]")
    for e in errors:
        print(f"  → {e}")

    return passed, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_word_counts(base)
    sys.exit(0 if ok else 1)
