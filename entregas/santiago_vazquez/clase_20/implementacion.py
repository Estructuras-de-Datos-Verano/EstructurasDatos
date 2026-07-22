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
        raise TypeError()
    if type(perfil.dirigido) is not bool:
        raise TypeError()
    if type(perfil.objetivo) is not str or type(perfil.tipo_pesos) is not str:
        raise TypeError()
    if perfil.objetivo not in OBJETIVOS or perfil.tipo_pesos not in TIPOS_PESO:
        raise ValueError()

def validar_algoritmo(algoritmo: str) -> None:
    """Helper para reutilizar la validación de excepciones requerida por los tests."""
    if type(algoritmo) is not str:
        raise TypeError("El algoritmo debe ser un string")
    if algoritmo not in ALGORITMOS:
        raise ValueError(f"Algoritmo '{algoritmo}' no está dentro de los estudiados")

def seleccionar_estrategia(perfil: PerfilProblema) -> DecisionAlgoritmica:
    if perfil.objetivo == "camino_minimo":
        if perfil.tipo_pesos == "sin_pesos":
            return DecisionAlgoritmica("BFS", "cola", "procesar por capas", "O(V+E)", "")
        if perfil.tipo_pesos == "cero_uno":
           
            return DecisionAlgoritmica("0-1 BFS", "deque", "priorizar frente/fondo con 0/1", "O(V+E)", "")
        if perfil.tipo_pesos == "no_negativos":
            return DecisionAlgoritmica("Dijkstra", "heap", "extraer menor distancia", "O((V+E) log V)", "")
    if perfil.objetivo == "conexion_minima" and not perfil.dirigido and perfil.tipo_pesos != "sin_pesos":
        return DecisionAlgoritmica("Kruskal", "Union-Find", "unir componentes con arista barata", "O(E log E)", "")
    if perfil.objetivo == "orden_dependencias" and perfil.dirigido and perfil.tipo_pesos == "sin_pesos":
        
        return DecisionAlgoritmica("Kahn", "cola + grados de entrada", "liberar grado de entrada cero", "O(V+E)", "")
    
    return DecisionAlgoritmica(None, None, "ninguna", None, "Ningun algoritmo aplica")

def es_aplicable(algoritmo: str, perfil: PerfilProblema) -> bool:
 
    validar_algoritmo(algoritmo)
    estrategia = seleccionar_estrategia(perfil)
    return estrategia.algoritmo == algoritmo

def explicar_descarte(algoritmo: str, perfil: PerfilProblema) -> str:
    validar_algoritmo(algoritmo)
    estrategia = seleccionar_estrategia(perfil)
    
    if estrategia.algoritmo is None:
        return f"El perfil excede el alcance. {algoritmo} no cumple el contrato."
    
    
    if algoritmo == estrategia.algoritmo:
        return f"El algoritmo {algoritmo} sí aplica ya que permite {estrategia.operacion_dominante} eficientemente."
    
   
    return f"Se debe usar {estrategia.algoritmo}. El propuesto es incorrecto (ej. BFS solo minimiza el número de aristas, ignorando pesos)."

def evaluar_propuesta(perfil: PerfilProblema, algoritmo: str, estructura: str) -> tuple[bool, list[str]]:
    validar_perfil(perfil)
   
    validar_algoritmo(algoritmo)
    
    estrategia = seleccionar_estrategia(perfil)
    errores = []
    
    if estrategia.algoritmo is None:
       
        errores.append("Perfil fuera del alcance estudiado (no tolera pesos negativos)")
        return False, errores
        
    if estrategia.algoritmo != algoritmo:
        errores.append(f"Algoritmo incorrecto, se requiere {estrategia.algoritmo}")
    if estrategia.estructura != estructura:
        errores.append(f"Estructura incorrecta, se requiere {estrategia.estructura}")
        
    return len(errores) == 0, errores