"""Interfaz didáctica para explorar estados precomputados de Kahn.

La lógica de generación vive en el repositorio del profesor. Este módulo solo
lee estados JSON, los dibuja y conecta controles de ``ipywidgets``.
"""

from __future__ import annotations

import asyncio
import json
import textwrap
from pathlib import Path
from typing import Any


RUTA_ESTADOS = Path(__file__).with_name("estados_clase19.json")


def diagnosticar_widgets() -> str:
    """Comprueba dependencias antes de construir la interfaz."""

    try:
        import ipywidgets  # noqa: F401
        import matplotlib  # noqa: F401
    except ImportError as exc:
        return f"Falta una dependencia: {exc}. Ejecuta pip install -r requirements.txt"
    if not RUTA_ESTADOS.exists():
        return f"No se encontró el registro de estados: {RUTA_ESTADOS}"
    return "Entorno listo: ipywidgets, Matplotlib y estados disponibles."


def cargar_estados() -> dict[str, list[dict[str, Any]]]:
    """Carga el registro serializable sin ejecutar el algoritmo."""

    with RUTA_ESTADOS.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, dict) or not datos:
        raise ValueError("el archivo de estados no contiene ejemplos")
    return datos


def _texto_nodo(nodo: str, grado: int, estado: str) -> str:
    nombre = textwrap.fill(nodo, width=18)
    return f"{nombre}\ngrado={grado}\n{estado}"


def dibujar_estado(estado: dict[str, Any]):
    """Construye una figura legible con grafo y estado algorítmico."""

    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch

    figura = plt.figure(figsize=(15, 8.4), constrained_layout=True)
    rejilla = figura.add_gridspec(
        2, 2, width_ratios=[1.45, 1], height_ratios=[1.15, 0.85],
        wspace=0.16, hspace=0.18,
    )
    ax_grafo = figura.add_subplot(rejilla[:, 0])
    ax_info = figura.add_subplot(rejilla[0, 1])
    ax_codigo = figura.add_subplot(rejilla[1, 1])
    figura.suptitle(estado["titulo"], fontsize=18, fontweight="bold", y=0.98)
    posiciones = {nodo: tuple(xy) for nodo, xy in estado["posiciones"].items()}
    grafo = estado["grafo"]
    procesados = set(estado["orden_parcial"])
    en_cola = set(estado["cola"])
    actual = estado["nodo_actual"]
    vecino_actual = estado["vecino_actual"]

    for origen, vecinos in grafo.items():
        x1, y1 = posiciones[origen]
        for destino in vecinos:
            x2, y2 = posiciones[destino]
            activa = origen == actual and destino == vecino_actual
            color = "#c56a00" if activa else "#66788a"
            estilo = "-" if activa else "--" if estado["ciclo_detectado"] and origen in estado["nodos_pendientes"] else "-"
            flecha = FancyArrowPatch(
                (x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16,
                linewidth=3 if activa else 1.5, color=color, linestyle=estilo,
                shrinkA=42, shrinkB=42, connectionstyle="arc3,rad=0.05",
            )
            ax_grafo.add_patch(flecha)
            if activa:
                ax_grafo.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.12, "ARISTA ACTUAL", color=color, fontsize=8, fontweight="bold")

    for nodo, (x, y) in posiciones.items():
        if nodo == actual:
            color, etiqueta, borde, estilo = "#f3a63b", "ACTUAL", "#8a4b00", "-"
        elif nodo in procesados:
            color, etiqueta, borde, estilo = "#9bd3b0", "PROCESADO ✓", "#256647", "-"
        elif nodo in en_cola:
            color, etiqueta, borde, estilo = "#a9cdec", "DISPONIBLE", "#245f91", "-"
        else:
            color, etiqueta, borde, estilo = "#e2e7eb", "BLOQUEADO", "#65717c", "--"
        ax_grafo.text(
            x, y, _texto_nodo(nodo, estado["grados"][nodo], etiqueta),
            ha="center", va="center", fontsize=8.5,
            bbox={"boxstyle": "round,pad=0.55", "facecolor": color, "edgecolor": borde, "linewidth": 2, "linestyle": estilo},
        )

    xs = [xy[0] for xy in posiciones.values()]
    ys = [xy[1] for xy in posiciones.values()]
    ax_grafo.set_xlim(min(xs) - 1, max(xs) + 1)
    ax_grafo.set_ylim(min(ys) - 1, max(ys) + 1)
    ax_grafo.set_title("Grafo dirigido — forma estable", fontsize=13)
    ax_grafo.axis("off")

    ax_info.axis("off")
    ax_info.set_title(f"Paso {estado['paso']} — {estado['accion']}", loc="left", fontsize=13, fontweight="bold")
    cola = textwrap.fill(" → ".join(estado["cola"]) or "∅", width=52)
    orden = textwrap.fill(", ".join(estado["orden_parcial"]) or "∅", width=52)
    pendientes = textwrap.fill(", ".join(estado["nodos_pendientes"]) or "ninguno", width=52)
    actual_txt = estado["nodo_actual"] or "—"
    arista_txt = (
        f"{estado['nodo_actual']} → {estado['vecino_actual']}"
        if estado["vecino_actual"] is not None else "—"
    )
    cambio = (
        f"{estado['grado_anterior']} → {estado['grado_nuevo']}"
        if estado["grado_anterior"] is not None else "—"
    )
    resumen = (
        f"COLA DISPONIBLE\n{cola}\n\n"
        f"NODO ACTUAL\n{actual_txt}\n\n"
        f"ARISTA / CAMBIO DE GRADO\n{arista_txt}   {cambio}\n\n"
        f"ORDEN PARCIAL\n{orden}\n\n"
        f"NODOS PENDIENTES\n{pendientes}\n\n"
        f"DECISIÓN\n{textwrap.fill(estado['decision'], width=52)}\n\n"
        f"EXPLICACIÓN\n{textwrap.fill(estado['mensaje'], width=52)}"
    )
    ax_info.text(0, 0.94, resumen, transform=ax_info.transAxes, va="top", fontsize=9.2, linespacing=1.25)

    ax_codigo.axis("off")
    ax_codigo.set_title("Pseudocódigo", loc="left", fontsize=11, fontweight="bold")
    for indice, linea in enumerate(estado["pseudocodigo"]):
        activa = indice == estado["linea_activa"]
        prefijo = "▶ " if activa else "  "
        ax_codigo.text(
            0, 0.94 - indice * 0.095, prefijo + linea, transform=ax_codigo.transAxes,
            fontsize=8.6, family="monospace", fontweight="bold" if activa else "normal",
            color="#8a4b00" if activa else "#263442",
        )
    if estado["ciclo_detectado"]:
        ax_codigo.text(0, 0.01, "CICLO: quedaron nodos bloqueados", transform=ax_codigo.transAxes, color="#a52323", fontsize=10.5, fontweight="bold")
    return figura


def mostrar_topologico() -> None:
    """Muestra selector, navegación, reproducción, velocidad y paso."""

    import matplotlib.pyplot as plt
    import ipywidgets as widgets
    from IPython.display import display

    ejemplos = cargar_estados()
    nombres = {nombre: estados[0]["titulo"] for nombre, estados in ejemplos.items()}
    selector = widgets.Dropdown(
        options=[(titulo, nombre) for nombre, titulo in nombres.items()],
        description="Ejemplo:", layout=widgets.Layout(width="520px"),
    )
    reiniciar = widgets.Button(description="Reiniciar", icon="refresh")
    anterior = widgets.Button(description="Anterior", icon="step-backward")
    siguiente = widgets.Button(description="Siguiente", icon="step-forward", button_style="primary")
    reproducir = widgets.Button(description="Reproducir", icon="play")
    pausar = widgets.Button(description="Pausar", icon="pause")
    paso = widgets.IntSlider(description="Paso:", min=0, max=len(ejemplos[selector.value]) - 1, value=0, continuous_update=False)
    velocidad = widgets.FloatSlider(description="Segundos:", min=0.4, max=3.0, step=0.2, value=1.2, readout_format=".1f", continuous_update=False)
    contador = widgets.HTML()
    salida = widgets.Output()
    tarea: dict[str, asyncio.Task | None] = {"actual": None}

    def estados_actuales() -> list[dict[str, Any]]:
        return ejemplos[selector.value]

    def renderizar(*_args: object) -> None:
        estados = estados_actuales()
        paso.max = len(estados) - 1
        paso.value = min(paso.value, paso.max)
        contador.value = f"<strong>Paso {paso.value + 1} de {len(estados)}</strong>"
        with salida:
            salida.clear_output(wait=True)
            figura = dibujar_estado(estados[paso.value])
            display(figura)
            plt.close(figura)

    def detener() -> None:
        if tarea["actual"] is not None and not tarea["actual"].done():
            tarea["actual"].cancel()
        tarea["actual"] = None

    async def avanzar_automaticamente() -> None:
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
        tarea["actual"] = asyncio.create_task(avanzar_automaticamente())

    def al_selector(cambio: dict[str, Any]) -> None:
        if cambio.get("name") == "value":
            detener()
            paso.max = len(estados_actuales()) - 1
            paso.value = 0
            renderizar()

    reiniciar.on_click(lambda _b: (detener(), setattr(paso, "value", 0)))
    anterior.on_click(lambda _b: setattr(paso, "value", max(0, paso.value - 1)))
    siguiente.on_click(lambda _b: setattr(paso, "value", min(paso.max, paso.value + 1)))
    reproducir.on_click(al_reproducir)
    pausar.on_click(lambda _b: detener())
    selector.observe(al_selector, names="value")
    paso.observe(renderizar, names="value")

    controles = widgets.VBox([
        selector,
        widgets.HBox([reiniciar, anterior, siguiente, reproducir, pausar, contador]),
        widgets.HBox([paso, velocidad]),
    ])
    display(controles, salida)
    renderizar()


__all__ = ["diagnosticar_widgets", "cargar_estados", "dibujar_estado", "mostrar_topologico"]
