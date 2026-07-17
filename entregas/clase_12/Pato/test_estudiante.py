from __future__ import annotations

import pytest

from entregas.clase_12.Pato.implementacion import ArbolBinarioBusqueda, Nodo


def construir(valores: list[int]) -> ArbolBinarioBusqueda:
    """Construye un BST insertando los valores en orden."""

    arbol = ArbolBinarioBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol

def test_comparaciones_igual_altura():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.altura() == arbol.comparaciones_busqueda(14)

def test_cantidad_nodos():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.cantidad_nodos() == 7

def test_es_degenerado():
    arbol1 = construir([1, 2, 3, 4])
    arbol2 = ArbolBinarioBusqueda()
    arbol3 = construir([8])

    assert arbol1.es_degenerado() == True
    assert arbol2.es_degenerado() == False
    assert arbol3.es_degenerado() == True