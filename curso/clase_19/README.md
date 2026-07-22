# Clase 19 asíncrona — Ordenamiento topológico y Kahn

## Pregunta central

¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?

Modalidad: **asíncrona**. Duración estimada: **4 horas**.

## Objetivos

Interpretar dependencias dirigidas; reconocer DAG y ciclos; calcular grados de entrada; ejecutar e implementar Kahn; normalizar grafos sin mutarlos; validar órdenes no únicos; ordenar cursos; diseñar pruebas por propiedades; y comparar cola, deque, heap y Union-Find por su operación dominante.

## Ruta recomendada

1. Abre `notebooks/clase_19_ordenamiento_topologico.ipynb`.
2. Responde exclusivamente en tu `notebook.md`.
3. Completa cada traza antes de avanzar el visualizador.
4. Copia `src/ordenamiento_topologico_base.py` como `implementacion.py`.
5. Implementa normalización y grados antes de Kahn.
6. Ejecuta pruebas públicas y al menos seis pruebas propias explicadas.
7. Completa discusión y reporte.

> [!IMPORTANT]
> No respondas dentro del `.ipynb` y no programes el visualizador. La entrega contiene exactamente cinco archivos dentro de tu carpeta.

## Archivos

- notebook autónomo y presentación offline;
- práctica y plantillas de los cinco entregables;
- código base sin soluciones;
- visualizador de Kahn con ocho ejemplos;
- pruebas públicas.

## Contratos esenciales

- las aristas significan `prerrequisito → tarea`;
- se aceptan grafos `Mapping` con vecinos en listas o tuplas;
- nodos y vecinos deben ser `str` en el grafo general;
- se agregan vecinos implícitos y se conservan aislados;
- duplicados se eliminan respetando primera aparición;
- ninguna función modifica el grafo o la lista de prerrequisitos;
- el grafo vacío devuelve `[]`; un ciclo devuelve `None`;
- cualquier orden válido es aceptable;
- en cursos, `bool` no es entero válido e índices incorrectos lanzan `IndexError`.

## Preparación

```bash
python3 -m pip install -r curso/clase_19/requirements.txt
```

Windows:

```powershell
py -m pip install -r curso/clase_19/requirements.txt
```

## Evaluación

Desde `curso-alumnos`:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests
python3 scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests entregas/nombre/clase_19/test_estudiante.py
```

Windows PowerShell:

```powershell
py scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests
py scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests entregas/nombre/clase_19/test_estudiante.py
```

## Entrega

```text
entregas/nombre/clase_19/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

## Si un test falla

1. Nombra el contrato protegido.
2. Reduce el grafo al menor contraejemplo.
3. Escribe grados, cola y orden parcial.
4. Decide si falla normalización, grados, Kahn, validación o adaptación de cursos.
5. Corrige una responsabilidad y vuelve a ejecutar todo.
6. Conserva el caso como prueba de regresión.

Errores frecuentes: invertir la flecha; contar salida en vez de entrada; omitir vecinos implícitos; contar duplicados; encolar con grado positivo; devolver un prefijo ante ciclo; exigir un orden único; aceptar índices negativos o booleanos.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y comprensión conceptual | 15 |
| Normalización y grados de entrada | 15 |
| Algoritmo de Kahn | 25 |
| Detección de ciclos | 10 |
| Validación de órdenes | 10 |
| Problema de cursos | 10 |
| Pruebas propias | 10 |
| Discusión, reporte y GitHub | 5 |
| **Total** | **100** |

## Referencias y cierre

- [CSES Course Schedule](https://cses.fi/problemset/task/1679/): problema principal.
- [LeetCode 207 — Course Schedule](https://leetcode.com/problems/course-schedule/): posibilidad de completar.
- [LeetCode 210 — Course Schedule II](https://leetcode.com/problems/course-schedule-ii/): construir un orden.

La Clase 20 será un laboratorio integrador: no agregará otro algoritmo, sino que pedirá identificar la operación dominante y elegir la estructura adecuada.

