from __future__ import annotations

class Nodo:

    def __init__(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        self.valor : int = valor
        self.izquierdo : Nodo = None
        self.derecho : Nodo = None



class ArbolBinarioBusqueda:

    def __init__(self) -> None:
        self.raiz = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")

        if self.raiz == None:
            self.raiz = Nodo(valor)
            return
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return
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
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")

        actual = self.raiz
        while actual is not None:
            if actual.valor == valor:
                return True
            elif actual.valor < valor:
                actual = actual.derecho
            else:
                actual = actual.izquierdo
        if self.raiz == Nodo(valor):
            return True
        return False
    
    def altura(self) -> int:
        def altura_nodo(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            altura_izquierda = altura_nodo(nodo.izquierdo)
            altura_derecha = altura_nodo(nodo.derecho)
            return max(altura_izquierda, altura_derecha) + 1
        return altura_nodo(self.raiz)

    def inorden(self) -> list[int]:
        listado = []
        def orden_inorden(nodo: Nodo | None) -> None:
            if nodo is None:
                return listado
            orden_inorden(nodo.izquierdo)
            listado.append(nodo.valor)
            orden_inorden(nodo.derecho)
        orden_inorden(self.raiz)
        return listado
    
            


    def preorden(self) -> list[int]:
        listado = []
        def orden_preorden(nodo: Nodo | None) -> None:
            if nodo is None:
                return listado
            listado.append(nodo.valor)
            orden_preorden(nodo.izquierdo)
            orden_preorden(nodo.derecho)
        orden_preorden(self.raiz)
        return listado

    def postorden(self) -> list[int]:
        listado = []
        def orden_postorden(nodo : Nodo | None) -> None:
            if nodo is None:
                return listado
            orden_postorden(nodo.izquierdo)
            orden_postorden(nodo.derecho)
            listado.append(nodo.valor)
        orden_postorden(self.raiz)
        return listado
    
    def cantidad_nodos(self) -> int:
        def contar_nodos(nodo: Nodo):
            if nodo is None:
                return 0
            return 1 + contar_nodos(nodo.izquierdo) + contar_nodos(nodo.derecho)
        return contar_nodos(self.raiz)

    def es_degenerado(self) -> bool:
        def es_degenerado_rec(nodo: Nodo):
            if nodo is None:
                return True
            if nodo.izquierdo is None and nodo.derecho is None:
                return True
            if nodo.izquierdo is not None and nodo.derecho is not None:
                return False
            return es_degenerado_rec(nodo.izquierdo) and es_degenerado_rec(nodo.derecho)
        return es_degenerado_rec(self.raiz)

    def comparaciones_busqueda(self, valor: int) -> int:
        def contar_comparaciones(nodo, valor):
            if nodo is None:
                return 0
            if nodo.valor == valor:
                return 1
            if valor < nodo.valor:
                return 1 + contar_comparaciones(nodo.izquierdo, valor)
            else:
                return 1 + contar_comparaciones(nodo.derecho, valor)
        return contar_comparaciones(self.raiz, valor)
    
