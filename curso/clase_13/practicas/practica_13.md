# Práctica 13: Árboles AVL y revisión técnica profesional

## Contexto

En la Clase 12 descubrimos que un BST correcto puede ser ineficiente si se
degenera. En esta práctica implementaremos una respuesta clásica: árboles AVL.

> [!NOTE]
> Un AVL no cambia lo que significa ser BST. Agrega una regla de balance y usa
> rotaciones para mantener baja la altura.

## Antes de comenzar

Consulta estos recursos:

- [Guía de Markdown](guia_markdown.md)
- [Guía de GitHub](guia_github.md)
- [Guía de revisión de PR](guia_revision_pr.md)

También revisa las secciones internas:

- [Convenciones obligatorias](#convenciones-obligatorias)
- [Checklist del PR](#checklist-del-pr)
- [Checklist del revisor](#checklist-del-revisor)
- [Rúbrica](#rúbrica)

## Objetivos

Al terminar esta práctica podrás:

- calcular factores de balance;
- identificar casos `LL`, `RR`, `LR` y `RL`;
- implementar rotaciones AVL;
- implementar inserción AVL;
- preservar el recorrido inorden después de rotar;
- escribir pruebas propias para rotaciones;
- preparar un Pull Request profesional;
- escribir una revisión técnica útil en Markdown.

## Instrucciones

1. Revisa el notebook.
2. Responde sus preguntas en `notebook.md`.
3. Implementa `NodoAVL` y `ArbolAVL` en `implementacion.py`.
4. Escribe al menos 3 pruebas propias en `test_estudiante.py`.
5. Ejecuta pruebas públicas con `scripts/evaluar.py`.
6. Guarda la salida completa en `reporte_pytest.md`.
7. Escribe `discusion.md`.
8. Abre Pull Request.
9. Revisa el PR asignado.
10. Agrega `revision_nombre.md` dentro de la carpeta de entrega del compañero.

> [!WARNING]
> No modifiques directamente `main`. La práctica evalúa también tu flujo de
> trabajo con rama, commit, PR y revisión.

## Convenciones obligatorias

Nombre de rama:

```text
clase-13-nombre
```

Ejemplo:

```text
clase-13-max
```

Carpeta de entrega:

```text
entregas/max/clase_13/
```

Archivos obligatorios en tu carpeta:

```text
implementacion.py
test_estudiante.py
notebook.md
discusion.md
reporte_pytest.md
```

Archivo obligatorio durante revisión:

```text
entregas/aristeo/clase_13/revision_max.md
```

## `implementacion.py`

Debe definir:

```python
class NodoAVL:
    ...

class ArbolAVL:
    ...
```

Métodos esperados:

```python
def insertar(self, valor: int) -> None: ...
def contiene(self, valor: int) -> bool: ...
def altura(self) -> int: ...
def inorden(self) -> list[int]: ...
def esta_balanceado(self) -> bool: ...
def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL: ...
def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL: ...
```

No implementes eliminación.

> [!IMPORTANT]
> Después de cada inserción debes actualizar alturas antes de decidir si hay que
> rotar. Una rotación con alturas viejas puede parecer correcta en inorden, pero
> fallar en pruebas de balance.

## `test_estudiante.py`

Debes escribir al menos tres pruebas propias.

Deben cubrir al menos:

- una rotación simple (`LL` o `RR`);
- una rotación doble (`LR` o `RL`);
- una propiedad general: inorden ordenado, altura baja, duplicados o búsqueda.

Cada prueba debe tener nombre claro y docstring o comentario breve.

## `notebook.md`

Es un documento de trabajo.

Contiene únicamente respuestas guiadas del notebook, en el mismo orden. No debe
contener código completo.

Estructura sugerida:

```text
# Notebook - Clase 13

## 1. Motivación
## 2. Degeneración
## 3. Altura y balance
## 4. Factor de balance
## 5. Rotaciones
## 6. Casos LL RR LR RL
## 7. Implementación
## 8. Complejidad
## 9. Pruebas
## 10. Revisión técnica
## 11. Discusión
```

## `discusion.md`

Es un documento técnico. No repitas literalmente `notebook.md`.

Debe incluir:

```text
# Discusión técnica

## 1. Problema que resuelve AVL
## 2. Factor de balance
## 3. Rotaciones e invariante BST
## 4. Casos LL RR LR RL
## 5. Complejidad
## 6. Pruebas propias
## 7. Revisión técnica recibida
## 8. Revisión técnica realizada
## 9. Pregunta abierta
```

## `reporte_pytest.md`

Debe contener:

- comando ejecutado;
- salida completa;
- interpretación;
- número de pruebas;
- cuántas pasaron;
- qué comportamiento verifican;
- qué pruebas diseñaste tú;
- qué caso importante todavía falta probar.

## Ejecutar pruebas públicas

Desde la raíz de `curso-alumnos`:

macOS / Linux:

```bash
python3 scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

Windows PowerShell:

```powershell
py scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

o:

```powershell
python scripts/evaluar.py entregas/nombre/clase_13 curso/clase_13/tests
```

## Ejecutar tests extra durante revisión

macOS / Linux:

```bash
git fetch origin
git switch clase-13-nombre-companero
python3 scripts/evaluar.py entregas/nombre_companero/clase_13 curso/clase_13/tests entregas/mi_nombre/clase_13/test_estudiante.py
```

Windows PowerShell:

```powershell
git fetch origin
git switch clase-13-nombre-companero
py scripts/evaluar.py entregas/nombre_companero/clase_13 curso/clase_13/tests entregas/mi_nombre/clase_13/test_estudiante.py
```

## Verificaciones antes del PR

macOS / Linux y Windows PowerShell:

```bash
git branch --show-current
git status
git diff --name-only origin/main
```

Debe ocurrir lo siguiente:

- la rama se llama `clase-13-nombre`;
- `git status` no muestra archivos temporales como `__pycache__` o `.pyc`;
- `git diff --name-only origin/main` muestra únicamente archivos de tu entrega y revisión asignada.

## Commits

Formato:

```text
[TIPO] Descripción
```

Tipos:

| Tipo | Cuándo usarlo | Ejemplo |
| --- | --- | --- |
| `FEAT` | agregas funcionalidad | `[FEAT] Implementar rotación derecha` |
| `FIX` | corriges un error | `[FIX] Actualizar altura después de rotar` |
| `TEST` | agregas o corriges pruebas | `[TEST] Cubrir caso LR` |
| `DOC` | escribes documentación | `[DOC] Completar discusión técnica` |
| `STYLE` | formato sin cambiar comportamiento | `[STYLE] Mejorar nombres de variables` |
| `REFACTOR` | reorganizas código sin cambiar resultado | `[REFACTOR] Separar cálculo de balance` |
| `REVIEW` | agregas revisión de compañero | `[REVIEW] Revisar PR de Ana` |

## Ejemplo de Pull Request

````markdown
# Resumen

Implementé inserción AVL con rotaciones simples y dobles.

## Cambios

- Agregué `NodoAVL` y `ArbolAVL`.
- Implementé `_rotar_izquierda` y `_rotar_derecha`.
- Agregué pruebas propias para casos LL, LR y duplicados.

## Pruebas

```bash
python3 scripts/evaluar.py entregas/max/clase_13 curso/clase_13/tests
```

Pegué la salida completa en `reporte_pytest.md`.

## Dificultades

Me costó distinguir el caso LR del caso LL. Lo resolví revisando el camino de inserción.

## Aspectos que deseo revisión

- Si mis alturas se actualizan en el orden correcto.
- Si mis pruebas propias cubren casos suficientes.

## Checklist

- [x] Mi código compila.
- [x] Pasé pruebas públicas.
- [x] Ejecuté `test_estudiante.py`.
- [x] No hay `__pycache__`.
- [x] No hay `.pyc`.
- [x] No hay archivos fuera de mi entrega.
- [x] La rama tiene el nombre correcto.
````

## Checklist del PR

- [ ] Mi código compila.
- [ ] Pasé pruebas.
- [ ] Ejecuté `test_estudiante.py`.
- [ ] No hay `__pycache__`.
- [ ] No hay `.pyc`.
- [ ] No hay archivos fuera de mi entrega.
- [ ] La rama tiene el nombre correcto.

## Plantilla de revisión

Guarda tu revisión como `revision_nombre_revisor.md` dentro de la carpeta del compañero.

```markdown
# Revisión de PR

## Resumen

## Código

## Pruebas

## Fortalezas

## Mejoras

## Salida completa de pytest

## Conclusión
```

## Checklist del revisor

- [ ] Descargué la rama.
- [ ] Ejecuté pruebas públicas.
- [ ] Ejecuté mis pruebas.
- [ ] Agregué `revision_nombre.md`.
- [ ] Pegué salida completa de pytest.
- [ ] Hice comentarios útiles.

## Escritura técnica

Observación mala:

> Está mal.

Observación buena:

> En el caso LR, el recorrido inorden se conserva, pero la raíz local esperada
> debería ser 20. Sugiero revisar el orden: primero rotación izquierda sobre el
> hijo izquierdo y después rotación derecha sobre el nodo desbalanceado.

> [!TIP]
> Una buena observación explica evidencia, impacto y una posible ruta de corrección.

## Problemas relacionados

LeetCode:

- 110 — Balanced Binary Tree.
- 98 — Validate Binary Search Tree.
- 701 — Insert into a Binary Search Tree.
- 1382 — Balance a Binary Search Tree.
- 104 — Maximum Depth of Binary Tree.

CSES:

- Subordinates.
- Company Queries I.
- Tree Diameter.

## Checklist de entrega

- [ ] Respondí el notebook en `notebook.md`.
- [ ] Implementé `NodoAVL`.
- [ ] Implementé `ArbolAVL`.
- [ ] Implementé rotación izquierda.
- [ ] Implementé rotación derecha.
- [ ] Cubrí `LL`, `RR`, `LR` y `RL`.
- [ ] Escribí al menos 3 pruebas propias.
- [ ] Ejecuté pruebas públicas.
- [ ] Guardé salida completa en `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Abrí PR.
- [ ] Revisé un PR de compañero.
- [ ] Agregué `revision_nombre.md`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| Implementación AVL | 25 |
| Rotaciones y actualización de alturas | 20 |
| Pruebas propias | 15 |
| `notebook.md` | 10 |
| `discusion.md` | 10 |
| Revisión técnica | 10 |
| Documentación y Markdown | 5 |
| Uso correcto de GitHub | 5 |
| **Total** | **100** |

> [!CAUTION]
> Una solución que pasa inorden pero no actualiza alturas correctamente puede fallar
> en pruebas privadas de balance.
