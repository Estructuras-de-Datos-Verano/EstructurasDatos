"""Pruebas públicas para Josephus Problem I.

Estas pruebas son retroalimentación para estudiantes. No cubren todos los
casos posibles y no sustituyen la discusión técnica ni las pruebas privadas.
"""

from __future__ import annotations

from importlib import import_module

import pytest


def cargar_modulo():
    """Carga la solución del estudiante o, si no existe, el código base."""

    try:
        return import_module("implementacion")
    except ModuleNotFoundError:
        return import_module("src.josephus")


modulo = cargar_modulo()


def test_validar_n_rechaza_cero():
    if not hasattr(modulo, "validar_n"):
        pytest.skip("validar_n solo existe en el código base de apoyo")
    with pytest.raises(ValueError):
        modulo.validar_n(0)


def test_formatear_salida():
    if not hasattr(modulo, "formatear_salida"):
        pytest.skip("formatear_salida solo existe en el código base de apoyo")
    assert modulo.formatear_salida([2, 4, 6, 1]) == "2 4 6 1"


def test_caso_minimo():
    assert modulo.orden_eliminacion(1) == [1]


def test_caso_dos_ninos():
    assert modulo.orden_eliminacion(2) == [2, 1]


def test_ejemplo_oficial():
    assert modulo.orden_eliminacion(7) == [2, 4, 6, 1, 5, 3, 7]


def test_resultado_contiene_todos_los_ninos_una_vez():
    n = 12
    orden = modulo.orden_eliminacion(n)
    assert len(orden) == n
    assert sorted(orden) == list(range(1, n + 1))


def test_resolver_desde_texto_si_existe():
    if not hasattr(modulo, "resolver_desde_texto"):
        pytest.skip("resolver_desde_texto solo existe en el código base de apoyo")
    assert modulo.resolver_desde_texto("7\n") == "2 4 6 1 5 3 7\n"

