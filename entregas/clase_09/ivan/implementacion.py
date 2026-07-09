
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any
import networkx as nx
import matplotlib.pyplot as plt

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
    def __init__(self, dict_adyacencia: dict[str, set[str]] = None) -> None:
        """Crea un grafo (vacío por defecto)."""
        if dict_adyacencia is None:
            self._adyacencia = {}
        else:
            self._adyacencia = dict_adyacencia   

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""
        if not self.contiene_vertice(vertice):
            self._adyacencia[vertice] = set()
            print(f"Se agregó vértice: {vertice}. Grafo actual: {self._adyacencia}")
        else:
            print(f"El vértice ya está en el grafo")
       

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        if self.contiene_vertice(origen) and self.contiene_vertice(destino):
            self._adyacencia[origen].add(destino)
            self._adyacencia[destino].add(origen)
            print(f"Se añade arista no dirigida entre {origen} y {destino}")
        
    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""
        return list(self._adyacencia[vertice])

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""
        return self.contiene_vertice(origen) and self.contiene_vertice(destino) and destino in self._adyacencia[origen]

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""
        return len(self._adyacencia)    

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""
        return sum(len(vecinos) for vecinos in self._adyacencia.values()) // 2


class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando matriz de adyacencia.

    Sugerencia de representación:

    - una lista de listas de booleanos;
    - un diccionario ``dict[str, int]`` para mapear vértices a índices.
    """

    def __init__(self, indices: dict[str, int] = None, matriz: list[list[bool]] = None) -> None:
        """Crea un grafo vacío."""
        if indices is None and matriz is  None:
            self._indices: dict[str, int] = {}
            self._matriz: list[list[bool]] = []
        else:
            self._indices: dict[str, int] = indices
            self._matriz: list[list[bool]] = matriz

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""
        if not self.contiene_vertice(vertice):
            n = len(self._matriz) 
            self._indices[vertice] = n #Le corresponde el n+1 en teoría pero se cuenta desde el cero
        
            for fila in self._matriz:
                fila.append(False)
                
            self._matriz.append([False] * (n + 1)) # Añado una nueva fila en donde hay n+1 columnas con False por defecto
            print(f"Se agregó vértice: {vertice}. Grafo actual: {self._matriz}")

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        if self.contiene_vertice(origen) and self.contiene_vertice(destino):
             o = self._indices[origen]
             d = self._indices[destino]
             self._matriz[o][d] = True
             self._matriz[d][o] = True
             print(f"Se añade arista no dirigida entre {origen} y {destino}")

    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""
        fila = self._indices[vertice]
        fila_matriz = self._matriz[fila]
        vecinos = []
        for pos, val in enumerate(fila_matriz):
            if val:
                for nombre, indice in self._indices.items():
                    if indice == pos:
                        vecinos.append(nombre)
                        break
        return vecinos
        
    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""
        return vertice in self._indices

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""
        if not self.contiene_vertice(origen) or not self.contiene_vertice(destino):
            return False # evitar errores
        o = self._indices[origen]
        d = self._indices[destino]
        return self._matriz[o][d] and self._matriz[d][o]


    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""
        return len(self._indices)

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""
        count = 0
        for y in range(len(self._matriz)):
            for x in range(len(self._matriz[y])):
                if self._matriz[y][x] == True and self._matriz[x][y] == True:
                    count += 1
        return count // 2

def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    """Construye un grafo pequeño para pruebas y visualización."""

    ejemplin = GrafoListaAdyacencia()
    ejemplin.agregar_vertice("A")
    ejemplin.agregar_vertice("B")
    ejemplin.agregar_vertice("C")
    ejemplin.agregar_arista("A", "B")
    ejemplin.agregar_arista("A", "C")
    ejemplin.cantidad_aristas()
    ejemplin.cantidad_vertices()
    ejemplin.vecinos("A")
    ejemplin.contiene_vertice("A")
    ejemplin.contiene_arista("A", "B")
    
    return ejemplin



def convertir_a_networkx(grafo: GrafoAbstracto) -> nx.Graph:
    """Convierte una implementación propia a ``networkx.Graph``.

    Esta función permite comparar nuestra implementación con una biblioteca
    externa y visualizar el grafo.
    """
    G = nx.Graph()
    
    # Solución universal: Usamos la cantidad de vértices basándonos en la clase
    # Si es matriz usamos _indices, si es lista usamos _adyacencia
    vertices = (
        grafo._indices.keys() 
        if isinstance(grafo, GrafoMatrizAdyacencia) 
        else grafo._adyacencia.keys()
    )
    
    for v in vertices:
        G.add_node(v)
        for vecino in grafo.vecinos(v):
            G.add_edge(v, vecino)
            
    return G  # IMPORTANTE: Retornamos el grafo de networkx para poder usarlo


# Modificamos esta función para que reciba y dibuje el grafo correcto
def guardar_visualizacion_grafo(
    grafo: GrafoAbstracto, ruta: str = "grafo_visual.png"
) -> None:
    """Convierte el grafo a NetworkX y guarda una visualización en PNG."""
    
    # 1. PASO CRUCIAL: Convertimos tu grafo al formato que NetworkX entiende
    G_nx = convertir_a_networkx(grafo)

    # 2. Ahora usamos G_nx en lugar de 'grafo'
    pos = nx.circular_layout(G_nx)
    plt.figure(figsize=(5, 4))
    
    # Dibujamos usando G_nx
    nx.draw(G_nx, pos, with_labels=False, node_color="#ddd6fe", edge_color="#64748b", node_size=1200)
    nx.draw_networkx_labels(G_nx, pos)
    
    plt.axis("off")
    plt.savefig(ruta, bbox_inches="tight")  # Usamos la variable 'ruta' dinámicamente
    plt.close() # Buena práctica para cerrar la ventana flotante en segundo plano
    print(f"Imagen guardada como {ruta}")


if __name__ == "__main__":
    grafo_ejemplo = construir_grafo_ejemplo()
    
    # 1. Mostramos la ventana interactiva con spring_layout
    grafo_nx_interactivo = convertir_a_networkx(grafo_ejemplo)
    pos = nx.spring_layout(grafo_nx_interactivo, seed=7)
    plt.figure(figsize=(5, 4))
    nx.draw(grafo_nx_interactivo, pos, with_labels=False, node_color="#bfdbfe", edge_color="#64748b", node_size=1200)
    nx.draw_networkx_labels(grafo_nx_interactivo, pos)
    plt.title("spring_layout")
    plt.axis("off")
    #plt.show() # Muestra el primer dibujo en pantalla
    
    # 2. Guardamos la visualización circular en un archivo físico PNG
    guardar_visualizacion_grafo(grafo_ejemplo)