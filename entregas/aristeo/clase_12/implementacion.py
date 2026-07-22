from __future__ import annotations
from typing import Optional

class Nodo:
    def __init__(self, valor: int):
        self.valor: int = valor
        self.izquierdo: Optional[Nodo] = None
        self.derecho: Optional[Nodo] = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz: Optional[Nodo] = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        """Inserta un valor en el BST. 
        Evita duplicados según el test_duplicados_no_aumentan_cantidad_de_nodos.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        
        actual = self.raiz
        while True:
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
        """Retorna True si el valor está en el árbol, False en caso contrario."""
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
        """Retorna la altura del árbol (longitud del camino más largo desde la raíz)."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo: Optional[Nodo]) -> int:
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierdo), self._altura_recursiva(nodo.derecho))

    def inorden(self) -> list[int]:
        """Retorna la lista de valores en recorrido inorden (ordenados)."""
        valores = []
        self._inorden_recursivo(self.raiz, valores)
        return valores

    def _inorden_recursivo(self, nodo: Optional[Nodo], valores: list[int]) -> None:
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, valores)
            valores.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, valores)
## bleh ## 

    def cantidad_nodos(self) -> int:
        """Cuenta recursivamente el total de nodos únicos en el árbol."""
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo: Optional[Nodo]) -> int:
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    def es_degenerado(self) -> bool:
        """Un árbol está degenerado si NINGÚN nodo tiene dos hijos al mismo tiempo.
        Es decir, se comporta como una lista enlazada (línea recta).
        """
        if self.esta_vacio():
            return True
        return self._verificar_degenerado(self.raiz)

    def _verificar_degenerado(self, nodo: Optional[Nodo]) -> bool:
        if nodo is None:
            return True
        
        if nodo.izquierdo is not None and nodo.derecho is not None:
            return False
            
        return self._verificar_degenerado(nodo.izquierdo) and self._verificar_degenerado(nodo.derecho)

    def comparaciones_busqueda(self, valor: int) -> int:
        """Busca un valor y retorna cuántas comparaciones (visitas a nodos no nulos)
        hizo en el intento, sin importar si lo encontró o no.
        """
        comparaciones = 0
        actual = self.raiz
        
        while actual is not None:
            comparaciones += 1
            
            if valor == actual.valor:
                return comparaciones
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
                
        return comparaciones