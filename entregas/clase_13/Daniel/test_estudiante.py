def test_arbol_grande():

    arbol = construir(list(range(1, 100)))
    assert arbol.inorden() == list(range(1, 100))
    assert arbol.altura() <= 7
    assert arbol.esta_balanceado()

def test_numeros_negativos():

    arbol = construir([-10, -20, -30, -5, -15])
    assert arbol.inorden() == [-30, -20, -15, -10, -5]
    assert arbol.altura() <= 3
    assert arbol.esta_balanceado()

def test_mezcla_numeros_positivos_y_negativos():

    arbol = construir([-10, 20, -30, 5, -15, 25])
    assert arbol.inorden() == [-30, -15, -10, 5, 20, 25]
    assert arbol.altura() <= 3
    assert arbol.esta_balanceado()

    # aqui aparecen en amarillo pero si los pones debajo de los test publicos como ahi
    # si esta definido el construir si jalan