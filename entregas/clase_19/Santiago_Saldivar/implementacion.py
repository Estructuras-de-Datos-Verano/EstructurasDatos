from __future__ import annotations

from collections.abc import Mapping, Sequence
from collections import deque


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido."""
    if isinstance(grafo, bool) or not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser una estructura de mapeo (Mapping).")

    resultado: dict[str, list[str]] = {}
    
    # Conservamos el orden de inserción original de las claves
    for nodo, vecinos in grafo.items():
        if isinstance(nodo, bool) or not isinstance(nodo, str):
            raise TypeError("Las llaves (nodos) del grafo deben ser cadenas de texto (str).")
        
        # Validar que los vecinos sean una secuencia real y no un str o conjunto
        if isinstance(vecinos, (str, bytes, set)) or not isinstance(vecinos, Sequence):
            raise TypeError("Los vecinos deben estar contenidos en una secuencia (Sequence).")
            
        lista_vecinos: list[str] = []
        vistos = set()
        for v in vecinos:
            if isinstance(v, bool) or not isinstance(v, str):
                raise TypeError("Cada vecino debe ser una cadena de texto (str).")
            if v not in vistos:
                vistos.add(v)
                lista_vecinos.append(v)
        resultado[nodo] = lista_vecinos

    # Obtener el orden de todos los nodos según su primera aparición
    todos_los_nodos: list[str] = []
    vistos_nodos = set()
    
    # 1. Añadimos primero las claves y sus vecinos respetando el orden
    for nodo, vecinos in resultado.items():
        if nodo not in vistos_nodos:
            vistos_nodos.add(nodo)
            todos_los_nodos.append(nodo)
        for v in vecinos:
            if v not in vistos_nodos:
                vistos_nodos.add(v)
                todos_los_nodos.append(v)
                
    # 2. Construimos el diccionario final en ese orden preciso de primera aparición
    grafo_normalizado: dict[str, list[str]] = {}
    for nodo in todos_los_nodos:
        grafo_normalizado[nodo] = resultado.get(nodo, [])

    return grafo_normalizado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo."""
    grafo_norm = normalizar_grafo_dirigido(grafo)
    grados = {nodo: 0 for nodo in grafo_norm}
    for vecinos in grafo_norm.values():
        for v in vecinos:
            grados[v] += 1
    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico o ``None`` si existe un ciclo."""
    try:
        grafo_norm = normalizar_grafo_dirigido(grafo)
    except (TypeError, ValueError):
        raise

    grados = {nodo: 0 for nodo in grafo_norm}
    for vecinos in grafo_norm.values():
        for v in vecinos:
            grados[v] += 1

    cola = deque([nodo for nodo, grado in grados.items() if grado == 0])
    orden: list[str] = []

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)

        for vecino in grafo_norm[nodo]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                cola.append(vecino)

    if len(orden) != len(grafo_norm):
        return None

    return orden


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""
    if isinstance(orden, bool) or not isinstance(orden, Sequence) or isinstance(orden, (str, bytes)):
        raise TypeError("El orden provisto debe ser una secuencia (Sequence).")

    try:
        grafo_norm = normalizar_grafo_dirigido(grafo)
    except (TypeError, ValueError):
        raise

    nodos_orden = []
    for nodo in orden:
        if isinstance(nodo, bool) or not isinstance(nodo, str):
            raise TypeError("Cada elemento del orden debe ser un str.")
        nodos_orden.append(nodo)

    if len(nodos_orden) != len(grafo_norm) or set(nodos_orden) != set(grafo_norm.keys()):
        return False

    posicion = {nodo: i for i, nodo in enumerate(nodos_orden)}

    for u, vecinos in grafo_norm.items():
        for v in vecinos:
            if posicion[u] >= posicion[v]:
                return False

    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares ``(prerrequisito, curso)``."""
    if isinstance(numero_cursos, bool) or not isinstance(numero_cursos, int):
        raise TypeError("El número de cursos debe ser un entero.")
    if numero_cursos < 0:
        raise ValueError("El número de cursos no puede ser negativo.")

    if not isinstance(prerrequisitos, list):
        raise TypeError("Los prerrequisitos deben ser una lista.")

    grafo: dict[int, list[int]] = {i: [] for i in range(numero_cursos)}
    grados = [0] * numero_cursos

    for item in prerrequisitos:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Cada prerrequisito debe ser una tupla de 2 enteros.")
        
        pre, curso = item
        if isinstance(pre, bool) or not isinstance(pre, int) or isinstance(curso, bool) or not isinstance(curso, int):
            raise TypeError("Los identificadores de los cursos deben ser enteros.")
            
        if pre < 0 or pre >= numero_cursos or curso < 0 or curso >= numero_cursos:
            raise IndexError("El identificador del curso está fuera de rango.")

        grafo[pre].append(curso)
        grados[curso] += 1

    cola = deque([i for i in range(numero_cursos) if grados[i] == 0])
    orden: list[int] = []

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)

        for vecino in grafo[nodo]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                cola.append(vecino)

    if len(orden) != numero_cursos:
        return None

    return orden


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    resultado = ordenar_cursos(numero_cursos, prerrequisitos)
    return resultado is not None


__all__ = [
    "normalizar_grafo_dirigido",
    "grados_entrada",
    "orden_topologico",
    "es_orden_topologico",
    "ordenar_cursos",
    "puede_completar_cursos",
]