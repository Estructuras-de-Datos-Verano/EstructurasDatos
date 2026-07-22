from __future__ import annotations

import pytest

from entregas.clase_11.arturo.implementacion import ArbolBinarioBusqueda, Nodo

def test_prueba_de_altura_nodos_flotantes():
    """ Verifica que el cálculo de altura sea consistente incluso con diferentes 
        tipos de inserciones en el árbol."""
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(15)
    assert arbol.altura() == 2

def test_insercion_orden_decreciente():
    """
    Verifica que la estructura se construye correctamente cuando los valores 
    se insertan de mayor a menor, creando un árbol sesgado a la izquierda.
    """

    arbol = ArbolBinarioBusqueda()
    for v in [5, 4, 3, 2, 1]:
        arbol.insertar(v)

    assert arbol.altura() == 5
    assert arbol.inorden() == [1, 2, 3, 4, 5]

def test_manejo_de_tipos_invalidos():
    """
    Verifica que el árbol lance un TypeError al insertar tipos inválidos
    y que mantenga su estado íntegro.
    """
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(10)
    
    # Usamos pytest.raises para verificar que la excepción se lanza
    with pytest.raises(TypeError):
        arbol.insertar("ocho")
        
    # Verificamos que el estado del árbol no se corrompió
    assert arbol.altura() == 1
    assert arbol.contiene(10) is True