import pytest
import math
from implementacion import dijkstra, camino_minimo, reconstruir_camino

def test_bool_no_se_acepta_como_peso():
    with pytest.raises(TypeError, match="numérico"):
        dijkstra({"A": [("B", True)]}, "A")

def test_vecino_implicito_y_no_mutacion():
    grafo_original = {"A": [("B", 5.0)]}
    distancias, predecesores = dijkstra(grafo_original, "A")
    assert "B" in distancias
    assert distancias["B"] == 5.0
    assert len(grafo_original) == 1
    assert "B" not in grafo_original

def test_entrada_obsoleta_heap():

    grafo = {
        "A": [("B", 10), ("C", 1)],
        "C": [("B", 1)],
        "B": [("D", 5)]
    }
    distancias, _ = dijkstra(grafo, "A")
    assert distancias["B"] == 2.0
    assert distancias["D"] == 7.0

def test_nan_o_infinito_lanzan_value_error():
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", float("nan"))]}, "A")
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", float("inf"))]}, "A")

def test_ciclo_de_predecesores_lanza_value_error():
    predecesores_corruptos = {"A": None, "B": "C", "C": "B"}
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino(predecesores_corruptos, "A", "B")

def test_grafo_no_es_mapping():
    with pytest.raises(TypeError, match="mapeo"):
        dijkstra([("A", "B", 5)], "A")

def test_nodo_no_es_str():
    with pytest.raises(TypeError, match="strings"):
        dijkstra({123: [("B", 5)]}, "123")
    with pytest.raises(TypeError, match="string"):
        dijkstra({"A": [(123, 5)]}, "A")
