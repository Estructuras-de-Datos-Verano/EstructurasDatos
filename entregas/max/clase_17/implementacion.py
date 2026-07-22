from __future__ import annotations
from collections.abc import Mapping, Sequence


class NodoSimple:
    def __init__(self, valor: str):
        self.valor = valor
        self.siguiente: NodoSimple | None = None

class ColaLigada:
    def __init__(self):
        self._frente: NodoSimple | None = None
        self._final: NodoSimple | None = None
        self._tamano: int = 0
        
    def encolar(self, valor: str) -> None:
        nuevo = NodoSimple(valor)
        if self._tamano == 0:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1
        
    def desencolar(self) -> str:
        if self._tamano == 0:
            raise IndexError("La cola esta vacia")
        nodo_retirado = self._frente
        valor = nodo_retirado.valor
        self._frente = self._frente.siguiente
        self._tamano -= 1
        if self._tamano == 0:
            self._final = None
        nodo_retirado.siguiente = None
        return valor
        
    def esta_vacia(self) -> bool:
        return self._tamano == 0



def _normalizar_grafo_bfs(grafo: Mapping[str, Sequence[str]]) -> dict[str, list[str]]:
    grafo_normalizado = {}
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("los nodos deben ser str")
        grafo_normalizado[nodo] = list(vecinos)
        for vecino in vecinos:
            if vecino not in grafo_normalizado and vecino not in grafo:
                grafo_normalizado[vecino] = []
    return grafo_normalizado



def bfs_predecesores(grafo: Mapping[str, Sequence[str]], origen: str) -> dict[str, str | None]:
    grafo_norm = _normalizar_grafo_bfs(grafo)
    if origen not in grafo_norm:
        raise KeyError(f"El origen {origen} no esta en el grafo")
    predecesores = {origen: None}
    cola = ColaLigada()
    cola.encolar(origen)
    while not cola.esta_vacia():
        actual = cola.desencolar()
        for vecino in grafo_norm.get(actual, []):
            if vecino not in predecesores:
                predecesores[vecino] = actual
                cola.encolar(vecino)           
    return predecesores


def reconstruir_camino(predecesores: Mapping[str, str | None], origen: str, destino: str) -> list[str]:
    if origen not in predecesores or destino not in predecesores:
        if origen != destino:
            raise KeyError("origen o destino ausentes")  
    if origen == destino:
        return [origen]
    camino = []
    actual = destino
    visitados = set()
    while actual is not None:
        if actual in visitados:
            raise ValueError("hay un ciclo en el diccionario")
        visitados.add(actual)
        camino.append(actual)     
        if actual == origen:
            camino.reverse()
            return camino     
        actual = predecesores.get(actual, None)
    return []


def bfs_camino(grafo: Mapping[str, Sequence[str]], origen: str, destino: str) -> list[str]:
    grafo_norm = _normalizar_grafo_bfs(grafo)
    if origen not in grafo_norm or (destino not in grafo_norm and origen != destino):
        raise KeyError("origen o destino no validos")
    preds = bfs_predecesores(grafo_norm, origen)
    if destino not in preds and origen != destino:
        return []
    return reconstruir_camino(preds, origen, destino)