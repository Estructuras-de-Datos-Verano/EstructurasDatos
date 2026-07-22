# Clase 20 presencial y final — Laboratorio integrador

## Pregunta central

Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?

Modalidad: **presencial**. Duración: **4 horas**.

## Objetivos

Modelar objetivo, dirección y pesos; distinguir camino mínimo, MST y orden topológico; elegir entre BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn; relacionar cada algoritmo con cola, deque, heap, Union-Find o grados de entrada; verificar contratos; reutilizar implementaciones; diseñar pruebas distintivas; y comunicar decisiones técnicas.

## Ruta recomendada

1. Abre `notebooks/clase_20_laboratorio_integrador.ipynb`.
2. Responde exclusivamente en tu `notebook.md`.
3. Predice cada decisión antes de avanzar el visualizador.
4. Copia `src/seleccion_estrategias_base.py` como `implementacion.py`.
5. Implementa primero validación y matriz de decisión.
6. Agrega descartes, evaluación de propuestas y pruebas propias.
7. Completa discusión, reporte y reflexión final.

> [!IMPORTANT]
> No reescribas BFS, 0-1 BFS, Dijkstra, Kruskal ni Kahn. La práctica evalúa modelado, selección, contratos, pruebas y comunicación.

## Método de decisión

```text
problema → objetivo → tipo de grafo → restricciones → operación dominante
         → estructura → algoritmo → contrato → prueba → complejidad → interpretación
```

## Matriz esencial

| Problema | Estructura | Algoritmo |
| --- | --- | --- |
| Camino sin pesos | cola | BFS |
| Camino con pesos 0/1 | deque | 0-1 BFS |
| Camino con pesos no negativos | heap | Dijkstra |
| Conexión global mínima no dirigida | Union-Find | Kruskal |
| Dependencias dirigidas | cola + grados de entrada | Kahn |

Los pesos negativos en caminos quedan fuera de los algoritmos estudiados. Kruskal sí puede aceptar aristas negativas en un grafo no dirigido.

## Preparación

```bash
python3 -m pip install -r curso/clase_20/requirements.txt
```

## Evaluación

Desde `curso-alumnos`:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_20 curso/clase_20/tests
python3 scripts/evaluar.py entregas/nombre/clase_20 curso/clase_20/tests entregas/nombre/clase_20/test_estudiante.py
```

## Entrega

```text
entregas/nombre/clase_20/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y diagnóstico de problemas | 20 |
| Motor de decisión y contratos | 20 |
| Justificación de alternativas descartadas | 15 |
| Reutilización y adaptación | 15 |
| Pruebas distintivas propias | 15 |
| Comunicación y trabajo en equipo | 10 |
| Reflexión final y GitHub | 5 |
| **Total** | **100** |

## Cierre

**Los algoritmos se vuelven eficientes cuando la estructura de datos coincide con la operación dominante del problema.**

