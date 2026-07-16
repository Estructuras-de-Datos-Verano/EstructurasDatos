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
        self.aristas = []
        self.vertices = []
        

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""
        
        if vertice in self.vertices:
            raise ValueError("Ya está dentro.")

        self.vertices.append(vertice)

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        if (origen,destino) or (destino, origen) in self.aristas:
            raise ValueError("No se admiten aristas repetidas.")
        
        self.aristas.append((origen,destino))
        

    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        if vertice not in self.vertices:
            raise ValueError("Ése no es un vértice presente.")
        
        vecinos = []

        for (i,j) in self.aristas:
            if i == vertice:
                vecinos.append(j)
            elif j == vertice:
                vecinos.append(i)

        return vecinos

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

        if vertice in self.vertices:
            return True
        
        else:
            return False

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""

        if (origen, destino) or (destino, origen) in self.aristas:
            return True
        else:
            return False

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        return len(self.vertices)

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas."""

        return len(self.aristas)


class GrafoMatrizAdyacencia(GrafoAbstracto):
    """Grafo no dirigido simple usando matriz de adyacencia.

    Sugerencia de representación:

    - una lista de listas de booleanos;
    - un diccionario ``dict[str, int]`` para mapear vértices a índices.
    """

    def __init__(self) -> None:
        """Crea un grafo vacío."""

        self._indices = {}
        self._matriz = []
        self._vertices = []

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega ``vertice`` al grafo si todavía no existe."""

        if vertice in self._vertices:
            raise ValueError("Ya está dentro.")

        self._vertices.append(vertice)
        self._indices[vertice] = len(self._vertices) - 1 
        #Agrega al diccionario el nuevo vértice con su índice correspondiente, el cual se obtiene restando uno porque comienza de cero.
        for fila in self._matriz:
            fila.append(False)
        self._matriz.append([False] * len(self._vertices))

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una arista no dirigida entre ``origen`` y ``destino``."""

        if origen not in self._indices or destino not in self._indices:
            raise ValueError("Uno o ambos vértices no existen en el grafo.")
        
        indice_origen = self._indices[origen]
        indice_destino = self._indices[destino]

        # Como no es dirigido, se marca la arista en ambas direcciones.
        self._matriz[indice_origen][indice_destino] = True
        self._matriz[indice_destino][indice_origen] = True

    def vecinos(self, vertice: str) -> list[str]:
        """Regresa los vecinos de ``vertice``."""

        if vertice not in self._indices:
            raise ValueError("Ése no es un vértice presente.")
        
        indice = self._indices[vertice]
        vecinos = []
        
        for i, es_vecino in enumerate(self._matriz[indice]): #Se va a la fila. Si se encuentra un true, el vértice de esa columna es vecino. 
            if es_vecino:
                vecinos.append(self._vertices[i])
        return vecinos

    def contiene_vertice(self, vertice: str) -> bool:
        """Indica si ``vertice`` pertenece al grafo."""

        if vertice in self._vertices:
            return True
        else:
            return False

    def contiene_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la arista no dirigida ``origen``--``destino``."""

        if origen not in self._indices or destino not in self._indices:
            return False
        return self._matriz[self._indices[origen]][self._indices[destino]]
        

    def cantidad_vertices(self) -> int:
        """Regresa la cantidad de vértices."""

        return len(self._vertices)

    def cantidad_aristas(self) -> int:
        """Regresa la cantidad de aristas no dirigidas.
            Solo revisa la mitad superior de la matriz, ya que es simétrica. 
            Si hay un True en [A][B], lo hay en [B][A]. 
            No queremos contar doble.
            Asimismo, 
        """

        total_aristas = 0
        n = len(self._vertices)
        for i in range(n):
            for j in range(i + 1, n):
                if self._matriz[i][j]:
                    total_aristas += 1
        return total_aristas