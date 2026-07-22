from __future__ import annotations

from copy import deepcopy

import pytest

from entregas.clase_19.arturo.implementacion import orden_topologico, es_orden_topologico

def test_varios_ordenes_validos_ARTURO():
    """
    Regla: Si un grafo admite múltiples secuencias topológicas válidas, la función
    debe devolver alguna de ellas, y el validador debe aceptarla como correcta.
    Entrada: A -> C y B -> C. (Admite [A, B, C] y [B, A, C]).
    """
    grafo = {"A": ["C"], "B": ["C"]}
    orden = orden_topologico(grafo)
    
    assert orden is not None, "El grafo es un DAG, no debe devolver None."
    assert es_orden_topologico(grafo, orden), "El orden devuelto debe ser lógicamente válido."
    
    # Comprobamos que el validador acepta ambas secuencias posibles
    assert es_orden_topologico(grafo, ["A", "B", "C"]) is True
    assert es_orden_topologico(grafo, ["B", "A", "C"]) is True


def test_ciclo_simple_ARTURO():
    """
    Regla: Si el grafo contiene un ciclo completo, es imposible ordenarlo
    topológicamente. La función debe detectarlo y devolver None.
    Entrada: A -> B y B -> A.
    """
    grafo = {"A": ["B"], "B": ["A"]}
    orden = orden_topologico(grafo)
    
    assert orden is None, "Un ciclo simple debe invalidar el orden topológico y devolver None."


def test_ciclo_parcial_ARTURO():
    """
    Regla: Incluso si una parte del grafo es acíclica (D -> E), un ciclo en otra 
    componente (A -> B -> C -> A) bloquea la resolución completa del grafo.
    Entrada: Grafo mixto.
    """
    grafo = {
        "D": ["E"], 
        "E": [],
        "A": ["B"], 
        "B": ["C"], 
        "C": ["A"]
    }
    orden = orden_topologico(grafo)
    
    assert orden is None, "Un ciclo en cualquier parte del grafo debe devolver None."


def test_vecino_implicito_ARTURO():
    """
    Regla: Si un destino existe dentro de una lista de adyacencia pero no tiene 
    su propia clave en el diccionario (vecino implícito), debe incluirse en el resultado.
    Entrada: {"A": ["B"]} (B no tiene lista de salida).
    """
    grafo = {"A": ["B"]}
    orden = orden_topologico(grafo)
    
    assert orden == ["A", "B"], "El vecino implícito 'B' debe normalizarse e incluirse."



def test_dependencias_duplicadas_ARTURO():
    """
    Regla: Si una arista se declara varias veces (A -> B, A -> B), el grado de 
    entrada de B no debe alterarse de forma engañosa, y el orden debe resolverse.
    Entrada: {"A": ["B", "B", "B"]}
    """
    grafo = {"A": ["B", "B", "B"], "B": []}
    orden = orden_topologico(grafo)
    
    assert orden == ["A", "B"], "Las dependencias duplicadas deben estabilizarse y resolverse."


@pytest.mark.parametrize("orden_invalido", [
    ["B", "A", "C"], # Falla: B antes que A (viola A -> B)
    ["A", "C", "B"], # Falla: C antes que B (viola B -> C)
    ["A", "B"],      # Falla: Longitud incorrecta (omite C)
    ["A", "B", "C", "D"] # Falla: Nodos desconocidos (incluye D)
])
def test_orden_incorrecto_es_rechazado_ARTURO(orden_invalido):
    """
    Regla: El validador `es_orden_topologico` debe rechazar rigurosamente secuencias 
    que violen las reglas de precedencia, tengan omisiones o incluyan nodos inexistentes.
    Grafo original: A -> B -> C
    """
    grafo = {"A": ["B"], "B": ["C"], "C": []}
    
    assert not es_orden_topologico(grafo, orden_invalido), f"El orden {orden_invalido} debería ser rechazado."