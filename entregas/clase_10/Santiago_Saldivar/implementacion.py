"""Código base para recorridos de grafos.

Clase 10: descubrimiento de BFS y DFS mediante recorridos manuales,
grafos, pilas, colas y visualización.

Este archivo contiene firmas y docstrings para trabajar durante la clase.
No contiene soluciones completas.
"""

from __future__ import annotations
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

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
    if origen not in grafo:
        raise ValueError("Ese nodo no se encuentra en el grafo.")
    
    #Esta parte realizará un seguimiento de los nodos ya visitados.
    visitados = set([origen])
    #Esta otra es la cola que necesita el BFS. Iremos agregando los nodos visitados. y guardaremos el orden.
    cola = deque([origen]) #El primero es el origen.

    #Esta parte almacenará el orden. Es lo que va a regresar.
    orden_visita = []

    while cola: #Como la cola abre con el origen, no estará vacía.
        nodo_actual = cola.popleft()
        orden_visita.append(nodo_actual)
        #Sacamos el primer elemento de la lista, que será el que fue visitado con más antigüedad.
        #Lo guardamos en l alsita que regresaremos.

        #Revisamos todos los vecinos del nodo actual.
        for vecino in grafo[nodo_actual]: 
            #grafo[nodo_actual] es una lista cuya guardada en el diccionario cuya calve es el vecino.
            if vecino not in visitados:
                #A cada uno que no haya sido visitado, lo marcamos como visitado.
                #Así, no se vuelve a agregar a la cola.
                visitados.add(vecino)
                #Se agrega a la cola para después revisar sus vecinos.
                cola.append(vecino)
    
    return orden_visita



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

    if origen not in grafo:
        raise ValueError("No está en el grafo.")
    visitados = set()
    pila = [origen]
    orden_visita = []
    #Hasta aquí lo mismo.

    while pila:
        #Sacamos el último nodo agregado, el más profundo hasta el momento.
        nodo_actual = pila.pop()

        if nodo_actual not in visitados:
            #Lo marcamos visitado y lo ponemos en la lista que regresa.
            visitados.add(nodo_actual)
            orden_visita.append(nodo_actual)

        #Lo invierte para regresarlos en orden, porque el dfs se va como de atrá para adelante.
        for vecino in reversed(grafo[nodo_actual]):
            if vecino not in visitados:
                pila.append(vecino)
    return orden_visita

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
    if origen not in grafo:
        raise ValueError("No está en el grafo.")
    
    # Todo acá como hace rato.
    cola = deque([origen])
    visitados = set() 
    #Nodos que ya procesamos revisando sus vecinos. Ya los sacamos de la cola.
    descubiertos = set([origen]) 
    #Los ya visitados. Todos los que ya estuvieron en la cola.
    aristas_exploradas = []

    historial_pasos = []
    contador_paso = 1

    while cola:
        #Sacamos el nodo actual porque ya fue visitado.
        nodo_actual = cola.popleft()
        visitados.add(nodo_actual)

        # Exploramos los vecinos.
        for vecino in grafo[nodo_actual]: 
            if (nodo_actual, vecino) not in aristas_exploradas:
                #Registra la visita si no estaba ya.
                aristas_exploradas.append((nodo_actual, vecino))

            #Si es nuevo el vecino, lo guarda
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)

        estado_actual = {
            "paso" : contador_paso,
            "nodo_actual" : nodo_actual,
            "cola" : list(cola),
            "visitados" : list(visitados),
            "descubiertos" : list(descubiertos),
            "aristas_exploradas" : list(aristas_exploradas)
        }
        #Como es un bucle, el diccionario se irá actualizando.

        historial_pasos.append(estado_actual) 
        #Se va guardando la nueva versión para tener todas al final.

        contados_paso += 1
    
    return historial_pasos

            


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

    if origen not in grafo:
        raise ValueError("No está en el grafo.")
    
    # Lo mismo.
    pila = deque([origen])
    visitados = set()
    descubiertos = set([origen])
    aristas_exploradas = []

    historial_pasos = []
    contador_paso = 1

    while pila:
        #Hace pop a lo último, como suelen hacer las pilas...
        nodo_actual = pila.pop()

        # En DFS el nodo puede volver varias veces a la pila. 
        # Sólo se procesa si no ha sido visitado.

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explora los vecinos en orden inverso pporque el DFS se adelanta y se va para atrás.
            for vecino in reversed(grafo[nodo_actual]):
                #Registramos la exploración
                if (nodo_actual, vecino) not in aristas_exploradas:
                    aristas_exploradas.append((nodo_actual, vecino))

                # Si es la primera vez que se visita, se registra apropiadamente.
                if vecino not in visitados:
                    descubiertos.add(vecino)
                    pila.append(vecino)

            estado_actual = {
            "paso" : contador_paso,
            "nodo_actual" : nodo_actual,
            "pila" : list(pila),
            "visitados" : list(visitados),
            "descubiertos" : list(descubiertos),
            "aristas_exploradas" : list(aristas_exploradas)
            }
        #Como es un bucle, el diccionario se irá actualizando.

        historial_pasos.append(estado_actual) 
        #Se va guardando la nueva versión para tener todas al final.

        contados_paso += 1
    
    return historial_pasos

# EXPERIMENTO FALLIDO
#EXPERIMENTO FALLIDO
def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    #Guarda una imagen del grafo resaltando el orden de recorrido.


    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        G.add_node(nodo)
        for vecino in vecinos:
            G.add_edge(nodo, vecino)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nodos_totales = list(G.nodes)
    nodos_no_visitados = [n for n in nodos_totales if n not in recorrido]

    if nodos_no_visitados:
        nx.draw_networkx_nodes(
            G, pos, 
            nodelist=nodos_no_visitados, 
            node_color="#E0E0E0", 
            node_size=600
        )

    orden_indices = list(range(len(recorrido)))

    if recorrido:
        nx.draw_networkx_nodes(
            G, pos, 
            nodelist=recorrido, 
            node_color=orden_indices, 
            cmap=plt.cm.Blues,  # Degradado de azules (puedes cambiarlo por 'Purples', 'Greens', 'viridis')
            node_size=700,
            edgecolors="black"  # Borde negro para que resalten
        )
    nx.draw_networkx_edges(G, pos, edge_color="#888888", arrowsize=15, width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif", font_weight="bold")
    
    # Ajustes estéticos finales
    plt.title("Visualización del Recorrido del Grafo", fontsize=14, fontweight="bold")
    plt.axis("off") # Ocultamos los ejes X e Y de la gráfica
    
    # 7. Guardar la imagen en el disco y cerrar la figura para liberar memoria
    plt.savefig(ruta, format="png", bbox_inches="tight", dpi=300)
    plt.close()
