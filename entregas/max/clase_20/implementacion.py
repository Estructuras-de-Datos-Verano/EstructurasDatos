from __future__ import annotations
from dataclasses import dataclass

OBJETIVOS = frozenset({"camino_minimo", "conexion_minima", "orden_dependencias"})
TIPOS_PESO = frozenset({"sin_pesos", "cero_uno", "no_negativos", "incluye_negativos"})
ALGORITMOS = frozenset({"BFS", "0-1 BFS", "Dijkstra", "Kruskal", "Kahn"})

@dataclass(frozen=True)
class PerfilProblema:
    objetivo: str
    dirigido: bool
    tipo_pesos: str


@dataclass(frozen=True)
class DecisionAlgoritmica:
    algoritmo: str | None
    estructura: str | None
    operacion_dominante: str
    complejidad: str | None
    advertencia: str


def validar_perfil(perfil: PerfilProblema) -> None:
    if not isinstance(perfil, PerfilProblema):
        raise TypeError("El perfil debe ser una instancia de PerfilProblema.")
    if not isinstance(perfil.objetivo, str):
        raise TypeError("El objetivo debe ser un string.")
    if not isinstance(perfil.tipo_pesos, str):
        raise TypeError("El tipo_pesos debe ser un string.")
    if not isinstance(perfil.dirigido, bool):
        raise TypeError("La restricción 'dirigido' debe ser un valor booleano.")
        
    if perfil.objetivo not in OBJETIVOS:
        raise ValueError(f"Objetivo no reconocido: {perfil.objetivo}")
    if perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError(f"Tipo de pesos no reconocido: {perfil.tipo_pesos}")


def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    if perfil.objetivo == "camino_minimo":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("BFS", "cola", "procesar por capas", "O(V+E)", "")
        elif perfil.tipo_pesos == "cero_uno":
            return DecisionAlgoritmica("0-1 BFS", "deque", "priorizar 0/1 frente/fondo", "O(V+E)", "")
        elif perfil.tipo_pesos == "no_negativos":
            return DecisionAlgoritmica("Dijkstra", "heap", "extraer menor distancia", "O((V+E) log V)", "")
        elif perfil.tipo_pesos == "incluye_negativos":
            return DecisionAlgoritmica(None, None, "ninguna", None, "Los pesos negativos violan el invariante de Dijkstra.")

    elif perfil.objetivo == "conexion_minima":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica(None, None, "ninguna", None, "Kruskal requiere pesos para minimizar la conexión.")
        if perfil.dirigido:
            return DecisionAlgoritmica(None, None, "ninguna", None, "Kruskal requiere un grafo no dirigido.")
        else:
            return DecisionAlgoritmica("Kruskal", "Union-Find", "unir componentes con arista barata", "O(E log E)", "")

    elif perfil.objetivo == "orden_dependencias":
        if perfil.tipo_pesos != "sin_pesos":
            return DecisionAlgoritmica(None, None, "ninguna", None, "Kahn no utiliza pesos en sus operaciones.")
        if not perfil.dirigido:
            return DecisionAlgoritmica(None, None, "ninguna", None, "Kahn requiere precedencias dirigidas.")
        else:
            return DecisionAlgoritmica("Kahn", "cola + grados de entrada", "liberar grado de entrada cero", "O(V+E)", "")
            
    return DecisionAlgoritmica(None, None, "ninguna", None, "Perfil no aplicable a los algoritmos estudiados.")


def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    if not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser un string.")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo no soportado o inválido: {algoritmo}")
        
    if algoritmo == "BFS":
        return perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "sin_pesos"
    if algoritmo == "0-1 BFS":
        return perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "cero_uno"
    if algoritmo == "Dijkstra":
        return perfil.objetivo == "camino_minimo" and perfil.tipo_pesos == "no_negativos"
    if algoritmo == "Kruskal":
        return perfil.objetivo == "conexion_minima" and not perfil.dirigido and perfil.tipo_pesos != "sin_pesos"
    if algoritmo == "Kahn":
        return perfil.objetivo == "orden_dependencias" and perfil.dirigido and perfil.tipo_pesos == "sin_pesos"
        
    return False


def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    if not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser un string.")
    if algoritmo not in ALGORITMOS:
        raise ValueError("Algoritmo no soportado.")

    if es_aplicable(algoritmo, perfil):
        estrategia = seleccionar_estrategia(perfil)
        return f"{algoritmo} sí aplica. Operación dominante: {estrategia.operacion_dominante}."
        
    if algoritmo in {"BFS", "0-1 BFS", "Dijkstra"} and perfil.objetivo != "camino_minimo":
        return f"{algoritmo} se utiliza para optimizar caminos mínimos, no para {perfil.objetivo}."
    if algoritmo == "Kruskal" and perfil.objetivo != "conexion_minima":
        return "Kruskal busca la conexión global mínima, no caminos mínimos ni orden topológico."
    if algoritmo == "Kahn" and perfil.objetivo != "orden_dependencias":
        return "Kahn produce un orden de precedencias, no rutas ni conexiones globales."
        
    if perfil.objetivo == "camino_minimo":
        if algoritmo == "BFS" and perfil.tipo_pesos != "sin_pesos":
            ideal = seleccionar_estrategia(perfil).algoritmo
            recomendacion = f" Se recomienda {ideal}." if ideal else ""
            return f"BFS minimiza el número de aristas, pero ignora los pesos del modelo.{recomendacion}"
        if algoritmo == "0-1 BFS" and perfil.tipo_pesos not in {"sin_pesos", "cero_uno"}:
            return "0-1 BFS solo soporta dominios de prioridades 0 y 1."
        if algoritmo == "Dijkstra" and perfil.tipo_pesos == "incluye_negativos":
            return "Dijkstra no es aplicable porque los pesos negativos rompen su invariante."
            
    if algoritmo == "Kruskal":
        if perfil.dirigido:
            return "Kruskal asume conexiones no dirigidas para la red global mínima."
        if perfil.tipo_pesos == "sin_pesos":
            return "Kruskal requiere pesos para poder minimizar la conexión."
            
    if algoritmo == "Kahn":
        if not perfil.dirigido:
            return "Kahn requiere un grafo dirigido para establecer precedencias unívocas."
        if perfil.tipo_pesos != "sin_pesos":
            return "Kahn no requiere de pesos, solo analiza dependencias."

    return "No satisface el contrato."


def evaluar_propuesta(perfil: PerfilProblema, algoritmo: str, estructura: str) -> tuple[bool, list[str]]:
    if not isinstance(algoritmo, str) or not isinstance(estructura, str):
        raise TypeError("Algoritmo y estructura deben ser strings.")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo desconocido: {algoritmo}")

    estrategia_ideal = seleccionar_estrategia(perfil)
    errores = []
    
    if algoritmo != estrategia_ideal.algoritmo:
        errores.append(f"Algoritmo incorrecto o subóptimo: {explicar_descarte(algoritmo, perfil)}")
        
    if estructura != estrategia_ideal.estructura:
        errores.append(f"Estructura incorrecta: se esperaba '{estrategia_ideal.estructura}' porque la operación dominante es '{estrategia_ideal.operacion_dominante}'.")
        
    es_correcta = len(errores) == 0
    return es_correcta, errores


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
