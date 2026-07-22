# Clase 09: Modelado de relaciones con grafos y NetworkX

En clases anteriores muchos problemas se modelaron como secuencias. En esta clase empezamos a modelar relaciones:

- personas conectadas con personas;
- ciudades conectadas por caminos;
- habitaciones conectadas por puertas;
- páginas conectadas por enlaces;
- tareas conectadas por dependencias.

Un grafo no es solamente un dibujo. Un grafo es una estructura matemática para representar relaciones. El dibujo es una visualización.

## Pregunta guía

¿Cómo representamos relaciones entre objetos y cómo elegimos una implementación adecuada?

## Objetivos

Al terminar la clase podrás:

- explicar qué es un grafo;
- identificar nodos y aristas en un problema;
- distinguir grafos dirigidos, no dirigidos, ponderados y no ponderados;
- representar grafos con lista de adyacencia y matriz de adyacencia;
- usar una interfaz común para varias implementaciones;
- probar ambas implementaciones con las mismas pruebas;
- usar NetworkX para visualizar y validar ideas;
- escribir una discusión técnica en Markdown.

## Problemas motivadores CSES

No resolveremos estos problemas por completo. Los usaremos para modelar.

- [Building Roads](https://cses.fi/problemset/task/1666/)
- [Counting Rooms](https://cses.fi/problemset/task/1192/)
- [Labyrinth](https://cses.fi/problemset/task/1193/)
- [Message Route](https://cses.fi/problemset/task/1667/)

Para cada problema pregunta:

- ¿qué representa un nodo?
- ¿qué representa una arista?
- ¿el grafo es dirigido?
- ¿tiene pesos?
- ¿qué pregunta algorítmica aparece?

## Estructura

```text
clase_09/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_09_modelado_grafos_networkx.ipynb
├── practicas/
│   └── practica_09.md
├── src/
│   ├── init.py
│   └── grafos.py
├── tests/
│   └── test_publico_grafos.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Instalación

Desde `clase_09/`:

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

## Cómo ejecutar el notebook

```bash
jupyter notebook notebooks/clase_09_modelado_grafos_networkx.ipynb
```

No respondas dentro del `.ipynb`. Cada pregunta indica que debes responder en `notebook.md`.

## Cómo ejecutar pruebas públicas

Desde `clase_09/`:

```bash
pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si esto ocurre, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` usando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

Para probar una entrega dentro de `entregas/nombre/clase_09/`, puedes ejecutar:

```bash
PYTHONPATH=entregas/nombre/clase_09 pytest -v
```

## Entrega

No entregues el notebook `.ipynb` como evidencia principal.

Entrega:

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

`notebook.md` contiene respuestas del notebook y no debe contener código completo.

`discusion.md` es un documento técnico: argumenta decisiones de modelado, representación, pruebas y visualización.

`reporte_pytest.md` debe incluir la salida completa de `pytest -v` o `python3 -m pytest -v`.

`grafo_visual.png` debe ser una visualización generada con NetworkX y matplotlib. Si no puedes generarla por un problema técnico, explícalo en `reporte_pytest.md` o `discusion.md`.

## Nota sobre NetworkX

NetworkX no reemplaza nuestra implementación. Nuestra implementación sirve para entender cómo se representa internamente un grafo; NetworkX sirve para explorar, visualizar y validar ideas.
