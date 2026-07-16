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
    while cola:
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
    while pila:
        actual = pila.pop()
        orden_visitados.append(actual)
        for vecino in grafo.get(actual, []):
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
    """
    cola = deque()
    cola.append(origen)
    descubiertos = {origen}
    visitados = set()
    registro = []
    paso = 0
    while cola:
        actual = cola.popleft()
        visitados.add(actual)
        estado_actual = {
            "paso": paso,
            "nodo_actual": actual,
            "cola": list(cola),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": [(actual, vecino) for vecino in grafo.get(actual, []) if vecino not in descubiertos]
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
    """

    pila = [origen]
    descubiertos = {origen}
    visitados = set()
    registro = []
    paso = 0
    while pila:
        actual = pila.pop()
        visitados.add(actual)
        estado_actual = {
            "paso": paso,
            "nodo_actual": actual,
            "pila": list(pila),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": [(actual, vecino) for vecino in grafo.get(actual, []) if vecino not in descubiertos]
        }
        registro.append(estado_actual)
        for vecino in grafo.get(actual, []):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
        paso += 1

    return registro