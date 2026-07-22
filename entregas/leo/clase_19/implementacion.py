"""Código base de la Clase 19; implementación."""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido."""
    normalizado: dict[str, list[str]] = {}

    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Los nodos deben ser str")
        if not isinstance(vecinos, (list, tuple)):
            raise TypeError("Los vecinos deben ser una secuencia")
        vistos: set[str] = set()
        normalizado[nodo] = []
        for vecino in vecinos:
            if not isinstance(vecino, str):
                raise TypeError("Cada vecino deben ser str")
            if vecino not in vistos:
                vistos.add(vecino)
                normalizado[nodo].append(vecino)
                if vecino not in normalizado:
                    normalizado[vecino] = []
    return normalizado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo."""

    grafo = normalizar_grafo_dirigido(grafo)
    grados = {nodo: 0 for nodo in grafo}
    for vecinos in grafo.values():
        for vecino in vecinos:
            grados[vecino] += 1
    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico o ``None`` si existe un ciclo."""

    grafo = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(grafo)
    cola = deque()
    for nodo, grado in grados.items():
        if grado == 0:
            cola.append(nodo)
    orden: list[str] = []
    while cola:
        actual = cola.popleft()
        orden.append(actual)
        for vecino in grafo[actual]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                cola.append(vecino)
    if len(orden) != len(grafo):
        return None
    return orden


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""

    grafo = normalizar_grafo_dirigido(grafo)
    if len(orden) != len(grafo):
        return False
    if len(set(orden)) != len(orden):
        return False
    if set(orden) != set(grafo):
        return False
    posicion = {nodo: i for i, nodo in enumerate(orden)}
    for origen, vecinos in grafo.items():
        for destino in vecinos:
            if posicion[origen] >= posicion[destino]:
                return False
    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares ``(prerrequisito, curso)``."""

    if isinstance(numero_cursos, bool) or not isinstance(numero_cursos, int):
        raise TypeError("El numero de cursos debe ser un entero")
    if numero_cursos < 0:
        raise ValueError("El numero de cursos debe ser un entero no negattivo")
    grafo: dict[str, list[str]] = {str(i): [] for i in range(numero_cursos)}
    for prerreq in prerrequisitos:
        if not isinstance(prerreq, (list, tuple)) or not len(prerreq) == 2:
            raise ValueError("Cada prerrequisito debe contener un par")
    for prerrequisito, curso in prerrequisitos:
        if not isinstance(prerrequisito, int) or isinstance(prerrequisito, bool) or not isinstance(curso, int) or isinstance(curso, bool):
            raise TypeError("La tupla debe contener enteros")
        if not (0 <= prerrequisito < numero_cursos) or not (0 <= curso < numero_cursos):
            raise IndexError("Índice de curso inválido")
        if prerrequisito == curso:
            return None
        origen = str(prerrequisito)
        destino = str(curso)
        if destino not in grafo[origen]:
            grafo[origen].append(destino)
    orden = orden_topologico(grafo)
    if orden is None:
        return None
    return [int(curso) for curso in orden]


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