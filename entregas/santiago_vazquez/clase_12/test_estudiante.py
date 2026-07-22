import pytest
from implementacion import ArbolBinarioBusqueda

def test_arbol_totalmente_vacio():
    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio() is True
    assert arbol.altura() == 0
    assert arbol.cantidad_nodos() == 0
    assert arbol.es_degenerado() is False
    assert arbol.comparaciones_busqueda(5) == 0

def test_arbol_con_un_solo_nodo():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(15)
    assert arbol.esta_vacio() is False
    assert arbol.altura() == 1
    assert arbol.cantidad_nodos() == 1
    assert arbol.es_degenerado() is True
    assert arbol.comparaciones_busqueda(15) == 1
    assert arbol.comparaciones_busqueda(100) == 1

def test_arbol_en_linea_recta():
    arbol = ArbolBinarioBusqueda()
    for numero in [10, 20, 30, 40]:
        arbol.insertar(numero)
    assert arbol.altura() == 4
    assert arbol.cantidad_nodos() == 4
    assert arbol.es_degenerado() is True
    assert arbol.comparaciones_busqueda(40) == 4
    assert arbol.comparaciones_busqueda(50) == 4