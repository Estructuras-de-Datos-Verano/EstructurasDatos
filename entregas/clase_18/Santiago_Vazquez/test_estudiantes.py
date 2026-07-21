import pytest
from implementacion import UnionFind, kruskal


def test_union_efectiva():
    """Prueba que une dos elementos separados y reduce componentes."""
    uf = UnionFind(5)
    assert uf.union(0, 1) is True
    assert uf.numero_componentes() == 4


def test_union_repetida():
    """Prueba que unir elementos ya conectados devuelve False sin cambiar componentes."""
    uf = UnionFind(5)
    uf.union(0, 1)
    assert uf.union(0, 1) is False
    assert uf.numero_componentes() == 4


def test_transitividad():
    """Prueba que la conexión se propaga de manera transitiva entre componentes."""
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.conectados(0, 2) is True


def test_tamano_componente():
    """Prueba que el tamaño de la componente aumenta adecuadamente tras una unión."""
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)
    assert uf.tamano_componente(3) == 4


def test_arista_rechazada_por_ciclo():
    """Prueba que Kruskal ignora aristas que cerrarían un ciclo en el árbol."""
    aristas = [(0, 1, 2), (1, 2, 3), (0, 2, 5)]
    res = kruskal(3, aristas)
    assert res is not None
    assert len(res[1]) == 2
    assert res[0] == 5.0


def test_grafo_desconectado():
    """Prueba que Kruskal retorna None si el grafo final no está totalmente conectado."""
    aristas = [(0, 1, 2), (2, 3, 4)]
    assert kruskal(4, aristas) is None