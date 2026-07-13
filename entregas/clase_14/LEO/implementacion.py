"""Código base documentado para la Clase 14: min-heaps.

Este archivo define el contrato de la práctica, pero no contiene la solución.
La implementación evaluable debe vivir en
``entregas/clase_14/nombre/implementacion.py``.
"""

from __future__ import annotations

from collections.abc import Iterable


class HeapMin:
    """Min-heap de enteros representado con un arreglo indexado desde cero.

    Convención
    ----------
    Para un índice ``i``:

    - ``padre(i) = (i - 1) // 2``;
    - ``izquierdo(i) = 2 * i + 1``;
    - ``derecho(i) = 2 * i + 2``.

    Notes
    -----
    Completa esta interfaz en tu carpeta de entrega. No modifiques este archivo
    para entregar la práctica.
    """

    def __init__(self, valores: Iterable[int] | None = None) -> None:
        """Crea un heap vacío o lo construye a partir de ``valores``.

        Parameters
        ----------
        valores : Iterable[int] | None
            Valores iniciales opcionales.
        """

        self.datos = []
        if valores is not None:
            self.construir_heap(valores)


    def esta_vacio(self) -> bool:
        """Devuelve ``True`` cuando el heap no almacena elementos."""

        if self.datos:
            return False
        else:
            return True

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""

        return len(self.datos)

    def minimo(self) -> int:
        """Consulta la raíz sin retirarla.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        return self.datos[0]

    def insertar(self, valor: int) -> None:
        """Agrega ``valor`` y restaura la propiedad mediante sift-up.

        Parameters
        ----------
        valor : int
            Valor que se insertará.

        Examples
        --------
        >>> heap = HeapMin()
        >>> heap.insertar(5)
        >>> heap.insertar(2)
        >>> heap.minimo()
        2
        """
        self.datos.append(valor)
        z = len(self.datos) - 1
        self._subir(z)
        

    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        if self.esta_vacio():
            raise IndexError("El heap está vacío")
        a = self.datos[0]
        if self.tamano() == 1:
            self.datos = []
            return a
        else: 
            b = self.datos[-1]
            x = self.datos[1:-1]
            self.datos = [b] + x
            self._bajar(0)
            return a

    def construir_heap(self, valores: Iterable[int]) -> None:
        """Reemplaza el contenido por un heap construido con ``valores``."""
        heap = HeapMin()
        for valor in valores:
            heap.insertar(valor)
        self.datos = heap

        raise NotImplementedError

    def _subir(self, indice: int) -> None:
        """Desplaza hacia arriba el nodo ubicado en ``indice``."""
        if indice == 0:
            raise IndexError("No se puede subir la raíz")
        while indice > 0:
            if self.datos[indice] < self.datos[self._indice_padre(indice)]:
                a = self.datos[indice]
                b = self.datos[self._indice_padre(indice)]
                self.datos[indice] = b
                self._indice_padre[indice] = a
                indice = self._indice_padre(indice)
            else:
                return

    def _bajar(self, indice: int) -> None:
        """Desplaza hacia abajo el nodo ubicado en ``indice``."""

        if indice == len(self.datos) - 1:
            raise IndexError("No se puede bajar el último nodo")
        while indice < len(self.datos) - 1:
            if self.datos[indice] > self.datos[self._indice_izquierdo(indice)] and self.datos[indice] > self.datos[self._indice_izquierdo(indice)]:
                if self.datos[self._indice_izquierdo(indice)] == self.datos[self._indice_derecho(indice)]:
                    a = self.datos[indice]
                    b = self.datos[self._indice_izquierdo(indice)]
                    self.datos[indice] = b
                    self._indice_izquierdo[indice] = a
                    indice = self._indice_izquierdo(indice)
                if self.datos[self._indice_izquierdo(indice)] < self.datos[self._indice_derecho(indice)]:
                    a = self.datos[indice]
                    b = self.datos[self._indice_izquierdo(indice)]
                    self.datos[indice] = b
                    self._indice_izquierdo[indice] = a
                    indice = self._indice_izquierdo(indice)
                if self.datos[self._indice_izquierdo(indice)] > self.datos[self._indice_derecho(indice)]:
                    a = self.datos[indice]
                    b = self.datos[self._indice_derecho(indice)]
                    self.datos[indice] = b
                    self._indice_derecho[indice] = a
                    indice = self._indice_derecho(indice)
            if self.datos[indice] > self.datos[self._indice_izquierdo(indice)] and not self.datos[indice] > self.datos[self._indice_izquierdo(indice)]:
                a = self.datos[indice]
                b = self.datos[self._indice_izquierdo(indice)]
                self.datos[indice] = b
                self._indice_izquierdo[indice] = a
                indice = self._indice_izquierdo(indice)      
            if not self.datos[indice] > self.datos[self._indice_izquierdo(indice)] and self.datos[indice] > self.datos[self._indice_izquierdo(indice)]:
                a = self.datos[indice]
                b = self.datos[self._indice_derecho(indice)]
                self.datos[indice] = b
                self._indice_derecho[indice] = a
                indice = self._indice_derecho(indice)
            else:
                return

    def _indice_padre(self, indice: int) -> int:
        """Calcula el índice del padre; la raíz no tiene padre."""
        if indice == 0:
            raise IndexError("La raíz no tiene padre")
        return (indice - 1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        """Calcula el índice del hijo izquierdo."""

        return 2 * indice + 1

    def _indice_derecho(self, indice: int) -> int:
        """Calcula el índice del hijo derecho."""

        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool:
        """Comprueba que todo padre sea menor o igual que sus hijos."""

        for i in range(len(self.datos)):
            if i == 0:
                if self.datos[0] > self.datos[1] or self.datos[0] > self.datos[2]:
                    return False
            if self.datos[self._indice_padre(i)] > self.datos[self._indice_izquierdo(i)] or self.datos[self._indice_padre(i)] > self.datos[self._indice_derecho(i)]:
                return False 
        return True


def ultima_piedra(piedras: list[int]) -> int:
    """Resuelve de forma guiada Last Stone Weight con una cola de prioridad.

    Parameters
    ----------
    piedras : list[int]
        Pesos positivos.

    Returns
    -------
    int
        Peso final, o 0 si no queda ninguna piedra.

    Notes
    -----
    Diseña primero el pseudocódigo en ``notebook.md``. Después completa esta
    función dentro de tu ``implementacion.py``.
    """
    if not isinstance(piedras, list[int]):
        raise TypeError("Piedras debe ser una lista de enteros")
    for piedra in piedras:
        if piedra < 0:
            raise ValueError("Los pesos de las piedras deben ser positivos")
    pesos = []
    for piedra in piedras:
        pesos.append(-piedra)
    heap = HeapMin(pesos)
    while heap.tamano > 1:
        a = heap.extraer_min()
        b = heap.extraer_min()
        if not a == b:
            heap.insertar(abs(a-b))
    if heap.esta_vacio():
        return 0
    else:
        return heap.minimo()