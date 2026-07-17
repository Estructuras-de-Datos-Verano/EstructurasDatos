import pytest
from implementacion import ArbolBinarioBusqueda

def test_mi_arbol_vacio_es_degenerado():
    arbol = ArbolBinarioBusqueda()
    assert arbol.es_degenerado() is True
    assert arbol.cantidad_nodos() == 0

def test_mi_arbol_balanceado_no_es_degenerado():
    arbol = ArbolBinarioBusqueda()
    for v in [4, 2, 6, 1, 3, 5, 7]:
        arbol.insertar(v)
    assert arbol.es_degenerado() is False
    assert arbol.cantidad_nodos() == 7

def test_mi_conteo_comparaciones_fallidas():
    arbol = ArbolBinarioBusqueda()
    for v in [10, 5, 15]:
        arbol.insertar(v)
    assert arbol.comparaciones_busqueda(2) == 2