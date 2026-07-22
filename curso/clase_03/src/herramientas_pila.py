"""Funciones auxiliares para motivar el uso de pilas.

Este modulo no implementa una clase ``Pila``. Solo contiene funciones pequenas
para discutir comportamiento LIFO antes de disenar una interfaz formal.
"""

from __future__ import annotations

from typing import Any


def visitar_pagina(historial: list[str], pagina: str) -> list[str]:
    """Agrega una pagina al historial y regresa el historial actualizado."""

    if not isinstance(historial, list):
        raise TypeError("historial debe ser una lista.")
    if not isinstance(pagina, str):
        raise TypeError("pagina debe ser texto.")
    if pagina == "":
        raise ValueError("pagina no puede estar vacia.")

    historial.append(pagina)
    return historial


def regresar(historial: list[str]) -> str | None:
    """Regresa a la pagina anterior si existe.

    La pagina actual se elimina del historial. Si no hay una pagina anterior,
    la funcion regresa ``None``.
    """

    if not isinstance(historial, list):
        raise TypeError("historial debe ser una lista.")
    if len(historial) <= 1:
        return None

    historial.pop()
    return historial[-1]


def pagina_actual(historial: list[str]) -> str | None:
    """Regresa la pagina actual sin modificar el historial."""

    if not isinstance(historial, list):
        raise TypeError("historial debe ser una lista.")
    if not historial:
        return None

    return historial[-1]


def registrar_accion(acciones: list[str], accion: str) -> list[str]:
    """Agrega una accion a la lista de acciones realizadas."""

    if not isinstance(acciones, list):
        raise TypeError("acciones debe ser una lista.")
    if not isinstance(accion, str):
        raise TypeError("accion debe ser texto.")
    if accion == "":
        raise ValueError("accion no puede estar vacia.")

    acciones.append(accion)
    return acciones


def deshacer_accion(acciones: list[str]) -> str | None:
    """Elimina y regresa la ultima accion realizada."""

    if not isinstance(acciones, list):
        raise TypeError("acciones debe ser una lista.")
    if not acciones:
        return None

    return acciones.pop()


def parentesis_balanceados_guiada(expresion: str) -> list[dict[str, Any]]:
    """Genera una traza guiada para discutir parentesis balanceados.

    La funcion no decide si la expresion esta balanceada. Solo muestra como
    cambia una pila tentativa al leer simbolos de apertura y donde aparecen
    simbolos de cierre. Los estudiantes completaran la regla en clase.
    """

    if not isinstance(expresion, str):
        raise TypeError("expresion debe ser texto.")

    pila: list[str] = []
    eventos: list[dict[str, Any]] = []
    aperturas = "([{"
    cierres = ")]}"

    for posicion, simbolo in enumerate(expresion):
        if simbolo in aperturas:
            pila.append(simbolo)
            eventos.append(
                {
                    "posicion": posicion,
                    "simbolo": simbolo,
                    "accion": "apilar apertura",
                    "pila": pila.copy(),
                }
            )
        elif simbolo in cierres:
            eventos.append(
                {
                    "posicion": posicion,
                    "simbolo": simbolo,
                    "accion": "TODO: verificar si cierra el tope",
                    "pila": pila.copy(),
                }
            )

    return eventos
