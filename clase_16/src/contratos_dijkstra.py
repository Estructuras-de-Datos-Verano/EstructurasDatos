"""Firmas y contratos para la implementación robusta de Dijkstra."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def _normalizar_grafo(grafo: GrafoPonderado) -> dict[str, list[tuple[str, float]]]:
    """Copia y valida el grafo sin compartir listas con la entrada."""

    raise NotImplementedError("Completa _normalizar_grafo en tu entrega")


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias y predecesores desde un origen válido."""

    raise NotImplementedError("Completa dijkstra en tu entrega")


def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye un camino o devuelve una lista vacía si es inalcanzable."""

    raise NotImplementedError("Completa reconstruir_camino en tu entrega")


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Coordina cálculo y reconstrucción para un destino."""

    raise NotImplementedError("Completa camino_minimo en tu entrega")

