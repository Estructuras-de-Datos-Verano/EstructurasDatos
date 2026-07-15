import pytest
from implementacion import dijkstra

# 1. Prueba para grafo que no sea Mapping
def test_rechaza_grafo_no_mapping():
    """
    Contrato: El grafo debe ser un mapeo estructurado (Mapping).
    Riesgo: Pasar una lista de tuplas en lugar de un diccionario rompería 
    la lectura por llaves. Debe lanzar TypeError.
    """
    grafo_lista = [("A", [("B", 5)])]
    with pytest.raises(TypeError, match="Mapping"):
        dijkstra(grafo_lista, "A")

# 2. Prueba donde el nombre de un nodo o vecino no sea str
def test_rechaza_nodos_no_str():
    """
    Contrato: Los identificadores de nodos deben ser cadenas de texto.
    Riesgo: Un entero u otro tipo de dato causaría inconsistencias en la tabla 
    de adyacencia. Debe lanzar TypeError tanto para llaves como para destinos.
    """
    # Validar que falle si el nodo origen (llave) es un int
    with pytest.raises(TypeError, match="str"):
        dijkstra({1: [("B", 5)]}, 1)
        
    # Validar que falle si el nodo destino (vecino) es un int
    with pytest.raises(TypeError, match="str"):
        dijkstra({"A": [(2, 5)]}, "A")

# 3. Prueba que obligue a detectar una entrada obsoleta
def test_procesa_correctamente_entrada_obsoleta():
    """
    Invariante: Guard clause de entradas obsoletas en el heap.
    Riesgo: El nodo 'B' entra al heap con costo 10 desde 'A'. Luego, 
    'A' visita 'C', quien ofrece una ruta a 'B' con costo total 3. 
    Se inserta (3, 'B') en el heap. Cuando el algoritmo extraiga (10, 'B') 
    más adelante, debe ignorarlo y no afectar el resultado.
    """
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "C": [("B", 2)],
        "B": [("D", 5)],
        "D": []
    }
    
    distancias, predecesores = dijkstra(grafo, "A")
    
    # Comprobamos que el costo y la ruta a B fueron los óptimos
    assert distancias["B"] == 3
    assert predecesores["B"] == "C"
    
    # Comprobamos que D se calculó correctamente a partir del B óptimo
    assert distancias["D"] == 8