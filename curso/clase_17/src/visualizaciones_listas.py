"""Widgets de lectura para operaciones sobre cola y deque ligadas.

La lógica algorítmica y el registro de estados viven en el repositorio del
profesor. Este módulo solo carga el registro preparado y lo representa.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

RUTA_ESTADOS = Path(__file__).with_name("estados_clase17.json")
COLORES = {
    "fondo": "#f7f8fa",
    "texto": "#182230",
    "normal": "#dce3ea",
    "actual": "#f5a623",
    "nuevo": "#7c5ce7",
    "borde": "#354052",
    "verde": "#2e9d69",
    "rojo": "#cf4b4b",
    "azul": "#3686c9",
}


def _cargar() -> dict:
    if not RUTA_ESTADOS.exists():
        raise FileNotFoundError(f"No se encontró el registro preparado: {RUTA_ESTADOS}")
    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def diagnosticar_widgets() -> str:
    """Comprueba las dependencias antes de construir la interfaz."""

    try:
        import ipywidgets  # noqa: F401
    except ImportError as error:
        return f"Falta ipywidgets: {error}. Ejecuta: pip install -r requirements.txt"
    return "Entorno listo: ipywidgets, matplotlib y el registro local están disponibles."


def _texto(valor: object) -> str:
    return "None" if valor is None else str(valor)


def dibujar_estado_lista(estado: dict):
    """Convierte un estado serializado en una lámina estable y legible."""

    fig = plt.figure(figsize=(13, 6.8), facecolor=COLORES["fondo"])
    rejilla = fig.add_gridspec(2, 2, height_ratios=[3.7, 2.3], width_ratios=[3, 2])
    ax = fig.add_subplot(rejilla[0, :])
    info = fig.add_subplot(rejilla[1, 0])
    explicacion = fig.add_subplot(rejilla[1, 1])
    for panel in (ax, info, explicacion):
        panel.set_axis_off()

    fig.suptitle(estado["titulo"], fontsize=20, fontweight="bold", color=COLORES["texto"], y=0.98)
    ax.set_title(estado["objetivo"], fontsize=12, color="#52606d", pad=10)
    ax.set_xlim(-0.7, 10.7)
    ax.set_ylim(-1.2, 3.2)

    nodos = estado["nodos"]
    separacion = 2.35
    inicio_x = 5 - separacion * (max(len(nodos), 1) - 1) / 2
    posiciones = {nodo["valor"]: inicio_x + i * separacion for i, nodo in enumerate(nodos)}

    for nodo in nodos:
        x = posiciones[nodo["valor"]]
        color = COLORES["nuevo"] if nodo.get("nuevo") else COLORES["actual"] if nodo["valor"] == estado.get("actual") else COLORES["normal"]
        caja = FancyBboxPatch((x - 0.65, 0.45), 1.3, 0.85, boxstyle="round,pad=0.08", facecolor=color, edgecolor=COLORES["borde"], linewidth=2)
        ax.add_patch(caja)
        ax.text(x, 0.88, nodo["valor"], ha="center", va="center", fontsize=14, fontweight="bold", color=COLORES["texto"])
        if nodo.get("siguiente") in posiciones:
            destino = posiciones[nodo["siguiente"]]
            ax.add_patch(FancyArrowPatch((x + 0.68, 0.92), (destino - 0.68, 0.92), arrowstyle="-|>", mutation_scale=14, linewidth=2, color=COLORES["azul"]))
        if nodo.get("anterior") in posiciones:
            destino = posiciones[nodo["anterior"]]
            ax.add_patch(FancyArrowPatch((x - 0.68, 0.65), (destino + 0.68, 0.65), arrowstyle="-|>", mutation_scale=14, linewidth=1.6, color=COLORES["verde"]))

    for etiqueta, valor, y, color in (("inicio / frente", estado["inicio"], 2.25, COLORES["azul"]), ("final", estado["final"], 1.8, COLORES["verde"])):
        if valor in posiciones:
            x = posiciones[valor]
            ax.annotate(etiqueta, xy=(x, 1.35), xytext=(x, y), ha="center", fontsize=10, fontweight="bold", color=color, arrowprops={"arrowstyle": "->", "color": color})
    if estado.get("retirado") is not None:
        ax.text(5, -0.55, f"valor devuelto: {estado['retirado']} (nodo ya desconectado)", ha="center", color=COLORES["rojo"], fontsize=11, fontweight="bold")

    info.text(0.02, 0.92, "ESTADO ACTUAL", fontsize=12, fontweight="bold", color=COLORES["texto"])
    lineas = [
        f"Paso: {estado['paso']}", f"Operación: {estado['operacion']}", f"Acción: {estado['accion']}",
        f"Inicio/frente: {_texto(estado['inicio'])}", f"Final: {_texto(estado['final'])}", f"Tamaño: {estado['tamano']}",
    ]
    info.text(0.02, 0.77, "\n".join(lineas), va="top", fontsize=10.5, linespacing=1.45, color=COLORES["texto"])
    explicacion.text(0.02, 0.92, "DECISIÓN E INVARIANTE", fontsize=12, fontweight="bold", color=COLORES["texto"])
    explicacion.text(0.02, 0.77, f"{estado['decision']}\n\n{estado['mensaje']}\n\nInvariante:\n{estado['invariante']}", va="top", fontsize=10.2, linespacing=1.35, wrap=True, color=COLORES["texto"])
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return fig


def _interfaz(catalogo: dict, opciones: dict[str, str], dibujar: Callable[[dict], object]):
    import ipywidgets as widgets
    from IPython.display import clear_output, display

    selector = widgets.Dropdown(options=[(etiqueta, clave) for clave, etiqueta in opciones.items()], description="Secuencia:", layout=widgets.Layout(width="430px"))
    paso = widgets.IntSlider(min=0, max=len(catalogo[selector.value]) - 1, value=0, description="Paso:", continuous_update=False, layout=widgets.Layout(width="500px"))
    anterior = widgets.Button(description="← Anterior")
    siguiente = widgets.Button(description="Siguiente →")
    reproducir = widgets.Play(value=0, min=0, max=paso.max, step=1, interval=1700, description="Reproducir")
    widgets.jslink((reproducir, "value"), (paso, "value"))
    reto = widgets.ToggleButton(value=False, description="Modo reto", icon="question")
    salida = widgets.Output()
    respuesta = widgets.HTML()

    def renderizar(*_):
        estado = catalogo[selector.value][paso.value]
        respuesta.value = ("<div style='padding:10px;border-left:4px solid #7c5ce7;background:#f2efff'><b>Predicción / respuesta:</b> " + estado.get("respuesta_reto", "") + "</div>") if reto.value else "<div style='padding:8px;color:#52606d'>Activa <b>Modo reto</b> para comparar tu predicción después de avanzar.</div>"
        with salida:
            clear_output(wait=True)
            figura = dibujar(estado)
            display(figura)
            plt.close(figura)

    def cambiar_secuencia(cambio):
        paso.max = len(catalogo[cambio["new"]]) - 1
        reproducir.max = paso.max
        paso.value = 0
        renderizar()

    anterior.on_click(lambda _: setattr(paso, "value", max(paso.min, paso.value - 1)))
    siguiente.on_click(lambda _: setattr(paso, "value", min(paso.max, paso.value + 1)))
    selector.observe(cambiar_secuencia, names="value")
    paso.observe(renderizar, names="value")
    reto.observe(renderizar, names="value")
    controles = widgets.VBox([widgets.HBox([selector, reto]), widgets.HBox([anterior, siguiente, reproducir]), paso, respuesta])
    renderizar()
    display(widgets.VBox([controles, salida]))


def mostrar_listas() -> None:
    """Muestra las seis operaciones ligadas con controles de navegación."""

    datos = _cargar()
    opciones = {
        "encolar": "Cola: encolar",
        "desencolar": "Cola: desencolar",
        "agregar_inicio": "Deque: agregar al inicio",
        "agregar_final": "Deque: agregar al final",
        "quitar_inicio": "Deque: quitar del inicio",
        "quitar_final": "Deque: quitar del final",
    }
    _interfaz({clave: datos[clave] for clave in opciones}, opciones, dibujar_estado_lista)


__all__ = ["diagnosticar_widgets", "dibujar_estado_lista", "mostrar_listas"]
