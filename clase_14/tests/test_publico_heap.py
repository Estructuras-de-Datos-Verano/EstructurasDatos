"""Pruebas públicas de Clase 14; evaluar.py agrega la entrega a sys.path."""

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


# TODO del alumno: agrega en test_estudiante.py una inserción con varios cambios.
# TODO del alumno: agrega una extracción que descienda más de un nivel.
# TODO del alumno: agrega un caso extremo de ultima_piedra.

