# Clase 15 — Caminos mínimos y Dijkstra

> [!IMPORTANT]
> Cuando las aristas tienen costos diferentes, procesamos primero la menor distancia acumulada conocida.

La clase continúa el hilo grafos → BFS/DFS → heaps → Dijkstra. Partimos de un caso donde BFS elige una ruta directa costosa, construimos distancias tentativas y relajaciones, y recuperamos el min-heap de la Clase 14 para decidir qué candidatura procesar.

## Ruta de trabajo

1. Abre `notebooks/clase_15_dijkstra.ipynb` y responde en `entregas/nombre/clase_15/notebook.md`.
2. Ejecuta el recorrido manual antes de comprobarlo con el visualizador.
3. Sigue `practicas/practica_15.md` e implementa las tres funciones solicitadas.
4. Agrega al menos tres pruebas propias explicadas.
5. Desde `curso-alumnos`, ejecuta:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_15 curso/clase_15/tests entregas/nombre/clase_15/test_estudiante.py
```

PowerShell:

```powershell
py scripts/evaluar.py entregas/nombre/clase_15 curso/clase_15/tests entregas/nombre/clase_15/test_estudiante.py
```

## Recursos

- Presentación local: `presentacion/index.html`.
- Visualizador preparado: `src/visualizador_dijkstra.py`.
- Estados precomputados: `src/estados_dijkstra.json`.
- Guías de Markdown, GitHub y revisión: `practicas/recursos/`.

> [!NOTE]
> El visualizador explica estados ya registrados. No contiene la solución evaluada y no debes programarlo.

## Contrato esencial

- Grafo como lista de adyacencia `dict[str, list[tuple[str, float]]]`.
- Pesos numéricos, finitos y no negativos.
- Inalcanzables con `float("inf")` y camino `[]`.
- La entrada no se modifica.
- Las entradas viejas del heap se ignoran al extraerlas.

