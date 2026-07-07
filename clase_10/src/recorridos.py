"""Código base para recorridos de grafos.

Clase 10: descubrimiento de BFS y DFS mediante recorridos manuales,
grafos, pilas, colas y visualización.

Este archivo contiene firmas y docstrings para trabajar durante la clase.
No contiene soluciones completas.
"""

from __future__ import annotations


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

    raise NotImplementedError("Completa bfs en tu entrega")


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

    raise NotImplementedError("Completa dfs en tu entrega")


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

    raise NotImplementedError("Completa registrar_bfs en tu entrega")


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

    raise NotImplementedError("Completa registrar_dfs en tu entrega")


def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido."""

    raise NotImplementedError("Completa guardar_visualizacion_recorrido en tu entrega")
