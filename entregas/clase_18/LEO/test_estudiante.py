from implementacion import *


def test_union_une_componentes_grandes_LEO():
    """
    Verifica la unión entre dos nodos disminuye el número de componentes y conecta los elementos
    """
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    assert uf.union(1, 2) is True
    assert uf.numero_componentes() == 3
    assert uf.conectados(0, 3)


def test_union_repetida_no_modifica_tamano_LEO():
    """
    Verifica que repetir una unión no cambia el tamaño ni el número de los componentes
    """
    uf = UnionFind(4)
    uf.union(0, 1)
    tamano = uf.tamano_componente(0)
    componentes = uf.numero_componentes()
    assert uf.union(0, 1) is False
    assert uf.tamano_componente(0) == tamano
    assert uf.numero_componentes() == componentes


def test_transitividad_cadena_larga_LEO():
    """
    Verifica la transitividad de caminos. Así, el primer y el último nodo deben quedar conectados.
    """
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)

    assert uf.conectados(0, 4)
    assert uf.tamano_componente(4) == 5


def test_tamano_componente_despues_de_varias_uniones_LEO():
    """
    Verifica que el tamaño de una componente se actualice correctamente después de varias uniones seguidas.
    """
    uf = UnionFind(7)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(1, 2)
    uf.union(0, 4)
    assert uf.tamano_componente(5) == 6
    assert uf.numero_componentes() == 2


def test_kruskal_descarta_camino_que_forma_ciclo_LEO():
    """
    Verifica que Kruskal descarte un camino barato cuando se forma un ciclo, aunque todavía existan aristas por revisar
    """
    resultado = kruskal(4, [(0, 1, 1), (1, 2, 1), (0, 2, 1), (2, 3, 2)])
    assert resultado is not None
    costo, mst = resultado
    assert costo == 4.0
    assert len(mst) == 3
    assert (0, 2, 1.0) not in mst or (1, 2, 1.0) not in mst


def test_kruskal_grafo_con_un_vertice_aislado_LEO():
    """
    Verifica que Kruskal devuelva None cuando existe un vértice aislado que evita que se construya un árbol
    """
    resultado = kruskal(5, [(0, 1, 2), (1, 2, 3), (2, 3, 1),])
    assert resultado is None