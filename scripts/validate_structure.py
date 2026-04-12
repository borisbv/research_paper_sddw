import os
import sys
import argparse

def validate_structure(target_dir):
    print(f"Validating structure for target: {target_dir}...")
    required_dirs = ['sections', 'references', 'figures', 'data']
    base_path = target_dir
    
    if not os.path.exists(base_path):
        print(f"Error: Target directory '{target_dir}' not found.")
        sys.exit(1)
        
    errors = 0
    for d in required_dirs:
        path = os.path.join(base_path, d)
        if not os.path.exists(path):
            print(f"Missing directory: {path}")
            errors += 1
    
    # Check for core files
    core_files = ['metadata.yaml', 'outline.md']
    for f in core_files:
        path = os.path.join(base_path, f)
        if not os.path.exists(path):
            print(f"Missing core file: {path}")
            errors += 1
            
    if errors > 0:
        print(f"Validation failed with {errors} errors.")
        sys.exit(1)
    else:
        print("✅ Structure validated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='paper', help='Research directory (paper or book)')
    args = parser.parse_args()
    validate_structure(args.dir)
