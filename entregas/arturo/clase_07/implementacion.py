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
    """

    validar_lista(numeros)
    pila = []
    respuestas = []

    for i,x in enumerate(numeros):

        while pila and numeros[pila[-1]] >= x:
            pila.pop()
        if len(pila) == 0 :
            respuestas.append(0)
        else: 
            respuestas.append(pila[-1]+1)
        pila.append(i)
        
    return respuestas







def valores_mayores_cercanos(numeros: list[int]) -> list[int]:
    """Variante de Nearest Smaller Values.

    Para cada posición, regresa la posición más cercana a la izquierda
    con valor mayor. Si no existe, regresa 0.

    Esta función se incluye como ejercicio de generalización.
    """

    validar_lista(numeros)
    raise NotImplementedError("Reto opcional: completa valores_mayores_cercanos")


def resolver_desde_texto(texto: str) -> str:
    """Convierte entrada estilo CSES en salida de Nearest Smaller Values."""

    if not isinstance(texto, str):
        raise TypeError("texto debe ser una cadena")

    partes = texto.split()
    if not partes:
        raise ValueError("la entrada no debe estar vacía")

    n = int(partes[0])
    numeros = [int(parte) for parte in partes[1:]]
    if len(numeros) != n:
        raise ValueError("la cantidad de números no coincide con n")

    respuesta = valores_menores_cercanos(numeros)
    return " ".join(str(valor) for valor in respuesta) + "\n"