from collections import deque
from copy import deepcopy
from collections.abc import Mapping

def normalizar_grafo_dirigido(grafo):

    if not isinstance(grafo, Mapping):
        raise TypeError("El grafo debe ser un diccionario.")
        
    normalizado = {}
    for nodo, vecinos in grafo.items():
       
        if not isinstance(nodo, str):
            raise TypeError("Los nodos deben ser cadenas de texto.")
        
  
        if not isinstance(vecinos, (list, tuple)):
            raise TypeError("Los vecinos deben ser una lista o tupla.")
            
        if nodo not in normalizado:
            normalizado[nodo] = []
            
        for vecino in vecinos:
         
            if not isinstance(vecino, str):
                raise TypeError("Los vecinos deben ser cadenas de texto.")
                
            if vecino not in normalizado:
                normalizado[vecino] = []
            
            if vecino not in normalizado[nodo]:
                normalizado[nodo].append(vecino)
                
    return normalizado

def grados_entrada(grafo):
    grados = {}

    for nodo, vecinos in grafo.items():
        if nodo not in grados:
            grados[nodo] = 0
        for vecino in set(vecinos):
            if vecino not in grados:
                grados[vecino] = 0
                
    for nodo, vecinos in grafo.items():
        for vecino in set(vecinos):
            grados[vecino] += 1
            
    return grados

def orden_topologico(grafo):
    normalizado = normalizar_grafo_dirigido(grafo)
    grados = grados_entrada(normalizado)
    disponibles = deque([nodo for nodo in normalizado if grados[nodo] == 0])
    orden = []
    
    while disponibles:
        actual = disponibles.popleft()
        orden.append(actual)
        for vecino in normalizado[actual]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                disponibles.append(vecino)
                
    if len(orden) != len(normalizado):
        return None
    return orden

def es_orden_topologico(grafo, orden):
    normalizado = normalizar_grafo_dirigido(grafo)
    if not orden or len(orden) != len(normalizado):
        return False
        
    posicion = {}
    for i, nodo in enumerate(orden):
        if nodo in posicion or nodo not in normalizado:
            return False
        posicion[nodo] = i
        
    for u in normalizado:
        for v in normalizado[u]:
            if posicion[u] >= posicion[v]:
                return False
    return True

def ordenar_cursos(numero_cursos, prerrequisitos):
   
    if type(numero_cursos) is bool or not isinstance(numero_cursos, int):
        raise TypeError("El número de cursos debe ser un número entero.")
        
    if numero_cursos < 0:
        raise ValueError("El número de cursos no puede ser negativo.")
        
    grafo = {str(i): [] for i in range(numero_cursos)}
    
    for par in prerrequisitos:
      
        if not isinstance(par, (list, tuple)):
            raise ValueError("Cada prerrequisito debe ser una tupla o lista.")
            
        if len(par) != 2:
            raise ValueError("El prerrequisito debe contener exactamente dos elementos.")
            
        pre, cur = par
       
        if type(pre) is bool or type(cur) is bool or not isinstance(pre, int) or not isinstance(cur, int):
            raise TypeError("Los prerrequisitos deben ser enteros.")
            
        if not (0 <= pre < numero_cursos and 0 <= cur < numero_cursos):
            raise IndexError("El índice del curso está fuera de los límites.")
            
        grafo[str(pre)].append(str(cur))
        
    resultado = orden_topologico(grafo)
    if resultado is None:
        return None
    return [int(x) for x in resultado]

def puede_completar_cursos(numero_cursos, prerrequisitos):
    return ordenar_cursos(numero_cursos, prerrequisitos) is not None