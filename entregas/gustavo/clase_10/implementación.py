from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    """Recorrido en anchura (por niveles). Usa una cola."""
    visitados = []
    descubiertos = set([origen])
    cola = deque([origen])

    while cola:
        nodo_actual = cola.popleft()
        visitados.append(nodo_actual)

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
                
    return visitados


def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    """Recorrido en profundidad. Usa una pila."""
    visitados = []
    descubiertos = set([origen])
    pila = [origen]

    while pila:
        nodo_actual = pila.pop()
        visitados.append(nodo_actual)

        # Recorremos los vecinos al revés para que los primeros
        # en la lista queden hasta arriba de la pila
        for vecino in reversed(grafo.get(nodo_actual, [])):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
                
    return visitados


def registrar_bfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    """Simula el BFS pero guardando el estado paso a pasito."""
    registro = []
    visitados = []
    descubiertos = [origen]
    cola = [origen]
    aristas_exploradas = []
    paso = 1

    while cola:
        nodo_actual = cola.pop(0)
        visitados.append(nodo_actual)

        registro.append({
            "paso": paso,
            "nodo_actual": nodo_actual,
            "cola": list(cola),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": list(aristas_exploradas),
            "linea_pseudocodigo": "procesar nodo"
        })
        
        paso += 1

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in descubiertos:
                descubiertos.append(vecino)
                cola.append(vecino)
                aristas_exploradas.append((nodo_actual, vecino))
                
    return registro


def registrar_dfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    """Simula el DFS pero guardando el estado paso a pasito."""
    registro = []
    visitados = []
    descubiertos = [origen]
    pila = [origen]
    aristas_exploradas = []
    paso = 1

    while pila:
        nodo_actual = pila.pop()
        visitados.append(nodo_actual)

        registro.append({
            "paso": paso,
            "nodo_actual": nodo_actual,
            "pila": list(pila),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": list(aristas_exploradas),
            "linea_pseudocodigo": "procesar nodo"
        })
        
        paso += 1

        for vecino in reversed(grafo.get(nodo_actual, [])):
            if vecino not in descubiertos:
                descubiertos.append(vecino)
                pila.append(vecino)
                aristas_exploradas.append((nodo_actual, vecino))
                
    return registro


def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Genera una imagen sencilla del grafo para visualizarlo."""
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        G.add_node(nodo)
        for vecino in vecinos:
            G.add_edge(nodo, vecino)

    # Posiciones fijas para los nodos
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(5, 4))
    nx.draw(
        G, pos, 
        with_labels=True, 
        node_color="#bfdbfe", 
        edge_color="#64748b", 
        node_size=1000
    )
    plt.axis("off")
    plt.savefig(ruta)
    plt.close()

if __name__ == "__main__":
    # Un grafo de prueba rápido sacado de la clase
    grafo_prueba = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }
    
    # Llamamos a la función para que genere y guarde el png
    guardar_visualizacion_recorrido(grafo_prueba, ["A", "B", "C", "D", "E", "F"])