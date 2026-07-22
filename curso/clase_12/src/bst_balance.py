"""Código base para estudiar altura, balance y degeneración en BST.

Clase 12: ¿qué hace que un BST sea eficiente?

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
        """Crea un nodo con ``valor`` y sin hijos."""

        raise NotImplementedError("Completa Nodo en tu entrega")


class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda sin valores repetidos.

    Invariante
    ----------
    Para cada nodo:

    - todos los valores del subárbol izquierdo son menores que el valor del nodo;
    - todos los valores del subárbol derecho son mayores que el valor del nodo.

    Convención de altura
    --------------------
    - árbol vacío: altura 0;
    - árbol con solo raíz: altura 1.
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
        """Inserta ``valor`` en el árbol.

        Si el árbol está vacío, el nuevo valor se convierte en la raíz.
        Si el valor ya existe, no debe insertarse de nuevo.

        Parámetros
        ----------
        valor : int
            Valor entero a insertar.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.insertar(8)
        >>> arbol.contiene(8)
        True
        """

        raise NotImplementedError

    def contiene(self, valor: int) -> bool:
        """Indica si ``valor`` está en el árbol.

        Parámetros
        ----------
        valor : int
            Valor entero a buscar.

        Regresa
        -------
        bool
            True si el valor aparece en el árbol; False en otro caso.
        """

        raise NotImplementedError

    def altura(self) -> int:
        """Regresa la altura del árbol.

        Convención:

        - árbol vacío: altura 0;
        - árbol con solo raíz: altura 1.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.altura()
        0
        """

        raise NotImplementedError

    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un BST, el recorrido inorden debe producir los valores ordenados.
        """

        raise NotImplementedError

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa raíz, subárbol izquierdo y subárbol derecho.
        """

        raise NotImplementedError

    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa subárbol izquierdo, subárbol derecho y raíz.
        """

        raise NotImplementedError

    def cantidad_nodos(self) -> int:
        """Regresa la cantidad de nodos almacenados en el árbol.

        Regresa
        -------
        int
            Número de valores distintos insertados.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.cantidad_nodos()
        0
        """

        raise NotImplementedError

    def es_degenerado(self) -> bool:
        """Indica si el árbol está degenerado.

        En esta práctica diremos que un árbol no vacío está degenerado si cada
        nodo tiene a lo más un hijo. Con esta forma, el árbol se parece a una
        lista enlazada y su altura coincide con su cantidad de nodos.

        Regresa
        -------
        bool
            True si el árbol está degenerado; False en otro caso.
        """

        raise NotImplementedError

    def comparaciones_busqueda(self, valor: int) -> int:
        """Cuenta cuántas comparaciones realiza la búsqueda de ``valor``.

        La función debe contar cada nodo visitado durante la búsqueda.

        Parámetros
        ----------
        valor : int
            Valor entero a buscar.

        Regresa
        -------
        int
            Número de comparaciones realizadas. En un árbol vacío regresa 0.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.comparaciones_busqueda(5)
        0
        >>> arbol.insertar(8)
        >>> arbol.comparaciones_busqueda(8)
        1
        """

        raise NotImplementedError
