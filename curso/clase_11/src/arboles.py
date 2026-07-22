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

        raise NotImplementedError("Completa Nodo en tu entrega")


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

        raise NotImplementedError("Completa ArbolBinarioBusqueda en tu entrega")

    def esta_vacio(self) -> bool:
        """Regresa True si el árbol no tiene nodos.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.esta_vacio()
        True
        """

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """

        raise NotImplementedError

    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        raise NotImplementedError
