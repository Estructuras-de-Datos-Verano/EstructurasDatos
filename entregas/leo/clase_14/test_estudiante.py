from implementacion import *


# TODO del alumno: agrega en test_estudiante.py una inserción con varios cambios.
def test_varios_cambios_por_insercion_LEO():
    """
    Test que inserta un valor menor que el mínimo actual y verifica que el mínimo se actualice correctamente y que la propiedad del heap se mantenga.
    """
    heap = HeapMin([10, 20, 30, 40, 50])
    heap.insertar(5)
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap()
# TODO del alumno: agrega una extracción que descienda más de un nivel.
def test_extraccion_varios_niveles_LEO():
    """
    Test que extrae el mínimo de un heap y verifica que el nuevo mínimo sea correcto y que la propiedad del heap se mantenga.
    """
    heap = HeapMin([1, 6, 7, 7, 8, 7, 8, 9, 10])
    assert heap.extraer_min() == 1
    assert heap.minimo() == 6
    assert heap.cumple_propiedad_heap()
# TODO del alumno: agrega un caso extremo de ultima_piedra.
def test_ultima_piedra_caso_extremo_LEO():
    """
    Test que verifica el comportamiento de la función ultima_piedra con un caso extremo de piedras.
    """
    piedras = [1001, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 8000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
    assert ultima_piedra(piedras) == 1