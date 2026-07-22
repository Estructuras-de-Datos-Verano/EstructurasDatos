from __future__ import annotations

import pytest

from entregas.clase_11.Pato.implementacion import ArbolBinarioBusqueda, Nodo

def construir_arbol_base() -> ArbolBinarioBusqueda:
    """Construye un BST con varios niveles."""

    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    return arbol

def test_inorden():
    arbol = construir_arbol_base()
    assert arbol.inorden() == [2, 4, 6, 8, 9, 10, 12]

def test_altura_entradas_nones():
    arbol = ArbolBinarioBusqueda()
    for valor in [4, 5, 7, 2, 3, 6, 9]:
        arbol.insertar(valor)
    assert arbol.altura() == 4

def test_postorden_inorden_con_dos_arboles():
    arbol1 = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6]:
        arbol1.insertar(valor)

    arbol2 = ArbolBinarioBusqueda()
    for valor in [4, 2, 8, 6, 10]:
        arbol2.insertar(valor)

    assert arbol1.postorden() != arbol2.postorden()
    assert arbol1.inorden() == arbol2.inorden()