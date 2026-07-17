"""Pruebas públicas guiadas para árboles binarios de búsqueda."""

from __future__ import annotations

import pytest

from implementacion import ArbolBinarioBusqueda, Nodo


def construir_arbol_base() -> ArbolBinarioBusqueda:
    """Construye un BST con varios niveles."""

    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    return arbol


def test_nodo_guarda_valor_y_empieza_sin_hijos():
    nodo = Nodo(10)
    assert nodo.valor == 10
    assert nodo.izquierdo is None
    assert nodo.derecho is None


def test_crear_arbol_vacio():
    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio()
    assert arbol.altura() == 0
    assert arbol.inorden() == []


def test_arbol_vacio_no_contiene_valores():
    arbol = ArbolBinarioBusqueda()
    assert not arbol.contiene(8)


def test_insertar_un_valor():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(8)
    assert not arbol.esta_vacio()
    assert arbol.contiene(8)
    assert arbol.altura() == 1


def test_buscar_valor_existente_e_inexistente():
    arbol = construir_arbol_base()
    assert arbol.contiene(6)
    assert arbol.contiene(12)
    assert not arbol.contiene(7)
    assert not arbol.contiene(100)


def test_insertar_varios_valores_inorden_ordenado():
    arbol = construir_arbol_base()
    assert arbol.inorden() == [2, 4, 6, 8, 9, 10, 12]


def test_altura_de_arbol_con_varios_niveles():
    arbol = construir_arbol_base()
    assert arbol.altura() == 3


def test_no_insertar_duplicados():
    arbol = construir_arbol_base()
    arbol.insertar(4)
    arbol.insertar(8)
    assert arbol.inorden() == [2, 4, 6, 8, 9, 10, 12]


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para preorden.")
def test_todo_preorden():
    """TODO alumno: verifica el recorrido preorden.

    Pista: para [8, 4, 10, 2, 6], preorden debe empezar con la raíz.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para postorden.")
def test_todo_postorden():
    """TODO alumno: verifica el recorrido postorden.

    Pista: en postorden, la raíz aparece al final.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para inserción creciente.")
def test_todo_insercion_en_orden_creciente():
    """TODO alumno: inserta valores crecientes y revisa altura.

    Pista: insertar [1, 2, 3, 4] produce un árbol degenerado de altura 4.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: comprueba que un repetido no aparece dos veces.")
def test_todo_repetido_no_aparece_dos_veces():
    """TODO alumno: inserta un valor repetido y cuenta apariciones.

    Pista: puedes usar ``arbol.inorden().count(valor)``.
    """

    assert False
