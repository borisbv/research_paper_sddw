#!/usr/bin/env python3
"""
validate-citations.py — Valida citaciones en el paper vs el archivo .bib.
Uso: python scripts/validate-citations.py
"""

import re
import sys
from pathlib import Path


CITATION_PATTERNS = [
    re.compile(r'\\cite\{([^}]+)\}'),             # \cite{key}
    re.compile(r'\[@([^\]]+)\]'),                  # [@key]
    # Harvard style in parentheses: (Author, 2023), (Author & Author, 2023), (Author et al., 2023)
    # Supporting Spanish "y": (Bell y Erdal, 2015)
    # Supporting page numbers: (Vermot, 2015: 145)
    re.compile(r'\(([A-Z][^,)]+,\s+\d{4}[a-z]?(?::\s*\d+)?)\)'),
    # Narrative style: Author (2023), Author & Author (2023), Author y Author (2023), Author et al. (2023)
    re.compile(r'\b([A-Z][^()]+\s*(?:et\s+al\.|y|&|and)?\s*[^()]*)\s+\((\d{4}[a-z]?)\)'),
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
    sections_dir = base_path / "paper"
    bib_file = base_path / "references" / "references.bib"

    if not sections_dir.exists():
        errors.append("FAIL: paper/ no encontrado")
        return False, errors

    # Collect all cited strings from paper
    all_cited_text: set[str] = set()
    total_uncited = 0
    
    # Metadata for better matching
    metadata_file = base_path / "paper" / "metadata.yaml"
    files_to_check = []
    if metadata_file.exists():
        try:
            with open(metadata_file) as f:
                import yaml
                meta = yaml.safe_load(f)
                if meta and 'sections' in meta:
                    files_to_check = [base_path / s['file'] for s in meta['sections'] if 'file' in s]
                else:
                    files_to_check = sorted(sections_dir.glob("*.md"))
        except Exception:
            files_to_check = sorted(sections_dir.glob("*.md"))
    else:
        files_to_check = sorted(sections_dir.glob("*.md"))

    for section_file in files_to_check:
        if not section_file.exists() or section_file.name in ["00_metadata.md", "review-report.md", "metadata.yaml"]:
            continue
        content = section_file.read_text(encoding='utf-8')
        
        # Extract matches using patterns
        for pattern in CITATION_PATTERNS:
            for match in pattern.finditer(content):
                all_cited_text.add(match.group(0))
        
        total_uncited += count_uncited_claims(content)

    # Check bib file
    bib_keys: set[str] = set()
    if bib_file.exists():
        bib_text = bib_file.read_text(encoding='utf-8')
        bib_keys = extract_bib_keys(bib_text)

        # Smart matching
        matched_keys = set()
        orphan_citations = []
        
        for cite_str in all_cited_text:
            found = False
            # Normalize cite string: "(Bell y Erdal, 2015)" -> "bell erdal 2015"
            norm_cite = re.sub(r'[^\w\s]', ' ', cite_str).lower()
            cite_words = norm_cite.split()
            
            for key in bib_keys:
                # Basic check: is key in cite_str or parts of key in cite_str
                year_match = re.search(r'\d{4}', key)
                year = year_match.group(0) if year_match else ""
                author_part = key.replace(year, "").lower() if year else key.lower()
                
                # Check if year matches
                if year and year not in norm_cite:
                    continue
                
                # Check if author_part is in norm_cite OR if any word in norm_cite matches author_part
                # This handles "Boccagni y Baldassar" matching "boccagni2015"
                if author_part in norm_cite or any(w == author_part for w in cite_words):
                    matched_keys.add(key)
                    found = True
                    break
                
                # Handle special case: "van Dijck" vs "vandijck"
                if author_part.replace(" ", "") in norm_cite.replace(" ", ""):
                    matched_keys.add(key)
                    found = True
                    break
            
            if not found:
                # Last resort: check if any part of the cite_str matches the key (e.g. key=boccagni2015 matches Baldassar)
                # Actually, check if the key's author part matches ANY part of the cite string
                # or vice-versa. But let's be careful.
                pass
                
            if not found:
                # Check for standard cite commands which might have direct keys
                key_match = re.search(r'\\cite\{([^}]+)\}|\[@([^\]]+)\]', cite_str)
                if key_match:
                    k = key_match.group(1) or key_match.group(2)
                    if k in bib_keys:
                        matched_keys.add(k)
                        found = True
                
                if not found:
                    orphan_citations.append(cite_str)

        orphan_bib = bib_keys - matched_keys

        if orphan_citations:
            errors.append(f"FAIL: Citas en texto sin entrada clara en .bib: {', '.join(sorted(orphan_citations)[:5])}")
        if orphan_bib:
            errors.append(f"WARN: Entradas en .bib posiblemente no citadas: {', '.join(sorted(orphan_bib)[:5])}")
    else:
        if all_cited_text:
            errors.append("FAIL: references/references.bib no existe")

    if total_uncited > 0:
        errors.append(f"WARN: ~{total_uncited} claims sin citación detectadas")

    passed = not any(e.startswith("FAIL") for e in errors)
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] Citaciones: {len(all_cited_text)} citas encontradas, {len(bib_keys)} en .bib, {len(matched_keys)} emparejadas")
    for e in errors:
        print(f"  - {e}")

    return passed, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_citations(base)
    sys.exit(0 if ok else 1)
