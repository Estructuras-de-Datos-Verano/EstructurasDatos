"""Implementación del algoritmo de Dijkstra y reconstrucción de caminos."""

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
        Distancias (con costo mínimo a cada nodo) y predecesores.

    Raises
    ------
    KeyError
        Si el origen no pertenece al grafo (ni como llave ni como vecino).
    ValueError
        Si aparece un peso negativo.
    """
    # 1. Identificar todos los nodos (incluyendo los que son solo vecinos) y validar pesos
    nodos_totales = set(grafo.keys())
    for vecinos in grafo.values():
        for vecino, peso in vecinos:
            if peso < 0:
                raise ValueError(f"Dijkstra no admite pesos negativos. Arista infractora con peso: {peso}")
            nodos_totales.add(vecino)

    if origen not in nodos_totales:
        raise KeyError(f"El origen '{origen}' no pertenece al grafo.")

    # 2. Inicializar diccionarios
    distancias: dict[str, float] = {nodo: math.inf for nodo in nodos_totales}
    predecesores: dict[str, str | None] = {nodo: None for nodo in nodos_totales}
    
    distancias[origen] = 0.0
    cola_prioridad = [(0.0, origen)]

    # 3. Bucle principal
    while cola_prioridad:
        dist_extraida, actual = heapq.heappop(cola_prioridad)

        # Eliminación perezosa de entradas obsoletas
        if dist_extraida != distancias[actual]:
            continue

        # Relajar aristas. Se usa .get() con fallback [] por si "actual" es un vecino implícito
        for vecino, peso in grafo.get(actual, []):
            candidata = dist_extraida + peso
            
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(cola_prioridad, (candidata, vecino))

    return distancias, predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino del origen al destino o devuelve lista vacía.
    
    Parameters
    ----------
    predecesores : Mapping[str, str | None]
        Diccionario generado por Dijkstra.
    origen : str
        Nodo inicial.
    destino : str
        Nodo objetivo.

    Returns
    -------
    list[str]
        Lista de nodos ordenados del origen al destino, o [] si es inalcanzable.
    """
    if destino not in predecesores:
        return []

    camino = []
    actual: str | None = destino

    while actual is not None:
        camino.append(actual)
        if actual == origen:
            # Si llegamos exitosamente al origen, invertimos la lista y la retornamos
            return camino[::-1]
        actual = predecesores.get(actual)

    # Si terminamos el rastro y nunca tocamos el origen, es inalcanzable
    return []


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Devuelve el costo mínimo y el camino correspondiente.
    
    Parameters
    ----------
    grafo : GrafoPonderado
        La red de conexiones y sus pesos.
    origen : str
        Nodo de inicio.
    destino : str
        Nodo a alcanzar.

    Returns
    -------
    tuple[float, list[str]]
        Una tupla con (costo, camino_reconstruido).
    """
    # Verificamos que el destino exista en algún lugar del grafo
    nodos_totales = set(grafo.keys())
    for vecinos in grafo.values():
        for v, _ in vecinos:
            nodos_totales.add(v)
            
    if destino not in nodos_totales:
        raise KeyError(f"El destino '{destino}' no pertenece al grafo.")

    # 1. Calculamos los datos estructurales
    distancias, predecesores = dijkstra(grafo, origen)
    
    # 2. Ensamblamos la tupla de respuesta
    costo_final = distancias[destino]
    camino_final = reconstruir_camino(predecesores, origen, destino)
    
    return costo_final, camino_final
