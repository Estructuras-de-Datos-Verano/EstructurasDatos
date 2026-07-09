# Clase 12: Altura, balance y eficiencia en BST

En la Clase 11 implementaste un árbol binario de búsqueda.

En esta clase veremos que implementar correctamente un BST no garantiza búsquedas rápidas. La eficiencia depende de la altura.

## Pregunta guía

¿Un BST siempre es mejor que una lista?

## Objetivos

Al terminar la clase podrás:

- explicar altura y profundidad;
- distinguir un árbol balanceado de un árbol degenerado;
- relacionar altura con comparaciones de búsqueda;
- explicar por qué un BST puede convertirse en una lista;
- comparar mejor caso, caso promedio y peor caso;
- extender un BST con métodos de análisis;
- usar `evaluar.py` con tests públicos y tests extra;
- revisar técnicamente el PR de un compañero ejecutando tus propias pruebas.

## Estructura

```text
clase_12/
├── presentacion/
│   └── index.html
├── notebooks/
│   ├── clase_12_altura_balance_bst.ipynb
│   └── gifs/
│       ├── busqueda_balanceado.gif
│       ├── busqueda_degenerado.gif
│       ├── insercion_balanceada.gif
│       ├── insercion_degenerada.gif
│       └── lista_vs_bst.gif
├── practicas/
│   └── practica_12.md
├── src/
│   ├── __init__.py
│   └── bst_balance.py
├── tests/
│   └── test_publico_bst_balance.py
├── pytest.ini
├── README.md
└── requirements.txt
```

Además, en la raíz del repositorio:

```text
evaluar.py
```

## Instalación

Desde `clase_12/`:

```bash
python3 -m pip install -r requirements.txt
```

## Presentación

Abre directamente:

```text
presentacion/index.html
```

La presentación es autocontenida e incluye los GIFs integrados.

## Notebook

```bash
jupyter notebook notebooks/clase_12_altura_balance_bst.ipynb
```

No respondas dentro del `.ipynb`.

Todas las respuestas van en `notebook.md`.

## Ejecutar pruebas

Desde la raíz de `curso-alumnos`:

macOS / Linux:

```bash
python3 evaluar.py entregas/clase_12/nombre clase_12/tests
```

Windows PowerShell:

```powershell
py evaluar.py entregas/clase_12/nombre clase_12/tests
```

o:

```powershell
python evaluar.py entregas/clase_12/nombre clase_12/tests
```

Con tests extra:

```bash
python3 evaluar.py entregas/clase_12/nombre clase_12/tests entregas/clase_12/mi_nombre/test_estudiante.py
```

## Entrega

```text
entregas/
└── clase_12/
    └── nombre/
        ├── implementacion.py
        ├── test_estudiante.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

`implementacion.py` contiene tu BST extendido.

`test_estudiante.py` contiene al menos 3 pruebas propias.

`notebook.md` contiene respuestas guiadas del notebook.

`discusion.md` argumenta técnicamente altura, degeneración, balance, complejidad, pruebas y revisión de PR.

`reporte_pytest.md` contiene salida completa de `evaluar.py`.

## Problemas relacionados

LeetCode:

- 104 — Maximum Depth of Binary Tree.
- 110 — Balanced Binary Tree.
- 222 — Count Complete Tree Nodes.
- 700 — Search in a Binary Search Tree.
- 701 — Insert into a Binary Search Tree.
- 98 — Validate Binary Search Tree.

CSES:

- Subordinates: https://cses.fi/problemset/task/1674/
- Tree Diameter: https://cses.fi/problemset/task/1131/
- Company Queries I: https://cses.fi/problemset/task/1687/
