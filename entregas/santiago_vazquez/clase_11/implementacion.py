from __future__ import annotations

class Nodo:
    def __init__(self, valor: int) -> None:
        self.valor: int = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None

class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        def _insertar(nodo: Nodo, val: int) -> None:
            if val < nodo.valor:
                if nodo.izquierdo is None:
                    nodo.izquierdo = Nodo(val)
                else:
                    _insertar(nodo.izquierdo, val)
            elif val > nodo.valor:
                if nodo.derecho is None:
                    nodo.derecho = Nodo(val)
                else:
                    _insertar(nodo.derecho, val)

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            _insertar(self.raiz, valor)

    def contiene(self, valor: int) -> bool:
        def _contiene(nodo: Nodo | None, val: int) -> bool:
            if nodo is None:
                return False
            if val == nodo.valor:
                return True
            if val < nodo.valor:
                return _contiene(nodo.izquierdo, val)
            return _contiene(nodo.derecho, val)

        return _contiene(self.raiz, valor)

    def altura(self) -> int:
        def _altura(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + max(_altura(nodo.izquierdo), _altura(nodo.derecho))

        return _altura(self.raiz)

    def inorden(self) -> list[int]:
        valores: list[int] = []
        def _inorden(nodo: Nodo | None) -> None:
            if nodo is not None:
                _inorden(nodo.izquierdo)
                valores.append(nodo.valor)
                _inorden(nodo.derecho)
        _inorden(self.raiz)
        return valores

    def preorden(self) -> list[int]:
        valores: list[int] = []
        def _preorden(nodo: Nodo | None) -> None:
            if nodo is not None:
                valores.append(nodo.valor)
                _preorden(nodo.izquierdo)
                _preorden(nodo.derecho)
        _preorden(self.raiz)
        return valores

    def postorden(self) -> list[int]:
        valores: list[int] = []
        def _postorden(nodo: Nodo | None) -> None:
            if nodo is not None:
                _postorden(nodo.izquierdo)
                _postorden(nodo.derecho)
                valores.append(nodo.valor)
        _postorden(self.raiz)
        return valores