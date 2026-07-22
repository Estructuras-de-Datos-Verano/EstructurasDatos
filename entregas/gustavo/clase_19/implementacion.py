from __future__ import annotations
from collections.abc import Mapping, Sequence
from collections import deque

def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido eliminando duplicados e incluyendo vecinos implícitos."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping")
        
    normalizado = {}
    
    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, str):
            raise TypeError("Los nodos explícitos deben ser cadenas de texto")
        if not isinstance(vecinos, Sequence) or isinstance(vecinos, str):
            raise TypeError("La lista de adyacencia debe ser una secuencia válida, no un string")
        
        if nodo not in normalizado:
            normalizado[nodo] = []
        
        visitados = set()
        for vecino in vecinos:
            if not isinstance(vecino, str):
                raise TypeError("Los vecinos deben ser cadenas de texto")
            
            # Conservar orden de aparición estable y eliminar dependencias duplicadas
            if vecino not in visitados:
                visitados.add(vecino)
                normalizado[nodo].append(vecino)
            
            # Agregar el vecino implícito como nodo sin sucesores
            if vecino not in normalizado:
                normalizado[vecino] = []
                
    return normalizado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo basándose en las dependencias entrantes."""
    # 1. Normalizar para asegurar que existen todos los nodos (incluyendo implícitos) y no hay duplicados
    grafo_normalizado = normalizar_grafo_dirigido(grafo)
    
    # 2. Inicializar el contador de grados en 0 para todos los nodos válidos
    grados = {nodo: 0 for nodo in grafo_normalizado}
    
    # 3. Contar las aristas entrantes
    for vecinos in grafo_normalizado.values():
        for vecino in vecinos:
            grados[vecino] += 1
            
    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico (Kahn) o None si existe un ciclo."""
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(normalizado)
    
    # Encolar todos los nodos sin requisitos pendientes
    disponibles = deque(nodo for nodo, grado in grados.items() if grado == 0)
    orden = []
    
    while disponibles:
        actual = disponibles.popleft()
        orden.append(actual)
        
        for vecino in normalizado[actual]:
            grados[vecino] -= 1
            # Se encola el vecino en el momento exacto en que su grado llega a cero
            if grados[vecino] == 0:
                disponibles.append(vecino)
                
    # Detección de ciclos evaluando la cobertura del grafo procesado
    if len(orden) != len(normalizado):
        return None
        
    return orden


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido validando por propiedades."""
    normalizado = normalizar_grafo_dirigido(grafo)
    
    # Validar longitud y ausencia de repetidos
    if len(orden) != len(normalizado) or len(set(orden)) != len(orden):
        return False
        
    posiciones = {nodo: indice for indice, nodo in enumerate(orden)}
    
    # Validar que no haya nodos ajenos al grafo
    if set(posiciones.keys()) != set(normalizado.keys()):
        return False
        
    # Comprobar que para toda arista u -> v, u aparezca antes que v
    for u, vecinos in normalizado.items():
        for v in vecinos:
            if posiciones[u] >= posiciones[v]:
                return False
                
    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares (prerrequisito, curso) mediante nodos enteros."""
    if type(numero_cursos) is not int:
        raise TypeError("La cantidad de cursos debe ser un entero no booleano")
    if numero_cursos < 0:
        raise ValueError("La cantidad de cursos no puede ser negativa")
        
    # Inicializar el grafo normalizado usando strings para acoplarse al algoritmo base
    grafo = {str(i): [] for i in range(numero_cursos)}
    
    for par in prerrequisitos:
        if type(par) is not tuple or len(par) != 2:
            raise ValueError("Cada prerrequisito debe ser una tupla de longitud 2")
        
        u, v = par
        if type(u) is not int or type(v) is not int:
            raise TypeError("Los identificadores deben ser enteros")
        
        if not (0 <= u < numero_cursos) or not (0 <= v < numero_cursos):
            raise IndexError("Índice de curso fuera de rango")
            
        grafo[str(u)].append(str(v))
        
    resultado = orden_topologico(grafo)
    
    # Diferenciar un ciclo de un grafo válidamente ordenado
    if resultado is None:
        return None
        
    return [int(nodo) for nodo in resultado]


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    return ordenar_cursos(numero_cursos, prerrequisitos) is not None