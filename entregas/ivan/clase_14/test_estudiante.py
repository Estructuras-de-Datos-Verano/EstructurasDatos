import pytest

from implementacion import HeapMin, ultima_piedra


def test_heap_nuevo_esta_vacio():
    heap = HeapMin()
    assert heap.esta_vacio() is True
    assert heap.tamano() == 0


def test_insertar_un_valor_y_consultar_minimo():
    heap = HeapMin()
    heap.insertar(7)
    assert heap.minimo() == 7
    assert heap.tamano() == 1


def test_insertar_varios_conserva_minimo_y_propiedad():
    heap = HeapMin()
    for valor in [7, 3, 9, 1, 6, 5]:
        heap.insertar(valor)
    assert heap.minimo() == 1
    assert heap.cumple_propiedad_heap()


def test_extraer_minimo_devuelve_orden_creciente():
    heap = HeapMin([7, 3, 9, 1, 6, 5])
    assert [heap.extraer_min() for _ in range(6)] == [1, 3, 5, 6, 7, 9]
    assert heap.esta_vacio()


def test_vacio_lanza_error_al_consultar_o_extraer():
    heap = HeapMin()
    with pytest.raises(IndexError):
        heap.minimo()
    with pytest.raises(IndexError):
        heap.extraer_min()


def test_duplicados_y_negativos():
    heap = HeapMin([3, -2, 3, -2, 0])
    assert [heap.extraer_min() for _ in range(5)] == [-2, -2, 0, 3, 3]


def test_construir_heap_reemplaza_contenido():
    heap = HeapMin([99])
    heap.construir_heap([8, 4, 7, 1, 5])
    assert heap.tamano() == 5
    assert heap.minimo() == 1
    assert heap.cumple_propiedad_heap()


def test_varios_sift_up():
    heap = HeapMin([2, 5, 4, 9, 8, 7])
    heap.insertar(1)
    assert heap.minimo() == 1
    assert heap.cumple_propiedad_heap()


def test_varios_sift_down():
    heap = HeapMin([1, 3, 2, 7, 6, 4, 5, 9, 8])
    assert heap.extraer_min() == 1
    assert heap.minimo() == 2
    assert heap.cumple_propiedad_heap()


@pytest.mark.parametrize(
    ("piedras", "esperado"),
    [([], 0), ([5], 5), ([2, 2], 0), ([2, 7, 4, 1, 8, 1], 1)],
)
def test_ultima_piedra(piedras, esperado):
    assert ultima_piedra(piedras) == esperado


def test_insercion_multiples_cambios():
    # Insertar un mínimo global en un heap ya formado hará que suba hasta la raíz
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    heap.insertar(5)
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap()


def test_extraccion_multiples_niveles():
    # Al extraer el 10, el 70 sube a la raíz y tiene que hacer sift-down intercambiándose con el 20 y luego con el 40
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    minimo = heap.extraer_min()
    assert minimo == 10
    assert heap.minimo() == 20
    assert heap.cumple_propiedad_heap()


def test_ultima_piedra_caso_extremo():
    # Caso donde todas las piedras tienen el mismo peso y son una cantidad impar
    assert ultima_piedra([100, 100, 100, 100, 100]) == 100
    # Caso con un peso masivo que pulveriza al resto en cascada
    assert ultima_piedra([1000, 500, 250, 250]) == 0

