from implementacion import ArbolBinarioBusqueda


def test_arbol_vacio_al_crear():
    """Verifica que un árbol recién creado está vacío y tiene altura 0."""
    arbol = ArbolBinarioBusqueda()
    assert arbol.esta_vacio() is True
    assert arbol.altura() == 0
    assert arbol.inorden() == []


def test_preorden_de_arbol_con_varios_niveles():
    """Verifica que preorden visita raíz, izquierda y derecha en ese orden."""
    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    assert arbol.preorden() == [8, 4, 2, 6, 10, 9, 12]


def test_postorden_de_arbol_con_varios_niveles():
    """Verifica que postorden visita izquierda, derecha y raíz en ese orden."""
    arbol = ArbolBinarioBusqueda()
    for valor in [8, 4, 10, 2, 6, 9, 12]:
        arbol.insertar(valor)
    assert arbol.postorden() == [2, 6, 4, 9, 12, 10, 8]


def test_altura_de_arbol_degenerado():
    """Verifica que un árbol degenerado (una sola rama) tiene altura
    igual a la cantidad de valores insertados, ya que se comporta
    como una lista enlazada."""
    arbol = ArbolBinarioBusqueda()
    valores = [1, 2, 3, 4, 5]
    for valor in valores:
        arbol.insertar(valor)
    assert arbol.altura() == len(valores)
    assert arbol.inorden() == valores


def test_busqueda_de_valor_inexistente():
    """Verifica que contiene() regresa False cuando el valor no está
    en el árbol, incluso si hay valores cercanos."""
    arbol = ArbolBinarioBusqueda()
    for valor in [10, 5, 15, 3, 7]:
        arbol.insertar(valor)
    assert arbol.contiene(100) is False
    assert arbol.contiene(6) is False
    assert arbol.contiene(7) is True


def test_no_permite_valores_duplicados():
    """Verifica que insertar un valor repetido no modifica la
    estructura del árbol (no se crean nodos duplicados)."""
    arbol = ArbolBinarioBusqueda()
    for valor in [5, 3, 8, 3, 5, 8]:
        arbol.insertar(valor)
    assert arbol.inorden() == [3, 5, 8]
    assert arbol.altura() == 2


def test_arbol_con_valores_negativos():
    """Verifica que el árbol organiza correctamente una mezcla de
    valores negativos y positivos, y que inorden los ordena."""
    arbol = ArbolBinarioBusqueda()
    valores = [0, -5, 10, -10, 5, -1]
    for valor in valores:
        arbol.insertar(valor)
    assert arbol.inorden() == sorted(valores)
    assert arbol.contiene(-10) is True
    assert arbol.contiene(-2) is False
