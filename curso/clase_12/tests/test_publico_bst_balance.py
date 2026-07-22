"""Pruebas públicas guiadas para altura, balance y degeneración en BST."""

from __future__ import annotations

import pytest

from implementacion import ArbolBinarioBusqueda, Nodo


def construir(valores: list[int]) -> ArbolBinarioBusqueda:
    """Construye un BST insertando los valores en orden."""

    arbol = ArbolBinarioBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def test_nodo_guarda_valor_y_empieza_sin_hijos():
    nodo = Nodo(10)
    assert nodo.valor == 10
    assert nodo.izquierdo is None
    assert nodo.derecho is None


def test_altura_de_arbol_vacio():
    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio()
    assert arbol.altura() == 0
    assert arbol.cantidad_nodos() == 0
    assert arbol.comparaciones_busqueda(8) == 0


def test_altura_de_arbol_con_raiz():
    arbol = construir([8])
    assert not arbol.esta_vacio()
    assert arbol.altura() == 1
    assert arbol.cantidad_nodos() == 1
    assert arbol.comparaciones_busqueda(8) == 1


def test_altura_de_arbol_balanceado():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.altura() == 3
    assert arbol.cantidad_nodos() == 7
    assert not arbol.es_degenerado()


def test_altura_de_arbol_degenerado():
    arbol = construir([1, 2, 3, 4, 5])
    assert arbol.altura() == 5
    assert arbol.cantidad_nodos() == 5
    assert arbol.es_degenerado()


def test_inorden_sigue_regresando_valores_ordenados():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.inorden() == [2, 4, 6, 8, 10, 12, 14]


def test_busqueda_con_conteo_de_comparaciones_balanceado():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.contiene(10)
    assert arbol.comparaciones_busqueda(10) == 3
    assert arbol.comparaciones_busqueda(7) == 3


def test_busqueda_con_conteo_de_comparaciones_degenerado():
    arbol = construir([1, 2, 3, 4, 5])
    assert arbol.contiene(5)
    assert arbol.comparaciones_busqueda(5) == 5
    assert arbol.comparaciones_busqueda(6) == 5


def test_duplicados_no_aumentan_cantidad_de_nodos():
    arbol = construir([8, 4, 12, 4, 8, 12])
    assert arbol.cantidad_nodos() == 3
    assert arbol.inorden() == [4, 8, 12]


@pytest.mark.skip(reason="TODO alumno: diseña una prueba de búsqueda en árbol balanceado.")
def test_todo_busqueda_balanceada():
    """TODO alumno: verifica comparaciones para un objetivo en un árbol balanceado.

    Pista: en [8, 4, 12, 2, 6, 10, 14], buscar 2 visita 8, 4 y 2.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba de búsqueda en árbol degenerado.")
def test_todo_busqueda_degenerada():
    """TODO alumno: verifica comparaciones en un árbol que parece lista.

    Pista: insertar [1, 2, 3, 4] y buscar 4 requiere 4 comparaciones.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba de altura máxima por inserción ordenada.")
def test_todo_insercion_ordenada_altura_maxima():
    """TODO alumno: comprueba que insertar valores ordenados produce altura máxima.

    Pista: para n valores distintos insertados en orden creciente, la altura debe ser n.
    """

    assert False
