#!/usr/bin/env python3
"""
validate-citations.py — Valida citaciones en el paper vs el archivo .bib.
Uso: python scripts/validate-citations.py
"""

import re
import sys
from pathlib import Path


CITATION_PATTERNS = [
    re.compile(r'\[(\d+)\]'),                    # [1], [2,3], [1-5]
    re.compile(r'\\cite\{([^}]+)\}'),             # \cite{key} or \cite{key1,key2}
    re.compile(r'\[@([^\]]+)\]'),                  # [@key] pandoc style
    re.compile(r'\(([A-Z][a-z]+(?:\s+et\s+al\.)?,\s+\d{4}[a-z]?)\)'),  # (Smith, 2023)
]

BIB_KEY_PATTERN = re.compile(r'@\w+\{([^,\s]+),')


def extract_cited_keys(text: str) -> set[str]:
    """Extract all citation keys/numbers from text."""
    keys = set()
    for pattern in CITATION_PATTERNS:
        for match in pattern.finditer(text):
            raw = match.group(1)
            # Handle multiple keys: \cite{key1,key2}
            for k in raw.split(','):
                keys.add(k.strip())
    return keys


def extract_bib_keys(bib_text: str) -> set[str]:
    """Extract all keys defined in .bib file."""
    return set(BIB_KEY_PATTERN.findall(bib_text))


def count_uncited_claims(text: str) -> int:
    """Rough estimate of sentences that look like claims but have no citation."""
    claim_indicators = [
        r'\b(studies|research|show|demonstrate|indicate|suggest|find|found|report)\b',
        r'\b(according to|as shown|it is known|it has been|previous work)\b',
        r'\b(\d+%|\d+ percent|significantly|substantially|notably)\b',
    ]
    sentences = re.split(r'(?<=[.!?])\s+', text)
    uncited = 0
    for sent in sentences:
        is_claim = any(re.search(p, sent, re.IGNORECASE) for p in claim_indicators)
        has_citation = any(pattern.search(sent) for pattern in CITATION_PATTERNS)
        if is_claim and not has_citation:
            uncited += 1
    return uncited


def validate_citations(base_path: Path) -> tuple[bool, list[str]]:
    errors = []
    sections_dir = base_path / "paper" / "sections"
    bib_file = base_path / "references" / "references.bib"

    if not sections_dir.exists():
        errors.append("FAIL: paper/sections/ no encontrado")
        return False, errors

    # Collect all cited keys from paper
    all_cited_keys: set[str] = set()
    total_uncited = 0
    all_text = ""

    for section_file in sorted(sections_dir.glob("*.md")):
        content = section_file.read_text(encoding="utf-8")
        all_text += content + "\n"
        keys = extract_cited_keys(content)
        all_cited_keys.update(keys)
        uncited = count_uncited_claims(content)
        total_uncited += uncited

    # Check bib file
    bib_keys: set[str] = set()
    if bib_file.exists():
        bib_text = bib_file.read_text(encoding="utf-8")
        bib_keys = extract_bib_keys(bib_text)

        # Check for numeric citations (can't validate against bib keys)
        numeric_only = all(k.isdigit() for k in all_cited_keys if k)
        if not numeric_only:
            orphan_citations = all_cited_keys - bib_keys
            orphan_bib = bib_keys - all_cited_keys

            if orphan_citations:
                errors.append(f"FAIL: Citas en texto sin entrada en .bib: {', '.join(sorted(orphan_citations)[:5])}")
            if orphan_bib:
                errors.append(f"WARN: Entradas en .bib no citadas en texto: {', '.join(sorted(orphan_bib)[:5])}")
    else:
        if all_cited_keys:
            errors.append("FAIL: references/references.bib no existe pero hay citaciones en el texto")

    if total_uncited > 0:
        errors.append(f"WARN: ~{total_uncited} claims sin citación detectadas")

    passed = not any(e.startswith("FAIL") for e in errors)
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] Citaciones: {len(all_cited_keys)} refs citadas, {len(bib_keys)} en .bib, ~{total_uncited} claims sin citar")
    for e in errors:
        print(f"  - {e}")

    return passed, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_citations(base)
    sys.exit(0 if ok else 1)
