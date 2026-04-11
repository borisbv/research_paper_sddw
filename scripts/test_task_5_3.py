import os
import re

def test_task_5_3():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if section 4.3 Results: Divergences is written
    section_match = re.search(r"### 4\.3 Divergencias.*?\n(.*?)(?=\s---)", content, re.DOTALL)
    assert section_match, "Section 4.3 Divergences not found"
    section_content = section_match.group(1).strip()
    
    assert "[Pendiente]" not in section_content, "Section 4.3 still contains [Pendiente] marker"
    
    # Word count check (~400 words)
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(section_content)
    print(f"Section 4.3 word count: {total_words}")
    assert 350 <= total_words <= 500, f"Section 4.3 word count should be around 400, found {total_words}"
    
    # Check for specific topics
    assert "redes de apoyo" in section_content.lower()
    assert "convergencias ilícitas" in section_content.lower()
    assert "trata" in section_content.lower()
    
    # Check for specific citations
    assert "Marat y Zabyelina (2021)" in section_content or "Marat y Zabyelina, 2021" in section_content
    
    # Check for terminology
    assert "economía de la trata" in section_content.lower()
    assert "infraestructura de riesgo" in section_content.lower()
    
    print("Task 5.3: Results (Divergences) validation passed!")

if __name__ == "__main__":
    try:
        test_task_5_3()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
