#!/usr/bin/env python3
"""
check-bib-dois.py — Verifica DOIs en references.bib contra CrossRef API.
Uso: python scripts/check-bib-dois.py [--offline]
"""

import re
import sys
import time
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
CROSSREF_API = "https://api.crossref.org/works/{doi}"


def check_doi_format(doi: str) -> bool:
    """Check if DOI has valid format."""
    doi = doi.strip().lstrip("https://doi.org/").lstrip("http://dx.doi.org/")
    return bool(DOI_FORMAT_PATTERN.match(doi))


def verify_doi_online(doi: str, timeout: int = 5) -> tuple[bool, str]:
    """Verify DOI exists via CrossRef API."""
    doi_clean = doi.strip().lstrip("https://doi.org/").lstrip("http://dx.doi.org/")
    url = CROSSREF_API.format(doi=quote(doi_clean, safe='/'))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SDD-Paper-Validator/1.0"})
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


def parse_bib_entries(bib_text: str) -> list[dict]:
    """Parse .bib file into list of entry dicts."""
    entries = []
    for match in BIB_ENTRY_PATTERN.finditer(bib_text):
        entry_type = match.group(1)
        key = match.group(2)
        body = match.group(3)

        doi_match = DOI_PATTERN.search(body)
        doi = doi_match.group(1).strip() if doi_match else None

        # Check for required fields
        missing_fields = []
        for field in ["title", "author", "year"]:
            if not re.search(rf'\b{field}\s*=', body, re.IGNORECASE):
                missing_fields.append(field)

        entries.append({
            "type": entry_type,
            "key": key,
            "doi": doi,
            "missing_fields": missing_fields,
        })
    return entries


def check_bib_dois(base_path: Path, offline: bool = False) -> tuple[bool, list[str]]:
    errors = []
    bib_file = base_path / "references" / "references.bib"

    if not bib_file.exists():
        print("[WARN] references/references.bib no encontrado — skip")
        return True, []

    bib_text = bib_file.read_text()
    entries = parse_bib_entries(bib_text)

    if not entries:
        print("[PASS] Referencias .bib: archivo vacío (sin entradas)")
        return True, []

    total = len(entries)
    with_doi = sum(1 for e in entries if e["doi"])
    without_doi = total - with_doi
    invalid_format = []
    not_found = []
    missing_fields_entries = []

    for entry in entries:
        # Check missing fields
        if entry["missing_fields"]:
            missing_fields_entries.append(f"{entry['key']} (falta: {', '.join(entry['missing_fields'])})")

        if not entry["doi"]:
            continue

        # Check DOI format
        if not check_doi_format(entry["doi"]):
            invalid_format.append(f"{entry['key']}: '{entry['doi']}'")
            continue

        # Online verification (rate-limited)
        if not offline and HAS_URLLIB:
            ok, msg = verify_doi_online(entry["doi"])
            if not ok:
                not_found.append(f"{entry['key']}: {msg}")
            time.sleep(0.1)  # Be respectful to CrossRef API

    if invalid_format:
        errors.append(f"FAIL: DOIs con formato inválido: {'; '.join(invalid_format[:3])}")
    if not_found:
        errors.append(f"WARN: DOIs no encontrados en CrossRef: {'; '.join(not_found[:3])}")
    if missing_fields_entries:
        errors.append(f"WARN: Entradas con campos faltantes: {', '.join(missing_fields_entries[:3])}")

    passed = not any(e.startswith("FAIL") for e in errors)
    status = "PASS" if passed else "FAIL"
    mode = "offline" if offline else "online"
    print(f"[{status}] Referencias .bib ({mode}): {total} entradas, {with_doi} con DOI, {without_doi} sin DOI")
    for e in errors:
        print(f"  → {e}")

    return passed, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Solo verificar formato, no consultar CrossRef")
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    ok, _ = check_bib_dois(base, offline=args.offline)
    sys.exit(0 if ok else 1)
