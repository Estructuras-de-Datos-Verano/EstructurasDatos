"""Ejecuta pruebas públicas sobre una entrega del curso.

Uso:

    python3 evaluar.py entregas/clase_11/nombre clase_11/tests

El script agrega temporalmente la carpeta de entrega al ``PYTHONPATH`` para
que los tests puedan importar directamente ``implementacion.py``.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    """Punto de entrada del evaluador."""

    if len(sys.argv) != 3:
        print("Uso: python3 evaluar.py <carpeta_entrega> <carpeta_tests>")
        return 2

    carpeta_entrega = Path(sys.argv[1]).resolve()
    carpeta_tests = Path(sys.argv[2]).resolve()
    implementacion = carpeta_entrega / "implementacion.py"

    if not carpeta_entrega.exists() or not carpeta_entrega.is_dir():
        print(f"No existe la carpeta de entrega: {carpeta_entrega}")
        return 2
    if not carpeta_tests.exists() or not carpeta_tests.is_dir():
        print(f"No existe la carpeta de tests: {carpeta_tests}")
        return 2
    if not implementacion.exists():
        print(f"No se encontró implementacion.py en: {carpeta_entrega}")
        return 2

    env = os.environ.copy()
    rutas = [str(carpeta_entrega)]
    if env.get("PYTHONPATH"):
        rutas.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(rutas)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    comando = [sys.executable, "-m", "pytest", "-v", str(carpeta_tests)]
    print("Ejecutando:", flush=True)
    print(" ".join(comando), flush=True)
    print(flush=True)

    resultado = subprocess.run(comando, env=env, check=False)
    return resultado.returncode


if __name__ == "__main__":
    raise SystemExit(main())
