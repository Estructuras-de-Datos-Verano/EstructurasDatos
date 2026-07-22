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
    """Valida tipos y vocabulario del perfil de manera estricta."""
    if perfil is None or not isinstance(perfil, PerfilProblema):
        raise TypeError("El perfil debe ser una instancia de PerfilProblema.")
    
    # Evitar que booleanos se hagan pasar por strings
    if isinstance(perfil.objetivo, bool) or not isinstance(perfil.objetivo, str):
        raise TypeError("El objetivo debe ser una cadena de texto (str).")
    if not isinstance(perfil.dirigido, bool):
        raise TypeError("El atributo 'dirigido' debe ser estrictamente un booleano.")
    if isinstance(perfil.tipo_pesos, bool) or not isinstance(perfil.tipo_pesos, str):
        raise TypeError("El tipo de pesos debe ser una cadena de texto (str).")

    if perfil.objetivo not in OBJETIVOS:
        raise ValueError(f"Objetivo desconocido: {perfil.objetivo}")
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError(f"Tipo de pesos desconocido: {perfil.tipo_pesos}")


def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    """Elige una estrategia estudiada o documenta que ninguna aplica."""
    validar_perfil(perfil)

    # 1. Camino Mínimo sin pesos (BFS)
    if perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "sin_pesos":
        return DecisionAlgoritmica(
            algoritmo="BFS",
            estructura="cola",
            operacion_dominante="búsqueda por capas",
            complejidad="O(V+E)",
            advertencia=""
        )

    # 2. Camino Mínimo con pesos 0/1 (0-1 BFS)
    if perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "cero_uno":
        return DecisionAlgoritmica(
            algoritmo="0-1 BFS",
            estructura="deque",
            operacion_dominante="inserción en extremos (0/1)",
            complejidad="O(V+E)",
            advertencia=""
        )

    # 3. Camino Mínimo con pesos no negativos (Dijkstra)
    if perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "no_negativos":
        return DecisionAlgoritmica(
            algoritmo="Dijkstra",
            estructura="heap",
            operacion_dominante="extracción de mínima distancia",
            complejidad="O(E log V)",
            advertencia=""
        )

    # 4. Conexión Mínima (Kruskal) -> Solo aplica a grafos no dirigidos
    if perfil.objetivo == "conexion_minima" and not perfil.dirigido:
        if perfil.tipo_pesos in {"no_negativos", "incluye_negativos"}:
            return DecisionAlgoritmica(
                algoritmo="Kruskal",
                estructura="Union-Find",
                operacion_dominante="unión y búsqueda de componentes",
                complejidad="O(E log E)",
                advertencia=""
            )

    # 5. Orden de Dependencias / Orden Topológico (Kahn) -> Solo aplica a grafos dirigidos y sin pesos
    if (
        perfil.objetivo == "orden_dependencias"
        and perfil.dirigido
        and perfil.tipo_pesos == "sin_pesos"
    ):
        return DecisionAlgoritmica(
            algoritmo="Kahn",
            estructura="cola + grados de entrada",
            operacion_dominante="procesamiento de nodos con grado de entrada cero",
            complejidad="O(V+E)",
            advertencia=""
        )

    # 6. Fuera de alcance (Casos no contemplados en los algoritmos base estudiados)
    advertencias = []
    if perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "incluye_negativos":
        advertencias.append("Los caminos mínimos con pesos negativos requieren Bellman-Ford (fuera de alcance).")
    elif perfil.objetivo == "conexion_minima" and perfil.dirigido:
        advertencias.append("La conexión mínima en grafos dirigidos (Arborescencia Mínima) requiere Edmonds (fuera de alcance).")
    elif perfil.objetivo == "conexion_minima" and perfil.tipo_pesos == "sin_pesos":
        advertencias.append("La conexión mínima no está definida de forma estándar para grafos sin pesos (fuera de alcance).")
    elif perfil.objetivo == "orden_dependencias" and not perfil.dirigido:
        advertencias.append("El ordenamiento topológico requiere estrictamente que el grafo sea dirigido.")
    elif perfil.objetivo == "orden_dependencias" and perfil.tipo_pesos != "sin_pesos":
        advertencias.append("El ordenamiento topológico no contempla pesos en las aristas.")
    else:
        advertencias.append("No existe un algoritmo aplicable dentro de las estrategias estudiadas.")

    return DecisionAlgoritmica(
        algoritmo=None,
        estructura=None,
        operacion_dominante="",
        complejidad=None,
        advertencia=" ".join(advertencias)
    )


def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    """Indica si el algoritmo satisface objetivo y restricciones."""
    validar_perfil(perfil)
    if isinstance(algoritmo, bool) or not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser una cadena de texto (str).")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no estudiado: {algoritmo}")

    decision = seleccionar_estrategia(perfil)
    return decision.algoritmo == algoritmo


def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    """Explica por qué un algoritmo conocido no es la elección correcta."""
    validar_perfil(perfil)
    if isinstance(algoritmo, bool) or not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser una cadena de texto (str).")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no estudiado: {algoritmo}")

    decision = seleccionar_estrategia(perfil)

    # Si es el algoritmo correcto, confirmamos su operación dominante
    if decision.algoritmo == algoritmo:
        return f"El algoritmo {algoritmo} sí aplica para este perfil mediante la operación de {decision.operacion_dominante}."

    # Si el algoritmo propuesto es BFS pero el problema tiene pesos
    if algoritmo == "BFS" and perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "no_negativos":
        return (
            "BFS no es adecuado porque asume que el costo del camino depende únicamente del número de aristas "
            "(pesos uniformes). Para aristas con pesos no negativos se recomienda Dijkstra."
        )

    # Explicación genérica de descarte orientada a lo que sí se recomienda
    if decision.algoritmo is not None:
        return (
            f"El algoritmo {algoritmo} no es óptimo o correcto para este escenario. "
            f"Se recomienda usar {decision.algoritmo} ya que su estructura asociada "
            f"es {decision.estructura}."
        )
    
    return f"El algoritmo {algoritmo} no aplica porque el problema está fuera de nuestro alcance: {decision.advertencia}"


def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Contrasta una propuesta con la decisión recomendada."""
    validar_perfil(perfil)
    
    if isinstance(algoritmo, bool) or not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser un str.")
    if isinstance(estructura, bool) or not isinstance(estructura, str):
        raise TypeError("La estructura debe ser un str.")

    decision_optima = seleccionar_estrategia(perfil)
    errores = []

    # Si el problema está fuera de alcance
    if decision_optima.algoritmo is None:
        if perfil.tipo_pesos == "incluye_negativos" and perfil.objetivo == "camino_minimo":
            errores.append("No se acepta la propuesta: el problema incluye pesos negativos y está fuera de alcance.")
        else:
            errores.append(f"No se acepta la propuesta: {decision_optima.advertencia}")
        return False, errores

    # Si el problema está dentro de alcance, contrastamos algoritmo y estructura
    if decision_optima.algoritmo != algoritmo:
        errores.append(f"Algoritmo incorrecto. Se esperaba {decision_optima.algoritmo} pero se propuso {algoritmo}.")
    if decision_optima.estructura != estructura:
        errores.append(f"Estructura incorrecta. Se esperaba {decision_optima.estructura} pero se propuso {estructura}.")

    if errores:
        return False, errores
    
    return True, []


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