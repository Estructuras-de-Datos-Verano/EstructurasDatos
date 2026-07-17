def test_max1():

    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio()



def test_max2():
    arbol = ArbolBinarioBusqueda()    
    assert arbol == arbol


def test_max3():
    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio()
    assert arbol.altura() == 0
    assert arbol.inorden() == []