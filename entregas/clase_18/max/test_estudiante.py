import math
import pytest
from implementacion import UnionFind, costo_reparacion, kruskal

from implementacion import UnionFind, kruskal

def prueba_max1():
    uf = UnionFind(4)
    resultado = uf.union(0, 1)
    assert resultado is True
    assert uf.conectados(0, 1) is True
    assert uf.numero_componentes() == 3


def prueba_max2():
    uf = UnionFind(3)
    uf.union(0, 1)
    resultado_repetido = uf.union(0, 1)
    resultado_inverso = uf.union(1, 0)
    assert resultado_repetido is False
    assert resultado_inverso is False
    assert uf.numero_componentes() == 2


def prueba_max3():
    uf = UnionFind(4)
    uf.union(0, 1)  
    uf.union(1, 2)  
    assert uf.conectados(0, 2) is True
    assert uf.conectados(2, 0) is True


def prueba_max4():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 2)
    assert uf.tamano_componente(0) == 4
    assert uf.tamano_componente(3) == 4
    assert uf.tamano_componente(4) == 1


def prueba_max5():
    aristas = [(0, 1, 1), (1, 2, 2), (0, 2, 5)  ]
    resultado = kruskal(3, aristas)
    assert resultado is not None
    costo, mst = resultado
    assert costo == 3.0
    assert len(mst) == 2
    assert (0, 2, 5.0) not in mst


def prueba_max6():
    aristas_desconectadas = [(0, 1, 2), (2, 3, 4)]
    resultado = kruskal(4, aristas_desconectadas)
    assert resultado is None