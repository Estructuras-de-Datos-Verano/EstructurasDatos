"""Pruebas públicas guiadas para Nearest Smaller Values.

Estas pruebas son retroalimentación visible. No cubren todos los casos y
contienen espacios TODO para que cada estudiante diseñe pruebas propias.
"""

from __future__ import annotations

from importlib import import_module

import pytest


def cargar_modulo():
    """Carga la implementación del estudiante o el código base."""

    try:
        return import_module("implementacion")
    except ModuleNotFoundError:
        return import_module("src.nearest_smaller")


modulo = cargar_modulo()


def test_ejemplo_oficial_nearest_smaller():
    numeros = [2, 5, 1, 4, 8, 3, 2, 5]
    esperado = [0, 1, 0, 3, 4, 3, 3, 7]
    assert modulo.valores_menores_cercanos(numeros) == esperado


def test_arreglo_creciente():
    numeros = [1, 2, 3, 4, 5]
    esperado = [0, 1, 2, 3, 4]
    assert modulo.valores_menores_cercanos(numeros) == esperado


def test_arreglo_decreciente():
    numeros = [5, 4, 3, 2, 1]
    esperado = [0, 0, 0, 0, 0]
    assert modulo.valores_menores_cercanos(numeros) == esperado


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para valores iguales.")
def test_todo_valores_iguales():
    """TODO alumno: prueba que valores iguales no cuentan como menores.

    Pista: en [3, 3, 3], ninguna posición tiene un valor estrictamente menor
    a la izquierda.
    """

    # Reemplaza este skip por una aserción concreta.
    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba donde usar > en vez de >= fallaría.")
def test_todo_error_comparacion_estricta():
    """TODO alumno: detecta el error de no descartar valores iguales.

    Pista: usa un arreglo donde un valor igual anterior bloquee un menor más
    lejano si la condición del while es incorrecta.
    """

    # Reemplaza este skip por una aserción concreta.
    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba de caso límite.")
def test_todo_caso_limite():
    """TODO alumno: prueba un caso mínimo o muy pequeño.

    Pista: un arreglo de un solo elemento debe regresar [0].
    """

    # Reemplaza este skip por una aserción concreta.
    assert False


@pytest.mark.skip(reason="TODO opcional: prueba la variante Nearest Greater Values.")
def test_todo_variante_nearest_greater():
    """TODO opcional: prueba valores_mayores_cercanos.

    Pista: para [2, 5, 1, 4], la respuesta de mayores cercanos es
    [0, 0, 2, 2].
    """

    # Reemplaza este skip por una aserción concreta si implementas el reto.
    assert False

