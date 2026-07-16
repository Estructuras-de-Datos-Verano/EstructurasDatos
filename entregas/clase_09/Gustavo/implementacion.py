from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import networkx as nx
import matplotlib.pyplot as plt


class GrafoAbstracto(ABC):
    """Interfaz común para grafos no dirigidos simples."""

    @abstractmethod
    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""
        pass

    @abstractmethod
    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""
        pass

    @abstractmethod
    def vecinos(self, vertice: str) -> list[str]:
        """Regresa la lista de vecinos de ``vertice``."""
        pass

    @abstractmethod
    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""
        pass

    @abstractmethod
    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe una arista entre ``origen`` y ``destino``."""
        pass

    @abstractmethod
    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices del grafo."""
        pass

    @abstractmethod
    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas del grafo."""
        pass


class GrafoListaAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando un diccionario de conjuntos."""

    def __init__(self) -> None:
        """Crea un grafo vacío."""
        self._adyacencia: dict[str, set[str]] = {}

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        # Al ser no dirigido, agregamos en ambos sentidos
        self._adyacencia[origen].add(destino)
        self._adyacencia[destino].add(origen)

    def vecinos(self, vertice: str) -> list[str]:
        if vertice not in self._adyacencia:
            return []
        return list(self._adyacencia[vertice])

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if origen not in self._adyacencia:
            return False
        return destino in self._adyacencia[origen]

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        # Sumamos todos los vecinos y dividimos entre 2 porque cada arista
        # se cuenta dos veces (una en cada extremo)
        total = sum(len(vecinos) for vecinos in self._adyacencia.values())
        return total // 2


class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando una matriz booleana e índices."""

    def __init__(self) -> None:
        """Crea un grafo vacío."""
        self._indices: dict[str, int] = {}
        self._vertices: list[str] = []
        self._matriz: list[list[bool]] = []

    def agregar_vertice(self, vertice: str) -> None:
        if vertice in self._indices:
            return
        
        nuevo_indice = len(self._vertices)
        self._indices[vertice] = nuevo_indice
        self._vertices.append(vertice)
        
        # Le agregamos una columna extra (False) a cada fila existente
        for fila in self._matriz:
            fila.append(False)
            
        # Agregamos una nueva fila completa de puros False al final
        nueva_fila = [False] * len(self._vertices)
        self._matriz.append(nueva_fila)

    def agregar_arista(self, origen: str, destino: str) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        
        idx_origen = self._indices[origen]
        idx_destino = self._indices[destino]
        
        # Marcamos True en ambos sentidos (es simétrico)
        self._matriz[idx_origen][idx_destino] = True
        self._matriz[idx_destino][idx_origen] = True

    def vecinos(self, vertice: str) -> list[str]:
        if vertice not in self._indices:
            return []
            
        idx = self._indices[vertice]
        resultado = []
        for i, conectado in enumerate(self._matriz[idx]):
            if conectado:
                resultado.append(self._vertices[i])
        return resultado

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._indices

    def contiene_arista(self, origen: str, destino: str) -> bool:
        if origen not in self._indices or destino not in self._indices:
            return False
            
        idx_origen = self._indices[origen]
        idx_destino = self._indices[destino]
        return self._matriz[idx_origen][idx_destino]

    def cantidad_vertices(self) -> int:
        return len(self._vertices)

    def cantidad_aristas(self) -> int:
        total = 0
        n = len(self._vertices)
        # Recorremos solo la mitad superior de la matriz para no contar doble
        for i in range(n):
            for j in range(i + 1, n):
                if self._matriz[i][j]:
                    total += 1
        return total


def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    """Construye un grafo sencillo de prueba y lo regresa."""
    grafo = GrafoListaAdyacencia()
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    return grafo


def convertir_a_networkx(grafo: GrafoAbstracto) -> nx.Graph:
    """Convierte cualquier clase que cumpla la interfaz a un grafo de NetworkX."""
    G = nx.Graph()
    # Para no asumir directamente cómo almacena internamente los datos, 
    # obtenemos sus aristas consultando los vecinos de cada vértice.
    aristas_agregadas = set()
    
    # Extraemos todos los vértices del grafo abstractamente si es posible,
    # o aprovechamos que podemos inspeccionarlos desde la implementación:
    if isinstance(grafo, GrafoListaAdyacencia):
        nodos = list(grafo._adyacencia.keys())
    elif isinstance(grafo, GrafoMatrizAdyacencia):
        nodos = list(grafo._vertices)
    else:
        nodos = []

    for origen in nodos:
        G.add_node(origen)
        for destino in grafo.vecinos(origen):
            # Ordenamos el par para no procesar dos veces la misma arista (A-B es igual a B-A)
            par = tuple(sorted([origen, destino]))
            if par not in aristas_agregadas:
                G.add_edge(origen, destino)
                aristas_agregadas.add(par)
                
    return G


def guardar_visualizacion_grafo(grafo: GrafoAbstracto, ruta: str = "grafo_visual.png") -> None:
    """Convierte el grafo a NetworkX y guarda una imagen PNG en la ruta indicada."""
    G = convertir_a_networkx(grafo)
    
    plt.figure(figsize=(6, 5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="#bbf7d0", edge_color="#64748b", node_size=1000, font_weight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(ruta, bbox_inches="tight")
    plt.close()


# Bloque opcional para que tú lo pruebes en tu consola. 
# Al estar dentro del 'if __name__ == "__main__":', NO ejecutará visualizaciones 
# ni importará ruido cuando el evaluador de tu universidad lo importe.
if __name__ == "__main__":
    g = construir_grafo_ejemplo()
    print("Vértices en el grafo de ejemplo:", g.cantidad_vertices())
    print("Aristas en el grafo de ejemplo:", g.cantidad_aristas())
    print("Vecinos de A:", g.vecinos("A"))
    
    # Prueba rápida de guardado
    guardar_visualizacion_grafo(g, "mi_prueba_visual.png")
    print("Se guardó la imagen de prueba como 'mi_prueba_visual.png'.")