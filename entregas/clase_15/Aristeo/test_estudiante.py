import math
import pytest
from implementacion import dijkstra, camino_minimo, reconstruir_camino

def test_distancia_mejora_multiples_veces():
    """1. Protege el caso donde un nodo mejora su costo más de una vez dejando

    entradas obsoletas en el heap que deben ser ignoradas de forma perezosa.
    """
    # Camino inicial directo A->B (100). Luego A->C->B (50). Luego A->C->D->B (20).
    grafo = {
        "A": [("B", 100), ("C", 10)],
        "C": [("B", 40), ("D", 5)],
        "D": [("B", 5)],
        "B": []
    }
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 20
    assert predecesores["B"] == "D"
    assert reconstruir_camino(predecesores, "A", "B") == ["A", "C", "D", "B"]


def test_destino_inalcanzable():
    """2. Protege el contrato ante destinos completamente aislados o inalcanzables.

    Se espera que la distancia sea infinito y el camino devuelto sea vacío [].
    """
    grafo = {
        "A": [("B", 5)],
        "B": [],
        "Z": []  # Totalmente aislado
    }
    costo, camino = camino_minimo(grafo, "A", "Z")
    assert math.isinf(costo)
    assert camino == []


def test_ruta_indirecta_supera_directa_costosa():
    """3. Protege la lógica codiciosa contra BFS. Una arista directa masiva

    debe ser descartada a favor de una ruta con múltiples aristas pero menor costo total.
    """
    grafo = {
        "A": [("B", 10), ("D", 50)],
        "B": [("C", 10)],
        "C": [("D", 10)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 30
    assert camino == ["A", "B", "C", "D"]