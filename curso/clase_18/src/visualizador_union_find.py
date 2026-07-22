"""Interfaz de lectura para los estados preparados de Union-Find."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

RUTA_ESTADOS = Path(__file__).with_name("estados_clase18.json")
COLORES = {
    "fondo": "#f5f7fa", "texto": "#172033", "muted": "#5f6f80",
    "normal": "#d9e1e8", "actual": "#f4a62a", "aceptada": "#2f855a",
    "rechazada": "#c43d3d", "azul": "#2b6cb0", "borde": "#344256",
}


def _cargar() -> dict:
    if not RUTA_ESTADOS.exists():
        raise FileNotFoundError(f"No se encontró el registro: {RUTA_ESTADOS}")
    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def diagnosticar_widgets() -> str:
    try:
        import ipywidgets  # noqa: F401
    except ImportError as error:
        return f"Falta ipywidgets: {error}. Ejecuta pip install -r requirements.txt"
    return "Entorno listo: registro local, ipywidgets y matplotlib disponibles."


def _profundidad(padres: list[int], nodo: int) -> int:
    profundidad = 0
    vistos = set()
    while padres[nodo] != nodo and nodo not in vistos:
        vistos.add(nodo)
        nodo = padres[nodo]
        profundidad += 1
    return profundidad


def dibujar_estado_union_find(estado: dict):
    """Dibuja bosque, componentes, arreglos y pseudocódigo activo."""

    fig = plt.figure(figsize=(14, 7.6), facecolor=COLORES["fondo"])
    rejilla = fig.add_gridspec(2, 2, width_ratios=[3, 2], height_ratios=[3.6, 2.4])
    bosque = fig.add_subplot(rejilla[0, 0])
    pseudo = fig.add_subplot(rejilla[0, 1])
    datos = fig.add_subplot(rejilla[1, 0])
    explicacion = fig.add_subplot(rejilla[1, 1])
    for panel in (bosque, pseudo, datos, explicacion):
        panel.set_axis_off()
    fig.suptitle(estado["titulo"], fontsize=20, fontweight="bold", color=COLORES["texto"], y=.98)

    padres = estado["padres"]
    bosque.set_xlim(-.8, max(len(padres) - .2, .8))
    bosque.set_ylim(-max([_profundidad(padres, i) for i in range(len(padres))] + [1]) - .7, 1)
    bosque.set_title("Bosque interno de representantes", fontsize=12, color=COLORES["muted"])
    actual = set((estado.get("arista_actual") or [])[:2])
    for nodo, padre in enumerate(padres):
        y = -_profundidad(padres, nodo)
        if padre != nodo:
            py = -_profundidad(padres, padre)
            bosque.add_patch(FancyArrowPatch((nodo, y + .12), (padre, py - .12), arrowstyle="-|>", mutation_scale=14, color="#8795a5", linewidth=1.7, connectionstyle="arc3,rad=.08"))
        color = COLORES["actual"] if nodo in actual else COLORES["azul"] if padre == nodo else COLORES["normal"]
        bosque.scatter([nodo], [y], s=850, c=[color], edgecolors=COLORES["borde"], linewidths=2, zorder=3)
        bosque.text(nodo, y, str(nodo), ha="center", va="center", fontsize=12, fontweight="bold", color="white" if padre == nodo and nodo not in actual else COLORES["texto"], zorder=4)
        if padre == nodo:
            bosque.text(nodo, y + .34, "RAÍZ", ha="center", fontsize=8.5, fontweight="bold", color=COLORES["azul"])

    pseudo.text(.02, .96, "PSEUDOCÓDIGO", fontsize=12, fontweight="bold", color=COLORES["texto"], va="top")
    y = .84
    for i, linea in enumerate(estado["pseudocodigo"]):
        marca = "▶ " if i == estado.get("linea_activa") else "  "
        color = COLORES["actual"] if i == estado.get("linea_activa") else COLORES["texto"]
        pseudo.text(.02, y, f"{marca}{i + 1}. {linea}", fontsize=9.5, family="monospace", fontweight="bold" if marca.strip() else "normal", color=color, va="top")
        y -= .115

    datos.text(.02, .94, "ESTADO", fontsize=12, fontweight="bold", color=COLORES["texto"])
    grupos = "  ".join("{" + ",".join(map(str, grupo)) + "}" for grupo in estado["grupos"])
    lineas = [
        f"Paso: {estado['paso']}", f"Padres:  {estado['padres']}", f"Tamaños: {estado['tamanos']}",
        f"Componentes ({estado['componentes']}): {grupos}",
        f"Raíces comparadas: {estado.get('raiz_u')} y {estado.get('raiz_v')}",
    ]
    datos.text(.02, .78, "\n".join(lineas), va="top", fontsize=10.5, family="monospace", linespacing=1.45, color=COLORES["texto"])
    explicacion.text(.02, .94, "DECISIÓN", fontsize=12, fontweight="bold", color=COLORES["texto"])
    explicacion.text(.02, .78, f"{estado['accion']}\n\n{estado['decision']}\n\nMotivo: {estado['motivo']}\n\n{estado['mensaje']}", va="top", fontsize=10.5, linespacing=1.35, wrap=True, color=COLORES["texto"])
    fig.tight_layout(rect=(0, 0, 1, .95))
    return fig


def _interfaz(catalogo: dict, opciones: dict[str, str], dibujar: Callable[[dict], object]) -> None:
    import ipywidgets as widgets
    from IPython.display import clear_output, display

    selector = widgets.Dropdown(options=[(etiqueta, clave) for clave, etiqueta in opciones.items()], description="Ejemplo:", layout=widgets.Layout(width="440px"))
    paso = widgets.IntSlider(value=0, min=0, max=len(catalogo[selector.value]) - 1, description="Paso:", continuous_update=False, layout=widgets.Layout(width="520px"))
    play = widgets.Play(value=0, min=0, max=paso.max, interval=1700, description="Reproducir / Pausar")
    widgets.jslink((play, "value"), (paso, "value"))
    velocidad = widgets.SelectionSlider(options=[("Lenta", 2600), ("Normal", 1700), ("Rápida", 900)], value=1700, description="Velocidad:")
    reiniciar = widgets.Button(description="Reiniciar")
    anterior = widgets.Button(description="← Anterior")
    siguiente = widgets.Button(description="Siguiente →")
    salida = widgets.Output()
    estado_texto = widgets.HTML()

    def renderizar(*_):
        estado = catalogo[selector.value][paso.value]
        estado_texto.value = f"<b>Paso {paso.value + 1} de {paso.max + 1}</b> — {estado['accion']}"
        with salida:
            clear_output(wait=True)
            figura = dibujar(estado)
            display(figura)
            plt.close(figura)

    def cambiar(cambio):
        paso.max = len(catalogo[cambio["new"]]) - 1
        play.max = paso.max
        paso.value = 0
        renderizar()

    selector.observe(cambiar, names="value")
    paso.observe(renderizar, names="value")
    velocidad.observe(lambda cambio: setattr(play, "interval", cambio["new"]), names="value")
    reiniciar.on_click(lambda _: setattr(paso, "value", 0))
    anterior.on_click(lambda _: setattr(paso, "value", max(0, paso.value - 1)))
    siguiente.on_click(lambda _: setattr(paso, "value", min(paso.max, paso.value + 1)))
    controles = widgets.VBox([widgets.HBox([selector, velocidad]), widgets.HBox([reiniciar, anterior, siguiente, play]), paso, estado_texto])
    renderizar()
    display(widgets.VBox([controles, salida]))


def mostrar_union_find() -> None:
    datos = _cargar()
    opciones = {
        "union_find_basico": "Union-Find básico", "union_efectiva": "Unión efectiva",
        "union_redundante": "Unión redundante", "compresion_caminos": "Compresión de caminos",
        "union_por_tamano": "Unión por tamaño",
    }
    _interfaz({clave: datos[clave] for clave in opciones}, opciones, dibujar_estado_union_find)


__all__ = ["diagnosticar_widgets", "dibujar_estado_union_find", "mostrar_union_find"]
