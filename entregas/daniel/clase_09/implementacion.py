

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class GrafoAbstracto(ABC):
    """Interfaz común para grafos no dirigidos simples."""

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
    """Grafo no dirigido simple implementado con diccionario de conjuntos."""

    def __init__(self) -> None:
        self._adyacencia: dict[str, set[str]] = {}
        self._cantidad_aristas = 0

    def agregar_vertice(self, vertice: str) -> None:
        if not self.contiene_vertice(vertice):
            self._adyacencia[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        if self.contiene_arista(origen, destino):
            return

        self._adyacencia[origen].add(destino)
        self._adyacencia[destino].add(origen)
        self._cantidad_aristas += 1

    def vecinos(self, vertice: str) -> list[str]:
        if not self.contiene_vertice(vertice):
            return []
        return sorted(self._adyacencia[vertice])

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            return False
        return destino in self._adyacencia[origen]

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        return self._cantidad_aristas


class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple implementado con matriz de adyacencia."""

    def __init__(self) -> None:
        self._vertices: dict[str, int] = {}
        self._matriz: list[list[bool]] = []
        self._cantidad_aristas = 0

    def agregar_vertice(self, vertice: str) -> None:
        if self.contiene_vertice(vertice):
            return

        indice = len(self._vertices)
        self._vertices[vertice] = indice

        for fila in self._matriz:
            fila.append(False)

        self._matriz.append([False] * (indice + 1))

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        if self.contiene_arista(origen, destino):
            return

        indice_origen = self._vertices[origen]
        indice_destino = self._vertices[destino]
        self._matriz[indice_origen][indice_destino] = True
        self._matriz[indice_destino][indice_origen] = True
        self._cantidad_aristas += 1

    def vecinos(self, vertice: str) -> list[str]:
        if not self.contiene_vertice(vertice):
            return []

        indice = self._vertices[vertice]
        vecinos: list[str] = []
        for nombre, posicion in self._vertices.items():
            if self._matriz[indice][posicion]:
                vecinos.append(nombre)

        return sorted(vecinos)

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._vertices

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            return False

        indice_origen = self._vertices[origen]
        indice_destino = self._vertices[destino]
        return self._matriz[indice_origen][indice_destino]

    def cantidad_vertices(self) -> int:
        return len(self._vertices)

    def cantidad_aristas(self) -> int:
        return self._cantidad_aristas


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:

    grafo = GrafoListaAdyacencia()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")
    return grafo


def _obtener_vertices(grafo: GrafoAbstracto) -> list[str]:
    if hasattr(grafo, "_adyacencia"):
        return list(grafo._adyacencia.keys())
    if hasattr(grafo, "_vertices"):
        return list(grafo._vertices.keys())
    return []


def convertir_a_networkx(grafo: GrafoAbstracto) -> Any:

    import networkx as nx

    vertices = _obtener_vertices(grafo)
    grafo_nx = nx.Graph()
    grafo_nx.add_nodes_from(vertices)

    for vertice in vertices:
        for vecino in grafo.vecinos(vertice):
            if vertice < vecino:
                grafo_nx.add_edge(vertice, vecino)

    return grafo_nx


def guardar_visualizacion_grafo(
    grafo: GrafoAbstracto, ruta: str = "grafo_visual.png"
) -> None:

    import matplotlib.pyplot as plt
    import networkx as nx

    grafo_nx = convertir_a_networkx(grafo)
    pos = nx.spring_layout(grafo_nx)
    nx.draw(grafo_nx, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    plt.savefig(ruta)
    plt.close()

