"""Punto de partida de la Clase 17.

Completa las operaciones sin cambiar sus nombres ni sus firmas públicas. No
uses ``collections.deque`` ni un heap: la finalidad es construir las
estructuras auxiliares que necesitan BFS y 0-1 BFS.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class NodoSimple(Generic[T]):
    """Nodo de una lista simplemente ligada."""

    valor: T
    siguiente: NodoSimple[T] | None = None


@dataclass(slots=True)
class NodoDoble(Generic[T]):
    """Nodo de una lista doblemente ligada."""

    valor: T
    anterior: NodoDoble[T] | None = None
    siguiente: NodoDoble[T] | None = None


class ColaLigada(Generic[T]):
    """Cola FIFO implementada con nodos simples."""

    def __init__(self) -> None:
        self._frente: NodoSimple[T] | None = None
        self._final: NodoSimple[T] | None = None
        self._tamano = 0

    def encolar(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""

        raise NotImplementedError

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""

        raise NotImplementedError

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""

        raise NotImplementedError

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""

        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class DequeLigada(Generic[T]):
    """Deque implementada con nodos dobles."""

    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
        """Agrega un valor al inicio en O(1)."""

        raise NotImplementedError

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""

        raise NotImplementedError

    def quitar_inicio(self) -> T:
        """Retira y devuelve el inicio; lanza IndexError si está vacía."""

        raise NotImplementedError

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""

        raise NotImplementedError

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""

        raise NotImplementedError

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""

        raise NotImplementedError

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""

        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Devuelve la tabla de predecesores de un BFS desde ``origen``."""

    raise NotImplementedError


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""

    raise NotImplementedError


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""

    raise NotImplementedError


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""

    raise NotImplementedError


def camino_cero_uno(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str
) -> tuple[float, list[str]]:
    """Devuelve el costo y un camino mínimo 0-1; ``(inf, [])`` si no existe."""

    raise NotImplementedError


__all__ = [
    "NodoSimple",
    "NodoDoble",
    "ColaLigada",
    "DequeLigada",
    "bfs_predecesores",
    "reconstruir_camino",
    "bfs_camino",
    "cero_uno_bfs",
    "camino_cero_uno",
]
