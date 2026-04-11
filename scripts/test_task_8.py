import re
import os

def count_words(text):
    # Remove markdown comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remove markers like [Pendiente: ...]
    text = re.sub(r'\[.*?\]', '', text)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def test_task_8():
    with open('paper/manuscrito.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Abstract Spanish
    spanish_abstract_match = re.search(r'## Abstract\n\n(.*?)\n\n## Abstract \(English\)', content, re.DOTALL)
    if not spanish_abstract_match:
        print("FAIL: Spanish Abstract section not found or empty")
        return False
    
    spanish_abstract = spanish_abstract_match.group(1).strip()
    if "[Pendiente" in spanish_abstract:
        print(f"FAIL: Spanish Abstract is still pending: {spanish_abstract}")
        return False
    
    count_es = count_words(spanish_abstract)
    print(f"Spanish Abstract word count: {count_es}")
    if not (100 <= count_es <= 130):
        print(f"FAIL: Spanish Abstract word count {count_es} is not between 100 and 130")
        return False

    # Find Abstract English
    english_abstract_match = re.search(r'## Abstract \(English\)\n\n(.*?)\n\n---', content, re.DOTALL)
    if not english_abstract_match:
        print("FAIL: English Abstract section not found or empty")
        return False
    
    english_abstract = english_abstract_match.group(1).strip()
    if "[Pendiente" in english_abstract:
        print(f"FAIL: English Abstract is still pending: {english_abstract}")
        return False

    count_en = count_words(english_abstract)
    print(f"English Abstract word count: {count_en}")
    if not (100 <= count_en <= 130):
        print(f"FAIL: English Abstract word count {count_en} is not between 100 and 130")
        return False

    # Check keywords
    keywords_es = re.findall(r'\*\*Palabras clave\*\*: (.*)', content)
    if not keywords_es:
        print("FAIL: Spanish keywords not found")
        return False
    
    num_keywords_es = len(keywords_es[0].split(','))
    print(f"Number of Spanish keywords: {num_keywords_es}")
    if not (4 <= num_keywords_es <= 8):
        print(f"FAIL: Number of Spanish keywords {num_keywords_es} is not between 4 and 8")
        return False

    keywords_en = re.findall(r'\*\*Keywords\*\*: (.*)', content)
    if not keywords_en:
        print("FAIL: English keywords not found")
        return False
    
    num_keywords_en = len(keywords_en[0].split(','))
    print(f"Number of English keywords: {num_keywords_en}")
    if not (4 <= num_keywords_en <= 8):
        print(f"FAIL: Number of English keywords {num_keywords_en} is not between 4 and 8")
        return False

    print("PASS: Task 8 validation successful")
    return True

if __name__ == "__main__":
    if test_task_8():
        exit(0)
    else:
        exit(1)
