
from __future__ import annotations

from implementacion import ArbolBinarioBusqueda


def construir(valores: list[int]) -> ArbolBinarioBusqueda:
    arbol = ArbolBinarioBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def test_busqueda_en_arbol_balanceado_cuenta_comparaciones_correctas():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])

    assert arbol.comparaciones_busqueda(2) == 3
    assert arbol.comparaciones_busqueda(7) == 3


def test_insercion_ordenada_produce_altura_maxima_y_arbol_degenerado():
    arbol = construir([1, 2, 3, 4, 5])

    assert arbol.altura() == 5
    assert arbol.es_degenerado() is True


def test_recorrido_preorden_y_postorden_son_coherentes():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])

    assert arbol.preorden() == [8, 4, 2, 6, 12, 10, 14]
    assert arbol.postorden() == [2, 6, 4, 10, 14, 12, 8]
