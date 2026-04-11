import os
import re

def test_task_5_1():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if section 4.1 Results: Connectivity is written
    # Section starts with "### 4.1 Conectividad: copresencia virtual, cercanía familiar y polisemia"
    # and ends before "### 4.2 Contexto de uso"
    section_match = re.search(r"### 4\.1 Conectividad: copresencia virtual, cercanía familiar y polisemia(.*?)(?=### 4\.2 Contexto de uso)", content, re.DOTALL)
    assert section_match, "Section 4.1 Connectivity not found"
    section_content = section_match.group(1).strip()
    
    assert "[Pendiente]" not in section_content, "Section 4.1 still contains [Pendiente] marker"
    assert len(section_content) > 100, "Section 4.1 seems too short"

    # Word count check (~700 words)
    def count_words(text):
        # Remove markdown comments
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        # Remove headers
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(section_content)
    print(f"Section 4.1 word count: {total_words}")
    assert 600 <= total_words <= 800, f"Section 4.1 word count should be around 700, found {total_words}"
    
    # Check for specific topics
    assert "WhatsApp" in section_content
    assert "videollamada" in section_content.lower()
    assert "copresencia virtual" in section_content.lower()
    assert "polisemia" in section_content.lower()
    
    # Check for testimonies (Cecilia, José, Patricia, Jackie)
    assert "Cecilia" in section_content
    assert "José" in section_content
    assert "Patricia" in section_content
    assert "Jackie" in section_content
    
    # Check for specific citations
    assert "Pearce y Rice (2013)" in section_content
    assert "Madianou (2014)" in section_content
    
    # Check for terminology
    assert "personas migrantes" in section_content
    assert "resignificación" in section_content
    
    print("Task 5.1: Results (Connectivity) validation passed!")

if __name__ == "__main__":
    try:
        test_task_5_1()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
