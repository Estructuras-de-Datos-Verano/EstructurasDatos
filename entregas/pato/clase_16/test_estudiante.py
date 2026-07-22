import math
import pytest

from implementacion import camino_minimo, dijkstra, reconstruir_camino

def test_grafo_no_sea_mapping():
    """TODO: Agrega un test para grafo que no sea Mapping."""
    grafo_invalido = [("A", "B", 5.0)]
    with pytest.raises(TypeError, match="Mapping"):
        dijkstra(grafo_invalido, "A")  


@pytest.mark.parametrize("grafo_invalido, origen", [
    ({1: [("B", 5.0)]}, "A"),       
    ({"A": [(2, 5.0)]}, "A"),       
    ({"A": [(None, 5.0)]}, "A"),    
])
def test_nombre_nodo_o_vecino_no_sea_str(grafo_invalido, origen):
    """TODO: Agrega un test donde el nombre de un nodo o vecino no sea str."""
    with pytest.raises(TypeError, match="str"):
        dijkstra(grafo_invalido, origen)  


def test_obliga_detectar_entrada_obsoleta():
    """TODO: Diseña una prueba que obligue a detectar una entrada obsoleta.
    
    Sin usar parches avanzados, probamos un grafo donde la ruta costosa a B
    entra primero al Heap (A->B costo 10), pero luego se encuentra un atajo 
    (A->C->B costo 2). Evaluamos que el sistema no falle y determine la
    distancia correcta, lo que a nivel de cobertura pasará por el `continue`.
    """
    grafo = {
        "A": [("B", 10.0), ("C", 1.0)],
        "B": [("D", 5.0)],
        "C": [("B", 1.0)],
        "D": []
    }
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 2.0
    assert predecesores["B"] == "C"

@pytest.mark.parametrize("peso_booleano", [True, False])
def test_bool_no_se_acepta_como_peso(peso_booleano):
    """1. bool no se acepta como peso (debe fallar diciendo numérico)."""
    grafo = {"A": [("B", peso_booleano)]}
    with pytest.raises(TypeError, match="numérico"):
        dijkstra(grafo, "A")  


def test_vecino_implicito_y_no_mutacion():
    """2. Vecino implícito y no mutación de la entrada."""
    grafo_original = {"A": [("B", 5.0)]}
    copia_seguridad = {"A": [("B", 5.0)]}
    
    distancias, _ = dijkstra(grafo_original, "A")
    
    assert "B" in distancias
    assert distancias["B"] == 5.0
    assert grafo_original == copia_seguridad


def test_componente_desconectado():
    """3. Prueba extra: Grafo con componentes inalcanzables."""
    grafo = {
        "A": [("B", 2.0)],
        "X": [("Y", 3.0)]  
    }
    distancias, _ = dijkstra(grafo, "A")
    
    assert distancias["B"] == 2.0
    assert math.isinf(distancias["X"])
    assert math.isinf(distancias["Y"])


@pytest.mark.parametrize("peso_anomalo", [float("nan"), float("inf"), float("-inf")])
def test_nan_o_infinito_como_peso(peso_anomalo):
    """4. NaN o infinito no deben ser válidos como costo."""
    grafo = {"A": [("B", peso_anomalo)]}
    with pytest.raises(ValueError, match="finito"):
        dijkstra(grafo, "A")


def test_ciclo_de_predecesores():
    """5. Ciclo de predecesores que debe frenar la reconstrucción."""
    predecesores_ciclicos = {"A": None, "B": "C", "C": "B"}
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino(predecesores_ciclicos, "A", "C")