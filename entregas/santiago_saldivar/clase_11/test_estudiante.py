from __future__ import annotations

import pytest

from implementacion import ArbolBinarioBusqueda, Nodo


def construir_arbol_base() -> ArbolBinarioBusqueda:
    """Construye un BST con varios niveles."""

    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    return arbol


def test_agregado_1_altura_mide_niveles():
    """Verifica que la altura sea igual en un árbol de raíz y un hijo que uno de raíz dos hijos."""

    arbol1 = ArbolBinarioBusqueda()
    arbol1.insertar(3)
    arbol1.insertar(2)
    arbol1.insertar(999)

    arbol2 = ArbolBinarioBusqueda()
    arbol2.insertar(3)
    arbol2.insertar(2)

    assert arbol1.altura() == arbol2.altura() 

def test_agregado_2_caso_minimo_recorridos():
    """Verifica que los recorridos funcionen en un árbol con un solo nodo."""

    arbol = ArbolBinarioBusqueda()
    arbol.insertar(1)

    assert arbol.preorden() == [1] == arbol.postorden() == [1] == arbol.inorden() == [1]

def test_agregado_3_inserta_del_lado_correcto():
    """Verifica que los nodos se inserten del lado correcto."""

    arbol = ArbolBinarioBusqueda()
    arbol.insertar(5)
    assert arbol.raiz.valor == 5

    arbol.insertar(3)

    assert arbol.raiz.izquierdo.valor == 3
    assert arbol.raiz.derecho is None

    arbol.insertar(7)
    assert arbol.raiz.derecho.valor == 7