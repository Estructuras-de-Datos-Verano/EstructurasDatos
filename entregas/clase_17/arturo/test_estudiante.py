import pytest
from math import inf
from entregas.clase_17.arturo.implementacion import (
    ColaLigada,
    DequeLigada,
    bfs_camino,
    cero_uno_bfs,
    camino_cero_uno,
)

def test_cola_respeta_fifo_estrictamente_ARTURO():
    """
    Regla: La cola debe extraer los elementos exactamente en el mismo orden 
    en el que fueron insertados (First In, First Out).
    """
    cola = ColaLigada()
    elementos = [10, 20, 30, 40, 50]
    
    for e in elementos:
        cola.encolar(e)
        
    extraidos = [cola.desencolar() for _ in range(5)]
    assert extraidos == elementos, "El orden de extracción no coincide con el de inserción."
    assert cola.esta_vacia(), "La cola debería quedar vacía al final."


def test_cola_reutilizacion_tras_vaciarla_ARTURO():
    """
    Regla: Al vaciar completamente una cola, los punteros internos deben 
    reiniciarse correctamente permitiendo su reutilización sin referencias muertas.
    """
    cola = ColaLigada()
    cola.encolar("A")
    cola.encolar("B")
    
    # Vaciamos la cola
    cola.desencolar()
    cola.desencolar()
    assert cola.esta_vacia() and len(cola) == 0
    
    # Reutilizamos
    cola.encolar("C")
    assert cola.primero() == "C"
    assert cola.desencolar() == "C"
    assert cola.esta_vacia()


def test_cola_secuencias_largas_y_alternadas_ARTURO():
    """
    Regla: La estructura de la cola debe mantenerse íntegra y el tamaño debe ser
    consistente incluso tras múltiples operaciones intercaladas de encolar/desencolar.
    """
    cola = ColaLigada()
    
    # Simulamos un flujo dinámico: entran 2, sale 1 repetidas veces
    for i in range(100):
        cola.encolar(i)
        cola.encolar(i + 1000)
        cola.desencolar()
        
    assert len(cola) == 100, "El tamaño no se actualizó correctamente tras intercalar."
    assert not cola.esta_vacia()


def test_deque_operaciones_combinadas_ARTURO():
    """
    Regla: El deque debe manejar de forma segura inserciones y extracciones 
    simultáneas por ambos extremos sin corromper los enlaces 'anterior' y 'siguiente'.
    """
    deque = DequeLigada()
    deque.agregar_inicio("Centro-Izq")
    deque.agregar_final("Centro-Der")
    deque.agregar_inicio("Extremo-Izq")
    deque.agregar_final("Extremo-Der")
    
    # Estado actual: Extremo-Izq ⇄ Centro-Izq ⇄ Centro-Der ⇄ Extremo-Der
    assert len(deque) == 4
    
    assert deque.quitar_final() == "Extremo-Der"
    assert deque.quitar_inicio() == "Extremo-Izq"
    assert deque.quitar_final() == "Centro-Der"
    assert deque.quitar_inicio() == "Centro-Izq"
    assert deque.esta_vacia()


def test_deque_reutilizacion_tras_vaciarla_ARTURO():
    """
    Regla: Vaciar el deque, ya sea por el inicio o el final, debe dejar los
    extremos limpios (None) permitiendo agregar elementos nuevos sin error.
    """
    deque = DequeLigada()
    deque.agregar_inicio("A")
    deque.quitar_final() # Retira "A" pero por el método contrario
    
    assert deque.esta_vacia()
    
    # Llenado inverso
    deque.agregar_final("B")
    deque.agregar_inicio("C")
    assert deque.quitar_final() == "B"
    assert deque.quitar_inicio() == "C"


def test_bfs_con_ciclo_ARTURO():
    """
    Regla: Si el grafo contiene un ciclo explícito, BFS debe usar su conjunto
    de visitados para no quedar atrapado en un bucle infinito.
    """
    grafo = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A", "D"], # El ciclo se cierra aquí, pero hay salida a D
        "D": []
    }
    camino = bfs_camino(grafo, "A", "D")
    assert camino == ["A", "B", "C", "D"], "BFS falló al escapar del ciclo."


def test_bfs_con_destino_inalcanzable_ARTURO():
    """
    Regla: Si un destino válido pertenece al grafo pero está en otra componente 
    conexa (inalcanzable), debe devolver una lista vacía.
    """
    grafo = {
        "A": ["B"], 
        "B": [],
        "X": ["Y"], 
        "Y": []
    }
    camino = bfs_camino(grafo, "A", "X")
    assert camino == [], "Un destino inalcanzable debe retornar lista vacía."



def test_cero_uno_ruta_mas_aristas_menor_costo_ARTURO():
    """
    Regla: 0-1 BFS debe favorecer el peso sobre el número de saltos. Una ruta 
    con 3 aristas de peso 0 debe ganar frente a una con 1 arista de peso 1.
    """
    grafo = {
        "A": [("D", 1), ("B", 0)],
        "B": [("C", 0)],
        "C": [("D", 0)],
        "D": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "D")
    assert costo == 0, "Debe priorizar la ruta de costo 0, aunque tenga más vértices."
    assert camino == ["A", "B", "C", "D"]


def test_cero_uno_mejora_distancia_despues_de_descubrirse_ARTURO():
    """
    Regla: Si un nodo (B) es descubierto primero por una arista costosa (peso 1),
    pero luego se descubre por una ruta más barata (peso 0), el algoritmo 
    debe actualizar su predecesor y reposicionarlo lógicamente.
    """
    grafo = {
        "A": [("B", 1), ("C", 0)], # A descubre B con costo 1. Luego A descubre C.
        "C": [("B", 0)],           # C descubre B con costo 0 (Mejora: 0 < 1).
        "B": [("D", 0)],
        "D": []
    }
    distancias, predecesores = cero_uno_bfs(grafo, "A")
    assert distancias["B"] == 0, "La distancia de B debió actualizarse a 0."
    assert predecesores["B"] == "C", "El predecesor debió actualizarse a C."
    
    costo, camino = camino_cero_uno(grafo, "A", "D")
    assert costo == 0
    assert camino == ["A", "C", "B", "D"]


@pytest.mark.parametrize("peso_invalido", [-1, 2, 5, 8])
def test_cero_uno_bfs_con_peso_invalido_ARTURO(peso_invalido):
    """
    Regla: El algoritmo 0-1 BFS solo es matemáticamente válido para pesos 0 y 1.
    Cualquier otro valor numérico ENTERO fuera de este dominio debe levantar 
    un ValueError explícito.
    """
    grafo = {"A": [("B", peso_invalido)], "B": []}
    
    with pytest.raises(ValueError, match="0 o 1"):
        cero_uno_bfs(grafo, "A")

@pytest.mark.parametrize("peso_tipo_invalido", [-0.5, 1.0, 0.5])
def test_cero_uno_bfs_con_peso_flotante_ARTURO(peso_tipo_invalido):
    """
    Regla: El algoritmo 0-1 BFS solo acepta enteros. Un flotante, 
    incluso si vale 1.0, debe levantar un TypeError.
    """
    grafo = {"A": [("B", peso_tipo_invalido)], "B": []}
    
    with pytest.raises(TypeError, match="entero 0 o 1"):
        cero_uno_bfs(grafo, "A")