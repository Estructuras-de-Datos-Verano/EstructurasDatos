"""Pruebas públicas guiadas para grafos.

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
        return import_module("src.grafos")


modulo = cargar_modulo()
ES_CODIGO_BASE = modulo.__name__ == "src.grafos"


def requiere_implementacion() -> None:
    """Omite pruebas de comportamiento cuando solo está el stub público."""

    if ES_CODIGO_BASE:
        pytest.skip("El código base no contiene implementación completa")


IMPLEMENTACIONES = [
    "GrafoListaAdyacencia",
    "GrafoMatrizAdyacencia",
]


@pytest.fixture(params=IMPLEMENTACIONES)
def clase_grafo(request):
    """Regresa cada implementación de grafo disponible."""

    requiere_implementacion()
    return getattr(modulo, request.param)


def test_existen_clases_requeridas():
    assert hasattr(modulo, "GrafoAbstracto")
    assert hasattr(modulo, "GrafoListaAdyacencia")
    assert hasattr(modulo, "GrafoMatrizAdyacencia")


def test_existen_funciones_auxiliares():
    assert hasattr(modulo, "construir_grafo_ejemplo")
    assert hasattr(modulo, "convertir_a_networkx")
    assert hasattr(modulo, "guardar_visualizacion_grafo")


def test_crear_grafo_vacio(clase_grafo):
    grafo = clase_grafo()
    assert grafo.cantidad_vertices() == 0
    assert grafo.cantidad_aristas() == 0


def test_agregar_vertice(clase_grafo):
    grafo = clase_grafo()
    grafo.agregar_vertice("A")
    assert grafo.contiene_vertice("A")
    assert grafo.cantidad_vertices() == 1


def test_agregar_arista_agrega_vertices(clase_grafo):
    grafo = clase_grafo()
    grafo.agregar_arista("A", "B")
    assert grafo.contiene_vertice("A")
    assert grafo.contiene_vertice("B")
    assert grafo.cantidad_vertices() == 2
    assert grafo.cantidad_aristas() == 1


def test_arista_no_dirigida_aparece_en_ambos_sentidos(clase_grafo):
    grafo = clase_grafo()
    grafo.agregar_arista("A", "B")
    assert "B" in grafo.vecinos("A")
    assert "A" in grafo.vecinos("B")


def test_vecinos_en_grafo_pequeno(clase_grafo):
    grafo = clase_grafo()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    assert set(grafo.vecinos("A")) == {"B", "C"}


def test_convertir_a_networkx():
    requiere_implementacion()
    pytest.importorskip("networkx")

    grafo = modulo.GrafoListaAdyacencia()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")

    grafo_nx = modulo.convertir_a_networkx(grafo)
    assert set(grafo_nx.nodes()) == {"A", "B", "C"}
    assert {frozenset(arista) for arista in grafo_nx.edges()} == {
        frozenset(("A", "B")),
        frozenset(("B", "C")),
    }


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para aristas duplicadas.")
def test_todo_arista_duplicada_no_aumenta_conteo():
    """TODO alumno: verifica que agregar la misma arista dos veces no duplica.

    Pista: agrega ``A``--``B`` dos veces y revisa que la cantidad de aristas
    siga siendo 1.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: compara vecinos entre ambas implementaciones.")
def test_todo_mismas_vecindades_en_ambas_implementaciones():
    """TODO alumno: construye el mismo grafo con ambas implementaciones.

    Pista: usa conjuntos para comparar vecinos sin depender del orden.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para un vértice aislado.")
def test_todo_vertice_sin_vecinos():
    """TODO alumno: prueba un vértice que existe pero no tiene aristas.

    Pista: ``vecinos("A")`` debería regresar una lista vacía.
    """

    assert False


@pytest.mark.skip(reason="TODO alumno: diseña una prueba para contiene_arista.")
def test_todo_contiene_arista():
    """TODO alumno: verifica aristas existentes e inexistentes.

    Pista: en un grafo con ``A``--``B``, ``contiene_arista("A", "B")`` y
    ``contiene_arista("B", "A")`` deberían ser verdaderas.
    """

    assert False
