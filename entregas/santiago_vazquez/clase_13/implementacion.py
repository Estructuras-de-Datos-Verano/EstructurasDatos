from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NodoAVL:
    valor: int
    izquierdo: NodoAVL | None = None
    derecho: NodoAVL | None = None
    altura: int = 1


class ArbolAVL:

    def __init__(self) -> None:
        self.raiz: NodoAVL | None = None

    def insertar(self, valor: int) -> None:
 
        def _insertar_interno(nodo: NodoAVL | None) -> NodoAVL:
            if nodo is None:
                return NodoAVL(valor)

            if valor < nodo.valor:
                nodo.izquierdo = _insertar_interno(nodo.izquierdo)
            elif valor > nodo.valor:
                nodo.derecho = _insertar_interno(nodo.derecho)
            else:
                return nodo

            self._actualizar_altura(nodo)
            fb = self._factor_balance(nodo)

    
            if fb > 1 and valor < nodo.izquierdo.valor:
                return self._rotar_derecha(nodo)
           
            if fb < -1 and valor > nodo.derecho.valor:
                return self._rotar_izquierda(nodo)
          
            if fb > 1 and valor > nodo.izquierdo.valor:
                nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
                return self._rotar_derecha(nodo)
         
            if fb < -1 and valor < nodo.derecho.valor:
                nodo.derecho = self._rotar_derecha(nodo.derecho)
                return self._rotar_izquierda(nodo)

            return nodo

        self.raiz = _insertar_interno(self.raiz)

    def contiene(self, valor: int) -> bool:
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return False

    def altura(self) -> int:
        return self._altura(self.raiz)

    def inorden(self) -> list[int]:

        if self.raiz is None:
            return []

        izq_arbol = ArbolAVL()
        izq_arbol.raiz = self.raiz.izquierdo

        der_arbol = ArbolAVL()
        der_arbol.raiz = self.raiz.derecho

        return izq_arbol.inorden() + [self.raiz.valor] + der_arbol.inorden()

    def esta_balanceado(self) -> bool:

        if self.raiz is None:
            return True

        if abs(self._factor_balance(self.raiz)) > 1:
            return False

        izq_arbol = ArbolAVL()
        izq_arbol.raiz = self.raiz.izquierdo

        der_arbol = ArbolAVL()
        der_arbol.raiz = self.raiz.derecho

        return izq_arbol.esta_balanceado() and der_arbol.esta_balanceado()

    def _altura(self, nodo: NodoAVL | None) -> int:
        if nodo is None:
            return 0
        return nodo.altura

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        nodo.altura = 1 + max(
            self._altura(nodo.izquierdo), self._altura(nodo.derecho)
        )

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        y = nodo.derecho
        T2 = y.izquierdo

        y.izquierdo = nodo
        nodo.derecho = T2

        self._actualizar_altura(nodo)
        self._actualizar_altura(y)
        return y

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        x = nodo.izquierdo
        T2 = x.derecho

        x.derecho = nodo
        nodo.izquierdo = T2

        self._actualizar_altura(nodo)
        self._actualizar_altura(x)
        return x