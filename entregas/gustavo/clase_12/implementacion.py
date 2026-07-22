from __future__ import annotations

class Nodo:
    """Nodo de un árbol binario."""
    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None

class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda sin valores repetidos con métricas de balance."""
    
    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        
        actual = self.raiz
        while True:
            if valor == actual.valor:
                return  # Invariante: no se permiten duplicados
            elif valor < actual.valor:
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
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return False

    def altura(self) -> int:
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo), self._altura_rec(nodo.derecho))

    def inorden(self) -> list[int]:
        valores: list[int] = []
        self._inorden_rec(self.raiz, valores)
        return valores

    def _inorden_rec(self, nodo: Nodo | None, valores: list[int]) -> None:
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, valores)
            valores.append(nodo.valor)
            self._inorden_rec(nodo.derecho, valores)

    def preorden(self) -> list[int]:
        valores: list[int] = []
        self._preorden_rec(self.raiz, valores)
        return valores

    def _preorden_rec(self, nodo: Nodo | None, valores: list[int]) -> None:
        if nodo is not None:
            valores.append(nodo.valor)
            self._preorden_rec(nodo.izquierdo, valores)
            self._preorden_rec(nodo.derecho, valores)

    def postorden(self) -> list[int]:
        valores: list[int] = []
        self._postorden_rec(self.raiz, valores)
        return valores

    def _postorden_rec(self, nodo: Nodo | None, valores: list[int]) -> None:
        if nodo is not None:
            self._postorden_rec(nodo.izquierdo, valores)
            self._postorden_rec(nodo.derecho, valores)
            valores.append(nodo.valor)

    def cantidad_nodos(self) -> int:
        return self._cantidad_nodos_rec(self.raiz)

    def _cantidad_nodos_rec(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return 0
        return 1 + self._cantidad_nodos_rec(nodo.izquierdo) + self._cantidad_nodos_rec(nodo.derecho)

    def es_degenerado(self) -> bool:
        if self.raiz is None:
            return False
        return self._es_degenerado_rec(self.raiz)

    def _es_degenerado_rec(self, nodo: Nodo | None) -> bool:
        if nodo is None:
            return True
        # Si un nodo posee ambos hijos, rompe el principio de degeneración lineal
        if nodo.izquierdo is not None and nodo.derecho is not None:
            return False
        return self._es_degenerado_rec(nodo.izquierdo) and self._es_degenerado_rec(nodo.derecho)

    def comparaciones_busqueda(self, valor: int) -> int:
        contador = 0
        actual = self.raiz
        while actual is not None:
            contador += 1
            if valor == actual.valor:
                break
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return contador