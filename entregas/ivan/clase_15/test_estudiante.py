import math

import pytest

from implementacion import camino_minimo, dijkstra, reconstruir_camino

def test_camino_mejora_dos_veces():
    """
    Prueba el camino mínimo con un grafo donde el camino más corto mejora dos veces antes de llegar al destino.
    """
    grafo = {"A": [("B", 5), ("C", 1)], 
             "B": [("C", 1)], 
             "C": []}
    costo, camino = camino_minimo(grafo, "A", "B")
    assert costo == 5
    assert camino == ["A", "B"]

def test_destino_inalcanzable():
    """
    Prueba el camino mínimo con un grafo donde el destino es inalcanzable.
    """
    grafo = {"A": [("B", 2)], "B": [], "X": []}
    costo, camino = camino_minimo(grafo, "A", "X")
    assert costo == float("inf")
    assert camino == []

def test_entrada_obsoleta_con_ruta_directa_costosa():
    """
    Prueba el camino mínimo con un grafo donde hay una ruta directa costosa y una ruta más barata indirecta.
    """
    grafo = {"A": [("B", 10), ("C", 1)], 
             "B": [("D", 1)], 
             "C": [("D", 1)], 
             "D": []}
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 2
    assert camino == ["A", "C", "D"]