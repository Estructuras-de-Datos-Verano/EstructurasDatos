from implementacion import *

def test_todo_preorden():
    """TODO alumno: verifica el recorrido preorden.

    Pista: para [8, 4, 10, 2, 6], preorden debe empezar con la raíz.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 10, 2, 6]:
        arbol.insertar(v)
    assert arbol.preorden() == [8, 4, 2, 6, 10]



def test_todo_postorden():
    """TODO alumno: verifica el recorrido postorden.

    Pista: en postorden, la raíz aparece al final.
    """
    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 10, 2, 6]:
        arbol.insertar(v)
    assert arbol.postorden() == [2,6,4,10,8]


def test_todo_insercion_en_orden_creciente():
    """TODO alumno: inserta valores crecientes y revisa altura.

    Pista: insertar [1, 2, 3, 4] produce un árbol degenerado de altura 4.
    """
    arbol = ArbolBinarioBusqueda()
    for v in [1, 2, 3, 4]:
        arbol.insertar(v)
    assert arbol.altura() == 4


def test_todo_repetido_no_aparece_dos_veces():
    """TODO alumno: inserta un valor repetido y cuenta apariciones.

    Pista: puedes usar ``arbol.inorden().count(valor)``.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 6, 10, 2, 6, 6]:
        arbol.insertar(v)
    assert arbol.inorden().count(6) == 1


def test_todo_inorden_LEO():
    """
    Construye unárbol y verifica que el método inorden haga lo esperado
    """
    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 10, 2, 6]:
        arbol.insertar(v)
    assert arbol.inorden() == [2,4,6,8,10]


def test_valor_mayor_a_raiz_hijo_derecho_LEO():
    """
    Construye unárbol y verifica que al insertar un valor mayor a la raíz se agrege a la derecha
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(4)
    arbol.insertar(5)
    assert ((arbol.raiz).derecho).valor == 5
    assert (arbol.raiz).izquierdo == None


def test_valor_menor_a_raiz_hijo_izquierdo_LEO():
    """
    Construye unárbol y verifica que al insertar un valor menor a la raíz se agrege a la izquierda
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(4)
    arbol.insertar(3)
    assert (arbol.raiz).derecho == None
    assert ((arbol.raiz).izquierdo).valor == 3