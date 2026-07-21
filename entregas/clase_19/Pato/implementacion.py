from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence


def normalizar_grafo_dirigido(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, list[str]]:
    """Copia y normaliza un grafo dirigido."""
    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un Mapping.")

    normalizado: dict[str, list[str]] = {}

    for origen, destinos in grafo.items():
        if type(origen) is not str:
            raise TypeError("Los nodos origen deben ser strings.")
        if not isinstance(destinos, Sequence) or isinstance(destinos, (str, bytes)):
            raise TypeError("Las adyacencias deben ser secuencias (no strings).")

        if origen not in normalizado:
            normalizado[origen] = []

        for destino in destinos:
            if type(destino) is not str:
                raise TypeError("Los vecinos deben ser strings.")
            
            # Eliminamos duplicados manteniendo el orden estable
            if destino not in normalizado[origen]:
                normalizado[origen].append(destino)
                
            # Agregamos los vecinos implícitos
            if destino not in normalizado:
                normalizado[destino] = []

    return normalizado


def grados_entrada(
    grafo: Mapping[str, Sequence[str]],
) -> dict[str, int]:
    """Calcula el grado de entrada de cada nodo."""
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = {nodo: 0 for nodo in normalizado}

    for origen, destinos in normalizado.items():
        for destino in destinos:
            grados[destino] += 1

    return grados


def orden_topologico(
    grafo: Mapping[str, Sequence[str]],
) -> list[str] | None:
    """Devuelve un orden topológico o ``None`` si existe un ciclo."""
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(normalizado)

    # Encolamos inicialmente los que tienen grado 0 (sin prerrequisitos)
    cola = deque([nodo for nodo, grado in grados.items() if grado == 0])
    orden = []

    while cola:
        actual = cola.popleft()
        orden.append(actual)

        for vecino in normalizado[actual]:
            grados[vecino] -= 1
            # Se encola justo cuando el grado llega a cero
            if grados[vecino] == 0:
                cola.append(vecino)

    # Si hay un ciclo (parcial o total), la cantidad no coincidirá
    if len(orden) == len(normalizado):
        return orden
        
    return None


def es_orden_topologico(
    grafo: Mapping[str, Sequence[str]],
    orden: Sequence[str],
) -> bool:
    """Comprueba si una secuencia es un orden topológico válido."""
    normalizado = normalizar_grafo_dirigido(grafo)
    
    # Exige cobertura total y ausencia de repetidos
    if len(orden) != len(normalizado) or len(set(orden)) != len(orden):
        return False
        
    if set(orden) != set(normalizado.keys()):
        return False

    posiciones = {nodo: indice for indice, nodo in enumerate(orden)}

    # Verifica que u se ejecute siempre antes que v
    for origen, destinos in normalizado.items():
        for destino in destinos:
            if posiciones[origen] >= posiciones[destino]:
                return False

    return True


def ordenar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> list[int] | None:
    """Ordena cursos usando pares ``(prerrequisito, curso)``."""
    if type(numero_cursos) is not int:
        raise TypeError("La cantidad de cursos debe ser un entero.")
    if numero_cursos < 0:
        raise ValueError("La cantidad de cursos no puede ser negativa.")

    # Inicializamos el grafo con todos los cursos posibles (incluyendo aislados)
    grafo: dict[str, list[str]] = {str(i): [] for i in range(numero_cursos)}

    for par in prerrequisitos:
        if type(par) not in (tuple, list) or len(par) != 2:
            raise ValueError("Las dependencias deben ser tuplas de 2 elementos.")
            
        u, v = par
        # Evitamos aceptar booleanos filtrando por tipo estricto
        if type(u) is not int or type(v) is not int:
            raise TypeError("Los cursos deben indicarse con enteros.")
            
        if not (0 <= u < numero_cursos) or not (0 <= v < numero_cursos):
            raise IndexError("Índice de curso fuera de rango.")

        grafo[str(u)].append(str(v))

    orden = orden_topologico(grafo)
    
    if orden is None:
        return None
        
    return [int(x) for x in orden]


def puede_completar_cursos(
    numero_cursos: int,
    prerrequisitos: list[tuple[int, int]],
) -> bool:
    """Indica si todos los cursos pueden completarse."""
    return ordenar_cursos(numero_cursos, prerrequisitos) is not None


__all__ = [
    "normalizar_grafo_dirigido",
    "grados_entrada",
    "orden_topologico",
    "es_orden_topologico",
    "ordenar_cursos",
    "puede_completar_cursos",
]

