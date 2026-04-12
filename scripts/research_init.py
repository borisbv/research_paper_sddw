import os
import argparse
import sys
import yaml

def init_research(target_type):
    target_dir = target_type.lower()
    if target_dir not in ['paper', 'book']:
        print("Error: Target type must be 'paper' or 'book'.")
        sys.exit(1)

    print(f"--- Research Engine Initialization: {target_dir.upper()} ---")
    
    # Check if exists
    is_continuation = os.path.exists(target_dir)
    
    if is_continuation:
        print(f"Detected existing project in /{target_dir}. Resuming iteration...")
    else:
        print(f"Creating new structure for {target_dir}...")
        subdirs = ['sections', 'references', 'figures', 'data', 'scripts']
        os.makedirs(target_dir, exist_ok=True)
        for sd in subdirs:
            os.makedirs(os.path.join(target_dir, sd), exist_ok=True)
        
        # Create _quarto.yml
        quarto_config = {
            'project': {'type': 'book' if target_dir == 'book' else 'default'},
            'format': {
                'pdf': {
                    'toc': True,
                    'number-sections': True,
                    'cite-method': 'biblatex'
                }
            },
            'bibliography': 'references/references.bib'
        }
        with open(os.path.join(target_dir, '_quarto.yml'), 'w', encoding='utf-8') as f:
            yaml.dump(quarto_config, f)
        
        # Create base files
        metadata = {
            'target': target_dir,
            'status': 'initialization',
            'title': f'Untitled {target_dir.capitalize()}',
            'authors': [],
            'last_iteration': 'now'
        }
        with open(os.path.join(target_dir, 'metadata.yaml'), 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f)
            
        with open(os.path.join(target_dir, 'outline.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Outline for {target_dir.capitalize()}\n\n## 1. Introduction\n...")

    print(f"✅ Ready to work on {target_dir}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='paper or book')
    args = parser.parse_args()
    init_research(args.type)
