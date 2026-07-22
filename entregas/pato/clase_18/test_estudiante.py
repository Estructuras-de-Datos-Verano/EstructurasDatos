import pytest
from implementacion import UnionFind, kruskal

# 1. SEIS PRUEBAS PROPIAS EXPLICADAS

def test_union_efectiva_reduce_componentes():
    uf = UnionFind(3)
    assert uf.union(0, 1) is True
    assert uf.numero_componentes() == 2


def test_union_repetida_no_reduce_componentes():
    uf = UnionFind(2)
    assert uf.union(0, 1) is True
    antes = uf.numero_componentes()
    assert uf.union(1, 0) is False
    assert uf.numero_componentes() == antes


def test_transitividad_y_conectividad():
    uf = UnionFind(3)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.conectados(0, 2) is True


def test_tamano_componente_actualizado():
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 2)
    assert uf.tamano_componente(0) == 4


def test_kruskal_arista_rechazada_por_ciclo():
    aristas = [(0, 1, 10), (1, 2, 20), (2, 0, 30)]
    costo, elegidas = kruskal(3, aristas)
    assert costo == 30.0
    assert len(elegidas) == 2
    assert (2, 0, 30) not in elegidas


def test_kruskal_grafo_desconectado():
    aristas = [(0, 1, 5), (2, 3, 5)]
    assert kruskal(4, aristas) is None

# 2. PRUEBAS COMPLEMENTARIAS

def test_union_find_indice_negativo():
    uf = UnionFind(3)
    with pytest.raises(IndexError):
        uf.find(-1)


def test_kruskal_peso_negativo():
    aristas = [(0, 1, -5), (1, 2, -10), (0, 2, 3)]
    costo, elegidas = kruskal(3, aristas)
    assert costo == -15.0


def test_kruskal_aristas_paralelas():
    aristas = [(0, 1, 15), (0, 1, 5), (1, 2, 10)]
    costo, elegidas = kruskal(3, aristas)
    assert costo == 15.0
    assert (0, 1, 5.0) in elegidas


def test_kruskal_autoaristas():
    aristas = [(0, 0, -100), (0, 1, 10)]
    costo, elegidas = kruskal(2, aristas)
    assert costo == 10.0
    assert len(elegidas) == 1


def test_kruskal_empates_valida_propiedades():
    aristas = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]
    resultado = kruskal(4, aristas)
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == 3.0
    assert len(elegidas) == 3
    uf = UnionFind(4)
    for u, v, _ in elegidas:
        uf.union(u, v)
    assert uf.numero_componentes() == 1


def test_kruskal_un_vertice():
    costo, elegidas = kruskal(1, [])
    assert costo == 0.0
    assert elegidas == []


def test_kruskal_no_muta_entrada():
    aristas = [(0, 1, 10), (1, 2, 5)]
    copia_aristas = list(aristas)
    kruskal(3, aristas)
    assert aristas == copia_aristas


def test_union_find_compresion_caminos():
    uf = UnionFind(4)
    uf._padre = [1, 2, 3, 3] 
    
    raiz = uf.find(0)
    assert raiz == 3
    assert uf._padre[0] == 3
    assert uf._padre[1] == 3