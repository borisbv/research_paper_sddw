import re
import os
import glob

def validate_figures():
    sections = glob.glob("paper/sections/*.md")
    figures = [os.path.basename(f) for f in glob.glob("figures/*.*")]
    
    print("Validating Figure Citations...")
    errors = []
    
    for section_path in sections:
        with open(section_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match Markdown image syntax or LaTeX figure references
            found_figures = re.findall(r'!\[.*?\]\((?:../)?figures/(.*?)\)', content)
            
            for fig in found_figures:
                if fig not in figures:
                    errors.append(f"Error: Figure '{fig}' referenced in {section_path} but not found in figures/ folder.")
    
    if not errors:
        print("✅ All referenced figures found.")
    else:
        for err in errors:
            print(err)
        exit(1)

if __name__ == "__main__":
    validate_figures()
