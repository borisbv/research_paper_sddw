import os
import requests
import argparse

def sync_zotero(library_id, api_key, output_file="references/references.bib"):
    print(f"Syncing Zotero library {library_id} to {output_file}...")
    url = f"https://api.zotero.org/groups/{library_id}/items?format=bibtex&limit=100"
    headers = {"Zotero-API-Key": api_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success: References synchronized.")
    else:
        print(f"Error: Failed to sync (Status {response.status_code})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sync Zotero library to BibTeX.')
    parser.add_argument('--id', help='Zotero Library/Group ID')
    parser.add_argument('--key', help='Zotero API Key')
    args = parser.parse_args()
    
    if args.id and args.key:
        sync_zotero(args.id, args.key)
    else:
        print("Zotero credentials not provided. Skipping API sync.")
