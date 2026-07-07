# Práctica 10: Recorridos de grafos con BFS y DFS

## Contexto

En la Clase 09 aprendimos a representar relaciones con grafos.

En esta práctica aprenderás a recorrerlos. Primero trabajarás recorridos manuales sin nombres formales. Después reconocerás esas estrategias como:

- Breadth-First Search, BFS;
- Depth-First Search, DFS.

La meta no es memorizar una plantilla. La meta es entender qué información debe mantenerse durante el recorrido y por qué aparecen una cola y una pila.

## Objetivos

Al terminar esta práctica podrás:

- simular recorridos de grafos a mano;
- distinguir exploración por niveles y por profundidad;
- implementar `bfs`;
- implementar `dfs`;
- registrar la ejecución paso a paso;
- interpretar cola, pila, visitados y nodo actual;
- generar `recorrido_visual.png`;
- diseñar pruebas propias;
- escribir una discusión técnica.

## Instrucciones

1. Revisa el notebook.
2. Responde sus preguntas en `notebook.md`.
3. Completa recorridos manuales en `notebook.md`.
4. Implementa `bfs` en `implementacion.py`.
5. Implementa `dfs` en `implementacion.py`.
6. Implementa `registrar_bfs` y `registrar_dfs`.
7. Genera `recorrido_visual.png`.
8. Completa o diseña las pruebas públicas marcadas con TODO.
9. Ejecuta `pytest -v`.
10. Crea `reporte_pytest.md`.
11. Escribe `discusion.md`.
12. Abre Pull Request.
13. Revisa el PR asignado por `asignar_revisiones.py`.

No respondas preguntas dentro del notebook.

No entregues el notebook `.ipynb` como evidencia principal.

No modifiques `main`.

No modifiques tests públicos salvo los TODOs explícitos.

Trabaja en:

```text
entregas/clase_10/nombre/
```

Usa Markdown para que GitHub permita una revisión clara.

Los GIFs completos no son obligatorios para alumnos.

## Entrega obligatoria

```text
entregas/
└── clase_10/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        ├── reporte_pytest.md
        └── recorrido_visual.png
```

Si por alguna razón técnica no puedes generar `recorrido_visual.png`, explica el problema en `reporte_pytest.md` o `discusion.md`.

## `implementacion.py`

Debe contener tu solución.

Debe definir:

```python
def bfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    ...

def dfs(grafo: dict[str, list[str]], origen: str) -> list[str]:
    ...

def registrar_bfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    ...

def registrar_dfs(grafo: dict[str, list[str]], origen: str) -> list[dict]:
    ...

def guardar_visualizacion_recorrido(
    grafo: dict[str, list[str]],
    recorrido: list[str],
    ruta: str = "recorrido_visual.png",
) -> None:
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
# Notebook - Clase 10

## 1. Problemas CSES
## 2. Recorridos manuales sin nombres
## 3. Estrategia por niveles
## 4. Estrategia por profundidad
## 5. Nacen BFS y DFS
## 6. Pseudocódigo
## 7. Registro paso a paso
## 8. Visualización
## 9. Diseño de pruebas
## 10. Patrón descubierto
## 11. Cierre
```

## `discusion.md`

Debe contener:

1. De representar a recorrer.
2. Estrategias manuales.
3. BFS.
4. DFS.
5. Comparación.
6. Visualización.
7. CSES.
8. Pruebas.
9. Patrón descubierto.
10. Pregunta abierta.

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

- crear una rama `clase-10-tu-nombre`;
- trabajar en su carpeta;
- hacer commits claros;
- abrir Pull Request;
- revisar el PR asignado;
- comentar al menos una cosa sobre claridad de explicación, recorrido manual, uso de cola o pila, prueba diseñada, visualización o redacción técnica.

## Checklist

- [ ] Respondí preguntas del notebook en `notebook.md`.
- [ ] Completé recorridos manuales en `notebook.md`.
- [ ] `notebook.md` no contiene código completo.
- [ ] Implementé `bfs`.
- [ ] Implementé `dfs`.
- [ ] Implementé `registrar_bfs`.
- [ ] Implementé `registrar_dfs`.
- [ ] Generé `recorrido_visual.png` o expliqué por qué no pude generarlo.
- [ ] Completé o diseñé pruebas en TODOs explícitos.
- [ ] Ejecuté `pytest -v` o `python3 -m pytest -v`.
- [ ] Escribí `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Expliqué por qué BFS usa cola.
- [ ] Expliqué por qué DFS usa pila.
- [ ] Abrí PR.
- [ ] Revisé el PR asignado.
- [ ] No modifiqué `main`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| `notebook.md` y recorridos manuales | 20 |
| Implementación BFS/DFS | 25 |
| Registro paso a paso y visualización | 15 |
| Diseño y ejecución de pruebas | 15 |
| `discusion.md` y redacción técnica | 15 |
| GitHub y revisión | 10 |

Total: 100 puntos.
