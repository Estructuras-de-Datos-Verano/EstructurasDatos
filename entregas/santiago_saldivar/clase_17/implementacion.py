from __future__ import annotations

import math
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
        nuevo = NodoSimple(valor)
        if self.esta_vacia():
            self._frente = nuevo
            self._final = nuevo
        else:
            assert self._final is not None
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía.")
        
        assert self._frente is not None
        nodo_retirado = self._frente
        valor = nodo_retirado.valor
        self._frente = nodo_retirado.siguiente
        
        if self._frente is None:
            self._final = None
            
        # Desconectar el nodo para no conservar extremos
        nodo_retirado.siguiente = None
            
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía.")
        assert self._frente is not None
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
        nuevo = NodoDoble(valor)
        if self.esta_vacia():
            self._inicio = nuevo
            self._final = nuevo
        else:
            assert self._inicio is not None
            nuevo.siguiente = self._inicio
            self._inicio.anterior = nuevo
            self._inicio = nuevo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""
        nuevo = NodoDoble(valor)
        if self.esta_vacia():
            self._inicio = nuevo
            self._final = nuevo
        else:
            assert self._final is not None
            nuevo.anterior = self._final
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def quitar_inicio(self) -> T:
        """Retira y devuelve el inicio; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque está vacía.")
        
        assert self._inicio is not None
        nodo_retirado = self._inicio
        valor = nodo_retirado.valor
        self._inicio = nodo_retirado.siguiente
        
        if self._inicio is None:
            self._final = None
        else:
            self._inicio.anterior = None
            
        # Desconectar por completo el nodo removido de la estructura
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
            
        self._tamano -= 1
        return valor

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque está vacía.")
        
        assert self._final is not None
        nodo_retirado = self._final
        valor = nodo_retirado.valor
        self._final = nodo_retirado.anterior
        
        if self._final is None:
            self._inicio = None
        else:
            self._final.siguiente = None
            
        # Desconectar por completo el nodo removido de la estructura
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
            
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque está vacía.")
        assert self._inicio is not None
        return self._inicio.valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo; lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("La deque está vacía.")
        assert self._final is not None
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
    # Encontrar todos los nodos del grafo para validar y poblar adecuadamente
    todos_los_nodos = set(grafo.keys())
    for u in grafo:
        for v in grafo[u]:
            todos_los_nodos.add(v)

    if origen not in todos_los_nodos:
        raise KeyError("El origen no pertenece al grafo.")

    predecesores: dict[str, str | None] = {v: None for v in todos_los_nodos}
    visitados = {origen}
    
    cola = ColaLigada[str]()
    cola.encolar(origen)

    while not cola.esta_vacia():
        actual = cola.desencolar()
        
        if actual not in grafo:
            continue
            
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                predecesores[vecino] = actual
                cola.encolar(vecino)

    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""
    if destino not in predecesores:
        return []

    camino = []
    nodo_actual = destino
    visitados = set()

    while nodo_actual is not None:
        if nodo_actual in visitados:
            raise ValueError("Se detectó un ciclo en el mapa de predecesores.")
        
        visitados.add(nodo_actual)
        camino.append(nodo_actual)
        
        if nodo_actual == origen:
            break
            
        nodo_actual = predecesores[nodo_actual]

    if not camino or camino[-1] != origen:
        return []

    return camino[::-1]


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""
    todos_los_nodos = set(grafo.keys())
    for u in grafo:
        for v in grafo[u]:
            todos_los_nodos.add(v)

    if origen not in todos_los_nodos:
        raise KeyError("El origen no pertenece al grafo.")
    if destino not in todos_los_nodos:
        raise KeyError("El destino no pertenece al grafo.")

    if origen == destino:
        return [origen]

    predecesores = bfs_predecesores(grafo, origen)
    return reconstruir_camino(predecesores, origen, destino)


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""
    todos_los_nodos = set(grafo.keys())
    
    # Validaciones rigurosas de la estructura del grafo, tipos y pesos
    for u in grafo:
        for arista in grafo[u]:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise ValueError("Cada arista debe constar de dos elementos (vecino, peso).")
            
            vecino, peso = arista
            
            if not isinstance(vecino, str):
                raise TypeError("El vecino debe ser de tipo string.")
                
            # Validar que sea un entero estricto de valor 0 o 1 (excluyendo booleanos)
            if isinstance(peso, bool) or not isinstance(peso, int):
                raise TypeError("El peso debe ser un entero 0 o 1.")
                
            if peso not in (0, 1):
                raise ValueError("El peso debe ser exclusivamente 0 o 1.")
                
            todos_los_nodos.add(vecino)

    if origen not in todos_los_nodos:
        raise KeyError("El origen no pertenece al grafo.")

    distancias = {v: float("inf") for v in todos_los_nodos}
    predecesores: dict[str, str | None] = {v: None for v in todos_los_nodos}

    distancias[origen] = 0.0

    deque = DequeLigada[str]()
    deque.agregar_inicio(origen)

    while not deque.esta_vacia():
        actual = deque.quitar_inicio()

        if actual not in grafo:
            continue

        for vecino, peso in grafo[actual]:
            nueva_dist = distancias[actual] + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = actual
                
                if peso == 0:
                    deque.agregar_inicio(vecino)
                else:
                    deque.agregar_final(vecino)

    return distancias, predecesores


def camino_cero_uno(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str
) -> tuple[float, list[str]]:
    """Devuelve el costo y un camino mínimo 0-1; ``(inf, [])`` si no existe."""
    # Validamos primero si el origen y destino existen dentro del ecosistema del grafo
    todos_los_nodos = set(grafo.keys())
    for u in grafo:
        for arista in grafo[u]:
            if isinstance(arista, tuple) and len(arista) > 0:
                todos_los_nodos.add(arista[0])

    if origen not in todos_los_nodos:
        raise KeyError("El origen no pertenece al grafo.")
    if destino not in todos_los_nodos:
        raise KeyError("El destino no pertenece al grafo.")

    distancias, predecesores = cero_uno_bfs(grafo, origen)

    if destino not in distancias or math.isinf(distancias[destino]):
        return float("inf"), []

    camino = reconstruir_camino(predecesores, origen, destino)
    return distancias[destino], camino