"""Funciones de apoyo para medir estructuras de datos en Python.

La idea de este modulo es mantener funciones pequenas y legibles para que
puedan usarse en notebooks, practicas y experimentos de clase.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterable
from random import Random
from time import perf_counter
from typing import Any


def generar_datos(n: int) -> list[int]:
    """Genera una lista reproducible de enteros para experimentos.

    Parametros
    ----------
    n:
        Cantidad de datos por generar. Debe ser un entero positivo.

    Regresa
    -------
    list[int]
        Lista de enteros con repeticiones. Las repeticiones son utiles para
        estudiar conteos con diccionarios y ``Counter``.
    """

    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    if n <= 0:
        raise ValueError("n debe ser positivo.")

    generador = Random(42)
    limite = max(10, n // 10) #division entera, limite es 10,000 para que solo haya numeros de a lo mas eso
    return [generador.randrange(limite) for _ in range(n)] 


def medir_tiempo(funcion: Callable[[], Any], repeticiones: int = 5) -> float:
    """Mide el tiempo promedio de ejecutar una funcion sin argumentos.

    Parametros
    ----------
    funcion:
        Funcion que se quiere medir. Se espera que no requiera argumentos.
    repeticiones:
        Numero de veces que se ejecutara la funcion.

    Regresa
    -------
    float
        Tiempo promedio en segundos.
    """

    if not callable(funcion):
        raise TypeError("funcion debe ser llamable.")
    if not isinstance(repeticiones, int):
        raise TypeError("repeticiones debe ser un entero.")
    if repeticiones <= 0:
        raise ValueError("repeticiones debe ser positivo.")

    tiempos: list[float] = []

    for _ in range(repeticiones):
        inicio = perf_counter()
        funcion()
        fin = perf_counter()
        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)


def buscar_en_lista(datos: Iterable[Any], objetivo: Any) -> bool:
    """Busca un valor recorriendo una coleccion como lista.

    Esta funcion usa el operador ``in`` sobre la coleccion recibida. Si
    ``datos`` es una lista, Python revisa elementos hasta encontrar el objetivo
    o hasta terminar la lista.
    """

    if datos is None:
        raise ValueError("datos no puede ser None.")

    return objetivo in datos #in es un for internamente


def buscar_en_conjunto(datos: set[Any], objetivo: Any) -> bool:
    """Busca un valor en un conjunto.

    Parametros
    ----------
    datos:
        Conjunto en el que se buscara. Se pide explicitamente un ``set`` para
        que el experimento mida busqueda en conjunto y no construccion del set.
    objetivo:
        Valor que se quiere encontrar.
    """

    if not isinstance(datos, set):
        raise TypeError("datos debe ser un set para esta medicion.")

    return objetivo in datos


def contar_con_diccionario(datos: Iterable[Any]) -> dict[Any, int]:
    """Cuenta frecuencias usando un diccionario comun.

    Regresa un diccionario donde las llaves son los valores observados y los
    valores son sus frecuencias.
    """

    if datos is None:
        raise ValueError("datos no puede ser None.")

    conteos: dict[Any, int] = {}

    for valor in datos:
        if valor not in conteos:
            conteos[valor] = 0
        conteos[valor] += 1

    return conteos


def contar_con_counter(datos: Iterable[Any]) -> Counter:
    """Cuenta frecuencias usando ``collections.Counter``.

    ``Counter`` es una clase especializada de Python para conteos. Internamente
    se comporta como un diccionario con metodos utiles para frecuencias.
    """

    if datos is None:
        raise ValueError("datos no puede ser None.")

    return Counter(datos)
