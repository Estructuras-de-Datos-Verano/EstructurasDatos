from implementacion import *

def test_todo_busqueda_balanceada():
    """TODO alumno: verifica comparaciones para un objetivo en un árbol balanceado.

    Pista: en [8, 4, 12, 2, 6, 10, 14], buscar 2 visita 8, 4 y 2.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 12, 2, 6, 10, 14]:
        arbol.insertar(v)
    assert arbol.comparaciones_busqueda(8) == 1
    assert arbol.comparaciones_busqueda(4) == 2
    assert arbol.comparaciones_busqueda(2) == 3




def test_todo_busqueda_degenerada():
    """TODO alumno: verifica comparaciones en un árbol que parece lista.

    Pista: insertar [1, 2, 3, 4] y buscar 4 requiere 4 comparaciones.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [1, 2, 3, 4]:
        arbol.insertar(v)
    assert arbol.comparaciones_busqueda(4) == 4


# @pytest.mark.skip(reason="TODO alumno: diseña una prueba de altura máxima por inserción ordenada.")
def test_todo_insercion_ordenada_altura_maxima():
    """TODO alumno: comprueba que insertar valores ordenados produce altura máxima.

    Pista: para n valores distintos insertados en orden creciente, la altura debe ser n.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        arbol.insertar(v)
    assert arbol.altura() == arbol.cantidad_nodos() 
    assert arbol.altura() == 20

def test_arbol_balanceado_altura_no_es_num_nodos_LEO():
    """
    Test en el que queremos verificar que en un arbol balanceado, la altura siempre es menor al número de nodos
    """

    arbol = ArbolBinarioBusqueda()
    for v in [50, 25, 75, 13, 37, 63, 87]:
        arbol.insertar(v)
    assert not arbol.altura() == arbol.cantidad_nodos
    assert arbol.altura() < arbol.cantidad_nodos()

def test_busqueda_en_arbol_vacio_es_0_LEO():
    """
    Test en el que queremos verificar que en un arbol vacío, el número de comparaciones hechas para encontrar un valor es 0
    """

    arbol = ArbolBinarioBusqueda()
    assert arbol.comparaciones_busqueda(7) == 0


def test_arbol_vacio_no_es_degenerado_LEO():
    """
    Test en el que queremos verificar que un árbol vacío no es degenerado
    """

    arbol = ArbolBinarioBusqueda()
    assert not arbol.es_degenerado() 