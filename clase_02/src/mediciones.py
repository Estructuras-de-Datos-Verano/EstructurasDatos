"""Funciones reutilizables para comparar estructuras de datos.

El objetivo de este modulo es apoyar experimentos pequenos de clase. El codigo
prioriza claridad sobre sofisticacion para que sea facil discutirlo en grupo.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterable, Sequence
from random import Random
from time import perf_counter
from typing import Any


def generar_datos(n: int, semilla: int = 42) -> list[int]:
    """Genera una lista reproducible de enteros con repeticiones.

    Parametros
    ----------
    n:
        Cantidad de datos por generar. Debe ser un entero positivo.
    semilla:
        Valor usado para hacer reproducible la generacion.

    Regresa
    -------
    list[int]
        Lista de enteros. Incluye repeticiones para poder estudiar conteos.
    """

    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    if n <= 0:
        raise ValueError("n debe ser positivo.")
    if not isinstance(semilla, int):
        raise TypeError("semilla debe ser un entero.")

    generador = Random(semilla)
    limite = max(10, n // 10)
    return [generador.randrange(limite) for _ in range(n)]


def medir_tiempo(funcion: Callable[[], Any], repeticiones: int = 10) -> float:
    """Mide el tiempo promedio de ejecutar una funcion sin argumentos.

    Se recomienda usar varias repeticiones porque una sola medicion puede verse
    afectada por ruido del sistema operativo, otros procesos o variaciones del
    interprete.
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
    """Busca ``objetivo`` en una coleccion usando pertenencia tipo lista."""

    if datos is None:
        raise ValueError("datos no puede ser None.")

    return objetivo in datos


def buscar_en_conjunto(datos: set[Any], objetivo: Any) -> bool:
    """Busca ``objetivo`` en un conjunto.

    La funcion exige recibir un ``set`` para medir la consulta de pertenencia y
    no mezclarla con el costo de construir el conjunto.
    """

    if not isinstance(datos, set):
        raise TypeError("datos debe ser un set.")

    return objetivo in datos


def contar_con_diccionario(datos: Iterable[Any]) -> dict[Any, int]:
    """Cuenta frecuencias usando un diccionario comun."""

    if datos is None:
        raise ValueError("datos no puede ser None.")

    conteos: dict[Any, int] = {}

    for valor in datos:
        if valor not in conteos:
            conteos[valor] = 0
        conteos[valor] += 1

    return conteos


def contar_con_counter(datos: Iterable[Any]) -> Counter:
    """Cuenta frecuencias usando ``collections.Counter``."""

    if datos is None:
        raise ValueError("datos no puede ser None.")

    return Counter(datos)


def comparar_busquedas_por_tamano(
    tamanos: Sequence[int],
    repeticiones: int = 10,
    semilla: int = 42,
) -> list[dict[str, float | int]]:
    """Compara busqueda en lista y conjunto para varios tamanos.

    Para cada tamano se genera una lista, se construye un conjunto una vez y se
    mide la busqueda de un valor ausente. Buscar un valor ausente en lista ayuda
    a observar el costo de recorrer todos los datos.

    Regresa una lista de diccionarios con las llaves:
    ``tamano``, ``tiempo_lista`` y ``tiempo_conjunto``.
    """

    if tamanos is None:
        raise ValueError("tamanos no puede ser None.")
    if not isinstance(repeticiones, int):
        raise TypeError("repeticiones debe ser un entero.")
    if repeticiones <= 0:
        raise ValueError("repeticiones debe ser positivo.")

    resultados: list[dict[str, float | int]] = []

    for tamano in tamanos:
        if not isinstance(tamano, int):
            raise TypeError("todos los tamanos deben ser enteros.")
        if tamano <= 0:
            raise ValueError("todos los tamanos deben ser positivos.")

        datos = generar_datos(tamano, semilla=semilla)
        conjunto = set(datos)
        objetivo_ausente = -1

        tiempo_lista = medir_tiempo(
            lambda: buscar_en_lista(datos, objetivo_ausente),
            repeticiones=repeticiones,
        )
        tiempo_conjunto = medir_tiempo(
            lambda: buscar_en_conjunto(conjunto, objetivo_ausente),
            repeticiones=repeticiones,
        )

        resultados.append(
            {
                "tamano": tamano,
                "tiempo_lista": tiempo_lista,
                "tiempo_conjunto": tiempo_conjunto,
            }
        )

    return resultados
