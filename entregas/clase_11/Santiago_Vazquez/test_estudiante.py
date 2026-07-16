from __future__ import annotations
from implementacion import ArbolBinarioBusqueda

def test_insercion_secuencia_estrictamente_creciente_altura():
    """Valida la degeneración asintótica del árbol a una estructura lineal O(n)."""
    arbol = ArbolBinarioBusqueda()
    valores = [1, 2, 3, 4, 5]
    for v in valores:
        arbol.insertar(v)
    assert arbol.altura() == 5
    assert arbol.inorden() == [1, 2, 3, 4, 5]

def test_busqueda_cota_inferior_y_superior_ausente():
    """Evalúa que la búsqueda devuelva Falso para elementos fuera de los intervalos del árbol."""
    arbol = ArbolBinarioBusqueda()
    valores = [15, 10, 20]
    for v in valores:
        arbol.insertar(v)
    assert arbol.contiene(5) is False
    assert arbol.contiene(25) is False

def test_recorridos_estructura_simetrica():
    """Verifica la correspondencia lineal de los recorridos preorden y postorden en un subárbol simétrico."""
    arbol = ArbolBinarioBusqueda()
    valores = [10, 5, 15]
    for v in valores:
        arbol.insertar(v)
    assert arbol.preorden() == [10, 5, 15]
    assert arbol.postorden() == [5, 15, 10]