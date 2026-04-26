import os
import re
import argparse

def sync_outline(target_dir):
    outline_path = os.path.join(target_dir, "outline.md")
    sections_dir = os.path.join(target_dir, "sections")

    if not os.path.exists(outline_path):
        print(f"Error: {outline_path} not found.")
        return

    with open(outline_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find headers like "# 1. Introduction" or "## 2. Methods"
        headers = re.findall(r'^(?:#+)\s+((?:\d+\.?\s*)?[\w\s]+)', content, re.MULTILINE)

    print(f"Syncing {len(headers)} sections from outline...")
    for i, header in enumerate(headers, 1):
        # Clean header name to valid filename
        filename = re.sub(r'[^\w\s-]', '', header).strip().replace(' ', '_').lower()
        file_path = os.path.join(sections_dir, f"{i:02d}_{filename}.md")

        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {header}\n\n[DRAFT: Contenido de la sección {header}]\n")
            print(f"Created: {file_path}")
        else:
            print(f"Exists: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    args = parser.parse_args()
    sync_outline(args.dir)