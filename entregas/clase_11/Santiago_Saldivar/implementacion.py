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
        self.izquierdo : Nodo | None = None
        self.derecho : Nodo | None= None


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

        self.raiz : Nodo | None= None

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
            elif valor > actual.valor:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return
                actual = actual.derecho #AAAAAAAAAAAA


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

        if self.raiz is None:
            return 0
        
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo: Nodo) -> int:
            if nodo is None:
                return 0
            
            altura_izquierda = self._altura_recursiva(nodo.izquierdo)
            altura_derecha = self._altura_recursiva(nodo.derecho)

            return 1 + max(altura_izquierda, altura_derecha)
        
    

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

        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo: Nodo) -> list[int]:
        if nodo is None:
            return [] #Junta listas.
        return (self._inorden_recursivo(nodo.izquierdo) + 
                [nodo.valor] +
                self._inorden_recursivo(nodo.derecho))  #Izquierda, raíz, derecha.
                #Se va a la izquierda tanto como pueda. Se detiene al no encontras más nodos. Entonces pasa a la derecha pasando por la raíz.

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """

        return self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo: Nodo) -> list[int]:
        if nodo is None:
            return []
        return ([nodo.valor] + self._preorden_recursivo(nodo.izquierdo) + self._preorden_recursivo(nodo.derecho))  #Raíz, izquierda, derecha.



    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """
        
        return self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo: Nodo) -> list[int]:
        if nodo is None:
            return []
        return (self._postorden_recursivo(nodo.izquierdo) + self._postorden_recursivo(nodo.derecho) + [nodo.valor])  #Izquierda, derecha, raíz.






