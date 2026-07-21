"""Pruebas públicas para contratos y robustez de Clase 16."""

import math
import pytest
import heapq
from implementacion import camino_minimo, dijkstra, reconstruir_camino, _normalizar_grafo
# from implementacion import dijkstra
#from revision_temporal import dijkstra, reconstruir_camino, _normalizar_grafo

def red_ciudades():
    """Grafo con mejoras sucesivas y rutas alternativas."""

    return {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1), ("E", 7)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
    }


def test_calcula_distancias_y_predecesores_conocidos():
    distancias, predecesores = dijkstra(red_ciudades(), "A")
    assert distancias == {"A": 0, "B": 3, "C": 1, "D": 4, "E": 7}
    assert reconstruir_camino(predecesores, "A", "E") == ["A", "C", "B", "D", "E"]


def test_no_muta_listas_de_adyacencia():
    grafo = red_ciudades()
    copia = {nodo: aristas.copy() for nodo, aristas in grafo.items()}
    dijkstra(grafo, "A")
    assert grafo == copia


def test_incluye_vecino_que_no_es_clave():
    distancias, predecesores = dijkstra({"A": [("B", 2)]}, "A")
    assert distancias == {"A": 0, "B": 2}
    assert predecesores["B"] == "A"


@pytest.mark.parametrize("peso", [-1, -0.5])
def test_rechaza_peso_negativo(peso):
    with pytest.raises(ValueError, match="no negativos"):
        dijkstra({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [math.inf, -math.inf, math.nan])
def test_rechaza_peso_no_finito(peso):
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [True, "3", None])
def test_rechaza_peso_no_numerico(peso):
    with pytest.raises(TypeError, match="numérico"):
        dijkstra({"A": [("B", peso)]}, "A")


def test_rechaza_arista_con_forma_incorrecta():
    with pytest.raises(TypeError, match="par"):
        dijkstra({"A": [("B", 1, "extra")]}, "A")


def test_rechaza_origen_inexistente():
    with pytest.raises(KeyError, match="origen"):
        dijkstra({"A": []}, "X")


def test_destino_inalcanzable_conserva_infinito_y_camino_vacio():
    grafo = {"A": [], "X": []}
    costo, camino = camino_minimo(grafo, "A", "X")
    assert math.isinf(costo)
    assert camino == []


def test_origen_igual_a_destino():
    assert camino_minimo({"A": []}, "A", "A") == (0, ["A"])


def test_reconstruccion_rechaza_ciclo():
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino({"A": None, "B": "C", "C": "B"}, "A", "B")

def test_grafo_no_mapping():
    with pytest.raises(TypeError, match="Mapping"):
        dijkstra([("A", [("B", 1)])], "A")
def test_nodo_no_str():
    with pytest.raises(TypeError, match="str"):
        dijkstra({1: [("B", 1)]}, 1)
def test_vecino_no_str():
    with pytest.raises(TypeError, match="str"):
        dijkstra({"A": [(2, 1)]}, "A")
def test_entrada_obsoleta():
    grafo = {"A": [("B", 1)], "B": [], "C": [("B", 2)]}
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 1
    assert predecesores["B"] == "A"

# 1. bool no se acepta como peso
def test_rechaza_peso_booleano():
    """Prueba que un booleano (True/False) lance TypeError, aunque Python lo considere int."""
    grafo_invalido = {"A": [("B", True)]}
    
    with pytest.raises(TypeError, match="numéricos"):
        dijkstra(grafo_invalido, "A")

# 2. vecino implícito y no mutación
def test_vecino_implicito_y_no_mutacion():
    """Prueba que el nodo 'B' se procese correctamente sin alterar el grafo original."""
    grafo_original = {"A": [("B", 1.0)]}
    # Hacemos una copia manual para verificar que el original no mute
    estado_inicial = {"A": [("B", 1.0)]}
    
    distancias, predecesores = dijkstra(grafo_original, "A")
    
    # Vecino implícito: B debe existir en los resultados
    assert "B" in distancias
    assert distancias["B"] == 1.0
    assert predecesores["B"] == "A"
    
    # No mutación: el grafo original debe seguir siendo exactamente igual
    assert grafo_original == estado_inicial
    assert "B" not in grafo_original  # No se debió inyectar la clave 'B' en el original


# 3. entrada obsoleta
def test_entrada_obsoleta():
    """Prueba que una entrada obsoleta en el heap no afecte el resultado final."""
    grafo = red_ciudades()
    
    # Ejecutamos Dijkstra y forzamos una entrada obsoleta
    distancias, predecesores = dijkstra(grafo, "A")
    
    # La distancia a C debe ser 2 (A -> B -> C)
    assert distancias["C"] == 1
    assert predecesores["C"] == "A"

# 4. NaN o infinito
def test_rechaza_nan_e_infinito():
    """Prueba que los pesos inválidos matemáticamente lancen ValueError."""
    grafo_nan = {"A": [("B", math.nan)]}
    grafo_inf = {"A": [("B", math.inf)]}
    grafo_inf_neg = {"A": [("B", -math.inf)]}
    
    with pytest.raises(ValueError, match="finitos"):
        dijkstra(grafo_nan, "A")
        
    with pytest.raises(ValueError, match="finitos"):
        dijkstra(grafo_inf, "A")
        
    with pytest.raises(ValueError, match="negativo|finitos"):
        dijkstra(grafo_inf_neg, "A")


# 5. ciclo de predecesores
def test_detecta_ciclo_predecesores():
    # El origen existe pacíficamente, pero el destino está atrapado en un bucle
    predecesores_malformados = {
        "Inicio": None,
        "A": "B",
        "B": "C",
        "C": "B"   # ¡Aquí está el ciclo infinito entre B y C!
    }
    
    # La prueba buscará la palabra "ciclo" en minúscula en tu mensaje de error
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino(predecesores_malformados, origen="Inicio", destino="A")