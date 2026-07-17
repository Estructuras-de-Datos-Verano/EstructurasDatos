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
        if self.esta_vacia(): 
            self._frente = nuevo
        else: 
            self._final.siguiente = nuevo
        self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("La cola está vacía")
        retirado = self._frente
        valor = retirado.valor
        self._frente = self._frente.siguiente
        if self._frente is None: 
            self._final = None
        retirado.siguiente = None
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("La cola está vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._tamano


class DequeLigada(Generic[T]):
    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
        nuevo = NodoDoble(valor)
        if self.esta_vacia(): 
            self._inicio = self._final = nuevo
        else:
            nuevo.siguiente = self._inicio
            self._inicio.anterior = nuevo
            self._inicio = nuevo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        nuevo = NodoDoble(valor)
        if self.esta_vacia(): 
            self._inicio = self._final = nuevo
        else:
            nuevo.anterior = self._final
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def quitar_inicio(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("El deque está vacío")
        retirado = self._inicio
        valor = retirado.valor
        self._inicio = self._inicio.siguiente
        if self._inicio is None: 
            self._final = None
        else: 
            self._inicio.anterior = None
        retirado.siguiente = None  # Desconectar el nodo retirado
        self._tamano -= 1
        return valor

    def quitar_final(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("El deque está vacío")
        retirado = self._final
        valor = retirado.valor
        self._final = self._final.anterior
        if self._final is None: 
            self._inicio = None
        else: 
            self._final.siguiente = None
        retirado.anterior = None  # Desconectar el nodo retirado
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("El deque está vacío")
        return self._inicio.valor

    def ultimo(self) -> T:
        if self.esta_vacia(): 
            raise IndexError("El deque está vacío")
        return self._final.valor

    def esta_vacia(self) -> bool:
        return self._inicio is None

    def __len__(self) -> int:
        return self._tamano


def _normalizar(grafo: Mapping[str, Sequence[str]]) -> dict[str, list[str]]:
    norm = {}
    for nodo, vecinos in grafo.items():
        if nodo not in norm: 
            norm[nodo] = []
        for v in vecinos:
            if v not in norm: 
                norm[v] = []
            norm[nodo].append(v)
    return norm


def bfs_predecesores(grafo: Mapping[str, Sequence[str]], origen: str) -> dict[str, str | None]:
    if origen not in grafo: 
        raise KeyError("origen")
    
    grafo_norm = _normalizar(grafo)
    pred = {n: None for n in grafo_norm}
    visitados = {origen}
    
    cola = ColaLigada()
    cola.encolar(origen)
    
    while not cola.esta_vacia():
        u = cola.desencolar()
        for v in grafo_norm[u]:
            if v not in visitados:
                visitados.add(v)
                pred[v] = u
                cola.encolar(v)
    return pred


def reconstruir_camino(pred: Mapping[str, str | None], origen: str, destino: str) -> list[str]:
    if destino not in pred: 
        raise KeyError("destino")
    if destino == origen: 
        return [origen]
    
    camino = []
    curr = destino
    vistos = set()
    
    while curr is not None:
        if curr in vistos: 
            raise ValueError("ciclo")
        vistos.add(curr)
        camino.append(curr)
        if curr == origen: 
            return list(reversed(camino))
        curr = pred.get(curr)
        
    return []


def bfs_camino(grafo: Mapping[str, Sequence[str]], origen: str, destino: str) -> list[str]:
    pred = bfs_predecesores(grafo, origen)
    return reconstruir_camino(pred, origen, destino)


def cero_uno_bfs(grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str) -> tuple[dict[str, float], dict[str, str | None]]:
    norm = {}
    for u, aristas in grafo.items():
        if u not in norm: 
            norm[u] = []
        for arista in aristas:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise ValueError("dos elementos")
            
            v, w = arista
            
            if isinstance(w, bool) or not isinstance(w, int): 
                raise TypeError("entero 0 o 1")
            if w not in (0, 1): 
                raise ValueError("0 o 1")
            if not isinstance(v, str): 
                raise TypeError("vecino")
                
            norm[u].append((v, w))
            if v not in norm: 
                norm[v] = []
                
    if origen not in norm: 
        raise KeyError("origen")
    
    dist = {n: float('inf') for n in norm}
    pred = {n: None for n in norm}
    dist[origen] = 0
    
    dq = DequeLigada()
    dq.agregar_inicio(origen)
    
    while not dq.esta_vacia():
        u = dq.quitar_inicio()
        for v, w in norm[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                if w == 0: 
                    dq.agregar_inicio(v)
                else: 
                    dq.agregar_final(v)
                    
    return dist, pred


def camino_cero_uno(grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str) -> tuple[float, list[str]]:
    dist, pred = cero_uno_bfs(grafo, origen)
    if destino not in dist: 
        raise KeyError("destino")
    camino = reconstruir_camino(pred, origen, destino)
    return dist[destino], camino