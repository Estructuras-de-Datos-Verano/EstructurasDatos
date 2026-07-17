from __future__ import annotations
import heapq
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias mínimas y predecesores desde un origen.

    Parameters
    ----------
    grafo : GrafoPonderado
        Lista de adyacencia con pares ``(vecino, peso)`` no negativos.
    origen : str
        Nodo inicial.

    Returns
    -------
    tuple[dict[str, float], dict[str, str | None]]
        Distancias y predecesores para reconstruir caminos.

    Raises
    ------
    KeyError
        Si el origen no pertenece al grafo.
    ValueError
        Si aparece un peso negativo.

    Notes
    -----
    Completa esta firma en ``entregas/clase_15/nombre/implementacion.py``.
    """

    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no se encuentra en el grafo.")

    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no se encuentra en el grafo.")

    distancias: dict[str, float] = {}
    predecesores: dict[str, str | None] = {}


    for nodo in grafo:
        if nodo not in distancias:
            distancias[nodo] = math.inf
            predecesores[nodo] = None
            
        for vecino, peso in grafo[nodo]:
            if vecino not in distancias:
                distancias[vecino] = math.inf
                predecesores[vecino] = None


    distancias[origen] = 0.0
    pq = [(0.0, origen)]

   
    while pq:
        dist_extraida, actual = heapq.heappop(pq)

        if dist_extraida != distancias[actual]:
            continue

        vecinos = grafo.get(actual, [])

        for vecino, peso in vecinos:
            if peso < 0:
                raise ValueError(f"Peso negativo ({peso}) detectado en la arista {actual} -> {vecino}.")

            candidata = dist_extraida + peso

            if candidata < distancias[vecino]:
                distancias[vecino] = float(candidata)
                predecesores[vecino] = actual
                heapq.heappush(pq, (candidata, vecino))

    return distancias, predecesores

def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino del origen al destino o devuelve lista vacía."""

    if destino not in predecesores:
        return []

    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = predecesores.get(actual)

    if not camino or camino[-1] != origen:
        return []

    camino.reverse()
    return camino


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Devuelve el costo mínimo y el camino correspondiente."""

    if destino not in grafo:
        raise KeyError(f"El nodo destino '{destino}' no se encuentra en el grafo.")
        
    distancias, predecesores = dijkstra(grafo, origen)
    
    costo_minimo = distancias[destino]
    
    if costo_minimo == math.inf:
        camino = []
    else:
        camino = reconstruir_camino(predecesores, origen, destino)
        
    return costo_minimo, camino
