def test_agregado_1_distancia_mejorada():
    """
    Revisa que no se vaya directo.
    """
    grafo = {"A": [("B", 1), ("D", 3)], "B":[("D", 1)], "D": [] }
    costo, camino = camino_minimo(grafo, "A", "D")

    assert costo < 3

def test_agregado_2_destino_ausente():
    """
    En el contrato, una lista vacía representa la ausencia del camino.
    """
    distancias, predecesores = dijkstra(red_ciudades(), "A")

    assert reconstruir_camino(predecesores, "A", "G") == []
    # Se espera que regrese una lista vacía

def test_agregado_3_ruta_claramente_obsoleta():
    """
    Revisa que elija la ruta óptima
    """
    grafo = {"A": [("B", 1), ("D", 999)], "B":[("D", 1)], "D": [] }
    costo, camino = camino_minimo(grafo, "A", "D")

    assert costo < 999