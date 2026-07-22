import pytest
from implementacion import ArbolAVL

def test_arbol_vacio():
    arbol = ArbolAVL()
    assert arbol.altura() == 0
    assert arbol.inorden() == []
    assert arbol.esta_balanceado() is True

def test_evitar_duplicados():
    arbol = ArbolAVL()
    arbol.insertar(10)
    arbol.insertar(10)
    assert arbol.inorden() == [10]
    assert arbol.altura() == 1

def test_rotacion_simple_ll():
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(20)
    arbol.insertar(10)
    assert arbol.raiz.valor == 20
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado() is True

def test_rotacion_doble_lr():
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(10)
    arbol.insertar(20)
    assert arbol.raiz.valor == 20
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado() is True