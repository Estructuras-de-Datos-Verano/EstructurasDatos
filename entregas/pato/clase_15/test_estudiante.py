import math
import pytest

from entregas.clase_15.Pato.implementacion import camino_minimo, dijkstra, reconstruir_camino

def test_distancia_mejora_dos_veces():
   
    grafo = {
        "A": [("E", 20), ("B", 5), ("C", 2)],
        "B": [("E", 10)],
        "C": [("D", 2)],
        "D": [("E", 2)],
        "E": []
    }
    
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["E"] == 6
    
    costo, camino = camino_minimo(grafo, "A", "E")
    assert costo == 6
    assert camino == ["A", "C", "D", "E"]


def test_destino_inalcanzable_contrato():
    
    grafo = {
        "A": [("B", 10)],
        "B": [],
        "X": [("Y", 5)],  
        "Y": []
    }
    
    costo, camino = camino_minimo(grafo, "A", "X")
    
    assert math.isinf(costo), "El costo hacia un nodo inalcanzable debe ser infinito."
    assert camino == [], "El camino hacia un nodo inalcanzable debe ser una lista vacía."


def test_entrada_obsoleta_ruta_directa_costosa():
    
    grafo = {
        "A": [("B", 100), ("C", 1)],
        "B": [],
        "C": [("B", 1)]
    }
    
    costo, camino = camino_minimo(grafo, "A", "B")
    
    assert costo == 2
    assert camino == ["A", "C", "B"]
    
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 2
    assert predecesores["B"] == "C"