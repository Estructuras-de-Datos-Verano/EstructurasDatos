"""Implementación de la Clase 17: Listas ligadas, BFS y 0-1 BFS."""

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
    """Cola FIFO (primero en entrar, primero en salir) con nodos simples."""

    def __init__(self) -> None:
        self._frente: NodoSimple[T] | None = None
        self._final: NodoSimple[T] | None = None
        self._tamano = 0

    def encolar(self, valor: T) -> None:
        """Agrega un valor al final."""
        nuevo = NodoSimple(valor)
        if self._tamano == 0:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        """Retira y devuelve el elemento del frente."""
        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        nodo_retirado = self._frente
        valor = nodo_retirado.valor
        self._frente = nodo_retirado.siguiente
        
        # Limpieza del nodo desconectado para evitar fugas de memoria
        nodo_retirado.siguiente = None 
        
        self._tamano -= 1
        if self._tamano == 0:
            self._final = None
        return valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo."""
        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        """Indica si la cola no tiene elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


class DequeLigada(Generic[T]):
    """Una cola doble que permite operar por ambos extremos."""

    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
        """Agrega un valor al principio."""
        nuevo = NodoDoble(valor)
        if self._tamano == 0:
            self._inicio = nuevo
            self._final = nuevo
        else:
            nuevo.siguiente = self._inicio
            self._inicio.anterior = nuevo
            self._inicio = nuevo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final."""
        nuevo = NodoDoble(valor)
        if self._tamano == 0:
            self._inicio = nuevo
            self._final = nuevo
        else:
            nuevo.anterior = self._final
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def quitar_inicio(self) -> T:
        """Retira y devuelve el elemento del inicio."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        nodo_retirado = self._inicio
        valor = nodo_retirado.valor
        self._inicio = nodo_retirado.siguiente
        self._tamano -= 1
        if self._tamano == 0:
            self._final = None
        else:
            self._inicio.anterior = None
            
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        return valor

    def quitar_final(self) -> T:
        """Retira y devuelve el elemento del final."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        nodo_retirado = self._final
        valor = nodo_retirado.valor
        self._final = nodo_retirado.anterior
        self._tamano -= 1
        if self._tamano == 0:
            self._inicio = None
        else:
            self._final.siguiente = None
            
        nodo_retirado.siguiente = None
        nodo_retirado.anterior = None
        return valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        return self._inicio.valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        return self._final.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


def _normalizar_grafo_bfs(grafo: Mapping[str, Sequence[str]]) -> dict[str, list[str]]:
    """Copia el grafo y añade vecinos implícitos sin alterar el original."""
    g_copia = {nodo: list(vecinos) for nodo, vecinos in grafo.items()}
    for vecinos in grafo.values():
        for v in vecinos:
            if v not in g_copia:
                g_copia[v] = []
    return g_copia


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Descubre el grafo por capas y registra de dónde vino cada nodo."""
    if origen not in grafo:
        raise KeyError("origen")
        
    g = _normalizar_grafo_bfs(grafo)
    predecesores = {nodo: None for nodo in g}
    descubiertos = {origen}
    
    cola = ColaLigada[str]()
    cola.encolar(origen)
    
    while not cola.esta_vacia():
        actual = cola.desencolar()
        for vecino in g[actual]:
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                predecesores[vecino] = actual
                cola.encolar(vecino)
                
    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Rastrea el camino hacia atrás desde el destino hasta el origen."""
    if origen not in predecesores:
        raise KeyError("origen")
    if destino not in predecesores:
        raise KeyError("destino")
        
    if origen == destino:
        return [origen]
        
    camino = []
    actual = destino
    visitados = set()
    
    while actual is not None:
        if actual in visitados:
            raise ValueError("ciclo")
        visitados.add(actual)
        camino.append(actual)
        if actual == origen:
            camino.reverse()
            return camino
        actual = predecesores[actual]
        
    return []


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Encuentra la ruta más corta contando el número de saltos."""
    if origen not in grafo:
        raise KeyError("origen")
        
    g = _normalizar_grafo_bfs(grafo)
    if destino not in g:
        raise KeyError("destino")
        
    pred = bfs_predecesores(grafo, origen)
    return reconstruir_camino(pred, origen, destino)


def _validar_y_normalizar_01(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> dict[str, list[tuple[str, int]]]:
    """Valida tipos, detecta booleanos tramposos y añade vecinos implícitos."""
    if origen not in grafo:
        raise KeyError("origen")
        
    g_copia = {}
    for nodo, aristas in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("nodo")
        g_copia[nodo] = []
        for edge in aristas:
            if not isinstance(edge, tuple) or len(edge) != 2:
                raise ValueError("dos elementos")
            vecino, peso = edge
            if not isinstance(vecino, str):
                raise TypeError("vecino")
            if type(peso) is bool:
                raise TypeError("entero 0 o 1")
            if not isinstance(peso, int):
                raise TypeError("entero 0 o 1")
            if peso not in (0, 1):
                raise ValueError("0 o 1")
            g_copia[nodo].append((vecino, peso))
            
    for aristas in list(g_copia.values()):
        for vecino, _ in aristas:
            if vecino not in g_copia:
                g_copia[vecino] = []
                
    return g_copia


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias óptimas cuando las aristas cuestan 0 o 1."""
    g = _validar_y_normalizar_01(grafo, origen)
    
    distancias: dict[str, float] = {nodo: inf for nodo in g}
    predecesores: dict[str, str | None] = {nodo: None for nodo in g}
    
    distancias[origen] = 0.0
    deque = DequeLigada[str]()
    deque.agregar_inicio(origen)
    
    while not deque.esta_vacia():
        actual = deque.quitar_inicio()
        
        for vecino, peso in g[actual]:
            candidato = distancias[actual] + peso
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
    """Devuelve el costo acumulado y la lista de nodos del camino mínimo."""
    g = _validar_y_normalizar_01(grafo, origen)
    if destino not in g:
        raise KeyError("destino")
        
    distancias, predecesores = cero_uno_bfs(grafo, origen)
    costo = distancias[destino]
    
    if costo == inf:
        return (inf, [])
        
    camino = reconstruir_camino(predecesores, origen, destino)
    return (costo, camino)


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