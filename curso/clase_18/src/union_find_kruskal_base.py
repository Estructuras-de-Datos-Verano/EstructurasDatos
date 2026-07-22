"""Código base de la Clase 18; no contiene las soluciones."""

from __future__ import annotations

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        raise NotImplementedError("Completa UnionFind.__init__ en tu entrega")

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento``."""

        raise NotImplementedError("Completa UnionFind.find en tu entrega")

    def union(self, a: int, b: int) -> bool:
        """Une componentes y devuelve si la unión fue efectiva."""

        raise NotImplementedError("Completa UnionFind.union en tu entrega")

    def conectados(self, a: int, b: int) -> bool:
        """Indica si dos elementos pertenecen a la misma componente."""

        raise NotImplementedError("Completa UnionFind.conectados en tu entrega")

    def tamano_componente(self, elemento: int) -> int:
        """Devuelve el tamaño de la componente del elemento."""

        raise NotImplementedError("Completa UnionFind.tamano_componente en tu entrega")

    def numero_componentes(self) -> int:
        """Devuelve la cantidad actual de componentes."""

        raise NotImplementedError("Completa UnionFind.numero_componentes en tu entrega")


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    """Calcula un árbol de expansión mínima o devuelve ``None``."""

    raise NotImplementedError("Completa kruskal en tu entrega")


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""

    raise NotImplementedError("Completa costo_reparacion en tu entrega")
