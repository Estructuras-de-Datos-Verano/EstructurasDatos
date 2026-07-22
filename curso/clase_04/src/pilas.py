"""Implementaciones pedagógicas de una pila.

La clase se centra en la idea de Tipo de Dato Abstracto: varias clases pueden
tener la misma interfaz pública aunque usen herramientas internas distintas.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Any


class PilaAbstracta(ABC):
    """Contrato común para cualquier implementación de pila."""

    @abstractmethod
    def push(self, elemento: Any) -> None:
        """Agrega ``elemento`` a la cima de la pila."""

    @abstractmethod
    def pop(self) -> Any:
        """Elimina y regresa el elemento en la cima.

        Debe lanzar ``IndexError`` si la pila está vacía.
        """

    @abstractmethod
    def peek(self) -> Any:
        """Regresa el elemento en la cima sin eliminarlo.

        Debe lanzar ``IndexError`` si la pila está vacía.
        """

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Indica si la pila no contiene elementos."""

    @abstractmethod
    def tamano(self) -> int:
        """Regresa la cantidad de elementos en la pila."""


class PilaLista(PilaAbstracta):
    """Pila implementada con ``list``.

    El final de la lista representa la cima de la pila.
    """

    def __init__(self) -> None:
        self._datos: list[Any] = []

    def push(self, elemento: Any) -> None:
        self._datos.append(elemento)

    def pop(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer pop de una pila vacía")
        return self._datos.pop()

    def peek(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer peek de una pila vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)


class PilaDeque(PilaAbstracta):
    """Pila implementada con ``collections.deque``.

    La derecha del deque representa la cima de la pila.
    """

    def __init__(self) -> None:
        self._datos: deque[Any] = deque()

    def push(self, elemento: Any) -> None:
        self._datos.append(elemento)

    def pop(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer pop de una pila vacía")
        return self._datos.pop()

    def peek(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer peek de una pila vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)


class PilaTupla(PilaAbstracta):
    """Pila implementada con ``tuple``.

    Esta implementación sirve para discutir inmutabilidad: cada ``push`` o
    ``pop`` reemplaza la tupla interna por una nueva tupla.
    """

    def __init__(self) -> None:
        self._datos: tuple[Any, ...] = ()

    def push(self, elemento: Any) -> None:
        self._datos = self._datos + (elemento,)

    def pop(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer pop de una pila vacía")
        elemento = self._datos[-1]
        self._datos = self._datos[:-1]
        return elemento

    def peek(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer peek de una pila vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        return len(self._datos) == 0

    def tamano(self) -> int:
        return len(self._datos)


@dataclass
class Nodo:
    """Nodo simple para el reto opcional de ``PilaNodo``."""

    valor: Any
    siguiente: "Nodo | None" = None


class PilaNodo(PilaAbstracta):
    """Reto opcional: pila con nodos enlazados.

    Esta implementación es una vista previa de listas ligadas. No es el centro
    de la Clase 04.
    """

    def __init__(self) -> None:
        self._cima: Nodo | None = None
        self._tamano = 0

    def push(self, elemento: Any) -> None:
        self._cima = Nodo(elemento, self._cima)
        self._tamano += 1

    def pop(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer pop de una pila vacía")
        assert self._cima is not None
        elemento = self._cima.valor
        self._cima = self._cima.siguiente
        self._tamano -= 1
        return elemento

    def peek(self) -> Any:
        if self.esta_vacia():
            raise IndexError("no se puede hacer peek de una pila vacía")
        assert self._cima is not None
        return self._cima.valor

    def esta_vacia(self) -> bool:
        return self._cima is None

    def tamano(self) -> int:
        return self._tamano


def vaciar_pila(pila: PilaAbstracta) -> list[Any]:
    """Extrae todos los elementos de una pila y los regresa en orden de salida."""

    elementos: list[Any] = []
    while not pila.esta_vacia():
        elementos.append(pila.pop())
    return elementos


def transferir_elementos(origen: PilaAbstracta, destino: PilaAbstracta) -> None:
    """Mueve todos los elementos de ``origen`` a ``destino`` usando la interfaz."""

    while not origen.esta_vacia():
        destino.push(origen.pop())
