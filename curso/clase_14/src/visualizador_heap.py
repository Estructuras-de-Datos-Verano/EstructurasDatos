"""Visualizador de Clase 14; consume estados precomputados, no implementa heaps."""

from __future__ import annotations

import json
import math
from pathlib import Path

import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import clear_output, display

RUTA_ESTADOS = Path(__file__).with_name("estados_heap.json")
COLORES = {"neutro": "#dce4ef", "actual": "#3b82f6", "padre": "#f59e0b", "hijo": "#8b5cf6", "comparacion": "#fde047", "cambio": "#ef4444", "correcto": "#22c55e", "linea": "#64748b"}


def cargar_estados() -> dict:
    """Carga el registro producido en el repositorio del profesor."""

    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def _posiciones(cantidad: int) -> dict[int, tuple[float, float]]:
    posiciones = {}
    if not cantidad:
        return posiciones
    niveles = math.floor(math.log2(cantidad)) + 1
    for indice in range(cantidad):
        nivel = math.floor(math.log2(indice + 1)); primero = 2**nivel - 1
        posiciones[indice] = ((indice - primero + 1) / (2**nivel + 1), 1 - (nivel + .5) / niveles)
    return posiciones


def _color(indice: int, estado: dict) -> str:
    if indice in (estado.get("intercambio") or []): return COLORES["cambio"]
    if indice == estado.get("indice_actual") and estado.get("accion", "").startswith("Finalizar"): return COLORES["correcto"]
    if indice == estado.get("indice_actual"): return COLORES["actual"]
    if indice == estado.get("indice_padre"): return COLORES["padre"]
    if indice == estado.get("indice_hijo_seleccionado"): return COLORES["hijo"]
    if indice in (estado.get("indice_izquierdo"), estado.get("indice_derecho")): return COLORES["comparacion"]
    return COLORES["neutro"]


def dibujar_estado(estado: dict, total: int):
    """Relaciona el árbol con el arreglo y la decisión registrada."""

    arreglo = estado["arreglo"]
    figura, (arbol, detalle) = plt.subplots(1, 2, figsize=(13, 5.8), gridspec_kw={"width_ratios": [1.5, 1]}, constrained_layout=True)
    figura.suptitle(f"{estado['titulo']} · Paso {estado['paso'] + 1} de {total}", fontsize=18, weight="bold")
    posiciones = _posiciones(len(arreglo))
    for indice, (x, y) in posiciones.items():
        for hijo in (2 * indice + 1, 2 * indice + 2):
            if hijo in posiciones:
                arbol.plot([x, posiciones[hijo][0]], [y, posiciones[hijo][1]], color=COLORES["linea"])
    for indice, valor in enumerate(arreglo):
        x, y = posiciones[indice]
        arbol.scatter(x, y, s=1250, color=_color(indice, estado), edgecolor="#172033", zorder=2)
        arbol.text(x, y, str(valor), ha="center", va="center", weight="bold", zorder=3)
        arbol.text(x, y - .09, f"i={indice}", ha="center", fontsize=9, color=COLORES["linea"])
    arbol.set(xlim=(-.03, 1.03), ylim=(-.12, 1.02), title="Árbol completo"); arbol.axis("off")
    if not arreglo: arbol.text(.5, .5, "Heap vacío", ha="center")
    detalle.axis("off"); detalle.set_title("Estado y decisión", loc="left")
    texto = "\n\n".join([
        f"OBJETIVO\n{estado['objetivo']}", f"ACCIÓN\n{estado['accion']}",
        f"COMPARACIÓN\n{estado['comparacion']}", f"DECISIÓN\n{estado['decision']}",
        f"INVARIANTE\n{estado['propiedad_heap']}", f"PSEUDOCÓDIGO\n▶ {estado['linea_pseudocodigo']}",
    ])
    detalle.text(0, .98, texto, va="top", wrap=True, fontsize=10.5)
    figura.text(.08, .02, "Arreglo: " + str(arreglo) + "    Índices: " + str(list(range(len(arreglo)))), family="monospace", fontsize=10)
    return figura


class VisualizadorHeapAlumno:
    """Interfaz guiada y modo reto sin exponer la solución algorítmica."""

    def __init__(self) -> None:
        self.catalogo = cargar_estados()
        self.ejemplo = widgets.Dropdown(options=[(d["nombre"], c) for c, d in self.catalogo.items()], description="Ejemplo:")
        self.modo = widgets.ToggleButtons(options=[("Guiado", "guiado"), ("Reto", "reto")], description="Modo:")
        self.anterior = widgets.Button(description="Anterior", icon="arrow-left")
        self.siguiente = widgets.Button(description="Siguiente", icon="arrow-right", button_style="primary")
        self.reiniciar = widgets.Button(description="Reiniciar", icon="refresh")
        self.reproducir = widgets.Button(description="Reproducir", icon="play")
        self.pausar = widgets.Button(description="Pausar", icon="pause")
        self.exportar = widgets.Button(description="Exportar PNG", icon="download")
        self.velocidad = widgets.Dropdown(options=[("Lenta", 1800), ("Normal", 1100), ("Rápida", 600)], value=1100, description="Velocidad:")
        self.play = widgets.Play(value=0, min=0, max=0, interval=1100)
        self.paso = widgets.IntSlider(value=0, min=0, max=0, description="Paso:", continuous_update=False)
        widgets.jslink((self.play, "value"), (self.paso, "value"))
        self.respuesta = widgets.RadioButtons(options=["intercambiar con el padre", "intercambiar con hijo izquierdo", "intercambiar con hijo derecho", "detener"], description="¿Qué sigue?")
        self.comprobar = widgets.Button(description="Comprobar", icon="check")
        self.revelar = widgets.Button(description="Revelar", icon="eye")
        self.mensaje = widgets.HTML(); self.progreso = widgets.HTML(); self.salida = widgets.Output()
        self._conectar(); self._cambiar()

    @property
    def estados(self): return self.catalogo[self.ejemplo.value]["estados"]

    def _conectar(self):
        self.ejemplo.observe(self._cambiar, names="value"); self.modo.observe(self._dibujar, names="value"); self.paso.observe(self._dibujar, names="value")
        self.velocidad.observe(lambda c: setattr(self.play, "interval", c["new"]), names="value")
        self.anterior.on_click(lambda _: setattr(self.paso, "value", max(0, self.paso.value - 1)))
        self.siguiente.on_click(lambda _: setattr(self.paso, "value", min(self.paso.max, self.paso.value + 1)))
        self.reiniciar.on_click(lambda _: setattr(self.paso, "value", 0))
        self.reproducir.on_click(lambda _: setattr(self.play, "playing", True)); self.pausar.on_click(lambda _: setattr(self.play, "playing", False))
        self.comprobar.on_click(self._comprobar); self.revelar.on_click(self._revelar); self.exportar.on_click(self._exportar)

    def _cambiar(self, _=None):
        self.paso.max = self.play.max = len(self.estados) - 1; self.paso.value = 0; self.mensaje.value = ""; self._dibujar()

    def _dibujar(self, _=None):
        estado = self.estados[self.paso.value].copy(); self.progreso.value = f"<b>Paso {self.paso.value + 1} de {len(self.estados)}</b>"
        reto = self.modo.value == "reto"
        if reto: estado["decision"] = "Decisión oculta: elige una opción y comprueba."
        for control in (self.respuesta, self.comprobar, self.revelar): control.layout.display = "" if reto else "none"
        with self.salida:
            clear_output(wait=True); figura = dibujar_estado(estado, len(self.estados)); display(figura); plt.close(figura)

    def _comprobar(self, _):
        correcta = self.respuesta.value == self.estados[self.paso.value].get("respuesta_reto", "detener")
        self.mensaje.value = "<b style='color:#15803d'>Correcto.</b> Justifica tu decisión." if correcta else "<b style='color:#b91c1c'>Revisa la comparación.</b>"

    def _revelar(self, _): self.mensaje.value = "Respuesta: <b>" + self.estados[self.paso.value].get("respuesta_reto", "detener") + "</b>."

    def _exportar(self, _):
        ruta = Path.cwd() / f"heap_paso_{self.paso.value + 1}.png"
        figura = dibujar_estado(self.estados[self.paso.value], len(self.estados)); figura.savefig(ruta, dpi=150, bbox_inches="tight"); plt.close(figura)
        self.mensaje.value = f"PNG exportado en <code>{ruta}</code>."

    def mostrar(self):
        interfaz = widgets.VBox([widgets.HBox([self.ejemplo, self.modo, self.velocidad]), widgets.HBox([self.reiniciar, self.anterior, self.siguiente, self.reproducir, self.pausar, self.exportar]), widgets.HBox([self.play, self.paso, self.progreso]), widgets.HBox([self.respuesta, self.comprobar, self.revelar]), self.mensaje, self.salida])
        display(interfaz); return interfaz


def mostrar_insercion_heap() -> VisualizadorHeapAlumno:
    """Crea la interfaz completa usada en el notebook de alumnos."""

    visualizador = VisualizadorHeapAlumno(); visualizador.mostrar(); return visualizador


def diagnosticar_widgets() -> dict[str, object]:
    """Diagnóstico corto para problemas de ejecución en Jupyter."""

    import ipywidgets
    return {"ipywidgets": ipywidgets.__version__, "archivo_estados": RUTA_ESTADOS.exists(), "ejemplos": len(cargar_estados()) if RUTA_ESTADOS.exists() else 0}
