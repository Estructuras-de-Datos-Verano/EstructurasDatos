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
    
    respuesta = []
    # La pila guardará tuplas simples: (valor, posicion_indexada_desde_1)
    pila: list[tuple[int, int]] = []
    
    for posicion, valor in enumerate(numeros, start=1):
        # Desapilamos mientras el tope sea mayor o igual al valor actual,
        # porque esos elementos pasados ya no sirven como "menor cercano".
        while pila and pila[-1][0] >= valor:
            pila.pop()
            
        # Si la pila quedó vacía, no hay ningún valor menor a la izquierda
        if not pila:
            respuesta.append(0)
        else:
            # El tope de la pila es el menor más cercano
            respuesta.append(pila[-1][1])
            
        # Guardamos el elemento actual como candidato para los futuros
        pila.append((valor, posicion))
        
    return respuesta


def valores_mayores_cercanos(numeros: list[int]) -> list[int]:
    """Variante de Nearest Smaller Values.

    Para cada posición, regresa la posición más cercana a la izquierda
    con valor mayor. Si no existe, regresa 0.

    Esta función se incluye como ejercicio de generalización.
    """
    validar_lista(numeros)
    
    respuesta = []
    pila: list[tuple[int, int]] = []
    
    for posicion, valor in enumerate(numeros, start=1):
        # La única diferencia: desapilamos mientras el tope sea MENOR o IGUAL.
        while pila and pila[-1][0] <= valor:
            pila.pop()
            
        if not pila:
            respuesta.append(0)
        else:
            respuesta.append(pila[-1][1])
            
        pila.append((valor, posicion))
        
    return respuesta


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