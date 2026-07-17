from __future__ import annotations

import heapq
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo sin compartir listas con la entrada."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser una estructura de tipo Mapping.")

    copia: dict[str, list[tuple[str, float]]] = {}
    
 
    for nodo in grafo:
        if isinstance(nodo, bool) or not isinstance(nodo, str):
            raise TypeError("Las claves del grafo (nodos) deben ser strings.")
        copia[nodo] = []

    
    for origen, vecinos in grafo.items():
        if not isinstance(vecinos, Sequence):
            raise TypeError("Los vecinos deben ser una secuencia.")
            
        for arista in vecinos:
            
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("Cada arista debe ser un par (destino, peso).")
                
            destino, peso = arista
            
            if isinstance(destino, bool) or not isinstance(destino, str):
                raise TypeError("Los destinos deben ser strings.")
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("Los pesos deben ser de tipo numérico.")
            
           
            if not math.isfinite(peso):
                raise ValueError("El peso debe ser un número finito (no inf ni nan).")
            if peso < 0:
                raise ValueError("Dijkstra no admite pesos no negativos.")
           
            if destino not in copia:
                copia[destino] = []
                
            copia[origen].append((destino, float(peso)))

    return copia


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias y predecesores desde un origen válido."""
    grafo_l = _normalizar_grafo(grafo)
    
    if origen not in grafo_l:
        raise KeyError(f"El nodo origen '{origen}' no existe en el grafo.")

    distancias = {nodo: float("inf") for nodo in grafo_l}
    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo_l}
    
    distancias[origen] = 0.0
    cola = [(0.0, origen)]

    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)

        if dist_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo_l[nodo_actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias, predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye un camino o devuelve una lista vacía si es inalcanzable."""
    if destino not in predecesores or origen not in predecesores:
        raise ValueError("Origen o destino ausentes del mapa de predecesores.")

    if origen == destino:
        return [origen]

    if predecesores[destino] is None:
        return []

    camino = []
    actual: str | None = destino
    visitados = set()

    while actual is not None:
        if actual in visitados:
            raise ValueError("Se detectó un ciclo en los predecesores.")
        visitados.add(actual)
        camino.append(actual)
        actual = predecesores[actual]

    camino.reverse()
    return camino if camino[0] == origen else []


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina cálculo y reconstrucción para un destino."""
    distancias, predecesores = dijkstra(grafo, origen)

    if destino not in distancias:
        raise ValueError(f"El nodo destino '{destino}' no existe en el grafo.")

    costo = distancias[destino]
    if costo == float("inf"):
        return float("inf"), []

    return costo, reconstruir_camino(predecesores, origen, destino)