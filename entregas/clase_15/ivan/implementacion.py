"""Código base documentado para Clase 15; no contiene la solución."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from heapq import heappop, heappush

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
    nodos = set(grafo.keys())
    for vecino in grafo.values():
        for v, peso in vecino:
            if peso < 0:
                raise ValueError("El grafo contiene un peso negativo.")
            nodos.add(v)
    if origen not in nodos:
        raise KeyError(f"El nodo {origen} no pertenece al grafo.")
    distancias = {nodo: float("inf") for nodo in nodos}
    distancias[origen] = 0.0 # por si acaso
    predecesores = {nodo: None for nodo in nodos}
    queue = [(0.0, origen)]
    while queue:
        distancia_actual, nodo_actual = heappop(queue)
        if distancia_actual > distancias[nodo_actual]:
            continue
        for vecino, peso in grafo.get(nodo_actual, []):
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heappush(queue, (nueva_distancia, vecino))
    return distancias, predecesores

def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino del origen al destino o devuelve lista vacía."""

    if destino not in predecesores:
        return []
    if origen == destino:
        return [origen]
    camino = []
    nodo_actual = destino
    visited = set()
    while nodo_actual is not None and nodo_actual not in visited:
        visited.add(nodo_actual)
        camino.append(nodo_actual)
        if nodo_actual == origen:
            break
        nodo_actual = predecesores.get(nodo_actual)
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
    distancias, predecesores = dijkstra(grafo, origen)
    try:
        distancias, predecesores = dijkstra(grafo, origen)
    except KeyError:
        return float("inf"), []
    if destino not in distancias or distancias[destino] == float("inf"):
        return float("inf"), []
    costo = distancias[destino]
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino
