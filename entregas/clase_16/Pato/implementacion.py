from __future__ import annotations

import heapq
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo asegurando los tipos y formas correctas."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping.")

    nodos_totales = set()
    
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError(f"El nodo '{nodo}' debe ser str.")
        nodos_totales.add(nodo)
        
        if not isinstance(vecinos, Sequence) or isinstance(vecinos, str):
            raise TypeError("Las conexiones deben ser una secuencia.")
            
        for item in vecinos:
            if not isinstance(item, (tuple, list)) or len(item) != 2:
                raise TypeError("La arista debe ser un par (vecino, peso).")
            
            vecino, peso = item
            
            if not isinstance(vecino, str):
                raise TypeError(f"El vecino '{vecino}' debe ser str.")
                
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("El peso debe ser numérico.")
                
            if math.isnan(peso) or math.isinf(peso):
                raise ValueError("El peso debe ser finito.")
                
            if peso < 0:
                raise ValueError("Los pesos deben ser no negativos.")
                
            nodos_totales.add(vecino)
            
    grafo_norm: dict[str, list[tuple[str, float]]] = {nodo: [] for nodo in nodos_totales}
    for nodo, vecinos in grafo.items():
        grafo_norm[nodo] = [(vecino, float(peso)) for vecino, peso in vecinos]
        
    return grafo_norm


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias y predecesores desde un origen válido."""
    grafo_norm = _normalizar_grafo(grafo)
    
    if not isinstance(origen, str):
        raise TypeError("El origen debe ser str.")
        
    if origen not in grafo_norm:
        raise KeyError("El nodo origen no pertenece al grafo.")
        
    distancias = {nodo: math.inf for nodo in grafo_norm}
    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo_norm}
    
    distancias[origen] = 0.0
    pendientes = [(0.0, origen)]
    
    while pendientes:
        distancia_actual, nodo_actual = heapq.heappop(pendientes)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo_norm[nodo_actual]:
            candidata = distancia_actual + peso
            
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = nodo_actual
                heapq.heappush(pendientes, (candidata, vecino))
                
    return distancias, predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye un camino previniendo ciclos infinitos."""
    if origen not in predecesores or destino not in predecesores:
        raise KeyError("Origen o destino no pertenecen a los predecesores.")
        
    if origen == destino:
        return [origen]
        
    camino = []
    actual: str | None = destino
    visitados: set[str] = set()
    
    while actual is not None:
        if actual in visitados:
            raise ValueError(f"Se detectó un ciclo al evaluar '{actual}'.")
        visitados.add(actual)
        
        camino.append(actual)
        if actual == origen:
            return camino[::-1]
            
        actual = predecesores.get(actual)
        
    return []


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina cálculo y reconstrucción para un destino."""
    distancias, predecesores = dijkstra(grafo, origen)
    
    if destino not in distancias:
        raise KeyError(f"El nodo destino '{destino}' no pertenece al grafo.")
        
    costo = distancias[destino]
    if math.isinf(costo):
        return float('inf'), []
        
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino