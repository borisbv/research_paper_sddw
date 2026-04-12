import os
import argparse
from PIL import Image

def optimize_figures(target_dir):
    figures_dir = os.path.join(target_dir, "figures")
    if not os.path.exists(figures_dir):
        return

    for filename in os.listdir(figures_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            path = os.path.join(figures_dir, filename)
            try:
                with Image.open(path) as img:
                    # Professional scientific standard: 300 DPI
                    if img.info.get('dpi') != (300, 300):
                        print(f"Optimizing {filename} to 300 DPI...")
                        img.save(path, dpi=(300, 300))
                    else:
                        print(f"{filename} is already at 300 DPI.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    args = parser.parse_args()
    optimize_figures(args.dir)
