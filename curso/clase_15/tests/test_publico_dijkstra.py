"""Pruebas públicas de Clase 15; scripts/evaluar.py importa la entrega directamente."""

import math

import pytest

from implementacion import camino_minimo, dijkstra, reconstruir_camino


def red_ciudades():
    """Grafo conductor con mejoras sucesivas y entradas obsoletas."""

    return {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1), ("E", 7)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
    }


def test_origen_tiene_distancia_cero_y_sin_predecesor():
    distancias, predecesores = dijkstra(red_ciudades(), "A")
    assert distancias["A"] == 0
    assert predecesores["A"] is None


def test_bfs_no_basta_cuando_pesos_difieren():
    grafo = {"A": [("D", 10), ("B", 1)], "B": [("D", 1)], "D": []}
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 2
    assert camino == ["A", "B", "D"]


def test_red_ciudades_calcula_distancias_minimas():
    distancias, _ = dijkstra(red_ciudades(), "A")
    assert distancias == {"A": 0, "B": 3, "C": 1, "D": 4, "E": 7}


def test_predecesores_reconstruyen_camino():
    distancias, predecesores = dijkstra(red_ciudades(), "A")
    assert distancias["E"] == 7
    assert reconstruir_camino(predecesores, "A", "E") == ["A", "C", "B", "D", "E"]


def test_nodo_inalcanzable_conserva_infinito():
    grafo = {"A": [("B", 2)], "B": [], "X": []}
    distancias, predecesores = dijkstra(grafo, "A")
    assert math.isinf(distancias["X"])
    assert predecesores["X"] is None
    assert reconstruir_camino(predecesores, "A", "X") == []


def test_camino_del_origen_a_si_mismo():
    costo, camino = camino_minimo({"A": []}, "A", "A")
    assert costo == 0
    assert camino == ["A"]


def test_pesos_cero_son_validos():
    grafo = {"A": [("B", 0), ("C", 5)], "B": [("C", 0)], "C": []}
    assert camino_minimo(grafo, "A", "C") == (0, ["A", "B", "C"])


def test_peso_negativo_se_rechaza():
    with pytest.raises(ValueError):
        dijkstra({"A": [("B", -1)], "B": []}, "A")


def test_origen_inexistente_se_rechaza():
    with pytest.raises(KeyError):
        dijkstra({"A": []}, "X")


def test_vecino_implicito_se_incluye():
    distancias, predecesores = dijkstra({"A": [("B", 3)]}, "A")
    assert distancias["B"] == 3
    assert predecesores["B"] == "A"


def test_no_muta_el_grafo_recibido():
    grafo = red_ciudades()
    copia = {nodo: vecinos.copy() for nodo, vecinos in grafo.items()}
    dijkstra(grafo, "A")
    assert grafo == copia


# TODO: en test_estudiante.py prueba una distancia que mejore al menos dos veces.
# TODO: prueba un destino inalcanzable y explica el contrato esperado.
# TODO: prueba una entrada obsoleta mediante un grafo con ruta directa costosa.

