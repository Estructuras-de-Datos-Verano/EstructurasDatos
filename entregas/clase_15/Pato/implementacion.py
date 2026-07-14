from __future__ import annotations
import heapq
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias mínimas y predecesores desde un origen."""
    
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
        
    nodos_totales = set(grafo.keys())
    for vecinos in grafo.values():
        for vecino, peso in vecinos:
            if peso < 0:
                raise ValueError("El grafo contiene pesos negativos; Dijkstra no es aplicable.")
            nodos_totales.add(vecino)

    distancias = {nodo: float('inf') for nodo in nodos_totales}
    distancias[origen] = 0.0
    predecesores = {nodo: None for nodo in nodos_totales}
    
    cola_prioridad: list[tuple[float, str]] = [(0.0, origen)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo.get(nodo_actual, []):
            nueva_distancia = distancia_actual + peso
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                
    return distancias, predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino del origen al destino o devuelve lista vacía."""
    
    if origen not in predecesores:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo de predecesores.")
    if destino not in predecesores:
        raise KeyError(f"El nodo destino '{destino}' no pertenece al grafo de predecesores.")
        
    camino = []
    nodo_actual = destino
    
    while nodo_actual is not None:
        camino.append(nodo_actual)
        if nodo_actual == origen:
            return camino[::-1]  
        nodo_actual = predecesores[nodo_actual]
        
    return []


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Devuelve el costo mínimo y el camino correspondiente."""
    
    if destino not in grafo:
        raise KeyError(f"El nodo destino '{destino}' no pertenece al grafo.")
    
    distancias, predecesores = dijkstra(grafo, origen)
    
    costo = distancias.get(destino, float('inf'))
    
    if costo == float('inf'):
        return float('inf'), []
        
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino

