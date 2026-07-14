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