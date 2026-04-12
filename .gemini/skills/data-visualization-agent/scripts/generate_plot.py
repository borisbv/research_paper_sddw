import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import os
import json

def generate_plot(data_path, output_path, config_path=None):
    if not os.path.exists(data_path):
        print(f"Error: Data file {data_path} not found.")
        return

    df = pd.read_csv(data_path)
    
    # Load theme if available
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            theme = json.load(f)
            sns.set_theme(**theme.get('sns_theme', {}))
    else:
        sns.set_theme(style="whitegrid")

    # Basic plot generation (default to barplot for simplicity, extend as needed)
    # This is a generic generator that can be customized via prompts
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Success: Plot saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate academic plots from CSV data.')
    parser.add_argument('--data', required=True, help='Path to CSV data file')
    parser.add_argument('--out', required=True, help='Path to output image file')
    parser.add_argument('--config', help='Path to theme config JSON')
    args = parser.parse_args()
    generate_plot(args.data, args.out, args.config)
