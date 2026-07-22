from __future__ import annotations

from abc import ABC, abstractmethod


class GrafoAbstracto(ABC):
    @abstractmethod
    def agregar_vertice(self, vertice: str) -> None:
        ...

    @abstractmethod
    def agregar_arista(self, origen: str, destino: str) -> None:
        ...

    @abstractmethod
    def vecinos(self, vertice: str) -> list[str]:
        ...

    @abstractmethod
    def contiene_vertice(self, vertice: str) -> bool:
        ...

    @abstractmethod
    def contiene_arista(self, origen: str, destino: str) -> bool:
        ...

    @abstractmethod
    def cantidad_vertices(self) -> int:
        ...

    @abstractmethod
    def cantidad_aristas(self) -> int:
        ...

    @abstractmethod
    def vertices(self) -> list[str]:
        ...


class GrafoListaAdyacencia(GrafoAbstracto):
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
        return destino in self._adyacencia.get(origen, set())

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        return sum(len(vecinos) for vecinos in self._adyacencia.values()) // 2

    def vertices(self) -> list[str]:
        return list(self._adyacencia.keys())


class GrafoMatrizAdyacencia(GrafoAbstracto):
    def __init__(self) -> None:
        self._indices: dict[str, int] = {}
        self._matriz: list[list[bool]] = []

    def agregar_vertice(self, vertice: str) -> None:
        if vertice in self._indices:
            return
        indice = len(self._indices)
        self._indices[vertice] = indice
        for fila in self._matriz:
            fila.append(False)
        self._matriz.append([False] * (indice + 1))

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        i = self._indices[origen]
        j = self._indices[destino]
        self._matriz[i][j] = True
        self._matriz[j][i] = True

    def vecinos(self, vertice: str) -> list[str]:
        if vertice not in self._indices:
            return []
        i = self._indices[vertice]
        return [v for v, j in self._indices.items() if self._matriz[i][j]]

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._indices

    def contiene_arista(self, origen: str, destino: str) -> bool:
        return (
            origen in self._indices
            and destino in self._indices
            and self._matriz[self._indices[origen]][self._indices[destino]]
        )

    def cantidad_vertices(self) -> int:
        return len(self._indices)

    def cantidad_aristas(self) -> int:
        total = 0
        n = len(self._matriz)
        for i in range(n):
            for j in range(i + 1, n):
                if self._matriz[i][j]:
                    total += 1
        return total

    def vertices(self) -> list[str]:
        return list(self._indices.keys())


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    grafo = GrafoListaAdyacencia()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")
    return grafo


def convertir_a_networkx(grafo: GrafoAbstracto):
    import networkx as nx

    G = nx.Graph()
    for vertice in grafo.vertices():
        G.add_node(vertice)

    for origen in grafo.vertices():
        for destino in grafo.vecinos(origen):
            if not G.has_edge(origen, destino):
                G.add_edge(origen, destino)
    return G


def guardar_visualizacion_grafo(grafo: GrafoAbstracto, ruta: str = "grafo_visual.png") -> None:
    import matplotlib.pyplot as plt
    import networkx as nx

    G = convertir_a_networkx(grafo)
    pos = nx.spring_layout(G, seed=7)
    plt.figure(figsize=(5, 4))
    nx.draw(G, pos, with_labels=False, node_color="#ddd6fe", edge_color="#64748b", node_size=1200)
    nx.draw_networkx_labels(G, pos)
    plt.axis("off")
    plt.savefig(ruta, bbox_inches="tight")
    plt.close()
