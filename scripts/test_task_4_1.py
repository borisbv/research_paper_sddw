import os
import re

def test_methodology_section():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if Metodología section is present
    meto_match = re.search(r"## 3\. Metodología(.*?)(?=## 4\. Resultados)", content, re.DOTALL)
    assert meto_match, "Metodología section not found"
    meto_content = meto_match.group(1)
    
    # Ensure [Pendiente] is gone
    assert "[Pendiente]" not in meto_content, "Metodología section still contains [Pendiente] markers"
    
    # Word count check (~800 words)
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(meto_content)
    print(f"Metodología word count: {total_words}")
    assert 600 <= total_words <= 1000, f"Metodología word count should be around 800, found {total_words}"
    
    # Check for specific requirements
    keywords = [
        "enfoque cualitativo",
        "revisión sistemática de literatura",
        "metaanálisis cualitativo",
        "Scopus",
        "últimos 5 años",
        "criterios de inclusión",
        "corpus",
        "160 artículos",
        "análisis de contenido cualitativo",
        "conectividad",
        "contexto de uso",
        "divergencias",
        "Hernández Sampieri",
        "Mendoza Torres",
        "2018"
    ]
    
    for word in keywords:
        assert word.lower() in meto_content.lower(), f"Missing keyword/concept: {word}"

    print("Task 4.1: Methodology validation passed!")

if __name__ == "__main__":
    try:
        test_methodology_section()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
