from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import networkx as nx
import matplotlib.pyplot as plt


class GrafoAbstracto(ABC):

    @abstractmethod
    def agregar_vertice(self, vertice: str) -> None:
        pass

    @abstractmethod
    def agregar_arista(self, origen: str, destino: str) -> None:
        pass

    @abstractmethod
    def vecinos(self, vertice: str) -> list[str]:
        pass

    @abstractmethod
    def contiene_vertice(self, vertice: str) -> bool:
        pass

    @abstractmethod
    def contiene_arista(self, origen: str, destino: str) -> bool:
        pass

    @abstractmethod
    def cantidad_vertices(self) -> int:
        pass

    @abstractmethod
    def cantidad_aristas(self) -> int:
        pass

class GrafoListaAdyacencia(GrafoAbstracto):
    def __init__(self) -> None:
        self._adyacencia: dict[str, set[str]] = {}
        self._num_aristas: int = 0

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        if origen not in self._adyacencia:
            self.agregar_vertice(origen)
        if destino not in self._adyacencia:
            self.agregar_vertice(destino)

        if destino not in self._adyacencia[origen]:
            self._adyacencia[origen].add(destino)
            self._adyacencia[destino].add(origen)
            self._num_aristas += 1

    def vecinos(self, vertice: str) -> list[str]:
        if not self.contiene_vertice(vertice):
            return []
        return list(self._adyacencia[vertice])

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            return False
        return destino in self._adyacencia[origen]

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        return self._num_aristas


class GrafoMatrizAdyacencia(GrafoAbstracto):
    def __init__(self) -> None:
        self._matriz: list[list[bool]] = []
        self._vertice_a_indice: dict[str, int] = {}
        self._indice_a_vertice: list[str] = []
        self._num_aristas: int = 0

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._vertice_a_indice:
            self._vertice_a_indice[vertice] = len(self._indice_a_vertice)
            self._indice_a_vertice.append(vertice)
            for fila in self._matriz:
                fila.append(False)
            self._matriz.append([False] * len(self._indice_a_vertice))

    def agregar_arista(self, origen: str, destino: str) -> None:
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            raise ValueError("Uno o ambos vértices no existen en el grafo.")
        if not self.contiene_arista(origen, destino):
            self._matriz[self._vertice_a_indice[origen]][self._vertice_a_indice[destino]] = True
            self._matriz[self._vertice_a_indice[destino]][self._vertice_a_indice[origen]] = True
            self._num_aristas += 1

    def vecinos(self, vertice: str) -> list[str]:
        if not self.contiene_vertice(vertice):
            return []
        indice = self._vertice_a_indice[vertice]
        return [self._indice_a_vertice[i] for i in range(len(self._matriz)) if self._matriz[indice][i]]

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._vertice_a_indice

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            return False
        return self._matriz[self._vertice_a_indice[origen]][self._vertice_a_indice[destino]]

    def cantidad_vertices(self) -> int:
        return len(self._indice_a_vertice)

    def cantidad_aristas(self) -> int:
        return self._num_aristas


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    grafo = GrafoListaAdyacencia()
    for vertice in ["A", "B", "C", "D", "E"]:
        grafo.agregar_vertice(vertice)
    return grafo


def convertir_a_networkx(grafo: GrafoAbstracto) -> Any:
    G = nx.Graph()
    if hasattr(grafo, '_adyacencia'):
        vertices = list(grafo._adyacencia.keys())
    elif hasattr(grafo, '_vertices_a_indice'):
        vertices = list(grafo._vertices_a_indice.keys())
    else:
        raise AttributeError("El grafo no cuenta con un atributo accesible para extraer los vértices.")
    G.add_nodes_from(vertices)
    for v in vertices:
        for vecino in grafo.vecinos(v):
            G.add_edge(v, vecino)      
    return G


def guardar_visualizacion_grafo(grafo: GrafoAbstracto, ruta: str = "grafo_visual.png") -> None:
    G = convertir_a_networkx(grafo)
    plt.clf()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
    plt.savefig(ruta, format ='png', bbox_inches='tight')
    plt.close()
