"""Pruebas unitarias de estudiantes para validar invariantes y contratos."""

import pytest
from math import inf
from entregas.clase_17.Aristeo.implementacion import (
    ColaLigada,
    DequeLigada,
    bfs_camino,
    cero_uno_bfs,
    camino_cero_uno,
)


def test_1_fifo_cola_ligada():
    """Regla: Los elementos salen exactamente en orden de inserción."""
    cola = ColaLigada[str]()
    cola.encolar("Primero")
    cola.encolar("Segundo")
    cola.encolar("Tercero")
    assert cola.desencolar() == "Primero"
    assert cola.desencolar() == "Segundo"
    assert cola.desencolar() == "Tercero"
    assert cola.esta_vacia()


def test_2_reutilizacion_cola_vaciada():
    """Regla: Vaciar la cola limpia sus referencias y permite volver a usarla desde cero."""
    cola = ColaLigada[int]()
    cola.encolar(1)
    cola.desencolar()
    assert cola._frente is None
    assert cola._final is None
    
    # Reutilización exitosa
    cola.encolar(42)
    assert cola.primero() == 42
    assert len(cola) == 1
    assert cola.desencolar() == 42


def test_3_operaciones_combinadas_deque():
    """Regla: Deque permite mutaciones consistentes y cruzadas de inicio/final."""
    dq = DequeLigada[str]()
    dq.agregar_inicio("B")
    dq.agregar_inicio("A")
    dq.agregar_final("C")
    
    assert dq.primero() == "A"
    assert dq.ultimo() == "C"
    assert len(dq) == 3
    
    assert dq.quitar_final() == "C"
    assert dq.quitar_inicio() == "A"
    assert dq.quitar_inicio() == "B"
    assert dq.esta_vacia()


def test_4_reutilizacion_deque_vaciada():
    """Regla: Vaciar la deque restaura de forma segura todos sus extremos a None."""
    dq = DequeLigada[int]()
    dq.agregar_final(10)
    dq.quitar_inicio()
    assert dq._inicio is None
    assert dq._final is None
    
    dq.agregar_inicio(20)
    assert dq.primero() == 20
    assert dq.ultimo() == 20
    assert dq.quitar_final() == 20


def test_5_bfs_con_ciclo():
    """Regla: BFS debe manejar correctamente ciclos sin entrar en bucles infinitos."""
    grafo_ciclico = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }
    # No debe colgarse y debe retornar el camino directo más corto
    assert bfs_camino(grafo_ciclico, "A", "C") == ["A", "B", "C"]


def test_6_bfs_destino_inalcanzable():
    """Regla: Si no hay ruta al destino, debe devolver una lista vacía []."""
    grafo_inconexo = {
        "A": ["B"],
        "B": [],
        "X": ["Y"],
        "Y": []
    }
    assert bfs_camino(grafo_inconexo, "A", "X") == []


def test_7_cero_uno_bfs_ruta_mas_larga_menor_costo():
    """Regla: 0-1 BFS prioriza el costo acumulado, no el menor número de saltos."""
    # A -> X cuesta 1 (1 salto)
    # A -> B -> C -> X cuesta 0 (3 saltos)
    grafo = {
        "A": [("X", 1), ("B", 0)],
        "B": [("C", 0)],
        "C": [("X", 0)],
        "X": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "X")
    assert costo == 0
    assert camino == ["A", "B", "C", "X"]


def test_8_cero_uno_bfs_peso_invalido():
    """Regla: Pesos que no sean estrictamente enteros 0 o 1 disparan TypeError o ValueError."""
    grafo_invalido_tipo = {
        "A": [("B", 0.5)]
    }
    grafo_invalido_valor = {
        "A": [("B", 2)]
    }
    with pytest.raises(TypeError):
        cero_uno_bfs(grafo_invalido_tipo, "A")
        
    with pytest.raises(ValueError):
        cero_uno_bfs(grafo_invalido_valor, "A")