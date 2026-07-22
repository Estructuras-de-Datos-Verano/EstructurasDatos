"""Implementaciones pedagógicas de una cola.

La clase se centra en la idea de Tipo de Dato Abstracto: una cola se reconoce
por su comportamiento FIFO, aunque pueda implementarse de distintas formas.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from typing import Any


class ColaAbstracta(ABC):
    """Contrato común para cualquier implementación de cola."""

    @abstractmethod
    def encolar(self, elemento: Any) -> None:
        """Agrega ``elemento`` al final lógico de la cola."""

    @abstractmethod
    def desencolar(self) -> Any:
        """Elimina y regresa el primer elemento que entró.

        Debe lanzar ``IndexError`` si la cola está vacía.
        """

    @abstractmethod
    def frente(self) -> Any:
        """Regresa el próximo elemento sin eliminarlo.

        Debe lanzar ``IndexError`` si la cola está vacía.
        """

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos."""

    @abstractmethod
    def tamano(self) -> int:
        """Regresa la cantidad de elementos en la cola."""


class ColaLista(ColaAbstracta):
    """Cola implementada con ``list``.

    El inicio de la lista representa el frente de la cola. Esta implementación
    es clara para aprender FIFO, pero ``pop(0)`` puede ser costoso porque los
    elementos restantes se recorren una posición.
    """

    def __init__(self) -> None:
        self._datos: list[Any] = []

    def encolar(self, elemento: Any) -> None:
        self._datos.append(elemento)

    def desencolar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede desencolar de una cola vacía")
        return self._datos.pop(0)

    def frente(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede consultar el frente de una cola vacía")
        return self._datos[0]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)


class ColaDeque(ColaAbstracta):
    """Cola implementada con ``collections.deque``.

    ``deque`` está diseñada para insertar y eliminar eficientemente por ambos
    extremos. Para una cola FIFO usamos ``append`` al final y ``popleft`` al
    frente.
    """

    def __init__(self) -> None:
        self._datos: deque[Any] = deque()

    def encolar(self, elemento: Any) -> None:
        self._datos.append(elemento)

    def desencolar(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede desencolar de una cola vacía")
        return self._datos.popleft()

    def frente(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede consultar el frente de una cola vacía")
        return self._datos[0]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)


def vaciar_cola(cola: ColaAbstracta) -> list[Any]:
    """Extrae todos los elementos de una cola en orden FIFO."""

    elementos: list[Any] = []
    while not cola.esta_vacia():
        elementos.append(cola.desencolar())
    return elementos


def cargar_cola(cola: ColaAbstracta, elementos: list[Any]) -> ColaAbstracta:
    """Agrega varios ``elementos`` a una cola y regresa la misma cola.

    Esta función sirve para practicar polimorfismo: funciona con cualquier
    objeto que respete la interfaz de ``ColaAbstracta``.
    """

    if not isinstance(elementos, list):
        raise TypeError("elementos debe ser una lista")

    for elemento in elementos:
        cola.encolar(elemento)
    return cola

