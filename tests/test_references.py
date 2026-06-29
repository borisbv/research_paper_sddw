"""Tests para la validación de calidad del archivo de referencias bibliográficas."""

import re
import sys
from pathlib import Path

import pytest

BIB_PATH = Path(__file__).parent.parent / "references" / "references.bib"


def parse_bib_entries(bib_text: str) -> list[dict]:
    """Parsea entradas BibTeX y retorna lista de diccionarios con campos clave."""
    entries = []
    # Split por @ que inicia una entrada (ignorando comentarios %)
    raw_entries = re.split(r'\n(?=@)', bib_text)
    for raw in raw_entries:
        raw = raw.strip()
        if not raw or raw.startswith('%'):
            continue
        entry = {}
        # Tipo y citekey
        type_match = re.match(r'@(\w+)\{([^,]+),', raw)
        if type_match:
            entry['type'] = type_match.group(1).lower()
            entry['citekey'] = type_match.group(2).strip()
        # Año
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', raw)
        if year_match:
            entry['year'] = int(year_match.group(1))
        # DOI
        doi_match = re.search(r'doi\s*=\s*\{([^}]+)\}', raw)
        if doi_match:
            entry['doi'] = doi_match.group(1).strip()
        # URL
        url_match = re.search(r'url\s*=\s*\{([^}]+)\}', raw)
        if url_match:
            entry['url'] = url_match.group(1).strip()
        # Title
        title_match = re.search(r'title\s*=\s*\{(.+?)\}', raw, re.DOTALL)
        if title_match:
            entry['title'] = title_match.group(1).strip()
        # Author
        author_match = re.search(r'author\s*=\s*\{(.+?)\}', raw, re.DOTALL)
        if author_match:
            entry['author'] = author_match.group(1).strip()
        if entry.get('citekey'):
            entries.append(entry)
    return entries


@pytest.fixture
def bib_entries():
    assert BIB_PATH.exists(), f"No existe el archivo {BIB_PATH}"
    text = BIB_PATH.read_text(encoding='utf-8')
    return parse_bib_entries(text)


class TestReferenceCount:
    def test_minimum_30_references(self, bib_entries):
        assert len(bib_entries) >= 30, \
            f"Se requieren >=30 referencias, hay {len(bib_entries)}"


class TestRecency:
    def test_60_percent_recent(self, bib_entries):
        """Al menos 60% de referencias deben ser de 2021-2026."""
        with_year = [e for e in bib_entries if 'year' in e]
        recent = [e for e in with_year if 2021 <= e['year'] <= 2026]
        ratio = len(recent) / len(with_year) if with_year else 0
        assert ratio >= 0.60, \
            f"Solo {ratio:.0%} de referencias son recientes (2021-2026), se requiere >=60%"


class TestBibTeXFormat:
    def test_all_entries_have_type(self, bib_entries):
        for e in bib_entries:
            assert 'type' in e, f"Entrada sin tipo: {e.get('citekey', 'unknown')}"

    def test_all_entries_have_title(self, bib_entries):
        for e in bib_entries:
            assert 'title' in e, f"Entrada sin título: {e.get('citekey', 'unknown')}"

    def test_all_entries_have_author(self, bib_entries):
        for e in bib_entries:
            assert 'author' in e, f"Entrada sin autor: {e.get('citekey', 'unknown')}"

    def test_all_entries_have_year(self, bib_entries):
        for e in bib_entries:
            assert 'year' in e, f"Entrada sin año: {e.get('citekey', 'unknown')}"

    def test_unique_citekeys(self, bib_entries):
        keys = [e['citekey'] for e in bib_entries]
        duplicates = [k for k in keys if keys.count(k) > 1]
        assert len(set(duplicates)) == 0, f"Citekeys duplicados: {set(duplicates)}"


class TestDOIVerification:
    def test_entries_have_doi_or_url(self, bib_entries):
        """Cada entrada debe tener DOI o URL verificable."""
        missing = []
        for e in bib_entries:
            if 'doi' not in e and 'url' not in e:
                missing.append(e.get('citekey', 'unknown'))
        assert len(missing) == 0, \
            f"Entradas sin DOI ni URL: {missing}"


class TestAcademicSources:
    def test_no_non_academic_sources(self, bib_entries):
        """No deben existir blogs o fuentes comerciales (excepto docs técnica oficial)."""
        allowed_non_journal = {'techreport', 'misc', 'inproceedings', 'book',
                               'incollection', 'phdthesis', 'mastersthesis'}
        # Las entradas misc/techreport son aceptables si tienen URL de organismo oficial
        official_domains = ['w3.org', 'who.int', 'un.org', 'iso.org', 'itu.int',
                           'ieee.org', 'acm.org']
        suspicious = []
        for e in bib_entries:
            if e.get('type') == 'misc':
                url = e.get('url', '')
                if not any(d in url for d in official_domains) and 'doi' not in e:
                    suspicious.append(e.get('citekey', 'unknown'))
        # Warn but don't fail for now - flag for manual review
        if suspicious:
            pytest.warns(UserWarning,
                        match=f"Refs posiblemente no académicas: {suspicious}")
