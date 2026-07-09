from implementacion import ArbolBinarioBusqueda

def test_todo_busqueda_balanceada():
    """Verifica comparaciones para un objetivo en un árbol balanceado.
    
    Pista: en [8, 4, 12, 2, 6, 10, 14], buscar 2 visita 8, 4 y 2.
    """
    arbol = ArbolBinarioBusqueda()
    for v in [8, 4, 12, 2, 6, 10, 14]:
        arbol.insertar(v)
        
    # El valor 2 está en el tercer nivel, por lo que toma 3 comparaciones
    assert arbol.comparaciones_busqueda(2) == 3


def test_todo_busqueda_degenerada():
    """Verifica comparaciones en un árbol que parece lista.
    
    Pista: insertar [1, 2, 3, 4] y buscar 4 requiere 4 comparaciones.
    """
    arbol = ArbolBinarioBusqueda()
    for v in [1, 2, 3, 4]:
        arbol.insertar(v)
        
    # Como es degenerado (lista), buscar el último insertado toma n comparaciones
    assert arbol.comparaciones_busqueda(4) == 4


def test_todo_insercion_ordenada_altura_maxima():
    """Comprueba que insertar valores ordenados produce altura máxima.
    
    Pista: para n valores distintos insertados en orden creciente, la altura debe ser n.
    """
    arbol = ArbolBinarioBusqueda()
    n = 5
    # Insertamos 5 valores en orden creciente
    for v in [10, 20, 30, 40, 50]:
        arbol.insertar(v)
        
    # La altura debe coincidir exactamente con el número de elementos (n)
    assert arbol.altura() == n