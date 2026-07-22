"""Punto de partida de la Clase 17.

Completa las operaciones sin cambiar sus nombres ni sus firmas públicas. No
uses ``collections.deque`` ni un heap: la finalidad es construir las
estructuras auxiliares que necesitan BFS y 0-1 BFS.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class NodoSimple(Generic[T]):
    """Nodo de una lista simplemente ligada."""

    valor: T
    siguiente: NodoSimple[T] | None = None


@dataclass(slots=True)
class NodoDoble(Generic[T]):
    """Nodo de una lista doblemente ligada."""

    valor: T
    anterior: NodoDoble[T] | None = None
    siguiente: NodoDoble[T] | None = None


class ColaLigada(Generic[T]):
    """Cola FIFO implementada con nodos simples."""

    def __init__(self) -> None:
        self._frente: NodoSimple[T] | None = None
        self._final: NodoSimple[T] | None = None
        self._tamano = 0

    def encolar(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""
        nuevo_nodo = NodoSimple(valor)
        if self.esta_vacia():
            self._frente = nuevo_nodo
        else:
            self._final.siguiente = nuevo_nodo
        self._final = nuevo_nodo
        self._tamano += 1

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola ligada está vacía")
        actual = self._frente
        self._frente = actual.siguiente
        if self._frente is None:
            self._final = None
        self._tamano -= 1
        return actual.valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola ligada está vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


class DequeLigada(Generic[T]):
    """Deque implementada con nodos dobles."""

    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
        """Agrega un valor al inicio en O(1)."""
        nuevo_nodo = NodoDoble(valor)
        if self._inicio is None:
            self._inicio = nuevo_nodo
            self._final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self._inicio
            self._inicio.anterior = nuevo_nodo
            self._inicio = nuevo_nodo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""
        nuevo_nodo = NodoDoble(valor)
        if self._final is None:
            self._inicio = nuevo_nodo
            self._final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self._final
            self._final.siguiente = nuevo_nodo
            self._final = nuevo_nodo
        self._tamano += 1

    def quitar_inicio(self) -> T:
        """Retira y devuelve el inicio; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque ligada está vacía")
        nodo_retirado = self._inicio
        self._inicio = self._inicio.siguiente
        if self._inicio is None:
            self._final = None
        else:
            self._inicio.anterior = None
            
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        self._tamano -= 1
        return nodo_retirado.valor

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque ligada está vacía")
        nodo_retirado = self._final
        self._final = self._final.anterior
        if self._final is None:
            self._inicio = None
        else:
            self._final.siguiente = None
            
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        self._tamano -= 1
        return nodo_retirado.valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("La deque ligada está vacía")
        return self._inicio.valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("La deque ligada está vacía")
        return self._final.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Devuelve la tabla de predecesores de un BFS desde ``origen``."""
    if origen not in grafo:
        raise KeyError("El nodo origen no se encuentra en el grafo")

    # Parche 4: Inicializar con todos los nodos del grafo en None para no omitir los inalcanzables[cite: 3]
    predecesores = {nodo: None for nodo in grafo}
    
    cola = ColaLigada()
    cola.encolar(origen)
    
    while not cola.esta_vacia():
        actual = cola.desencolar()
        for vecino in grafo.get(actual, []):
            # Usamos get para verificar si ya lo visitamos (evita sobreescribir el origen)
            if predecesores.get(vecino) is None and vecino != origen:
                predecesores[vecino] = actual
                cola.encolar(vecino)
                
    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""
    # Parche 3: Validación exacta de destinos no alcanzados y ciclo while seguro[cite: 3]
    if predecesores.get(destino) is None and origen != destino:
        return []
    
    camino = []
    actual = destino
    
    while actual is not None:
        if actual in camino:
            raise ValueError("Se detectó un ciclo en el diccionario de predecesores")
            
        camino.append(actual)
        
        if actual == origen:
            break
            
        actual = predecesores.get(actual)
    
    # Invertimos la lista porque la armamos de destino a origen
    camino.reverse()
    return camino


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""
    # Parche 2: Validar ambos nodos y apoyarse limpiamente en las funciones ya creadas[cite: 3]
    if origen not in grafo:
        raise KeyError("El nodo origen no se encuentra en el grafo")
    if destino not in grafo and not any(destino in vecinos for vecinos in grafo.values()):
        raise KeyError("El nodo destino no se encuentra en el grafo")
        
    predecesores = bfs_predecesores(grafo, origen)
    return reconstruir_camino(predecesores, origen, destino)


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""
    if origen not in grafo:
        raise KeyError("El nodo origen no se encuentra en el grafo")
    nodos_totales = set(grafo.keys())
    
    for vecinos in grafo.values():
        for arista in vecinos:
            if not isinstance(arista, (tuple, list)) or len(arista) != 2:
                raise ValueError("La arista debe tener exactamente dos elementos")
            
            vecino, peso = arista
            
            # Parche 1: Validación de string para el vecino y mensajes de error exactos[cite: 3]
            if type(vecino) is not str:
                raise TypeError("El vecino debe ser de tipo str")
            
            if type(peso) is not int:
                raise TypeError("Error: El peso es inválido, se esperaba un entero 0 o 1")
                
            if peso not in (0, 1):
                raise ValueError("El peso debe ser 0 o 1")
                
            nodos_totales.add(vecino)

    distancias = {}
    predecesores = {}
    for nodo in nodos_totales:
        distancias[nodo] = float('inf')
        predecesores[nodo] = None
        
    distancias[origen] = 0.0
    deque = DequeLigada()
    deque.agregar_inicio(origen)

    while not deque.esta_vacia():
        actual = deque.quitar_inicio()
        
        for vecino, peso in grafo.get(actual, []):
            nueva_distancia = distancias[actual] + peso
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = actual
                
                if peso == 0:
                    deque.agregar_inicio(vecino)
                elif peso == 1: 
                    deque.agregar_final(vecino)
                    
    return distancias, predecesores


def camino_cero_uno(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str
) -> tuple[float, list[str]]:
    """Devuelve el costo y un camino mínimo 0-1; ``(inf, [])`` si no existe."""
    distancias, predecesores = cero_uno_bfs(grafo, origen)
    costo = distancias.get(destino, float('inf'))
    if destino not in distancias:
        raise KeyError("El nodo destino no se encuentra en el grafo")
    if costo == float('inf'):
        return (float('inf'), [])
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino


__all__ = [
    "NodoSimple",
    "NodoDoble",
    "ColaLigada",
    "DequeLigada",
    "bfs_predecesores",
    "reconstruir_camino",
    "bfs_camino",
    "cero_uno_bfs",
    "camino_cero_uno",
]