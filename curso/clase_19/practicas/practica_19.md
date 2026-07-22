# Práctica 19 — Ordenamiento topológico y algoritmo de Kahn

## Idea central

> [!IMPORTANT]
> Un nodo puede procesarse cuando su grado de entrada actual llega a cero: ya no tiene requisitos pendientes.

Esta práctica es asíncrona y no exige revisión cruzada. Trabaja únicamente dentro de `entregas/nombre/clase_19/`.

## Entrega exacta

```text
entregas/nombre/clase_19/
├── implementacion.py
├── test_estudiante.py
├── notebook.md
├── discusion.md
└── reporte_pytest.md
```

Copia `curso/clase_19/src/ordenamiento_topologico_base.py` como `implementacion.py` y conserva firmas, retornos y excepciones.

## Parte 1 — Normalización y grados

Implementa `normalizar_grafo_dirigido` y `grados_entrada`.

- acepta un `Mapping` con listas o tuplas;
- copia defensivamente y no comparte listas;
- nodos y vecinos son `str`;
- agrega destinos implícitos y conserva aislados;
- elimina duplicados en orden estable;
- no modifica la entrada;
- grado de entrada cuenta aristas que llegan, no vecinos salientes.

## Parte 2 — Kahn y ciclos

Implementa `orden_topologico` con `collections.deque`.

- encola inicialmente todos los grados cero;
- procesa cada nodo una vez;
- reduce el grado de cada sucesor;
- encola justo cuando el grado llega a cero;
- devuelve todos los nodos de un DAG;
- devuelve `None` si queda algún nodo sin procesar;
- no devuelve prefijos ante ciclos.

## Parte 3 — Validar órdenes

Implementa `es_orden_topologico`: exige cobertura, nodos conocidos, ausencia de repetidos y `posicion[u] < posicion[v]` para cada arista. No presupongas que existe un único orden.

## Parte 4 — Cursos

Implementa `ordenar_cursos` y `puede_completar_cursos`.

- cada par es `(prerrequisito, curso)`;
- cantidad entera no negativa; `bool` es inválido;
- índices válidos entre 0 y n−1;
- duplicados se ignoran;
- auto dependencia y ciclos devuelven `None`;
- sin prerrequisitos aparecen todos los cursos;
- la función booleana reutiliza la función de orden.

## Parte 5 — Pruebas propias

Escribe y explica al menos seis pruebas:

1. varios órdenes válidos;
2. ciclo simple;
3. ciclo dentro de una parte del grafo;
4. vecino implícito;
5. dependencias duplicadas;
6. orden incorrecto.

Documenta regla, entrada, resultado esperado y relevancia. Recomendados: vacío, aislado, cadena, varias fuentes, autoarista, no mutación, índice inválido, cursos sin prerrequisitos, repetidos y faltantes.

## Comandos

```bash
python3 scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests
python3 scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests entregas/nombre/clase_19/test_estudiante.py
```

Windows:

```powershell
py scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests
py scripts/evaluar.py entregas/nombre/clase_19 curso/clase_19/tests entregas/nombre/clase_19/test_estudiante.py
```

## Problemas externos

- Principal: [CSES Course Schedule](https://cses.fi/problemset/task/1679/).
- Relacionados: [LeetCode 207](https://leetcode.com/problems/course-schedule/) y [LeetCode 210](https://leetcode.com/problems/course-schedule-ii/).

No copies soluciones externas ni incluyas implementaciones completas de esos jueces en tu entrega.

## GitHub

Rama: `clase-19-nombre`.

PR: `[Clase 19] Nombre - Ordenamiento topológico`.

Commits sugeridos:

```text
[FEAT] Normaliza grafos dirigidos y dependencias
[TEST] Protege vecinos implícitos y duplicados
[FEAT] Calcula grados de entrada
[FEAT] Implementa algoritmo de Kahn
[TEST] Detecta ciclos y órdenes inválidos
[FEAT] Agrega planificación de cursos
[DOC] Compara Kahn con BFS y otros algoritmos
```

Antes del PR ejecuta `git branch --show-current`, `git status` y `git diff --name-only origin/main`. Solo deben aparecer archivos de tu entrega.

## Checklist

- [ ] Entregué exactamente cinco archivos.
- [ ] Respondí fuera del notebook.
- [ ] Conservé la dirección prerrequisito → curso.
- [ ] No muté entradas ni compartí listas.
- [ ] Incluí vecinos implícitos, aislados y duplicados normalizados.
- [ ] Solo encolé grados cero.
- [ ] Detecté ciclos completos y parciales.
- [ ] Validé por propiedades, no por una lista exacta.
- [ ] Rechacé booleanos e índices inválidos.
- [ ] Agregué seis pruebas explicadas.
- [ ] Guardé `pytest -v` completo.
- [ ] No agregué cachés.

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

