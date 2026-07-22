"""Visualizador de estados precomputados; no contiene la lógica de decisión."""

from __future__ import annotations

import asyncio
import json
import textwrap
from pathlib import Path
from typing import Any

RUTA_ESTADOS = Path(__file__).with_name("estados_clase20.json")


def diagnosticar_widgets() -> str:
    try:
        import ipywidgets  # noqa: F401
        import matplotlib  # noqa: F401
    except ImportError as exc:
        return f"Falta una dependencia: {exc}. Ejecuta pip install -r requirements.txt"
    return "Entorno listo: widgets, Matplotlib y estados disponibles." if RUTA_ESTADOS.exists() else f"No se encontró {RUTA_ESTADOS}"


def cargar_estados() -> dict[str, list[dict[str, Any]]]:
    with RUTA_ESTADOS.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, dict) or not datos:
        raise ValueError("el registro de estados está vacío")
    return datos


def dibujar_estado(estado: dict[str, Any], ocultar_decision: bool = False):
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    figura = plt.figure(figsize=(15, 8.2), constrained_layout=True)
    rejilla = figura.add_gridspec(2, 1, height_ratios=[0.37, 1], hspace=0.12)
    ax_ruta = figura.add_subplot(rejilla[0])
    ax_info = figura.add_subplot(rejilla[1])
    figura.suptitle(estado["titulo"], fontsize=18, fontweight="bold")
    etapas = ["Leer", "Objetivo", "Dirección", "Pesos", "Operación", "Estructura", "Algoritmo", "Contrato", "Prueba", "Complejidad", "Interpretar"]
    for indice, etapa in enumerate(etapas):
        x = indice / (len(etapas) - 1)
        completada = indice < estado["paso"]
        actual = indice == estado["paso"] - 1
        color = "#f3a63b" if actual else "#79b995" if completada else "#d9e0e6"
        borde = "#8a4b00" if actual else "#346a4d" if completada else "#71808c"
        ax_ruta.add_patch(FancyBboxPatch((x - 0.04, 0.35), 0.08, 0.3, boxstyle="round,pad=0.01", facecolor=color, edgecolor=borde, linewidth=2))
        ax_ruta.text(x, 0.5, str(indice + 1), ha="center", va="center", fontweight="bold", fontsize=9)
        ax_ruta.text(x, 0.19, etapa, ha="center", va="top", fontsize=7.5, rotation=18 if len(etapa) > 8 else 0)
        if indice < len(etapas) - 1:
            ax_ruta.plot([x + 0.045, (indice + 1) / (len(etapas) - 1) - 0.045], [0.5, 0.5], color="#70808c", linewidth=1.5)
    ax_ruta.set_xlim(-0.06, 1.06)
    ax_ruta.set_ylim(0, 1)
    ax_ruta.axis("off")

    ax_info.axis("off")
    ax_info.set_title(f"Paso {estado['paso']} — {estado['etapa']}", loc="left", fontsize=14, fontweight="bold")
    algoritmo = "PREDICE ANTES DE REVELAR" if ocultar_decision and estado["decision_visible"] else estado["algoritmo"]
    estructura = "PREDICE ANTES DE REVELAR" if ocultar_decision and estado["decision_visible"] else estado["estructura"]
    izquierda = (
        f"PROBLEMA\n{textwrap.fill(estado['problema'], 65)}\n\n"
        f"OBJETIVO\n{estado['objetivo']}\n\nDIRECCIÓN\n{estado['dirigido']}\n\n"
        f"PESOS\n{estado['pesos']}\n\nOPERACIÓN DOMINANTE\n{textwrap.fill(estado['operacion_dominante'], 65)}"
    )
    derecha = (
        f"ESTRUCTURA\n{estructura}\n\nALGORITMO\n{algoritmo}\n\n"
        f"CONTRATO\n{textwrap.fill(estado['contrato'], 62)}\n\n"
        f"PRUEBA DISTINTIVA\n{textwrap.fill(estado['prueba'], 62)}\n\n"
        f"COMPLEJIDAD\n{estado['complejidad']}\n\nINTERPRETACIÓN\n{textwrap.fill(estado['interpretacion'], 62)}"
    )
    ax_info.text(0.01, 0.96, izquierda, transform=ax_info.transAxes, va="top", fontsize=9.7, linespacing=1.3)
    ax_info.text(0.53, 0.96, derecha, transform=ax_info.transAxes, va="top", fontsize=9.7, linespacing=1.3)
    ax_info.plot([0.5, 0.5], [0.04, 0.96], transform=ax_info.transAxes, color="#9aa7b1", linewidth=1)
    ax_info.text(0.01, 0.02, textwrap.fill(estado["mensaje"], 135), transform=ax_info.transAxes, fontsize=9, fontweight="bold")
    return figura


def mostrar_laboratorio_decisiones() -> None:
    import matplotlib.pyplot as plt
    import ipywidgets as widgets
    from IPython.display import display

    ejemplos = cargar_estados()
    selector = widgets.Dropdown(options=[(estados[0]["titulo"], nombre) for nombre, estados in ejemplos.items()], description="Caso:", layout=widgets.Layout(width="590px"))
    reiniciar = widgets.Button(description="Reiniciar", icon="refresh")
    anterior = widgets.Button(description="Anterior", icon="step-backward")
    siguiente = widgets.Button(description="Siguiente", icon="step-forward", button_style="primary")
    reproducir = widgets.Button(description="Reproducir", icon="play")
    pausar = widgets.Button(description="Pausar", icon="pause")
    reto = widgets.ToggleButton(description="Modo reto", icon="eye-slash")
    paso = widgets.IntSlider(description="Paso:", min=0, max=10, value=0, continuous_update=False)
    velocidad = widgets.FloatSlider(description="Segundos:", min=0.5, max=3.0, step=0.25, value=1.25, continuous_update=False)
    contador = widgets.HTML()
    salida = widgets.Output()
    tarea: dict[str, asyncio.Task | None] = {"actual": None}

    def renderizar(*_args: object) -> None:
        estados = ejemplos[selector.value]
        paso.max = len(estados) - 1
        contador.value = f"<strong>Paso {paso.value + 1} de {len(estados)}</strong>"
        with salida:
            salida.clear_output(wait=True)
            figura = dibujar_estado(estados[paso.value], reto.value)
            display(figura)
            plt.close(figura)

    def detener() -> None:
        if tarea["actual"] is not None and not tarea["actual"].done():
            tarea["actual"].cancel()
        tarea["actual"] = None

    async def avanzar() -> None:
        try:
            while paso.value < paso.max:
                await asyncio.sleep(velocidad.value)
                paso.value += 1
        except asyncio.CancelledError:
            return
        finally:
            tarea["actual"] = None

    def al_reproducir(_boton: object) -> None:
        detener()
        if paso.value == paso.max:
            paso.value = 0
        tarea["actual"] = asyncio.create_task(avanzar())

    def al_selector(cambio: dict[str, Any]) -> None:
        if cambio.get("name") == "value":
            detener()
            paso.value = 0
            renderizar()

    reiniciar.on_click(lambda _b: (detener(), setattr(paso, "value", 0)))
    anterior.on_click(lambda _b: setattr(paso, "value", max(0, paso.value - 1)))
    siguiente.on_click(lambda _b: setattr(paso, "value", min(paso.max, paso.value + 1)))
    reproducir.on_click(al_reproducir)
    pausar.on_click(lambda _b: detener())
    selector.observe(al_selector, names="value")
    paso.observe(renderizar, names="value")
    reto.observe(renderizar, names="value")
    display(widgets.VBox([selector, widgets.HBox([reiniciar, anterior, siguiente, reproducir, pausar, reto, contador]), widgets.HBox([paso, velocidad])]), salida)
    renderizar()


__all__ = ["cargar_estados", "diagnosticar_widgets", "dibujar_estado", "mostrar_laboratorio_decisiones"]
