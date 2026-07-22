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
    
    if type(perfil.objetivo) is not str:
        raise TypeError("El campo 'objetivo' debe ser de tipo str")
    if type(perfil.dirigido) is not bool:
        raise TypeError("El campo 'dirigido' debe ser exactamente un bool")
    if type(perfil.tipo_pesos) is not str:
        raise TypeError("El campo 'tipo_pesos' debe ser de tipo str")
        
    if perfil.objetivo not in OBJETIVOS:
        raise ValueError(f"Objetivo desconocido: {perfil.objetivo}")
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError(f"Tipo de pesos desconocido: {perfil.tipo_pesos}")


def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    """Elige una estrategia estudiada o documenta que ninguna aplica."""
    validar_perfil(perfil)
    
    obj = perfil.objetivo
    dirigido = perfil.dirigido
    pesos = perfil.tipo_pesos
    
    if obj == "camino_minimo":
        if pesos == "sin_pesos":
            return DecisionAlgoritmica(
                algoritmo="BFS",
                estructura="cola",
                operacion_dominante="procesar por capas",
                complejidad="O(V+E)",
                advertencia=""
            )
        elif pesos == "cero_uno":
            return DecisionAlgoritmica(
                algoritmo="0-1 BFS",
                estructura="deque",
                operacion_dominante="priorizar frente/fondo (0/1)",
                complejidad="O(V+E)",
                advertencia=""
            )
        elif pesos == "no_negativos":
            return DecisionAlgoritmica(
                algoritmo="Dijkstra",
                estructura="heap",
                operacion_dominante="extract menor distancia",
                complejidad="O((V+E) log V)",
                advertencia=""
            )
            
    elif obj == "conexion_minima":
        if not dirigido and (pesos == "no_negativos" or pesos == "incluye_negativos"):
            return DecisionAlgoritmica(
                algoritmo="Kruskal",
                estructura="Union-Find",
                operacion_dominante="unir componentes con arista barata",
                complejidad="O(E log E)",
                advertencia=""
            )
            
    elif obj == "orden_dependencias":
        if dirigido and pesos == "sin_pesos":
            return DecisionAlgoritmica(
                algoritmo="Kahn",
                estructura="cola + grados de entrada",
                operacion_dominante="liberar grado de entrada cero",
                complejidad="O(V+E)",
                advertencia=""
            )
            
    return DecisionAlgoritmica(
        algoritmo=None,
        estructura=None,
        operacion_dominante="",
        complejidad=None,
        advertencia=f"Fuera de alcance: No hay algoritmo estudiado para objetivo={obj}, dirigido={dirigido}, pesos={pesos}."
    )


def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    """Indica si el algoritmo satisface objetivo y restricciones."""
    if type(algoritmo) is not str:
        raise TypeError("El algoritmo debe ser una cadena de texto (str)")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no estudiado en el curso: {algoritmo}")
        
    validar_perfil(perfil)
    decision = seleccionar_estrategia(perfil)
    return decision.algoritmo == algoritmo


def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    """Explica por qué un algoritmo conocido no es la elección correcta."""
    if type(algoritmo) is not str:
        raise TypeError("El algoritmo debe ser un str")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no estudiado: {algoritmo}")
        
    validar_perfil(perfil)
    decision = seleccionar_estrategia(perfil)
    
    if decision.algoritmo == algoritmo:
        return f"El algoritmo {algoritmo} sí aplica porque resuelve mediante la operación de {decision.operacion_dominante}."
        
    if algoritmo == "BFS":
        msg = "BFS solo minimiza el número de aristas (asume costo uniforme)."
        if decision.algoritmo == "Dijkstra":
            msg += " Para pesos no negativos, se recomienda usar Dijkstra."
        elif decision.algoritmo == "0-1 BFS":
            msg += " Para pesos 0/1, se recomienda usar 0-1 BFS."
        return msg
        
    if algoritmo == "Dijkstra":
        if perfil.tipo_pesos == "incluye_negativos":
            return "Dijkstra no aplica porque el perfil incluye pesos negativos, lo que rompe su invariante de optimización."
        return "Dijkstra busca caminos mínimos acumulativos con costos no negativos, no conexiones globales ni ordenamientos."
        
    if algoritmo == "0-1 BFS":
        return "0-1 BFS está limitado estrictamente a un dominio de pesos discretos 0 y 1."
        
    if algoritmo == "Kruskal":
        return "Kruskal requiere un grafo no dirigido orientado a la conexión global mínima (MST)."
        
    if algoritmo == "Kahn":
        return "Kahn exige un orden de dependencias dirigido sin pesos basado en liberar grados de entrada."
        
    return f"El algoritmo {algoritmo} no cumple las restricciones de este perfil."


def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Contrasta una propuesta con la decisión recomendada."""
    validar_perfil(perfil)
    if type(algoritmo) is not str or type(estructura) is not str:
        raise TypeError("El algoritmo y la estructura deben ser cadenas de texto")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no estudiado: {algoritmo}")
        
    decision = seleccionar_estrategia(perfil)
    errores = []
    
    if decision.algoritmo is None:
        if perfil.tipo_pesos == "incluye_negativos" and perfil.objetivo == "camino_minimo":
            errores.append("Propuesta inválida: El perfil contiene pesos negativos para camino mínimo, que está fuera de alcance.")
        else:
            errores.append(decision.advertencia)
        return False, errores
        
    if algoritmo != decision.algoritmo:
        errores.append(f"Algoritmo incorrecto. Se esperaba '{decision.algoritmo}' pero se propuso '{algoritmo}'.")
        
    if estructura != decision.estructura:
        errores.append(f"Estructura incorrecta. Se esperaba '{decision.estructura}' pero se propuso '{estructura}'.")
        
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