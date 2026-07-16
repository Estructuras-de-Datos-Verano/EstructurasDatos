import heapq
import math
from typing import Mapping, Sequence
from collections.abc import MutableMapping

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]
# aqui se define el tipo de datos para un grafo ponderado, donde cada nodo es una cadena y cada arista es una tupla que contiene un nodo vecino y un peso numérico.

class PredecesoresValidados(MutableMapping):
    """Wrapper de predecesores que valida consistencia con el grafo normalizado."""
    
    def __init__(self, predecesores_dict: dict, grafo_normalizado: dict, grafo_original: GrafoPonderado):
        self._preds = predecesores_dict
        self._grafo = grafo_normalizado
        self._grafo_original = grafo_original
        # Registra el estado inicial del grafo original
        self._grafo_snapshot = dict(grafo_original) if isinstance(grafo_original, dict) else None
    
    def __getitem__(self, key):
        # Valida que el grafo normalizado aún tiene la estructura esperada
        if key not in self._grafo:
            raise KeyError(f"Entrada obsoleta: nodo '{key}' no existe en el grafo actual.")
        # También valida si el grafo original ha cambiado
        if self._grafo_snapshot is not None and isinstance(self._grafo_original, dict):
            if dict(self._grafo_original) != self._grafo_snapshot:
                raise KeyError("Entrada obsoleta: el grafo ha sido modificado.")
        return self._preds[key]
    
    def __setitem__(self, key, value):
        self._preds[key] = value
    
    def __delitem__(self, key):
        del self._preds[key]
    
    def __iter__(self):
        return iter(self._preds)
    
    def __len__(self):
        return len(self._preds)
    
    def __contains__(self, key):
        return key in self._preds
def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un diccionario (Mapping).")
    
    resultado: dict[str, list[tuple[str, float]]] = {}
    
    for nodo, aristas in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Los nodos deben ser cadena de texto.")
        if not isinstance(aristas, Sequence) or isinstance(aristas, (str, bytes)):
            raise TypeError("Las aristas deben ser una secuencia (lista o tupla).")
            
        resultado.setdefault(nodo, [])
        
        for arista in aristas:
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("Cada arista debe ser un par (vecino, peso).")
                
            vecino, peso = arista
            if not isinstance(vecino, str):
                raise TypeError("El vecino debe ser cadena de texto.")
                
            # Excluimos booleanos explícitamente porque isinstance(True, int) es True
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("El peso debe ser numérico y no booleano.")
                
            if not math.isfinite(peso):
                raise ValueError("El peso no puede ser infinito ni NaN.")
            if peso < 0:
                raise ValueError("Pesos no negativos.")
                
            resultado[nodo].append((vecino, float(peso)))
            resultado.setdefault(vecino, [])  # Agrega vecinos que no tienen salida
            
    return resultado

# Implementación del algoritmo de Dijkstra
def dijkstra(grafo: GrafoPonderado, origen: str) -> tuple[dict[str, float], dict[str, str | None]]:
    grafo_limpio = _normalizar_grafo(grafo)
    
    if origen not in grafo_limpio:
        raise KeyError(f"El nodo origen '{origen}' no existe en el grafo.")
        
    distancias = {nodo: math.inf for nodo in grafo_limpio}
    predecesores = {nodo: None for nodo in grafo_limpio}
    
    distancias[origen] = 0.0
    pendientes = [(0.0, origen)]
    
    while pendientes:
        dist_actual, actual = heapq.heappop(pendientes)
        
        # Ignora registros antiguos del heap
        if dist_actual != distancias[actual]:
            continue
            
        for vecino, peso in grafo_limpio[actual]:
            candidata = dist_actual + peso
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (candidata, vecino))
                
    return distancias, PredecesoresValidados(predecesores, grafo_limpio, grafo)

# aqui se define la función para reconstruir el camino más corto desde el origen hasta el destino usando la tabla de predecesores generada por Dijkstra.
def reconstruir_camino(predecesores: dict[str, str | None], origen: str, destino: str) -> list[str]:
    if origen not in predecesores or destino not in predecesores:
        raise KeyError("El origen o el destino no existen en la tabla de predecesores.")
        
    if origen == destino:
        return [origen]
        
    camino = []
    actual = destino
    vistos = set()
    
    while actual is not None:
        if actual in vistos:
            raise ValueError("Ciclo infinito: ciclo detectado en la tabla de predecesores.")
        vistos.add(actual)
        camino.append(actual)
        
        if actual == origen:
            break
        actual = predecesores[actual]
        
    if camino[-1] != origen:
        return []  # Destino inalcanzable
        
    camino.reverse()
    return camino

# aquí se define la función para calcular el camino mínimo entre dos nodos en un grafo ponderado utilizando Dijkstra y reconstruyendo el camino.
def camino_minimo(grafo: GrafoPonderado, origen: str, destino: str) -> tuple[float, list[str]]:
    distancias, predecesores = dijkstra(grafo, origen)
    
    if destino not in distancias:
        raise KeyError(f"El destino '{destino}' no existe en el grafo calculado.")
        
    return distancias[destino], reconstruir_camino(predecesores, origen, destino)