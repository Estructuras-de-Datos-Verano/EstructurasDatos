"""Código base para la Clase 13: árboles AVL.

Un árbol AVL es un árbol binario de búsqueda que mantiene baja su altura
mediante rotaciones. Este archivo contiene una interfaz documentada para que
la uses como punto de partida en tu entrega.

> [!IMPORTANT]
> Este archivo no es una solución completa. Tu implementación evaluable debe
> vivir en ``entregas/nombre/clase_13/implementacion.py``.
"""

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

        raise NotImplementedError("Completa insertar en tu entrega")

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

        raise NotImplementedError

    def altura(self) -> int:
        """Regresa la altura del árbol.

        Convención
        ----------
        - árbol vacío: altura 0;
        - árbol con solo raíz: altura 1.
        """

        raise NotImplementedError

    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un AVL, como sigue siendo un BST, el recorrido inorden debe producir
        los valores ordenados.
        """

        raise NotImplementedError

    def esta_balanceado(self) -> bool:
        """Verifica si todos los nodos cumplen el invariante AVL.

        Regresa
        -------
        bool
            True si todo nodo tiene factor de balance entre -1 y 1.
        """

        raise NotImplementedError

    def _altura(self, nodo: NodoAVL | None) -> int:
        """Regresa la altura almacenada de ``nodo`` o 0 si es None."""

        raise NotImplementedError

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        """Actualiza la altura de ``nodo`` a partir de sus hijos."""

        raise NotImplementedError

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        """Calcula ``altura(izquierdo) - altura(derecho)`` para ``nodo``."""

        raise NotImplementedError

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación izquierda y devuelve la nueva raíz local.

        Esta rotación corrige el caso RR y participa en el caso RL.
        """

        raise NotImplementedError

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación derecha y devuelve la nueva raíz local.

        Esta rotación corrige el caso LL y participa en el caso LR.
        """

        raise NotImplementedError
