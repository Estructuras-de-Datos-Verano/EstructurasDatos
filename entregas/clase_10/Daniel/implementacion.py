def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    cola = [origen]
    visitados = [origen]

    while cola:
        actual = cola.pop(0)
        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return visitados

def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    pila = [origen]
    visitados = [origen]

    while pila:
        actual = pila.pop()
        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.append(vecino)
                pila.append(vecino)

    return visitados
def registrar_bfs(grafo, origen): 
    visitados = bfs(grafo, origen)
    print(f"Recorrido BFS desde {origen}: {visitados}") 

    
def registrar_dfs(grafo, origen): 
    visitados = dfs(grafo, origen)
    print(f"Recorrido DFS desde {origen}: {visitados}")