import subprocess
import os

def render_quarto(format="pdf"):
    print(f"Rendering paper in {format} format using Quarto...")
    try:
        # Check if quarto is installed
        subprocess.run(["quarto", "--version"], check=True, capture_output=True)
        
        cmd = ["quarto", "render", "paper/outline.md", "--to", format, "--output", f"manuscript.{format}"]
        subprocess.run(cmd, check=True)
        print(f"Success: manuscript.{format} generated.")
    except Exception as e:
        print(f"Error: Quarto rendering failed. Make sure Quarto is installed. Details: {e}")

if __name__ == "__main__":
    render_quarto()
