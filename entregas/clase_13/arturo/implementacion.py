from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NodoAVL:
    """Nodo de un árbol AVL.

    Parámetros
    ----------
    valor : int
        Valor entero almacenado en el nodo.

    Atributos
    ---------
    valor : int
        Valor del nodo.
    izquierdo : NodoAVL | None
        Hijo izquierdo del nodo.
    derecho : NodoAVL | None
        Hijo derecho del nodo.
    altura : int
        Altura del subárbol cuya raíz es este nodo. Por convención, un nodo
        recién creado tiene altura 1.

    Ejemplo
    -------
    >>> nodo = NodoAVL(10)
    >>> nodo.valor
    10
    >>> nodo.altura
    1
    >>> nodo.izquierdo is None and nodo.derecho is None
    True
    """

    valor: int
    izquierdo: NodoAVL | None = None
    derecho: NodoAVL | None = None
    altura: int = 1


class ArbolAVL:
    """Árbol AVL sin valores repetidos.

    Un AVL mantiene el invariante de BST y además exige que, en cada nodo, la
    diferencia entre las alturas del subárbol izquierdo y derecho sea a lo más
    1 en valor absoluto.

    Invariante de BST
    -----------------
    Para cada nodo:

    - todos los valores del subárbol izquierdo son menores que el nodo;
    - todos los valores del subárbol derecho son mayores que el nodo.

    Invariante AVL
    --------------
    Para cada nodo:

    ``abs(altura(izquierdo) - altura(derecho)) <= 1``.
    """

    def __init__(self) -> None:
        """Crea un árbol AVL vacío.

        Ejemplo
        -------
        >>> arbol = ArbolAVL()
        >>> arbol.altura()
        0
        """

        self.raiz: NodoAVL | None = None

    def insertar(self, valor: int) -> None:
        """Inserta ``valor`` manteniendo balanceado el árbol.

        Si ``valor`` ya existe, el árbol no debe cambiar.

        Parámetros
        ----------
        valor : int
            Valor entero a insertar.

        Ejemplo
        -------
        >>> arbol = ArbolAVL()
        >>> arbol.insertar(30)
        >>> arbol.insertar(20)
        >>> arbol.insertar(10)  # caso LL: requiere rotación derecha
        >>> arbol.inorden()
        [10, 20, 30]
        """
        def _insertar( nodo: NodoAVL | None, valor: int) -> NodoAVL:
            if nodo is None:
                return NodoAVL(valor)
            
            if valor == nodo.valor:
                return nodo
            if valor < nodo.valor:
                nodo.izquierdo = _insertar(nodo.izquierdo, valor)
            else:
                nodo.derecho = _insertar(nodo.derecho, valor)

            self._actualizar_altura(nodo)
            balance = self._factor_balance(nodo)

            if balance > 1 and nodo.izquierdo is not None and valor < nodo.izquierdo.valor:
                return self._rotar_derecha(nodo)
    
            if balance < -1 and nodo.derecho is not None and valor > nodo.derecho.valor:
                return self._rotar_izquierda(nodo)
            if balance > 1 and nodo.izquierdo is not None and valor > nodo.izquierdo.valor:
                nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
                return self._rotar_derecha(nodo)
            if balance < -1 and nodo.derecho is not None and valor < nodo.derecho.valor:
                nodo.derecho = self._rotar_derecha(nodo.derecho)
                return self._rotar_izquierda(nodo)
            
            return nodo
        self.raiz = _insertar(self.raiz, valor)
        

    def contiene(self, valor: int) -> bool:
        """Indica si ``valor`` aparece en el árbol.

        Parámetros
        ----------
        valor : int
            Valor entero a buscar.

        Regresa
        -------
        bool
            True si el valor está en el árbol; False en caso contrario.
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

        Convención
        ----------
        - árbol vacío: altura 0;
        - árbol con solo raíz: altura 1.
        """

        return self._altura(self.raiz)

    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un AVL, como sigue siendo un BST, el recorrido inorden debe producir
        los valores ordenados.
        """

        def inorden_nodo(nodo: NodoAVL | None) -> list[int]:
            if nodo is None:
                return []
            else:
                return inorden_nodo(nodo.izquierdo) + [nodo.valor] + inorden_nodo(nodo.derecho)
        return inorden_nodo(self.raiz)

    def esta_balanceado(self) -> bool:
        """Verifica si todos los nodos cumplen el invariante AVL.

        Regresa
        -------
        bool
            True si todo nodo tiene factor de balance entre -1 y 1.
        """

        def balance_nodo(nodo: NodoAVL | None) -> bool:
            if nodo is None:
                return True
            actual = nodo

            if self._factor_balance(actual) in [-1,1,0] and balance_nodo(actual.derecho) and balance_nodo(actual.izquierdo):
                    return True
            return False
        return balance_nodo(self.raiz)


    def _altura(self, nodo: NodoAVL | None) -> int:
        """Regresa la altura almacenada de ``nodo`` o 0 si es None."""

        if nodo is None:
            return 0
        else:
            return nodo.altura

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        """Actualiza la altura de ``nodo`` a partir de sus hijos."""

        nodo.altura = 1 + max(self._altura(nodo.izquierdo),self._altura(nodo.derecho))

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        """Calcula ``altura(izquierdo) - altura(derecho)`` para ``nodo``."""

        if nodo is None:
            return 0
        else:
            return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación izquierda y devuelve la nueva raíz local.

        Esta rotación corrige el caso RR y participa en el caso RL.
        """
        punto_fijo = nodo.derecho
        if punto_fijo is None:
            return nodo
        
        nodo.derecho = punto_fijo.izquierdo
        punto_fijo.izquierdo = nodo

        self._actualizar_altura(nodo)
        self._actualizar_altura(punto_fijo)

        return punto_fijo
        

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación derecha y devuelve la nueva raíz local.

        Esta rotación corrige el caso LL y participa en el caso LR.
        """

        punto_fijo = nodo.izquierdo
        if punto_fijo is None:
            return nodo
        
        nodo.izquierdo = punto_fijo.derecho
        punto_fijo.derecho = nodo

        self._actualizar_altura(nodo)
        self._actualizar_altura(punto_fijo)
        return punto_fijo
