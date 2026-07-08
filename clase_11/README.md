# Clase 11: Árboles binarios de búsqueda

Una lista guarda datos en secuencia.

Un árbol organiza datos de forma jerárquica.

En esta clase estudiaremos árboles binarios de búsqueda, BST, como una forma de organizar datos cuando necesitamos buscar muchas veces.

## Pregunta guía

¿Cómo podemos organizar datos para buscar más eficientemente que en una lista?

## Objetivos

Al terminar la clase podrás:

- explicar qué es un árbol, un nodo, una raíz, una hoja y la altura;
- explicar qué significa que un árbol sea binario;
- enunciar el invariante de un árbol binario de búsqueda;
- insertar y buscar valores en un BST;
- calcular la altura de un árbol;
- recorrer un árbol en preorden, inorden y postorden;
- explicar por qué inorden devuelve valores ordenados en un BST;
- reconocer cuándo un BST puede degradarse;
- escribir pruebas propias;
- usar `evaluar.py` para ejecutar pruebas públicas sobre una entrega;
- escribir discusión técnica en Markdown.

## Problemas relacionados

Usaremos estos problemas como mapa de práctica y motivación:

- LeetCode 94: Binary Tree Inorder Traversal.
- LeetCode 144: Binary Tree Preorder Traversal.
- LeetCode 145: Binary Tree Postorder Traversal.
- LeetCode 700: Search in a Binary Search Tree.
- LeetCode 701: Insert into a Binary Search Tree.
- CSES Subordinates: https://cses.fi/problemset/task/1674/

No resolveremos todos durante la clase.

## Estructura

```text
clase_11/
├── presentacion/
│   └── index.html
├── notebooks/
│   ├── clase_11_arboles_bst.ipynb
│   └── gifs/
│       ├── insercion_bst.gif
│       ├── busqueda_bst.gif
│       ├── recorrido_inorden.gif
│       ├── recorrido_preorden.gif
│       └── recorrido_postorden.gif
├── practicas/
│   └── practica_11.md
├── src/
│   ├── __init__.py
│   └── arboles.py
├── tests/
│   └── test_publico_arboles.py
├── pytest.ini
├── README.md
└── requirements.txt
```

Además, en la raíz del repositorio está:

```text
evaluar.py
```

## Instalación

Desde `clase_11/`:

```bash
python3 -m pip install -r requirements.txt
```

## Cómo abrir la presentación

Abre directamente:

```text
presentacion/index.html
```

La presentación es un archivo HTML autocontenido. Incluye navegación, notas del profesor, temporizador y GIFs integrados.

Atajos:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

```bash
jupyter notebook notebooks/clase_11_arboles_bst.ipynb
```

No respondas dentro del `.ipynb`.

Cada pregunta del notebook debe responderse en `notebook.md`.

## Cómo ejecutar pruebas públicas

A partir de esta clase, las pruebas públicas importan directamente:

```python
from implementacion import ArbolBinarioBusqueda, Nodo
```

Por eso debes usar el evaluador desde la raíz de `curso-alumnos`:

```bash
python3 evaluar.py entregas/clase_11/nombre clase_11/tests
```

El script agrega tu carpeta de entrega al entorno de Python y ejecuta internamente:

```bash
pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si necesitas ejecutar pytest directamente, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` usando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

## Entrega

No entregues el notebook `.ipynb` como evidencia principal.

Entrega:

```text
entregas/
└── clase_11/
    └── nombre/
        ├── implementacion.py
        ├── test_estudiante.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

`implementacion.py` contiene tu solución del BST.

`test_estudiante.py` contiene al menos 3 pruebas propias.

`notebook.md` contiene respuestas guiadas del notebook. No debe contener código completo.

`discusion.md` es un documento técnico: argumenta lista vs árbol, invariante, inserción, recorridos, altura, pruebas, `evaluar.py` y problemas relacionados.

`reporte_pytest.md` debe incluir la salida completa del comando:

```bash
python3 evaluar.py entregas/clase_11/nombre clase_11/tests
```

## Archivos de apoyo

- `src/arboles.py`: firmas, docstrings y estructura base. No contiene soluciones completas.
- `tests/test_publico_arboles.py`: pruebas públicas y algunos TODOs guiados.
- `notebooks/gifs/`: GIFs de inserción, búsqueda e inorden, preorden y postorden.

Puedes usar `src/arboles.py` como molde para crear tu `entregas/clase_11/nombre/implementacion.py`.

Los alumnos no programan las animaciones en esta clase.
