def test_varios_cambios():
    heap = HeapMin([10, 20, 15, 30, 40])
    heap.insertar(5)
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap()
    assert heap.extraer_min() == 5
    assert heap.minimo() == 10
    assert heap.cumple_propiedad_heap()

def desciende_mas_de_un_nivel():
    heap = HeapMin([1, 3, 2, 7, 6, 4, 5, 9, 8])
    assert heap.extraer_min() == 1
    assert heap.minimo() == 2
    assert heap.cumple_propiedad_heap()
    assert heap.extraer_min() == 2
    assert heap.minimo() == 3
    assert heap.cumple_propiedad_heap()

def test_ultima_piedra_extremo():
    piedras = [1] * 1000 + [2] * 1000
    assert ultima_piedra(piedras) == 0

    ## algunas cosas que se me ocurrieron para testear el heap
    ## hay algunos errores que ya en el archivo test_publico_heap.py si corren por que ahi estan ya defidas
    ## saludos : 0