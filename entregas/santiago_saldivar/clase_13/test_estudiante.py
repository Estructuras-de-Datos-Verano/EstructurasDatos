
from __future__ import annotations
from implementacion import ArbolAVL, NodoAVL
def construir(valores: list[int]) -> ArbolAVL:
    """Construye un AVL insertando los valores en el orden recibido."""

    arbol = ArbolAVL()
    for valor in valores:
        arbol.insertar(valor)
    return arbol

#10
def test_agregado_1_revisa_balance_en_aumento():
    """Revisa que se mantenga el balance según aumenta."""
    lista = [10,30,20]
    auxiliar =[]
    for valor in lista:
        auxiliar.append(valor)
        arbol = construir(auxiliar)
        assert arbol.esta_balanceado()
#11
def test_agregado_2_revisa_altura_maximo():
    """Revisa que la altura no crezca demasiado"""
    lista = [7,1,2,3,8,9,10]
    auxiliar = []

    for valor in lista:
        auxiliar.append(valor)
        arbol = construir(auxiliar)
        assert arbol.altura() < len(lista)

#12
def test_agregado_3_insercion_balanceada_persiste():
    """Revisa que no haga cambios innecesarios."""
    lista = [7,4,10,3,9,5,12]
    arbol = construir(lista)
    assert arbol.raiz.valor == 7
    assert arbol.raiz.izquierdo.valor == 4
    assert arbol.raiz.derecho.valor == 10
    assert arbol.raiz.izquierdo.izquierdo.valor == 3
    assert arbol.raiz.izquierdo.derecho.valor == 5
    assert arbol.raiz.derecho.izquierdo.valor == 9
    assert arbol.raiz.derecho.derecho.valor == 12