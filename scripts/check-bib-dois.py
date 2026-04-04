#!/usr/bin/env python3
"""
check-bib-dois.py — Verifica DOIs en references.bib contra CrossRef API.
Incluye cross-check de metadatos (titulo, autor, anio) para detectar citas incorrectas.
Uso: python scripts/check-bib-dois.py [--offline] [--no-cross-check]
"""

import difflib
import json
import re
import sys
import time
import unicodedata
import argparse
from pathlib import Path
from urllib.parse import quote

try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


DOI_PATTERN = re.compile(r'\bdoi\s*=\s*[{"]([^}"]+)[}"]', re.IGNORECASE)
DOI_FORMAT_PATTERN = re.compile(r'^10\.\d{4,}/\S+$')
BIB_ENTRY_PATTERN = re.compile(r'@(\w+)\{([^,\s]+),([^@]*)', re.DOTALL)
FIELD_PATTERN = re.compile(r'\b(title|author|year)\s*=\s*[{"](.+?)[}"]', re.IGNORECASE | re.DOTALL)
CROSSREF_API = "https://api.crossref.org/works/{doi}"


def clean_doi(doi: str) -> str:
    """Limpia un DOI removiendo prefijos URL."""
    doi = doi.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "http://dx.doi.org/", "https://dx.doi.org/"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):]
    return doi


def check_doi_format(doi: str) -> bool:
    """Verifica si el DOI tiene formato valido."""
    return bool(DOI_FORMAT_PATTERN.match(clean_doi(doi)))


def normalize_text(s: str) -> str:
    """Normaliza texto para comparacion: minusculas, sin acentos, sin puntuacion extra."""
    # Descomponer caracteres Unicode y remover marcas de acento
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    # Minusculas, colapsar whitespace, remover puntuacion comun
    s = s.lower()
    s = re.sub(r'[{}\\"\']', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def extract_bib_field(body: str, field_name: str) -> str | None:
    """Extrae el valor de un campo BibTeX del body de una entrada."""
    pattern = re.compile(
        rf'\b{field_name}\s*=\s*[{{"](.+?)[}}"]\s*[,}}]',
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(body)
    return match.group(1).strip() if match else None


def extract_first_author_lastname(author_str: str) -> str | None:
    """Extrae el apellido del primer autor de un string BibTeX author."""
    if not author_str:
        return None
    # BibTeX: "Lastname, Firstname and ..." o "Firstname Lastname and ..."
    first_author = author_str.split(' and ')[0].strip()
    if ',' in first_author:
        return first_author.split(',')[0].strip()
    parts = first_author.split()
    return parts[-1].strip() if parts else None


def verify_doi_online(doi: str, timeout: int = 10) -> tuple[bool, str]:
    """Verifica que un DOI exista via CrossRef API."""
    doi_clean = clean_doi(doi)
    url = CROSSREF_API.format(doi=quote(doi_clean, safe='/'))
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "SDD-Paper-Validator/1.0 (mailto:paperops@example.com)",
        })
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                return True, "OK"
            return False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "DOI no encontrado en CrossRef"
        return False, f"HTTP error {e.code}"
    except Exception as e:
        return False, f"Error de red: {str(e)[:50]}"


def fetch_crossref_metadata(doi: str, timeout: int = 10) -> dict | None:
    """Obtiene metadatos completos de CrossRef para un DOI.

    Retorna dict con title, authors (lista de apellidos), year, o None si falla.
    """
    doi_clean = clean_doi(doi)
    url = CROSSREF_API.format(doi=quote(doi_clean, safe='/'))
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "SDD-Paper-Validator/1.0 (mailto:paperops@example.com)",
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = json.loads(response.read().decode('utf-8'))

        work = data.get("message", {})

        # Titulo
        titles = work.get("title", [])
        title = titles[0] if titles else None

        # Autores (lista de apellidos)
        authors_raw = work.get("author", [])
        authors = [a.get("family", "") for a in authors_raw if a.get("family")]

        # Anio (intentar varios campos de fecha)
        year = None
        for date_field in ("published-print", "published-online", "issued", "created"):
            date_info = work.get(date_field, {})
            date_parts = date_info.get("date-parts", [[]])
            if date_parts and date_parts[0] and date_parts[0][0]:
                year = date_parts[0][0]
                break

        return {"title": title, "authors": authors, "year": year}
    except Exception:
        return None


def cross_check_entry(bib_entry: dict, crossref_meta: dict) -> list[str]:
    """Compara metadatos del .bib contra CrossRef. Retorna lista de discrepancias."""
    issues = []
    key = bib_entry["key"]

    # --- Titulo ---
    bib_title = bib_entry.get("bib_title")
    cr_title = crossref_meta.get("title")
    if bib_title and cr_title:
        ratio = difflib.SequenceMatcher(
            None, normalize_text(bib_title), normalize_text(cr_title)
        ).ratio()
        if ratio < 0.5:
            issues.append(
                f"FAIL: {key}: titulo muy diferente al de CrossRef (similitud: {ratio:.0%})"
            )
        elif ratio < 0.75:
            issues.append(
                f"WARN: {key}: titulo difiere del de CrossRef (similitud: {ratio:.0%})"
            )

    # --- Anio ---
    bib_year = bib_entry.get("bib_year")
    cr_year = crossref_meta.get("year")
    if bib_year and cr_year:
        try:
            if int(bib_year) != int(cr_year):
                issues.append(
                    f"WARN: {key}: anio en .bib ({bib_year}) != CrossRef ({cr_year})"
                )
        except ValueError:
            pass

    # --- Primer autor ---
    bib_author = bib_entry.get("bib_author")
    cr_authors = crossref_meta.get("authors", [])
    if bib_author and cr_authors:
        bib_lastname = extract_first_author_lastname(bib_author)
        cr_lastname = cr_authors[0] if cr_authors else None
        if bib_lastname and cr_lastname:
            ratio = difflib.SequenceMatcher(
                None, normalize_text(bib_lastname), normalize_text(cr_lastname)
            ).ratio()
            if ratio < 0.6:
                issues.append(
                    f"WARN: {key}: primer autor en .bib ({bib_lastname}) != CrossRef ({cr_lastname})"
                )

    return issues


def parse_bib_entries(bib_text: str) -> list[dict]:
    """Parsea archivo .bib en lista de dicts con metadatos."""
    entries = []
    for match in BIB_ENTRY_PATTERN.finditer(bib_text):
        entry_type = match.group(1)
        key = match.group(2)
        body = match.group(3)

        doi_match = DOI_PATTERN.search(body)
        doi = doi_match.group(1).strip() if doi_match else None

        # Extraer campos para cross-check
        bib_title = extract_bib_field(body, "title")
        bib_author = extract_bib_field(body, "author")
        bib_year = extract_bib_field(body, "year")

        # Verificar campos requeridos
        missing_fields = []
        for field in ["title", "author", "year"]:
            if not re.search(rf'\b{field}\s*=', body, re.IGNORECASE):
                missing_fields.append(field)

        entries.append({
            "type": entry_type,
            "key": key,
            "doi": doi,
            "missing_fields": missing_fields,
            "bib_title": bib_title,
            "bib_author": bib_author,
            "bib_year": bib_year,
        })
    return entries


def check_bib_dois(base_path: Path, offline: bool = False, cross_check: bool = True) -> tuple[bool, list[str]]:
    errors = []
    bib_file = base_path / "references" / "references.bib"

    if not bib_file.exists():
        print("[WARN] references/references.bib no encontrado -- skip")
        return True, []

    bib_text = bib_file.read_text(encoding="utf-8")
    entries = parse_bib_entries(bib_text)

    if not entries:
        print("[PASS] Referencias .bib: archivo vacio (sin entradas)")
        return True, []

    total = len(entries)
    with_doi = sum(1 for e in entries if e["doi"])
    without_doi = total - with_doi
    invalid_format = []
    not_found = []
    missing_fields_entries = []
    cross_check_issues = []

    for entry in entries:
        # Verificar campos requeridos
        if entry["missing_fields"]:
            missing_fields_entries.append(
                f"{entry['key']} (falta: {', '.join(entry['missing_fields'])})"
            )

        if not entry["doi"]:
            continue

        # Verificar formato DOI
        if not check_doi_format(entry["doi"]):
            invalid_format.append(f"{entry['key']}: '{entry['doi']}'")
            continue

        # Verificacion online
        if not offline and HAS_URLLIB:
            if cross_check:
                # Cross-check: obtener metadatos completos y comparar
                meta = fetch_crossref_metadata(entry["doi"])
                if meta is None:
                    not_found.append(f"{entry['key']}: no se pudo obtener metadatos")
                else:
                    issues = cross_check_entry(entry, meta)
                    cross_check_issues.extend(issues)
            else:
                # Solo verificar existencia
                ok, msg = verify_doi_online(entry["doi"])
                if not ok:
                    not_found.append(f"{entry['key']}: {msg}")
            time.sleep(0.1)  # Respetar rate limit de CrossRef

    if invalid_format:
        errors.append(f"FAIL: DOIs con formato invalido: {'; '.join(invalid_format[:3])}")
    if not_found:
        errors.append(f"WARN: DOIs no verificados en CrossRef: {'; '.join(not_found[:3])}")
    if missing_fields_entries:
        errors.append(f"WARN: Entradas con campos faltantes: {', '.join(missing_fields_entries[:3])}")

    # Cross-check issues
    for issue in cross_check_issues:
        errors.append(issue)

    has_fail = any(e.startswith("FAIL") for e in errors)
    passed = not has_fail
    status = "PASS" if passed else "FAIL"
    mode = "offline" if offline else ("online+cross-check" if cross_check else "online")
    print(f"[{status}] Referencias .bib ({mode}): {total} entradas, {with_doi} con DOI, {without_doi} sin DOI")
    if cross_check_issues:
        cc_fails = sum(1 for i in cross_check_issues if i.startswith("FAIL"))
        cc_warns = sum(1 for i in cross_check_issues if i.startswith("WARN"))
        print(f"  Cross-check: {cc_fails} discrepancias criticas, {cc_warns} advertencias")
    for e in errors:
        print(f"  - {e}")

    return passed, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica DOIs contra CrossRef API")
    parser.add_argument("--offline", action="store_true",
                        help="Solo verificar formato, no consultar CrossRef")
    parser.add_argument("--no-cross-check", action="store_true",
                        help="Solo verificar existencia del DOI, no cruzar metadatos")
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    ok, _ = check_bib_dois(base, offline=args.offline, cross_check=not args.no_cross_check)
    sys.exit(0 if ok else 1)
