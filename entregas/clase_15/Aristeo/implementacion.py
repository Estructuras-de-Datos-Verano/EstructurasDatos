import heapq
import math


def dijkstra(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula las distancias mínimas y predecesores desde un nodo origen usando Dijkstra.

    Args:
        grafo: Diccionario que representa las listas de adyacencia.
        origen: El nodo inicial del recorrido.

    Returns:
        Una tupla con:
            - Un diccionario de distancias mínimas desde el origen a cada nodo.
            - Un diccionario con el predecesor de cada nodo en el camino mínimo.

    Raises:
        KeyError: Si el origen no pertenece al grafo.
        ValueError: Si se detecta una arista con peso negativo.

    Example:
        >>> g = {"A": [("B", 2)], "B": []}
        >>> dijkstra(g, "A")
        ({'A': 0.0, 'B': 2.0}, {'A': None, 'B': 'A'})
    """
    # 1. Validar la existencia del origen
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no se encuentra en el grafo.")

    # Inicializar estructuras mapeando todos los nodos (incluyendo vecinos implícitos)
    distancias: dict[str, float] = {}
    predecesores: dict[str, str | None] = {}
    
    todos_los_nodos = set(grafo.keys())
    for vecinos in grafo.values():
        for destino, peso in vecinos:
            if peso < 0:
                raise ValueError("El algoritmo de Dijkstra no soporta pesos negativos.")
            todos_los_nodos.add(destino)

    for nodo in todos_los_nodos:
        distancias[nodo] = math.inf
        predecesores[nodo] = None

    distancias[origen] = 0.0
    
    # Heap de prioridad conteniendo tuplas (distancia_acumulada, nodo)
    cola_prioridad: list[tuple[float, str]] = [(0.0, origen)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Eliminación perezosa: ignorar candidaturas obsoletas
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Si el nodo actual no tiene aristas salientes en el dict, continuamos
        if nodo_actual not in grafo:
            continue

        for vecino, peso in grafo[nodo_actual]:
            distancia_candidata = distancia_actual + peso
            
            # Relajación de la arista
            if distancia_candidata < distancias[vecino]:
                distancias[vecino] = distancia_candidata
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_candidata, vecino))

    return distancias, predecesores


def reconstruir_camino(
    predecesores: dict[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino mínimo desde el origen al destino usando el mapa de predecesores.

    Args:
        predecesores: Diccionario que asocia cada nodo con su predecesor óptimo.
        origen: El nodo inicial del camino.
        destino: El nodo final del camino.

    Returns:
        Una lista de nodos ordenados desde origen a destino, o [] si es inalcanzable.
    """
    if destino not in predecesores:
        return []
    
    if origen == destino:
        return [origen]

    camino: list[str] = []
    nodo_actual: str | None = destino

    # Ciclar hacia atrás guardando el camino
    while nodo_actual is not None:
        camino.append(nodo_actual)
        if nodo_actual == origen:
            break
        nodo_actual = predecesores.get(nodo_actual)
    else:
        # Si terminamos el bucle sin alcanzar el origen, el destino es inalcanzable
        return []

    camino.reverse()
    return camino


def camino_minimo(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina el cálculo de Dijkstra y la reconstrucción para obtener costo y camino."""
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no se encuentra en el grafo.")
        
    distancias, predecesores = dijkstra(grafo, origen)
    
    # CORRECCIÓN AQUÍ: Quita la palabra 'Bios'
    if destino not in distancias:
        return math.inf, []
        
    costo = distancias[destino]
    if math.isinf(costo):
        return costo, []
        
    camino = reconstruir_camino(predecesores, origen, destino)
    return costo, camino