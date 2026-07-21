"""Implementación de listas ligadas, BFS y 0-1 BFS."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from math import inf
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
        if self._tamano == 0:
            self._frente = nuevo
            self._final = nuevo
        else:
            assert self._final is not None
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""
        if self._tamano == 0:
            raise IndexError("La cola está vacía.")
        
        assert self._frente is not None
        nodo_retirado = self._frente
        valor = nodo_retirado.valor
        
        self._frente = nodo_retirado.siguiente
        nodo_retirado.siguiente = None  # Evitar referencias residuales
        self._tamano -= 1
        
        if self._tamano == 0:
            self._final = None
            
        return valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""
        if self._tamano == 0:
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
        if self._tamano == 0:
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
        if self._tamano == 0:
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
        if self._tamano == 0:
            raise IndexError("La deque está vacía.")
        assert self._inicio is not None
        nodo_retirado = self._inicio
        valor = nodo_retirado.valor
        
        self._inicio = nodo_retirado.siguiente
        if self._inicio is not None:
            self._inicio.anterior = None
        
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        self._tamano -= 1
        
        if self._tamano == 0:
            self._final = None
            
        return valor

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía.")
        assert self._final is not None
        nodo_retirado = self._final
        valor = nodo_retirado.valor
        
        self._final = nodo_retirado.anterior
        if self._final is not None:
            self._final.siguiente = None
            
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        self._tamano -= 1
        
        if self._tamano == 0:
            self._inicio = None
            
        return valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía.")
        assert self._inicio is not None
        return self._inicio.valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía.")
        assert self._final is not None
        return self._final.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


def _normalizar_grafo_simple(
    grafo: Mapping[str, Sequence[str]]
) -> dict[str, list[str]]:
    """Copia defensivamente e incluye vecinos implícitos."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser una estructura Mapping.")
        
    normalizado: dict[str, list[str]] = {}
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Las claves del grafo deben ser strings.")
        if not isinstance(vecinos, Sequence) or isinstance(vecinos, (str, bytes)):
            raise TypeError("Los vecinos deben ser una secuencia (no string).")
        for v in vecinos:
            if not isinstance(v, str):
                raise TypeError("Los vecinos del grafo deben ser strings.")
        normalizado[nodo] = list(vecinos)

    # Añadir vecinos implícitos que no están como claves
    for vecinos in list(normalizado.values()):
        for v in vecinos:
            if v not in normalizado:
                normalizado[v] = []
                
    return normalizado


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Devuelve la tabla de predecesores de un BFS desde ``origen``."""
    g_norm = _normalizar_grafo_simple(grafo)
    if origen not in g_norm:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")

    predecesores: dict[str, str | None] = {nodo: None for nodo in g_norm}
    descubiertos = {origen}
    
    cola = ColaLigada[str]()
    cola.encolar(origen)

    while not cola.esta_vacia():
        actual = cola.desencolar()
        for vecino in g_norm[actual]:
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                predecesores[vecino] = actual
                cola.encolar(vecino)
                
    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""
    if origen not in predecesores:
        raise KeyError(f"El origen '{origen}' no está en la tabla de predecesores.")
    if destino not in predecesores:
        raise KeyError(f"El destino '{destino}' no está en la tabla de predecesores.")

    if origen == destino:
        return [origen]

    camino = []
    actual = destino
    visitados_camino = set()

    while actual is not None:
        if actual in visitados_camino:
            raise ValueError("Se detectó un ciclo en la tabla de predecesores.")
        visitados_camino.add(actual)
        camino.append(actual)
        if actual == origen:
            camino.reverse()
            return camino
        actual = predecesores[actual]

    return []


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""
    predecesores = bfs_predecesores(grafo, origen)
    if destino not in predecesores:
        raise KeyError(f"El nodo destino '{destino}' no pertenece al grafo.")
    return reconstruir_camino(predecesores, origen, destino)


def _normalizar_grafo_01(
    grafo: Mapping[str, Sequence[tuple[str, int]]]
) -> dict[str, list[tuple[str, int]]]:
    """Copia defensivamente un grafo ponderado con aristas 0-1."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser una estructura Mapping.")
        
    normalizado: dict[str, list[tuple[str, int]]] = {}
    for nodo, aristas in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Las claves del grafo deben ser strings.")
        if not isinstance(aristas, Sequence) or isinstance(aristas, (str, bytes)):
            raise TypeError("Las adyacencias deben ser una secuencia.")
            
        lista_aristas = []
        for arista in aristas:
            if not isinstance(arista, tuple):
                raise TypeError("Cada arista debe ser una tupla.")
            if len(arista) != 2:
                raise ValueError("Cada arista debe ser una tupla de dos elementos (vecino, peso).")
            
            vecino, peso = arista
            if not isinstance(vecino, str):
                raise TypeError("El vecino debe ser de tipo str.")
            # Rechazar booleanos explícitamente ya que son subclase de int
            if isinstance(peso, bool) or not isinstance(peso, int):
                raise TypeError("El peso debe ser un entero 0 o 1.")
            if peso not in (0, 1):
                raise ValueError("El peso de la arista debe ser estrictamente 0 o 1.")
                
            lista_aristas.append((vecino, peso))
        normalizado[nodo] = lista_aristas

    # Vecinos implícitos
    for aristas in list(normalizado.values()):
        for vecino, _ in aristas:
            if vecino not in normalizado:
                normalizado[vecino] = []
                
    return normalizado


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""
    g_norm = _normalizar_grafo_01(grafo)
    if origen not in g_norm:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")

    distancias: dict[str, float] = {nodo: inf for nodo in g_norm}
    predecesores: dict[str, str | None] = {nodo: None for nodo in g_norm}

    distancias[origen] = 0.0
    deque = DequeLigada[str]()
    deque.agregar_inicio(origen)

    while not deque.esta_vacia():
        actual = deque.quitar_inicio()
        dist_actual = distancias[actual]

        for vecino, peso in g_norm[actual]:
            candidato = dist_actual + peso
            if candidato < distancias[vecino]:
                distancias[vecino] = candidato
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
    distancias, predecesores = cero_uno_bfs(grafo, origen)
    if destino not in distancias:
        raise KeyError(f"El destino '{destino}' no pertenece al grafo.")
        
    costo = distancias[destino]
    if costo == inf:
        return inf, []
        
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino

