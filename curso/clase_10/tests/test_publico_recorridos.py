"""Pruebas públicas guiadas para recorridos de grafos.

Estas pruebas son retroalimentación visible. No cubren todos los casos y
contienen espacios TODO para que cada estudiante diseñe pruebas propias.
"""

from __future__ import annotations

from importlib import import_module

import pytest


def cargar_modulo():
    """Carga la implementación del estudiante o el código base."""

    try:
        return import_module("implementacion")
    except ModuleNotFoundError:
        return import_module("src.recorridos")


modulo = cargar_modulo()
ES_CODIGO_BASE = modulo.__name__ == "src.recorridos"


def requiere_implementacion() -> None:
    """Omite pruebas de comportamiento cuando solo está el stub público."""

    if ES_CODIGO_BASE:
        pytest.skip("El código base no contiene implementación completa")


def grafo_clase() -> dict[str, list[str]]:
    """Grafo pequeño usado para recorridos manuales."""

    return {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }


def test_existen_funciones_requeridas():
    assert hasattr(modulo, "bfs")
    assert hasattr(modulo, "dfs")
    assert hasattr(modulo, "registrar_bfs")
    assert hasattr(modulo, "registrar_dfs")
    assert hasattr(modulo, "guardar_visualizacion_recorrido")


def test_bfs_en_grafo_simple():
    requiere_implementacion()
    assert modulo.bfs(grafo_clase(), "A") == ["A", "B", "C", "D", "E", "F"]


def test_dfs_en_grafo_simple():
    requiere_implementacion()
    assert modulo.dfs(grafo_clase(), "A") == ["A", "B", "D", "E", "C", "F"]


def test_bfs_en_grafo_con_ciclo():
    requiere_implementacion()
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
        "D": ["C"],
    }
    assert modulo.bfs(grafo, "A") == ["A", "B", "C", "D"]


def test_dfs_en_grafo_con_ciclo():
    requiere_implementacion()
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
        "D": ["C"],
    }
    assert modulo.dfs(grafo, "A") == ["A", "B", "C", "D"]


def test_grafo_desconectado_solo_visita_componente_del_origen():
    requiere_implementacion()
    grafo = {
        "A": ["B"],
        "B": ["A"],
        "X": ["Y"],
        "Y": ["X"],
    }
    assert modulo.bfs(grafo, "A") == ["A", "B"]
    assert modulo.dfs(grafo, "A") == ["A", "B"]


def test_registro_bfs_contiene_cola():
    requiere_implementacion()
    registro = modulo.registrar_bfs(grafo_clase(), "A")
    assert registro
    assert "cola" in registro[0]
    assert "linea_pseudocodigo" in registro[0]


def test_registro_dfs_contiene_pila():
    requiere_implementacion()
    registro = modulo.registrar_dfs(grafo_clase(), "A")
    assert registro
    assert "pila" in registro[0]
    assert "linea_pseudocodigo" in registro[0]


def test_bfs_encuentra_camino_en_red_no_ponderada():
    requiere_implementacion()
    grafo = {
        "1": ["2", "3"],
        "2": ["1", "4"],
        "3": ["1", "4"],
        "4": ["2", "3", "5"],
        "5": ["4"],
    }
    recorrido = modulo.bfs(grafo, "1")
    assert recorrido.index("4") < recorrido.index("5")


@pytest.mark.skip(reason="TODO alumno: diseña una prueba donde BFS y DFS tengan órdenes distintos.")
def test_todo_bfs_y_dfs_ordenes_distintos():
    """TODO alumno: usa un grafo donde BFS y DFS visiten en orden diferente.

    Pista: el grafo de clase con ramas desde A funciona bien.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para un nodo aislado.")
def test_todo_nodo_aislado():
    """TODO alumno: prueba un grafo con un solo nodo sin vecinos.

    Pista: ``{\"A\": []}`` debería regresar ``[\"A\"]`` para BFS y DFS.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: verifica que no se visitan nodos repetidos.")
def test_todo_no_visita_repetidos():
    """TODO alumno: usa un grafo con ciclo y revisa que no haya duplicados.

    Pista: compara ``len(recorrido)`` con ``len(set(recorrido))``.
    """

    assert False
