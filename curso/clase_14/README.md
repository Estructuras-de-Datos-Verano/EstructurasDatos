# Clase 14 — Colas de prioridad y heaps

> [!IMPORTANT]
> Elegimos una estructura de datos según la operación que queremos optimizar.

Si casi nunca buscamos cualquier elemento y repetidamente necesitamos el menor o el mayor, una cola de prioridad evita trabajo innecesario. En esta clase conectamos BST y AVL con min-heaps, `heapq`, el reto guiado *Last Stone Weight* y la selección que usará Dijkstra.

## Ruta de trabajo

1. Abre `notebooks/clase_14_heaps_colas_prioridad.ipynb`.
2. Responde todo en `entregas/nombre/clase_14/notebook.md`.
3. Sigue `practicas/practica_14.md` y completa `implementacion.py` y tres pruebas propias.
4. Ejecuta desde `curso-alumnos`:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_14 curso/clase_14/tests entregas/nombre/clase_14/test_estudiante.py
```

En PowerShell usa `py` o `python` en lugar de `python3`.

## Recursos

- Presentación sin conexión: `presentacion/index.html`.
- Visualización preparada: `src/visualizador_heap.py`.
- Guías de Markdown, GitHub y revisión: `practicas/recursos/`.

> [!NOTE]
> El visualizador no forma parte de la implementación evaluada. Sus estados ya fueron preparados para concentrarte en observar y razonar.

