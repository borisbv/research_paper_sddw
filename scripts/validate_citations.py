import os
import re
import argparse
import glob

def validate_citations(target_dir):
    print(f"Validating citations for target: {target_dir}...")
    sections_path = os.path.join(target_dir, "sections", "*.md")
    bib_path = os.path.join(target_dir, "references", "references.bib")
    
    if not os.path.exists(bib_path):
        print(f"Warning: BibTeX file not found at {bib_path}")
        return

    with open(bib_path, 'r', encoding='utf-8') as f:
        bib_content = f.read()
        bib_keys = re.findall(r'@\w+\{(.*?),', bib_content)

    sections = glob.glob(sections_path)
    errors = []
    for section in sections:
        with open(section, 'r', encoding='utf-8') as f:
            content = f.read()
            citations = re.findall(r'\\cite\{(.*?)\}', content)
            for cite in citations:
                for key in cite.split(','):
                    key = key.strip()
                    if key not in bib_keys:
                        errors.append(f"Error: Citation '{key}' in {section} not found in {bib_path}")

    if not errors:
        print("✅ All citations validated.")
    else:
        for err in errors:
            print(err)
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='paper', help='Research directory (paper or book)')
    args = parser.parse_args()
    validate_citations(args.dir)
