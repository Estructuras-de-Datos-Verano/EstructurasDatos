import pytest
from implementacion import dijkstra, reconstruir_camino, camino_minimo

def test_mejoras_multiples_y_obsoletos():
    """Caso 1: Comprueba la correcta eliminación perezosa de entradas obsoletas.
    El nodo B recibe una propuesta inicial costosa (9) y luego una óptima (3).
    """
    grafo = {
        "A": [("B", 9), ("C", 1)],
        "B": [],
        "C": [("B", 2)]
    }
    distancias, _ = dijkstra(grafo, "A")
    assert distancias["B"] == 3

def test_destino_inalcanzable():
    """Caso 2: Comprueba que un destino completamente aislado devuelva camino vacío e infinito."""
    grafo = {
        "A": [("B", 2)],
        "B": [],
        "C": []
    }
    costo, camino = camino_minimo(grafo, "A", "C")
    assert costo == float("inf")
    assert camino == []

def test_ruta_indirecta_supera_directa_costosa():
    """Caso 3: Comprueba que una ruta con más aristas pero menor peso sea la seleccionada."""
    grafo = {
        "A": [("D", 15), ("B", 2)],
        "B": [("C", 3)],
        "C": [("D", 1)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 6
    assert camino == ["A", "B", "C", "D"]

def test_error_pesos_negativos():
    """Caso 4: Valida que se lance un ValueError ante aristas con pesos negativos."""
    grafo = {
        "A": [("B", -1)],
        "B": []
    }
    with pytest.raises(ValueError):
        dijkstra(grafo, "A")