"""Código base para modelado de grafos.

Clase 09: Modelado de relaciones con grafos, implementaciones
polimórficas y visualización con NetworkX.

Este archivo contiene firmas y docstrings para trabajar durante la clase.
No contiene soluciones completas.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class GrafoAbstracto(ABC):
    """Interfaz común para grafos no dirigidos simples.

    Esta clase representa el contrato que deben cumplir las implementaciones.
    Un grafo no dirigido simple no distingue orientación en las aristas y no
    permite aristas duplicadas entre el mismo par de vértices.
    """

    @abstractmethod
    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

    @abstractmethod
    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

    @abstractmethod
    def vecinos(self, vertice: str) -> list[str]:
        """Regresa la lista de vecinos de ``vertice``."""

    @abstractmethod
    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

    @abstractmethod
    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe una arista entre ``origen`` y ``destino``."""

    @abstractmethod
    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices del grafo."""

    @abstractmethod
    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas del grafo."""


class GrafoListaAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando un diccionario de conjuntos.

    Sugerencia de representación:

    ``dict[str, set[str]]``

    Cada llave es un vértice y su conjunto asociado contiene sus vecinos.
    """

    def __init__(self) -> None:
        """Crea un grafo vacío."""

        raise NotImplementedError("Completa GrafoListaAdyacencia en tu entrega")

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

        raise NotImplementedError

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        raise NotImplementedError

    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        raise NotImplementedError

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

        raise NotImplementedError

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""

        raise NotImplementedError

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        raise NotImplementedError

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""

        raise NotImplementedError


class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando matriz de adyacencia.

    Sugerencia de representación:

    - una lista de listas de booleanos;
    - un diccionario ``dict[str, int]`` para mapear vértices a índices.
    """

    def __init__(self) -> None:
        """Crea un grafo vacío."""

        raise NotImplementedError("Completa GrafoMatrizAdyacencia en tu entrega")

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

        raise NotImplementedError

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        raise NotImplementedError

    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        raise NotImplementedError

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

        raise NotImplementedError

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""

        raise NotImplementedError

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        raise NotImplementedError

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""

        raise NotImplementedError


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    """Construye un grafo pequeño para pruebas y visualización."""

    raise NotImplementedError("Completa construir_grafo_ejemplo en tu entrega")


def convertir_a_networkx(grafo: GrafoAbstracto) -> Any:
    """Convierte una implementación propia a ``networkx.Graph``.

    Esta función permite comparar nuestra implementación con una biblioteca
    externa y visualizar el grafo.
    """

    raise NotImplementedError("Completa convertir_a_networkx en tu entrega")


def guardar_visualizacion_grafo(
    grafo: GrafoAbstracto, ruta: str = "grafo_visual.png"
) -> None:
    """Convierte el grafo a NetworkX y guarda una visualización en PNG."""

    raise NotImplementedError("Completa guardar_visualizacion_grafo en tu entrega")
