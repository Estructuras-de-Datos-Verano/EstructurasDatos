import math

import pytest

from entregas.clase_15.arturo.implementacion import camino_minimo, dijkstra, reconstruir_camino


def test_distancia_mejora_al_menos_dos_veces_ARTURO():
    """
    Prueba que el algoritmo actualiza correctamente la distancia de un nodo
    múltiples veces conforme descubre rutas más eficientes.
    """
    grafo = {
        "A": [("D", 10), ("B", 1)],
        "B": [("D", 7), ("C", 1)],
        "C": [("D", 1)],
        "D": []
    }
    
    # Traza esperada para D:
    # 1. Desde A: D = 10
    # 2. Desde B: D = 1 + 7 = 8 (Primera mejora)
    # 3. Desde C: D = 1 + 1 + 1 = 3 (Segunda mejora)
    
    distancias, predecesores = dijkstra(grafo, "A")
    
    assert distancias["D"] == 3
    assert reconstruir_camino(predecesores, "A", "D") == ["A", "B", "C", "D"]


def test_destino_inalcanzable_devuelve_infinito_y_lista_vacia_ARTURO():
    """
    El contrato esperado dicta que si un nodo destino no puede ser alcanzado 
    desde el origen (está en una componente desconectada), su costo mínimo 
    debe permanecer como infinito y el camino devuelto debe ser una lista vacía.
    """
    grafo = {
        "A": [("B", 5)],
        "B": [],
        "X": [("Y", 2)],
        "Y": []
    }
    
    costo, camino = camino_minimo(grafo, "A", "X")
    
    assert math.isinf(costo)
    assert camino == []


def test_entrada_obsoleta_ruta_directa_costosa_ARTURO():
    """
    Prueba que una ruta directa inicial muy cara genera una entrada en el heap 
    que luego se vuelve obsoleta al encontrar un atajo más barato. 
    El algoritmo debe ser capaz de ignorar la entrada vieja sin fallar.
    """
    grafo = {
        "A": [("B", 100), ("C", 5)],  # Ruta directa A->B cuesta 100
        "C": [("B", 10)],             # Ruta indirecta A->C->B cuesta 15
        "B": []
    }
    

    costo, camino = camino_minimo(grafo, "A", "B")
    
    assert costo == 15
    assert camino == ["A", "C", "B"]