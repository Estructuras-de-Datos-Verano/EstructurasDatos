"""Ejecuta pruebas públicas y opcionales sobre una entrega del curso.

Uso general:

    python3 scripts/evaluar.py <carpeta_entrega> <tests_publicos> [tests_extra]

Ejemplo macOS / Linux:

    python3 scripts/evaluar.py entregas/max/clase_12 curso/clase_12/tests
    python3 scripts/evaluar.py entregas/max/clase_12 curso/clase_12/tests entregas/leo/clase_12/test_estudiante.py

Ejemplo Windows PowerShell:

    py scripts/evaluar.py entregas/max/clase_12 curso/clase_12/tests
    python scripts/evaluar.py entregas/max/clase_12 curso/clase_12/tests

El script agrega temporalmente la carpeta de entrega al entorno de Python para
que los tests puedan importar directamente ``implementacion.py``.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def _validar_ruta_tests(ruta: Path, nombre: str) -> bool:
    """Regresa True si ``ruta`` existe como archivo o carpeta de pruebas."""

    if ruta.exists():
        return True
    print(f"No existe {nombre}: {ruta}")
    return False


def main() -> int:
    """Punto de entrada del evaluador."""

    if len(sys.argv) not in (3, 4):
        print("Uso: python3 scripts/evaluar.py <carpeta_entrega> <tests_publicos> [tests_extra]")
        return 2

    carpeta_entrega = Path(sys.argv[1]).resolve()
    tests_publicos = Path(sys.argv[2]).resolve()
    tests_extra = Path(sys.argv[3]).resolve() if len(sys.argv) == 4 else None
    implementacion = carpeta_entrega / "implementacion.py"

    if not carpeta_entrega.exists() or not carpeta_entrega.is_dir():
        print(f"No existe la carpeta de entrega: {carpeta_entrega}")
        return 2
    if not implementacion.exists():
        print(f"No se encontró implementacion.py en: {carpeta_entrega}")
        return 2
    if not _validar_ruta_tests(tests_publicos, "la carpeta de tests públicos"):
        return 2
    if tests_extra is not None and not _validar_ruta_tests(tests_extra, "tests_extra"):
        return 2

    env = os.environ.copy()
    rutas = [str(carpeta_entrega)]
    if env.get("PYTHONPATH"):
        rutas.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(rutas)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    objetivos = [str(tests_publicos)]
    if tests_extra is not None:
        objetivos.append(str(tests_extra))

    comando = [sys.executable, "-m", "pytest", "-v", *objetivos]
    print("Ejecutando:", flush=True)
    print(" ".join(comando), flush=True)
    print(flush=True)

    resultado = subprocess.run(comando, env=env, check=False)
    return resultado.returncode


if __name__ == "__main__":
    raise SystemExit(main())
