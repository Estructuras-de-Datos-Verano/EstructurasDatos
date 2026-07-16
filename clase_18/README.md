# Clase 18 presencial — Union-Find y Kruskal

## Pregunta central

¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?

Modalidad: **presencial**. Duración estimada: **4 horas**.

## Objetivos

Construir Union-Find con compresión y unión por tamaño; distinguir caminos mínimos y árboles de expansión; implementar Kruskal; detectar desconexión; resolver Road Reparation; y probar invariantes, validación y propiedades del MST.

## Conexión con Clases 16 y 17

| Necesidad | Estructura |
| --- | --- |
| menor distancia tentativa | heap — Dijkstra |
| prioridad 0/1 | deque — 0-1 BFS |
| orden por capas | cola — BFS |
| pertenencia a la misma componente | Union-Find — Kruskal |

## Ruta de estudio

1. Abre `notebooks/clase_18_union_find_kruskal.ipynb`.
2. Responde exclusivamente en tu `notebook.md`.
3. Completa las trazas antes de avanzar los visualizadores.
4. Copia `src/union_find_kruskal_base.py` como `implementacion.py`.
5. Implementa y prueba Union-Find antes de Kruskal.
6. Ejecuta pruebas públicas y seis pruebas propias.
7. Completa discusión y reporte.

> [!IMPORTANT]
> No respondas dentro del `.ipynb` y no programes los visualizadores: ya están preparados y no forman parte de la evaluación.

## Contratos esenciales

- cantidad entera no negativa; `bool` no es válida;
- índices enteros dentro de `0…n−1`; negativos producen `IndexError`;
- `union` devuelve `True` solo cuando fusiona componentes;
- compresión no cambia la partición;
- unión por tamaño actualiza el tamaño de la nueva raíz;
- Kruskal copia y normaliza las aristas, sin mutar la entrada;
- acepta pesos negativos y cero, pero no booleanos ni no finitos;
- devuelve `(0.0, [])` con cero o un vértice y `None` si está desconectado;
- con empates pueden existir varios MST correctos.

## Archivos

- notebook guiado y presentación offline;
- práctica y plantillas de cinco entregables;
- base sin soluciones;
- visualizadores de Union-Find y Kruskal;
- pruebas públicas.

## Preparación

```bash
python3 -m pip install -r clase_18/requirements.txt
```

Windows:

```powershell
py -m pip install -r clase_18/requirements.txt
```

## Evaluación

```bash
python3 evaluar.py entregas/clase_18/nombre clase_18/tests
python3 evaluar.py entregas/clase_18/nombre clase_18/tests entregas/clase_18/nombre/test_estudiante.py
```

En Windows sustituye `python3` por `py`.

## Entrega

```text
entregas/clase_18/nombre/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

## Si un test falla

1. Nombra el contrato protegido.
2. Reduce la entrada.
3. Dibuja padres, tamaños y componentes.
4. Distingue fallo de Union-Find, normalización o Kruskal.
5. Corrige una responsabilidad y vuelve a ejecutar todo.
6. Conserva el caso como regresión.

Errores frecuentes: aceptar índices negativos; unir nodos en vez de raíces; reducir componentes en una unión redundante; consultar tamaño fuera de la raíz; ordenar la entrada in-place; sumar aristas rechazadas; exigir un MST exacto con empates; rechazar pesos negativos.

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

## Cierre hacia Clase 19

Pasaremos de componentes en grafos no dirigidos a dependencias dirigidas: grados de entrada, cola y ordenamiento topológico.
