import os
import re

def test_task_5_2():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if section 4.2 Results: Context of Use is written
    # Use a more flexible regex for the headers
    section_match = re.search(r"### 4\.2 Contexto de uso.*?\n(.*?)(?=### 4\.3)", content, re.DOTALL)
    if not section_match:
        # Try without the dotall or with different markers
        print("DEBUG: Could not find section 4.2 with primary regex")
        # print(f"DEBUG: Content after 4.2 header: {content[content.find('### 4.2'):content.find('### 4.2')+500]}")
    
    assert section_match, "Section 4.2 Context of Use not found"
    section_content = section_match.group(1).strip()
    print(f"DEBUG: captured content length: {len(section_content)}")
    # print(f"DEBUG: captured content start: {section_content[:200]}...")
    
    assert "[Pendiente]" not in section_content, "Section 4.2 still contains [Pendiente] marker"
    
    # Word count check (~700 words)
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    total_words = count_words(section_content)
    print(f"Section 4.2 word count: {total_words}")
    assert 600 <= total_words <= 800, f"Section 4.2 word count should be around 700, found {total_words}"
    
    # Check for specific topics
    # print(f"DEBUG: whole content: {section_content}")
    import re as regex
    match = regex.search(r"Dedecek Gertz y .*? \(2022\)", section_content)
    if match:
        print(f"DEBUG: found citation: {match.group(0)}")
    else:
        print("DEBUG: citation not found with regex")
    assert "WhatsApp" in section_content, "Missing WhatsApp"
    assert "YouTube" in section_content, "Missing YouTube"
    assert "salud" in section_content.lower(), "Missing salud"
    assert "educación" in section_content.lower(), "Missing educación"
    assert "seguridad" in section_content.lower(), "Missing seguridad"
    assert "movilidad" in section_content.lower(), "Missing movilidad"
    
    # Check for specific citations
    assert re.search(r"Dedecek Gertz y S[uü][\s\S]er,?\s?2022", section_content), "Missing Dedecek Gertz y Süßer (2022)"
    assert "Haythornthwaite, 2002" in section_content or "Haythornthwaite (2002)" in section_content, "Missing Haythornthwaite (2002)"
    assert "Zhao" in section_content, "Missing Zhao"
    
    # Check for specific concepts
    assert "vínculos latentes" in section_content.lower(), "Missing vínculos latentes"
    assert "silos informativos" in section_content.lower(), "Missing silos informativos"
    
    print("Task 5.2: Results (Context of Use) validation passed!")

if __name__ == "__main__":
    try:
        test_task_5_2()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
