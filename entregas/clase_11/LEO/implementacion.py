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
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


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
        if self.raiz == None:
            return True
        else: 
            return False


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
            raise TypeError("El valor debe ser un entero")

        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        
        actual = self.raiz
        while True:
            if actual.valor == valor:
                return
            elif actual.valor < valor:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return
                else:
                    actual = actual.derecho
            else: 
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return
                else: 
                    actual = actual.izquierdo
        

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

        if self.raiz is None:
            return False
        actual = self.raiz
        while True:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                if actual.izquierdo is None:
                    return False
                else:
                    actual = actual.izquierdo
            else:
                if actual.derecho == None:
                    return False
                else:
                    actual = actual.derecho

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
            alt_iz = altura_nodo(nodo.izquierdo)
            alt_der = altura_nodo(nodo.derecho)
            return 1 + max(alt_iz, alt_der)
        
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
        inord = []
        def inorden_nodo(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            inorden_nodo(nodo.izquierdo)
            inord.append(nodo.valor)
            inorden_nodo(nodo.derecho)  
            
        inorden_nodo(self.raiz)
        return inord

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """
        preord = []

        def preorden_nodo(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            preord.append(nodo.valor)
            preorden_nodo(nodo.izquierdo)
            preorden_nodo(nodo.derecho)
            
        preorden_nodo(self.raiz)
        return preord

    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        postord = []

        def postorden_nodo(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            postorden_nodo(nodo.izquierdo)
            postorden_nodo(nodo.derecho)
            postord.append(nodo.valor)
            
        postorden_nodo(self.raiz)
        return postord