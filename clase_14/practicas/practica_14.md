# Práctica 14 — Heap y cola de prioridad

## Idea central

> [!IMPORTANT]
> Elegimos una estructura de datos según la operación que queremos optimizar. Un heap no es un BST: mantiene orden parcial y coloca el mínimo (o máximo) en la raíz.

## Entrega

Crea `entregas/clase_14/nombre/` con:

- `implementacion.py`
- `test_estudiante.py`
- `notebook.md`
- `discusion.md`
- `reporte_pytest.md`

No copies `src/heap.py`: úsalo como guía de firmas y docstrings. Implementa `HeapMin` con arreglo indexado desde cero y `ultima_piedra(piedras)` con cola de prioridad.

## Parte 1 — Trabajo manual

Con la secuencia `7, 3, 9, 1, 6, 5` completa en `notebook.md`:

| Inserción | Arreglo después de sift-up | Intercambios | Mínimo |
| ---: | --- | ---: | ---: |
| 7 | | | |
| 3 | | | |
| 9 | | | |
| 1 | | | |
| 6 | | | |
| 5 | | | |

Dibuja el árbol, identifica padre e hijos y luego simula una extracción: retirar raíz, mover último, elegir hijo menor e intercambiar hasta restaurar `padre <= hijos`.

> [!NOTE]
> Fórmulas: `padre(i) = (i - 1) // 2`, `izquierdo(i) = 2*i + 1`, `derecho(i) = 2*i + 2`.

## Parte 2 — Implementación

Implementa:

- construcción, vacío, tamaño y mínimo;
- inserción y `_subir`;
- extracción y `_bajar`;
- construcción de heap;
- índices y verificación de propiedad;
- `ultima_piedra`.

Convenciones: entradas enteras, `IndexError` al consultar o extraer de vacío y árbol completo representado por una lista. Mantén type hints y docstrings con parámetros, retorno, excepciones y ejemplo.

> [!TIP]
> En sift-down compara ambos hijos y elige el menor antes de intercambiar. Elegir solo el izquierdo es un error común.

## Parte 3 — Last Stone Weight

Lee el resumen y enlace del [problema 1046](https://leetcode.com/problems/last-stone-weight/). En cada turno se retiran las dos piedras más pesadas; si son distintas se reinserta su diferencia. Simula `[2, 7, 4, 1, 8, 1]`, identifica la operación dominante y usa negativos con `heapq` para representar un max-heap.

No se copia el enunciado original. Explica pseudocódigo, complejidad y por qué la lista de entrada no debe mutarse.

## Parte 4 — Pruebas

Escribe al menos tres pruebas con nombre descriptivo y comentario/docstring:

1. Inserción con varios intercambios.
2. Extracción con varios descensos.
3. Caso extremo o `ultima_piedra`.

Desde `curso-alumnos`:

```bash
python3 evaluar.py entregas/clase_14/nombre clase_14/tests entregas/clase_14/nombre/test_estudiante.py
```

PowerShell:

```powershell
py evaluar.py entregas/clase_14/nombre clase_14/tests entregas/clase_14/nombre/test_estudiante.py
```

En `reporte_pytest.md` incluye comando, salida completa, número de pruebas, aprobadas, errores, prueba propia y caso pendiente.

## Parte 5 — Discusión

Responde en `discusion.md`:

1. Operación dominante.
2. FIFO vs prioridad.
3. BST/AVL vs heap.
4. Propiedad min-heap.
5. Representación por arreglo.
6. Sift-up.
7. Sift-down.
8. Complejidad.
9. Last Stone Weight.
10. Pruebas propias.
11. Revisión técnica.
12. Relación con Dijkstra.
13. Pregunta abierta: ¿qué operación haría preferible otra estructura?

## Parte 6 — Revisión y GitHub

Rama: `clase-14-nombre`. Commits: `[TIPO] Descripción breve`. PR: `[Clase 14] Nombre - Heap y cola de prioridad`. Sigue las tres guías de `practicas/recursos/`.

> [!WARNING]
> El visualizador ipywidgets es una herramienta preparada y no se evalúa como implementación. Si no aparece, ejecuta la celda de diagnóstico; no cambies `HeapMin` para corregir el entorno.

## Checklist de entrega

- [ ] Mi rama cumple `clase-14-nombre`.
- [ ] Solo modifiqué `entregas/clase_14/nombre/`.
- [ ] Los cinco archivos obligatorios existen.
- [ ] Respondí el notebook en `notebook.md`.
- [ ] Implementé todas las firmas y docstrings.
- [ ] Agregué tres pruebas explicadas.
- [ ] Guardé la salida completa de pytest.
- [ ] Realicé o recibí la revisión técnica.
- [ ] `git diff --name-only origin/main` no muestra basura ni otros alumnos.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y comprensión conceptual | 20 |
| Implementación de HeapMin | 25 |
| Inserción, extracción y propiedad | 15 |
| Last Stone Weight | 10 |
| Pruebas propias y evaluar.py | 10 |
| Revisión técnica | 10 |
| discusion.md y redacción | 5 |
| GitHub y organización | 5 |
| **Total** | **100** |

## Práctica posterior

| Referencia | Operación dominante | Uso del heap | Dificultad | Tipo |
| --- | --- | --- | --- | --- |
| LeetCode 703 | mantener k mayores en flujo | min-heap de tamaño k | fácil | sugerida |
| LeetCode 215 | seleccionar k-ésimo mayor | heap parcial | media | sugerida |
| LeetCode 347 | extraer frecuencias altas | prioridad por frecuencia | media | opcional |
| LeetCode 973 | conservar k distancias menores | heap limitado | media | opcional |
| LeetCode 295 | consultar mediana dinámica | dos heaps | difícil | opcional |
| LeetCode 23 | elegir cabeza mínima | min-heap | difícil | opcional |
| CSES Concert Tickets | elegir mejor precio permitido | requiere búsqueda ordenada; contraste | media | opcional |
| CSES Room Allocation | liberar habitación más próxima | min-heap de finales | media | sugerida |
| CSES Tasks and Deadlines | ordenar por duración | contraste con heap | fácil | opcional |
| CSES Traffic Lights | vecinos ordenados | otra estructura ordenada | difícil | contraste |
| CSES Shortest Routes I | menor distancia pendiente | cola de prioridad | media | preparación para Dijkstra |

