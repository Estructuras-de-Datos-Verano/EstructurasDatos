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
    cola = deque([origen])
    visitados = set([origen])
    orden_recorrido = []
    while cola:
        nodo_actual = cola.popleft()
        orden_recorrido.append(nodo_actual)
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return orden_recorrido


def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    """Recorre un grafo usando Depth-First Search."""
    stack = [origen]
    visitados = set()
    orden_recorrido = []
    
    while stack:
        # 1. Sacamos el elemento más reciente (LIFO)
        nodo_actual = stack.pop()
        # 2. Verificamos SI YA FUE VISITADO en este punto (no antes)
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            orden_recorrido.append(nodo_actual)
            # 3. Metemos los vecinos a la pila.
            # Usamos reversed() para que el DFS visite en el orden natural
            # (ej: A -> B antes que A -> C, porque la pila saca el último en entrar).
            for vecino in reversed(grafo.get(nodo_actual, [])):
                if vecino not in visitados:
                    stack.append(vecino)
                    
    return orden_recorrido

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
    paso = 0
    nodo_actual = None
    cola = deque([origen])
    visitados = set([origen])
    descubiertos = set([origen])
    aristas_exploradas = []
    registro = []
    
    registro.append({
        "paso":paso,
        "nodo actual":nodo_actual,
        "cola":list(cola),
        "visitados":list(visitados),
        "descubiertos":list(descubiertos),
        "aristas exploradas":aristas_exploradas
    })
    while cola:
        paso += 1
        nodo_actual = cola.popleft()
        visitados.add(nodo_actual)
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
                aristas_exploradas.append((nodo_actual, vecino))
        registro.append(
            {
                "paso":paso,
                "nodo actual":nodo_actual,
                "cola":list(cola),
                "visitados":list(visitados),
                "descubiertos":list(descubiertos),
                "aristas exploradas":aristas_exploradas
            })
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

    paso = 0
    nodo_actual = None
    stack = []
    visitados = set([origen])
    descubiertos = set([origen])
    aristas_exploradas = []
    registro = []

    registro.append({
        "paso":paso,
        "nodo actual":nodo_actual,
        "cola":stack,
        "visitados":list(visitados),
        "descubiertos":list(descubiertos),
        "aristas exploradas":aristas_exploradas
    })
    while stack:
        paso += 1
        nodo_actual = stack.pop()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for vecino in grafo.get(nodo_actual, []):
                descubiertos.append(vecino)
                aristas_exploradas.append((nodo_actual, vecino))
        registro.append(
            {
                "paso":paso,
                "nodo actual":nodo_actual,
                "cola":stack,
                "visitados":list(visitados),
                "descubiertos":list(descubiertos),
                "aristas exploradas":aristas_exploradas
            }
        )
    return registro

def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    estado: dict,  # Cambiamos a dict para poder recibir: nodo_actual, cola, visitados...
    ruta: str = "entregas/clase_10/ivan/recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido."""
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)
            
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(5, 4))
    
    # Podemos usar el paso del estado para el título
    plt.title(f"Recorrido de grafo - Paso {estado.get('paso', 0)}")
    colores_nodos = []
    for nodo in G.nodes():
        if nodo == estado.get("nodo_actual"):
            colores_nodos.append("red")         # rojo: nodo actual
        elif nodo in estado.get("visitados", []):
            colores_nodos.append("green")       # verde: procesado
        elif nodo in estado.get("cola", []):
            colores_nodos.append("blue")        # azul: descubierto o pendiente
        else:
            colores_nodos.append("gray")        # gris: no visitado

    colores_aristas = []
    aristas_exploradas = estado.get("aristas_exploradas", [])
    
    for u, v in G.edges():
        # Verificamos ambas direcciones porque G es un grafo no dirigido
        if (u, v) in aristas_exploradas or (v, u) in aristas_exploradas:
            colores_aristas.append("orange")    # naranja: arista explorada
        else:
            colores_aristas.append("lightgray") # gris: arista pendiente
    nx.draw(
        G, pos, 
        with_labels=True, 
        node_color=colores_nodos, 
        edge_color=colores_aristas, 
        node_size=1000,
        width=2.5  # Hacemos las aristas más gruesas para que el naranja resalte
    )
    plt.axis("off")
    with open(ruta, "wb") as f:
        plt.savefig(f, format="png", bbox_inches="tight")  
    plt.close()  # Buena práctica: cierra la figura para liberar memoria

if __name__ == "__main__":
    # Ejemplo de uso
    grafo_ejemplo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    origen = "A"
    recorrido_bfs = bfs(grafo_ejemplo, origen)
    print("Recorrido BFS:", recorrido_bfs)
    
    recorrido_dfs = dfs(grafo_ejemplo, origen)
    print("Recorrido DFS:", recorrido_dfs)
    guardar_visualizacion_recorrido(grafo_ejemplo, registrar_bfs(grafo_ejemplo, origen)[0])
