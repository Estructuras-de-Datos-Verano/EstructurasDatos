"""Código base documentado para Clase 15; no contiene la solución."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from minheaptiago import HeapMin

Peso = int | float
GrafoPonderado = Mapping[str, Sequence[tuple[str, Peso]]]


def dijkstra(
    grafo: GrafoPonderado,
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias mínimas y predecesores desde un origen.

    Parameters
    ----------
    grafo : GrafoPonderado
        Lista de adyacencia con pares ``(vecino, peso)`` no negativos.
    origen : str
        Nodo inicial.

    Returns
    -------
    tuple[dict[str, float], dict[str, str | None]]
        Distancias y predecesores para reconstruir caminos.

    Raises
    ------
    KeyError
        Si el origen no pertenece al grafo.
    ValueError
        Si aparece un peso negativo.

    Notes
    -----
    Completa esta firma en ``entregas/clase_15/nombre/implementacion.py``.
    """

    # Validaciones
    if origen not in grafo:
        raise KeyError("EL nodo no pertenece al grafo.")
    
    for u in grafo:
        for vecino, peso in grafo[u]:
            if peso < 0:
                raise ValueError("No puede ser negativo")
            
    # Le ponemos cada vértice su infinito, nomás mientras.
    # Porque no conocemos un camino aún.

    todos_los_nodos = set(grafo.keys())
    for u in grafo:
        for vecino, _ in grafo[u]:
            todos_los_nodos.add(vecino)


    distancias = {v: float('inf') for v in todos_los_nodos}

    predecesores = {v: None for v in todos_los_nodos}
    # Les asigna nada de momento. 
    # Luego le movemos.

    distancias[origen] = 0.0
    # La distanicia del origen al origen es 0.


    # Uso el HeapMin() de la clase pasada.
    cola_prioridad_d = HeapMin() #d de Dijskastra
    cola_prioridad_d.insertar((distancias[origen], origen))
    # Le metemos la distancia, cuya llave en el diccionario es el origen. Y aparte el origen.
    # Recibe una especie de par ordenado y así.

    # Seguiremos explorando nodos mietnras haya nodos que explorar.
    while not cola_prioridad_d.esta_vacio():
        
        """
        Sacamos el mínimo.    
        El MinHeap ya le sabe a eso.
        """

        distancia_actual, nodo_actual = cola_prioridad_d.extraer_min()
        """# Extraemos tanto la distancia como el nodo.

        # Si la distancia extraída es mayor a la que ya tenemos en el diccionario 
        # relacionada al nodo en que estamos, no hay que moverle.
        # ya tenemos una ruta superior. O sea superior de mejor.
        # Queremos rutas más chicas."""

        if distancia_actual > distancias[nodo_actual]:
            continue

        # Checamos los vecinos de nuestro nodo actual.
        if nodo_actual in grafo:
            for vecino, peso in grafo[nodo_actual]: # CHeca los vecinos
                nueva_distancia = distancia_actual + peso # Suma distancia

                if nueva_distancia < distancias[vecino]: # Guarda las menores y actualiza
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    cola_prioridad_d.insertar((nueva_distancia, vecino))


    return distancias, predecesores




def reconstruir_camino(
    predecesores: Mapping[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    """Reconstruye el camino del origen al destino o devuelve lista vacía."""

    # Validacion
    if destino not in predecesores:

        return []
    
    # Abro mi listita para llenarla al ratito.
    camino = []
    nodo_actual = destino

    # Iteramos de tras hacia delante.
    # Nos detenemos si llegamos a un nodo sin predecesor
    # (podría o no ser el origen)
    
    while nodo_actual is not None:

        # Lo metemos a la lista
        camino.append(nodo_actual)

        # Si llegamos al inicio
        # ya ahí muere

        if nodo_actual == origen:
            break

        # Como nos vamos para atrás, tenemos que 
        # actualizar. El predecesor será el que evaluamos,
        # es decir, el nodo_actual

        nodo_actual = predecesores[nodo_actual]

    # Si el nodo del final no es el origen, 
    # pues valió.
    # Regresa lista vacía.
    if not camino or camino [-1] != origen:
        return []
    
    # Le damos la vuelta

    camino_invertido = camino [::-1]

    return camino_invertido


def camino_minimo(
    grafo: GrafoPonderado,
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    """Devuelve el costo mínimo y el camino correspondiente."""

    # Esta función usa el Dijkstra

    distancias, predecesores = dijkstra(grafo, origen)

    # Validaciones
    if destino not in distancias:
        raise KeyError("El nodo no está en el grafo.")
    
    # Dijsktra nos regresa dos diccionarios.
    # De ellos, queremos que nos regrese las distancias entre origen y destino.
    costo = distancias[destino]

    # Checa que sí sea un número.
    # Si sigue marcado como infinito, no hay ningún camino.
    # Hay que tomar eso en cuenta.

    if costo == float('inf'):
        return float('inf'), []
    
    # Usamos la de hace rato para el caminito.

    camino = reconstruir_camino(predecesores, origen, destino)

    return costo, camino

