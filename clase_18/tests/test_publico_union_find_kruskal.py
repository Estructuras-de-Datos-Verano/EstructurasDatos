"""Pruebas públicas de Union-Find, Kruskal y Road Reparation."""

import math

import pytest

from implementacion import UnionFind, costo_reparacion, kruskal


def test_union_find_cero_elementos():
    uf = UnionFind(0)
    assert uf.numero_componentes() == 0
    with pytest.raises(IndexError):
        uf.find(0)


def test_union_find_un_elemento():
    uf = UnionFind(1)
    assert uf.find(0) == 0
    assert uf.tamano_componente(0) == 1
    assert uf.numero_componentes() == 1


def test_union_find_inicialmente_separado():
    uf = UnionFind(5)
    assert [uf.find(i) for i in range(5)] == list(range(5))
    assert not uf.conectados(0, 4)
    assert uf.numero_componentes() == 5


def test_union_efectiva_repetida_y_reflexiva():
    uf = UnionFind(3)
    assert uf.union(0, 1) is True
    assert uf.numero_componentes() == 2
    assert uf.union(1, 0) is False
    assert uf.union(0, 0) is False
    assert uf.numero_componentes() == 2


def test_transitividad_conectividad_y_tamano():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(1, 3)
    assert uf.conectados(0, 2)
    assert uf.tamano_componente(3) == 4
    assert uf.numero_componentes() == 3


def test_compresion_no_cambia_particion_ni_contador():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)
    antes = uf.numero_componentes()
    raiz = uf.find(3)
    assert uf._padre[3] == raiz
    assert uf.conectados(1, 3)
    assert uf.numero_componentes() == antes


@pytest.mark.parametrize("cantidad", [True, False, 3.0, "3", None])
def test_union_find_rechaza_cantidad_de_tipo_invalido(cantidad):
    with pytest.raises(TypeError):
        UnionFind(cantidad)


def test_union_find_rechaza_cantidad_negativa():
    with pytest.raises(ValueError):
        UnionFind(-1)


@pytest.mark.parametrize("indice", [-1, 3])
def test_union_find_rechaza_indice_fuera_de_rango(indice):
    uf = UnionFind(3)
    with pytest.raises(IndexError):
        uf.find(indice)
    with pytest.raises(IndexError):
        uf.union(0, indice)


@pytest.mark.parametrize("indice", [True, 1.0, "1", None])
def test_union_find_rechaza_indice_de_tipo_invalido(indice):
    uf = UnionFind(3)
    with pytest.raises(TypeError):
        uf.find(indice)


def grafo_conductor():
    return [
        (0, 1, 4), (0, 2, 2), (0, 3, 5), (1, 3, 3),
        (2, 3, 1), (2, 4, 6), (3, 4, 2),
    ]


def test_kruskal_grafo_conductor_costo_y_v_menos_uno():
    resultado = kruskal(5, grafo_conductor())
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == 8.0
    assert len(elegidas) == 4
    assert set(elegidas) == {(2, 3, 1.0), (0, 2, 2.0), (3, 4, 2.0), (1, 3, 3.0)}


def test_kruskal_cero_y_un_vertice():
    assert kruskal(0, []) == (0.0, [])
    assert kruskal(1, []) == (0.0, [])


def test_kruskal_dos_vertices_y_una_arista():
    assert kruskal(2, [(0, 1, 7)]) == (7.0, [(0, 1, 7.0)])


def test_kruskal_triangulo_rechaza_ciclo():
    resultado = kruskal(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)])
    assert resultado == (3.0, [(0, 1, 1.0), (1, 2, 2.0)])


def test_kruskal_desconectado_devuelve_none():
    assert kruskal(4, [(0, 1, 1), (2, 3, 1)]) is None


def test_kruskal_admite_pesos_negativos_y_cero():
    resultado = kruskal(3, [(0, 1, -4), (1, 2, 0), (0, 2, 9)])
    assert resultado is not None and resultado[0] == -4.0


def test_kruskal_empates_verifica_propiedades_no_lista_exacta():
    aristas = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1)]
    resultado = kruskal(4, aristas)
    assert resultado is not None
    costo, elegidas = resultado
    assert costo == 3.0 and len(elegidas) == 3
    uf = UnionFind(4)
    assert all(uf.union(u, v) for u, v, _ in elegidas)
    assert uf.numero_componentes() == 1


def test_kruskal_aristas_paralelas_y_autoaristas():
    resultado = kruskal(2, [(0, 0, -10), (0, 1, 2), (0, 1, 7)])
    assert resultado == (2.0, [(0, 1, 2.0)])


def test_kruskal_no_modifica_aristas():
    aristas = grafo_conductor()
    copia = aristas.copy()
    kruskal(5, aristas)
    assert aristas == copia


@pytest.mark.parametrize("numero", [True, 3.0, "3", None])
def test_kruskal_rechaza_numero_vertices_invalido(numero):
    with pytest.raises(TypeError):
        kruskal(numero, [])


def test_kruskal_rechaza_numero_vertices_negativo():
    with pytest.raises(ValueError):
        kruskal(-1, [])


@pytest.mark.parametrize("arista", [(0, 1), (0, 1, 2, 3)])
def test_kruskal_rechaza_arista_mal_formada(arista):
    with pytest.raises(ValueError):
        kruskal(2, [arista])


@pytest.mark.parametrize("extremo", [True, 0.0, "0", None])
def test_kruskal_rechaza_extremo_de_tipo_invalido(extremo):
    with pytest.raises(TypeError):
        kruskal(2, [(extremo, 1, 3)])


@pytest.mark.parametrize("extremo", [-1, 2])
def test_kruskal_rechaza_vertice_fuera_de_rango(extremo):
    with pytest.raises(IndexError):
        kruskal(2, [(0, extremo, 3)])


@pytest.mark.parametrize("peso", [True, "3", None, object()])
def test_kruskal_rechaza_peso_no_numerico(peso):
    with pytest.raises(TypeError):
        kruskal(2, [(0, 1, peso)])


@pytest.mark.parametrize("peso", [math.inf, -math.inf, math.nan])
def test_kruskal_rechaza_peso_no_finito(peso):
    with pytest.raises(ValueError):
        kruskal(2, [(0, 1, peso)])


def test_costo_reparacion_red_conectada_y_resultado_entero():
    carreteras = [(0, 1, 3), (1, 2, 5), (1, 3, 2), (2, 3, 8), (4, 0, 7), (4, 3, 4)]
    resultado = costo_reparacion(5, carreteras)
    assert resultado == 14 and isinstance(resultado, int)


def test_costo_reparacion_desconectada_y_una_ciudad():
    assert costo_reparacion(4, [(0, 1, 2), (2, 3, 2)]) is None
    assert costo_reparacion(1, []) == 0


def test_costo_reparacion_no_muta_y_rechaza_costo_float():
    carreteras = [(0, 1, 2)]
    copia = carreteras.copy()
    assert costo_reparacion(2, carreteras) == 2
    assert carreteras == copia
    with pytest.raises(TypeError):
        costo_reparacion(2, [(0, 1, 2.0)])


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
