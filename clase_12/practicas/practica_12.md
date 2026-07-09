# Práctica 12: Altura, balance y eficiencia en BST

## Contexto

En la Clase 11 implementaste un árbol binario de búsqueda.

Ahora vamos a cuestionar una idea peligrosa:

> ¿Un BST siempre es mejor que una lista?

La respuesta corta es no.

Un BST puede buscar rápido si su altura se mantiene baja. Pero si se degenera, puede comportarse como una lista.

## Objetivos

Al terminar esta práctica podrás:

- explicar altura y profundidad;
- distinguir un árbol balanceado de un árbol degenerado;
- explicar por qué la altura controla el costo de búsqueda;
- contar comparaciones a mano;
- extender tu BST con métodos nuevos;
- medir comparaciones de búsqueda;
- escribir pruebas propias;
- usar `evaluar.py` con tests públicos y tests extra;
- ejecutar pruebas propias contra la implementación de un compañero durante la revisión de PR;
- escribir una discusión técnica con evidencia.

## Instrucciones

1. Revisa el notebook.
2. Responde sus preguntas en `notebook.md`.
3. Implementa los métodos nuevos en `implementacion.py`.
4. Escribe al menos 3 pruebas propias en `test_estudiante.py`.
5. Ejecuta `evaluar.py` con tests públicos.
6. Crea `reporte_pytest.md`.
7. Escribe `discusion.md`.
8. Abre Pull Request.
9. Revisa el PR asignado.
10. Ejecuta tus propias pruebas contra la implementación del compañero.
11. Pega la salida completa de `pytest -v` en el comentario del PR.

No respondas preguntas dentro del notebook.

No entregues el notebook `.ipynb`.

No programes animaciones. Los GIFs ya están integrados como material de apoyo.

No implementes eliminación.

No implementes AVL.

No implementes Red-Black Tree.

No modifiques `main`.

Trabaja en:

```text
entregas/clase_12/nombre/
```

Puedes usar `src/bst_balance.py` como molde para crear tu `implementacion.py`, pero las pruebas evaluarán tu archivo de entrega.

## Entrega obligatoria

```text
entregas/
└── clase_12/
    └── nombre/
        ├── implementacion.py
        ├── test_estudiante.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

## `implementacion.py`

Debe definir:

```python
class Nodo:
    ...

class ArbolBinarioBusqueda:
    ...
```

Métodos esperados:

```python
def insertar(self, valor: int) -> None: ...
def contiene(self, valor: int) -> bool: ...
def altura(self) -> int: ...
def inorden(self) -> list[int]: ...
def preorden(self) -> list[int]: ...
def postorden(self) -> list[int]: ...
def cantidad_nodos(self) -> int: ...
def es_degenerado(self) -> bool: ...
def comparaciones_busqueda(self, valor: int) -> int: ...
```

Convención:

- árbol vacío: altura 0;
- árbol con solo raíz: altura 1.

`es_degenerado()` debe regresar `False` para árbol vacío y `True` para un árbol no vacío donde ningún nodo tiene dos hijos.

`comparaciones_busqueda(valor)` debe contar cuántos nodos visita una búsqueda.

## `test_estudiante.py`

Debes escribir al menos 3 pruebas propias.

Deben cubrir al menos:

- un caso de altura;
- un caso de búsqueda;
- un caso de degeneración o balance.

Cada prueba debe tener nombre claro y docstring o comentario breve.

## `notebook.md`

Contiene tus respuestas a las preguntas del notebook, en el mismo orden.

No debe contener código completo.

Estructura:

```text
# Notebook - Clase 12

## 1. Motivación
## 2. Lista vs BST
## 3. Conteo manual de comparaciones
## 4. Altura
## 5. Árbol balanceado y árbol degenerado
## 6. Búsqueda y altura
## 7. Experimentos
## 8. Animaciones
## 9. Complejidad
## 10. Problemas relacionados
## 11. evaluar.py y pruebas
## 12. Revisión técnica de PR
## 13. Patrón descubierto
## 14. Cierre
```

## `discusion.md`

Es un documento técnico. No debe repetir literalmente `notebook.md`.

Debe incluir:

```text
# Discusión técnica

## 1. ¿Un BST siempre es eficiente?
## 2. Lista vs BST
## 3. Altura y comparaciones
## 4. Árbol balanceado vs árbol degenerado
## 5. Orden de inserción
## 6. Complejidad
## 7. Experimentos y evidencia
## 8. Animaciones
## 9. Pruebas propias
## 10. Revisión técnica del PR
## 11. Problemas relacionados
## 12. Pregunta abierta
```

## `reporte_pytest.md`

Debe contener:

- comando ejecutado;
- salida completa;
- interpretación;
- cuántas pruebas se ejecutaron;
- cuántas pasaron;
- si hubo errores;
- qué comportamiento verifican;
- qué prueba diseñaste tú;
- qué caso todavía falta probar.

## Ejecutar pruebas públicas

Desde la raíz de `curso-alumnos`:

macOS / Linux:

```bash
python3 evaluar.py entregas/clase_12/nombre clase_12/tests
```

Windows PowerShell:

```powershell
py evaluar.py entregas/clase_12/nombre clase_12/tests
```

o:

```powershell
python evaluar.py entregas/clase_12/nombre clase_12/tests
```

`evaluar.py` ejecuta internamente `pytest -v` y permite que los tests importen:

```python
from implementacion import ArbolBinarioBusqueda, Nodo
```

## Ejecutar tests extra

Forma general:

```text
evaluar.py <carpeta_entrega> <tests_publicos> [tests_extra]
```

Ejemplo macOS / Linux:

```bash
python3 evaluar.py entregas/clase_12/max clase_12/tests entregas/clase_12/leo/test_estudiante.py
```

Ejemplo Windows PowerShell:

```powershell
py evaluar.py entregas/clase_12/max clase_12/tests entregas/clase_12/leo/test_estudiante.py
```

o:

```powershell
python evaluar.py entregas/clase_12/max clase_12/tests entregas/clase_12/leo/test_estudiante.py
```

## Revisión técnica de PR

Cuando revises el PR asignado:

1. Descarga la rama del compañero.
2. Cambia a esa rama.
3. Ejecuta las pruebas públicas y tus pruebas propias contra su implementación.
4. Pega la salida completa de `pytest -v` en el comentario del PR.
5. Agrega una observación constructiva.

macOS / Linux:

```bash
git fetch origin
git switch nombre-rama-del-compañero
python3 evaluar.py entregas/clase_12/nombre_compañero clase_12/tests entregas/clase_12/mi_nombre/test_estudiante.py
```

Windows PowerShell:

```powershell
git fetch origin
git switch nombre-rama-del-compañero
py evaluar.py entregas/clase_12/nombre_compañero clase_12/tests entregas/clase_12/mi_nombre/test_estudiante.py
```

o:

```powershell
python evaluar.py entregas/clase_12/nombre_compañero clase_12/tests entregas/clase_12/mi_nombre/test_estudiante.py
```

Ejemplo de comentario:

````markdown
Ejecuté pruebas públicas y mis pruebas propias contra esta implementación.

Comando:

```bash
python3 evaluar.py entregas/clase_12/ana clase_12/tests entregas/clase_12/luis/test_estudiante.py
```

Salida:

```text
Pega aquí la salida completa de pytest -v.
```

Observación:

La implementación calcula bien la altura en árboles balanceados. Revisaría el caso degenerado creciente porque mis pruebas muestran una diferencia en `comparaciones_busqueda`.
````

## Problemas relacionados

LeetCode:

- 104 — Maximum Depth of Binary Tree.
- 110 — Balanced Binary Tree.
- 222 — Count Complete Tree Nodes.
- 700 — Search in a Binary Search Tree.
- 701 — Insert into a Binary Search Tree.
- 98 — Validate Binary Search Tree.

CSES:

- Subordinates: https://cses.fi/problemset/task/1674/
- Tree Diameter: https://cses.fi/problemset/task/1131/
- Company Queries I: https://cses.fi/problemset/task/1687/

No los resolveremos todos en esta práctica. Son mapa para práctica futura.

## Checklist

- [ ] Respondí preguntas del notebook en `notebook.md`.
- [ ] Implementé `cantidad_nodos`.
- [ ] Implementé `es_degenerado`.
- [ ] Implementé `comparaciones_busqueda`.
- [ ] Mantuve los métodos de BST de la clase anterior.
- [ ] No implementé eliminación.
- [ ] Escribí al menos 3 pruebas propias.
- [ ] Ejecuté `evaluar.py` con tests públicos.
- [ ] Guardé salida completa en `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Abrí PR.
- [ ] Ejecuté mis pruebas contra el PR asignado.
- [ ] Pegué salida completa de `pytest -v` en el comentario del PR.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| `notebook.md` y análisis conceptual | 20 |
| Implementación de métodos nuevos | 20 |
| Complejidad, altura y balance | 20 |
| Pruebas propias y evaluación con `evaluar.py` | 15 |
| Revisión técnica del PR | 10 |
| `discusion.md` y redacción técnica | 10 |
| GitHub y organización | 5 |

Total: 100 puntos.
