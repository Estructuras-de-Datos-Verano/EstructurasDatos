"""Código base para recorridos de grafos.

Clase 10: descubrimiento de BFS y DFS mediante recorridos manuales,
grafos, pilas, colas y visualización.

Este archivo contiene firmas y docstrings para trabajar durante la clase.
No contiene soluciones completas.
"""

from __future__ import annotations
from collections import deque


def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    """Recorre un grafo usando Breadth-First Search.

    Parámetros
    ----------
    grafo : dict[str, list[str]]
        Representación del grafo como lista de adyacencia.
    origen : str
        Nodo inicial.

    Regresa
    -------
    list[str]
        Orden en que se visitan los nodos.

    Nota
    ----
    BFS explora por niveles y usa una cola.
    """
    cola = deque()
    cola.append(origen)
    descubiertos: set = {origen}
    lista = []
    while cola: 
        actual = cola.popleft()
        lista.append(actual)
        for vecino in grafo[actual]:
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
    return lista



def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    """Recorre un grafo usando Depth-First Search.

    Parámetros
    ----------
    grafo : dict[str, list[str]]
        Representación del grafo como lista de adyacencia.
    origen : str
        Nodo inicial.

    Regresa
    -------
    list[str]
        Orden en que se visitan los nodos.

    Nota
    ----
    DFS explora por profundidad y puede implementarse con pila.
    """
    pila = [origen]
    descubiertos: set = {origen}
    lista = []
    while pila:  
        actual = pila.pop()
        lista.append(actual)
        for vecino in reversed(grafo[actual]):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
    return lista

def registrar_bfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    """Ejecuta BFS y registra la ejecución paso a paso.

    Cada estado debe incluir:

    - paso;
    - nodo_actual;
    - cola;
    - visitados;
    - descubiertos;
    - aristas_exploradas;
    - linea_pseudocodigo.
    """
    cola = deque()
    cola.append(origen)
    visitados = []
    descubiertos: set = {origen}
    historial: list[dict] = []
    paso = 0
    step: dict = {} 
    aristas_exploradas: list[tuple] = []
    historial.append({"paso": 0,"nodo_actual": "ninguno","cola": list(cola),"visitados": "Vacío","descubiertos": set(descubiertos),"aristas_exploradas": "Vacío"})

    while cola: 
            paso += 1
            step["paso"] = paso
            actual = cola.popleft()
            visitados.append(actual)
            step["nodo_actual"] = actual
            for vecino in grafo[actual]:
                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    cola.append(vecino)
                    aristas_exploradas.append((actual, vecino))
            step["cola"] = list(cola)
            step["aristas_exploradas"] = tuple(aristas_exploradas)
            step["visitados"] = list(visitados)
            step["descubiertos"] = set(descubiertos)
            historial.append(step)
            step = {}
    return historial



def registrar_dfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    """Ejecuta DFS y registra la ejecución paso a paso.

    Cada estado debe incluir:

    - paso;
    - nodo_actual;
    - pila;
    - visitados;
    - descubiertos;
    - aristas_exploradas;
    - linea_pseudocodigo.
    """
    pila = [origen]
    visitados = []
    descubiertos: set = {origen}
    historial: list[dict] = []
    paso = 0
    step: dict = {} 
    aristas_exploradas: list[tuple] = []
    historial.append({"paso": 0,"nodo_actual": "ninguno","pila": list(pila),"visitados": "Vacío","descubiertos": set(descubiertos),"aristas_exploradas": "Vacío"})

    while pila: 
            paso += 1
            step["paso"] = paso
            actual = pila.pop()
            visitados.append(actual)
            step["nodo_actual"] = actual
            for vecino in reversed(grafo[actual]):
                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    pila.append(vecino)
                    aristas_exploradas.append((actual, vecino))
            step["pila"] = list(pila)
            step["aristas_exploradas"] = tuple(aristas_exploradas)
            step["visitados"] = list(visitados)
            step["descubiertos"] = set(descubiertos)
            historial.append(step)
            step = {}
    return historial



def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido."""

    raise NotImplementedError("Completa guardar_visualizacion_recorrido en tu entrega")