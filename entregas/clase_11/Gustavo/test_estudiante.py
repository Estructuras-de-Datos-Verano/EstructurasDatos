def test_todo_preorden():
    """TODO alumno: verifica el recorrido preorden."""
    arbol = construir_arbol_base()
    # Raíz, Izquierda, Derecha
    assert arbol.preorden() == [8, 4, 2, 6, 10, 9, 12]

def test_todo_postorden():
    """TODO alumno: verifica el recorrido postorden."""
    arbol = construir_arbol_base()
    # Izquierda, Derecha, Raíz
    assert arbol.postorden() == [2, 6, 4, 9, 12, 10, 8]

def test_todo_insercion_en_orden_creciente():
    """TODO alumno: inserta valores crecientes y revisa altura."""
    arbol = ArbolBinarioBusqueda()
    for valor in [1, 2, 3, 4]:
        arbol.insertar(valor)
    # Al insertar en orden, el árbol se hace una línea recta (degenerado)
    assert arbol.altura() == 4

def test_todo_repetido_no_aparece_dos_veces():
    """TODO alumno: inserta un valor repetido y cuenta apariciones."""
    arbol = construir_arbol_base()
    arbol.insertar(8)  # 8 ya es la raíz, es un repetido
    assert arbol.inorden().count(8) == 1