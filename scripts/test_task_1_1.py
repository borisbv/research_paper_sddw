import os
import re

def test_manuscrito_structure():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check bilingual titles (two H1 headers)
    titles = re.findall(r"^# .+", content, re.MULTILINE)
    assert len(titles) >= 2, "Should have at least two H1 titles (Spanish and English)"
    
    # Check bilingual abstract sections
    assert "## Abstract" in content, "Missing Abstract section"
    assert "## Abstract (English)" in content or "## Abstract (Inglés)" in content, "Missing English Abstract section"
    
    # Check keywords
    assert "Palabras clave" in content, "Missing Palabras clave"
    assert "Keywords" in content, "Missing Keywords"
    
    # Check keywords count (4-8)
    keywords_line = re.search(r"Palabras clave\*\*: (.+)", content)
    if keywords_line:
        keywords = [k.strip() for k in keywords_line.group(1).split(",")]
        assert 4 <= len(keywords) <= 8, f"Keywords count should be between 4 and 8, found {len(keywords)}"
    
    # Check main sections
    required_sections = [
        "Introducción",
        "Marco teórico",
        "Metodología",
        "Resultados",
        "Discusión",
        "Conclusiones",
        "Referencias bibliográficas"
    ]
    for section in required_sections:
        assert f"## {section}" in content or f"## {required_sections.index(section)+1}. {section}" in content, f"Missing section: {section}"

    # Check for estimated extensions (e.g., ~1.200 palabras)
    assert re.search(r"Extensión estimada: ~?\d+[\.,]?\d* palabras", content), "Missing estimated extension markers"

    print("Task 1.1: All structural checks passed!")

if __name__ == "__main__":
    try:
        test_manuscrito_structure()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
