from implementacion import ArbolAVL

def test_rotacion_simple_rr():
    """
    Verifica que una inserción secuencial ascendente (10, 20, 30)
    provoque una rotación simple a la izquierda (Caso RR) y la raíz cambie a 20.
    """
    arbol = ArbolAVL()
    arbol.insertar(10)
    arbol.insertar(20)
    arbol.insertar(30)
    
    assert arbol.raiz.valor == 20
    assert arbol.esta_balanceado()
    assert arbol.inorden() == [10, 20, 30]

def test_rotacion_doble_lr():
    """
    Verifica que el caso Izquierda-Derecha (LR) balancee correctamente el árbol
    mediante una rotación doble (izquierda sobre el hijo, derecha sobre la raíz).
    """
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(10)
    arbol.insertar(20)
    
    assert arbol.raiz.valor == 20
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]

def test_propiedad_inorden_y_balance_masivo():
    """
    Inserta múltiples elementos desordenados y valida que el recorrido inorden
    permanezca perfectamente ordenado y la propiedad AVL se mantenga intacta.
    """
    arbol = ArbolAVL()
    valores = [50, 25, 75, 15, 35, 60, 120, 10, 68]
    
    for v in valores:
        arbol.insertar(v)
        
    assert arbol.esta_balanceado()
    assert arbol.inorden() == sorted(valores)