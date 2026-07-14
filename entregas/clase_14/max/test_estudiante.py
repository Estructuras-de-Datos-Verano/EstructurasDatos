import pytest

from implementacion import HeapMin, ultima_piedra

def test_max1():
    heap = HeapMin([2, 5, 4, 8, 9, 7, 10])
    heap.insertar(1)
    
    assert heap.minimo() == 1
    assert heap.tamano() == 8
    assert heap.cumple_propiedad_heap()

def test_max2():

    heap = HeapMin([1, 2, 4, 3, 5, 7, 6, 9])
    assert heap.extraer_min() == 1
    assert heap.minimo() == 2 
    assert heap.cumple_propiedad_heap()

def test_max3():
    piedras_extremas = [1000, 1000, 500, 500, 1, 1, 45, 45]
    assert ultima_piedra(piedras_extremas) == 0
