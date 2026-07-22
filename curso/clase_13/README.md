# Clase 13: Árboles AVL

En la Clase 12 vimos que un BST puede degenerarse hasta parecer una lista.

La pregunta de esta clase es:

> Si un BST puede convertirse en una lista, ¿cómo podemos impedirlo?

Un árbol AVL responde manteniendo una propiedad adicional: el balance local de
cada nodo. No cambia el invariante de BST; añade rotaciones para conservar baja
la altura.

> [!IMPORTANT]
> En esta clase no implementamos eliminación. Nos concentramos en inserción,
> rotaciones, pruebas y revisión técnica.

## Objetivos

Al terminar la clase podrás:

- explicar qué significa que un árbol esté balanceado;
- calcular factores de balance;
- identificar casos `LL`, `RR`, `LR` y `RL`;
- comprender por qué las rotaciones preservan el invariante del BST;
- implementar rotaciones;
- implementar inserción AVL;
- diseñar pruebas para rotaciones;
- revisar implementaciones de otros alumnos;
- escribir documentación técnica profesional.

## Estructura

```text
clase_13/
├── presentacion/
│   └── index.html
├── notebooks/
│   ├── clase_13_avl.ipynb
│   └── gifs/
│       ├── avl_ll_rotacion_derecha.gif
│       ├── avl_rr_rotacion_izquierda.gif
│       ├── avl_lr_rotacion_doble.gif
│       ├── avl_rl_rotacion_doble.gif
│       ├── avl_{ll,rr,lr,rl}_nivel_2_local.gif
│       ├── avl_{ll,rr,lr,rl}_nivel_3_evolucion.gif
│       ├── avl_sin_rotacion.gif
│       ├── avl_multiples_rotaciones.gif
│       └── bst_vs_avl.gif
├── practicas/
│   ├── practica_13.md
│   ├── guia_markdown.md
│   ├── guia_revision_pr.md
│   └── guia_github.md
├── src/
│   ├── __init__.py
│   └── avl.py
├── tests/
│   └── test_publico_avl.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Instalación

Desde `clase_13/`:

macOS / Linux:

```bash
python3 -m pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m pip install -r requirements.txt
```

## Presentación

Abre directamente:

```text
presentacion/index.html
```

La presentación funciona sin internet y referencia los GIFs locales de
`notebooks/gifs/`.

## Notebook

```bash
jupyter notebook notebooks/clase_13_avl.ipynb
```

No respondas dentro del `.ipynb`.

Todas tus respuestas van en `notebook.md`.

## Guías de apoyo

Antes de comenzar consulta:

- [Guía de Markdown](practicas/guia_markdown.md)
- [Guía de GitHub](practicas/guia_github.md)
- [Guía de revisión de PR](practicas/guia_revision_pr.md)

## Ejecutar pruebas

Desde la raíz de `curso-alumnos`:

macOS / Linux:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

Windows PowerShell:

```powershell
py scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

o:

```powershell
python scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

> [!TIP]
> `scripts/evaluar.py` ejecuta internamente `pytest -v`, por eso el reporte debe pegar
> la salida completa y detallada.

## Entrega

```text
entregas/
└── clase_13/
    └── nombre/
        ├── implementacion.py
        ├── test_estudiante.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

Además, durante la revisión de PR debes agregar un archivo dentro de la carpeta
del compañero revisado:

```text
entregas/aristeo/clase_13/revision_max.md
```

## Problemas relacionados

LeetCode:

- 110 — Balanced Binary Tree.
- 98 — Validate Binary Search Tree.
- 701 — Insert into a Binary Search Tree.
- 1382 — Balance a Binary Search Tree.
- 104 — Maximum Depth of Binary Tree.

CSES:

- Subordinates: https://cses.fi/problemset/task/1674/
- Company Queries I: https://cses.fi/problemset/task/1687/
- Tree Diameter: https://cses.fi/problemset/task/1131/
