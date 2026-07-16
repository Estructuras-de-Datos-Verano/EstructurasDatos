from abc import abstractmethod, ABC


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

    @abstractmethod
    def vertices(self) -> list[str]: 
        pass


class GrafoListaAdyacencia(GrafoAbstracto):
    def __init__(self):
        self._adyacencia: dict[str, set[str]] = {}

    def agregar_vertice(self, vertice: str) -> None:
        self._adyacencia[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        if origen not in self._adyacencia:
            self.agregar_vertice(origen)
        if destino not in self._adyacencia:
            self.agregar_vertice(destino)

        self._adyacencia[origen].add(destino)
        self._adyacencia[destino].add(origen)

    def vecinos(self, vertice: str) -> list[str]: 
        return list(self._adyacencia[vertice])

    def contiene_vertice(self, vertice: str) -> bool: 
        if vertice in self._adyacencia:
            return True
        else:
            return False

    def contiene_arista(self, origen: str, destino: str) -> bool: 
        if destino in self._adyacencia[origen] or origen in self._adyacencia[destino]:
            return True
        else:
            return False
    
    def cantidad_vertices(self) -> int: 
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int: 
        num_aris = 0
        for llave in self._adyacencia.keys():
            num_aris += len(self._adyacencia[llave])
        return num_aris/2
    
    def vertices(self) -> list[str]: 
        vertices = []
        for llave in self._adyacencia.keys():
            vertices.append(llave) 
        return vertices



class GrafoMatrizAdyacencia(GrafoAbstracto):
    
    def __init__(self):
        self._indices: dict[str, int] = {}
        self._matriz: list[list[bool]] = []

    def agregar_vertice(self, vertice: str) -> None:
        if vertice in self._indices:
            return
        indice = len(self._indices)
        self._indices[vertice] = indice
        for fila in self._matriz:
            fila.append(False)
        self._matriz.append([False] * (len(self ._indices)))
    
    def agregar_arista(self, origen: str, destino: str) -> None:
        if origen not in self._indices:
            self.agregar_vertice(origen)
        if destino not in self._indices:
            self.agregar_vertice(destino)
        i = self._indices[origen]
        j = self._indices[destino]
        self._matriz[i][j] = True
        self._matriz[j][i] = True

    def vecinos(self, vertice: str) -> list[str]:
        vecinos = []
        i = self._indices[vertice]
        for j in range(len(self._matriz)):
            if self._matriz[i][j]:
                for value, indice in self._indices.items():
                    if indice == j:
                        vecinos.append(value)

        return vecinos

    def contiene_vertice(self, vertice: str) -> bool: 
        if vertice in self._indices:
            return True
        else:
            return False

    def contiene_arista(self, origen: str, destino: str) -> bool: 
        if (self._matriz[self._indices[origen]])[self._indices[destino]] == True or (self._matriz[self._indices[destino]])[self._indices[origen]] == True:
            return True
        else:
            return False
    
    def cantidad_vertices(self) -> int: 
        return len(self._indices)

    def cantidad_aristas(self) -> int: 
        conteo_aris = 0
        for i in range(len(self._matriz)):
           for j in range(len(self._matriz)):
               if (self._matriz[i])[j] == True:
                   conteo_aris += 0.5
        return conteo_aris

    def vertices(self) -> list[str]: 
        vertices_l = []
        for llave in self._indices.keys():
            vertices_l.append(llave)
        return vertices_l





import networkx as nx
import matplotlib.pyplot as plt

def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    EJ = GrafoListaAdyacencia()
    EJ.agregar_vertice("A")
    EJ.agregar_vertice("B")
    EJ.agregar_vertice("C")
    EJ.agregar_vertice("D")
    EJ.agregar_vertice("E")
    EJ.agregar_arista("A", "B")
    EJ.agregar_arista("B", "C")
    EJ.agregar_arista("C", "D")
    EJ.agregar_arista("D", "E")
    EJ.agregar_arista("E", "A")
    return EJ

    
def convertir_a_networkx(grafo: GrafoAbstracto):
    G = nx.Graph()
    for vertice in grafo.vertices():
        G.add_node(vertice)
    for vert in grafo.vertices():
        for vecino in grafo.vecinos(vert):
            G.add_edge(vert, vecino)

    return G


def guardar_visualizacion_grafo(grafo: GrafoAbstracto, ruta: str = "grafo_visual.png") -> None:
    pos = nx.circular_layout(grafo)
    plt.figure(figsize=(5, 4))
    nx.draw(grafo, pos, with_labels=False, node_color="#ddd6fe", edge_color="#64748b", node_size=1200)
    nx.draw_networkx_labels(grafo, pos)
    plt.axis("off")
    plt.savefig(ruta, bbox_inches="tight")
    print("Imagen guardada como grafo_visual.png")