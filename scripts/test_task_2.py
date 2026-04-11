import os
import re

def test_introduction():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if introduction section is not "Pendiente"
    intro_match = re.search(r"## 1\. Introducción(.*?)(?=## 2\. Marco teórico)", content, re.DOTALL)
    assert intro_match, "Introduction section not found"
    intro_content = intro_match.group(1)
    
    assert "[Pendiente]" not in intro_content, "Introduction still contains [Pendiente] marker"
    
    # Check sub-sections
    assert "### 1.1 Contexto del fenómeno migratorio y la transformación digital" in intro_content
    assert "### 1.2 Problema de investigación, hipótesis y objetivos" in intro_content
    
    # Word count check (Introduction ~1200 words)
    # 1.1 ~600, 1.2 ~600
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(intro_content)
    print(f"Introduction word count: {total_words}")
    assert 1000 <= total_words <= 1400, f"Introduction word count should be around 1200, found {total_words}"
    
    # Check for specific data/citations in 1.1
    assert "281 millones" in intro_content, "Missing UN migration data (281 million)"
    assert "1,6 millones" in intro_content, "Missing Chile migration data (1.6 million)"
    assert "Diminescu (2008)" in intro_content, "Missing Diminescu (2008) citation"
    assert "91%" in intro_content and "77,4%" in intro_content, "Missing Chile penetration data"
    
    # Check for specific concepts in 1.2
    assert "¿Cómo las personas migrantes resignifican" in intro_content, "Missing research question"
    assert "hipótesis" in intro_content.lower(), "Missing hypothesis statement"
    assert "objetivo general" in intro_content.lower(), "Missing general objective"
    assert "objetivos específicos" in intro_content.lower(), "Missing specific objectives"

    print("Task 2: Introduction validation passed!")

if __name__ == "__main__":
    try:
        test_introduction()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
