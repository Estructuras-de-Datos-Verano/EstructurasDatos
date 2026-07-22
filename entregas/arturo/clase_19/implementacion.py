from __future__ import annotations

from collections.abc import Mapping, Sequence
from collections import deque


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
        
    normalizado: dict[str, list[str]] = {}
    
    for nodo, sucesores in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("El nodo debe ser un string")
            
        if isinstance(sucesores, str) or not isinstance(sucesores, Sequence):
            raise TypeError("La adyacencia debe ser una secuencia no string")
            
        if nodo not in normalizado:
            normalizado[nodo] = []
            
        for sucesor in sucesores:
            if not isinstance(sucesor, str):
                raise TypeError("Cada sucesor debe ser un string")
                
            if sucesor not in normalizado:
                normalizado[sucesor] = []
                
            if sucesor not in normalizado[nodo]:
                normalizado[nodo].append(sucesor)
                
    return normalizado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo."""
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = {nodo: 0 for nodo in normalizado}
    
    for sucesores in normalizado.values():
        for sucesor in sucesores:
            grados[sucesor] += 1
            
    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico o ``None`` si existe un ciclo."""
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(normalizado)
    
    orden = []
    cola = deque([nodo for nodo, grado in grados.items() if grado == 0])

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        for sucesor in normalizado[nodo]:
            grados[sucesor] -= 1
            if grados[sucesor] == 0:
                cola.append(sucesor)

    if len(orden) == len(normalizado):
        return orden
    else:
        return None


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""
    normalizado = normalizar_grafo_dirigido(grafo)
    

    if len(orden) != len(normalizado):
        return False
        
    if set(orden) != set(normalizado):
        return False
        
    posicion = {nodo: i for i, nodo in enumerate(orden)}
    for nodo, sucesores in normalizado.items():
        for sucesor in sucesores:
            if posicion[nodo] >= posicion[sucesor]:
                return False
    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares ``(prerrequisito, curso)``."""
    if isinstance(numero_cursos, bool) or not isinstance(numero_cursos, int):
        raise TypeError("numero_cursos debe ser de tipo entero")
        
    if numero_cursos < 0:
        raise ValueError("numero_cursos no puede ser un valor negativo")
        
    grafo = {str(i): [] for i in range(numero_cursos)}
    
    for par in prerrequisitos:
        if not isinstance(par, tuple) or len(par) != 2:
            raise ValueError("Cada prerrequisito debe ser una tupla de dos elementos")
            
        prereq, curso = par

        if isinstance(prereq, bool) or not isinstance(prereq, int) or isinstance(curso, bool) or not isinstance(curso, int):
            raise TypeError("Los elementos internos del prerrequisito deben ser enteros")
            
        if prereq < 0 or prereq >= numero_cursos or curso < 0 or curso >= numero_cursos:
            raise IndexError("Índice de curso proporcionado está fuera de rango")
            
        grafo[str(prereq)].append(str(curso))

    orden = orden_topologico(grafo)
    
    if orden is None:
        return None
    else:
        return [int(nodo) for nodo in orden]


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    return ordenar_cursos(numero_cursos, prerrequisitos) is not None


__all__ = [
    "normalizar_grafo_dirigido",
    "grados_entrada",
    "orden_topologico",
    "es_orden_topologico",
    "ordenar_cursos",
    "puede_completar_cursos",
]