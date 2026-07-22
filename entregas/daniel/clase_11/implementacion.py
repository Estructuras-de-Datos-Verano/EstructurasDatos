from __future__ import annotations

class Nodo:
    def __init__(self, valor: int):
        self.valor: int = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz: Nodo | None = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual: Nodo | None, valor: int) -> Nodo:
        if nodo_actual is None:
            return Nodo(valor)
        
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._insertar_recursivo(nodo_actual.derecho, valor)
        return nodo_actual

    def contiene(self, valor: int) -> bool:
        return self._contiene_recursivo(self.raiz, valor)

    def _contiene_recursivo(self, nodo_actual: Nodo | None, valor: int) -> bool:
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._contiene_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._contiene_recursivo(nodo_actual.derecho, valor)

    def altura(self) -> int:
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, nodo_actual: Nodo | None) -> int:
        if nodo_actual is None:
            return 0
        return 1 + max(self._altura_recursivo(nodo_actual.izquierdo), 
                       self._altura_recursivo(nodo_actual.derecho))

    def inorden(self) -> list[int]:
        resultado: list[int] = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo_actual: Nodo | None, resultado: list[int]) -> None:
        if nodo_actual is not None:
            self._inorden_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecho, resultado)

    def preorden(self) -> list[int]:
        resultado: list[int] = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo_actual: Nodo | None, resultado: list[int]) -> None:
        if nodo_actual is not None:
            resultado.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierdo, resultado)
            self._preorden_recursivo(nodo_actual.derecho, resultado)

    def postorden(self) -> list[int]:
        resultado: list[int] = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo_actual: Nodo | None, resultado: list[int]) -> None:
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierdo, resultado)
            self._postorden_recursivo(nodo_actual.derecho, resultado)
            resultado.append(nodo_actual.valor)