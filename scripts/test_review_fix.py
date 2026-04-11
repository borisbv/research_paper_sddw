import os
import sys

def check_abstract_length(file_path, min_words=200):
    if not os.path.exists(file_path):
        print(f"FAILED: {file_path} not found.")
        return False
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Simple word count (split by whitespace)
        words = content.split()
        count = len(words)
        if count < min_words:
            print(f"FAILED: Abstract too short ({count} words). Need at least {min_words}.")
            return False
        print(f"PASSED: Abstract length is {count} words.")
        return True

def check_figures(figure_dir, required_figures):
    missing = []
    for fig in required_figures:
        path = os.path.join(figure_dir, fig)
        if not os.path.exists(path):
            missing.append(fig)
    
    if missing:
        print(f"FAILED: Missing figures: {', '.join(missing)}")
        return False
    print("PASSED: All required figures exist.")
    return True

if __name__ == "__main__":
    abstract_path = "paper/sections/abstract.md"
    figure_dir = "figures"
    required_figures = [
        "graphical_abstract.png",
        "prisma_flowchart.png",
        "conceptual_framework.png",
        "comparison_matrix.png",
        "social_capital_functions.png"
    ]
    
    print("--- Running Review Fix Validation (RED) ---")
    abs_ok = check_abstract_length(abstract_path)
    fig_ok = check_figures(figure_dir, required_figures)
    
    if not abs_ok or not fig_ok:
        sys.exit(1)
    print("--- All tests passed! ---")
    sys.exit(0)
