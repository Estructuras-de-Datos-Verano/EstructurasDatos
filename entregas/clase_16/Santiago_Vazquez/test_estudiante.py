import pytest
import math
from entregas.clase_16.Santiago_Vazquez.implementacion import (
    dijkstra,
    camino_minimo,
    reconstruir_camino
)

def test_bool_no_se_acepta_como_peso():
    """Valida que pasar un booleano (True/False) como peso lance TypeError.
    
    Python trata a los bools como subclase de int (True == 1), por lo que es un caso
    de borde crítico que requiere una validación de tipo estricta 'isinstance(peso, bool)'.
    """
    grafo_invalido = {
        "A": [("B", True)]  
    }
    with pytest.raises(TypeError, match="pesos deben ser de tipo numérico"):
        dijkstra(grafo_invalido, "A")


def test_vecino_implicito_y_no_mutacion():
    """Verifica que si un nodo aparece solo como destino (vecino implícito),
    el grafo se normalice correctamente sin mutar la estructura de entrada.
    """
    grafo_original = {
        "A": [("B", 4.5)]
    }
    

    grafo_copia = {"A": [("B", 4.5)]}
    
    distancias, predecesores = dijkstra(grafo_original, "A")
    

    assert "B" in distancias
    assert distancias["B"] == 4.5
    assert predecesores["B"] == "A"
    

    assert grafo_original == grafo_copia
    assert "B" not in grafo_original  


def test_entrada_obsoleta():
    """Prueba que dijkstra ignore o maneje correctamente entradas desactualizadas en la cola.
    
    Esto ocurre cuando un nodo se añade a la cola de prioridad con una distancia,
    pero luego se encuentra un camino más corto y se vuelve a añadir con menor costo.
    El algoritmo debe procesar el más barato y descartar el obsoletizado.
    """
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "C": [("B", 2)],
        "B": []
    }
    
    distancias, predecesores = dijkstra(grafo, "A")
    
    assert distancias["B"] == 3.0
    assert predecesores["B"] == "C"


def test_peso_nan_o_infinito():
    """Valida que se rechacen explícitamente pesos que sean NaN, inf o -inf
    lanzando un ValueError que haga referencia a que el peso debe ser 'finito'.
    """
    grafo_nan = {"A": [("B", math.nan)]}
    grafo_inf = {"A": [("B", math.inf)]}
    grafo_ninf = {"A": [("B", -math.inf)]}

    for g in (grafo_nan, grafo_inf, grafo_ninf):
        with pytest.raises(ValueError, match="finito"):
            dijkstra(g, "A")


def test_ciclo_de_predecesores():
    """Verifica que reconstruir_camino detecte ciclos infinitos en el diccionario
    de predecesores y lance un ValueError para evitar bucles infinitos.
    """
    predecesores_con_ciclo = {
        "A": "B",
        "B": "A"
    }
    
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino(predecesores_con_ciclo, "A", "B")