import heapq

def dijkstra(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula las distancias mínimas y predecesores desde un origen usando Dijkstra.

    Args:
        grafo: Grafo representado como lista de adyacencia con pesos.
        origen: Nodo inicial del recorrido.

    Returns:
        Un tupla con el diccionario de distancias y el diccionario de predecesores.
    """
    if origen not in grafo:
        raise KeyError("El nodo origen no existe en el grafo.")

    distancias: dict[str, float] = {}
    predecesores: dict[str, str | None] = {}

    
    for u in grafo:
        distancias[u] = float("inf")
        predecesores[u] = None
        for v, peso in grafo[u]:
            if peso < 0:
                raise ValueError("Dijkstra no soporta grafos con pesos negativos.")
            if v not in distancias:
                distancias[v] = float("inf")
                predecesores[v] = None

    distancias[origen] = 0.0
    heap = [(0.0, origen)]

    while heap:
        dist_actual, u = heapq.heappop(heap)

        if dist_actual != distancias[u]:
            continue

        if u not in grafo:
            continue

        for v, peso in grafo[u]:
            candidata = dist_actual + peso
            if candidata < distancias[v]:
                distancias[v] = candidata
                predecesores[v] = u
                heapq.heappush(heap, (candidata, v))

    return distancias, predecesores

def reconstruir_camino(
    predecesores: dict[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino mínimo desde el origen al destino usando los predecesores.

    Args:
        predecesores: Diccionario con el mapa de predecesores.
        origen: Nodo inicial de la ruta.
        destino: Nodo final de la ruta.

    Returns:
        Una lista de strings con la ruta ordenada, o [] si no es alcanzable.
    """
    if destino not in predecesores:
        return []
    if origen == destino:
        return [origen]

    camino = []
    actual: str | None = destino
    
    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = predecesores.get(actual)
    else:
       
        return []

    camino.reverse()
    return camino

def camino_minimo(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Función coordinadora que calcula el costo total y la ruta óptima entre dos nodos.

    Args:
        grafo: Diccionario con la lista de adyacencia y pesos.
        origen: Nodo origen.
        destino: Nodo destino.

    Returns:
        Un tupla con el costo total (float) y la lista de la ruta (list).
    """
    if origen not in grafo or destino not in grafo:
        raise KeyError("El origen o el destino no pertenecen al grafo.")

    distancias, predecesores = dijkstra(grafo, origen)
    costo = distancias.get(destino, float("inf"))
    camino = reconstruir_camino(predecesores, origen, destino)

    return costo, camino