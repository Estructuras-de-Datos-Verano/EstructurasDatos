from typing import Optional, List

class PerfilProblema:
    def __init__(self, objetivo: str, dirigido: bool, tipo_pesos: str):
        # Asignación directa mediante __dict__ para simular inmutabilidad de forma nativa
        self.__dict__["objetivo"] = objetivo
        self.__dict__["dirigido"] = dirigido
        self.__dict__["tipo_pesos"] = tipo_pesos

    def __setattr__(self, name, value):
        raise AttributeError("PerfilProblema es inmutable.")

class DecisionAlgoritmica:
    def __init__(self, algoritmo: Optional[str], estructura: Optional[str], 
                 operacion_dominante: Optional[str] = None, complejidad: Optional[str] = None, 
                 advertencia: Optional[str] = ""):
        self.__dict__["algoritmo"] = algoritmo
        self.__dict__["estructura"] = estructura
        self.__dict__["operacion_dominante"] = operacion_dominante
        self.__dict__["complejidad"] = complejidad
        self.__dict__["advertencia"] = advertencia

    def __setattr__(self, name, value):
        raise AttributeError("DecisionAlgoritmica es inmutable.")

def validar_perfil(perfil: PerfilProblema) -> None:
    if not isinstance(perfil, PerfilProblema):
        raise TypeError("El perfil debe ser una instancia de PerfilProblema.")
    if not isinstance(perfil.objetivo, str) or not isinstance(perfil.tipo_pesos, str):
        raise TypeError("Los campos de texto deben ser cadenas.")
    if type(perfil.dirigido) is not bool:
        raise TypeError("El campo 'dirigido' debe ser exactamente un booleano.")

    if perfil.objetivo not in {"camino_minimo", "conexion_minima", "orden_dependencias"}:
        raise ValueError("Objetivo desconocido.")
    if perfil.tipo_pesos not in {"sin_pesos", "cero_uno", "no_negativos", "incluye_negativos"}:
        raise ValueError("Tipo de pesos desconocido.")

def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    validar_perfil(perfil)
    obj, dig, pesos = perfil.objetivo, perfil.dirigido, perfil.tipo_pesos

    if obj == "camino_minimo":
        if pesos == "sin_pesos":
            return DecisionAlgoritmica("BFS", "cola", "procesar por capas", "O(V+E)")
        elif pesos == "cero_uno":
            return DecisionAlgoritmica("0-1 BFS", "deque", "inserción 0/1 frente/fondo", "O(V+E)")
        elif pesos == "no_negativos":
            return DecisionAlgoritmica("Dijkstra", "heap", "extraer menor distancia", "O(E log V)")
        elif pesos == "incluye_negativos":
            return DecisionAlgoritmica(None, None, None, None, "Los pesos negativos invalidan el contrato de Dijkstra.")

    elif obj == "conexion_minima":
        if dig:
            return DecisionAlgoritmica(None, None, None, None, "Kruskal no soporta grafos dirigidos.")
        return DecisionAlgoritmica("Kruskal", "Union-Find", "unir componentes conexas sin ciclos", "O(E log E)")

    elif obj == "orden_dependencias":
        if not dig:
            return DecisionAlgoritmica(None, None, None, None, "El orden topológico requiere relaciones dirigidas.")
        if pesos != "sin_pesos":
            return DecisionAlgoritmica(None, None, None, None, "Kahn procesa precedencias puras y no modela costos.")
        return DecisionAlgoritmica("Kahn", "cola + grados de entrada", "liberar nodos con grado de entrada cero", "O(V+E)")

    return DecisionAlgoritmica(None, None, None, None, "Fuera de alcance.")

def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
    if not isinstance(algoritmo, str):
        raise TypeError("El algoritmo debe ser una cadena.")
    if algoritmo not in {"BFS", "0-1 BFS", "Dijkstra", "Kruskal", "Kahn"}:
        raise ValueError("Algoritmo no estudiado.")
    try:
        return seleccionar_estrategia(perfil).algoritmo == algoritmo
    except (TypeError, ValueError):
        return False

def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    validar_perfil(perfil)
    if es_aplicable(algoritmo, perfil):
        if algoritmo == "Kahn":
            return "El algoritmo sí aplica mediante el procesamiento de grado de entrada cero."
        return "El algoritmo sí aplica."
    
    if algoritmo == "BFS" and perfil.tipo_pesos == "no_negativos":
        return "BFS calcula rutas basándose únicamente en el número de aristas y falla ante pesos variables. Se recomienda usar Dijkstra."
    return f"El algoritmo {algoritmo} no cumple las restricciones del perfil."

def evaluar_propuesta(perfil: PerfilProblema, algoritmo_propuesto: Optional[str], estructura_propuesta: Optional[str]) -> tuple[bool, List[str]]:
    try:
        validar_perfil(perfil)
    except (TypeError, ValueError) as e:
        return False, [str(e)]
    
    decision = seleccionar_estrategia(perfil)
    if decision.algoritmo is None:
        return False, ["pesos negativos u otra restricción fuera de alcance"]
        
    errores = []
    if algoritmo_propuesto != decision.algoritmo:
        errores.append(f"Se esperaba Dijkstra pero se propuso {algoritmo_propuesto}")
    if estructura_propuesta != decision.estructura:
        errores.append(f"Se esperaba heap pero se propuso {estructura_propuesta}")
        
    return (len(errores) == 0, errores)