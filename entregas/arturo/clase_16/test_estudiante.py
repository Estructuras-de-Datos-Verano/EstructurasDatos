
import math

import pytest

from entregas.clase_16.arturo.implementacion import camino_minimo, dijkstra, reconstruir_camino


@pytest.mark.parametrize("peso_invalido", [
    True, 
    False, 
    "5", 
    None, 
    []
])
def test_peso_tipo_invalido_lanza_type_error_ARTURO(peso_invalido):
    """
    Un bool en Python hereda de int, por lo que True podría interpretarse como 1.
    Esta prueba garantiza que la función exija tipos numéricos estrictos y rechace booleanos o cadenas.
    """
    grafo = {"A": [("B", peso_invalido)]}
    with pytest.raises(TypeError):
        camino_minimo(grafo, "A", "B")



def test_vecino_implicito_y_no_mutacion_ARTURO():
    """
    Verifica que un nodo que solo aparece como destino (B) se añada correctamente
    a las tablas internas sin modificar el diccionario original proporcionado por el usuario.
    """
    grafo_original = {"A": [("B", 5)]}
    grafo_referencia = {"A": [("B", 5)]}
    
    distancias, predecesores = dijkstra(grafo_original, "A")
    
    # Comprobación de vecino implícito
    assert "B" in distancias, "El nodo B debe inicializarse en distancias aunque no sea clave principal."
    assert "B" in predecesores, "El nodo B debe inicializarse en predecesores."
    assert distancias["B"] == 5
    
    # Comprobación de no mutación
    assert grafo_original == grafo_referencia, "El grafo original no debe sufrir mutaciones."



def test_procesamiento_entradas_obsoletas_ARTURO():
    """
    Alimenta el grafo con una ruta inicial costosa y una ruta posterior más barata.
    Asegura que el algoritmo descarte la evaluación de la entrada obsoleta (10, B) 
    y mantenga el resultado de la óptima (3, B).
    """
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "C": [("B", 2)],
        "B": []
    }
    costo, ruta = camino_minimo(grafo, "A", "B")
    
    assert costo == 3, "Debe priorizar la ruta más corta ignorando el 10 inicial."
    assert ruta == ["A", "C", "B"]



# Parametrizamos los valores que, aunque numéricos, violan el dominio matemático del algoritmo.
@pytest.mark.parametrize("peso_invalido", [
    math.nan, 
    math.inf, 
    -math.inf, 
    -5
])
def test_peso_fuera_de_dominio_lanza_value_error_ARTURO(peso_invalido):
    """
    NaN corrompe el ordenamiento de un min-heap y los pesos negativos rompen 
    el invariante de monotonía de Dijkstra. Deben lanzar ValueError explícitamente.
    """
    grafo = {"A": [("B", peso_invalido)]}
    with pytest.raises(ValueError):
        camino_minimo(grafo, "A", "B")


def test_ciclo_predecesores_lanza_value_error_ARTURO():
    """
    Si el diccionario de predecesores está corrupto y contiene un ciclo lógico
    que nunca llega al origen, la función debe lanzar ValueError.
    """
    predecesores_corruptos = {"A": None, "B": "C", "C": "B"}
    
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino(predecesores_corruptos, "A", "B")