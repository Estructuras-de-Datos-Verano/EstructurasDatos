import pytest

from entregas.clase_14.Pato.implementacion import HeapMin, ultima_piedra

def test_insercion_multiples_cambios():
    """Prueba que un valor pequeño suba múltiples niveles (sift-up) hasta la raíz."""
    
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
 
    heap.insertar(5)
    
    assert heap.minimo() == 5
    
    assert heap.valores == [5, 10, 30, 20, 50, 60, 70, 40]
    assert heap.cumple_propiedad_heap() is True

def test_extraccion_multiples_descensos():
    """Prueba que al extraer, la nueva raíz baje más de un nivel (sift-down)."""

    heap = HeapMin([5, 10, 15, 20, 25, 30, 35])

    minimo_extraido = heap.extraer_min()

    assert minimo_extraido == 5

    assert heap.minimo() == 10

    assert heap.valores == [10, 20, 15, 35, 25, 30]
    assert heap.cumple_propiedad_heap() is True

def test_ultima_piedra_casos_extremos():
    """Verifica el comportamiento de ultima_piedra ante entradas inusuales."""

    assert ultima_piedra([]) == 0

    assert ultima_piedra([42]) == 42

    assert ultima_piedra([100, 2, 1, 1]) == 96

    assert ultima_piedra([10, 10, 10, 10, 5]) == 5