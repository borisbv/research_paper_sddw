import os
import glob
import argparse

def count_words(target_dir):
    print(f"Counting words for target: {target_dir}...")
    path = os.path.join(target_dir, "sections", "*.md")
    files = glob.glob(path)
    total = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            words = len(file.read().split())
            print(f"{os.path.basename(f)}: {words} words")
            total += words
    print(f"--- Total: {total} words ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='paper', help='Research directory (paper or book)')
    args = parser.parse_args()
    count_words(args.dir)