"""Valida la organización del repositorio sin modificar archivos."""

from __future__ import annotations

import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
CURSO = RAIZ / "curso"
ENTREGAS = RAIZ / "entregas"
INDICES = RAIZ / "docs" / "entregas_por_clase"
PATRON_CLASE = re.compile(r"^clase_(\d{2})$")
PATRON_ALUMNO = re.compile(r"^[a-z0-9_]+$")
PATRON_ENLACE = re.compile(r"\]\((\.\./\.\./entregas/[^)]+)\)")
PATRON_ENTREGA_ANTIGUA = re.compile(r"entregas/clase_\d{2}")
PATRON_CLASE_FUNCIONAL_ANTIGUA = re.compile(
    r"(?<![A-Za-z0-9_/])clase_\d{2}/(?:tests|requirements\.txt|src|notebooks)"
)
EXTENSIONES_TEXTO = {".md", ".py", ".ini", ".toml", ".ipynb", ".html"}


def _clases_en(ruta: Path) -> list[Path]:
    if not ruta.is_dir():
        return []
    return sorted(
        (
            elemento
            for elemento in ruta.iterdir()
            if elemento.is_dir() and PATRON_CLASE.fullmatch(elemento.name)
        ),
        key=lambda elemento: elemento.name,
    )


def _validar_enlaces(errores: list[str]) -> None:
    if not INDICES.is_dir():
        errores.append("No existe docs/entregas_por_clase/.")
        return
    for indice in sorted(INDICES.glob("clase_*.md")):
        texto = indice.read_text(encoding="utf-8")
        for enlace in PATRON_ENLACE.findall(texto):
            destino = (indice.parent / enlace).resolve()
            if not destino.is_dir():
                errores.append(f"Enlace roto en {indice.relative_to(RAIZ)}: {enlace}")


def _validar_referencias(errores: list[str]) -> None:
    for base in (CURSO, RAIZ / "scripts"):
        if not base.is_dir():
            continue
        for archivo in base.rglob("*"):
            if not archivo.is_file() or archivo.suffix.lower() not in EXTENSIONES_TEXTO:
                continue
            try:
                texto = archivo.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            relativa = archivo.relative_to(RAIZ)
            if PATRON_ENTREGA_ANTIGUA.search(texto):
                errores.append(f"Referencia antigua de entregas en {relativa}")
            if PATRON_CLASE_FUNCIONAL_ANTIGUA.search(texto):
                errores.append(f"Referencia funcional antigua de clase en {relativa}")


def _temporales() -> list[Path]:
    encontrados: list[Path] = []
    for ruta in RAIZ.rglob("*"):
        if ".git" in ruta.parts:
            continue
        if ruta.name in {".DS_Store", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}:
            encontrados.append(ruta)
        elif ruta.is_file() and ruta.suffix == ".pyc":
            encontrados.append(ruta)
    return sorted(set(encontrados))


def main() -> int:
    errores: list[str] = []
    clases = _clases_en(CURSO)
    if len(clases) != 20:
        errores.append(f"Se esperaban 20 clases en curso/ y se encontraron {len(clases)}.")

    clases_en_raiz = _clases_en(RAIZ)
    if clases_en_raiz:
        errores.append("Persisten clases antiguas en la raíz: " + ", ".join(r.name for r in clases_en_raiz))

    alumnos = sorted((ruta for ruta in ENTREGAS.iterdir() if ruta.is_dir()), key=lambda r: r.name)
    entregas = 0
    for alumno in alumnos:
        if not PATRON_ALUMNO.fullmatch(alumno.name):
            errores.append(f"Identificador de alumno inválido: {alumno.name}")
        clases_alumno = _clases_en(alumno)
        entregas += len(clases_alumno)
        extras = [
            ruta.name
            for ruta in alumno.iterdir()
            if ruta.is_dir() and not PATRON_CLASE.fullmatch(ruta.name)
        ]
        if extras:
            errores.append(f"Carpetas inesperadas en entregas/{alumno.name}: {', '.join(extras)}")

    legadas = [ruta.name for ruta in _clases_en(ENTREGAS)]
    if legadas:
        errores.append("Persisten carpetas entrega/clase_XX: " + ", ".join(legadas))

    for temporal in _temporales():
        errores.append(f"Archivo temporal: {temporal.relative_to(RAIZ)}")

    _validar_enlaces(errores)
    _validar_referencias(errores)

    print(f"Clases: {len(clases)}")
    print(f"Alumnos: {len(alumnos)}")
    print(f"Entregas: {entregas}")
    if errores:
        print("Errores estructurales:")
        for error in errores:
            print(f"- {error}")
        return 1

    print("Estructura válida.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

