"""Código base de la Clase 19; no contiene las soluciones."""

from __future__ import annotations

from collections.abc import Mapping, Sequence


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido."""
    raise NotImplementedError(
        "Completa normalizar_grafo_dirigido en tu entrega"
    )


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo."""
    raise NotImplementedError("Completa grados_entrada en tu entrega")


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico o ``None`` si existe un ciclo."""
    raise NotImplementedError("Completa orden_topologico en tu entrega")


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""
    raise NotImplementedError("Completa es_orden_topologico en tu entrega")


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares ``(prerrequisito, curso)``."""
    raise NotImplementedError("Completa ordenar_cursos en tu entrega")


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    raise NotImplementedError("Completa puede_completar_cursos en tu entrega")


__all__ = [
    "normalizar_grafo_dirigido",
    "grados_entrada",
    "orden_topologico",
    "es_orden_topologico",
    "ordenar_cursos",
    "puede_completar_cursos",
]

