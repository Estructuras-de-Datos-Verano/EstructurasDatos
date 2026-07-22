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
        self.valor = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


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
    
        self.raiz: Nodo | None = None

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
        if self.raiz is None:
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
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                if actual.izquierdo is None:
                    return False
                else: 
                    actual = actual.izquierdo
            else: 
                if actual.derecho is None:
                    return False
                else:
                    actual = actual.derecho



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
        def altura_nodo(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            else: 
                return 1 + max(altura_nodo(nodo.izquierdo), altura_nodo(nodo.derecho))
            
        return altura_nodo(self.raiz)


    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un BST, el recorrido inorden debe producir los valores ordenados.
        """
        def inorden_nodo(nodo: Nodo | None) -> list[int]:
            if nodo is None: 
                return []
            else:
                return inorden_nodo(nodo.izquierdo) + [nodo.valor] + inorden_nodo(nodo.derecho)
            
        return inorden_nodo(self.raiz)


    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa raíz, subárbol izquierdo y subárbol derecho.
        """
        def preorden_nodo(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            else:
                valores = [nodo.valor]
                valores += preorden_nodo(nodo.izquierdo)
                valores += preorden_nodo(nodo.derecho)
            return valores

        return preorden_nodo(self.raiz)


    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa subárbol izquierdo, subárbol derecho y raíz.
        """
        def postorden_nodo(nodo: Nodo | None) -> list[int]:
            if nodo is None: 
                return []
            else:
                return postorden_nodo(nodo.izquierdo) + postorden_nodo(nodo.derecho) + [nodo.valor]
            
        return postorden_nodo(self.raiz)


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
        def len_nodo(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            else: 
                return 1 + len_nodo(nodo.izquierdo) + len_nodo(nodo.derecho)
            
        return len_nodo(self.raiz)


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
        return self.raiz is not None and self.altura() == self.cantidad_nodos()

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

        def comparacion_nodo(nodo: Nodo | None, valor: int) -> int:
            if nodo is None:
                return 0
            elif valor == nodo.valor:
                return 1
            elif valor < nodo.valor:
                return 1 + comparacion_nodo(nodo.izquierdo, valor)
            else:
                return 1 + comparacion_nodo(nodo.derecho, valor)
            
        return comparacion_nodo(self.raiz, valor)

