from implementacion import * 
import pytest

# TODO: agrega un test para grafo que no sea Mapping.
def test_grafo_debe_ser_mapping_LEO():
    """
    Verifica que el grafo deba implementar Mapping.
    """
    with pytest.raises(TypeError):
        dijkstra([("A", [("B", 1)])], "A")

# TODO: agrega un test donde el nombre de un nodo o vecino no sea str.
@pytest.mark.parametrize("grafo", [{1: [("B", 2)], "B": []}, {"A": [(2, 3)], "B": []}])
def test_nombres_de_nodos_y_vecinos_deben_ser_str_LEO(grafo):
    """
    Verifica que los nombres de nodos y vecinos sean cadenas.
    """
    with pytest.raises(TypeError):
        dijkstra(grafo, "A")


# TODO: diseña una prueba que obligue a detectar una entrada obsoleta.
def test_entrada_obsoleta_LEO():
    """
    Verifica que una mejor distancia sustituya una anterior y que
    la entrada obsoleta del heap sea ignorada.
    """
    grafo = {"A": [("B", 10), ("C", 1)], "B": [], "C": [("B", 1)]}
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 2
    assert reconstruir_camino(predecesores, "A", "B") == ["A", "C", "B"]


@pytest.mark.parametrize("peso", [True, False])
def test_bool_no_se_acepta_como_peso_LEO(peso):
    """
    Verifica que los valores booleanos no sean aceptados como pesos.
    """
    grafo = {"A": [("B", peso)], "B": []}
    with pytest.raises(TypeError):
        dijkstra(grafo, "A")

def test_vecino_implicito_y_no_mutacion_LEO():
    """
    Verifica que un vecino implícito sea agregado internamente sin
    modificar el grafo recibido.
    """
    grafo = {"A": [("B", 4)]}
    copia = {"A": [("B", 4)]}
    distancias, _ = dijkstra(grafo, "A")
    assert distancias["B"] == 4
    assert grafo == copia


@pytest.mark.parametrize("peso", [float("nan"), float("inf"), float("-inf")])
def test_pesos_no_finitos_LEO(peso):
    """
    Verifica que los pesos NaN o infinitos sean rechazados.
    """
    grafo = {"A": [("B", peso)], "B": []}
    with pytest.raises(ValueError):
        dijkstra(grafo, "A")

def test_ciclo_de_predecesores_LEO():
    """
    Verifica que reconstruir_camino detecte un ciclo
    en el diccionario de predecesores.
    """
    predecesores = {"A": "B", "B": "A"}
    with pytest.raises(ValueError):
        reconstruir_camino(predecesores, "A", "B")

