
# Primero lo primero, importamos todas las librerias necesarias.
#----------------------------------------------------------------------


from collections import deque
from pathlib import Path
import sys
from __future__ import annotations

raiz = Path.cwd()
if not (raiz / "src").exists() and (raiz.parent / "src").exists():
    raiz = raiz.parent
if str(raiz) not in sys.path:
    sys.path.insert(0, str(raiz))


# Luego copiamos y pegamos la función auxiliar
#----------------------------------------------------------------------


def validar_lista(numeros: list[int]) -> None:
    """Valida que ``numeros`` sea una lista no vacía de enteros."""

    if not isinstance(numeros, list):
        raise TypeError("numeros debe ser una lista")
    if not numeros:
        raise ValueError("numeros no debe estar vacía")
    if not all(isinstance(numero, int) for numero in numeros):
        raise TypeError("todos los elementos deben ser enteros")
    

# Luego implementamos la función principal
#----------------------------------------------------------------------


def valores_menores_cercanos(numeros: list[int]) -> list[int]:
    validar_lista(numeros) 
    
    resultado = []
    pila = deque() 
    
    for i, valor in enumerate(numeros):
        while pila and numeros[pila[-1]] >= valor:
            pila.pop()
        if pila:
            resultado.append(pila[-1] + 1)
        else:
            resultado.append(0)
        pila.append(i)
    return resultado


def valores_mayores_cercanos(numeros: list[int]) -> list[int]:
    validar_lista(numeros)
    resultado = []
    pila = deque()
    for i, valor in enumerate(numeros):
        while pila and numeros[pila[-1]] <= valor:
            pila.pop()
        if pila:
            resultado.append(pila[-1] + 1)
        else:
            resultado.append(0)
        pila.append(i)
    return resultado
