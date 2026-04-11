import os
import re

def test_task_7():
    file_path = "paper/manuscrito.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check Section 6.1
    section_6_1_match = re.search(r"### 6\.1 Respuesta a la pregunta de investigación, contribución y líneas futuras.*?(\n.*?)(?=\n---|\n#|$)", content, re.DOTALL)
    assert section_6_1_match, "Section 6.1 Conclusion not found"
    section_6_1_content = section_6_1_match.group(1).strip()
    
    if "[Pendiente]" in section_6_1_content:
        print("Section 6.1 is [Pendiente]")
        assert False, "Section 6.1 still contains [Pendiente] marker"
    
    def count_words(text):
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        text = re.sub(r'^#+\s.*$', '', text, flags=re.MULTILINE)
        return len(text.split())

    words_6_1 = count_words(section_6_1_content)
    print(f"Section 6.1 word count: {words_6_1}")
    # Target is ~600, so we check between 500 and 700
    assert 500 <= words_6_1 <= 750, f"Section 6.1 word count should be around 600, found {words_6_1}"

    # Check for content in 7.1
    print(f"Content for assertions (lowercase):\n{section_6_1_content.lower()[:500]}...")
    
    assert "pregunta de investigación" in section_6_1_content.lower(), "Missing 'pregunta de investigación'"
    assert "contribución" in section_6_1_content.lower(), "Missing 'contribución'"
    assert "futura" in section_6_1_content.lower(), "Missing 'futura'"
    assert "resignifican" in section_6_1_content.lower(), "Missing 'resignifican'"
    assert "marco analítico" in section_6_1_content.lower(), "Missing 'marco analítico'"
    assert "categorías" in section_6_1_content.lower(), "Missing 'categorías'"

    print("Task 7: Conclusion validation passed!")

if __name__ == "__main__":
    try:
        test_task_7()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
