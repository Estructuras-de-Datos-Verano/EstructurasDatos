import math
import heapq
from typing import Mapping, Sequence, Any, Tuple, Dict, List

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[Tuple[str, Peso]]]

def _normalizar_grafo(grafo: Any) -> Dict[str, List[Tuple[str, float]]]:
    """
    Valida la estructura del grafo, realiza una copia defensiva
    y normaliza pesos a floats, asegurando representación total.
    """
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser una estructura de mapeo (Mapping).")
        
    resultado: Dict[str, List[Tuple[str, float]]] = {}
    
    for nodo, aristas in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Las claves del grafo (nodos) deben ser strings.")
        if not isinstance(aristas, Sequence) or isinstance(aristas, str):
            raise TypeError("Las aristas de un nodo deben ser una secuencia.")
            
        resultado[nodo] = []
        for arista in aristas:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("Cada arista debe ser un par (vecino, peso).")
                
            vecino, peso = arista
            if not isinstance(vecino, str):
                raise TypeError("El nodo vecino debe ser un string.")
                
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("El peso debe ser numérico (no booleano).")
                
            if not math.isfinite(peso):
                raise ValueError("El peso debe ser un número finito (no NaN ni infinito).")
            if peso < 0:
                raise ValueError("Los pesos deben ser no negativos para Dijkstra.")
                
            resultado[nodo].append((vecino, float(peso)))
            
    vecinos_implicitos = set()
    for aristas in resultado.values():
        for vecino, _ in aristas:
            if vecino not in resultado:
                vecinos_implicitos.add(vecino)
                
    for vecino in vecinos_implicitos:
        resultado[vecino] = []
        
    return resultado

def dijkstra(grafo: GrafoPonderado, origen: str) -> Tuple[Dict[str, float], Dict[str, str | None]]:
    """
    Calcula distancias mínimas y predecesores desde un nodo origen usando Dijkstra.
    """
    grafo_norm = _normalizar_grafo(grafo)
    
    if origen not in grafo_norm:
        raise KeyError(f"El nodo origen '{origen}' no existe en el grafo.")
        
    distancias: Dict[str, float] = {nodo: math.inf for nodo in grafo_norm}
    predecesores: Dict[str, str | None] = {nodo: None for nodo in grafo_norm}
    
    distancias[origen] = 0.0
    pendientes = [(0.0, origen)]
    
    while pendientes:
        distancia_extraida, actual = heapq.heappop(pendientes)
        
        if distancia_extraida != distancias[actual]:
            continue
            
        for vecino, peso in grafo_norm[actual]:
            candidata = distancia_extraida + peso

            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (candidata, vecino))
                
    return distancias, predecesores

def reconstruir_camino(predecesores: Dict[str, str | None], origen: str, destino: str) -> List[str]:
    """
    Reconstruye la secuencia de nodos desde el origen hasta el destino.
    """
    if origen not in predecesores or destino not in predecesores:
        raise KeyError("El origen o destino no se encuentran en el mapeo de predecesores.")
        
    if origen == destino:
        return [origen]
        
    camino = []
    actual = destino
    vistos = set()
    
    while actual is not None:
        if actual in vistos:
            raise ValueError("Se detectó un ciclo infinito en la cadena de predecesores.")
        vistos.add(actual)
        camino.append(actual)
        if actual == origen:
            break
        actual = predecesores[actual]
        
    if camino[-1] != origen:
        return []
        
    return camino[::-1]

def camino_minimo(grafo: GrafoPonderado, origen: str, destino: str) -> Tuple[float, List[str]]:
    """
    Coordina la obtención de distancias y reconstrucción del camino mínimo sin duplicar lógica.
    """
    distancias, predecesores = dijkstra(grafo, origen)
    
    if destino not in distancias:
        raise KeyError(f"El nodo destino '{destino}' no existe en el grafo.")
        
    costo = distancias[destino]
    camino = reconstruir_camino(predecesores, origen, destino)
    
    return costo, camino