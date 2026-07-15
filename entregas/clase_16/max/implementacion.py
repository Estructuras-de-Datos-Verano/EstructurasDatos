from __future__ import annotations
import heapq
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    grafo_normalizado: dict[str, list[tuple[str, float]]] = {}
    for nodo, vecinos in grafo.items():
        lista_vecinos: list[tuple[str, float]] = []
        for item in vecinos:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Cada arista debe ser un par (vecino, peso).")
            vecino, peso = item
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("El peso de la arista debe ser un valor numérico.")
            if not math.isfinite(peso):
                raise ValueError("El peso debe ser un número real finito.")
            if peso < 0:
                raise ValueError("Los pesos de las aristas deben ser no negativos.")
            lista_vecinos.append((vecino, float(peso)))
        grafo_normalizado[nodo] = lista_vecinos
    return grafo_normalizado



def dijkstra(grafo: GrafoPonderado, origen: str,) -> tuple[dict[str, float], dict[str, str | None]]:
    grafo_normalizado = _normalizar_grafo(grafo)
    if origen not in grafo_normalizado:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
    for secuencia in grafo.values():
        for value in secuencia:
            if value[1] < 0:
                raise ValueError("El peso debe de ser positivo.")
    if origen not in grafo_normalizado:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
    distancias = {nodo: float('inf') for nodo in grafo_normalizado}
    predecesores = {nodo: None for nodo in grafo_normalizado}
    distancias[origen] = 0
    cola = [(0, origen)]
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if distancia_actual > distancias[nodo_actual]:
            pass
        for vecino, peso in grafo_normalizado.get(nodo_actual,[]):
            nueva_distancia = distancia_actual + peso
            if vecino not in distancias:
                distancias[vecino] = float('inf')
                predecesores[vecino] = None
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))
    return distancias, predecesores


def reconstruir_camino(predecesores: Mapping[str, str | None], origen: str, destino: str,) -> list[str]:
    if destino not in predecesores:
        return []
    camino = []
    nodo_actual = destino
    visitados = set()
    while nodo_actual is not None:
        if nodo_actual in visitados:
            raise ValueError("ciclo")
        visitados.add(nodo_actual)
        camino.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    camino.reverse()
    if camino[0] and camino == origen:
        return camino
    return camino


def camino_minimo(grafo: GrafoPonderado, origen: str, destino: str,) -> tuple[float, list[str]]:
    distancias, predecesores = dijkstra(grafo, origen)
    costo = distancias.get(destino, float('inf'))
    if costo == float('inf'):
        return float('inf'), []
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino