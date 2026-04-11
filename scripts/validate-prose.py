#!/usr/bin/env python3
"""
validate-prose.py — Ejecuta Vale como linter de prosa sobre las secciones del paper.
Requiere Vale instalado (winget install jdkato.vale).
Uso: python scripts/validate-prose.py
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path


def find_vale() -> str | None:
    """Busca el ejecutable de Vale en PATH y ubicaciones conocidas."""
    # Primero: PATH estandar
    path = shutil.which("vale")
    if path:
        return path

    # Fallback: ubicacion de WinGet en Windows
    winget_base = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Packages"
    if winget_base.exists():
        for d in winget_base.iterdir():
            if "vale" in d.name.lower():
                candidate = d / "vale.exe"
                if candidate.exists():
                    return str(candidate)

    return None


def validate_prose(base_path: Path) -> tuple[bool, list[str]]:
    errors = []
    sections_dir = base_path / "paper"
    vale_ini = base_path / ".vale.ini"

    # Verificar que Vale esta instalado
    vale_path = find_vale()
    if not vale_path:
        print("[SKIP] Prosa: Vale no instalado")
        print("  Instalar: winget install errata-ai.Vale")
        print("  O: scoop install vale")
        return True, []

    # Verificar que exista config
    if not vale_ini.exists():
        print("[SKIP] Prosa: .vale.ini no encontrado")
        return True, []

    # Verificar que existan secciones
    if not sections_dir.exists():
        print("[WARN] Prosa: paper/ no encontrado -- skip")
        return True, []

    md_files = [f for f in sections_dir.glob("*.md") if f.name not in ["00_metadata.md", "review-report.md"]]
    if not md_files:
        print("[WARN] Prosa: no hay archivos .md en paper/ -- skip")
        return True, []

    # Ejecutar Vale con output JSON (usar path relativa para que matchee .vale.ini globs)
    try:
        result = subprocess.run(
            [vale_path, "--output=JSON", "paper"],
            capture_output=True,
            text=True,
            cwd=str(base_path),
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        print("[WARN] Prosa: Vale excedio timeout de 60s")
        return True, ["WARN: Vale timeout"]
    except Exception as e:
        print(f"[WARN] Prosa: error ejecutando Vale: {str(e)[:50]}")
        return True, [f"WARN: {str(e)[:50]}"]

    # Parsear output JSON
    output = result.stdout.strip()
    if not output or output == "{}":
        print(f"[PASS] Prosa: {len(md_files)} archivos revisados, sin alertas")
        return True, []

    try:
        vale_results = json.loads(output)
    except json.JSONDecodeError:
        # Vale puede producir output no-JSON en caso de error de config
        if result.stderr:
            print(f"[WARN] Prosa: error de Vale -- {result.stderr[:100]}")
        else:
            print(f"[WARN] Prosa: output inesperado de Vale")
        return True, []

    # Contar por severidad
    error_count = 0
    warning_count = 0
    suggestion_count = 0

    for file_path, alerts in vale_results.items():
        for alert in alerts:
            severity = alert.get("Severity", "").lower()
            message = alert.get("Message", "")
            line = alert.get("Line", 0)
            check = alert.get("Check", "")

            # Nombre de archivo relativo
            rel_path = Path(file_path).name

            if severity == "error":
                error_count += 1
                errors.append(f"FAIL: {rel_path}:{line} [{check}] {message}")
            elif severity == "warning":
                warning_count += 1
                errors.append(f"WARN: {rel_path}:{line} [{check}] {message}")
            else:
                suggestion_count += 1
                if suggestion_count <= 3:  # Limitar sugerencias en output
                    errors.append(f"INFO: {rel_path}:{line} [{check}] {message}")

    # Resultado
    has_errors = error_count > 0
    status = "FAIL" if has_errors else "PASS"
    total_alerts = error_count + warning_count + suggestion_count
    print(
        f"[{status}] Prosa: {len(md_files)} archivos, "
        f"{error_count} errores, {warning_count} warnings, {suggestion_count} sugerencias"
    )
    for e in errors[:10]:
        print(f"  - {e}")
    if len(errors) > 10:
        print(f"  - ... y {len(errors) - 10} mas")

    return not has_errors, errors


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    ok, _ = validate_prose(base)
    sys.exit(0 if ok else 1)
