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
        self._nodos = []
        self._forma = {}
        self._raiz = None
    def esta_vacio(self) -> bool:
        """Regresa True si el árbol no tiene nodos.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.esta_vacio()
        True
        """

        return len(set(self._forma)) == 0

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

        if len(self._forma) == 0:
            self._raiz = Nodo(valor)
            self._forma = {
                self._raiz : valor
            }
        elif valor in self._forma.values():
            print(f"Valor ya corresponde a un nodo en el árbol")
        nuevo_nodo = Nodo(valor)
        actual = self._raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    self._forma[nuevo_nodo] = valor
                    break
                else:
                    actual = actual.izquierdo
            elif valor > actual.valor:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    self._forma[nuevo_nodo] = valor
                    break
                else:
                    actual = actual.derecho
            else:
                print(f"Valor ya corresponde a un nodo en el árbol")
                break


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
        return valor in set(self._forma.values())

        

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
        if self._forma == {}:
            return 0
        else:
            def altura_nodo(nodo):
                if nodo is None:
                    return 0
                else:
                    altura_izquierda = altura_nodo(nodo.izquierdo)
                    altura_derecha = altura_nodo(nodo.derecho)
                    return 1 + max(altura_izquierda, altura_derecha)

            return altura_nodo(self._raiz)

    def inorden(self):
        """"
        Lo mismo, pero simplificado
        """
        lista = []
        def viajar(nodo):
            if nodo is None:
                return
            viajar(nodo.izquierdo)
            lista.append(nodo.valor)
            viajar(nodo.derecho)
        viajar(self._raiz)
        return lista

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """

        lista = []
        def viajar_preorden(nodo):
            if nodo is None:
                return
            lista.append(nodo)
            viajar_preorden(nodo.izquierdo)
            viajar_preorden(nodo.derecho)
        viajar_preorden(self._raiz)
        return lista


    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        lista = []
        def viajar_postorden(nodo):
            if nodo is None:
                return None
            viajar_postorden(nodo.izquierdo)
            viajar_postorden(nodo.derecho)
            lista.append(nodo.valor)
        viajar_postorden(self._raiz)
        return lista
