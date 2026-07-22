# Clase 10: Recorridos de grafos, BFS, DFS y visualización

En la Clase 09 aprendimos a modelar relaciones con grafos.

Ahora queremos recorrer esos grafos.

La idea central de esta clase es que BFS y DFS no son recetas para memorizar. Son estrategias naturales:

- BFS aparece cuando exploramos por niveles.
- DFS aparece cuando exploramos tan profundo como sea posible antes de regresar.

## Pregunta guía

Ya sabemos representar un grafo. Ahora, ¿cómo lo recorremos?

## Objetivos

Al terminar la clase podrás:

- explicar qué significa recorrer un grafo;
- simular manualmente recorridos por niveles y por profundidad;
- explicar por qué BFS usa una cola;
- explicar por qué DFS usa una pila;
- implementar `bfs` y `dfs`;
- registrar la ejecución paso a paso;
- usar registros para visualización;
- generar `recorrido_visual.png`;
- diseñar pruebas propias;
- escribir una discusión técnica en Markdown.

## Problemas CSES

Usaremos estos problemas como motivación y aplicación:

- [Counting Rooms](https://cses.fi/problemset/task/1192/): componentes conectados en una cuadrícula.
- [Labyrinth](https://cses.fi/problemset/task/1193/): búsqueda de camino en un laberinto.
- [Message Route](https://cses.fi/problemset/task/1667/): rutas en una red no ponderada.

No usaremos caminos ponderados.

No introduciremos Dijkstra todavía.

## Estructura

```text
clase_10/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_10_recorridos_bfs_dfs.ipynb
├── practicas/
│   └── practica_10.md
├── src/
│   ├── init.py
│   └── recorridos.py
├── tests/
│   └── test_publico_recorridos.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Instalación

Desde `clase_10/`:

```bash
python3 -m pip install -r requirements.txt
```

## Cómo abrir la presentación

Abre directamente:

```text
presentacion/index.html
```

Atajos:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

La presentación incluye visualizaciones interactivas de BFS y DFS hechas con HTML, CSS y JavaScript puro.

## Cómo ejecutar el notebook

```bash
jupyter notebook notebooks/clase_10_recorridos_bfs_dfs.ipynb
```

No respondas dentro del `.ipynb`. Cada pregunta indica que debes responder en `notebook.md`.

## Cómo ejecutar pruebas públicas

Desde `clase_10/`:

```bash
pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si esto ocurre, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` usando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

Para probar una entrega dentro de `entregas/nombre/clase_10/`, puedes ejecutar:

```bash
PYTHONPATH=entregas/nombre/clase_10 pytest -v
```

## Entrega

No entregues el notebook `.ipynb` como evidencia principal.

Entrega:

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

`notebook.md` contiene respuestas del notebook y recorridos manuales. No debe contener código completo.

`discusion.md` es un documento técnico: argumenta diferencias entre BFS y DFS, uso de cola/pila, visualización, pruebas y CSES.

`reporte_pytest.md` debe incluir la salida completa de `pytest -v` o `python3 -m pytest -v`.

`recorrido_visual.png` puede ser una imagen estática del grafo con el recorrido o una captura generada con NetworkX y matplotlib.

Los GIFs completos no son obligatorios para alumnos.
