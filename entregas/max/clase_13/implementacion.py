from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NodoAVL:
    valor: int
    izquierdo: NodoAVL | None = None
    derecho: NodoAVL | None = None
    altura: int = 1

    def __post_init__(self) -> None:
        if not isinstance(self.valor, int):
            raise TypeError("valor debe de ser int")
    @property
    def raiz(self) -> NodoAVL | None:
        return self.nodo

class ArbolAVL:
    def __init__(self) -> None:
        self.nodo: NodoAVL | None = None

    def insertar(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("valor debe de ser int")

        self.nodo = self._insertar(self.nodo, valor)

    def _insertar(self, nodo: NodoAVL | None, valor: int) -> NodoAVL:
        if nodo is None:
            return NodoAVL(valor)

        if valor == nodo.valor:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar(nodo.derecho, valor)

        self._actualizar_altura(nodo)
        balance = self._factor_balance(nodo)

        if balance > 1 and valor < nodo.izquierdo.valor:
            return self._rotar_derecha(nodo)

        if balance < -1 and valor > nodo.derecho.valor:
            return self._rotar_izquierda(nodo)

        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def contiene(self, valor: int) -> bool:
        nodo = self.nodo
        while nodo is not None:
            if valor == nodo.valor:
                return True
            nodo = nodo.izquierdo if valor < nodo.valor else nodo.derecho
        return False

    def altura(self) -> int:
        return self._altura(self.nodo)

    def inorden(self) -> list[int]:
        return self._inorden(self.nodo)

    def esta_balanceado(self) -> bool:
        return self._esta_balanceado(self.nodo)

    def _inorden(self, nodo: NodoAVL | None) -> list[int]:
        if nodo is None:
            return []
        return self._inorden(nodo.izquierdo) + [nodo.valor] + self._inorden(nodo.derecho)

    def _esta_balanceado(self, nodo: NodoAVL | None) -> bool:
        if nodo is None:
            return True
        balance = self._factor_balance(nodo)
        return (
            abs(balance) <= 1
            and self._esta_balanceado(nodo.izquierdo)
            and self._esta_balanceado(nodo.derecho)
        )

    def _altura(self, nodo: NodoAVL | None) -> int:
        return nodo.altura if nodo is not None else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        nuevo_padre = nodo.derecho
        assert nuevo_padre is not None
        nodo.derecho = nuevo_padre.izquierdo
        nuevo_padre.izquierdo = nodo
        self._actualizar_altura(nodo)
        self._actualizar_altura(nuevo_padre)
        return nuevo_padre

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        nuevo_padre = nodo.izquierdo
        assert nuevo_padre is not None
        nodo.izquierdo = nuevo_padre.derecho
        nuevo_padre.derecho = nodo
        self._actualizar_altura(nodo)
        self._actualizar_altura(nuevo_padre)
        return nuevo_padre