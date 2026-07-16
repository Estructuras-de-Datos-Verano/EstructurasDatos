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
    descubiertos = {origen}
    orden_visitados = []
    while not len(cola) == 0:
        actual = cola.popleft()
        orden_visitados.append(actual)
        for vecino in grafo.get(actual, []):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
    return orden_visitados
        




    
    

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
    descubiertos = {origen}
    orden_visitados = []
    while len(pila) != 0:
        actual = pila.pop()
        orden_visitados.append(actual)
        for vecino in grafo.get(actual,[]):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
    return orden_visitados




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
    descubiertos = {origen}
    orden_visitados = []
    registro = [] 
    paso = 0
    while not len(cola) == 0:
        actual = cola.popleft()
        orden_visitados.append(actual)
        estado_actual = {
            "paso": paso,
            "nodo_actual": actual,
            "cola": list(cola),
            "visitados": list(orden_visitados),
            "descubiertos": set(descubiertos),
            "aristas_exploradas": [(actual,v) for v in grafo.get(actual,[]) if v not in descubiertos]
            }
        registro.append(estado_actual)
        for vecino in grafo.get(actual, []):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
        paso += 1
    return registro
    

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
    descubiertos = {origen}
    orden_visitados = []
    registro = []
    paso = 0
    while len(pila) != 0:
        actual = pila.pop()
        orden_visitados.append(actual)
        estado_actual = {
            "paso": paso,
            "nodo_actual": actual,
            "pila": list(pila),
            "visitados": list(orden_visitados),
            "descubiertos": set(descubiertos),
            "aristas_exploradas": [(actual,v) for v in grafo.get(actual,[]) if v not in descubiertos]
        }
        registro.append(estado_actual)
        for vecino in grafo.get(actual,[]):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
        paso += 1
    return registro
    


def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido."""

    raise NotImplementedError("Completa guardar_visualizacion_recorrido en tu entrega")
