"""Pruebas propias para la Clase 13: árboles AVL."""

from implementacion import ArbolAVL


def test_estudiante_insercion_masiva_mantiene_altura_logaritmica():
    """Verifica una propiedad general: al insertar 15 elementos en orden, 
    el árbol se autobalancea perfectamente manteniendo una altura de 4.
    """
    arbol = ArbolAVL()
    # Insertamos en el peor caso posible para un BST (ascendente)
    for i in range(1, 16):
        arbol.insertar(i)
    
    # Un árbol AVL perfecto de 15 nodos debe tener exactamente altura 4 (2^4 - 1 = 15)
    assert arbol.altura() == 4
    assert arbol.esta_balanceado()
    
    # Verificamos que las búsquedas funcionen para todos los nodos
    for i in range(1, 16):
        assert arbol.contiene(i)


def test_estudiante_rotacion_rr_en_subarbol():
    """Cubre rotación simple (RR) aplicada en una rama interna, no en la raíz principal."""
    arbol = ArbolAVL()
    
    # Creamos un árbol base balanceado
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    
    # Forzamos un desbalance RR en el subárbol derecho (nodo 70)
    arbol.insertar(80)
    arbol.insertar(90)
    
    # La raíz no debió cambiar
    assert arbol.raiz.valor == 50
    # El subárbol derecho (originalmente 70) debió rotar a la izquierda, subiendo el 80
    assert arbol.raiz.derecho.valor == 80
    assert arbol.raiz.derecho.izquierdo.valor == 70
    assert arbol.raiz.derecho.derecho.valor == 90
    
    # Verificamos inorden y balance
    assert arbol.inorden() == [30, 50, 70, 80, 90]
    assert arbol.esta_balanceado()


def test_estudiante_rotacion_lr_en_subarbol():
    """Cubre rotación doble (LR) aplicada en una rama interna, no en la raíz principal."""
    arbol = ArbolAVL()
    
    # Creamos un árbol base balanceado
    arbol.insertar(50)
    arbol.insertar(80)
    arbol.insertar(30)
    
    # Forzamos un desbalance LR en el subárbol izquierdo (nodo 30)
    # 30 está desbalanceado hacia la izquierda-derecha al insertar 10 y luego 20
    arbol.insertar(10)
    arbol.insertar(20)
    
    # La raíz no debió cambiar
    assert arbol.raiz.valor == 50
    # El subárbol izquierdo (originalmente 30) debió aplicar LR, subiendo el 20
    assert arbol.raiz.izquierdo.valor == 20
    assert arbol.raiz.izquierdo.izquierdo.valor == 10
    assert arbol.raiz.izquierdo.derecho.valor == 30
    
    # Verificamos inorden y balance
    assert arbol.inorden() == [10, 20, 30, 50, 80]
    assert arbol.esta_balanceado()