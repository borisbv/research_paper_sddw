#!/usr/bin/env python3
"""
tidy-bib.py — Normaliza references/references.bib.
Ordena entradas, normaliza campos, detecta duplicados.
Uso: python scripts/tidy-bib.py [--check] [--dry-run]
"""

import argparse
import re
import sys
from pathlib import Path


# Orden preferido de campos (el resto va alfabéticamente después)
FIELD_ORDER = [
    "author", "title", "journal", "booktitle", "year", "date",
    "volume", "number", "pages", "edition", "publisher", "address",
    "editor", "chapter", "series", "doi", "url", "isbn", "issn",
    "abstract", "keywords", "note",
]


def parse_bib_file(text: str) -> tuple[list[dict], list[str]]:
    """Parsea un archivo .bib respetando llaves anidadas.

    Retorna (entries, preamble_lines) donde entries es lista de dicts con:
      type, key, fields (lista de (name, value)), raw_comments (líneas pre-entry)
    """
    entries = []
    preamble_lines = []
    pos = 0
    length = len(text)
    current_comments = []

    while pos < length:
        # Buscar inicio de entrada @type{
        match = re.search(r'@(\w+)\s*\{', text[pos:])
        if not match:
            # Resto es comentario/whitespace
            rest = text[pos:].strip()
            if rest:
                current_comments.append(rest)
            break

        # Capturar comentarios entre entradas
        before = text[pos:pos + match.start()].strip()
        if before:
            current_comments.extend(before.splitlines())

        entry_type = match.group(1).lower()
        brace_start = pos + match.start() + match.end() - match.start()

        # Manejar @preamble, @string, @comment
        if entry_type in ("preamble", "string", "comment"):
            depth = 1
            i = brace_start
            while i < length and depth > 0:
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                i += 1
            raw = text[pos + match.start():i]
            preamble_lines.append(raw)
            pos = i
            current_comments = []
            continue

        # Extraer key (hasta la primera coma)
        key_end = text.find(',', brace_start)
        if key_end == -1:
            pos = brace_start
            continue

        key = text[brace_start:key_end].strip()

        # Extraer body respetando llaves anidadas
        depth = 1
        i = key_end + 1
        while i < length and depth > 0:
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
            i += 1

        body = text[key_end + 1:i - 1]

        # Parsear campos del body
        fields = parse_fields(body)

        entries.append({
            "type": entry_type,
            "key": key,
            "fields": fields,
            "comments": current_comments[:],
        })
        current_comments = []
        pos = i

    return entries, preamble_lines


def parse_fields(body: str) -> list[tuple[str, str]]:
    """Extrae campos (name, value) de un body BibTeX."""
    fields = []
    pos = 0
    length = len(body)

    while pos < length:
        # Buscar nombre de campo
        match = re.search(r'(\w+)\s*=\s*', body[pos:])
        if not match:
            break

        field_name = match.group(1).lower()
        value_start = pos + match.end()

        # Extraer valor (puede ser {..}, "..", o número)
        value, end_pos = extract_field_value(body, value_start)
        if value is not None:
            fields.append((field_name, value))
            pos = end_pos
        else:
            pos = value_start + 1

    return fields


def extract_field_value(text: str, start: int) -> tuple[str | None, int]:
    """Extrae un valor de campo BibTeX desde la posición dada."""
    length = len(text)
    i = start

    # Saltar whitespace
    while i < length and text[i] in ' \t\n\r':
        i += 1

    if i >= length:
        return None, i

    if text[i] == '{':
        # Valor delimitado por llaves
        depth = 1
        j = i + 1
        while j < length and depth > 0:
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
            j += 1
        value = text[i + 1:j - 1]
        # Avanzar pasado posible coma
        while j < length and text[j] in ' \t\n\r,':
            j += 1
        return value, j

    elif text[i] == '"':
        # Valor delimitado por comillas
        j = i + 1
        while j < length and text[j] != '"':
            if text[j] == '\\':
                j += 1  # Saltar carácter escapado
            j += 1
        value = text[i + 1:j]
        j += 1
        while j < length and text[j] in ' \t\n\r,':
            j += 1
        return value, j

    else:
        # Valor numérico o macro (sin delimitador)
        j = i
        while j < length and text[j] not in ',}\n':
            j += 1
        value = text[i:j].strip()
        if j < length and text[j] == ',':
            j += 1
        while j < length and text[j] in ' \t\n\r':
            j += 1
        return value, j


def sort_fields(fields: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Ordena campos según FIELD_ORDER, resto alfabéticamente."""
    order_map = {name: idx for idx, name in enumerate(FIELD_ORDER)}
    max_order = len(FIELD_ORDER)

    return sorted(fields, key=lambda f: (order_map.get(f[0], max_order), f[0]))


def format_entry(entry: dict) -> str:
    """Formatea una entrada BibTeX normalizada."""
    lines = []

    # Comentarios previos a la entrada
    for comment in entry.get("comments", []):
        if comment.strip():
            lines.append(comment)

    # Header
    lines.append(f"@{entry['type']}{{{entry['key']},")

    # Campos ordenados
    sorted_fields = sort_fields(entry["fields"])
    for name, value in sorted_fields:
        # Normalizar: siempre usar llaves (no comillas)
        lines.append(f"  {name} = {{{value}}},")

    lines.append("}")
    return "\n".join(lines)


def format_bib(entries: list[dict], preamble_lines: list[str]) -> str:
    """Genera el archivo .bib completo normalizado."""
    parts = []

    # Preamble/strings primero
    for p in preamble_lines:
        parts.append(p)

    if preamble_lines:
        parts.append("")

    # Entradas ordenadas por key
    sorted_entries = sorted(entries, key=lambda e: e["key"].lower())
    for entry in sorted_entries:
        parts.append(format_entry(entry))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def find_duplicates(entries: list[dict]) -> list[str]:
    """Detecta keys duplicados."""
    seen = {}
    duplicates = []
    for entry in entries:
        key = entry["key"]
        if key in seen:
            duplicates.append(key)
        else:
            seen[key] = True
    return duplicates


def tidy_bib(base_path: Path, check_only: bool = False, dry_run: bool = False) -> tuple[bool, list[str]]:
    errors = []
    bib_file = base_path / "references" / "references.bib"

    if not bib_file.exists():
        print("[WARN] references/references.bib no encontrado — skip")
        return True, []

    original = bib_file.read_text(encoding="utf-8")

    if not original.strip():
        print("[PASS] BibTeX tidy: archivo vacío")
        return True, []

    entries, preamble = parse_bib_file(original)

    if not entries:
        print("[PASS] BibTeX tidy: sin entradas")
        return True, []

    # Detectar duplicados
    dupes = find_duplicates(entries)
    if dupes:
        errors.append(f"WARN: Keys duplicados: {', '.join(dupes[:5])}")

    # Generar salida normalizada
    normalized = format_bib(entries, preamble)

    # Comparar
    is_tidy = original == normalized
    diff_lines = 0
    if not is_tidy:
        orig_lines = original.splitlines()
        norm_lines = normalized.splitlines()
        diff_lines = abs(len(orig_lines) - len(norm_lines))
        for a, b in zip(orig_lines, norm_lines):
            if a != b:
                diff_lines += 1

    if check_only:
        if is_tidy:
            print(f"[PASS] BibTeX tidy: {len(entries)} entradas, archivo normalizado")
            return True, errors
        else:
            errors.append(f"FAIL: references.bib no está normalizado (~{diff_lines} líneas difieren)")
            errors.append("  Ejecute: python scripts/tidy-bib.py")
            print(f"[FAIL] BibTeX tidy: {len(entries)} entradas, archivo requiere normalización")
            for e in errors:
                print(f"  - {e}")
            return False, errors

    if dry_run:
        print(normalized, end="")
        return True, errors

    if not is_tidy:
        bib_file.write_text(normalized, encoding="utf-8")
        print(f"[OK] BibTeX tidy: {len(entries)} entradas normalizadas (~{diff_lines} líneas cambiadas)")
    else:
        print(f"[OK] BibTeX tidy: {len(entries)} entradas, ya normalizado")

    for e in errors:
        print(f"  - {e}")

    return True, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normaliza references/references.bib")
    parser.add_argument("--check", action="store_true",
                        help="Solo verificar, exit 1 si el archivo cambiaría")
    parser.add_argument("--dry-run", action="store_true",
                        help="Imprimir resultado normalizado a stdout sin modificar")
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    ok, _ = tidy_bib(base, check_only=args.check, dry_run=args.dry_run)
    sys.exit(0 if ok else 1)
