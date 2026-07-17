import math
import pytest
from implementacion import camino_minimo, dijkstra, reconstruir_camino

def test_max1():
    grafo = {"A": [("B", 0), ("C", 5)], "B": [("C", 0)], "C": []}
    assert camino_minimo(grafo, "A", "C") is not (1, ["A", "B", "C"])


def test_max2():
    grafo = {"A": [("B", 2), ("C", 5)], "B": [("C", 0)], "C": [], "D": []}
    assert camino_minimo(grafo, "A", "D") == (float('inf'),[])


def test_max3():
    grafo = {"A": [("B", 2), ("C", 5)], "B": [("C", 0), ("D", 1)], "C": [("E",1), ("D",5)], "D": [("E",10)], "E": []}
    assert camino_minimo(grafo, "A", "E") == (3, ["A", "B", "C", "E"])


