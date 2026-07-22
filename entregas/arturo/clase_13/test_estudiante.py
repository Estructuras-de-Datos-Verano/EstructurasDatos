from __future__ import annotations

from entregas.clase_13.arturo.implementacion import ArbolAVL, NodoAVL

def test_rotacion_simple_ll():
    """
    Prueba de Rotación Simple (Caso LL).

    Se insertan tres valores en orden descendente (30, 20, 10) para forzar 
    un peso excesivo en el subárbol izquierdo de la raíz. El árbol debe 
    detectar un factor de balance > 1 y aplicar una rotación derecha.
    """
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(20)
    arbol.insertar(10)

    # La nueva raíz debe ser 20, con 10 a la izquierda y 30 a la derecha
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo is not None and arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho is not None and arbol.raiz.derecho.valor == 30
    assert arbol.esta_balanceado() is True



def test_rotacion_doble_lr():
    """
    Prueba de Rotación Doble (Caso LR).

    Se insertan valores (30, 10, 20) de forma que el desbalance ocurra en
    el hijo derecho del subárbol izquierdo. El árbol debe aplicar primero
    una rotación izquierda en el nodo 10 y luego una rotación derecha en la raíz.
    """
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(10)
    arbol.insertar(20)

    # El resultado estructural debe ser idéntico al caso LL
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo is not None and arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho is not None and arbol.raiz.derecho.valor == 30
    assert arbol.esta_balanceado() is True



def test_propiedades_generales():
    """
    Prueba de Propiedad General: Inorden, Búsqueda y Duplicados.

    Se insertan varios valores desordenados, incluyendo un duplicado.
    Se verifica que:
    1. El duplicado sea ignorado silenciosamente.
    2. El recorrido inorden devuelva la lista estrictamente ordenada.
    3. El método contiene devuelva True para elementos existentes y False para los que no.
    """
    arbol = ArbolAVL()
    valores_a_insertar = [15, 5, 20, 3, 10, 15, 25]  # El 15 está duplicado
    
    for val in valores_a_insertar:
        arbol.insertar(val)

    # Verificación de inorden ordenado y exclusión de duplicado
    assert arbol.inorden() == [3, 5, 10, 15, 20, 25]
    
    # Verificación de búsqueda
    assert arbol.contiene(10) is True
    assert arbol.contiene(100) is False
    
    # El árbol entero debe mantenerse balanceado
    assert arbol.esta_balanceado() is True