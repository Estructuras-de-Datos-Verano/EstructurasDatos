"""Pruebas públicas de la Clase 19.

Se ejecutan contra ``implementacion.py`` en la carpeta de entrega.
"""

from __future__ import annotations

from copy import deepcopy

import pytest

from implementacion import (
    es_orden_topologico,
    grados_entrada,
    normalizar_grafo_dirigido,
    orden_topologico,
    ordenar_cursos,
    puede_completar_cursos,
)


def validar_orden_cursos(numero: int, aristas: list[tuple[int, int]], orden: list[int]) -> None:
    assert len(orden) == numero
    assert set(orden) == set(range(numero))
    posicion = {curso: indice for indice, curso in enumerate(orden)}
    assert all(posicion[antes] < posicion[despues] for antes, despues in set(aristas))


def test_normalizar_vacio():
    assert normalizar_grafo_dirigido({}) == {}


def test_normalizar_copia_defensiva_y_no_comparte_listas():
    entrada = {"A": ["B"]}
    salida = normalizar_grafo_dirigido(entrada)
    assert salida == {"A": ["B"], "B": []}
    assert salida["A"] is not entrada["A"]
    salida["A"].append("C")
    assert entrada == {"A": ["B"]}


def test_normalizar_vecino_implicito_y_aislado():
    assert normalizar_grafo_dirigido({"A": ["B"], "Z": []}) == {
        "A": ["B"], "B": [], "Z": []
    }


def test_normalizar_elimina_duplicados_establemente():
    assert normalizar_grafo_dirigido({"A": ["B", "B", "C", "B"]}) == {
        "A": ["B", "C"], "B": [], "C": []
    }


def test_normalizar_conserva_orden_de_primera_aparicion():
    assert list(normalizar_grafo_dirigido({"A": ["C"], "B": []})) == ["A", "C", "B"]


@pytest.mark.parametrize("grafo", [[("A", ["B"])], "AB", 3, None])
def test_normalizar_rechaza_grafo_que_no_es_mapping(grafo):
    with pytest.raises(TypeError):
        normalizar_grafo_dirigido(grafo)


def test_normalizar_rechaza_nodo_no_string():
    with pytest.raises(TypeError):
        normalizar_grafo_dirigido({1: ["A"]})


def test_normalizar_rechaza_vecino_no_string():
    with pytest.raises(TypeError):
        normalizar_grafo_dirigido({"A": [1]})


@pytest.mark.parametrize("vecinos", ["B", 3, None, {"B"}])
def test_normalizar_rechaza_adyacencia_invalida(vecinos):
    with pytest.raises(TypeError):
        normalizar_grafo_dirigido({"A": vecinos})


def test_normalizar_acepta_tuplas_y_no_muta():
    entrada = {"A": ("B", "C"), "C": ()}
    copia = deepcopy(entrada)
    assert normalizar_grafo_dirigido(entrada) == {"A": ["B", "C"], "B": [], "C": []}
    assert entrada == copia


def test_grados_vacio():
    assert grados_entrada({}) == {}


def test_grados_cadena():
    assert grados_entrada({"A": ["B"], "B": ["C"]}) == {"A": 0, "B": 1, "C": 1}


def test_grados_varias_fuentes():
    assert grados_entrada({"A": ["C"], "B": ["C"], "C": ["D"]}) == {
        "A": 0, "C": 2, "B": 0, "D": 1
    }


def test_grados_vecino_implicito_duplicados_y_aislado():
    assert grados_entrada({"A": ["B", "B"], "Z": []}) == {"A": 0, "B": 1, "Z": 0}


def test_orden_vacio():
    assert orden_topologico({}) == []


def test_orden_un_nodo():
    assert orden_topologico({"A": []}) == ["A"]


def test_orden_cadena():
    assert orden_topologico({"A": ["B"], "B": ["C"]}) == ["A", "B", "C"]


def test_orden_varias_fuentes_y_varios_ordenes():
    grafo = {"A": ["C"], "B": ["C"], "C": ["D"]}
    orden = orden_topologico(grafo)
    assert orden is not None and es_orden_topologico(grafo, orden)
    assert es_orden_topologico(grafo, ["B", "A", "C", "D"])


def test_orden_ciclo_simple():
    assert orden_topologico({"A": ["B"], "B": ["C"], "C": ["A"]}) is None


def test_orden_ciclo_parcial_no_devuelve_prefijo():
    grafo = {"D": ["E"], "A": ["B"], "B": ["C"], "C": ["A"]}
    assert orden_topologico(grafo) is None


def test_orden_autoarista():
    assert orden_topologico({"A": ["A"]}) is None


def test_orden_desconectado_aciclico_y_aislado():
    grafo = {"A": ["B"], "X": ["Y"], "Z": []}
    orden = orden_topologico(grafo)
    assert orden is not None and es_orden_topologico(grafo, orden)


def test_orden_vecino_implicito_y_duplicado():
    grafo = {"A": ["B", "B"]}
    assert orden_topologico(grafo) == ["A", "B"]


def test_orden_no_muta_entrada():
    entrada = {"A": ["B"], "B": []}
    copia = deepcopy(entrada)
    orden_topologico(entrada)
    assert entrada == copia


def test_validacion_orden_principal_y_alternativo():
    grafo = {"A": ["C"], "B": ["C"]}
    assert es_orden_topologico(grafo, ["A", "B", "C"])
    assert es_orden_topologico(grafo, ["B", "A", "C"])


@pytest.mark.parametrize(
    "orden",
    [
        ["C", "A", "B"],
        ["A", "C"],
        ["A", "A", "C"],
        ["A", "B", "X"],
        ["A", "B", "C", "X"],
    ],
)
def test_validacion_rechaza_ordenes_invalidos(orden):
    assert not es_orden_topologico({"A": ["C"], "B": ["C"]}, orden)


def test_validacion_grafo_ciclico_no_acepta_orden():
    assert not es_orden_topologico({"A": ["B"], "B": ["A"]}, ["A", "B"])


def test_cursos_cero_y_uno():
    assert ordenar_cursos(0, []) == []
    assert ordenar_cursos(1, []) == [0]


def test_cursos_sin_prerrequisitos_incluye_todos():
    assert ordenar_cursos(4, []) == [0, 1, 2, 3]


def test_cursos_cadena():
    assert ordenar_cursos(4, [(0, 1), (1, 2), (2, 3)]) == [0, 1, 2, 3]


def test_cursos_varias_dependencias_y_orden_no_unico():
    aristas = [(0, 2), (1, 2), (2, 3)]
    orden = ordenar_cursos(4, aristas)
    assert orden is not None
    validar_orden_cursos(4, aristas, orden)


def test_cursos_ciclo_y_auto_dependencia():
    assert ordenar_cursos(2, [(0, 1), (1, 0)]) is None
    assert ordenar_cursos(1, [(0, 0)]) is None
    assert not puede_completar_cursos(2, [(0, 1), (1, 0)])


def test_cursos_dependencia_duplicada_se_ignora():
    assert ordenar_cursos(2, [(0, 1), (0, 1)]) == [0, 1]


@pytest.mark.parametrize("par", [[(-1, 0)], [(0, -1)], [(2, 0)], [(0, 2)]])
def test_cursos_rechaza_indices_invalidos(par):
    with pytest.raises(IndexError):
        ordenar_cursos(2, par)


@pytest.mark.parametrize("cantidad", [True, 2.0, "2", None])
def test_cursos_rechaza_cantidad_de_tipo_invalido(cantidad):
    with pytest.raises(TypeError):
        ordenar_cursos(cantidad, [])


def test_cursos_rechaza_cantidad_negativa():
    with pytest.raises(ValueError):
        ordenar_cursos(-1, [])


@pytest.mark.parametrize("par", [[(True, 1)], [(0, False)], [(0.0, 1)], [(0, "1")]])
def test_cursos_rechaza_extremos_de_tipo_invalido(par):
    with pytest.raises(TypeError):
        ordenar_cursos(2, par)


@pytest.mark.parametrize("par", [[(0,)], [(0, 1, 2)], [0], ["01"]])
def test_cursos_rechaza_pares_mal_formados(par):
    with pytest.raises(ValueError):
        ordenar_cursos(2, par)


def test_cursos_no_muta_y_funcion_complementaria_reutilizable():
    entrada = [(0, 2), (1, 2)]
    copia = deepcopy(entrada)
    assert puede_completar_cursos(3, entrada)
    assert entrada == copia

