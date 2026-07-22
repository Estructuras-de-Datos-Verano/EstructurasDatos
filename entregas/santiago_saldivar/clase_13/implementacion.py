"""Código base para la Clase 13: árboles AVL.

Un árbol AVL es un árbol binario de búsqueda que mantiene baja su altura
mediante rotaciones. Este archivo contiene una interfaz documentada para que
la uses como punto de partida en tu entrega.

> [!IMPORTANT]
> Este archivo no es una solución completa. Tu implementación evaluable debe
> vivir en ``entregas/clase_13/nombre/implementacion.py``.
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
        if not isinstance(valor, int):
            raise TypeError("El valor a insertar debe ser un entero.")
        
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo: NodoAVL | None, valor: int) -> NodoAVL:
        """Función recursiva auxiliar. """

        if nodo is None:
            return NodoAVL(valor)
        
        
        #A continuación, bases del BST.
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)

        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)

        else:
            return nodo #Caso nodo == valor
        
        return self._balancear(nodo)


    def _balancear(self, nodo: NodoAVL) -> NodoAVL:
        """Función privada que usaré para asegurar que cada que agrego un nodo se mantenga balanceado."""

        self._actualizar_altura(nodo) 
        balance = self._factor_balance(nodo)

        """
        Hay varios casos posibles. Según qué tan positivo o negativo sea 
        el balance, el árbol es degenerado a la izquierda o a la derecha.
        Mientras más negativo, más grande es a la izquierda.
        Mientras más positivo, más a la derecha.
        Nos guiaremos con eso para decidir qué rotación aplicar.
        """
        # Caso primero: LL
        # Árbol tendente a la izquierda. Hijo izquierdo de tendencia zurda o neutra.
        # Si el balance es positivo, hay más a la izquierda.
        if balance > 1 and self._factor_balance(nodo.izquierdo) >= 0:
            return self._rotar_derecha(nodo)
        

        # Caso segundo: RR
        # Árbol tendente a la derecha. Hijo derecho de tendencia diestra no neutra.
        if balance < -1 and self._factor_balance(nodo.derecho) <= 0:
            #Esencialmente lo mismo que el caso LL, pero al revés.
            return self._rotar_izquierda(nodo)

        # Caso tercero: LR
        # Árbol tendente a la izquierda. Hijo tendende a la derecha.
        if balance > 1 and self._factor_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo) 
            return self._rotar_derecha(nodo)
        
        #Caso cuarto: RL
        # Árbol tendente a la derecha. Hijo tendente a la izquierda.
        if balance < -1 and self._factor_balance(nodo.derecho) > 0:
            # Más o menos lo mismo, pero al revés.
            nodo.derecho = self._rotar_derecha(nodo.derecho)

            return self._rotar_izquierda(nodo)
        
        return nodo


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

        if self.raiz is None:
            return 0
        return self.raiz.altura

    def inorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido inorden.

        En un AVL, como sigue siendo un BST, el recorrido inorden debe producir
        los valores ordenados.
        """


        return self._inorden_recursivo(self.raiz)
    
    def _inorden_recursivo(self, nodo: NodoAVL | None) -> list[int]:
        if nodo is None:
            return [] #Junta listas.
        return (self._inorden_recursivo(nodo.izquierdo) + 
                [nodo.valor] +
                self._inorden_recursivo(nodo.derecho))

    def esta_balanceado(self) -> bool:
        """Verifica si todos los nodos cumplen el invariante AVL.

        Regresa
        -------
        bool
            True si todo nodo tiene factor de balance entre -1 y 1.
        """

        return self._balance_recursivo(self.raiz)
    
    def _balance_recursivo(self, nodo: NodoAVL | None) -> bool:
        if nodo is None:
            return True
        
        balance = self._factor_balance(nodo)
        if balance < -1 or balance > 1:
            return False
        
        return (self._balance_recursivo(nodo.izquierdo) and self._balance_recursivo(nodo.derecho))

    def _altura(self, nodo: NodoAVL | None) -> int:
        """Regresa la altura almacenada de ``nodo`` o 0 si es None."""

        return nodo.altura if nodo is not None else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        """Actualiza la altura de ``nodo`` a partir de sus hijos."""

        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        """Calcula ``altura(izquierdo) - altura(derecho)`` para ``nodo``."""

        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho) 

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación izquierda y devuelve la nueva raíz local.

        Esta rotación corrige el caso RR y participa en el caso RL.
        """

        nodo2 = nodo.derecho
        T2variableauxiliar = nodo2.izquierdo

        #Rotar
        nodo2.izquierdo = nodo
        nodo.derecho = T2variableauxiliar

        #Actualizar la altura
        self._actualizar_altura(nodo)
        self._actualizar_altura(nodo2)

        return nodo2
        

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación derecha y devuelve la nueva raíz local.

        Esta rotación corrige el caso LL y participa en el caso LR.
        """

        nodo2 = nodo.izquierdo
        T2variableauxiliar = nodo2.derecho

        #Rotar
        nodo2.derecho = nodo
        nodo.izquierdo = T2variableauxiliar


        #Actualizar la altura
        self._actualizar_altura(nodo)
        self._actualizar_altura(nodo2)

        return nodo2