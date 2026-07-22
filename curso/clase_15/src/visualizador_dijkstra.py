"""Visualizador estudiantil; consume estados y no implementa Dijkstra."""

from __future__ import annotations

import json
from pathlib import Path

import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import clear_output, display
from matplotlib.patches import FancyArrowPatch

RUTA_ESTADOS = Path(__file__).with_name("estados_dijkstra.json")
COLORES = {"neutral":"#dce4ef","actual":"#3b82f6","arista":"#f59e0b","mejora":"#22c55e","obsoleta":"#ef4444","linea":"#64748b"}


def cargar_estados() -> dict:
    """Carga el catálogo precomputado por el repositorio del profesor."""

    return json.loads(RUTA_ESTADOS.read_text(encoding="utf-8"))


def dibujar_estado(estado: dict, total: int):
    """Dibuja grafo, distancias y cola de prioridad sincronizados."""

    figura, (grafo_ax, detalle) = plt.subplots(1,2,figsize=(13,6),gridspec_kw={"width_ratios":[1.45,1]},constrained_layout=True)
    figura.suptitle(f"{estado['titulo']} · Paso {estado['paso']+1} de {total}", fontsize=18, weight="bold")
    posiciones={n:tuple(p) for n,p in estado["posiciones"].items()}; activa=tuple(estado["arista_actual"]) if estado.get("arista_actual") else None
    for a in estado["aristas"]:
        u,v,peso=a["origen"],a["destino"],a["peso"]; x1,y1=posiciones[u]; x2,y2=posiciones[v]; color=COLORES["arista"] if activa==(u,v) else COLORES["linea"]
        grafo_ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=16,linewidth=2.5 if activa==(u,v) else 1.4,color=color,shrinkA=24,shrinkB=24)); grafo_ax.text((x1+x2)/2,(y1+y2)/2+.035,f"{peso:g}",ha="center")
    destino=activa[1] if activa else None
    for nodo,(x,y) in posiciones.items():
        color=COLORES["obsoleta"] if estado.get("entrada_obsoleta") and nodo==estado.get("nodo_actual") else COLORES["actual"] if nodo==estado.get("nodo_actual") else COLORES["mejora"] if nodo==destino else COLORES["neutral"]
        grafo_ax.scatter(x,y,s=1450,color=color,edgecolor="#172033",zorder=3); d=estado["distancias"][nodo]; grafo_ax.text(x,y+.012,nodo,ha="center",weight="bold",zorder=4); grafo_ax.text(x,y-.075,"d="+("∞" if d is None else f"{d:g}"),ha="center",fontsize=9,zorder=4)
    grafo_ax.set(xlim=(0,1),ylim=(0,1),title="Red ponderada"); grafo_ax.axis("off")
    detalle.axis("off"); detalle.set_title("Tabla, heap y decisión",loc="left")
    filas="\n".join(f"{n}: d={'∞' if estado['distancias'][n] is None else format(estado['distancias'][n],'g')}, pred={estado['predecesores'][n] or '—'}" for n in estado["nodos"]); cola="  ".join(f"({d:g},{n})" for d,n in estado["cola_prioridad"]) or "∅"
    texto=f"DISTANCIAS\n{filas}\n\nHEAP\n{cola}\n\nACCIÓN\n{estado['accion']}\n\nCOMPARACIÓN\n{estado['comparacion']}\n\nDECISIÓN\n{estado['decision']}\n\nLÍNEA ACTIVA\n▶ {estado['linea_pseudocodigo']}\n\n{estado['mensaje']}"; detalle.text(0,.98,texto,va="top",fontsize=10.2,wrap=True)
    return figura


class VisualizadorDijkstraAlumno:
    """Interfaz guiada y modo reto sobre registros ya preparados."""

    def __init__(self):
        self.catalogo=cargar_estados(); self.ejemplo=widgets.Dropdown(options=[(d["nombre"],k) for k,d in self.catalogo.items()],description="Ejemplo:"); self.modo=widgets.ToggleButtons(options=[("Guiado","guiado"),("Reto","reto")],description="Modo:")
        self.reiniciar=widgets.Button(description="Reiniciar",icon="refresh"); self.anterior=widgets.Button(description="Anterior",icon="arrow-left"); self.siguiente=widgets.Button(description="Siguiente",icon="arrow-right",button_style="primary"); self.reproducir=widgets.Button(description="Reproducir",icon="play"); self.pausar=widgets.Button(description="Pausar",icon="pause"); self.exportar=widgets.Button(description="Exportar PNG",icon="download")
        self.velocidad=widgets.Dropdown(options=[("Lenta",2000),("Normal",1200),("Rápida",650)],value=1200,description="Velocidad:"); self.play=widgets.Play(value=0,min=0,max=0,interval=1200); self.paso=widgets.IntSlider(value=0,min=0,max=0,description="Paso:",continuous_update=False); widgets.jslink((self.play,"value"),(self.paso,"value"))
        self.respuesta=widgets.RadioButtons(options=["extraer el mínimo","relajar vecinos","actualizar distancia","conservar distancia","ignorar entrada obsoleta","detener"],description="¿Qué sigue?"); self.comprobar=widgets.Button(description="Comprobar"); self.revelar=widgets.Button(description="Revelar"); self.mensaje=widgets.HTML(); self.progreso=widgets.HTML(); self.salida=widgets.Output(); self._conectar(); self._cambiar()

    @property
    def estados(self): return self.catalogo[self.ejemplo.value]["estados"]
    def _conectar(self):
        self.ejemplo.observe(self._cambiar,names="value"); self.modo.observe(self._dibujar,names="value"); self.paso.observe(self._dibujar,names="value"); self.velocidad.observe(lambda c:setattr(self.play,"interval",c["new"]),names="value"); self.reiniciar.on_click(lambda _:setattr(self.paso,"value",0)); self.anterior.on_click(lambda _:setattr(self.paso,"value",max(0,self.paso.value-1))); self.siguiente.on_click(lambda _:setattr(self.paso,"value",min(self.paso.max,self.paso.value+1))); self.reproducir.on_click(lambda _:setattr(self.play,"playing",True)); self.pausar.on_click(lambda _:setattr(self.play,"playing",False)); self.comprobar.on_click(self._comprobar); self.revelar.on_click(self._revelar); self.exportar.on_click(self._exportar)
    def _cambiar(self,_=None): self.play.max=self.paso.max=len(self.estados)-1; self.paso.value=0; self.mensaje.value=""; self._dibujar()
    def _dibujar(self,_=None):
        estado=self.estados[self.paso.value].copy(); reto=self.modo.value=="reto"; estado["decision"]="Decisión oculta: predice antes de revelar." if reto else estado["decision"]; self.progreso.value=f"<b>Paso {self.paso.value+1} de {len(self.estados)}</b>"; [setattr(c.layout,"display","" if reto else "none") for c in (self.respuesta,self.comprobar,self.revelar)]
        with self.salida: clear_output(wait=True); figura=dibujar_estado(estado,len(self.estados)); display(figura); plt.close(figura)
    def _comprobar(self,_): self.mensaje.value="<b>Correcto.</b> Justifica con la comparación." if self.respuesta.value==self.estados[self.paso.value]["respuesta_reto"] else "<b>Revisa distancia, candidata y heap.</b>"
    def _revelar(self,_): self.mensaje.value="Respuesta: <b>"+self.estados[self.paso.value]["respuesta_reto"]+"</b>."
    def _exportar(self,_):
        ruta=Path.cwd()/f"dijkstra_paso_{self.paso.value+1}.png"; figura=dibujar_estado(self.estados[self.paso.value],len(self.estados)); figura.savefig(ruta,dpi=150,bbox_inches="tight"); plt.close(figura); self.mensaje.value=f"PNG exportado en <code>{ruta}</code>."
    def mostrar(self):
        interfaz=widgets.VBox([widgets.HBox([self.ejemplo,self.modo,self.velocidad]),widgets.HBox([self.reiniciar,self.anterior,self.siguiente,self.reproducir,self.pausar,self.exportar]),widgets.HBox([self.play,self.paso,self.progreso]),widgets.HBox([self.respuesta,self.comprobar,self.revelar]),self.mensaje,self.salida]); display(interfaz); return interfaz


def mostrar_dijkstra() -> VisualizadorDijkstraAlumno:
    """Crea y muestra el visualizador utilizado por el notebook."""

    visualizador=VisualizadorDijkstraAlumno(); visualizador.mostrar(); return visualizador


def diagnosticar_widgets() -> dict[str, object]:
    """Informa versión, existencia de estados y cantidad de ejemplos."""

    import ipywidgets
    return {"ipywidgets":ipywidgets.__version__,"archivo_estados":RUTA_ESTADOS.exists(),"ejemplos":len(cargar_estados()) if RUTA_ESTADOS.exists() else 0}

