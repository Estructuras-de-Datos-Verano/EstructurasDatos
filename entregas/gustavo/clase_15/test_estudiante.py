import math
from entregas.clase_15.Gustavo.implementacion import camino_minimo, dijkstra, reconstruir_camino

def test_distancia_mejora_dos_veces_y_deja_obsoletas():
    """
    Protege: El algoritmo debe manejar correctamente múltiples actualizaciones 
    para un mismo nodo y descartar las candidaturas previas en el heap.
    """
    # A->D directo es 15. A->B->D es 12. A->B->C->D es 9.
    grafo = {
        "A": [("B", 5), ("D", 15)],
        "B": [("C", 2), ("D", 7)],
        "C": [("D", 2)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 9
    assert camino == ["A", "B", "C", "D"]

def test_destino_inalcanzable_devuelve_infinito_y_vacio():
    """
    Protege: El contrato establece que si no hay ruta al destino, 
    el costo debe ser math.inf y el camino debe ser [].
    """
    grafo = {
        "A": [("B", 4)],
        "B": [],
        "Z": []  # Z no está conectado a nada
    }
    costo, camino = camino_minimo(grafo, "A", "Z")
    assert math.isinf(costo)
    assert camino == []

def test_ruta_indirecta_supera_directa_costosa():
    """
    Protege: El algoritmo no debe precipitarse cerrando un nodo solo por 
    tener una arista directa. Debe buscar atajos más baratos.
    """
    grafo = {
        "Origen": [("Destino", 100), ("Intermedio", 1)],
        "Intermedio": [("Destino", 2)]
    }
    distancias, predecesores = dijkstra(grafo, "Origen")
    assert distancias["Destino"] == 3
    assert reconstruir_camino(predecesores, "Origen", "Destino") == ["Origen", "Intermedio", "Destino"]

