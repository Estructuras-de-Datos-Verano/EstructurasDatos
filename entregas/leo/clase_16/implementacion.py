from __future__ import annotations
import heapq, math

from collections.abc import Mapping, Sequence


Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]



def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo sin compartir listas con la entrada."""

    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
    for llave in grafo.keys():
        if not isinstance(llave, str):
            raise TypeError("Las llaves del grafo deben ser str")
    for secuencia in grafo.values():
        for value in secuencia:
            if not isinstance(value[0], str):
                raise TypeError("Los vecinos de los nodos deben ser str")
    for secuencia in grafo.values():
        for value in secuencia:
            if not len(value) == 2:
                raise TypeError("Las tuplas deben ser pares")
            
    copia = {nodo: list(vecinos) for nodo, vecinos in grafo.items()}

    faltantes = []
    for secuencia in copia.values():
        for value in secuencia:
            if value[0] not in copia:
                faltantes.append(value[0])
    for vecino in faltantes:
        copia[vecino] = []

    for secuencia in copia.values():
        for value in secuencia:
            if isinstance(value[1], bool) or not isinstance(value[1], (int, float)):
                raise TypeError("Los pesos deben ser números")
            if math.isnan(value[1]) or math.isinf(value[1]):
                raise ValueError("Los pesos deben ser finitos")
            if value[1] < 0:
                raise ValueError("Los pesos no pueden ser negativos")
    return copia

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
    """
    grafo_n = _normalizar_grafo(grafo)

    if origen not in grafo_n.keys():
        raise KeyError("El origen debe pertenecer al grafo")
    
    distancias = {nodo: float('inf') for nodo in grafo_n}
    predecesores = {nodo: None for nodo in grafo_n}
    distancias[origen] = 0
    cola = [(0,origen)]
    while cola:
        dist_a, nodo_a = heapq.heappop(cola)
        if not dist_a == distancias[nodo_a]:
            continue
        for vecino, peso in grafo_n[nodo_a]:
            candidata = distancias[nodo_a] + peso
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = nodo_a
                heapq.heappush(cola,(candidata,vecino))

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
    visitados = set()
    nodo_a = destino
    while nodo_a is not None:
        if nodo_a in visitados:
            raise ValueError("Se detectó un ciclo en los predecesores")
        visitados.add(nodo_a)
        camino.append(nodo_a)
        nodo_a = predecesores[nodo_a]
    camino.reverse()
    if camino[0] == origen:
        return camino
    return []


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Devuelve el costo mínimo y el camino correspondiente."""


    if origen not in grafo:
        raise KeyError("El origen deb estar en el grafo")

    if destino not in grafo:
        raise KeyError("El destino debe estar en el grafo")

    distancias, predecesores = dijkstra(grafo, origen)
    costo = distancias.get(destino,float('inf'))
    if costo == float('inf'):
        return float('inf'), []
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino