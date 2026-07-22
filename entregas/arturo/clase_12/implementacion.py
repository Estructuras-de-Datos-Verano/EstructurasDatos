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
            raise TypeError()
        self.valor: int = valor
        self.izquierdo: Nodo | None = None 
        self.derecho: Nodo | None = None   
        

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

        self.raiz: Nodo | None = None
        self.tamano: int = 0

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
            raise TypeError("Valor debe ser un entero")
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
            self.tamano += 1
            return
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return 
            elif valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    self.tamano += 1
                    return 
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    self.tamano += 1
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
            raise TypeError("Valor debe ser un entero")
        
        if self.raiz is None:
            return False 
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

        def altur_nodo(nodo: Nodo | None) ->  int:
            if nodo is None :
                return 0
            else:
                return 1 + max(altur_nodo(nodo.derecho), altur_nodo(nodo.izquierdo))
        return altur_nodo(self.raiz)


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

        def inorden_nodo(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            else:
                return inorden_nodo(nodo.izquierdo) + [nodo.valor] + inorden_nodo(nodo.derecho)
        return inorden_nodo(self.raiz)

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
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

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        def postorden_nodo(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            else:
                valores = postorden_nodo(nodo.izquierdo)
                valores += postorden_nodo(nodo.derecho)
                valores += [nodo.valor] 
                return valores
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
        return self.tamano


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
        if self.raiz is None:
            return False
        else:
            if self.altura() == self.cantidad_nodos():
                return True
            return False

        

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

        def comparaciones_nodo(nodo: Nodo | None, valor: int) -> int:
            if nodo is None:
                return 0
            elif valor == nodo.valor:
                return 1
            elif valor < nodo.valor:
                return 1  + comparaciones_nodo(nodo.izquierdo,valor)
            else:
                return 1 + comparaciones_nodo(nodo.derecho, valor)
            
        return comparaciones_nodo(self.raiz,valor)
