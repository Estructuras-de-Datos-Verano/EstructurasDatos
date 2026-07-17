from implementacion import *

def test_rotacion_ll_LEO():
    """Insertar 30, 20 y 10 debe provocar una rotación simple LL."""
    arbol = ArbolAVL()
    for valor in [30, 20, 10]:
        arbol.insertar(valor)
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.altura() == 2
    assert arbol.esta_balanceado()


def test_rotacion_lr_LEO():
    """Insertar 30, 10 y 20 debe provocar una rotación doble LR."""

    arbol = ArbolAVL()
    for valor in [30, 10, 20]:
        arbol.insertar(valor)
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.altura() == 2
    assert arbol.esta_balanceado()


def test_busqueda_LEO():
    """La búsqueda debe encontrar valores existentes y rechazar ausentes."""

    arbol = ArbolAVL()
    for valor in [15, 10, 20, 8, 12, 17, 25]:
        arbol.insertar(valor)
    assert arbol.contiene(12)
    assert arbol.contiene(25)
    assert not arbol.contiene(100)
    assert arbol.esta_balanceado()

