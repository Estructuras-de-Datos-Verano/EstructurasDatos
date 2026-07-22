from __future__ import annotations
from collections import deque


def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:

    visitados = set()
    cola = deque([origen])
    recorrido = []

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    cola.append(vecino)

    return recorrido

def registrar_bfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:

    visitados = set()
    descubiertos = {origen}  
    cola = deque([origen])
    historial = []
    paso = 1
    historial.append({
        "paso": paso,
        "nodo_actual": None,
        "cola": list(cola),
        "visitados": list(visitados),
        "descubiertos": list(descubiertos),
        "aristas_exploradas": []
    })
    paso += 1

    while cola:
        nodo_actual = cola.popleft()
        historial.append({
            "paso": paso,
            "nodo_actual": nodo_actual,
            "cola": list(cola),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": [],
        })
        paso += 1

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            historial.append({
                "paso": paso,
                "nodo_actual": nodo_actual,
                "cola": list(cola),
                "visitados": list(visitados),
                "descubiertos": list(descubiertos),
                "aristas_exploradas": [],
            })
            paso += 1

            aristas_del_nodo = []
            for vecino in grafo.get(nodo_actual, []):
                aristas_del_nodo.append((nodo_actual, vecino))
                
                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    cola.append(vecino)
                    
                    historial.append({
                        "paso": paso,
                        "nodo_actual": nodo_actual,
                        "cola": list(cola),
                        "visitados": list(visitados),
                        "descubiertos": list(descubiertos),
                        "aristas_exploradas": list(aristas_del_nodo),
                    })
                else:
                    historial.append({
                        "paso": paso,
                        "nodo_actual": nodo_actual,
                        "cola": list(cola),
                        "visitados": list(visitados),
                        "descubiertos": list(descubiertos),
                        "aristas_exploradas": list(aristas_del_nodo),
                    })
                paso += 1

    return historial

""" 
def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:

    visitados = set()
    pila = [origen]
    recorrido = []

    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in grafo.get(nodo, [])[::-1]:
                if vecino not in visitados:
                    pila.append(vecino)

    return recorrido """

def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    visitados = set()
    pila = [origen]
    recorrido = []

    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)
            vecinos = grafo.get(nodo, [])
            for vecino in reversed(vecinos):
                if vecino not in visitados:
                    pila.append(vecino)

    return recorrido


def registrar_dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    visitados = set()
    descubiertos = {origen}  
    cola = [origen]
    historial = []
    paso = 1
    historial.append({
        "paso": paso,
        "nodo_actual": None,
        "cola": list(cola),
        "visitados": list(visitados),
        "descubiertos": list(descubiertos),
        "aristas_exploradas": []
    })
    paso += 1

    while cola:
        nodo_actual = cola.pop(0)
        historial.append({
            "paso": paso,
            "nodo_actual": nodo_actual,
            "cola": list(cola),
            "visitados": list(visitados),
            "descubiertos": list(descubiertos),
            "aristas_exploradas": [],
        })
        paso += 1

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            historial.append({
                "paso": paso,
                "nodo_actual": nodo_actual,
                "cola": list(cola),
                "visitados": list(visitados),
                "descubiertos": list(descubiertos),
                "aristas_exploradas": [],
            })
            paso += 1

            aristas_del_nodo = []
            for vecino in grafo.get(nodo_actual, []):
                aristas_del_nodo.append((nodo_actual, vecino))
                
                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    cola.append(vecino)
                    
                    historial.append({
                        "paso": paso,
                        "nodo_actual": nodo_actual,
                        "cola": list(cola),
                        "visitados": list(visitados),
                        "descubiertos": list(descubiertos),
                        "aristas_exploradas": list(aristas_del_nodo),
                    })
                else:
                    historial.append({
                        "paso": paso,
                        "nodo_actual": nodo_actual,
                        "cola": list(cola),
                        "visitados": list(visitados),
                        "descubiertos": list(descubiertos),
                        "aristas_exploradas": list(aristas_del_nodo),
                    })
                paso += 1

    return historial


def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
    """Guarda una imagen del grafo resaltando el orden de recorrido."""

    raise NotImplementedError("Completa guardar_visualizacion_recorrido en tu entrega")