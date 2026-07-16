from __future__ import annotations
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass(slots=True)
class NodoSimple(Generic[T]):
    valor: T
    siguiente: NodoSimple[T] | None = None

@dataclass(slots=True)
class NodoDoble(Generic[T]):
    valor: T
    anterior: NodoDoble[T] | None = None
    siguiente: NodoDoble[T] | None = None

class ColaLigada(Generic[T]):
    def __init__(self) -> None:
        self._frente: NodoSimple[T] | None = None
        self._final: NodoSimple[T] | None = None
        self._tamano = 0

    def encolar(self, valor: T) -> None:
        nuevo = NodoSimple(valor)
        if self._tamano == 0:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        nodo = self._frente
        self._frente = nodo.siguiente
        self._tamano -= 1
        if self._tamano == 0:
            self._final = None
        nodo.siguiente = None
        return nodo.valor

    def primero(self) -> T:
        if self._tamano == 0:
            raise IndexError("La cola está vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano

class DequeLigada(Generic[T]):
    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
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
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        nodo = self._inicio
        self._inicio = nodo.siguiente
        self._tamano -= 1
        if self._tamano == 0:
            self._final = None
        else:
            self._inicio.anterior = None
        nodo.siguiente = None
        nodo.anterior = None
        return nodo.valor

    def quitar_final(self) -> T:
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        nodo = self._final
        self._final = nodo.anterior
        self._tamano -= 1
        if self._tamano == 0:
            self._inicio = None
        else:
            self._final.siguiente = None
        nodo.siguiente = None
        nodo.anterior = None
        return nodo.valor

    def primero(self) -> T:
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        return self._inicio.valor

    def ultimo(self) -> T:
        if self._tamano == 0:
            raise IndexError("La deque está vacía")
        return self._final.valor

    def esta_vacia(self) -> bool:
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano

def _normalizar_grafo_simple(grafo: Mapping[str, Sequence[str]]) -> dict[str, list[str]]:
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
    normalizado = {}
    for u, vecinos in grafo.items():
        if not isinstance(u, str) or isinstance(u, bool):
            raise TypeError("Las claves del grafo deben ser strings")
        if not isinstance(vecinos, Sequence):
            raise TypeError("La lista de adyacencia debe ser una secuencia")
        for v in vecinos:
            if not isinstance(v, str) or isinstance(v, bool):
                raise TypeError("Los vecinos deben ser strings")
        normalizado[u] = list(vecinos)
    for u in list(normalizado.keys()):
        for v in normalizado[u]:
            if v not in normalizado:
                normalizado[v] = []
    return normalizado



def bfs_predecesores(grafo: Mapping[str, Sequence[str]], origen: str) -> dict[str, str | None]:
    g = _normalizar_grafo_simple(grafo)
    if origen not in g:
        raise KeyError(f"El origen {origen} no pertenece al grafo")
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

def reconstruir_camino(predecesores: Mapping[str, str | None], origen: str, destino: str) -> list[str]:
    if origen not in predecesores or destino not in predecesores:
        raise KeyError("Origen o destino no se encuentran en la tabla de predecesores")
    if origen == destino:
        return [origen]
    camino = []
    actual = destino
    visitados = set()
    while actual is not None:
        if actual in visitados:
            raise ValueError("Se detectó un ciclo en la tabla de predecesores")
        visitados.add(actual)
        camino.append(actual)
        if actual == origen:
            camino.reverse()
            return camino
        actual = predecesores[actual]
    return []

def bfs_camino(grafo: Mapping[str, Sequence[str]], origen: str, destino: str) -> list[str]:
    pred = bfs_predecesores(grafo, origen)
    return reconstruir_camino(pred, origen, destino)

def _normalizar_grafo_pesado(grafo: Mapping[str, Sequence[tuple[str, int]]]) -> dict[str, list[tuple[str, int]]]:
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
    normalizado = {}
    for u, vecinos in grafo.items():
        if not isinstance(u, str) or isinstance(u, bool):
            raise TypeError("Las claves del grafo deben ser strings")
        if not isinstance(vecinos, Sequence):
            raise TypeError("La lista de adyacencia debe ser una secuencia")
        lista_vecinos = []
        for elem in vecinos:
       
            if not isinstance(elem, tuple) or len(elem) != 2:
                raise ValueError("Las aristas deben ser tuplas de dos elementos (vecino, peso)")
            v, peso = elem
            if not isinstance(v, str) or isinstance(v, bool):
    
                raise TypeError("El nodo vecino debe ser un string")
            
            
            if isinstance(peso, bool) or not isinstance(peso, int):
                raise TypeError("El peso debe ser un entero 0 o 1")
            if peso not in (0, 1):
                raise ValueError("El peso debe ser un entero 0 o 1")
            lista_vecinos.append((v, peso))
        normalizado[u] = lista_vecinos
    for u in list(normalizado.keys()):
        for v, _ in normalizado[u]:
            if v not in normalizado:
                normalizado[v] = []
    return normalizado

def cero_uno_bfs(grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str) -> tuple[dict[str, float], dict[str, str | None]]:
    g = _normalizar_grafo_pesado(grafo)
    if origen not in g:
        raise KeyError(f"El origen {origen} no está en el grafo")
    distancias = {nodo: float("inf") for nodo in g}
    predecesores = {nodo: None for nodo in g}
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

def camino_cero_uno(grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str) -> tuple[float, list[str]]:
    try:
        g = _normalizar_grafo_pesado(grafo)
    except (TypeError, ValueError):
        raise
    if origen not in g or destino not in g:
        raise KeyError("Origen o destino fuera del grafo")
    distancias, predecesores = cero_uno_bfs(grafo, origen)
    costo = distancias[destino]
    if costo == float("inf"):
        return float("inf"), []
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino