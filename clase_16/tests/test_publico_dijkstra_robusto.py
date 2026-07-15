"""Pruebas públicas para contratos y robustez de Clase 16."""

import math

import pytest

from implementacion import camino_minimo, dijkstra, reconstruir_camino


def red_ciudades():
    """Grafo con mejoras sucesivas y rutas alternativas."""

    return {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1), ("E", 7)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
    }


def test_calcula_distancias_y_predecesores_conocidos():
    distancias, predecesores = dijkstra(red_ciudades(), "A")
    assert distancias == {"A": 0, "B": 3, "C": 1, "D": 4, "E": 7}
    assert reconstruir_camino(predecesores, "A", "E") == ["A", "C", "B", "D", "E"]


def test_no_muta_listas_de_adyacencia():
    grafo = red_ciudades()
    copia = {nodo: aristas.copy() for nodo, aristas in grafo.items()}
    dijkstra(grafo, "A")
    assert grafo == copia


def test_incluye_vecino_que_no_es_clave():
    distancias, predecesores = dijkstra({"A": [("B", 2)]}, "A")
    assert distancias == {"A": 0, "B": 2}
    assert predecesores["B"] == "A"


@pytest.mark.parametrize("peso", [-1, -0.5])
def test_rechaza_peso_negativo(peso):
    with pytest.raises(ValueError, match="no negativos"):
        dijkstra({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [math.inf, -math.inf, math.nan])
def test_rechaza_peso_no_finito(peso):
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [True, "3", None])
def test_rechaza_peso_no_numerico(peso):
    with pytest.raises(TypeError, match="numérico"):
        dijkstra({"A": [("B", peso)]}, "A")


def test_rechaza_arista_con_forma_incorrecta():
    with pytest.raises(TypeError, match="par"):
        dijkstra({"A": [("B", 1, "extra")]}, "A")


def test_rechaza_origen_inexistente():
    with pytest.raises(KeyError, match="origen"):
        dijkstra({"A": []}, "X")


def test_destino_inalcanzable_conserva_infinito_y_camino_vacio():
    grafo = {"A": [], "X": []}
    costo, camino = camino_minimo(grafo, "A", "X")
    assert math.isinf(costo)
    assert camino == []


def test_origen_igual_a_destino():
    assert camino_minimo({"A": []}, "A", "A") == (0, ["A"])


def test_reconstruccion_rechaza_ciclo():
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino({"A": None, "B": "C", "C": "B"}, "A", "B")


# TODO: agrega un test para grafo que no sea Mapping.
# TODO: agrega un test donde el nombre de un nodo o vecino no sea str.
# TODO: diseña una prueba que obligue a detectar una entrada obsoleta.
