
from __future__ import annotations

import pytest

from implementacion import ArbolBinarioBusqueda, Nodo

from collections import deque


def construir(valores: list[int]) -> ArbolBinarioBusqueda:
    """Construye un BST insertando los valores en orden."""

    arbol = ArbolBinarioBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def test_agregado_1_balance_mas_eficiente():
    """Compara eficiencia entre balanceado y degenerado."""

    lista1 = [3,4,5,7,9,10,12]
    lista2 = [7,4,10,3,9,5,12]

    arbol1 = construir(lista1)
    arbol2 = construir(lista2)
    assert arbol1.comparaciones_bisqueda(12) > arbol2.comparacines_busqueda(12)

def test_agregado_2_altura_maxima():
    """Verifica que mida la ruta más larga para regresar la altura en el degenerado, pero no en el otro."""

    lista = [7,5,6,4,8,9,10,11,12]
    lista2 = [7,4,10,3,9,5,12]

    arbol = construir(lista)
    arbol2 = construir(lista2)

    assert arbol.altura == 6
    assert arbol2.altura == 3

def test_agregado_3_busqueda_degenerada():
    """Verifica que las comparaciones sigan creciendo según se degenera más el árbol."""

    valores = [1,2,3,4,5,6,7]
    lista = []

    for valor in valores:
        lista.append(valor)
        arbol = construir(lista)

        assert arbol.altura == len(lista)

    valores2 = [7,4,10,3] #9,5,12
    auxiliar = [9, 5, 12]


    for valor in auxiliar:
        valores2.append(auxiliar.popleft())
        arbol2 = construir(valores2)

        assert arbol2.altura == 3


        