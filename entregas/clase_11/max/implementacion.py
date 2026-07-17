"""Código base para árboles binarios de búsqueda.

Clase 11: motivación, conceptos, invariante, búsqueda, inserción y recorridos.

Este archivo contiene firmas y docstrings para trabajar durante la clase.
No contiene soluciones completas.
"""

from __future__ import annotations


class Nodo:
    """Nodo de un árbol binario.

    Parámetros
    ----------
    valor : int
        Valor almacenado en el nodo.

    Atributos
    ---------
    valor : int
        Valor del nodo.
    izquierdo : Nodo | None
        Hijo izquierdo.
    derecho : Nodo | None
        Hijo derecho.

    Ejemplo
    -------
    >>> nodo = Nodo(10)
    >>> nodo.valor
    10
    >>> nodo.izquierdo is None
    True
    """

    def __init__(self, valor: int) -> None:
        """Crea un nodo con ``valor``."""
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un entero.")
        self.valor : int = valor
        self.izquierdo : Nodo = None
        self.derecho : Nodo = None



class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda.

    Invariante
    ----------
    Para cada nodo:

    - todos los valores del subárbol izquierdo son menores que el valor del nodo;
    - todos los valores del subárbol derecho son mayores que el valor del nodo.

    En esta práctica no se permiten valores repetidos.
    """

    def __init__(self) -> None:
        """Crea un árbol binario de búsqueda vacío."""

        self.raiz = None

    def esta_vacio(self) -> bool:
        """Regresa True si el árbol no tiene nodos.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.esta_vacio()
        True
        """
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        """Inserta un valor en el árbol.


        Si el árbol está vacío, el nuevo valor se convierte en la raíz.
        Si el valor ya existe, no debe insertarse de nuevo.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.insertar(8)
        >>> arbol.contiene(8)
        True
        """
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
        """Indica si el valor está en el árbol.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.insertar(8)
        >>> arbol.contiene(8)
        True
        >>> arbol.contiene(5)
        False
        """
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
        """Regresa la altura del árbol.

        Convención de esta clase:

        - árbol vacío: altura 0;
        - árbol con solo raíz: altura 1.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.altura()
        0
        >>> arbol.insertar(8)
        >>> arbol.altura()
        1
        """
        
        def altura_nodo(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            altura_izquierda = altura_nodo(nodo.izquierdo)
            altura_derecha = altura_nodo(nodo.derecho)
            return max(altura_izquierda, altura_derecha) + 1
        return altura_nodo(self.raiz)

    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un BST, el recorrido inorden debe producir los valores ordenados.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> for valor in [8, 4, 10, 2, 6]:
        ...     arbol.insertar(valor)
        >>> arbol.inorden()
        [2, 4, 6, 8, 10]
        """
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
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """

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
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        listado = []
        def orden_postorden(nodo : Nodo | None) -> None:
            if nodo is None:
                return listado
            orden_postorden(nodo.izquierdo)
            orden_postorden(nodo.derecho)
            listado.append(nodo.valor)
        orden_postorden(self.raiz)
        return listado
    
