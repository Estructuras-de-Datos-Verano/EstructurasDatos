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

        raise NotImplementedError("Completa __init__ en tu implementacion.py")

    def esta_vacio(self) -> bool:
        """Devuelve ``True`` cuando el heap no almacena elementos."""

        raise NotImplementedError

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""

        raise NotImplementedError

    def minimo(self) -> int:
        """Consulta la raíz sin retirarla.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        raise NotImplementedError

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

        raise NotImplementedError

    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        raise NotImplementedError

    def construir_heap(self, valores: Iterable[int]) -> None:
        """Reemplaza el contenido por un heap construido con ``valores``."""

        raise NotImplementedError

    def _subir(self, indice: int) -> None:
        """Desplaza hacia arriba el nodo ubicado en ``indice``."""

        raise NotImplementedError

    def _bajar(self, indice: int) -> None:
        """Desplaza hacia abajo el nodo ubicado en ``indice``."""

        raise NotImplementedError

    def _indice_padre(self, indice: int) -> int:
        """Calcula el índice del padre; la raíz no tiene padre."""

        raise NotImplementedError

    def _indice_izquierdo(self, indice: int) -> int:
        """Calcula el índice del hijo izquierdo."""

        raise NotImplementedError

    def _indice_derecho(self, indice: int) -> int:
        """Calcula el índice del hijo derecho."""

        raise NotImplementedError

    def cumple_propiedad_heap(self) -> bool:
        """Comprueba que todo padre sea menor o igual que sus hijos."""

        raise NotImplementedError


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

    raise NotImplementedError("Completa ultima_piedra en tu entrega")
