"""Implementación robusta, reutilizable y testeable del algoritmo de Dijkstra."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import heapq
import math

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo sin modificar la entrada ni compartir referencias.
    
    Resuelve la consistencia de tipos, detecta valores fuera de dominio (NaN, negativos)
    y asegura la existencia explícita de los vecinos implícitos.
    """
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un mapeo estructurado (Mapping).")
    
    resultado: dict[str, list[tuple[str, float]]] = {}
    
    # Primero registramos todas las llaves de origen provistas
    for nodo in grafo:
        if not isinstance(nodo, str):
            raise TypeError("El nombre del nodo debe ser un str.")
        if nodo not in resultado:
            resultado[nodo] = []

    # Validamos y estructuramos las aristas
    for nodo, aristas in grafo.items():
        if not isinstance(aristas, Sequence) or isinstance(aristas, (str, bytes)):
            raise TypeError("Las aristas de adyacencia deben ser una Sequence.")
        
        for arista in aristas:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("Cada arista debe representarse como un par (vecino, peso).")
            
            vecino, peso = arista
            
            if not isinstance(vecino, str):
                raise TypeError("El nombre del nodo vecino debe ser un str.")
            
            # Comprobación explícita porque isinstance(True, int) es True en Python
            if isinstance(peso, bool):
                raise TypeError("El peso debe ser un valor numérico, no bool.")
                
            if not isinstance(peso, (int, float)):
                raise TypeError("El peso debe ser un valor numérico (int o float).")
                
            if not math.isfinite(peso):
                raise ValueError("El peso debe ser un número finito (no NaN ni infinito).")
                
            if peso < 0:
                raise ValueError("Los pesos de las aristas deben ser no negativos.")
            
            # Garantizar la representación total de vecinos implícitos
            if vecino not in resultado:
                resultado[vecino] = []
                
            resultado[nodo].append((vecino, float(peso)))
            
    return resultado


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias mínimas y predecesores desde un origen válido.
    
    Sostiene el invariante de tablas totales y el descarte de candidaturas
    obsoletas del min-heap en tiempo de ejecución.
    """
    # La normalización ofrece una copia defensiva limpia y valida la frontera
    normalizado = _normalizar_grafo(grafo)
    
    if origen not in normalizado:
        raise KeyError("El nodo origen no existe en el grafo proporcionado.")
        
    # Invariante 1: Tablas inicializadas en su totalidad
    distancias = {nodo: math.inf for nodo in normalizado}
    predecesores: dict[str, str | None] = {nodo: None for nodo in normalizado}
    
    distancias[origen] = 0.0
    
    # Invariante 2: El min-heap almacena tuplas históricas (distancia, nodo)
    pendientes = [(0.0, origen)]
    
    while pendientes:
        distancia_extraida, actual = heapq.heappop(pendientes)
        
        # Invariante 3: Guard clause para ignorar de forma perezosa entradas obsoletas
        if distancia_extraida != distancias[actual]:
            continue
            
        for vecino, peso in normalizado[actual]:
            candidata = distancia_extraida + peso
            
            if candidata < distancias[vecino]:
                # Invariante 4: Actualización atómica de costo, predecesor y heap
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (candidata, vecino))
                
    return distancias, predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye la secuencia de nodos desde el origen hasta el destino.
    
    Lanza KeyError si los nodos no pertenecen a la estructura, detecta ciclos
    de corrupción y procesa componentes inalcanzables devolviendo una lista vacía.
    """
    if origen not in predecesores or destino not in predecesores:
        raise KeyError("El origen o destino no existen en la tabla de predecesores.")
        
    if origen == destino:
        return [origen]
        
    camino = []
    actual: str | None = destino
    vistos = set()
    
    while actual is not None:
        # Defensa activa contra grafos con ciclos lógicos infinitos
        if actual in vistos:
            raise ValueError("Se ha detectado un ciclo en los predecesores.")
            
        vistos.add(actual)
        camino.append(actual)
        
        if actual == origen:
            break
            
        actual = predecesores[actual]
    else:
        # Se llegó a None sin interceptar el origen (Destino inalcanzable)
        return []
        
    # El camino se recolectó a la inversa; se retorna invertido
    return camino[::-1]


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina de manera segura el cálculo de rutas y la reconstrucción del camino.
    
    Evita la duplicación lógica delegando el trabajo pesado a dijkstra y reconstruir_camino.
    """
    distancias, predecesores = dijkstra(grafo, origen)
    
    if destino not in distancias:
        raise KeyError("El nodo destino solicitado no existe en el grafo.")
        
    costo = distancias[destino]
    camino = reconstruir_camino(predecesores, origen, destino)
    
    return costo, camino