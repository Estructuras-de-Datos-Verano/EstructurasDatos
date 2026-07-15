"""Versión deliberadamente incompleta para practicar revisión de código.

No la entregues como solución. Identifica qué contratos no protege y diseña
pruebas que reproduzcan cada problema antes de corregirlo en tu entrega.
"""

from __future__ import annotations

import heapq
import math


def dijkstra_para_revisar(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula rutas en algunos grafos válidos, pero omite robustez."""

    distancias = {nodo: math.inf for nodo in grafo}
    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo}
    distancias[origen] = 0.0
    pendientes = [(0.0, origen)]
    while pendientes:
        distancia, actual = heapq.heappop(pendientes)
        for vecino, peso in grafo[actual]:
            candidata = distancia + peso
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (candidata, vecino))
    return distancias, predecesores

