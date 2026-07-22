# Práctica 18 — Union-Find, Kruskal y Road Reparation

## Idea central

> [!IMPORTANT]
> Kruskal necesita comprobar repetidamente si dos extremos pertenecen a la misma componente. Union-Find hace eficiente esa consulta.

## Entrega exacta

```text
entregas/nombre/clase_18/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

No se exige revisión cruzada. Solo modifica tu carpeta de entrega.

## Parte 1 — Union-Find

Copia la base como `implementacion.py`. Implementa inicialización, `_validar_indice`, `find`, `union`, `conectados`, `tamano_componente` y `numero_componentes`.

- `bool` no cuenta como entero válido;
- cantidad negativa: `ValueError`;
- índice con tipo incorrecto: `TypeError`;
- índice negativo o fuera de rango: `IndexError`;
- `union` devuelve `True` solo al fusionar;
- unión repetida o reflexiva devuelve `False` sin cambiar contador;
- `find` comprime caminos;
- `union` coloca el árbol pequeño debajo del grande;
- el tamaño se consulta en la raíz.

## Parte 2 — Kruskal

Implementa `kruskal(numero_vertices, aristas)`.

- valida y copia la lista;
- normaliza pesos válidos a `float`;
- acepta pesos negativos, cero, paralelas y autoaristas;
- rechaza `bool`, pesos no numéricos y no finitos;
- usa Union-Find para aceptar o rechazar;
- se detiene en V−1 aristas;
- devuelve `None` si está desconectado;
- no presupone MST único con empates.

## Parte 3 — Road Reparation

Implementa `costo_reparacion`: recibe ciudades 0-based y costos enteros; devuelve el costo entero mínimo o `None`. Para el formato oficial de [CSES Road Reparation](https://cses.fi/problemset/task/1675/), convierte etiquetas 1-based y muestra `IMPOSSIBLE` cuando corresponda.

## Parte 4 — Pruebas propias

Escribe y explica al menos seis:

1. unión efectiva;
2. unión repetida;
3. transitividad;
4. tamaño de componente;
5. arista rechazada por ciclo;
6. grafo desconectado.

Cada prueba documenta regla, entrada, resultado esperado y razón. Recomendados: índice negativo, compresión, peso negativo, paralelas, autoarista, empate, no mutación y un vértice.

## Comandos

```bash
python3 scripts/evaluar.py entregas/nombre/clase_18 curso/clase_18/tests
python3 scripts/evaluar.py entregas/nombre/clase_18 curso/clase_18/tests entregas/nombre/clase_18/test_estudiante.py
```

Windows:

```powershell
py scripts/evaluar.py entregas/nombre/clase_18 curso/clase_18/tests
py scripts/evaluar.py entregas/nombre/clase_18 curso/clase_18/tests entregas/nombre/clase_18/test_estudiante.py
```

## Actividades opcionales

- [LeetCode 684 — Redundant Connection](https://leetcode.com/problems/redundant-connection/).
- Comparar ciclos con DFS y Union-Find.
- Investigar Prim.
- Dibujar compresión de caminos.
- Construir dos MST distintos con el mismo costo.

No forman parte de la evaluación.

## GitHub

Rama: `clase-18-nombre`.

PR: `[Clase 18] Nombre - Union-Find y Kruskal`.

Commits sugeridos:

```text
[FEAT] Implementa Union-Find básico
[FEAT] Agrega compresión de caminos
[FEAT] Incorpora unión por tamaño
[TEST] Protege uniones redundantes e índices inválidos
[FEAT] Implementa Kruskal
[TEST] Verifica ciclos y grafos desconectados
[DOC] Compara Dijkstra y Kruskal
```

Antes del PR ejecuta `git branch --show-current`, `git status` y `git diff --name-only origin/main`. Solo deben aparecer archivos de tu entrega.

## Checklist

- [ ] Entregué exactamente cinco archivos.
- [ ] Respondí fuera del notebook.
- [ ] Probé índices negativos y `bool`.
- [ ] La unión redundante no altera contador.
- [ ] Implementé compresión y unión por tamaño.
- [ ] No muté las aristas.
- [ ] Admití pesos negativos y rechacé no finitos.
- [ ] Detecté grafo desconectado.
- [ ] No exigí un MST específico con empates.
- [ ] Agregué seis pruebas explicadas.
- [ ] Guardé la salida completa de `pytest -v`.
- [ ] No agregué cachés.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y comprensión conceptual | 15 |
| Union-Find básico e invariantes | 20 |
| compresión y unión por tamaño | 15 |
| Kruskal | 20 |
| Road Reparation | 10 |
| pruebas propias | 10 |
| discusión y reporte | 5 |
| organización y GitHub | 5 |
| **Total** | **100** |
