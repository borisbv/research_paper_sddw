import os
import requests
import re
import argparse

def enrich_bib(target_dir):
    bib_path = os.path.join(target_dir, "references", "references.bib")
    if not os.path.exists(bib_path):
        print("No BibTeX file found to enrich.")
        return

    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find DOIs in entries
    dois = re.findall(r'doi\s*=\s*\{(.*?)\}', content)
    print(f"Found {len(dois)} DOIs. Querying Crossref...")

    # This is a simplified version, ideally would use a bibtex parser
    # But for a script, regex is token-efficient and fast
    for doi in dois:
        url = f"https://api.crossref.org/works/{doi}"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()['message']
                title = data.get('title', ['Unknown'])[0]
                year = data.get('published-print', {}).get('date-parts', [[0]])[0][0]
                print(f"Enriched: {doi} -> {title} ({year})")
        except:
            print(f"Failed to enrich DOI: {doi}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    args = parser.parse_args()
    enrich_bib(args.dir)