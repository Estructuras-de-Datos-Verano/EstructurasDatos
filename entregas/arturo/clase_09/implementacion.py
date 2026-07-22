from __future__ import annotations
import networkx as nx
from abc import ABC, abstractmethod
from typing import Any
import matplotlib as plt

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
        self.adyacencias : dict[str, set[str]] = {}

        
    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        self.agregar_vertice(destino)
        self.agregar_vertice(origen)
        
        self.adyacencias[origen].add(destino)
        self.adyacencias[destino].add(origen)



    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        if vertice in self.adyacencias:
            return list(self.adyacencias[vertice])

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

        return vertice in self.adyacencias

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""
        if origen in self.adyacencias:
            return destino in self.adyacencias[origen]


    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        return len(self.adyacencias)

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""

        total = sum(len(vecinos) for vecinos in self.adyacencias.values())
        return total // 2

class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando matriz de adyacencia.

    Sugerencia de representación:

    - una lista de listas de booleanos;
    - un diccionario ``dict[str, int]`` para mapear vértices a índices.
    """

    def __init__(self) -> None:
        """Crea un grafo vacío."""
        self.indices: dict[str, int] = {}
        self.matriz: list[list[bool]] = []
        
    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

        if vertice not in self.indices:
            nuevo_idx = len(self.indices)
            self.indices[vertice] = nuevo_idx

            for fila in self.matriz:
                fila.append(False)

            nueva_fila = [False] * (nuevo_idx + 1)
            self.matriz.append(nueva_fila)

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        i = self.indices[origen]
        j = self.indices[destino]

        self.matriz[i][j] = True
        self.matriz[j][i] = True


    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        if vertice not in self.indices:
            return []
        
        indice = self.indices[vertice]
        lista_vecinos = []

        for nombre, columna in self.indices.items():
            if self.matriz[indice][columna]:
                lista_vecinos.append(nombre)
        return lista_vecinos


    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""
        return vertice in self.indices
        

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""
        if self.contiene_vertice(origen) and self.contiene_vertice(destino):
            indice_origen = self.indices[origen]
            indice_destino = self.indices[destino]
            
            return self.matriz[indice_destino][indice_origen]
        else: 
            return False
        

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        return len(self.indices)

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""
        total_conexiones = sum(fila.count(True) for fila in self.matriz)

        return total_conexiones // 2
        


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    """Construye un grafo pequeño para pruebas y visualización."""
    grafo = GrafoListaAdyacencia()

    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")

    grafo.agregar_arista("A","B")
    grafo.agregar_arista("A","D")
    
    return grafo

    

def convertir_a_networkx(grafo: GrafoAbstracto) -> Any:
    """Convierte una implementación propia a ``networkx.Graph``.

    Esta función permite comparar nuestra implementación con una biblioteca
    externa y visualizar el grafo.
    """
    g_nx = nx.Graph()

    if hasattr(grafo, 'adyacencias'):
        vertices = grafo.adyacencias.keys()
    else:
        vertices = grafo.indices.keys()

    for vertice in vertices:
        g_nx.add_node(vertice)
        for vecino in grafo.vecinos(vertice):
            g_nx.add_edge(vertice,vecino)
        
    return g_nx

def guardar_visualizacion_grafo(
    grafo: GrafoAbstracto, ruta: str = "grafo_visual.png"
) -> None:
    """Convierte el grafo a NetworkX y guarda una visualización en PNG."""

    g_nx = convertir_a_networkx(grafo)
    nx.draw(g_nx , with_labels=True)
    plt.savefig(ruta)
    plt.close()