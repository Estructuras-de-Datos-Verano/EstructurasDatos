from __future__ import annotations
import heapq
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]

def dijkstra(grafo: GrafoPonderado, origen: str,) -> tuple[dict[str, float], dict[str, str | None]]:
    for secuencia in grafo.values():
        for value in secuencia:
            if value[1] < 0:
                raise ValueError("El peso debe de ser positivo.")
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    cola = [(0, origen)]
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if distancia_actual > distancias[nodo_actual]:
            pass
        for vecino, peso in grafo[nodo_actual]:
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
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    camino.reverse()
    if camino[0] == origen:
        return camino
    return []


def camino_minimo(grafo: GrafoPonderado, origen: str, destino: str,) -> tuple[float, list[str]]:
    distancias, predecesores = dijkstra(grafo, origen)
    costo = distancias.get(destino, float('inf'))
    if costo == float('inf'):
        return float('inf'), []
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino