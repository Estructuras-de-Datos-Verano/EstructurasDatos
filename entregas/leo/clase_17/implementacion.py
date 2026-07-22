"""Punto de partida de la Clase 17.

Completa las operaciones sin cambiar sus nombres ni sus firmas públicas. No
uses ``collections.deque`` ni un heap: la finalidad es construir las
estructuras auxiliares que necesitan BFS y 0-1 BFS.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from math import dist
from typing import Generic, TypeVar

from numpy import inf
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
        nuevo = NodoSimple(valor)
        if self._tamano == 0:
            self._frente = nuevo
            self._final = nuevo
        else:
            (self._final).siguiente = nuevo
            self._final = (self._final).siguiente
        self._tamano += 1
            

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""

        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        else: 
            valor = (self._frente).valor
            self._frente = (self._frente).siguiente
            if self._frente is None:
                self._final = None
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""

        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        else:
            return (self._frente).valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""

        if self._tamano == 0:
            return True
        else:
            return False

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

        nuevo = NodoDoble(valor)
        if self._tamano == 0:
            self._inicio = nuevo
            self._final = nuevo
        else:
            (self._inicio).anterior = nuevo
            (nuevo).siguiente = self._inicio
            self._inicio = nuevo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""

        nuevo = NodoDoble(valor)
        if self._tamano == 0:
            self._inicio = nuevo
            self._final = nuevo
        else:
            (self._final).siguiente = nuevo
            ((self._final).siguiente).anterior = self._final
            self._final = (self._final).siguiente
        self._tamano += 1

    def quitar_inicio(self) -> T:
        """Retira y devuelve el inicio; lanza IndexError si está vacía."""

        if self._tamano == 0:
            raise IndexError("El deque está vacío")
        else:
            nodo = self._inicio
            valor = nodo.valor
            self._inicio = nodo.siguiente
            if self._inicio is not None:
                (self._inicio).anterior = None
            else:
                self._final = None

            nodo.siguiente = None
            nodo.anterior = None
            self._tamano -= 1
            return valor

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""

        if self._tamano == 0:
            raise IndexError("El deque está vacío")
        else:
            nodo = self._final
            valor = nodo.valor
            self._final = nodo.anterior
            if self._final is not None:
                (self._final).siguiente = None
            else:
                self._inicio = None

            nodo.anterior = None
            nodo.siguiente = None
            self._tamano -= 1
            return valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("El deque está vacío")
        return (self._inicio).valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("El deque está vacío")
        return (self._final).valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""

        if self._tamano == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        return self._tamano


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Devuelve la tabla de predecesores de un BFS desde ``origen``."""

    if not isinstance(grafo, dict):
        raise TypeError("El grafo debe ser un diccionario")
    if not isinstance(origen, str):
        raise TypeError("El origen debe ser un string")
    if origen not in grafo.keys():
        raise KeyError("El origen no está en el grafo")
    for secuencia in grafo.values():
        if not isinstance(secuencia, (list, tuple)):
            raise TypeError("Los valores del grafo deben ser secuencias")
        for vertice in secuencia:
            if not isinstance(vertice, str):
                raise TypeError("Los vértices deben ser strings")
    
    cola = ColaLigada()
    cola.encolar(origen)
    predecesores = {origen: None}

    while not cola.esta_vacia():
        actual = cola.desencolar()
        for vecino in grafo.get(actual, []):
            if vecino not in predecesores:
                predecesores[vecino] = actual
                cola.encolar(vecino)

    for v in grafo:
        if v not in predecesores:
            predecesores[v] = None
    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""

    if origen not in predecesores:
        raise ValueError("El origen no está en la tabla de predecesores")
    if destino not in predecesores:
        raise ValueError("El destino no está en la tabla de predecesores")
    camino = []
    visitados = set()
    actual = destino
    while actual is not None:
        if actual in visitados:
            raise ValueError("Se ha llegado a un ciclo en la tabla de predecesores")
        visitados.add(actual)
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    if camino[0] != origen:
        return []
    return camino 


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""

    vertices = set(grafo.keys())
    for vecinos in grafo.values():
        for vecino in vecinos:
            vertices.add(vecino)
    if origen not in vertices:
        raise KeyError("El origen no está en el grafo")
    if destino not in vertices:
        raise KeyError("El destino no está en el grafo")
    
    predecesores = bfs_predecesores(grafo, origen)
    if destino not in predecesores:
        return []
    return reconstruir_camino(predecesores, origen, destino)


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""

    if not isinstance(grafo, dict):
        raise TypeError("El grafo debe ser un diccionario")
    if not isinstance(origen, str):
        raise TypeError("El origen debe ser un string")
    if origen not in grafo.keys():
        raise KeyError("El origen no está en el grafo")
    for secuencia in grafo.values():
        if not isinstance(secuencia, (list, tuple)):
            raise TypeError("Los valores del grafo deben ser secuencias")
        for vertice in secuencia:
            if not isinstance(vertice, tuple):
                raise TypeError("Los vecinos deben ser tuplas")
            if not len(vertice) == 2:
                raise ValueError("Cada tupla debe ser par")
            if type(vertice[1]) is not int:
                raise TypeError("Los pesos deben ser enteros")
            if vertice[1] not in (0, 1):
                raise ValueError("Los pesos deben ser 0 o 1")
            if not isinstance(vertice[0], str):
                raise TypeError("Los vecinos deben ser strings")

    vertices = set(grafo.keys())
    predecesores = {v: None for v in vertices}
    for aristas in grafo.values():
        for vecino, _ in aristas:
            vertices.add(vecino)
    distancias = {v: inf for v in vertices}
    predecesores = {v: None for v in vertices}
    distancias[origen] = 0
    dq = DequeLigada[str]()
    dq.agregar_inicio(origen)

    while not dq.esta_vacia():
        actual = dq.quitar_inicio()
        for vecino, peso in grafo.get(actual, []):
            nueva = distancias[actual] + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                predecesores[vecino] = actual
                if peso == 0:
                    dq.agregar_inicio(vecino)
                else:
                    dq.agregar_final(vecino)
    return distancias, predecesores


def camino_cero_uno(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str
) -> tuple[float, list[str]]:
    """Devuelve el costo y un camino mínimo 0-1; ``(inf, [])`` si no existe."""

    vertices = set(grafo.keys())

    for vecinos in grafo.values():
        for vecino, _ in vecinos:
            vertices.add(vecino)
    vertices = set(grafo)
    distancias = {v: inf for v in vertices}
    predecesores = {v: None for v in vertices}
    distancias[origen] = 0

    if destino not in vertices:
        raise KeyError("El destino no está en el grafo")

    if destino not in vertices:
        raise KeyError("El destino no está en el grafo")
    
    distancias, predecesores = cero_uno_bfs(grafo, origen)
    if distancias[destino] == inf:
        return inf, []
    camino = reconstruir_camino(predecesores, origen, destino)
    return distancias[destino], camino

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
