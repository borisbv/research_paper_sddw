import os
import re

def test_task_6():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check Section 5.1
    section_5_1_match = re.search(r"### 5\.1 Síntesis de hallazgos y contraste usos convencionales frente a migrantes(.*?)(?=### 5\.2)", content, re.DOTALL)
    assert section_5_1_match, "Section 5.1 Discussion: Synthesis not found"
    section_5_1_content = section_5_1_match.group(1).strip()
    
    assert "[Pendiente]" not in section_5_1_content, "Section 5.1 still contains [Pendiente] marker"
    
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    words_5_1 = count_words(section_5_1_content)
    print(f"Section 5.1 word count: {words_5_1}")
    assert 500 <= words_5_1 <= 750, f"Section 5.1 word count should be around 600, found {words_5_1}"

    # Check for content in 5.1
    assert "Tabla 1" in section_5_1_content or "tabla de categorías" in section_5_1_content.lower()
    assert "ocio" in section_5_1_content.lower()
    assert "supervivencia" in section_5_1_content.lower()
    assert "copresencia" in section_5_1_content.lower()

    # Check Section 5.2
    section_5_2_match = re.search(r"### 5\.2 Implicaciones teóricas, limitaciones y brecha digital(.*?)(?=---|\n## 6\.)", content, re.DOTALL)
    assert section_5_2_match, "Section 5.2 Discussion: Implications not found"
    section_5_2_content = section_5_2_match.group(1).strip()
    
    assert "[Pendiente]" not in section_5_2_content, "Section 5.2 still contains [Pendiente] marker"
    
    words_5_2 = count_words(section_5_2_content)
    print(f"Section 5.2 word count: {words_5_2}")
    assert 500 <= words_5_2 <= 750, f"Section 5.2 word count should be around 600, found {words_5_2}"

    # Check for content in 5.2
    assert "van Dijck" in section_5_2_content
    assert "Diminescu" in section_5_2_content
    assert "brecha digital" in section_5_2_content.lower()
    assert "limitaciones" in section_5_2_content.lower()
    assert "Scopus" in section_5_2_content

    print("Task 6: Discussion validation passed!")

if __name__ == "__main__":
    try:
        test_task_6()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
