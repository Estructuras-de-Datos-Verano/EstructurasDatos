"""Widgets de lectura para BFS y 0-1 BFS a partir de estados preparados."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from .visualizaciones_listas import COLORES, _interfaz

RUTA_ESTADOS = Path(__file__).with_name("estados_clase17.json")
POSICIONES = {"A": (0, 1), "B": (2, 2), "C": (2, 0), "D": (4, 2), "E": (4, 0), "F": (6, 1), "X": (4, 1)}
ARISTAS_BFS = [("A", "B", None), ("A", "C", None), ("B", "D", None), ("B", "E", None), ("C", "E", None), ("D", "F", None), ("E", "F", None)]
ARISTAS_01 = [("A", "B", 0), ("A", "C", 1), ("B", "D", 0), ("B", "E", 1), ("C", "D", 0), ("D", "F", 1), ("E", "F", 0)]
ARISTAS_MEJORA = [("A", "X", 1), ("A", "B", 0), ("B", "C", 0), ("C", "X", 0), ("X", "F", 0)]


def _cargar() -> dict:
    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def dibujar_estado_bfs(estado: dict):
    """Dibuja grafo, estructura pendiente y tablas sin mover los nodos."""

    fig = plt.figure(figsize=(13.5, 7.2), facecolor=COLORES["fondo"])
    rejilla = fig.add_gridspec(2, 2, height_ratios=[3.8, 2.2], width_ratios=[3, 2])
    ax = fig.add_subplot(rejilla[0, :])
    estado_ax = fig.add_subplot(rejilla[1, 0])
    tabla_ax = fig.add_subplot(rejilla[1, 1])
    for panel in (ax, estado_ax, tabla_ax):
        panel.set_axis_off()
    fig.suptitle(estado["titulo"], fontsize=20, fontweight="bold", color=COLORES["texto"], y=0.98)
    ax.set_title(estado["objetivo"], fontsize=12, color="#52606d")
    ax.set_xlim(-0.7, 6.7)
    ax.set_ylim(-0.7, 2.7)
    clave = "mejora" if "MEJORA" in estado["titulo"] else "01" if estado["tipo"] == "01" else "bfs"
    aristas = ARISTAS_MEJORA if clave == "mejora" else ARISTAS_01 if clave == "01" else ARISTAS_BFS
    activa = estado.get("arista") or []
    for origen, destino, peso in aristas:
        x1, y1 = POSICIONES[origen]
        x2, y2 = POSICIONES[destino]
        es_activa = len(activa) >= 2 and activa[0] == origen and activa[1] == destino
        ax.add_patch(FancyArrowPatch((x1 + 0.18, y1), (x2 - 0.18, y2), arrowstyle="-|>", mutation_scale=14, linewidth=3 if es_activa else 1.4, color=COLORES["rojo"] if es_activa else "#9aa6b2", connectionstyle="arc3,rad=0.05"))
        if peso is not None:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.13, str(peso), fontsize=10, fontweight="bold", color=COLORES["rojo"] if es_activa else COLORES["texto"], bbox={"boxstyle": "circle", "fc": "white", "ec": "none"})

    nodos = sorted({n for arista in aristas for n in arista[:2]} | {"A"})
    for nodo in nodos:
        if nodo == estado.get("actual"):
            color = COLORES["actual"]
        elif nodo in estado.get("procesados", []):
            color = COLORES["verde"]
        elif nodo in estado.get("descubiertos", []):
            color = COLORES["azul"]
        else:
            color = COLORES["normal"]
        x, y = POSICIONES[nodo]
        ax.scatter([x], [y], s=950, c=[color], edgecolors=COLORES["borde"], linewidths=2.2, zorder=3)
        ax.text(x, y, nodo, ha="center", va="center", fontsize=13, fontweight="bold", color="white" if color in (COLORES["verde"], COLORES["azul"]) else COLORES["texto"], zorder=4)

    pendientes = estado["pendientes"]
    nombre = "deque (inicio → final)" if estado["tipo"] == "01" else "cola (frente → final)"
    estado_ax.text(0.02, 0.94, "ESTADO Y DECISIÓN", fontsize=12, fontweight="bold", color=COLORES["texto"])
    estado_ax.text(0.02, 0.79, f"Paso {estado['paso']}: {estado['accion']}\n\n{nombre}: {pendientes}\nProcesados: {estado['procesados']}\n\nDecisión: {estado['decision']}\n\nInvariante: {estado['invariante']}", va="top", fontsize=10.2, linespacing=1.35, wrap=True, color=COLORES["texto"])
    tabla_ax.text(0.02, 0.94, "TABLAS DEL ALGORITMO", fontsize=12, fontweight="bold", color=COLORES["texto"])
    lineas = []
    for nodo in sorted(estado["predecesores"]):
        pred = estado["predecesores"][nodo]
        distancia = estado["distancias"][nodo] if estado.get("distancias") else (0 if nodo == "A" else "por capas")
        lineas.append(f"{nodo}: dist={distancia}, pred={pred}")
    tabla_ax.text(0.02, 0.79, "\n".join(lineas), va="top", family="monospace", fontsize=10.2, linespacing=1.35, color=COLORES["texto"])
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return fig


def mostrar_bfs() -> None:
    """Muestra BFS, el ejemplo conductor 0-1 y una mejora posterior."""

    datos = _cargar()
    opciones = {
        "bfs": "BFS con cola ligada",
        "cero_uno_bfs": "0-1 BFS: ejemplo conductor",
        "cero_uno_mejora": "0-1 BFS: mejora posterior",
    }
    _interfaz({clave: datos[clave] for clave in opciones}, opciones, dibujar_estado_bfs)


__all__ = ["dibujar_estado_bfs", "mostrar_bfs"]
