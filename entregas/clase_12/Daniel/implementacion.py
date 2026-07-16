from __future__ import annotations


class Nodo:
    """Nodo de un árbol binario de búsqueda."""

    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda sin valores repetidos."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        if self.esta_vacio():
            self.raiz = Nodo(valor)
            return

        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return
                actual = actual.derecho

    def contiene(self, valor: int) -> bool:
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return False

    def altura(self) -> int:
        def _altura(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + max(_altura(nodo.izquierdo), _altura(nodo.derecho))

        return _altura(self.raiz)

    def inorden(self) -> list[int]:
        resultado: list[int] = []

        def _recorrer(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            _recorrer(nodo.izquierdo)
            resultado.append(nodo.valor)
            _recorrer(nodo.derecho)

        _recorrer(self.raiz)
        return resultado

    def preorden(self) -> list[int]:
        resultado: list[int] = []

        def _recorrer(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            resultado.append(nodo.valor)
            _recorrer(nodo.izquierdo)
            _recorrer(nodo.derecho)

        _recorrer(self.raiz)
        return resultado

    def postorden(self) -> list[int]:
        resultado: list[int] = []

        def _recorrer(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            _recorrer(nodo.izquierdo)
            _recorrer(nodo.derecho)
            resultado.append(nodo.valor)

        _recorrer(self.raiz)
        return resultado

    def cantidad_nodos(self) -> int:
        def _contar(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + _contar(nodo.izquierdo) + _contar(nodo.derecho)

        return _contar(self.raiz)

    def es_degenerado(self) -> bool:
        if self.raiz is None:
            return False

        def _degenerado(nodo: Nodo | None) -> bool:
            if nodo is None:
                return True
            if nodo.izquierdo is not None and nodo.derecho is not None:
                return False
            return _degenerado(nodo.izquierdo) and _degenerado(nodo.derecho)

        return _degenerado(self.raiz)

    def comparaciones_busqueda(self, valor: int) -> int:
        if self.raiz is None:
            return 0

        comparaciones = 0
        actual = self.raiz
        while actual is not None:
            comparaciones += 1
            if valor == actual.valor:
                return comparaciones
            if valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return comparaciones
