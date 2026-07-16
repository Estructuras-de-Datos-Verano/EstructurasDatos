import math

import pytest

from entregas.clase_18.arturo.implementacion import UnionFind, costo_reparacion, kruskal

def test_ARTURO_union_efectiva_reduce_componentes():
    """Regla: Unión efectiva agrupa componentes distintas y reduce el contador."""
    uf = UnionFind(3)

    assert uf.numero_componentes() == 3
    assert uf.union(0, 2) is True
    assert uf.numero_componentes() == 2


def test_ARTURO_union_repetida_y_autoarista_es_redundante():
    """Regla: La unión de una misma raíz o una autoarista devuelve False."""
    uf = UnionFind(2)
   
    assert uf.union(1, 1) is False
    assert uf.union(0, 1) is True
    assert uf.union(0, 1) is False
    assert uf.numero_componentes() == 1


def test_ARTURO_transitividad_y_compresion_de_caminos():
    """Regla: Conectividad indirecta es válida y find comprime el árbol."""
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)

    assert uf.conectados(0, 3) is True

    raiz = uf.find(3)
    assert uf._padre[0] == raiz


def test_ARTURO_tamano_componente_se_actualiza_en_la_raiz():
    """Regla: El tamaño se consolida en la raíz al fusionar componentes."""
    uf = UnionFind(5)
    
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)
    raiz_principal = uf.find(0)

    assert uf.tamano_componente(raiz_principal) == 4


def test_ARTURO_kruskal_rechaza_ciclos_paralelas_y_empates():
    """Regla: Aristas que forman ciclos o son paralelas se descartan en empates."""
    aristas = [
        (0, 1, 5),
        (0, 1, 5), 
        (1, 2, 5), 
        (0, 2, 5)  
    ]
    resultado = kruskal(3, aristas)
    assert resultado is not None
    
    costo, elegidas = resultado
    assert costo == 10.0
    assert len(elegidas) == 2


def test_ARTURO_kruskal_grafo_desconectado_con_pesos_negativos():
    """Regla: Devuelve None si no hay V-1 aristas, sin importar pesos negativos."""
    aristas = [
        (0, 1, -100),
        (2, 3, -50)
    ]

    resultado = kruskal(4, aristas)
    assert resultado is None