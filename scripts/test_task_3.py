import os
import re

def test_theoretical_framework():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if Marco Teórico section is present
    marco_match = re.search(r"## 2\. Marco teórico(.*?)(?=## 3\. Metodología)", content, re.DOTALL)
    assert marco_match, "Marco Teórico section not found"
    marco_content = marco_match.group(1)
    
    # Check sub-sections
    assert "### 2.1 Significación convencional de las redes sociales y usos locales" in marco_content
    assert "### 2.2 Comunicación transnacional y resignificación" in marco_content
    assert "### 2.3 Capital social y redes migratorias digitales" in marco_content
    
    # Ensure [Pendiente] is gone for these sections
    assert "[Pendiente]" not in marco_content, "Marco Teórico still contains [Pendiente] markers"
    
    # Word count check (~2000 words total for section 2)
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(marco_content)
    print(f"Marco Teórico word count: {total_words}")
    assert 1700 <= total_words <= 2300, f"Marco Teórico word count should be around 2000, found {total_words}"
    
    # Check for specific content in 2.1
    assert "Facebook" in marco_content or "Meta" in marco_content, "Missing Facebook/Meta mention"
    assert "WhatsApp" in marco_content, "Missing WhatsApp mention"
    assert "Instagram" in marco_content, "Missing Instagram mention"
    assert "TikTok" in marco_content, "Missing TikTok mention"
    assert "Chile" in marco_content, "Missing Chile data"
    assert "Pew Research" in marco_content, "Missing Pew Research mention"
    
    # Citations list (flexible check)
    citations = [
        "Diminescu", "2008",
        "Baldassar", "2016",
        "Peñaranda", "2010",
        "Peñaranda", "2011",
        "van Dijck", "2013",
        "Zhao",
        "Bell", "Erdal", "2015",
        "Vermot", "2015",
        "Massey", "España", "1987",
        "Oxford",
        "vínculos fuertes",
        "vínculos débiles"
    ]
    
    for cit in citations:
        assert cit in marco_content, f"Missing {cit} citation or concept in Marco Teórico"

    print("Task 3: Theoretical Framework validation passed!")

if __name__ == "__main__":
    try:
        test_theoretical_framework()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
