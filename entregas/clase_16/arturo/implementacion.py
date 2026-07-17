import heapq
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]

def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    normalizado = {}
    for origen, adyacentes in grafo.items():
        if origen not in normalizado:
            normalizado[origen] = []
        for arista in adyacentes:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("La arista debe ser un par")
            
            destino, peso = arista
            
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("El peso debe ser numérico")
            if not math.isfinite(peso):
                raise ValueError("El peso debe ser finito")
            if peso < 0:
                raise ValueError("Los pesos deben ser no negativos")
                
            normalizado[origen].append((destino, float(peso)))
            if destino not in normalizado:
                normalizado[destino] = []
    return normalizado

def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    grafo_normalizado = _normalizar_grafo(grafo)
    
    if origen not in grafo_normalizado:
        raise KeyError("origen")

    distancias = {nodo: float("inf") for nodo in grafo_normalizado}
    predecesores = {nodo: None for nodo in grafo_normalizado}
    distancias[origen] = 0.0

    pendientes = [(0.0, origen)]

    while pendientes:
        distancia_extraida, actual = heapq.heappop(pendientes)

        if distancia_extraida != distancias[actual]:
            continue

        for vecino, peso in grafo_normalizado[actual]:
            nueva_distancia = distancia_extraida + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (nueva_distancia, vecino))

    return distancias, predecesores

def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    if destino not in predecesores:
        return []

    camino = []
    actual = destino
    vistos = set()

    while actual is not None:
        if actual in vistos:
            raise ValueError("ciclo")
        vistos.add(actual)
        camino.append(actual)
        
        if actual == origen:
            return list(reversed(camino))
            
        actual = predecesores.get(actual)

    return []

def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    distancias, predecesores = dijkstra(grafo, origen)
    camino = reconstruir_camino(predecesores, origen, destino)
    distancia_total = distancias.get(destino, float("inf"))

    return distancia_total, camino