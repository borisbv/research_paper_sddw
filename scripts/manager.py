import argparse
import sys
import subprocess
import os

def run_script(script_name, args):
    script_path = os.path.join("scripts", script_name)
    cmd = [sys.executable, script_path] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def main():
    parser = argparse.ArgumentParser(description='Research Engine Management CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Init
    init_parser = subparsers.add_parser('init', help='Initialize research target')
    init_parser.add_argument('type', choices=['paper', 'book'], help='Type of research')

    # Validate
    val_parser = subparsers.add_parser('validate', help='Run all validations')
    val_parser.add_argument('--dir', required=True, help='Research directory')

    # Render
    render_parser = subparsers.add_parser('render', help='Render manuscript')
    render_parser.add_argument('--dir', required=True, help='Research directory')
    render_parser.add_argument('--format', default='pdf', help='Output format')

    # Sync Bibliography
    sync_parser = subparsers.add_parser('sync', help='Sync bibliography from external sources')
    sync_parser.add_argument('--dir', required=True, help='Research directory')

    # Sync Outline
    subparsers.add_parser('sync-outline', help='Create section files from outline').add_argument('--dir', required=True)

    # Enrich Bib
    subparsers.add_parser('enrich-bib', help='Complete BibTeX metadata using DOIs').add_argument('--dir', required=True)

    # Optimize Figures
    subparsers.add_parser('optimize-figs', help='Set all figures to 300 DPI').add_argument('--dir', required=True)

    # Package Submission
    subparsers.add_parser('package', help='Create an anonymized submission ZIP').add_argument('--dir', required=True)

    # Test
    subparsers.add_parser('test', help='Run framework tests')

    args = parser.parse_args()

    if args.command == 'init':
        stdout, stderr, code = run_script("research_init.py", [args.type])
        print(stdout or stderr)

    elif args.command == 'validate':
        print(f"--- Running Full Validation for {args.dir} ---")
        scripts = ["validate_structure.py", "validate_citations.py", "validate_figure_sync.py", "validate_word_count.py"]
        for s in scripts:
            stdout, stderr, code = run_script(s, ["--dir", args.dir])
            print(f"[{s}]: {'✅ PASS' if code == 0 else '❌ FAIL'}")
            if code != 0: print(stdout or stderr)

        # Style Linting (Vale)
        print("\n--- Running Academic Style Linting (Vale) ---")
        try:
            val_res = subprocess.run(["vale", args.dir], capture_output=True, text=True)
            if val_res.returncode == 0:
                print("✅ Prose style validated.")
            else:
                print(val_res.stdout)
        except FileNotFoundError:
            print("⚠️ Vale not installed. Skipping prose linting.")

    elif args.command == 'render':
        stdout, stderr, code = run_script("quarto_render.py", ["--dir", args.dir, "--format", args.format])
        print(stdout or stderr)

    elif args.command == 'sync':
        stdout, stderr, code = run_script("sync_zotero.py", ["--dir", args.dir])
        print(stdout or stderr)

    elif args.command == 'sync-outline':
        stdout, stderr, code = run_script("sync_outline.py", ["--dir", args.dir])
        print(stdout or stderr)

    elif args.command == 'enrich-bib':
        stdout, stderr, code = run_script("enrich_bib.py", ["--dir", args.dir])
        print(stdout or stderr)

    elif args.command == 'optimize-figs':
        stdout, stderr, code = run_script("optimize_figures.py", ["--dir", args.dir])
        print(stdout or stderr)

    elif args.command == 'package':
        stdout, stderr, code = run_script("package_submission.py", ["--dir", args.dir])
        print(stdout or stderr)

    elif args.command == 'test':
        print("--- Running Framework Tests with Coverage (pytest) ---")
        result = subprocess.run([sys.executable, "-m", "pytest", "--cov=scripts", "tests/"], capture_output=False)
        sys.exit(result.returncode)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()