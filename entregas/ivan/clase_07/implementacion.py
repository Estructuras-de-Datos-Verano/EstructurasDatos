"""Código base para Nearest Smaller Values.

Problema principal:
CSES Problem Set - Nearest Smaller Values
https://cses.fi/problemset/task/1645/

Este archivo contiene firmas y docstrings para trabajar durante la Clase 07.
No contiene la solución completa.
"""

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

    #validar_lista(numeros)
    stack_pares = []
    respuestas = []
    for pos, val in enumerate(numeros, start=1):
        while stack_pares and stack_pares[-1][0]>=val:
            stack_pares.pop()
        if not stack_pares:
            respuestas.append(0)
        else:
            respuestas.append(stack_pares[-1][1])
        stack_pares.append((val, pos))
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