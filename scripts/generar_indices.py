"""Genera índices derivados de la estructura longitudinal de entregas.

Este script solo escribe:

- ``entregas/alumnos.csv``;
- ``entregas/<alumno>/README.md``;
- ``docs/entregas_por_clase/clase_XX.md``.

Nunca modifica archivos dentro de una carpeta ``clase_XX``.
"""

from __future__ import annotations

import csv
import os
import re
import tempfile
from dataclasses import dataclass
from io import StringIO
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
ENTREGAS = RAIZ / "entregas"
CURSO = RAIZ / "curso"
INDICES = RAIZ / "docs" / "entregas_por_clase"
PATRON_ALUMNO = re.compile(r"^[a-z0-9_]+$")
PATRON_CLASE = re.compile(r"^clase_(\d{2})$")


@dataclass(frozen=True)
class MetadatosAlumno:
    nombre_mostrado: str
    nombres_encontrados: tuple[str, ...]
    usuario_github: str = ""


METADATOS: dict[str, MetadatosAlumno] = {
    "aristeo": MetadatosAlumno("Aristeo", ("Aristeo", "aristeo")),
    "arturo": MetadatosAlumno("Arturo", ("arturo",)),
    "daniel": MetadatosAlumno("Daniel", ("Daniel",)),
    "gustavo": MetadatosAlumno("Gustavo", ("Gustavo",)),
    "ivan": MetadatosAlumno("Ivan", ("ivan",)),
    "leo": MetadatosAlumno("Leo", ("LEO",)),
    "max": MetadatosAlumno("Max", ("max",)),
    "pato": MetadatosAlumno("Pato", ("Pato",)),
    "santiago_saldivar": MetadatosAlumno(
        "Santiago Saldivar", ("Santiago_Saldivar",)
    ),
    "santiago_vazquez": MetadatosAlumno(
        "Santiago Vazquez", ("Santiago_Vazquez",)
    ),
}


def _es_clase(ruta: Path) -> bool:
    return ruta.is_dir() and PATRON_CLASE.fullmatch(ruta.name) is not None


def _alumnos() -> list[Path]:
    alumnos = [ruta for ruta in ENTREGAS.iterdir() if ruta.is_dir()]
    invalidos = [ruta.name for ruta in alumnos if not PATRON_ALUMNO.fullmatch(ruta.name)]
    if invalidos:
        raise ValueError(f"Identificadores de alumno inválidos: {', '.join(invalidos)}")
    return sorted(alumnos, key=lambda ruta: ruta.name)


def _clases_de(alumno: Path) -> list[Path]:
    return sorted(
        (ruta for ruta in alumno.iterdir() if _es_clase(ruta)),
        key=lambda ruta: ruta.name,
    )


def _metadatos(identificador: str) -> MetadatosAlumno:
    return METADATOS.get(
        identificador,
        MetadatosAlumno(identificador.replace("_", " ").title(), (identificador,)),
    )


def _escribir_atomico(destino: Path, contenido: str) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=destino.parent, delete=False
    ) as temporal:
        temporal.write(contenido)
        nombre_temporal = temporal.name
    os.replace(nombre_temporal, destino)


def _generar_csv(alumnos: list[Path]) -> None:
    salida = StringIO()
    escritor = csv.writer(salida, lineterminator="\n")
    escritor.writerow(
        [
            "id",
            "nombre_mostrado",
            "usuario_github",
            "nombres_encontrados",
            "clases",
        ]
    )
    for alumno in alumnos:
        datos = _metadatos(alumno.name)
        clases = [ruta.name for ruta in _clases_de(alumno)]
        escritor.writerow(
            [
                alumno.name,
                datos.nombre_mostrado,
                datos.usuario_github,
                ";".join(datos.nombres_encontrados),
                ";".join(clases),
            ]
        )
    _escribir_atomico(ENTREGAS / "alumnos.csv", salida.getvalue())


def _generar_readme_alumno(alumno: Path) -> None:
    datos = _metadatos(alumno.name)
    clases = _clases_de(alumno)
    github = datos.usuario_github or "No identificado"
    enlaces = "\n".join(
        f"- [Clase {clase.name[-2:]}]({clase.name}/)" for clase in clases
    )
    contenido = f"""<!-- Generado por scripts/generar_indices.py -->
# Entregas de {datos.nombre_mostrado}

- **Identificador:** `{alumno.name}`
- **Nombre mostrado:** {datos.nombre_mostrado}
- **Usuario de GitHub:** {github}
- **Total de entregas:** {len(clases)}

## Clases entregadas

{enlaces}

> [!NOTE]
> El contenido enlazado corresponde al trabajo entregado durante el curso. Este
> índice no contiene evaluaciones ni un resumen de desempeño.
"""
    _escribir_atomico(alumno / "README.md", contenido)


def _contar_archivos(ruta: Path) -> int:
    return sum(1 for archivo in ruta.rglob("*") if archivo.is_file())


def _clases_conocidas(alumnos: list[Path]) -> list[str]:
    clases = {ruta.name for ruta in CURSO.iterdir() if _es_clase(ruta)}
    for alumno in alumnos:
        clases.update(ruta.name for ruta in _clases_de(alumno))
    return sorted(clases)


def _generar_indice_clase(clase: str, alumnos: list[Path]) -> None:
    filas: list[str] = []
    for alumno in alumnos:
        entrega = alumno / clase
        if not entrega.is_dir():
            continue
        datos = _metadatos(alumno.name)
        ruta = f"../../entregas/{alumno.name}/{clase}/"
        filas.append(
            f"| {datos.nombre_mostrado} | [Abrir entrega]({ruta}) | "
            f"{_contar_archivos(entrega)} |"
        )

    numero = clase[-2:]
    tabla = "\n".join(filas) if filas else "| — | — | 0 |"
    contenido = f"""<!-- Generado por scripts/generar_indices.py -->
# Entregas de la Clase {numero}

| Alumno | Ruta | Archivos |
|---|---|---:|
{tabla}
"""
    _escribir_atomico(INDICES / f"{clase}.md", contenido)


def main() -> int:
    if not ENTREGAS.is_dir() or not CURSO.is_dir():
        raise SystemExit("Deben existir las carpetas curso/ y entregas/.")

    alumnos = _alumnos()
    _generar_csv(alumnos)
    for alumno in alumnos:
        _generar_readme_alumno(alumno)
    clases = _clases_conocidas(alumnos)
    for clase in clases:
        _generar_indice_clase(clase, alumnos)

    print(f"Alumnos indexados: {len(alumnos)}")
    print(f"Clases indexadas: {len(clases)}")
    print(f"Entregas indexadas: {sum(len(_clases_de(a)) for a in alumnos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

