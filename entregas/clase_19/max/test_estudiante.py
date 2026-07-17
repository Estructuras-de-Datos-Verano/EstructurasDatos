from implementacion import *


def test_max1():
    grafo = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    orden = orden_topologico(grafo)
    assert orden is not None
    assert es_orden_topologico(grafo, orden)


def test_max2():
    grafo = {"A": ["B"], "B": ["A"], "C": ["D"], "D": []}
    assert orden_topologico(grafo) is None


def test_max3():
    esperado = {"A": ["B"], "B": []}
    assert normalizar_grafo_dirigido({"A": ["B"]}) == esperado


def test_max4():
    grados = grados_entrada({"A": ["B", "B", "B"]})
    assert grados == {"A": 0, "B": 1}


def test_max5():
    grafo = {"A": ["B"], "B": ["C"], "C": []}
    assert not es_orden_topologico(grafo, ["C", "B", "A"])


def test_max6():
    prerrequisitos = [(0, 1), (2, 3)]
    orden = ordenar_cursos(4, prerrequisitos)
    assert orden is not None
