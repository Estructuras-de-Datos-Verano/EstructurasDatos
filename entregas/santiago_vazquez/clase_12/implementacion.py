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
        def _insertar_recursivo(nodo: Nodo, valor: int) -> Nodo:
            if valor < nodo.valor:
                if nodo.izquierdo is None:
                    nodo.izquierdo = Nodo(valor)
                else:
                    _insertar_recursivo(nodo.izquierdo, valor)
            elif valor > nodo.valor:
                if nodo.derecho is None:
                    nodo.derecho = Nodo(valor)
                else:
                    _insertar_recursivo(nodo.derecho, valor)
            return nodo

        if self.esta_vacio():
            self.raiz = Nodo(valor)
        else:
            _insertar_recursivo(self.raiz, valor)

    def contiene(self, valor: int) -> bool:
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if valor == nodo_actual.valor:
                return True
            elif valor < nodo_actual.valor:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        return False

    def altura(self) -> int:
        def _altura_recursiva(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + max(_altura_recursiva(nodo.izquierdo), _altura_recursiva(nodo.derecho))
        return _altura_recursiva(self.raiz)

    def inorden(self) -> list[int]:
        valores = []
        def _inorden_recursivo(nodo: Nodo | None):
            if nodo is not None:
                _inorden_recursivo(nodo.izquierdo)
                valores.append(nodo.valor)
                _inorden_recursivo(nodo.derecho)
        _inorden_recursivo(self.raiz)
        return valores

    def preorden(self) -> list[int]:
        valores = []
        def _preorden_recursivo(nodo: Nodo | None):
            if nodo is not None:
                valores.append(nodo.valor)
                _preorden_recursivo(nodo.izquierdo)
                _preorden_recursivo(nodo.derecho)
        _preorden_recursivo(self.raiz)
        return valores

    def postorden(self) -> list[int]:
        valores = []
        def _postorden_recursivo(nodo: Nodo | None):
            if nodo is not None:
                _postorden_recursivo(nodo.izquierdo)
                _postorden_recursivo(nodo.derecho)
                valores.append(nodo.valor)
        _postorden_recursivo(self.raiz)
        return valores

    def cantidad_nodos(self) -> int:
        def _contar(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + _contar(nodo.izquierdo) + _contar(nodo.derecho)
        return _contar(self.raiz)

    def es_degenerado(self) -> bool:
        if self.esta_vacio():
            return False
        
        def _verificar_nodo(nodo: Nodo) -> bool:
            if nodo.izquierdo is not None and nodo.derecho is not None:
                return False
            res_izq = _verificar_nodo(nodo.izquierdo) if nodo.izquierdo is not None else True
            res_der = _verificar_nodo(nodo.derecho) if nodo.derecho is not None else True
            return res_izq and res_der

        return _verificar_nodo(self.raiz)

    def comparaciones_busqueda(self, valor: int) -> int:
        comparaciones = 0
        nodo_actual = self.raiz
        while nodo_actual is not None:
            comparaciones += 1
            if valor == nodo_actual.valor:
                return comparaciones
            elif valor < nodo_actual.valor:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        return comparaciones
