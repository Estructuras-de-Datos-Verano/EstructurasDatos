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
    if not isinstance(perfil.objetivo, str) or not isinstance(perfil.tipo_pesos, str):
        raise TypeError("El objetivo y tipo_pesos deben ser strings")
    if not isinstance(perfil.dirigido, bool):
        raise TypeError(f"dirigido debe ser un booleano, no {perfil.dirigido}")
        
    if perfil.objetivo not in OBJETIVOS:
        raise ValueError(f"Objetivo desconocido: {perfil.objetivo}")
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError(f"Tipo de pesos desconocido: {perfil.tipo_pesos}")

def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    """Elige una estrategia estudiada o documenta que ninguna aplica."""
    validar_perfil(perfil)
    
    if perfil.objetivo == "camino_minimo":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("BFS", "cola", "procesar por capas", "O(V+E)", "")
        elif perfil.tipo_pesos == "cero_uno":
            return DecisionAlgoritmica("0-1 BFS", "deque", "priorizar 0/1 frente/fondo", "O(V+E)", "")
        elif perfil.tipo_pesos == "no_negativos":
            return DecisionAlgoritmica("Dijkstra", "heap", "extraer menor distancia", "O((V+E) log V)", "")
        elif perfil.tipo_pesos == "incluye_negativos":
            return DecisionAlgoritmica(None, None, "N/A", None, "Ningún algoritmo estudiado resuelve camino mínimo con pesos negativos.")
            
    elif perfil.objetivo == "conexion_minima":
        if not perfil.dirigido and perfil.tipo_pesos in {"no_negativos", "incluye_negativos", "cero_uno"}:
            return DecisionAlgoritmica("Kruskal", "Union-Find", "unir componentes evitando ciclos", "O(E log E)", "")
        else:
            return DecisionAlgoritmica(None, None, "N/A", None, "Kruskal requiere un grafo no dirigido ponderado.")
            
    elif perfil.objetivo == "orden_dependencias":
        if perfil.dirigido and perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("Kahn", "cola + grados de entrada", "liberar grado de entrada cero", "O(V+E)", "")
        else:
            return DecisionAlgoritmica(None, None, "N/A", None, "Kahn requiere precedencias dirigidas sin pesos.")

def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    """Indica si el algoritmo satisface objetivo y restricciones."""
    if not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser un string")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo desconocido o no estudiado: {algoritmo}")
        
    decision = seleccionar_estrategia(perfil)
    return decision.algoritmo == algoritmo

def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    """Explica por qué un algoritmo conocido no es la elección correcta."""
    if not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser un string")
    if algoritmo not in ALGORITMOS:
        raise ValueError("Algoritmo no estudiado")
        
    decision = seleccionar_estrategia(perfil)
    
    if decision.algoritmo == algoritmo:
        return f"El algoritmo {algoritmo} sí aplica. Su operación dominante es {decision.operacion_dominante}."
        
    if algoritmo == "BFS":
        razon = "BFS minimiza el número de aristas asumiendo costo uniforme, no optimiza sumas de pesos variables."
    elif algoritmo == "0-1 BFS":
        razon = "0-1 BFS solo soporta dominios binarios exactos (0 y 1)."
    elif algoritmo == "Dijkstra":
        razon = "Dijkstra falla ante pesos negativos o busca caminos simples desde un origen, no conexiones globales ni órdenes topológicos."
    elif algoritmo == "Kruskal":
        razon = "Kruskal requiere grafos no dirigidos y busca el MST global, no caminos ni dependencias."
    elif algoritmo == "Kahn":
        razon = "Kahn requiere grafos dirigidos acíclicos para resolver órdenes de dependencias."
        
    if decision.algoritmo:
        recomendacion = f"Para este perfil se recomienda {decision.algoritmo}."
    else:
        recomendacion = "Ningún algoritmo estudiado aplica para este perfil."
        
    return f"{algoritmo} descartado: {razon} {recomendacion}"

def evaluar_propuesta(
    perfil: PerfilProblema,
    algoritmo: str,
    estructura: str,
) -> tuple[bool, list[str]]:
    """Contrasta una propuesta con la decisión recomendada."""
    decision = seleccionar_estrategia(perfil)
    errores = []
    
    if decision.algoritmo is None:
        errores.append(decision.advertencia)
        return False, errores
        
    if algoritmo != decision.algoritmo:
        errores.append(f"Algoritmo propuesto '{algoritmo}' incorrecto. Se esperaba '{decision.algoritmo}'.")
        
    if decision.estructura and estructura not in decision.estructura:
        errores.append(f"Estructura propuesta '{estructura}' incorrecta. Se esperaba '{decision.estructura}'.")
        
    return len(errores) == 0, errores