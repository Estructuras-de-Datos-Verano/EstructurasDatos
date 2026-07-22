from implementacion import *

def test_distancia_mejora_y_descarta_entrada_obsoleta_LEO():
    """
    Verifica que una distancia pueda mejorar más de una vez y que
    el algoritmo conserve la mejor ruta encontrada.
    """
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "B": [],
        "C": [("D", 1)],
        "D": [("B", 1)],
    }

    costo, camino = camino_minimo(grafo, "A", "B")

    assert costo == 3
    assert camino == ["A", "C", "D", "B"]


def test_destino_inalcanzable_LEO():
    """
    Verifica que un destino sin conexión desde el origen devuelva
    costo infinito y camino vacío.
    """
    grafo = {
        "A": [("B", 1)],
        "B": [],
        "C": [],
    }

    costo, camino = camino_minimo(grafo, "A", "C")

    assert costo == float("inf")
    assert camino == []


def test_ruta_indirecta_es_mejor_que_directa_LEO():
    """
    Verifica que el algoritmo elija una ruta indirecta cuando su
    costo total es menor que una arista directa.
    """
    grafo = {
        "A": [("B", 10), ("C", 2)],
        "B": [],
        "C": [("B", 3)],
    }

    costo, camino = camino_minimo(grafo, "A", "B")

    assert costo == 5
    assert camino == ["A", "C", "B"]