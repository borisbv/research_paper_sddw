#!/usr/bin/env python3
"""
Script de validación automática del paper.
Verifica requisitos hard: conteo de palabras, formato de citas,
guiones, viñetas, mención de revista, coherencia terminológica,
y consistencia citas-referencias.
"""

import re
import sys
import os
from pathlib import Path
from collections import Counter

# Configuración
PAPER_DIR = Path(__file__).parent.parent / "paper"
REFERENCES_FILE = Path(__file__).parent.parent / "references" / "references.bib"
GLOSSARY_FILE = PAPER_DIR / "glosario.md"

# Presupuesto de palabras por sección (±5%)
WORD_BUDGET = {
    "02_introduction.md": (950, 1050),
    "03_marco_teorico.md": (1710, 1890),
    "04_methodology.md": (570, 630),
    "05_results_discussion.md": (2660, 2940),
    "06_conclusions.md": (760, 840),
}

TOTAL_MAX_WORDS = 9000

# Secciones argumentativas del cuerpo (donde no debe haber viñetas)
BODY_SECTIONS = [
    "02_introduction.md",
    "03_marco_teorico.md",
    "04_methodology.md",
    "05_results_discussion.md",
    "06_conclusions.md",
]

# Nombres de la revista que no deben aparecer
JOURNAL_NAMES = [
    "REIS",
    "Revista Española de Investigaciones Sociológicas",
    "Centro de Investigaciones Sociológicas",
]


def count_words(text):
    """Cuenta palabras en un texto, excluyendo encabezados markdown."""
    lines = text.split("\n")
    content_lines = [l for l in lines if not l.strip().startswith("#")]
    content = " ".join(content_lines)
    words = re.findall(r"\b\w+\b", content)
    return len(words)


def check_word_counts():
    """Verifica conteo de palabras total y por sección."""
    errors = []
    warnings = []
    total_words = 0

    for filename, (min_w, max_w) in WORD_BUDGET.items():
        filepath = PAPER_DIR / filename
        if not filepath.exists():
            errors.append(f"FALTA: {filename} no existe")
            continue
        text = filepath.read_text(encoding="utf-8")
        wc = count_words(text)
        total_words += wc

        if wc < min_w:
            warnings.append(
                f"BAJO MINIMO: {filename} tiene {wc} palabras (mínimo: {min_w})"
            )
        elif wc > max_w:
            warnings.append(
                f"EXCEDE LIMITE: {filename} tiene {wc} palabras (máximo: {max_w})"
            )
        else:
            print(f"  OK: {filename} — {wc} palabras (rango: {min_w}-{max_w})")

    # Contar abstract
    abstract_file = PAPER_DIR / "01_abstract.md"
    if abstract_file.exists():
        total_words += count_words(abstract_file.read_text(encoding="utf-8"))

    if total_words > TOTAL_MAX_WORDS:
        errors.append(
            f"TOTAL EXCEDIDO: {total_words} palabras (máximo: {TOTAL_MAX_WORDS})"
        )
    else:
        print(f"  OK: Total — {total_words} palabras (máximo: {TOTAL_MAX_WORDS})")

    return errors, warnings


def check_citation_format():
    """Verifica que las citas sigan el formato (Apellido, año) o (Apellido, año: página)."""
    warnings = []
    # Patrón para citas parentéticas válidas
    valid_cite = re.compile(
        r"\([A-ZÁÉÍÓÚÑ][a-záéíóúñüA-ZÁÉÍÓÚÑ\s]+(?:et al\.)?,\s*(?:s\.f\.|(?:en\s)?[12]\d{3})(?::\s*\d+(?:-\d+)?)?\)"
    )
    # Patrón para detectar posibles citas mal formateadas
    suspect_cite = re.compile(r"\([A-Z][a-z]+\s+\d{4}\)")  # Sin coma

    for filename in BODY_SECTIONS:
        filepath = PAPER_DIR / filename
        if not filepath.exists():
            continue
        text = filepath.read_text(encoding="utf-8")
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            suspects = suspect_cite.findall(line)
            for s in suspects:
                if not valid_cite.search(s.replace(s, f"({s[1:-1].split()[0]}, {s[1:-1].split()[1]})")):
                    warnings.append(
                        f"CITA SIN COMA: {filename}:{i} — '{s}' (debe ser 'Apellido, año')"
                    )

    return warnings


def check_dashes():
    """Detecta guiones usados como separadores de ideas."""
    warnings = []
    # Guión largo como separador de ideas (con espacios alrededor)
    dash_pattern = re.compile(r"\s[—–-]\s(?!.*\bpágina\b)")

    for filename in BODY_SECTIONS:
        filepath = PAPER_DIR / filename
        if not filepath.exists():
            continue
        text = filepath.read_text(encoding="utf-8")
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            if line.strip().startswith("#"):
                continue
            matches = dash_pattern.findall(line)
            if matches:
                warnings.append(
                    f"GUION SEPARADOR: {filename}:{i} — posible guión como separador de ideas"
                )

    return warnings


def check_bullet_lists():
    """Detecta listas con viñetas en secciones argumentativas."""
    warnings = []
    bullet_pattern = re.compile(r"^\s*[-*+]\s+\S")

    for filename in BODY_SECTIONS:
        filepath = PAPER_DIR / filename
        if not filepath.exists():
            continue
        text = filepath.read_text(encoding="utf-8")
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            if bullet_pattern.match(line):
                warnings.append(
                    f"VIÑETA EN CUERPO: {filename}:{i} — lista con viñetas en sección argumentativa"
                )

    return warnings


def check_journal_mention():
    """Verifica que no se mencione la revista de destino."""
    errors = []

    all_files = list(PAPER_DIR.glob("*.md"))
    for filepath in all_files:
        text = filepath.read_text(encoding="utf-8")
        for journal_name in JOURNAL_NAMES:
            if journal_name.lower() in text.lower():
                errors.append(
                    f"MENCION REVISTA: {filepath.name} contiene '{journal_name}'"
                )

    return errors


def check_glossary_consistency():
    """Verifica coherencia terminológica contra el glosario."""
    warnings = []

    if not GLOSSARY_FILE.exists():
        warnings.append("GLOSARIO: archivo glosario.md no encontrado")
        return warnings

    glossary_text = GLOSSARY_FILE.read_text(encoding="utf-8")
    # Extraer términos en negrita del glosario
    terms = re.findall(r"\*\*([^*]+):\*\*", glossary_text)

    # Verificar que cada término aparezca al menos una vez en el cuerpo
    for term in terms:
        term_lower = term.lower().strip()
        found = False
        for filename in BODY_SECTIONS:
            filepath = PAPER_DIR / filename
            if not filepath.exists():
                continue
            text = filepath.read_text(encoding="utf-8").lower()
            if term_lower in text:
                found = True
                break
        if not found:
            warnings.append(
                f"TERMINO NO USADO: '{term}' del glosario no aparece en el cuerpo del paper"
            )

    return warnings


def extract_citations_from_text():
    """Extrae todas las citas del texto (Apellido, año)."""
    citations = set()
    cite_pattern = re.compile(
        r"\(([A-ZÁÉÍÓÚÑ][a-záéíóúñüA-ZÁÉÍÓÚÑ\s]+(?:et al\.)?),\s*(?:en\s)?(\d{4}|s\.f\.)"
    )

    all_files = list(PAPER_DIR.glob("*.md"))
    for filepath in all_files:
        if filepath.name == "glosario.md":
            continue
        text = filepath.read_text(encoding="utf-8")
        matches = cite_pattern.findall(text)
        for author, year in matches:
            citations.add((author.strip(), year.strip()))

    return citations


def extract_bib_entries():
    """Extrae claves y autores/años del archivo .bib."""
    entries = {}
    if not REFERENCES_FILE.exists():
        return entries

    text = REFERENCES_FILE.read_text(encoding="utf-8")
    # Extraer bloques de entrada
    entry_pattern = re.compile(r"@\w+\{(\w+),")
    author_pattern = re.compile(r"author\s*=\s*\{([^}]+)\}", re.IGNORECASE)
    year_pattern = re.compile(r"year\s*=\s*\{(\d{4})\}", re.IGNORECASE)

    current_key = None
    current_block = []

    for line in text.split("\n"):
        entry_match = entry_pattern.match(line.strip())
        if entry_match:
            if current_key and current_block:
                block_text = "\n".join(current_block)
                a = author_pattern.search(block_text)
                y = year_pattern.search(block_text)
                entries[current_key] = {
                    "author": a.group(1) if a else "",
                    "year": y.group(1) if y else "",
                }
            current_key = entry_match.group(1)
            current_block = [line]
        elif current_key:
            current_block.append(line)

    # Última entrada
    if current_key and current_block:
        block_text = "\n".join(current_block)
        a = author_pattern.search(block_text)
        y = year_pattern.search(block_text)
        entries[current_key] = {
            "author": a.group(1) if a else "",
            "year": y.group(1) if y else "",
        }

    return entries


def check_citation_bib_consistency():
    """Verifica consistencia entre citas en texto y entradas en .bib."""
    warnings = []

    bib_entries = extract_bib_entries()
    text_citations = extract_citations_from_text()

    if not bib_entries:
        warnings.append(
            "REFERENCIAS: archivo .bib vacío o no encontrado"
        )
        return warnings

    # Extraer apellidos y años del .bib
    bib_authors_years = set()
    for key, info in bib_entries.items():
        if info["author"] and info["year"]:
            # Tomar primer apellido
            first_author = info["author"].split(" and ")[0].split(",")[0].strip()
            bib_authors_years.add((first_author, info["year"]))

    # Verificar que las citas en texto tengan entrada en .bib
    for author, year in text_citations:
        if year == "s.f.":
            continue
        # Buscar match aproximado
        found = False
        for bib_author, bib_year in bib_authors_years:
            if bib_author.lower() in author.lower() and bib_year == year:
                found = True
                break
        if not found:
            warnings.append(
                f"CITA SIN BIB: ({author}, {year}) no tiene entrada en references.bib"
            )

    return warnings


def main():
    print("=" * 60)
    print("VALIDACIÓN DEL PAPER")
    print("=" * 60)

    all_errors = []
    all_warnings = []

    print("\n1. CONTEO DE PALABRAS")
    print("-" * 40)
    errors, warnings = check_word_counts()
    all_errors.extend(errors)
    all_warnings.extend(warnings)

    print("\n2. FORMATO DE CITAS")
    print("-" * 40)
    warnings = check_citation_format()
    all_warnings.extend(warnings)
    if not warnings:
        print("  OK: No se detectaron citas mal formateadas")

    print("\n3. GUIONES COMO SEPARADORES")
    print("-" * 40)
    warnings = check_dashes()
    all_warnings.extend(warnings)
    if not warnings:
        print("  OK: No se detectaron guiones como separadores")

    print("\n4. VIÑETAS EN SECCIONES ARGUMENTATIVAS")
    print("-" * 40)
    warnings = check_bullet_lists()
    all_warnings.extend(warnings)
    if not warnings:
        print("  OK: No se detectaron viñetas en secciones argumentativas")

    print("\n5. MENCIÓN DE REVISTA")
    print("-" * 40)
    errors = check_journal_mention()
    all_errors.extend(errors)
    if not errors:
        print("  OK: No se menciona la revista de destino")

    print("\n6. COHERENCIA TERMINOLÓGICA")
    print("-" * 40)
    warnings = check_glossary_consistency()
    all_warnings.extend(warnings)
    if not warnings:
        print("  OK: Todos los términos del glosario aparecen en el cuerpo")

    print("\n7. CONSISTENCIA CITAS-REFERENCIAS")
    print("-" * 40)
    warnings = check_citation_bib_consistency()
    all_warnings.extend(warnings)
    if not warnings:
        print("  OK: Todas las citas tienen entrada en .bib")

    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)

    if all_errors:
        print(f"\n  ERRORES ({len(all_errors)}):")
        for e in all_errors:
            print(f"    [ERROR] {e}")

    if all_warnings:
        print(f"\n  ADVERTENCIAS ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"    [WARN] {w}")

    if not all_errors and not all_warnings:
        print("\n  [PASS] Todas las validaciones pasaron correctamente")

    # Exit code
    if all_errors:
        sys.exit(1)
    elif all_warnings:
        sys.exit(0)  # Warnings no bloquean
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
