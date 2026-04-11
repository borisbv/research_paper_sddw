import re
from pathlib import Path

def split_manuscript(file_path):
    content = Path(file_path).read_text(encoding='utf-8')
    
    # Define sections and their starting headers
    sections = {
        "abstract": r"## Abstract\n",
        "introduction": r"## 1. Introducción",
        "related-work": r"## 2. Marco teórico",
        "methodology": r"## 3. Metodología",
        "results": r"## 4. Resultados",
        "discussion": r"## 5. Discusión",
        "conclusion": r"## 6. Conclusiones",
    }
    
    output_dir = Path("paper/sections")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Sort sections by their appearance in the text
    pos = {name: content.find(header.replace("\\n", "\n")) for name, header in sections.items()}
    sorted_sections = sorted(pos.keys(), key=lambda x: pos[x])
    
    for i, name in enumerate(sorted_sections):
        start = pos[name]
        if i + 1 < len(sorted_sections):
            end = pos[sorted_sections[i+1]]
        else:
            # For the last section (conclusion), we stop before References if exists
            end = content.find("## Referencias bibliográficas")
            if end == -1:
                end = len(content)
        
        section_content = content[start:end].strip()
        (output_dir / f"{name}.md").write_text(section_content, encoding='utf-8')
        print(f"Created {name}.md")

if __name__ == "__main__":
    split_manuscript("paper/manuscrito.md")
