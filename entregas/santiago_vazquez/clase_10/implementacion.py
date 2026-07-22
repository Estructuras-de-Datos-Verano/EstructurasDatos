from __future__ import annotations
import os
import matplotlib.pyplot as plt
import networkx as nx

def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    
    if origen not in grafo:
        return []
        
    cola = [origen]
    descubiertos = {origen}
    visitados_orden = []
    
    while cola:
        actual = cola.pop(0)  # FIFO
        visitados_orden.append(actual)
        
        for vecino in grafo[actual]:
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
                
    return visitados_orden

    

def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    if origen not in grafo:
        return []
        
    pila = [origen]
    descubiertos = {origen}
    visitados_orden = []
    
    while pila:
        actual = pila.pop()  
        visitados_orden.append(actual)
        
        for vecino in reversed(grafo[actual]):
            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
                
    return visitados_orden


def registrar_bfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    if origen not in grafo:
        return []

    historial = []
    cola = [origen]
    descubiertos = {origen}
    visitados = []
    aristas_exploradas = []
    paso = 0

    
    historial.append({
        "paso": paso,
        "nodo_actual": None,
        "cola": list(cola),
        "visitados": list(visitados),
        "descubiertos": list(descubiertos),
        "aristas_exploradas": list(aristas_exploradas),
        "linea_pseudocodigo": "inicializacion"
        })

    while cola:
        paso += 1
        actual = cola.pop(0)
        visitados.append(actual)

        historial.append({
            "paso": paso,
            "nodo_actual": actual,
            "cola": list(cola),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": list(aristas_exploradas),
            "linea_pseudocodigo": "visitar actual"
        })

        for vecino in grafo[actual]:
            
            if (actual, vecino) not in aristas_exploradas and (vecino, actual) not in aristas_exploradas:
                aristas_exploradas.append((actual, vecino))

            if vecino not in descubiertos:
                descubiertos.add(vecino)
                cola.append(vecino)
                
                historial.append({
                    "paso": paso,
                    "nodo_actual": actual,
                    "cola": list(cola),
                    "visitados": list(visitados),
                    "descubiertos": list(descubiertos),
                    "aristas_exploradas": list(aristas_exploradas),
                    "linea_pseudocodigo": "marcar y encolar"
                })
                
    return historial


def registrar_dfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    """Ejecuta DFS y registra la ejecución paso a paso."""
    if origen not in grafo:
        return []

    historial = []
    pila = [origen]
    descubiertos = {origen}
    visitados = []
    aristas_exploradas = []
    paso = 0

    historial.append({
        "paso": paso,
        "nodo_actual": None,
        "pila": list(pila),
        "visitados": list(visitados),
        "descubiertos": list(descubiertos),
        "aristas_exploradas": list(aristas_exploradas),
        "linea_pseudocodigo": "inicializacion"
    })

    while pila:
        paso += 1
        actual = pila.pop()
        visitados.append(actual)

        historial.append({
            "paso": paso,
            "nodo_actual": actual,
            "pila": list(pila),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": list(aristas_exploradas),
            "linea_pseudocodigo": "visitar actual"
        })

        for vecino in reversed(grafo[actual]):
            if (actual, vecino) not in aristas_exploradas and (vecino, actual) not in aristas_exploradas:
                aristas_exploradas.append((actual, vecino))

            if vecino not in descubiertos:
                descubiertos.add(vecino)
                pila.append(vecino)
                
                historial.append({
                    "paso": paso,
                    "nodo_actual": actual,
                    "pila": list(pila),
                    "visitados": list(visitados),
                    "descubiertos": list(descubiertos),
                    "aristas_exploradas": list(aristas_exploradas),
                    "linea_pseudocodigo": "marcar y apilar"
                })
                
    return historial

    

def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido usando NetworkX."""
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)
            
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)  
    
    color_map = []
    for nodo in G.nodes():
        if nodo in recorrido:
            
            color_map.append(recorrido.index(nodo))
        else:
            color_map.append(-1)  
            
    
    nx.draw_networkx_nodes(
        G, pos, 
        node_color=color_map, 
        cmap=plt.cm.Blues, 
        node_size=700, 
        edgecolors="black"
    )
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6)
    
    
    etiquetas = {nodo: f"{nodo}\n({recorrido.index(nodo)+1})" if nodo in recorrido else nodo for nodo in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=10, font_weight="bold")
    
    plt.title("Visualización del Recorrido (Nodo e Índice de Visita)")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(ruta, format="png", dpi=300)
    plt.close()

def simular_pasos_recorrido(grafo: dict[str, list[str]], origen: str, base_ruta: str = "pasos_recorrido"):
    """Ejecuta BFS y usa la función original para guardar imágenes de cada paso."""
    if not os.path.exists(base_ruta):
        os.makedirs(base_ruta)

    cola = [origen]
    visitados = {origen}
    historial_recorrido = []
    paso = 0

    # Guardar estado inicial (Paso 0)
    guardar_visualizacion_recorrido(grafo, list(historial_recorrido), f"{base_ruta}/paso_{paso}.png")

    while cola:
        actual = cola.pop(0)
        historial_recorrido.append(actual)
        
        # Guardamos foto cada vez que un nodo se vuelve oficialmente visitado
        paso += 1
        guardar_visualizacion_recorrido(grafo, list(historial_recorrido), f"{base_ruta}/paso_{paso}.png")

        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

# --- BLOQUE DE EJECUCIÓN CON EL GRAFO DE LA CLASE ---
if __name__ == "__main__":
    grafo_clase_10 = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"]
    }
    
    print("Generando simulación paso a paso con tu función original...")
    simular_pasos_recorrido(grafo_clase_10, "A")
    print("¡Listo! En la carpeta 'pasos_recorrido/' tienes las imágenes en orden secuencial.")
