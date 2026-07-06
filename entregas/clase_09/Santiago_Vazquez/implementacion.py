from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import networkx as nx
import matplotlib.pyplot as plt

class GrafoAbstracto(ABC):
    """Interfaz común para grafos no dirigidos simples."""

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
    """Grafo no dirigido simple usando un diccionario de conjuntos."""

    def __init__(self) -> None:
        self._adyacencia: dict[str, set[str]] = {}

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self._adyacencia[origen].add(destino)
        self._adyacencia[destino].add(origen)

    def vecinos(self, vertice: str) -> list[str]:
        return list(self._adyacencia.get(vertice, []))

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if origen in self._adyacencia:
            return destino in self._adyacencia[origen]
        return False

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        suma_grados = sum(len(adyacentes) for adyacentes in self._adyacencia.values())
        return suma_grados // 2

class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando matriz de adyacencia."""

    def __init__(self) -> None:
        self._indices: dict[str, int] = {}
        self._matriz: list[list[bool]] = []

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._indices:
            nuevo_indice = len(self._indices)
            self._indices[vertice] = nuevo_indice
            for fila in self._matriz:
                fila.append(False)
            self._matriz.append([False] * (nuevo_indice + 1))

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        idx_origen = self._indices[origen]
        idx_destino = self._indices[destino]
        self._matriz[idx_origen][idx_destino] = True
        self._matriz[idx_destino][idx_origen] = True

    def vecinos(self, vertice: str) -> list[str]:
        if vertice not in self._indices:
            return []
        idx_vertice = self._indices[vertice]
        vecinos_lista = []
        for nodo, idx_nodo in self._indices.items():
            if self._matriz[idx_vertice][idx_nodo]:
                vecinos_lista.append(nodo)
        return vecinos_lista

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._indices

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if origen not in self._indices or destino not in self._indices:
            return False
        return self._matriz[self._indices[origen]][self._indices[destino]]

    def cantidad_vertices(self) -> int:
        return len(self._indices)

    def cantidad_aristas(self) -> int:
        contador = 0
        n = len(self._indices)
        for i in range(n):
            for j in range(i, n):
                if self._matriz[i][j]:
                    contador += 1
        return contador

def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    grafo = GrafoListaAdyacencia()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "E")
    return grafo

def convertir_a_networkx(grafo: GrafoAbstracto) -> Any:
    nx_grafo = nx.Graph()
    if isinstance(grafo, GrafoListaAdyacencia):
        for origen, vecinos_nodos in grafo._adyacencia.items():
            nx_grafo.add_node(origen)
            for destino in vecinos_nodos:
                nx_grafo.add_edge(origen, destino)
    elif isinstance(grafo, GrafoMatrizAdyacencia):
        nodos = list(grafo._indices.keys())
        for nodo in nodos:
            nx_grafo.add_node(nodo)
        n = len(nodos)
        for i in range(n):
            for j in range(i, n):
                if grafo._matriz[i][j]:
                    nx_grafo.add_edge(nodos[i], nodos[j])
    return nx_grafo

def guardar_visualizacion_grafo(
    grafo: GrafoAbstracto, ruta: str = "grafo_visual.png"
) -> None:
    G = convertir_a_networkx(grafo)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 5))
    nx.draw(G, pos, with_labels=True, node_color="#bfdbfe", edge_color="#64748b", node_size=1000)
    plt.savefig(ruta, bbox_inches="tight")
    plt.close()