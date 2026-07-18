"""Implementación de ordenamiento topológico y algoritmo de Kahn."""

from __future__ import annotations
from collections import deque
from collections.abc import Mapping, Sequence


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia defensivamente y normaliza un grafo dirigido."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping (ej. dict)")

    # Para recolectar las claves y vecinos válidos manteniendo orden estricto de primera aparición
    nodos_en_orden: list[str] = []
    adyacencias_temporales: dict[str, list[str]] = {}

    # Primera pasada: Validar tipos y registrar apariciones en orden
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Las claves del grafo deben ser strings")
        if not isinstance(vecinos, (list, tuple)):
            raise TypeError("Las adyacencias deben ser secuencias (listas o tuplas)")
            
        if nodo not in nodos_en_orden:
            nodos_en_orden.append(nodo)
            
        if nodo not in adyacencias_temporales:
            adyacencias_temporales[nodo] = []
            
        for vecino in vecinos:
            if not isinstance(vecino, str):
                raise TypeError("Los vecinos deben ser strings")
            
            # Registrar el vecino en la lista de orden si aparece por primera vez
            if vecino not in nodos_en_orden:
                nodos_en_orden.append(vecino)
                
            if vecino not in adyacencias_temporales[nodo]:
                adyacencias_temporales[nodo].append(vecino)

    # Construir el resultado final respetando el orden exacto de descubrimiento
    resultado: dict[str, list[str]] = {}
    for nodo in nodos_en_orden:
        # Si era un destino implícito, su lista de adyacencia por defecto es vacía
        resultado[nodo] = adyacencias_temporales.get(nodo, [])

    return resultado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo tras normalizar."""
    grafo_norm = normalizar_grafo_dirigido(grafo)
    grados = {nodo: 0 for nodo in grafo_norm}
    
    for vecinos in grafo_norm.values():
        for vecino in vecinos:
            grados[vecino] += 1
            
    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico usando el Algoritmo de Kahn o None si hay ciclo."""
    grafo_norm = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(grafo_norm)
    
    # Encolar inicialmente todos los nodos con grado cero
    disponibles = deque(nodo for nodo in grafo_norm if grados[nodo] == 0)
    orden: list[str] = []
    
    while disponibles:
        actual = disponibles.popleft()
        orden.append(actual)
        
        for vecino in grafo_norm[actual]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                disponibles.append(vecino)
                
    # Si no se procesaron todos los nodos, hay un ciclo presente en el grafo
    if len(orden) != len(grafo_norm):
        return None
        
    return orden


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""
    try:
        grafo_norm = normalizar_grafo_dirigido(grafo)
    except (TypeError, ValueError):
        return False

    # 1. Comprobar longitud y cobertura exacta
    if len(orden) != len(grafo_norm) or set(orden) != set(grafo_norm.keys()):
        return False
        
    # 2. Ausencia de repetidos
    if len(set(orden)) != len(orden):
        return False

    # 3. Mapear posiciones
    posicion = {nodo: indice for indice, nodo in enumerate(orden)}
    
    # 4. Validar aristas: posicion[u] < posicion[v]
    for u, vecinos in grafo_norm.items():
        for v in vecinos:
            if posicion[u] >= posicion[v]:
                return False
                
    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos basándose en el contrato estricto de enteros."""
    if isinstance(numero_cursos, bool):
        raise TypeError("La cantidad no puede ser un booleano")
    if not isinstance(numero_cursos, int):
        raise TypeError("La cantidad debe ser un entero")
    if numero_cursos < 0:
        raise ValueError("La cantidad de cursos no puede ser negativa")

    grafo: dict[int, list[int]] = {i: [] for i in range(numero_cursos)}
    grados = {i: 0 for i in range(numero_cursos)}
    
    for par in prerrequisitos:
        if not isinstance(par, tuple) or len(par) != 2:
            raise ValueError("Cada prerrequisito debe ser un par (tupla de 2)")
        u, v = par
        
        if isinstance(u, bool) or isinstance(v, bool):
            raise TypeError("Los índices no pueden ser booleanos")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los extremos deben ser enteros")
            
        if u < 0 or u >= numero_cursos or v < 0 or v >= numero_cursos:
            raise IndexError("Índice de curso fuera de rango legal (0 a n-1)")
            
        if v not in grafo[u]:
            grafo[u].append(v)
            grados[v] += 1

    disponibles = deque(i for i in range(numero_cursos) if grados[i] == 0)
    orden: list[int] = []
    
    while disponibles:
        actual = disponibles.popleft()
        orden.append(actual)
        for vecino in grafo[actual]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                disponibles.append(vecino)
                
    if len(orden) != numero_cursos:
        return None
        
    return orden


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    return ordenar_cursos(numero_cursos, prerrequisitos) is not None