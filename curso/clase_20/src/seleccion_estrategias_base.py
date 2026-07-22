"""Código base de la Clase 20; no contiene las decisiones resueltas."""

from __future__ import annotations

from dataclasses import dataclass


OBJETIVOS = frozenset({"camino_minimo", "conexion_minima", "orden_dependencias"})
TIPOS_PESO = frozenset({"sin_pesos", "cero_uno", "no_negativos", "incluye_negativos"})
ALGORITMOS = frozenset({"BFS", "0-1 BFS", "Dijkstra", "Kruskal", "Kahn"})


@dataclass(frozen=True)
class PerfilProblema:
    """Restricciones relevantes de un problema de grafos."""

    objetivo: str
    dirigido: bool
    tipo_pesos: str


@dataclass(frozen=True)
class DecisionAlgoritmica:
    """Decisión explicable; ``None`` significa que falta un algoritmo estudiado."""

    algoritmo: str | None
    estructura: str | None
    operacion_dominante: str
    complejidad: str | None
    advertencia: str


def validar_perfil(perfil: PerfilProblema) -> None:
    """Valida tipos y vocabulario; no devuelve una decisión."""
    raise NotImplementedError("Completa validar_perfil en tu entrega")


def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    """Elige una estrategia estudiada o documenta que ninguna aplica."""
    raise NotImplementedError("Completa seleccionar_estrategia en tu entrega")


def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    """Indica si el algoritmo satisface objetivo y restricciones."""
    raise NotImplementedError("Completa es_aplicable en tu entrega")


def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    """Explica por qué un algoritmo conocido no es la elección correcta."""
    raise NotImplementedError("Completa explicar_descarte en tu entrega")


def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Contrasta una propuesta con la decisión recomendada."""
    raise NotImplementedError("Completa evaluar_propuesta en tu entrega")


__all__ = [
    "ALGORITMOS",
    "OBJETIVOS",
    "TIPOS_PESO",
    "DecisionAlgoritmica",
    "PerfilProblema",
    "es_aplicable",
    "evaluar_propuesta",
    "explicar_descarte",
    "seleccionar_estrategia",
    "validar_perfil",
]
