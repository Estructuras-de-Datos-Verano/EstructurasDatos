"""Código base de la Clase 20; implementación."""

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
    """Decisión explicable."""

    algoritmo: str | None
    estructura: str | None
    operacion_dominante: str
    complejidad: str | None
    advertencia: str


def validar_perfil(perfil: PerfilProblema) -> None:
    """Valida tipos y vocabulario."""

    if not isinstance(perfil, PerfilProblema):
        raise TypeError("Se esperaba un PerfilProblema.")
    if not isinstance(perfil.objetivo, str):
        raise TypeError("El objetivo debe ser str.")
    if type(perfil.dirigido) is not bool:
        raise TypeError("Dirigido debe ser bool.")
    if not isinstance(perfil.tipo_pesos, str):
        raise TypeError("tipo_pesos debe ser str.")
    if perfil.objetivo not in OBJETIVOS:
        raise ValueError("El objetivo es desconocido.")
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError("Tipo de pesos desconocido.")


def seleccionar_estrategia(
    perfil: PerfilProblema,
) -> DecisionAlgoritmica:
    """Selecciona la estrategia estudiada adecuada."""

    validar_perfil(perfil)

    if perfil.objetivo == "camino_minimo":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica(algoritmo="BFS", estructura="cola", operacion_dominante="procesar por capas", complejidad="O(V+E)", advertencia="")
        if perfil.tipo_pesos == "cero_uno":
            return DecisionAlgoritmica(algoritmo="0-1 BFS", estructura="deque", operacion_dominante="procesar pesos 0/1", complejidad="O(V+E)", advertencia="")
        if perfil.tipo_pesos == "no_negativos":
            return DecisionAlgoritmica(algoritmo="Dijkstra", estructura="heap", operacion_dominante="extraer menor distancia", complejidad="O((V+E) log V)", advertencia="")
        return DecisionAlgoritmica(algoritmo=None, estructura=None, operacion_dominante="camino mínimo", complejidad=None, advertencia=("Los algoritmos estudiados no resuelven " "Hay caminos con pesos negativos."))

    if perfil.objetivo == "conexion_minima":
        if perfil.dirigido:
            return DecisionAlgoritmica(algoritmo=None, estructura=None, operacion_dominante="conectar componentes", complejidad=None, advertencia=("Kruskal requiere un grafo no dirigido."))
        if perfil.tipo_pesos == "incluye_negativos":
            return DecisionAlgoritmica(algoritmo="Kruskal", estructura="Union-Find", operacion_dominante="unir componentes", complejidad="O(E log E)",advertencia="")
        if perfil.tipo_pesos != "sin_pesos":
            return DecisionAlgoritmica(algoritmo="Kruskal", estructura="Union-Find", operacion_dominante="unir componentes", complejidad="O(E log E)",advertencia="")
        return DecisionAlgoritmica(algoritmo=None, estructura=None, operacion_dominante="conectar componentes", complejidad=None, advertencia=("La conexión mínima requiere aristas con costo."),)


    if perfil.objetivo == "orden_dependencias" and perfil.dirigido and perfil.tipo_pesos == "sin_pesos":
        return DecisionAlgoritmica(algoritmo="Kahn", estructura="cola + grados de entrada", operacion_dominante="grado de entrada cero", complejidad="O(V+E)", advertencia="")
    return DecisionAlgoritmica(algoritmo=None, estructura=None, operacion_dominante="ordenar dependencias", complejidad=None, advertencia=("Kahn requiere un grafo dirigido sin pesos."))


def es_aplicable(
    algoritmo: str,
    perfil: PerfilProblema,
) -> bool:
    """Indica si un algoritmo aplica al perfil."""

    validar_perfil(perfil)
    if not isinstance(algoritmo, str):
        raise TypeError("algoritmo debe ser str.")

    if algoritmo not in ALGORITMOS:
        raise ValueError("Algoritmo desconocido.")
    return seleccionar_estrategia(perfil).algoritmo == algoritmo


def explicar_descarte(
    algoritmo: str,
    perfil: PerfilProblema,
) -> str:
    """Explica por qué un algoritmo no es adecuado."""

    validar_perfil(perfil)
    if algoritmo not in ALGORITMOS:
        return "Algoritmo desconocido."
    if es_aplicable(algoritmo, perfil):
        operaciones = {"BFS": "capas", "0-1 BFS": "pesos 0/1", "Dijkstra": "distancia mínima", "Kruskal": "componentes", "Kahn": "grado de entrada cero"}
        return f"{algoritmo} sí aplica porque trabaja con " f"{operaciones[algoritmo]}."
    
    recomendacion = seleccionar_estrategia(perfil)
    razones = {"BFS": ("BFS minimiza el número de aristas y no el costo total."), "0-1 BFS": ("0-1 BFS requiere pesos únicamente 0 y 1."), "Dijkstra": ("Dijkstra requiere pesos no negativos y resuelve caminos mínimos, no MST."),
        "Kruskal": ("Kruskal solo construye una conexión mínima en grafos no dirigidos."), "Kahn": ("Kahn solo produce un orden de dependencias en grafos dirigidos.")}
    mensaje = razones[algoritmo]
    if recomendacion.algoritmo is not None:
        mensaje += f" Se recomienda {recomendacion.algoritmo}."
    else:
        mensaje += " Ningún algoritmo estudiado aplica."
    return mensaje


def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Evalúa una propuesta contra la recomendación."""

    errores: list[str] = []
    validar_perfil(perfil)
    if algoritmo not in ALGORITMOS:
        errores.append("Algoritmo desconocido.")
        return False, errores
    decision = seleccionar_estrategia(perfil)
    if decision.algoritmo is None:
        errores.append(decision.advertencia)
        return False, errores
    if not algoritmo == decision.algoritmo:
        errores.append(f"Algoritmo incorrecto: se esperaba {decision.algoritmo}.")
    if not estructura == decision.estructura:
        errores.append(f"Estructura incorrecta: se esperaba {decision.estructura}.")
    return len(errores) == 0, errores


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