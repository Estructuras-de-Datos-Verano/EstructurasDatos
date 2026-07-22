# Clase 17 asíncrona — Listas ligadas, BFS y 0-1 BFS

## Pregunta central

¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?

Modalidad: **asíncrona**. Duración estimada: **4 horas**.

## Objetivos

Al finalizar podrás construir una cola con lista simple, una deque con lista doble, usar esas estructuras en BFS y 0-1 BFS, reconstruir caminos, validar grafos sin mutarlos y proteger invariantes mediante pruebas.

## Ruta recomendada

1. Abre `notebooks/clase_17_listas_bfs.ipynb` y responde en tu `notebook.md`.
2. Predice y explora las ocho operaciones visualizadas.
3. Copia `src/estructuras_bfs_base.py` como `implementacion.py` dentro de tu entrega.
4. Completa primero `ColaLigada` y BFS; después `DequeLigada` y 0-1 BFS.
5. Ejecuta las pruebas públicas después de cada bloque.
6. Agrega al menos ocho pruebas propias explicadas.
7. Completa `discusion.md` y `reporte_pytest.md` con las plantillas.
8. Revisa la presentación como síntesis final.

> [!IMPORTANT]
> No respondas dentro del notebook. Todas las respuestas van en `entregas/nombre/clase_17/notebook.md`.

## Archivos de la clase

- `notebooks/clase_17_listas_bfs.ipynb`: cuaderno autónomo y visualizaciones.
- `presentacion/index.html`: resumen visual offline.
- `practicas/practica_17.md`: especificación y rúbrica.
- `practicas/plantillas/`: documentos de entrega.
- `src/estructuras_bfs_base.py`: firmas y contratos sin resolver.
- `src/visualizaciones_listas.py` y `src/visualizaciones_bfs.py`: visualizadores preparados.
- `tests/test_publico_estructuras_bfs.py`: pruebas públicas.

## Contratos esenciales

- Cola vacía: frente y final en `None`, tamaño 0.
- Deque vacía: inicio y final en `None`, tamaño 0.
- Todo nodo retirado queda sin referencias residuales.
- BFS usa `ColaLigada` y marca al encolar.
- 0-1 BFS usa `DequeLigada`: peso 0 al inicio; peso 1 al final.
- Los pesos aceptados son enteros exactamente 0 o 1; `bool` no es válido.
- Los grafos se normalizan en una copia e incluyen vecinos implícitos.
- No se modifica la entrada.

## Preparación

Desde `curso-alumnos`:

```bash
python3 -m pip install -r curso/clase_17/requirements.txt
```

En Windows PowerShell:

```powershell
py -m pip install -r curso/clase_17/requirements.txt
```

## Evaluación local

Pruebas públicas:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests
```

Públicas y propias:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests entregas/nombre/clase_17/test_estudiante.py
```

En Windows sustituye `python3` por `py`.

## Entrega

```text
entregas/nombre/clase_17/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

## Si una prueba falla

1. Lee el nombre de la prueba y expresa la regla que protege.
2. Reproduce la entrada mínima sin cambiar el test.
3. Dibuja extremos, enlaces y tamaño antes y después.
4. Corrige una responsabilidad a la vez.
5. Vuelve a ejecutar públicas y propias.
6. Conserva el fallo como prueba de regresión.

Errores frecuentes: olvidar limpiar el segundo extremo al vaciar; dejar enlaces en nodos retirados; marcar BFS al desencolar; usar `pop(0)`; no actualizar predecesor en una mejora 0-1; aceptar `True`; mutar el grafo; confundir inalcanzable con clave ausente.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md | 10 |
| ColaLigada | 15 |
| BFS | 15 |
| DequeLigada | 20 |
| 0-1 BFS | 20 |
| pruebas propias | 10 |
| discusión y reporte | 5 |
| organización y GitHub | 5 |
| **Total** | **100** |
