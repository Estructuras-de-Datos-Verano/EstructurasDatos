"""Explorador estudiantil de estados precomputados de lectura de código."""

from __future__ import annotations

import html
import json
from pathlib import Path

import ipywidgets as widgets
from IPython.display import display

RUTA_ESTADOS = Path(__file__).with_name("estados_lectura_codigo.json")


def cargar_estados() -> list[dict[str, object]]:
    """Carga el recorrido generado en el repositorio del profesor."""

    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


class ExploradorCodigoDijkstra:
    """Navega por contrato, código, invariante, riesgo y prueba."""

    def __init__(self) -> None:
        self.estados = cargar_estados()
        self.reiniciar = widgets.Button(description="Reiniciar", icon="refresh")
        self.anterior = widgets.Button(description="Anterior", icon="arrow-left")
        self.siguiente = widgets.Button(description="Siguiente", icon="arrow-right", button_style="primary")
        self.reproducir = widgets.Button(description="Reproducir", icon="play")
        self.pausar = widgets.Button(description="Pausar", icon="pause")
        self.velocidad = widgets.Dropdown(
            options=[("Lenta", 2600), ("Normal", 1700), ("Rápida", 900)],
            value=1700,
            description="Velocidad:",
        )
        self.play = widgets.Play(value=0, min=0, max=len(self.estados) - 1, interval=1700)
        self.paso = widgets.IntSlider(value=0, min=0, max=len(self.estados) - 1, description="Paso:", continuous_update=False)
        widgets.jslink((self.play, "value"), (self.paso, "value"))
        self.modo = widgets.ToggleButtons(options=[("Guiado", "guiado"), ("Reto", "reto")], description="Modo:")
        self.respuesta = widgets.RadioButtons(options=["contrato", "invariante", "riesgo", "prueba"], description="Primero leo:")
        self.comprobar = widgets.Button(description="Comprobar", icon="check")
        self.mensaje = widgets.HTML()
        self.salida = widgets.HTML()
        self._conectar()
        self._dibujar()

    def _conectar(self) -> None:
        self.paso.observe(self._dibujar, names="value")
        self.modo.observe(self._dibujar, names="value")
        self.velocidad.observe(lambda cambio: setattr(self.play, "interval", cambio["new"]), names="value")
        self.reiniciar.on_click(lambda _: setattr(self.paso, "value", 0))
        self.anterior.on_click(lambda _: setattr(self.paso, "value", max(0, self.paso.value - 1)))
        self.siguiente.on_click(lambda _: setattr(self.paso, "value", min(self.paso.max, self.paso.value + 1)))
        self.reproducir.on_click(lambda _: setattr(self.play, "playing", True))
        self.pausar.on_click(lambda _: setattr(self.play, "playing", False))
        self.comprobar.on_click(self._comprobar)

    def _dibujar(self, _=None) -> None:
        estado = self.estados[self.paso.value]
        codigo = "\n".join(
            f"<tr><td style='color:#64748b;padding-right:.8rem;text-align:right'>{linea['numero']}</td>"
            f"<td><code>{html.escape(linea['texto']) or '&nbsp;'}</code></td></tr>"
            for linea in estado["codigo"]
        )
        reto = self.modo.value == "reto"
        prueba = "Predice qué prueba protege este bloque." if reto else estado["prueba"]
        self.respuesta.layout.display = "" if reto else "none"
        self.comprobar.layout.display = "" if reto else "none"
        self.mensaje.value = ""
        self.salida.value = f"""
        <div style="font-family:system-ui;color:#172033">
          <h3>{html.escape(estado['titulo'])}</h3>
          <p><b>Paso {self.paso.value + 1} de {len(self.estados)} · {html.escape(estado['funcion'])}</b></p>
          <p>{html.escape(estado['objetivo'])}</p>
          <table style="width:100%;background:#f8fafc;padding:.6rem;white-space:pre-wrap">{codigo}</table>
          <p><b>Contrato:</b> {html.escape(estado['contrato'])}</p>
          <p><b>Invariante:</b> {html.escape(estado['invariante'])}</p>
          <p><b>Riesgo:</b> {html.escape(estado['riesgo'])}</p>
          <p><b>Prueba:</b> {html.escape(prueba)}</p>
          <p><b>Pregunta:</b> {html.escape(estado['pregunta'])}</p>
        </div>"""

    def _comprobar(self, _) -> None:
        correcta = self.respuesta.value == "contrato"
        self.mensaje.value = (
            "<b style='color:#15803d'>Correcto:</b> empieza por el contrato y úsalo para juzgar el cuerpo."
            if correcta
            else "<b style='color:#b91c1c'>Reordena:</b> primero contrato; luego invariante, riesgo y prueba."
        )

    def mostrar(self):
        """Muestra controles y recorrido en el notebook."""

        interfaz = widgets.VBox([
            widgets.HBox([self.modo, self.velocidad]),
            widgets.HBox([self.reiniciar, self.anterior, self.siguiente, self.reproducir, self.pausar]),
            widgets.HBox([self.play, self.paso]),
            widgets.HBox([self.respuesta, self.comprobar]),
            self.mensaje,
            self.salida,
        ])
        display(interfaz)
        return interfaz


def mostrar_lectura_codigo() -> ExploradorCodigoDijkstra:
    """Crea y muestra el explorador completo."""

    explorador = ExploradorCodigoDijkstra()
    explorador.mostrar()
    return explorador


def diagnosticar_widgets() -> dict[str, object]:
    """Reporta dependencias y cantidad de estados disponibles."""

    import ipywidgets

    return {
        "ipywidgets": ipywidgets.__version__,
        "archivo_estados": RUTA_ESTADOS.exists(),
        "estados": len(cargar_estados()) if RUTA_ESTADOS.exists() else 0,
    }

