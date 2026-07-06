from __future__ import annotations


def valores_menores_cercanos(numeros: list[int]) -> list[int]:
    """Devuelve la posición del menor valor más cercano a la izquierda.

    Para cada posición, se busca el primer valor estrictamente menor a la
    izquierda. Si no existe, se devuelve 0. La implementación usa una pila
    monótona de candidatos.
    """

    if not isinstance(numeros, list):
        raise TypeError("numeros debe ser una lista")
    if not numeros:
        raise ValueError("numeros no debe estar vacía")
    if not all(isinstance(numero, int) for numero in numeros):
        raise TypeError("todos los elementos deben ser enteros")

    pila: list[tuple[int, int]] = []
    respuestas: list[int] = []

    for posicion_actual, valor_actual in enumerate(numeros, start=1):
        while pila and pila[-1][0] >= valor_actual:
            pila.pop()

        if not pila:
            respuestas.append(0)
        else:
            respuestas.append(pila[-1][1])

        pila.append((valor_actual, posicion_actual))

    return respuestas
