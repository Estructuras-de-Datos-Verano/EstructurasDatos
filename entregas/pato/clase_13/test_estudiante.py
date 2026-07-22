from __future__ import annotations

from entregas.clase_13.Pato.implementacion import ArbolAVL, NodoAVL


def construir(valores: list[int]) -> ArbolAVL:
    """Construye un AVL insertando los valores en el orden recibido."""

    arbol = ArbolAVL()
    for valor in valores:
        arbol.insertar(valor)
    return arbol

def test_insercion_descendente():
    """Insertar una secuencia descendente no debe degenerar el AVL."""
    
    arbol = construir([50, 40, 30, 20, 10])
    assert arbol.inorden() == [10, 20, 30, 40, 50]
    assert arbol.altura() == 3
    assert arbol.esta_balanceado()

def test_insercion_valores_negativos():
    """El AVL debe manejar correctamente números negativos y el cero."""
    
    arbol = construir([0, -10, 5, -20])
    assert arbol.contiene(-10)
    assert arbol.contiene(0)
    assert not arbol.contiene(-5)
    assert arbol.inorden() == [-20, -10, 0, 5]
    assert arbol.esta_balanceado()

def test_alturas_internas_nodos():
    
    arbol = construir([20, 10, 30, 40])
    
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.altura == 3
    assert arbol.raiz.izquierdo is not None
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.izquierdo.altura == 1
    assert arbol.raiz.derecho is not None
    assert arbol.raiz.derecho.valor == 30
    assert arbol.raiz.derecho.altura == 2
    assert arbol.raiz.derecho.derecho is not None
    assert arbol.raiz.derecho.derecho.valor == 40
    assert arbol.raiz.derecho.derecho.altura == 1
    assert arbol.esta_balanceado()