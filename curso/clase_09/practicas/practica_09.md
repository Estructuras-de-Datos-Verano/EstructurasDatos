# Práctica 09: Grafos, representaciones y NetworkX

## Contexto

Esta práctica marca un cambio de modelo: pasamos de secuencias a relaciones.

Usaremos grafos para representar conexiones entre objetos y compararemos dos implementaciones polimórficas:

- `GrafoListaAdyacencia`;
- `GrafoMatrizAdyacencia`.

También usaremos NetworkX para visualizar grafos. NetworkX no sustituye tu implementación: te ayuda a explorar, dibujar y validar ideas.

## Objetivos

Al terminar esta práctica podrás:

- identificar nodos y aristas en problemas sencillos;
- distinguir grafos dirigidos/no dirigidos y ponderados/no ponderados;
- implementar un grafo no dirigido simple con lista de adyacencia;
- implementar un grafo no dirigido simple con matriz de adyacencia;
- usar polimorfismo para probar ambas implementaciones;
- convertir una implementación propia a NetworkX;
- generar `grafo_visual.png`;
- escribir una discusión técnica con contraste.

## Instrucciones

1. Revisa el notebook.
2. Responde sus preguntas en `notebook.md`.
3. Implementa `GrafoListaAdyacencia` en `implementacion.py`.
4. Implementa `GrafoMatrizAdyacencia` en `implementacion.py`.
5. Implementa `convertir_a_networkx`.
6. Genera `grafo_visual.png`.
7. Completa o diseña las pruebas públicas marcadas con TODO.
8. Ejecuta `pytest -v`.
9. Crea `reporte_pytest.md`.
10. Escribe `discusion.md`.
11. Abre Pull Request.
12. Revisa el PR asignado por `asignar_revisiones.py`.

No respondas preguntas dentro del notebook.

No entregues el notebook `.ipynb` como evidencia principal.

No modifiques `main`.

No modifiques tests públicos salvo los TODOs explícitos.

Trabaja en:

```text
entregas/nombre/clase_09/
```

Usa Markdown para que GitHub permita una revisión clara.

## Entrega obligatoria

```text
entregas/
└── clase_09/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        ├── reporte_pytest.md
        └── grafo_visual.png
```

Si por alguna razón técnica no puedes generar `grafo_visual.png`, explica el problema en `reporte_pytest.md` o `discusion.md`.

## `implementacion.py`

Debe contener tu solución.

Debe definir:

```python
class GrafoAbstracto:
    ...

class GrafoListaAdyacencia(GrafoAbstracto):
    ...

class GrafoMatrizAdyacencia(GrafoAbstracto):
    ...

def construir_grafo_ejemplo() -> GrafoListaAdyacencia:
    ...

def convertir_a_networkx(grafo: GrafoAbstracto):
    ...

def guardar_visualizacion_grafo(grafo: GrafoAbstracto, ruta: str = "grafo_visual.png") -> None:
    ...
```

No debe ejecutar visualizaciones al importarse.

No debe contener código de pruebas.

Puede incluir funciones auxiliares si ayudan a la claridad.

## `notebook.md`

Contiene tus respuestas a las preguntas del notebook, en el mismo orden.

No debe contener código completo.

Estructura sugerida:

```text
# Notebook - Clase 09

## 1. Problemas motivadores CSES
## 2. Modelado de relaciones
## 3. Conceptos básicos de grafos
## 4. Representaciones
## 5. Interfaz común
## 6. Implementaciones
## 7. Visualización con NetworkX
## 8. Diseño de pruebas
## 9. Patrón descubierto
## 10. Cierre
```

## `discusion.md`

Debe contener:

1. De secuencias a relaciones.
2. Problemas CSES.
3. Elección de representación.
4. Polimorfismo.
5. NetworkX.
6. Pruebas.
7. Patrón descubierto.
8. Pregunta abierta.

No debe repetir literalmente `notebook.md`.

## `reporte_pytest.md`

Debe contener:

- comando ejecutado;
- salida completa;
- interpretación;
- cuántas pruebas se ejecutaron;
- cuántas pasaron;
- si hubo errores;
- qué comportamiento verifican;
- qué prueba diseñaste tú;
- qué caso todavía falta probar.

Usa:

```bash
pytest -v
```

o:

```bash
python3 -m pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si esto ocurre, utiliza `python3 -m pytest -v`.

## Actividad GitHub

Cada alumno debe:

- crear una rama `clase-09-tu-nombre`;
- trabajar en su carpeta;
- hacer commits claros;
- abrir Pull Request;
- revisar el PR asignado;
- comentar al menos una cosa sobre claridad de explicación, modelado de nodos/aristas, elección de representación, prueba diseñada, visualización o redacción técnica.

## Checklist

- [ ] Respondí preguntas del notebook en `notebook.md`.
- [ ] `notebook.md` no contiene código completo.
- [ ] Implementé `GrafoListaAdyacencia`.
- [ ] Implementé `GrafoMatrizAdyacencia`.
- [ ] Implementé `convertir_a_networkx`.
- [ ] Generé `grafo_visual.png` o expliqué por qué no pude generarlo.
- [ ] Completé o diseñé pruebas en TODOs explícitos.
- [ ] Ejecuté `pytest -v` o `python3 -m pytest -v`.
- [ ] Escribí `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Expliqué cuándo usar lista de adyacencia.
- [ ] Expliqué cuándo usar matriz de adyacencia.
- [ ] Abrí PR.
- [ ] Revisé el PR asignado.
- [ ] No modifiqué `main`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| `notebook.md` y modelado de problemas | 15 |
| Implementación de grafos | 25 |
| Visualización con NetworkX | 15 |
| Diseño y ejecución de pruebas | 15 |
| `discusion.md` y redacción técnica | 20 |
| GitHub y revisión | 10 |

Total: 100 puntos.
