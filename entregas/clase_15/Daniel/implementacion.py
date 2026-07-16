"""
dijkstra debe:

validar el origen y todos los pesos;
inicializar distancias y predecesores;
usar heapq con pares (distancia, nodo);
ignorar candidaturas obsoletas antes de relajar;
no mutar el grafo;
incluir nodos que aparezcan únicamente como vecinos.
reconstruir_camino sigue predecesores desde destino, invierte el resultado y devuelve [] si no alcanza el origen. camino_minimo coordina ambas funciones.
"""

import heapq

def dijkstra(grafo, origen):
    # El punto de partida debe existir en nuestro mapa
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")

    # Reunimos todos los lugares para no dejar fuera a los que solo son destinos
    todos_los_nodos = set(grafo.keys())
    for vecinos in grafo.values():
        for vecino, peso in vecinos:
            if peso < 0:
                raise ValueError("Dijkstra no funciona con caminos de costo negativo.")
            todos_los_nodos.add(vecino)

    # Al principio, no conocemos ningún camino, así que la distancia es "infinita"
    distancias = {nodo: float('inf') for nodo in todos_los_nodos}
    predecesores = {nodo: None for nodo in todos_los_nodos}
    
    # Empezamos en casa: la distancia al origen siempre es cero
    distancias[origen] = 0.0
    
    # Usamos una cola de prioridad para revisar siempre el camino más prometedor (más barato)
    cola_prioridad = [(0.0, origen)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si ya encontramos un camino más corto antes, ignoramos esta opción vieja
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        # Revisamos a dónde podemos ir desde aquí
        vecinos = grafo.get(nodo_actual, [])
        for vecino, peso in vecinos:
            if peso < 0:
                raise ValueError("Dijkstra no funciona con caminos de costo negativo.")
                
            # Calculamos cuánto nos costaría llegar al vecino usando esta ruta
            distancia_candidata = distancia_actual + peso
            
            # Si este camino es mejor que el que ya conocíamos, lo actualizamos
            if distancia_candidata < distancias[vecino]:
                distancias[vecino] = distancia_candidata
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_candidata, vecino))
                
    return distancias, predecesores


def reconstruir_camino(predecesores, origen, destino):
    # Si el destino no está registrado, no hay nada que buscar
    if destino not in predecesores:
        return []
        
    # Si ya estamos en el destino, el viaje terminó antes de empezar
    if origen == destino:
        return [origen]
        
    camino = []
    nodo_actual = destino
    visitados = set()
    
    # Caminamos hacia atrás desde el destino siguiendo los rastros
    while nodo_actual is not None:
        # Si pasamos por el mismo lugar dos veces, hay un bucle sin salida
        if nodo_actual in visitados:
            return []
        visitados.add(nodo_actual)
        camino.append(nodo_actual)
        
        if nodo_actual == origen:
            break
        nodo_actual = predecesores.get(nodo_actual)
        
    # Si nunca pudimos conectar el camino de regreso al origen, es inalcanzable
    if camino[-1] != origen:
        return []
        
    # Volteamos el camino para que se lea desde el inicio hasta el final
    camino.reverse()
    return camino


def camino_minimo(grafo, origen, destino):
    if origen not in grafo:
        raise KeyError(f"El nodo origen '{origen}' no pertenece al grafo.")
        
    # Calculamos todos los caminos posibles desde el origen
    distancias, predecesores = dijkstra(grafo, origen)
    
    if destino not in distancias:
        raise KeyError(f"El nodo destino '{destino}' no pertenece al grafo.")
        
    costo_final = distancias[destino]
    
    # Si el costo es infinito, significa que es imposible llegar
    if costo_final == float('inf'):
        return float('inf'), []
        
    # Reconstruimos la ruta paso a paso
    ruta = reconstruir_camino(predecesores, origen, destino)
    return costo_final, ruta