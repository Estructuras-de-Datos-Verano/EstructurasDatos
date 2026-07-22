"""Interfaz de lectura de Kruskal a partir del registro preparado."""

from __future__ import annotations

import json
from math import cos, pi, sin
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from .visualizador_union_find import COLORES, _interfaz

RUTA_ESTADOS = Path(__file__).with_name("estados_clase18.json")


def _cargar() -> dict:
    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def _posiciones(numero: int) -> dict[int, tuple[float, float]]:
    return {i: (cos(2 * pi * i / max(numero, 1)), sin(2 * pi * i / max(numero, 1))) for i in range(numero)}


def dibujar_estado_kruskal(estado: dict):
    """Dibuja el grafo, la cola ordenada y el estado de Union-Find."""

    fig = plt.figure(figsize=(15, 8), facecolor=COLORES["fondo"])
    rejilla = fig.add_gridspec(2, 3, width_ratios=[2.7, 1.55, 1.75], height_ratios=[3.8, 2.2])
    grafo = fig.add_subplot(rejilla[0, :2])
    orden = fig.add_subplot(rejilla[0, 2])
    estado_ax = fig.add_subplot(rejilla[1, :2])
    pseudo = fig.add_subplot(rejilla[1, 2])
    for panel in (grafo, orden, estado_ax, pseudo):
        panel.set_axis_off()
    fig.suptitle(estado["titulo"], fontsize=20, fontweight="bold", color=COLORES["texto"], y=.985)
    posiciones = _posiciones(estado["numero_vertices"])
    actual = estado.get("arista_actual")
    seleccionadas = {tuple(a) for a in estado["aristas_seleccionadas"]}
    rechazadas = {tuple(a) for a in estado["aristas_rechazadas"]}

    for u, v, peso in estado["aristas"]:
        x1, y1 = posiciones[u]
        x2, y2 = posiciones[v]
        arista = (u, v, peso)
        es_actual = actual == [u, v, peso]
        if arista in seleccionadas:
            color, ancho, estilo = COLORES["aceptada"], 4, "-"
        elif arista in rechazadas:
            color, ancho, estilo = COLORES["rechazada"], 3, "--"
        elif es_actual:
            color, ancho, estilo = COLORES["actual"], 4, "-"
        else:
            color, ancho, estilo = "#a6b1bd", 1.4, "-"
        grafo.plot([x1, x2], [y1, y2], color=color, linewidth=ancho, linestyle=estilo, zorder=1)
        grafo.text((x1 + x2) / 2, (y1 + y2) / 2, f"{peso:g}", fontsize=9, fontweight="bold", ha="center", va="center", bbox={"boxstyle": "circle", "fc": COLORES["fondo"], "ec": "none"}, zorder=2)
    extremos = set((actual or [])[:2])
    for nodo, (x, y) in posiciones.items():
        color = COLORES["actual"] if nodo in extremos else COLORES["azul"]
        grafo.scatter([x], [y], s=850, c=[color], edgecolors=COLORES["borde"], linewidths=2, zorder=3)
        grafo.text(x, y, str(nodo), ha="center", va="center", fontsize=12, fontweight="bold", color="white" if nodo not in extremos else COLORES["texto"], zorder=4)
    grafo.set_xlim(-1.35, 1.35)
    grafo.set_ylim(-1.3, 1.3)
    grafo.set_title("Verde continua = aceptada · roja discontinua = rechazada · naranja = actual", fontsize=10.5, color=COLORES["muted"])

    orden.text(.02, .96, "ARISTAS ORDENADAS", fontsize=11.5, fontweight="bold", color=COLORES["texto"], va="top")
    y = .86
    for i, arista in enumerate(estado["aristas_ordenadas"]):
        marca = "▶" if actual == arista else "✓" if tuple(arista) in seleccionadas else "×" if tuple(arista) in rechazadas else "·"
        color = COLORES["actual"] if marca == "▶" else COLORES["aceptada"] if marca == "✓" else COLORES["rechazada"] if marca == "×" else COLORES["texto"]
        orden.text(.03, y, f"{marca} ({arista[0]}, {arista[1]})  peso {arista[2]:g}", fontsize=9.2, family="monospace", color=color, va="top")
        y -= .078

    grupos = "  ".join("{" + ",".join(map(str, g)) + "}" for g in estado["grupos"])
    estado_ax.text(.01, .94, "ESTADO Y DECISIÓN", fontsize=12, fontweight="bold", color=COLORES["texto"])
    texto = (
        f"Paso {estado['paso']}: {estado['accion']}\n"
        f"Decisión: {estado['decision']} — {estado['motivo']}\n"
        f"Raíces: {estado.get('raiz_u')} / {estado.get('raiz_v')}   Componentes ({estado['componentes']}): {grupos}\n"
        f"Padres: {estado['padres']}   Tamaños: {estado['tamanos']}\n"
        f"Seleccionadas: {estado['aristas_seleccionadas']}   Costo: {estado['costo_acumulado']:g}\n"
        f"{estado['mensaje']}"
    )
    estado_ax.text(.01, .78, texto, va="top", fontsize=9.8, family="monospace", linespacing=1.35, color=COLORES["texto"])

    pseudo.text(.02, .94, "PSEUDOCÓDIGO", fontsize=11.5, fontweight="bold", color=COLORES["texto"])
    y = .79
    for i, linea in enumerate(estado["pseudocodigo"]):
        marca = "▶ " if i == estado.get("linea_activa") else "  "
        pseudo.text(.02, y, f"{marca}{linea}", fontsize=8.6, family="monospace", fontweight="bold" if marca.strip() else "normal", color=COLORES["actual"] if marca.strip() else COLORES["texto"], va="top")
        y -= .095
    fig.tight_layout(rect=(0, 0, 1, .95))
    return fig


def mostrar_kruskal() -> None:
    datos = _cargar()
    opciones = {
        "kruskal_basico": "Red de ciudades", "arista_rechazada": "Arista rechazada por ciclo",
        "pesos_repetidos": "Pesos repetidos", "grafo_desconectado": "Grafo desconectado",
        "road_reparation": "CSES Road Reparation",
    }
    _interfaz({clave: datos[clave] for clave in opciones}, opciones, dibujar_estado_kruskal)


__all__ = ["dibujar_estado_kruskal", "mostrar_kruskal"]
