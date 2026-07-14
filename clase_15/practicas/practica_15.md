# Práctica 15 — Caminos mínimos con Dijkstra

## Idea central

> [!IMPORTANT]
> Relajar una arista significa intentar mejorar la mejor distancia conocida. Entre las candidaturas pendientes, Dijkstra procesa la de menor costo acumulado.

## Entrega

Crea `entregas/clase_15/nombre/` con:

- `implementacion.py`
- `test_estudiante.py`
- `notebook.md`
- `discusion.md`
- `reporte_pytest.md`

No copies `src/visualizador_dijkstra.py` ni sus estados. Implementa en `implementacion.py`:

```python
def dijkstra(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
) -> tuple[dict[str, float], dict[str, str | None]]:
    ...

def reconstruir_camino(
    predecesores: dict[str, str | None],
    origen: str,
    destino: str,
) -> list[str]:
    ...

def camino_minimo(
    grafo: dict[str, list[tuple[str, float]]],
    origen: str,
    destino: str,
) -> tuple[float, list[str]]:
    ...
```

Incluye type hints y docstrings con parámetros, retorno, excepciones y un ejemplo breve.

## Parte 1 — Recorrido manual

Usa:

```python
grafo = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1), ("E", 7)],
    "C": [("B", 2), ("D", 5)],
    "D": [("E", 3)],
    "E": [],
}
```

Completa en `notebook.md`:

| Extracción | Arista | Candidata | Comparación | Decisión | Heap después |
| --- | --- | ---: | --- | --- | --- |
| `(0,A)` | `A→B` | | | | |
| `(0,A)` | `A→C` | | | | |
| `(1,C)` | `C→B` | | | | |
| `(1,C)` | `C→D` | | | | |
| … | | | | | |

Marca qué entradas son obsoletas y reconstruye el camino A→E.

## Parte 2 — Implementación

`dijkstra` debe:

1. validar el origen y todos los pesos;
2. inicializar distancias y predecesores;
3. usar `heapq` con pares `(distancia, nodo)`;
4. ignorar candidaturas obsoletas antes de relajar;
5. no mutar el grafo;
6. incluir nodos que aparezcan únicamente como vecinos.

`reconstruir_camino` sigue predecesores desde destino, invierte el resultado y devuelve `[]` si no alcanza el origen. `camino_minimo` coordina ambas funciones.

> [!WARNING]
> Rechaza pesos negativos con `ValueError`. Dijkstra no conserva su garantía con esos datos.

## Parte 3 — Pruebas

Agrega al menos tres pruebas propias y explica qué protegen:

1. una distancia mejora más de una vez y deja una entrada obsoleta;
2. un destino es inalcanzable;
3. una ruta indirecta supera a una arista directa costosa.

Casos opcionales: empates, peso cero, origen igual a destino, nodo que solo aparece como vecino y entrada no mutada.

```bash
python3 evaluar.py entregas/clase_15/nombre clase_15/tests entregas/clase_15/nombre/test_estudiante.py
```

```powershell
py evaluar.py entregas/clase_15/nombre clase_15/tests entregas/clase_15/nombre/test_estudiante.py
```

En `reporte_pytest.md` registra comando, salida completa, cantidad de pruebas, aprobadas, errores, caso propio y pendiente conocido.

## Parte 4 — Discusión

Responde en `discusion.md`:

1. Diferencia entre distancia por aristas y por pesos.
2. Significado de distancia tentativa.
3. Relajación con un ejemplo numérico.
4. Razón para usar min-heap.
5. Entrada obsoleta y eliminación perezosa.
6. Reconstrucción mediante predecesores.
7. Complejidad temporal y espacial.
8. Restricción de pesos no negativos.
9. Caso donde BFS falla.
10. Evidencia de tus pruebas.
11. Hallazgo de la revisión técnica.

## Parte 5 — Revisión y GitHub

Rama: `clase-15-nombre`. Commits: `[TIPO] Descripción breve`. PR: `[Clase 15] Nombre - Dijkstra`.

Ejemplo de commits:

```text
[FEAT] Implementa relajación con cola de prioridad
[TEST] Agrega caso de entrada obsoleta
[DOC] Explica reconstrucción del camino
```

Sigue las guías de `practicas/recursos/`. Una observación accionable incluye entrada, comportamiento observado y cambio verificable.

> [!CAUTION]
> Antes de ejecutar código de otra rama, revisa que el diff solo contenga la entrega del compañero.

## Checklist

- [ ] La rama cumple `clase-15-nombre`.
- [ ] Solo modifiqué `entregas/clase_15/nombre/`.
- [ ] Entregué los cinco archivos obligatorios.
- [ ] Respondí todas las preguntas del notebook en `notebook.md`.
- [ ] Usé las firmas, type hints y docstrings solicitados.
- [ ] No muté el grafo.
- [ ] Rechacé pesos negativos.
- [ ] Probé entradas obsoletas e inalcanzables.
- [ ] Guardé la salida completa de pytest.
- [ ] Realicé o recibí revisión técnica.
- [ ] No agregué `.DS_Store`, `__pycache__` ni `.pyc`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y recorrido manual | 20 |
| Dijkstra y relajación | 25 |
| Reconstrucción y función coordinadora | 15 |
| Contratos y casos límite | 10 |
| Pruebas propias y evidencia | 10 |
| Revisión técnica | 10 |
| Discusión y redacción | 5 |
| GitHub y organización | 5 |
| **Total** | **100** |

## Práctica adicional

| Contexto | Adaptación | Dificultad |
| --- | --- | --- |
| tiempos desde una ciudad | Dijkstra desde un origen | sugerida |
| retraso de una señal | máximo de distancias alcanzables | sugerida |
| cuadrícula con costos | cada celda es un nodo | media |
| camino con descuento | ampliar el estado | reto opcional |

