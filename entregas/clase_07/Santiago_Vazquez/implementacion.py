from __future__ import annotations

def validar_lista(numeros: list[int]) -> None:
    if not isinstance(numeros, list):
        raise TypeError("numeros debe ser una lista")
    if not numeros:
        raise ValueError("numeros no debe estar vacía")
    if not all(isinstance(numero, int) for numero in numeros):
        raise TypeError("todos los elementos deben ser enteros")

def valores_menores_cercanos(numeros: list[int]) -> list[int]:
    
    validar_lista(numeros)
    

    pila: list[tuple[int, int]] = []
    respuesta: list[int] = []
    
    for indice_actual, valor_actual in enumerate(numeros, start=1):

        while pila and pila[-1][0] >= valor_actual:
            pila.pop()
            
        if not pila:
            respuesta.append(0)
        else:
            respuesta.append(pila[-1][1])
            
        
        pila.append((valor_actual, indice_actual))
        
    return respuesta