def testmax1():
    arbol = construir([1, 2, 5, 6, 7])
    assert arbol.inorden() == [1, 2, 5, 6, 7]
    assert arbol.altura() == 3
    assert arbol.esta_balanceado()

def testmax2():
    arbol = construir([1, 2, 5, 6, 7])
    assert arbol.inorden() == [1, 2, 5, 6, 7, 3, 4, 8, 9]
    assert arbol.esta_balanceado()

def testmax3():
    arbol = construir([1, 2, 5, 6, 7])
    assert arbol.inorden() == [1, 2, 5]
    assert arbol.altura() == 2