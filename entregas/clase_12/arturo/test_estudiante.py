from __future__ import annotations

import pytest

from entregas.clase_12.arturo.implementacion import ArbolBinarioBusqueda, Nodo

def test_prueba_altura():
    """ Prueba sencilla que verifica altura en un arbol degenerado """
    arbol = ArbolBinarioBusqueda()
    for v in range(1,10):
        arbol.insertar(v)
    assert arbol.altura() == 9

def tet_prueba_busqueda():
    """ Prueba que verfica el comportamiento de la funcion contiene y busqueda """
    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 12, 2, 6, 10, 14]:
        arbol.insertar(v)

    assert arbol.comparaciones_busqueda(2) == 3
    assert arbol.contiene(2)

def test_prueba_balance():
    """Prueba que un árbol perfectamente balanceado no se marca como degenerado."""
    arbol = ArbolBinarioBusqueda()

    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(15)
    
    assert arbol.es_degenerado() == False
    