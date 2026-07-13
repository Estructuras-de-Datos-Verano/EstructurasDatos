import pytest
from implementacion import HeapMin, ultima_piedra

def test_insercion_con_varios_intercambios():
    """Valida que un elemento suba múltiples niveles hasta la raíz (sift-up)."""
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    heap.insertar(5)
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap() is True

def test_extraccion_con_varios_descensos():
    """Valida que al sacar la raíz, el nuevo elemento baje varios niveles (sift-down)."""
    heap = HeapMin([2, 12, 15, 22, 24, 30, 32, 40, 42])
    assert heap.extraer_min() == 2
    assert heap.minimo() == 12
    assert heap.cumple_propiedad_heap() is True

def test_caso_extremo_ultima_piedra_valores_identicos():
    """Valida el comportamiento de ultima_piedra con elementos homogéneos."""
    assert ultima_piedra([8, 8, 8, 8, 8, 8]) == 0