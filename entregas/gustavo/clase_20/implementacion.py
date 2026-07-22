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
    if not isinstance(perfil, PerfilProblema):
        raise TypeError("El perfil debe ser una instancia de PerfilProblema")
    
    if type(perfil.objetivo) is not str or type(perfil.tipo_pesos) is not str:
        raise TypeError("Los atributos objetivo y tipo_pesos deben ser cadenas de texto (str)")
    
    if type(perfil.dirigido) is not bool:
        raise TypeError("El atributo dirigido debe ser un valor booleano (bool)")
        
    if perfil.objetivo not in OBJETIVOS:
        raise ValueError(f"Objetivo desconocido: {perfil.objetivo}")
        
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError(f"Tipo de pesos desconocido: {perfil.tipo_pesos}")

def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    """Elige una estrategia estudiada o documenta que ninguna aplica."""
    if perfil.objetivo == "camino_minimo":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("BFS", "cola", "procesar por capas", "O(V+E)", "")
        elif perfil.tipo_pesos == "cero_uno":
            return DecisionAlgoritmica("0-1 BFS", "deque", "priorizar frente/fondo para 0/1", "O(V+E)", "")
        elif perfil.tipo_pesos == "no_negativos":
            return DecisionAlgoritmica("Dijkstra", "heap", "extraer menor distancia", "O((V+E) log V)", "")
        elif perfil.tipo_pesos == "incluye_negativos":
            return DecisionAlgoritmica(None, None, "N/A", None, "Contrato violado: Dijkstra no admite pesos negativos.")

    elif perfil.objetivo == "conexion_minima":
        if not perfil.dirigido and perfil.tipo_pesos in {"no_negativos", "incluye_negativos"}:
            return DecisionAlgoritmica("Kruskal", "Union-Find", "unir componentes con arista barata", "O(E log E)", "")
        else:
            return DecisionAlgoritmica(None, None, "N/A", None, "Fuera de alcance: Kruskal requiere un grafo no dirigido y pesos para funcionar correctamente.")

    elif perfil.objetivo == "orden_dependencias":
        if perfil.dirigido and perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("Kahn", "cola + grados de entrada", "liberar grado de entrada cero", "O(V+E)", "")
        else:
            return DecisionAlgoritmica(None, None, "N/A", None, "Fuera de alcance: Kahn requiere grafo dirigido y sin pesos.")

    return DecisionAlgoritmica(None, None, "N/A", None, "Perfil fuera del alcance estudiado.")

def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    """Indica si el algoritmo satisface objetivo y restricciones."""
    if type(algoritmo) is not str:
        raise TypeError("El algoritmo debe ser una cadena de texto (str)")
    if algoritmo not in ALGORITMOS:
        raise ValueError("Algoritmo no estudiado")

    decision = seleccionar_estrategia(perfil)
    return decision.algoritmo == algoritmo

def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    """Explica por qué un algoritmo conocido no es la elección correcta."""
    if type(algoritmo) is not str:
        raise TypeError("El algoritmo debe ser una cadena de texto (str)")
    if algoritmo not in ALGORITMOS:
        raise ValueError("Algoritmo no estudiado")

    decision = seleccionar_estrategia(perfil)
    
    if decision.algoritmo == algoritmo:
        return f"El algoritmo {algoritmo} sí aplica para este problema. Su operación dominante es {decision.operacion_dominante}."

    if decision.algoritmo is None:
        return f"El algoritmo {algoritmo} se descarta porque el problema está fuera del alcance: {decision.advertencia}"

    if algoritmo == "BFS":
        return f"BFS minimiza el número de aristas, pero no modela adecuadamente estos pesos. Se recomienda {decision.algoritmo}."
    elif algoritmo == "0-1 BFS":
        return f"0-1 BFS solo admite pesos en el dominio {{0,1}}. Se recomienda {decision.algoritmo}."
    elif algoritmo == "Dijkstra":
        return f"Dijkstra optimiza caminos mínimos desde un origen, lo cual no empata con este dominio u objetivo. Se recomienda {decision.algoritmo}."
    elif algoritmo == "Kruskal":
        return f"Kruskal busca conectar globalmente mediante un MST en grafos no dirigidos. Se recomienda {decision.algoritmo}."
    elif algoritmo == "Kahn":
        return f"Kahn ordena dependencias dirigidas secuencialmente. Se recomienda {decision.algoritmo}."

    return f"Se descarta {algoritmo} por violar el contrato. La elección correcta es {decision.algoritmo}."

def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Contrasta una propuesta con la decisión recomendada."""
    errores = []
    decision = seleccionar_estrategia(perfil)

    if decision.algoritmo is None:
        errores.append(f"Propuesta rechazada. El problema está fuera del alcance estudiado: {decision.advertencia}")
        return False, errores

    valida = True
    if decision.algoritmo != algoritmo:
        valida = False
        errores.append(f"Algoritmo incorrecto. Esperado: {decision.algoritmo}, Propuesto: {algoritmo}")

    if decision.estructura != estructura:
        valida = False
        errores.append(f"Estructura incorrecta. Esperada: {decision.estructura}, Propuesta: {estructura}")

    return valida, errores

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