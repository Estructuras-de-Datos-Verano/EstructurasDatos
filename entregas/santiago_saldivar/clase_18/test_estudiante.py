def test_agregado_1_TIAGO_union():
    """Revisa la unión"""
    uf = UnionFind(4)

    assert uf.numero_componentes() == 4

    assert uf.union(0,1) is True

    assert uf.numero_componentes() == 3

def test_agregado_2_TIAGO_repeticion():
    """Verifica que evite uniones redundantes."""
    uf = UnionFind(3)
    uf.union(0,1)

    assert uf.union(0,1) is False
    assert uf.union(1,0) is False
    assert uf.union(2,2) is False
    assert uf.numero_componentes() == 2

def test_agregado_3_TIAGO_transitividad():
    """Verifica transitividad."""
    uf = UnionFind(5)
    uf.union(0,1)
    uf.union(1,2)
    assert uf.conectados(0,2) is True
    assert uf.conectados(0,4) is False

def test_agregado_4_TIAGO_tamano_de_componente():
    """Verifica que los tamaños de los componentes"""
    uf = UnionFind(5)

    assert uf.tamano_componente(0) == 1

    uf.union(0,1)
    uf.union(1,2)

    assert uf.tamano_componente(0) == 3
    assert uf.tamano_componente(2) == 3
    assert uf.tamano_componente(4) == 1

    def test_agregado_5_TIAGO_arista_rechazada_ciclo():
    """Verifica que evite ciclos."""

    aristas =[(0, 1, 2), (1, 2, 3), (0, 2, 10)] 

    resultado = kruskal(3, aristas)
    assert resultado is not None

    costo, elegidas = resultado
    assert costo == 5.0
    assert len(elegidas) == 2
    assert (0,2,10.0) not in elegidas

def test_agregado_6_TIAGO_grafo_desconectado():
    """Verifica que no tome en cuenta nodos aislados."""
    uf = UnionFind(7)

    assert uf.tamano_componente(3) == 1

    uf.union(0,1)
    uf.union(1,2)

    assert uf.conectados(0,2) is True
    assert uf.conectados(0,4) is False

