"""Pruebas públicas para Clase 13: árboles AVL.

Estas pruebas dan retroalimentación temprana. No cubren todos los casos; cada
estudiante debe escribir al menos tres pruebas propias en ``test_estudiante.py``.
"""

from __future__ import annotations

from implementacion import ArbolAVL, NodoAVL


def construir(valores: list[int]) -> ArbolAVL:
    """Construye un AVL insertando los valores en el orden recibido."""

    arbol = ArbolAVL()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def test_nodo_avl_guarda_valor_y_altura_inicial():
    """Verifica el contrato mínimo de un nodo recién creado."""

    nodo = NodoAVL(10)
    assert nodo.valor == 10
    assert nodo.altura == 1
    assert nodo.izquierdo is None
    assert nodo.derecho is None


def test_arbol_vacio():
    """Un AVL vacío tiene altura 0, recorrido vacío y está balanceado."""

    arbol = ArbolAVL()
    assert arbol.raiz is None
    assert arbol.altura() == 0
    assert arbol.inorden() == []
    assert arbol.esta_balanceado()
    assert not arbol.contiene(5)


def test_insercion_y_busqueda_basica():
    """Insertar valores distintos permite encontrarlos después."""

    arbol = construir([8, 4, 12])
    assert arbol.contiene(8)
    assert arbol.contiene(4)
    assert arbol.contiene(12)
    assert not arbol.contiene(10)
    assert arbol.inorden() == [4, 8, 12]
    assert arbol.esta_balanceado()


def test_caso_ll_aplica_rotacion_derecha():
    """El patrón LL debe producir una rotación derecha local."""

    arbol = construir([30, 20, 10])
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho.valor == 30
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado()


def test_caso_rr_aplica_rotacion_izquierda():
    """El patrón RR debe producir una rotación izquierda local."""

    arbol = construir([10, 20, 30])
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho.valor == 30
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado()


def test_caso_lr_aplica_rotacion_doble():
    """El patrón LR debe aplicar izquierda en el hijo y derecha en el nodo."""

    arbol = construir([30, 10, 20])
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho.valor == 30
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado()


def test_caso_rl_aplica_rotacion_doble():
    """El patrón RL debe aplicar derecha en el hijo e izquierda en el nodo."""

    arbol = construir([10, 30, 20])
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho.valor == 30
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]
    assert arbol.esta_balanceado()


def test_altura_se_mantiene_baja_con_insercion_ordenada():
    """Insertar una secuencia ordenada no debe degenerar el AVL."""

    arbol = construir([1, 2, 3, 4, 5, 6, 7])
    assert arbol.inorden() == [1, 2, 3, 4, 5, 6, 7]
    assert arbol.altura() == 3
    assert arbol.esta_balanceado()


def test_duplicados_no_se_insertan():
    """Los valores duplicados deben ignorarse según el contrato del curso."""

    arbol = construir([8, 4, 12, 4, 8, 12])
    assert arbol.inorden() == [4, 8, 12]
    assert arbol.altura() == 2
    assert arbol.esta_balanceado()
