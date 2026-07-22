
#Acá lo que esta haciendo es que esta construyendo un arbol, y en el esta checando que la altura del arbol sea la correcta.
def test_max1():
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(14)
    arbol.insertar(12)
    arbol.insertar(13)
    arbol.insertar(4)
    arbol.insertar(5)
    assert arbol.altura() == 4

#Acá lo que esta haciendo es que esta intentando que en la busqueda del nodo este si contenga el valor que le debe de corresponder.
def test_max2():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.comparaciones_busqueda(3) == 3

#Acá e esta revisando que el arbol se este generando de manera correcta
def test_max3():
    arbol = construir([8, 4, 12, 2, 6, 10, 14, 4])
    assert arbol.cantidad_nodos() == 7
    assert arbol.inorden() == [2, 4, 6, 8, 10, 12, 14]