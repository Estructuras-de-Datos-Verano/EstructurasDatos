from __future__ import annotations


def validar_lista(numeros: list[int]) -> None:
    """Valida que ``numeros`` sea una lista no vacía de enteros."""

    if not isinstance(numeros, list):
        raise TypeError("numeros debe ser una lista")
    if not numeros:
        raise ValueError("numeros no debe estar vacía")
    if not all(isinstance(numero, int) for numero in numeros):
        raise TypeError("todos los elementos deben ser enteros")


def valores_menores_cercanos(numeros: list[int]) -> list[int]:
    """Resuelve el problema Nearest Smaller Values de CSES.

    Parámetros
    ----------
    numeros : list[int]
        Lista de números del problema.

    Regresa
    -------
    list[int]
        Lista de posiciones, indexadas desde 1, donde cada entrada indica
        la posición más cercana a la izquierda con valor menor. Si no existe,
        se coloca 0.

    Referencia
    ----------
    CSES Problem Set - Nearest Smaller Values
    https://cses.fi/problemset/task/1645/
    """

    validar_lista(numeros)

    pila = []
    respuestas = []
    for i, numero in enumerate(numeros):
        while pila and numeros[pila[-1]] >= numero:
            pila.pop()
        if len(pila) == 0:
            respuestas.append(0)
        else:
            respuestas.append(pila[-1] + 1)  # +1 para indexar desde 1
        
        pila.append(i)
            

    return respuestas  
        


def valores_mayores_cercanos(numeros: list[int]) -> list[int]:
    """Variante de Nearest Smaller Values.

    Para cada posición, regresa la posición más cercana a la izquierda
    con valor mayor. Si no existe, regresa 0.

    Esta función se incluye como ejercicio de generalización.
    """

    validar_lista(numeros)

    pila = []
    respuestas = []
    for i, numero in enumerate(numeros):
        while pila and numeros[pila[-1]] <= numero:
            pila.pop()
        if len(pila) == 0:
            respuestas.append(0)
        else:
            respuestas.append(pila[-1] + 1)  # +1 para indexar desde 1
        
        pila.append(i)
            

    return respuestas  