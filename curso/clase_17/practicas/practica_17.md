# Práctica 17 — Listas ligadas, BFS y 0-1 BFS

## Idea central

> [!IMPORTANT]
> La estructura auxiliar cambia con la prioridad: cola para una prioridad, deque para incrementos 0/1 y heap para prioridades generales.

Esta práctica es asíncrona. No exige revisión cruzada. Trabaja únicamente dentro de `entregas/nombre/clase_17/`.

## Entrega exacta

```text
entregas/nombre/clase_17/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

Copia `curso/clase_17/src/estructuras_bfs_base.py` como `implementacion.py` y conserva todas las firmas públicas. No uses `collections.deque`, `list.pop(0)` ni heap para resolver las operaciones obligatorias.

## Parte 1 — Cola ligada simple

Implementa `NodoSimple` y `ColaLigada` con `encolar`, `desencolar`, `primero`, `esta_vacia` y `len`.

Contratos:

- encolar y desencolar son O(1);
- vacío implica frente/final `None` y tamaño 0;
- un elemento implica frente `is` final;
- `final.siguiente is None`;
- retirar el último limpia ambos extremos;
- el nodo retirado no conserva `siguiente`;
- la cola puede vaciarse y reutilizarse.

## Parte 2 — BFS y caminos

Implementa `bfs_predecesores`, `reconstruir_camino` y `bfs_camino`.

- BFS debe usar tu `ColaLigada`.
- Marca cada vértice al encolarlo.
- Conserva el primer predecesor.
- Incluye vecinos implícitos sin mutar la entrada.
- Origen o destino ausentes producen `KeyError`.
- Origen igual a destino produce `[origen]`.
- Destino inalcanzable produce `[]`.
- Una tabla cíclica o rota produce `ValueError`.

## Parte 3 — Deque ligada doble

Implementa `NodoDoble` y `DequeLigada`: agregar/quitar por inicio y final, consultar extremos, vacío y tamaño.

Protege enlaces bidireccionales, extremos, tamaño, caso de un elemento, separación total de nodos retirados y reutilización después de vaciar.

## Parte 4 — 0-1 BFS

Implementa `cero_uno_bfs` y `camino_cero_uno` usando tu `DequeLigada`.

- una mejora por peso 0 entra al inicio;
- una mejora por peso 1 entra al final;
- solo una mejora estricta actualiza distancia y predecesor;
- acepta únicamente enteros 0 y 1;
- `bool` y pesos no enteros producen `TypeError`;
- enteros distintos de 0/1 producen `ValueError`;
- origen ausente produce `KeyError`;
- inalcanzable produce `(inf, [])`;
- origen=destino produce `(0, [origen])`;
- no muta el grafo.

## Parte 5 — Pruebas propias

Escribe al menos ocho pruebas explicadas:

1. FIFO en `ColaLigada`.
2. Reutilización de cola después de vaciarla.
3. Operaciones combinadas en `DequeLigada`.
4. Reutilización de deque después de vaciarla.
5. BFS con ciclo.
6. BFS con destino inalcanzable.
7. 0-1 BFS con ruta de más aristas pero menor costo.
8. 0-1 BFS con peso inválido.

En cada prueba indica regla protegida, entrada, resultado esperado y razón de importancia. Se recomiendan además: origen=destino, vecino implícito, no mutación, solo ceros, solo unos, mejora posterior, referencias consistentes y repetidos.

## Comandos

Desde `curso-alumnos`:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests
python3 scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests entregas/nombre/clase_17/test_estudiante.py
```

Windows PowerShell:

```powershell
py scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests
py scripts/evaluar.py entregas/nombre/clase_17 curso/clase_17/tests entregas/nombre/clase_17/test_estudiante.py
```

## GitHub

Rama: `clase-17-nombre`.

PR: `[Clase 17] Nombre - Listas ligadas, BFS y 0-1 BFS`.

Commits sugeridos:

```text
[FEAT] Implementa ColaLigada y sus invariantes
[FEAT] Integra ColaLigada en BFS
[FEAT] Implementa DequeLigada por ambos extremos
[FEAT] Resuelve caminos mínimos con 0-1 BFS
[TEST] Protege reutilización, referencias y contratos
[DOC] Completa notebook, discusión y reporte
```

## Checklist

- [ ] Entregué exactamente cinco archivos.
- [ ] Respondí fuera del `.ipynb`.
- [ ] No usé `collections.deque`, `pop(0)` ni heap.
- [ ] Cola y deque restauran extremos al vaciarse.
- [ ] Los nodos retirados no conservan enlaces.
- [ ] BFS marca al encolar y usa mi cola.
- [ ] 0-1 BFS usa mi deque y actualiza mejoras.
- [ ] No muté grafos y acepté vecinos implícitos.
- [ ] Distinguí `TypeError`, `ValueError` y `KeyError`.
- [ ] Agregué ocho pruebas explicadas.
- [ ] Guardé la salida completa de `pytest -v`.
- [ ] No agregué cachés ni archivos ajenos.

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
