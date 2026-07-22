"""
    Documento de pruebas para la clase ArbolBinarioBusqueda.
"""

from entregas.clase_11.ivan.implementacion import ArbolBinarioBusqueda

def test_altura_cero():
    """ 
    Verifica que la altura de un árbol vacío es cero.
    """
    arbol = ArbolBinarioBusqueda()
    assert arbol.altura() == 0
def test_altura_uno():
    """ 
    Verifica que la altura de un árbol con un solo nodo es uno.
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(8)
    assert arbol.altura() == 1
def test_visualizacion_forma():
    """
    Verifica que la forma del árbol se mantiene correcta después de varias inserciones.
    Árbol: 
            8
           / \
          4   10
         / \   / \
        2   6 9  12
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(8)
    arbol.insertar(4)
    arbol.insertar(10)
    arbol.insertar(2)
    arbol.insertar(6)
    arbol.insertar(9)
    arbol.insertar(12)
    assert arbol._forma == {
        arbol._raiz: 8,
        arbol._raiz.izquierdo: 4,
        arbol._raiz.derecho: 10,
        arbol._raiz.izquierdo.izquierdo: 2,
        arbol._raiz.izquierdo.derecho: 6,
        arbol._raiz.derecho.izquierdo: 9,
        arbol._raiz.derecho.derecho: 12
    }