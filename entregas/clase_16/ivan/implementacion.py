from __future__ import annotations
import heapq
import itertools
import math
from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]

def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo sin compartir listas con la entrada."""
    copia: dict[str, list[tuple[str, float]]] = {}
    # 0. Validar que el grafo sea un Mapping
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping.")
    # 1. Validar que las claves principales sean strings y crear la base de la copia
    for nodo in grafo:
        if not isinstance(nodo, str):
            raise TypeError(f"El nodo origen debe ser un string. Recibido: {type(nodo)}")
        copia[nodo] = []
        
    # 2. Iterar, validar aristas y poblar la copia
    for u, aristas in grafo.items():
        for arista in aristas:
            
            # Contrato: rechazar aristas que no sean pares (tuplas de tamaño 2)
            if not isinstance(arista, tuple) or len(arista) != 2:
                raise TypeError("La arista debe ser un par (tupla de 2 elementos).")
            
            v, peso = arista
            
            # Contrato: rechazar vecinos que no sean str
            if not isinstance(v, str):
                raise TypeError(f"El nodo destino debe ser un string. Recibido: {type(v)}")
                
            # Contrato: rechazar bool y pesos no numéricos con TypeError
            if isinstance(peso, bool) or not isinstance(peso, (int, float)):
                raise TypeError("Los pesos deben ser numéricos (int o float).")
            
            # Contrato: rechazar NaN, infinitos y negativos con ValueError
            if not math.isfinite(peso):
                raise ValueError("Los pesos deben ser números finitos (no infinito ni NaN).")
            if peso < 0:
                raise ValueError("Los pesos deben ser no negativos.")
            
            # Contrato: convertir pesos válidos a float y hacer copia defensiva
            copia[u].append((v, float(peso)))
            
            # Contrato: agregue vecinos que solo aparezcan como destino (vecino implícito)
            if v not in copia:
                copia[v] = []
                
    return copia

def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias y predecesores desde un origen válido."""
    
    # Invariante 5: el grafo original no cambia (creamos y usamos una copia independiente)
    grafo_seguro = _normalizar_grafo(grafo)
    
    if origen not in grafo_seguro:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
    
    # Invariante 1: todo nodo normalizado existe en distancias y predecesores
    distancias: dict[str, float] = {nodo: math.inf for nodo in grafo_seguro}
    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo_seguro}
    
    distancias[origen] = 0.0
    
    # Invariante 2: el heap guarda candidaturas históricas (distancia, nodo)
    pendientes = [(0.0, origen)]
    
    while pendientes:
        distancia, actual = heapq.heappop(pendientes)
        
        # Invariante 3: solo una candidatura igual a la distancia vigente relaja vecinos.
        # (Si la extraída es mayor, significa que es un dato histórico obsoleto)
        if distancia > distancias[actual]:
            continue
            
        for vecino, peso in grafo_seguro[actual]:
            candidata = distancia + peso
            
            # Invariante 4: una mejora actualiza distancia, predecesor y heap
            if candidata < distancias[vecino]:
                distancias[vecino] = candidata
                predecesores[vecino] = actual
                heapq.heappush(pendientes, (candidata, vecino))
                
    return distancias, predecesores

def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye un camino o devuelve una lista vacía si es inalcanzable."""
    
    # Distingue: clave ausente (origen o destino no registrados)
    if destino not in predecesores or origen not in predecesores:
        return []
        
    camino = []
    actual: str | None = destino
    visitados = set()
    
    while actual is not None:
        # Distingue: ciclo (si el diccionario está malformado y entra en bucle)
        if actual in visitados:
            raise ValueError("El ciclo detectado es inválido en diccionario de predecesores.")
            
        visitados.add(actual)
        camino.append(actual)
        
        # Distingue: origen = destino (y condición de parada exitosa)
        if actual == origen:
            break
            
        actual = predecesores.get(actual)
        
    # Distingue: inalcanzable (recorrimos hacia atrás pero nunca llegamos al origen)
    if not camino or camino[-1] != origen:
        return []
        
    camino.reverse()
    return camino


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina cálculo y reconstrucción para un destino."""
    
    # Coordina sin duplicar: llama a las piezas de Lego que ya validamos
    distancias, predecesores = dijkstra(grafo, origen)
    
    # Extrae el costo final (retorna inf si el destino no está o no es alcanzable)
    costo = distancias.get(destino, math.inf)
    
    # Si la distancia es infinita, ni siquiera intentamos reconstruir
    if costo == math.inf:
        return math.inf, []
        
    ruta = reconstruir_camino(predecesores, origen, destino)
    
    return costo, ruta  
